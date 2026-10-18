"""R1's decision file for the instrument types (protocol §13) and its parser.

  make  --name types_2026-10-17   writes extraction/decisions/instrument_types_R1.md (one block per instrument family:
                                  names, reports, items, AI draft for the total score and each subscale)
  parse --out CSV                 reads R1's decisions -> extraction/instruments.csv (family, part, type, source)

Decision line, one per family:
  =                          agree with the AI draft (total and all subscales)
  T1 / T2 / T3 / T4          the total score's type; subscales as drafted
  T4; Instrumental=T2; ...   the total's type, then subscale overrides by the subscale name as shown
  ?                          not decided yet
Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/instrument_types_md.py make --name types_2026-10-17
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "decisions" / "instrument_types_R1.md"
TYPE_RU = {"T1": "аддиктивная", "T2": "функциональная", "T3": "эмоциональная", "T4": "смешанная или неясно"}
HEADER_RE = re.compile(r"^###\s+(\d+)\s*·\s*([A-Z0-9_]+)\s*$")
DECISION_RE = re.compile(r"^\*\*Решение:\*\*\s*(.*)$")

GUIDE = """# Типы шкал зависимости от ИИ (протокол §13)

Тип определяется по **содержанию пунктов**, а не по названию шкалы. Решаете вы; черновик ИИ — над строкой решения.

| Тип | Пункты про… |
| --- | --- |
| T1 аддиктивная | компоненты поведенческой зависимости: поглощённость, изменение настроения, толерантность, абстиненция, конфликт или негативные последствия, потеря контроля, рецидив |
| T2 функциональная | опору на ИИ в задачах и мышлении: учёба, письмо, решения; трудно работать или думать без ИИ |
| T3 эмоциональная | эмоциональную опору: поддержка, утешение, компания, привязанность, тоска без ИИ как без близкого |
| T4 смешанная или неясно | сумма пунктов разных типов без явного большинства; или пунктов нет и судить не по чему |

**Строка решения:**
- `=` — согласен с черновиком (и для суммы, и для подшкал);
- `T1`…`T4` — свой тип суммы, подшкалы как в черновике;
- `T4; Instrumental Dependency=T2; Relationship Dependency=T3` — сумма и подшкалы (имя подшкалы как в черновике);
- `?` — пока не решил.

