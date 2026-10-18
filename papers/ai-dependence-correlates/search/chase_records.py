"""Records for full-text assessment from the citation search (protocol §9; deviations.md, D2).

citation_chase.py found the works citing or cited by the included reports and the protocol's reviews that the main
search had not found. Those with the exposure concept in the title or abstract (mentions_term) go straight to full-text
assessment, as in the misophonia review. This script gives them record IDs R6001, R6002, ... (in OpenAlex ID order; the
main run ends below R6000) in the record format of the main search and writes records_unique.jsonl in the same run
folder, so that fetch_oa.py, ft_screen.py and ft_md.py process them like the main records.
Template: papers/misophonia-prevalence/search/chase_records.py.

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/search/chase_records.py --run 2026-10-17-citations
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIRST_ID = 6001


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.run
    hits = [r for r in (json.loads(l) for l in (run / "records_new.jsonl").open(encoding="utf-8")) if r.get("mentions_term")]
    hits.sort(key=lambda r: r["source_id"])
    out = []
    for i, h in enumerate(hits):
        out.append({
            "rec_id": f"R{FIRST_ID + i}", "title": h["title"], "abstract": h.get("abstract", ""), "year": h.get("year"),
            "first_author": h.get("first_author", ""), "venue": h.get("venue", ""), "doi": h.get("doi", ""),
            "all_dois": h.get("doi", ""), "pmid": h.get("pmid", ""), "types": f"openalex:{h.get('type', '')}",
            "language": h.get("language", ""), "sources": h["source"], "n_sources": 1,
            "source_ids": h["source_id"], "url": f"https://doi.org/{h['doi']}" if h.get("doi") else
            f"https://openalex.org/{h['source_id']}", "chase": h["source"],
        })
    with (run / "records_unique.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(out)} records: {out[0]['rec_id']}..{out[-1]['rec_id']} -> {run / 'records_unique.jsonl'}")


if __name__ == "__main__":
    main()
