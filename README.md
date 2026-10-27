# claude-job-monitor

Weekly scheduled monitor for robotics PhD research internship openings.

- `openings.csv` — every opening seen so far (`first_seen` = date first recorded). Each weekly run compares new search results against this file and only notifies about rows not already present (matched by URL / company+title).
- `checked.md` — companies checked with no relevant opening, plus run log.
- `manual_notes.md` — dated manual notes from the user; read before each run and act on them.
