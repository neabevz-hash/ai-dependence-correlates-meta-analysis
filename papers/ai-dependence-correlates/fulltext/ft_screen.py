"""AI full-text proposals (protocol, section 11b): Claude Opus 5.5 drafts a decision for every retrieved full text.
Template: papers/misophonia-prevalence/fulltext/ft_screen.py (unchanged logic).

Reads the fixed prompt and schema from ft_prompt.md, the retrieved reports from retrieval_log.csv and their texts
from fulltext/text/<rec_id>.txt, and appends one JSON line per report to fulltext/llm/<name>.jsonl (resumable).
The proposals are drafts; R1 decides every report.

Run (pilot):  .venv/Scripts/python.exe papers/ai-dependence-correlates/fulltext/ft_screen.py --run 2026-10-16 --name pilot --only R.... (five reports)
Run (all):    .venv/Scripts/python.exe papers/ai-dependence-correlates/fulltext/ft_screen.py --run 2026-10-16 --name ft_2026-10-16
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))

from llmaudit.judge import Judge, judge_all  # noqa: E402

SEED = 20261019
MAX_CHARS = 400_000   # about 110k tokens; longer texts (some theses) are cut and the prompt says so


def load_prompt() -> tuple[str, dict, str]:
    md = (HERE / "ft_prompt.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```(\w*)\n(.*?)```", md, re.S)
    system = next(body for lang, body in blocks if lang == "" and body.startswith("You are assessing"))
    schema = json.loads(next(body for lang, body in blocks if lang == "json"))
    user = next(body for lang, body in blocks if lang == "" and body.startswith("Report {k}"))
    return system.strip(), schema, user


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only", nargs="*", help="rec_ids to process (e.g., the pilot set)")
    ap.add_argument("--concurrency", type=int, default=3)
    a = ap.parse_args()
    system, schema, user_tpl = load_prompt()
    recs = {}
    for line in (PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8"):
        u = json.loads(line)
        recs[u["rec_id"]] = u
    log = [r for r in csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig")) if r["status"] == "retrieved"]
    items = []
    for k, r in enumerate(sorted(log, key=lambda x: x["rec_id"]), 1):
        if a.only and r["rec_id"] not in a.only:
            continue
        raw = (HERE / "text" / f"{r['rec_id']}.txt").read_text(encoding="utf-8")
        text = raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw
        u = recs[r["rec_id"]]
        items.append({"conv_id": r["rec_id"], "k": k, "title": u["title"], "year": u["year"], "venue": u["venue"],
                      "source": r["source"], "chars": len(text),
                      "truncated": f"; cut to the first {MAX_CHARS:,} characters" if len(text) > MAX_CHARS else "",
                      "text": text[:MAX_CHARS]})

    def render(it: dict) -> str:
        return user_tpl.format(**{k: it[k] for k in ("k", "title", "year", "venue", "source", "truncated", "text")},
                               chars=f"{it['chars']:,}")

    judge = Judge(system_prompt=system, schema=schema, model="claude-opus-5-5", effort="high", timeout=900)
    out = HERE / "llm" / f"{a.name}.jsonl"
    asyncio.run(judge_all(items, render, judge, out, concurrency=a.concurrency, seed=SEED, limit=a.limit))


if __name__ == "__main__":
    main()
