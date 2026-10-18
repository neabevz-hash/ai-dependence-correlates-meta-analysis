"""AI draft labels for title/abstract screening (protocol, section 11b): two independent passes.

Reads the fixed prompt and schema from llm_screener_prompt.md and the records from
search/runs/<run>/screening.csv, and appends one JSON line per record to screening/llm/<run>_<pass>.jsonl
(resumable). Passes: opus = Claude Opus 5.5, sonnet = Claude Sonnet 5.5, same prompt, same seeded order.
When every record has a label, <file>.sha256 is written: its hash is committed before R1's calibration is unblinded.
Template: papers/misophonia-prevalence/screening/llm_screen.py.

Run:
  .venv/Scripts/python.exe papers/ai-dependence-correlates/screening/llm_screen.py --run 2026-10-17 --pass opus
  .venv/Scripts/python.exe papers/ai-dependence-correlates/screening/llm_screen.py --run 2026-10-17 --pass sonnet
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "harness"))

from llmaudit.judge import Judge, judge_all, utcnow  # noqa: E402

SEED = 20261017
PASSES = {"opus": "claude-opus-5-5", "sonnet": "claude-sonnet-5-5"}


def load_prompt() -> tuple[str, dict]:
    md = (HERE / "llm_screener_prompt.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```(\w*)\n(.*?)```", md, re.S)
    system = next(body for lang, body in blocks if lang == "" and body.startswith("You are screening"))
    schema = json.loads(next(body for lang, body in blocks if lang == "json"))
    return system.strip(), schema


def render(item: dict) -> str:
    abstract = item["abstract"].strip() or "[no abstract available]"
    return (f"Record {item['k']} of the screening set.\n"
            f"Title: {item['title']}\n"
            f"Year: {item['year']}\n"
            f"Source/venue: {item['venue']}\n"
            f"Record type(s): {item['types_plain']}\n"
            f"Abstract: {abstract}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--pass", dest="pass_", choices=list(PASSES), required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--effort", default="high")
    a = ap.parse_args()
    system, schema = load_prompt()
    rows = list(csv.DictReader((ROOT / "papers/ai-dependence-correlates/search/runs" / a.run / "screening.csv").open(encoding="utf-8-sig")))
    items = []
    for k, r in enumerate(rows, 1):
        types_plain = "; ".join(sorted({t.split(":", 1)[1] for t in r["types"].split(" | ") if ":" in t and t.split(":", 1)[1]}))
        items.append({"conv_id": r["rec_id"], "k": k, "title": r["title"], "year": r["year"], "venue": r["venue"],
                      "types_plain": types_plain, "abstract": r["abstract"]})
    judge = Judge(system_prompt=system, schema=schema, model=PASSES[a.pass_], effort=a.effort, timeout=600)
    out = HERE / "llm" / f"{a.run}_{a.pass_}.jsonl"
    out.parent.mkdir(exist_ok=True)
    asyncio.run(judge_all(items, render, judge, out, concurrency=a.concurrency, seed=SEED, limit=a.limit))
    done = {json.loads(line)["conv_id"] for line in out.open(encoding="utf-8") if line.strip()} if out.exists() else set()
    if a.limit is None and done == {it["conv_id"] for it in items}:
        digest = hashlib.sha256(out.read_bytes()).hexdigest()
        (out.parent / (out.name + ".sha256")).write_text(
            json.dumps({"file": out.name, "sha256": digest, "records": len(done), "written_at_utc": utcnow(),
                        "model": PASSES[a.pass_], "system_prompt_sha": judge.fingerprint()["system_prompt_sha"]}, indent=2) + "\n",
            encoding="utf-8")
        print(f"all {len(done)} records labelled; sha256 {digest}")


if __name__ == "__main__":
    main()
