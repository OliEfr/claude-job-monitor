#!/usr/bin/env python3
"""Archive job description pages for every opening in openings.csv.

For each URL in openings.csv that has no captured description yet (per
postings/index.csv), this script:
  1. downloads the raw page HTML  -> postings/<slug>.html
  2. extracts the job description -> postings/<slug>.md
  3. records the attempt          -> postings/index.csv

Description extraction, in order of preference:
  - public ATS APIs (Greenhouse, Lever, Ashby) / known static mirrors (MERL)
  - schema.org JobPosting JSON-LD embedded in the HTML (Workday, Lever, ...)
  - visible text of the HTML (scripts/styles/nav removed)

Pages that only render in a logged-in browser or block plain HTTP clients
(metacareers.com, tesla.com) are recorded with status "unavailable" and
retried on the next run. Stdlib only; no browser needed.

Usage: python3 fetch_postings.py [--retry-all]
"""
import csv
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
OPENINGS = os.path.join(ROOT, "openings.csv")
OUT = os.path.join(ROOT, "postings")
INDEX = os.path.join(OUT, "index.csv")
INDEX_FIELDS = ["url", "company", "title", "slug", "fetched_at", "http_status",
                "description_source", "description_chars", "status"]
UA = "Mozilla/5.0 (X11; Linux x86_64) claude-job-monitor archiver"
MIN_DESC_CHARS = 400  # below this, treat as "no real description captured"


def get(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except Exception as e:  # network error, timeout, ...
        return 0, str(e)


class _Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "nav", "header", "footer", "head", "form"}
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "section", "ul", "ol"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in self.BLOCK:
            self.out.append("\n- " if tag == "li" else "\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def html_to_text(s):
    p = _Text()
    p.feed(s)
    text = "".join(p.out)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n\s*(\n\s*)+", "\n\n", text)
    return "\n".join(line.strip() for line in text.splitlines()).strip()


def jsonld_description(page):
    for m in re.finditer(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', page, re.S | re.I):
        try:
            data = json.loads(m.group(1).strip())
        except ValueError:
            continue
        for d in data if isinstance(data, list) else data.get("@graph", [data]):
            if isinstance(d, dict) and d.get("@type") == "JobPosting" and d.get("description"):
                parts = [html_to_text(html.unescape(d["description"]))]
                # Some sites (e.g. Meta) put most of the posting in these extra fields.
                for key in ("responsibilities", "qualifications", "skills", "educationRequirements",
                            "experienceRequirements", "baseSalary", "datePosted", "validThrough"):
                    v = d.get(key)
                    if v:
                        v = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
                        parts.append(f"## {key}\n\n{html_to_text(html.unescape(v))}")
                return "\n\n".join(parts)
    return ""


def api_description(url):
    """Description from a public ATS API or static mirror, or ''."""
    m = re.match(r"https://(?:job-boards|boards)\.greenhouse\.io/([^/]+)/jobs/(\d+)", url)
    if m:
        st, body = get(f"https://boards-api.greenhouse.io/v1/boards/{m[1]}/jobs/{m[2]}")
        if st == 200:
            return "greenhouse-api", html_to_text(html.unescape(json.loads(body).get("content", "")))
    m = re.match(r"https://jobs\.lever\.co/([^/]+)/([0-9a-f-]{36})", url)
    if m:
        st, body = get(f"https://api.lever.co/v0/postings/{m[1]}/{m[2]}")
        if st == 200:
            d = json.loads(body)
            parts = [d.get("descriptionPlain", "")]
            for l in d.get("lists", []):
                parts.append(l.get("text", "") + "\n" + html_to_text(l.get("content", "")))
            parts.append(d.get("additionalPlain", ""))
            return "lever-api", "\n\n".join(p for p in parts if p).strip()
    m = re.match(r"https://jobs\.ashbyhq\.com/([^/]+)/([0-9a-f-]{36})", url)
    if m:
        st, body = get(f"https://api.ashbyhq.com/posting-api/job-board/{m[1]}")
        if st == 200:
            for j in json.loads(body).get("jobs", []):
                if m[2] in (j.get("id", ""), j.get("jobUrl", "")) or j.get("jobUrl", "").endswith(m[2]):
                    return "ashby-api", j.get("descriptionPlain") or html_to_text(j.get("descriptionHtml", ""))
    if "merl.clearcompany.com" in url:
        return "merl.com/internship/openings", ""  # filled in by merl_description()
    return "", ""


_merl_cache = None


def merl_description(title):
    """MERL's ClearCompany pages are JS-only; merl.com mirrors them as static HTML keyed by code."""
    global _merl_cache
    code = re.search(r"\(([A-Z]{2}\d{4})\)", title)
    if not code:
        return ""
    if _merl_cache is None:
        _merl_cache = get("https://www.merl.com/internship/openings")[1]
    m = re.search(rf'<h2 id="{code[1]}">(.*?)(?=<h2 id="[A-Z]{{2}}\d{{4}}"|</section>)', _merl_cache, re.S)
    return html_to_text(m.group(1)) if m else ""


def slugify(s, n=60):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n].strip("-")


def main():
    retry_all = "--retry-all" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    index = {}
    if os.path.exists(INDEX):
        with open(INDEX, newline="") as f:
            index = {r["url"]: r for r in csv.DictReader(f)}
    with open(OPENINGS, newline="") as f:
        openings = list(csv.DictReader(f))

    for row in openings:
        url = row["url"].strip()
        prev = index.get(url)
        if prev and prev["status"] == "ok" and not retry_all:
            continue
        slug = prev["slug"] if prev else (
            f"{slugify(row['company'].split('(')[0], 25)}_{slugify(row['title'])}_"
            f"{hashlib.sha1(url.encode()).hexdigest()[:6]}")
        now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        status, page = get(url)
        if status == 200:
            with open(os.path.join(OUT, slug + ".html"), "w") as f:
                f.write(page)

        source, desc = api_description(url)
        if source.startswith("merl"):
            desc = merl_description(row["title"])
        from_api = source.endswith("-api") and desc.strip() != ""
        if len(desc) < MIN_DESC_CHARS and status == 200 and not from_api:
            ld = jsonld_description(page)
            if len(ld) > len(desc):
                source, desc = "json-ld", ld
        if len(desc) < MIN_DESC_CHARS and status == 200 and not from_api:
            txt = html_to_text(page)
            if len(txt) > len(desc):
                source, desc = "html-text", txt

        # ATS APIs are authoritative even for very short postings; scraped text needs a minimum length.
        ok = len(desc) >= MIN_DESC_CHARS or from_api
        if ok:
            with open(os.path.join(OUT, slug + ".md"), "w") as f:
                f.write(f"# {row['title']}\n\n"
                        f"- Company: {row['company']}\n- Location: {row['location']}\n"
                        f"- URL: {url}\n- First seen: {row['first_seen']}\n"
                        f"- Fetched: {now}\n- Description source: {source}\n\n---\n\n{desc}\n")
        index[url] = {"url": url, "company": row["company"], "title": row["title"], "slug": slug,
                      "fetched_at": now, "http_status": status, "description_source": source if ok else "",
                      "description_chars": len(desc) if ok else 0,
                      "status": "ok" if ok else ("gone" if status in (404, 410) else "unavailable")}
        print(f"{index[url]['status']:<11} {status:>3} {source or '-':<28} {slug}")

    with open(INDEX, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=INDEX_FIELDS)
        w.writeheader()
        w.writerows(index.values())


if __name__ == "__main__":
    main()
