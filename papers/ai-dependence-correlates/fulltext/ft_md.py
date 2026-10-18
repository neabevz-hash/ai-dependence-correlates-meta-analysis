"""Full-text decision files in Markdown (protocol, section 11b). Template: papers/misophonia-prevalence/fulltext/ft_md.py.

Each retrieved report is one block: title, year, venue, links to the full text (local PDF or text, and the source
URL), and the AI proposal: decision, primary reason, sample, AI system, dependence measures, and every zero-order
correlation with an eligible correlate, with its value, location and a verbatim quote. R1 writes a code in the decision line:
  =        agree with the AI proposal
  +        eligible
  -1 … -6  not eligible, the digit is the primary reason (REASONS below)
  ?        not decided yet (must be resolved before the files are closed)
Anything after the code is a note.

  make  --run 2026-10-16 --name ft_2026-10-16   write fulltext/decisions/ft_R1_<nn>.md from fulltext/llm/<name>.jsonl
  parse FILE... --out CSV         decisions -> CSV, and a check that every report has a valid code
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
FILE_SIZE = 50
REASONS = {
    "1": ("E5_design", "обзор, комментарий, теоретическое, протокол, качественное без количественной меры зависимости"),
    "2": ("E1_no_dependence_measure", "нет меры зависимости от ИИ (только частота, принятие, доверие, грамотность, технострес, страх ИИ; over-reliance только в эксперименте)"),
    "3": ("E3_out_of_scope", "социальные роботы, ИИ лечит или выявляет зависимость, ИИ как инструмент анализа, «dependence» в другом смысле"),
    "4": ("no_eligible_correlate", "есть мера зависимости, но нет ни одного нашего коррелята"),
    "5": ("E4_no_zero_order", "нет корреляции нулевого порядка (только пути SEM, многомерные β, частные корреляции, HTMT)"),
    "6": ("E6_duplicate", "та же выборка, что в другом отчёте (связать)"),
    "7": ("other", "другое — напишите почему"),
}
AI_TO_CODE = {"E5_design": "-1", "E1_no_dependence_measure": "-2", "E3_out_of_scope": "-3", "no_eligible_correlate": "-4",
              "E4_no_zero_order": "-5", "other": "-7"}
HEADER_RE = re.compile(r"^###\s+(\d+)\s*·\s*(R\d{4,5})\b")
DECISION_RE = re.compile(r"^\**\s*Решение\s*:?\s*\**\s*:?\s*(.*)$", re.I)
AI_RE = re.compile(r"^\**\s*ИИ предлагает\s*:?\s*\**\s*:?\s*(\S+)")

GUIDE = """**Как размечать.** Откройте полный текст (ссылка в блоке), сверьте предложение ИИ и допишите код в строку **Решение:**.

| Код | Что значит |
| --- | --- |
| `=` | согласен с ИИ |
| `+` | подходит: есть мера зависимости от ИИ, наш коррелят и корреляция нулевого порядка между ними |
{reasons}
| `?` | пока не решил (до закрытия файла нужно решить) |

