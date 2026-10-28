# claude-job-monitor

Weekly scheduled monitor for robotics PhD research internship openings.

- `openings.csv` — every opening seen so far (`first_seen` = date first recorded). Each weekly run compares new search results against this file and only notifies about rows not already present (matched by URL / company+title).
- `checked.md` — companies checked with no relevant opening, plus run log.
- `manual_notes.md` — dated manual notes from the user; read before each run and act on them.
- `postings/` — long-term archive of job descriptions, one snapshot per opening: `<slug>.html` (raw page as fetched) and `<slug>.md` (extracted description text for analysis). `postings/index.csv` maps each URL to its files and fetch status (`ok` / `gone` = 404 / `unavailable` = blocked or JS-only, retried next run).
- `fetch_postings.py` — fills `postings/` for every row in `openings.csv` not yet archived. Stdlib Python, no browser needed. **After adding new rows to `openings.csv`, run `python3 fetch_postings.py` and commit `postings/` together with the CSV.**
