# Check run of the v1.0 search code (2026-10-16)

Before registration: does the code run on every source, how many records reach screening, and does it find the seed set?

- `search_log.json` — query strings, record counts and times per source. The sources were run in three passes on the same day: all sources; then Crossref, instrument citations and CORE after two fixes (Crossref `select` field; CORE early stop); then PubMed, Europe PMC, OpenAlex, Semantic Scholar and DataCite after the "usage" forms and the companion query were added.
- `dedup_report.json` — 11,374 records, 5,258 unique, 203 removed automatically, 5,055 to screen.
- `recall_seed_set.json` — 35 of the 37 studies of Dagnino et al. (2026). The two misses have no quantitative dependence measure (protocol §10).
- Raw exports, `records_unique.jsonl` and `screening.csv` are not committed (git-ignored): the final search is run again after registration.
