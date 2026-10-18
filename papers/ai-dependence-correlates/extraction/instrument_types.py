"""Draft the type of every AI-dependence instrument family (protocol §13): T1 addiction-type, T2 functional dependence,
T3 emotional dependence, T4 mixed or unclear; for the total score and for each subscale.

Input: extraction/instrument_mentions.csv (instrument_families.py) and, where the included reports print too few items,
the development paper in extraction/devpapers/<family>.txt. One Claude Opus 5.5 call per family (headless Claude Code).
Output: extraction/llm/<name>.jsonl. The drafts go to R1 in extraction/instrument_types_R1.md (instrument_types_md.py);
R1 decides every type before effect sizes are extracted.

Run: .venv/Scripts/python.exe papers/ai-dependence-correlates/extraction/instrument_types.py --name types_2026-10-17
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "harness"))
from llmaudit.judge import Judge, judge_all  # noqa: E402

SEED = 20261021
DEV_CHARS = 60_000

SYSTEM = """You type an instrument that measures dependence on AI, for a meta-analysis (protocol: type is decided by ITEM CONTENT, not by the scale's name).

Types:
- T1 addiction-type: items operationalise behavioural-addiction components — salience or preoccupation, mood modification, tolerance, withdrawal, conflict or negative consequences, relapse or loss of control, compulsive use (Griffiths, 2005; Bergen and Internet Addiction Test adaptations; DSM-5 Internet Gaming Disorder criteria).
- T2 functional dependence: items ask about relying on AI to perform tasks or to think (studying, writing, deciding, problem solving), difficulty working or thinking without AI, delegating cognition, over-reliance.
- T3 emotional dependence: items ask about relying on AI for emotional support, comfort or companionship, an attachment-like bond, distress at separation from the AI as a relationship partner.
- T4 mixed or unclear: a total score whose items span more than one type, or no item text and no subscale content to judge from.

Rules:
- Type the TOTAL score and EACH subscale separately. A subscale named after an addiction component (e.g., withdrawal, salience) is T1 even when only its name is known; say that the evidence is the subscale name.
- When most items of a total score are of one type and one or two are of another, give the majority type and say so; when no type has a clear majority, T4.
- Quote two or three items (verbatim, any language) that decide the type. Never invent items.
- evidence: "items" (you read item texts), "subscale_names" (only names or definitions of subscales), or "none".

Return only JSON matching the schema."""

SCHEMA = {
    "type": "object",
    "properties": {
        "total_type": {"type": "string", "enum": ["T1", "T2", "T3", "T4"]},
        "total_rationale": {"type": "string", "maxLength": 500},
        "subscales": {"type": "array", "maxItems": 10, "items": {
            "type": "object",
            "properties": {"name": {"type": "string", "maxLength": 120},
                           "type": {"type": "string", "enum": ["T1", "T2", "T3", "T4"]},
                           "rationale": {"type": "string", "maxLength": 300}},
            "required": ["name", "type", "rationale"], "additionalProperties": False}},
        "evidence": {"type": "string", "enum": ["items", "subscale_names", "none"]},
        "quoted_items": {"type": "array", "maxItems": 4, "items": {"type": "string", "maxLength": 300}},
        "note": {"type": "string", "maxLength": 300},
    },
    "required": ["total_type", "total_rationale", "subscales", "evidence", "quoted_items", "note"],
    "additionalProperties": False,
}


def families() -> dict[str, list[dict]]:
    fam = defaultdict(list)
    for r in csv.DictReader((HERE / "instrument_mentions.csv").open(encoding="utf-8")):
        fam[r["family"]].append(r)
    return fam


def render(it: dict) -> str:
    return it["prompt"]


def build_items() -> list[dict]:
    items = []
    for k, (fid, ms) in enumerate(sorted(families().items()), 1):
        names = sorted({m["name"] for m in ms})
        cites = sorted({m["source_citation"] for m in ms})[:4]
        subs = sorted({m["subscales"] for m in ms if m["subscales"]})[:4]
        item_text = []
        for m in sorted(ms, key=lambda m: -int(m["n_items_printed"])):
            for x in (m["items"].split(" || ") if m["items"] else []):
                if x and x not in item_text:
                    item_text.append(x)
        dev = HERE / "devpapers" / f"{fid}.txt"
        dev_text = dev.read_text(encoding="utf-8")[:DEV_CHARS] if dev.exists() else ""
        prompt = (f"Instrument family {fid} (used in {len(ms)} included report(s): {', '.join(m['rec_id'] for m in ms)}).\n"
                  f"Names: {' | '.join(names)}\nSource citations: {' | '.join(cites)}\n"
                  f"Declared items: {' | '.join(sorted({m['n_items'] for m in ms}))}\n"
                  f"Subscales as reported: {' | '.join(subs) or 'none reported'}\n"
                  f"Adapted from: {' | '.join(sorted({m['adapted_from'] for m in ms if m['adapted_from']})) or 'not stated'}\n"
                  f"Item texts printed in the included reports ({len(item_text)}):\n" + "\n".join(f"- {x}" for x in item_text[:40])
                  + (f"\n\nDevelopment paper (first {DEV_CHARS:,} characters):\n{dev_text}" if dev_text else "\n\nDevelopment paper: not available."))
        items.append({"conv_id": fid, "k": k, "prompt": prompt})
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    items = [it for it in build_items() if not a.only or it["conv_id"] in a.only]
    judge = Judge(system_prompt=SYSTEM, schema=SCHEMA, model="claude-opus-5-5", effort="high", timeout=600)
    out = HERE / "llm" / f"{a.name}.jsonl"
    asyncio.run(judge_all(items, render, judge, out, concurrency=a.concurrency, seed=SEED))


if __name__ == "__main__":
    main()
