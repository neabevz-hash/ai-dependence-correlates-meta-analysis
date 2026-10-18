"""Are the AI's quotes in the source? An automatic audit of the extraction drafts.

For every effect and every key sample field (n_analysed, population, sampling, ai_system) of the drafts, the quote is
searched in the full texts of the job (main and attached reports) after normalisation: case, whitespace, punctuation
and hyphenation are ignored, an ellipsis ("...", "…") splits a quote into fragments that must all be found, and
English translations in square brackets are removed (brackets with words, not confidence intervals). A quote counts as found when every fragment of at least 10
characters occurs in the text. Table rows ("label | .31** | .12") are matched cell by cell, in the quoted order, each cell within 60 characters of
the one before. Writes
extraction/decisions/quote_check.json and lists quotes not found.
Template: papers/misophonia-prevalence/extraction/quote_check.py (same rules; effects instead of estimates).

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/quote_check.py --draft extract_<date>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
KEY_FIELDS = ("n_analysed", "population", "sampling", "ai_system")


def norm(t: str) -> str:
    """Letters and digits only: spacing, punctuation, line-end hyphens and PDF spacing between characters vanish."""
    t = unicodedata.normalize("NFKC", t or "").lower()
    return re.sub(r"[\W_]+", "", t)


TRANSLATION = re.compile(r"\[[^\]]*[^\W\d_]{3}[^\]]*\]")   # "[English translation]", not "[0.66, 0.74]"


def fragments(q: str) -> list[str]:
    q = re.sub(TRANSLATION, " ", q)          # translations in brackets
    parts = re.split(r"\.\.\.|…|\s\|\s|\|", q)
    return [norm(p) for p in parts if len(norm(p)) >= 10]


def row_found(q: str, hay: str) -> bool | None:
    """A table-row quote ("label | .31** | .12"): the cells in the quoted order, each within 60 characters (after
    normalisation) of the end of the one before. None if the quote is not a table row."""
    if "|" not in q:
        return None
    cells = [norm(c) for c in re.split(r"\||\.\.\.|…", re.sub(TRANSLATION, " ", q))]
    cells = [c for c in cells if c]
    if len(cells) < 2:
        return None
    start = 0
    for _ in range(5000):
        pos = hay.find(cells[0], start)
        if pos < 0:
            return False
        cur, ok = pos + len(cells[0]), True
        for c in cells[1:]:
            k = hay.find(c, cur, cur + 60 + len(c))
            if k < 0:
                ok = False
                break
            cur = k + len(c)
        if ok:
            return True
        start = pos + 1
    return False


def text_of(rec: str) -> str:
    p = PAPER / "fulltext" / "text" / f"{rec}.txt"
    return norm(p.read_text(encoding="utf-8", errors="replace")) if p.exists() else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    ap.add_argument("--out", help="output file (default extraction/decisions/quote_check.json)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    jobs = {j["job_id"]: j for j in json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))}
    cache: dict[str, str] = {}
    stats = {"effects": [0, 0, 0], "key_fields": [0, 0, 0]}   # quotes checked, found, not checkable (too short)
    missing = []
    for line in (HERE / "draft" / f"{a.draft}.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        j = jobs[d["conv_id"]]
        recs = [j["main"], *j["attached"], *j["listed_only"]]
        for r in recs:
            cache.setdefault(r, text_of(r))
        hay = " ".join(cache[r] for r in recs)
        for s in d["codes"]["samples"]:
            items = [("effects", f"E{i}", e["quote"]) for i, e in enumerate(s["effects"], 1)]
            items += [("key_fields", f, s[f]["quote"]) for f in KEY_FIELDS]
            for kind, what, q0 in items:
                q = re.sub(r"\bR\d{4}\s*[:,]\s*", " ", q0 or "")   # "R2687: ..." names the attached report
                q = re.sub(r"\((?:columns?|rows?)\b[^)]*\)", " ", q, flags=re.I)   # the AI's own column legend
                lost = []   # a quote may join a table row and a sentence: "... | .41** ; text: ... (r = .415)"
                checkable = False
                for part in re.split(r";\s*text\s*:", q, flags=re.I):
                    row = row_found(part, hay)
                    if row is not None:
                        checkable = True
                        if not row:
                            lost.append("table row: cells not found together")
                        continue
                    fr = fragments(part)
                    checkable = checkable or bool(fr)
                    lost += [f for f in fr if f not in hay]
                if not checkable:
                    stats[kind][2] += 1
                    continue
                stats[kind][0] += 1
                if not lost:
                    stats[kind][1] += 1
                else:
                    missing.append({"job": d["conv_id"], "sample": s["label"][:80], "item": what, "quote": (q0 or "")[:300],
                                    "not_found": lost[0][:160]})
    out = {k: {"quotes_checked": v[0], "found_verbatim": v[1], "too_short_to_check": v[2],
               "share_found": round(v[1] / v[0], 4) if v[0] else None} for k, v in stats.items()}
    out["not_found"] = missing
    path = Path(a.out) if a.out else HERE / "decisions" / "quote_check.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in out.items() if k != "not_found"}, indent=1))
    print(f"not found: {len(missing)}")
    for m in missing[:40]:
        print(f"  {m['job']} {m['item']} | {m['not_found']}")


if __name__ == "__main__":
    main()