Почему это важно: главный модератор — тип шкалы; в сравнение T1/T2/T3 идут только шкалы и подшкалы, которым вы дали тип T1–T3, а T4 показываются отдельно.
"""


def mentions() -> dict[str, list[dict]]:
    fam = defaultdict(list)
    for r in csv.DictReader((HERE / "instrument_mentions.csv").open(encoding="utf-8")):
        fam[r["family"]].append(r)
    return fam


def one(t: str) -> str:
    return re.sub(r"\s+", " ", t or "").strip()


def all_drafts() -> dict[str, dict]:
    """Type drafts of every run (types_<date>.jsonl; later runs add families, D9)."""
    out = {}
    for f in sorted((HERE / "llm").glob("types_*.jsonl")):
        out.update({json.loads(l)["conv_id"]: json.loads(l)["codes"] for l in f.open(encoding="utf-8") if l.strip()})
    return out


def make(a) -> None:
    fam = mentions()
    drafts = {json.loads(l)["conv_id"]: json.loads(l)["codes"] for l in (HERE / "llm" / f"{a.name}.jsonl").open(encoding="utf-8")}
    out_path = Path(a.out) if a.out else OUT
    order = sorted((f for f in fam if f in drafts), key=lambda f: (f.startswith("ADHOC_"), -len(fam[f]), f))
    blocks = []
    for n, fid in enumerate(order, 1):
        ms, d = fam[fid], drafts[fid]
        items = []
        for m in sorted(ms, key=lambda m: -int(m["n_items_printed"])):
            for x in (m["items"].split(" || ") if m["items"] else []):
                if x and x not in items:
                    items.append(x)
        lines = ["---", "", f"### {n} · {fid}", "",
                 f"**{one(ms[0]['name'])}**" + (f" (и ещё {len({m['name'] for m in ms}) - 1} вариантов названия)" if len({m['name'] for m in ms}) > 1 else ""), "",
                 f"- Отчёты ({len(ms)}): {', '.join(m['rec_id'] for m in ms)}",
                 f"- Источник: {one(ms[0]['source_citation'])[:250]}",
                 f"- Пунктов: {' / '.join(sorted({one(m['n_items']) for m in ms}))}; подшкалы: {one(max((m['subscales'] for m in ms), key=len))[:300] or 'нет'}"]
        if items:
            lines.append(f"- Пункты ({len(items)}" + (", показаны первые 15" if len(items) > 15 else "") + "):")
            lines += [f"  - {one(x)}" for x in items[:15]]
        else:
            lines.append("- Пунктов нет ни в одном отчёте" + (" (статья-разработка прочитана)" if (HERE / "devpapers" / f"{fid}.txt").exists() else ""))
        lines += ["", f"**ИИ:** сумма {d['total_type']} ({TYPE_RU[d['total_type']]}) · основание: {d['evidence']} · {one(d['total_rationale'])}"]
        for s in d["subscales"]:
            lines.append(f"- подшкала «{one(s['name'])}»: {s['type']} — {one(s['rationale'])}")
        if d["quoted_items"]:
            lines.append("- Решающие пункты: " + " | ".join(f"«{one(q)}»" for q in d["quoted_items"]))
        lines += ["", "**Решение:** ", ""]
        blocks.append("\n".join(lines))
    out_path.parent.mkdir(exist_ok=True)
    if out_path.exists() and not a.force:
        sys.exit(f"{out_path} exists; refusing to overwrite R1's work")
    out_path.write_text(GUIDE + "\n" + "\n".join(blocks), encoding="utf-8", newline="\n")
    print(f"{out_path}  ({len(blocks)} instrument families)")


def parse(a) -> None:
    drafts = all_drafts()
    rows, problems, cur = [], [], None
    lines = [l for f in sorted(OUT.parent.glob("instrument_types_R1*.md")) for l in f.read_text(encoding="utf-8").splitlines()]
    for line in lines:
        h = HEADER_RE.match(line.strip())
        if h:
            cur = h.group(2)
            continue
        d = DECISION_RE.match(line.strip())
        if d and cur:
            raw = d.group(1).strip()
            draft = drafts[cur]
            subs = {s["name"]: s["type"] for s in draft["subscales"]}
            if not raw or raw.startswith("?"):
                problems.append(f"{cur}: {'undecided' if raw else 'no decision'}")
                cur = None
                continue
            if raw.startswith("="):
                total, src = draft["total_type"], "agree"
            else:
                parts = [p.strip() for p in raw.split(";") if p.strip()]
                m = re.fullmatch(r"T[1-4]", parts[0].split()[0]) if parts else None
                if not m:
                    problems.append(f"{cur}: cannot read {raw!r}")
                    cur = None
                    continue
                total, src = m.group(0), "R1"
                for p in parts[1:]:
                    k, _, v = p.partition("=")
                    k, v = k.strip(), v.strip()
                    match = next((s for s in subs if s.lower().startswith(k.lower()) or k.lower() in s.lower()), None)
                    if match and re.fullmatch(r"T[1-4]", v):
                        subs[match] = v
                    else:
                        problems.append(f"{cur}: cannot read subscale part {p!r}")
            rows.append({"family": cur, "part": "total", "type": total, "draft": draft["total_type"], "decided_by": src})
            for s in draft["subscales"]:
                rows.append({"family": cur, "part": s["name"], "type": subs[s["name"]], "draft": s["type"],
                             "decided_by": "agree" if subs[s["name"]] == s["type"] else "R1"})
            cur = None
    if a.out:
        with Path(a.out).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["family", "part", "type", "draft", "decided_by"], lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    fams = {r["family"] for r in rows}
    print(f"{len(fams)} families decided, {len(rows)} rows; changed from draft: {sum(1 for r in rows if r['type'] != r['draft'])}")
    for p in problems:
        print("  " + p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--name", required=True)
    m.add_argument("--force", action="store_true")
    m.add_argument("--out", help="decision file (default decisions/instrument_types_R1.md)")
    p = sub.add_parser("parse")
    p.add_argument("--name", help="unused: every types_*.jsonl is read")
    p.add_argument("--out")
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