Корреляции ИИ брал из текста, но выписываться они будут на следующем этапе по оригиналу — здесь решаем только «подходит / нет» и причину. Таблица корреляций часто в конце статьи или в приложении.
"""


def one_line(t: str) -> str:
    return re.sub(r"\s+", " ", t or "").strip()


def block(n: int, rid: str, rec: dict, ret: dict, prop: dict) -> str:
    c = prop["codes"]
    code = "+" if c["decision"] == "eligible" else ("?" if c["decision"] == "unclear" else AI_TO_CODE.get(c["reason"], "-7"))
    local = f"fulltext/pdf/{rid}.pdf" if (HERE / "pdf" / f"{rid}.pdf").exists() else f"fulltext/text/{rid}.txt"
    lines = ["---", "", f"### {n} · {rid}", "", f"**{one_line(rec['title'])}**", "",
             " · ".join(x for x in [str(rec.get('year') or ''), one_line(rec.get('venue')), ret.get('source', '')] if x), "",
             f"Текст: `{local}` · источник: {ret.get('url', '')}", "",
             f"**ИИ предлагает:** {code} · {c['decision']} · {c['reason']}", "",
             f"- Выборка: {one_line(c['sample'])}", f"- Система ИИ: {one_line(c['ai_system'])}",
             f"- Мера зависимости: {one_line(c['dependence_measures'])}"]
    for d in c["correlations"]:
        lines.append(f"- r: {one_line(d['exposure'])} × {one_line(d['correlate'])} ({one_line(d['correlate_instrument'])}) = "
                     f"{d['value']} [{d['stat_type']}, n = {d['n']}]; {d['location']}: «{one_line(d['quote'])}»")
    if one_line(c["possible_duplicate"]):
        lines.append(f"- Возможный дубль: {one_line(c['possible_duplicate'])}")
    if one_line(c["note"]):
        lines.append(f"- Заметка ИИ: {one_line(c['note'])}")
    lines += ["", "**Решение:** ", ""]
    return "\n".join(lines)


def make(a) -> None:
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in
            (PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")}
    ret = {r["rec_id"]: r for r in csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig"))}
    props = {json.loads(l)["conv_id"]: json.loads(l) for l in (HERE / "llm" / f"{a.name}.jsonl").open(encoding="utf-8")}
    ids = sorted(props)
    out_dir = HERE / "decisions"
    out_dir.mkdir(exist_ok=True)
    reasons = "\n".join(f"| `-{d}` | не подходит: {t} |" for d, (_, t) in REASONS.items())
    for part, start in enumerate(range(0, len(ids), FILE_SIZE), a.first_part):
        chunk = ids[start:start + FILE_SIZE]
        path = out_dir / f"ft_{a.screener}_{part:02d}.md"
        if path.exists() and not a.force:
            sys.exit(f"{path} exists; refusing to overwrite R1's work")
        blocks = [block(start + i, rid, recs[rid], ret[rid], props[rid]) for i, rid in enumerate(chunk, 1)]
        head = (f"# Полные тексты, часть {part}\n\nОтчёты {start + 1}–{start + len(chunk)} из {len(ids)}. "
                f"Предложение ИИ — черновик, решаете вы.\n\n{GUIDE.format(reasons=reasons)}\n")
        path.write_text(head + "\n".join(blocks), encoding="utf-8", newline="\n")
        print(f"{path}  ({len(chunk)} reports)")


def parse_code(raw: str) -> tuple[str, str, str, str]:
    text = raw.strip().replace("−", "-").replace("–", "-").replace("—", "-")
    text = re.sub(r"^-\s+(\d)", r"-\1", text)
    if not text:
        return "", "", "", ""
    head, _, note = text.partition(" ")
    if head == "+":
        return head, "eligible", "", note.strip()
    if head == "?":
        return head, "undecided", "", note.strip()
    if head == "=":
        return head, "agree", "", note.strip()
    m = re.fullmatch(r"-([1-7])", head)
    if m:
        return head, "not_eligible", REASONS[m.group(1)][0], note.strip()
    return head, "", "", text


def parse(a) -> None:
    rows, problems = [], []
    for f in a.files:
        lines = [x.strip() for x in Path(f).read_text(encoding="utf-8").splitlines()]
        cur = None
        for i, line in enumerate(lines):
            h = HEADER_RE.match(line)
            if h:
                cur = {"file": Path(f).name, "k": int(h.group(1)), "rec_id": h.group(2), "ai_code": ""}
                continue
            if cur is None:
                continue
            m = AI_RE.match(line)
            if m:
                cur["ai_code"] = m.group(1)
                continue
            d = DECISION_RE.match(line)
            if d:
                raw = d.group(1)
                if not raw.strip():
                    nxt = next((x for x in lines[i + 1:] if x), "")
                    if nxt and not nxt.startswith("---") and not HEADER_RE.match(nxt):
                        raw = nxt
                code, decision, reason, note = parse_code(raw)
                if decision == "agree":
                    ai = cur["ai_code"]
                    _, decision, reason, _ = parse_code(ai) if ai else ("", "", "", "")
                    code = f"={ai}"
                    if decision == "undecided":
                        problems.append(f"{cur['rec_id']}: '=' but the AI proposal is unclear — choose a code")
                if not code:
                    problems.append(f"{cur['rec_id']}: no decision")
                elif not decision:
                    problems.append(f"{cur['rec_id']}: cannot read the code {code!r}")
                elif decision == "undecided":
                    problems.append(f"{cur['rec_id']}: still undecided ('?')")
                rows.append({**cur, "code": code, "decision": decision, "reason": reason, "note": note})
                cur = None
    if a.out:
        with Path(a.out).open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["rec_id", "k", "file", "code", "decision", "reason", "note", "ai_code"])
            w.writeheader()
            w.writerows(rows)
    counts = {k: sum(1 for r in rows if r["decision"] == k) for k in ("eligible", "not_eligible", "undecided", "")}
    print(f"{len(rows)} reports: eligible {counts['eligible']}, not eligible {counts['not_eligible']}, "
          f"undecided {counts['undecided']}, no code {counts['']}")
    for p in problems[:40]:
        print("  " + p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--run", required=True)
    m.add_argument("--name", required=True)
    m.add_argument("--screener", default="R1")
    m.add_argument("--force", action="store_true")
    m.add_argument("--first-part", type=int, default=1, help="number of the first file (continue a series)")
    p = sub.add_parser("parse")
    p.add_argument("files", nargs="+")
    p.add_argument("--out")
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
