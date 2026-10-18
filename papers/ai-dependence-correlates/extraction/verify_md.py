"""Verification files for R1 (protocol §11c, §14): the AI extraction drafts as Markdown, and the parser of R1's corrections.

make  - writes extraction/verify/verify_R1_NN.md from the drafts: one block per study, one sub-block per sample with the
        effects (key numbers in a table), the key fields, the other fields and the six risk-of-bias items, each with its
        location and quote. Under every sample R1 writes corrections in "Правки" and "да" after "Проверено:".
parse - reads the filled files, applies R1's corrections to the stored drafts and writes
        extraction/decisions/samples_R1.csv, effects_R1.csv and corrections_R1.csv (AI value vs R1 value, for the
        share of corrected values); lists unverified samples and lines it could not read.
Template: papers/misophonia-prevalence/extraction/verify_md.py (same file layout and correction syntax; prevalence
estimates replaced by correlations, JBI by the six AXIS items).

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/verify_md.py make --run 2026-10-16 --draft extract_<date>
     .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/verify_md.py parse --run 2026-10-16 --draft extract_<date>
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
PAPER = HERE.parent
VERIFY = HERE / "verify"
sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402
STUDIES_PER_FILE = 10

KEY_SAMPLE = ["n_analysed", "population", "sampling", "ai_system"]
OTHER_SAMPLE = ["country", "data_years", "design", "clinical_group", "age_mean", "age_sd", "age_min", "age_max",
                "pct_female", "mode", "attention_checks", "pub_status", "language", "funding_coi"]
SAMPLE_FIELDS = KEY_SAMPLE + OTHER_SAMPLE
EFF_FIELDS = ["exposure_family", "exposure_part", "exposure_alpha", "correlate_construct", "correlate_instrument",
              "correlate_alpha", "direction_note", "stat_type", "value", "ci_or_se", "n", "wave", "location", "quote",
              "note"]
KEY_EFF = ["exposure_family", "exposure_part", "correlate_construct", "correlate_instrument", "direction_note",
           "stat_type", "value", "n"]
ROB_Q = {1: "отбор выборки", 2: "отклик", 3: "валидная шкала зависимости от ИИ", 4: "надёжность шкалы ИИ в выборке",
         5: "валидные шкалы коррелятов", 6: "качество данных"}
VERIFIED = {"да", "+", "x", "х", "yes", "ok"}

HEADER = """# Проверка выписывания — файл {i} из {n}

Черновик заполнил ИИ (Claude Opus 5.5) по полному тексту; у каждого значения указано место и цитата. Проверяете вы, один проход.

**Как проверять выборку:**
1. Откройте полный текст по ссылке у исследования.
2. **Ключевые числа** — сверить с таблицей корреляций статьи всегда: в таблице эффектов шкала ИИ и её часть, коррелят, r, n, тип статистики; под таблицей n_analysed, population, sampling, ai_system.
3. Остальные поля и пункты риска смещения: проверить, что значение есть в цитате и место указано верно.
4. Неверное — исправьте строкой в блоке «Правки» этой выборки (по одной правке на строку):
   - `n_analysed = 412`, `sampling = convenience` — поле выборки;
   - `E3.value = -.21`, `E3.correlate_construct = stress`, `E3.n = 398` — поле эффекта E3;
   - `E3 удалить` — убрать эффект (например, частная корреляция или коррелят не из словаря);
   - `+ эффект: exposure_family=DAI; exposure_part=total; correlate_construct=loneliness; correlate_instrument=UCLA-3; stat_type=pearson; value=.24; n=412; wave=1; location=Table 2` — добавить пропущенный эффект;
   - `rob_3 = no` — пункт риска смещения;
   - `выборка удалить: причина` — если это не отдельная выборка или её нельзя брать;
   - после `#` — комментарий для Claude.
5. Когда выборка проверена, напишите `да` после «Проверено:».

**Подсказки в файле:** «⚠ Проверка скриптом» — места, где скрипт нашёл повод присмотреться: r вне [−1; 1]; n эффекта не равно n выборки; коррелят со шкалой «наоборот» (знак перевернём в анализе); часть шкалы не из списка семейства; число не встретилось в независимом проходе ИИ по полному тексту (на этапе решений о включении) или наоборот — там было, а здесь нет. «Расхождения в тексте» — ошибки самих авторов, которые нашёл ИИ; в этом случае ИИ берёт числа из таблицы.

**Тип статистики:** pearson, spearman; latent — корреляция латентных переменных (таблица Форнелла — Ларкера, корреляции факторов); beta_single_predictor — β регрессии с одним предиктором; converted_or / converted_d — сравнение групп, переведём в r. Частные корреляции, β с несколькими предикторами, пути SEM и HTMT не выписываем.
**Конструкты коррелятов** (`forms/construct_dictionary.csv`): первичные — depression, anxiety, stress, loneliness, social_anxiety, self_esteem, procrastination; остальные вторичные. **Тип шкалы ИИ** в таблице — ваше решение по `instrument_types_R1.md`, для справки.
**population:** adolescents, university_students, employees, general_adults, clinical, mixed. **sampling:** probability, census, quota or online panel, convenience, snowball, NR. **ai_system:** general_chatbot, ai_companion, task_assistant, ai_unspecified, mixed.
"""


def load(run: str, draft: str):
    recs = load_records(run)
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    drafts = {}
    for line in (HERE / "draft" / f"{draft}.jsonl").open(encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            drafts[d["conv_id"]] = d
    return recs, jobs, drafts


def sample_keys(jobs: list[dict], drafts: dict) -> list[tuple[str, dict, int, dict]]:
    """(sample_key, job, index in job, sample) in study order; keys are <study_id>-<n>."""
    out, count = [], {}
    for j in sorted(jobs, key=lambda x: (x["study_id"], x["job_id"])):
        d = drafts.get(j["job_id"])
        if not d:
            continue
        for i, s in enumerate(d["codes"]["samples"]):
            count[j["study_id"]] = count.get(j["study_id"], 0) + 1
            out.append((f"{j['study_id']}-{count[j['study_id']]}", j, i, s))
    return out


def clip(t: str, n: int) -> str:
    t = re.sub(r"\s+", " ", t or "").strip()
    return t if len(t) <= n else t[: n - 1] + "…"


def cell(t: str) -> str:
    return (t or "").replace("|", "/").replace("\n", " ")


def link(rec: str, label: str) -> str:
    pdf = PAPER / "fulltext" / "pdf" / f"{rec}.pdf"
    parts = [f"[текст](../../fulltext/text/{rec}.txt)"]
    if pdf.exists():
        parts.append(f"[PDF](../../fulltext/pdf/{rec}.pdf)")
    else:
        for ext in (".docx", ".pdf", ".html"):
            m = PAPER / "fulltext" / "manual" / f"{rec}{ext}"
            if m.exists():
                parts.append(f"[файл](../../fulltext/manual/{rec}{ext})")
                break
    return f"{label} {rec}: " + " · ".join(parts)


NUM = re.compile(r"[-−–]?\s*\d*\.\d+|[-−–]?\s*\d+")


def coef(v: str) -> float | None:
    """The first number of a printed coefficient (".31**", "−0.12", "0,25"), or None."""
    m = NUM.search((v or "").replace(",", "."))
    if not m:
        return None
    try:
        return float(re.sub(r"\s", "", m.group(0)).replace("−", "-").replace("–", "-"))
    except ValueError:
        return None


def as_int(v: str) -> int | None:
    try:
        return int(float((v or "").replace(",", "").strip()))
    except ValueError:
        return None


FT_PROPOSALS: dict[str, dict] = {}   # rec_id -> full-text proposal (fulltext/llm/ft_*.jsonl), filled by make()
TYPES: dict[tuple[str, str], str] = {}   # (family, part) -> R1's type (instruments.csv)
PARTS: dict[str, list[str]] = defaultdict(list)


def ft_values(recs: list[str]) -> set[float]:
    out = set()
    for r in recs:
        p = FT_PROPOSALS.get(r)
        if p:
            for c in p["codes"]["correlations"]:
                x = coef(c["value"])
                if x is not None:
                    out.add(round(x, 2))
    return out


def canon_part(fam: str, part: str) -> str | None:
    """The part of instruments.csv an effect refers to: exact, or the same name without bracketed text, or a prefix."""
    if part in PARTS.get(fam, []):
        return part
    def base(x: str) -> str:
        return re.sub(r"\s*\([^)]*\)", "", x or "").strip().lower()
    hits = [p for p in PARTS.get(fam, []) if base(p) == base(part)]
    if not hits:
        hits = [p for p in PARTS.get(fam, []) if base(p).startswith(base(part)) or base(part).startswith(base(p))]
    return hits[0] if len(hits) == 1 else None


def flags(s: dict, recs: list[str]) -> list[str]:
    """Checks by script, shown to R1 next to the effects; the drafts themselves are not changed."""
    groups: dict[str, list[str]] = {}
    n_sample = as_int(s["n_analysed"]["value"])
    ft = ft_values(recs)
    drafted = set()
    for i, e in enumerate(s["effects"], 1):
        x = coef(e["value"])
        if e["stat_type"] in ("pearson", "spearman", "latent", "beta_single_predictor"):
            if x is None:
                groups.setdefault("значение не число", []).append(f"E{i}")
            elif abs(x) > 1:
                groups.setdefault("|r| > 1", []).append(f"E{i}")
            else:
                drafted.add(round(x, 2))
                if ft and round(x, 2) not in ft:
                    groups.setdefault("этого числа нет в независимом проходе ИИ по полному тексту — сверьте с таблицей", []).append(f"E{i}")
        n = as_int(e["n"])
        if n and n_sample and n != n_sample:
            groups.setdefault(f"n эффекта не равно n_analysed выборки ({n_sample})", []).append(f"E{i}")
        if "revers" in (e["direction_note"] or "").lower():
            groups.setdefault("шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление", []).append(f"E{i}")
        fam = e["exposure_family"]
        if fam not in PARTS:
            groups.setdefault("шкала ИИ не из списка семейств: напишите, какая это шкала", []).append(f"E{i}")
        elif canon_part(fam, e["exposure_part"]) is None:
            groups.setdefault("часть шкалы ИИ не из списка её подшкал: проверьте, какая подшкала", []).append(f"E{i}")
        if e["wave"].strip().lower().startswith("lagged"):
            groups.setdefault("корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера", []).append(f"E{i}")
        elif e["wave"].strip() not in ("1", ""):
            groups.setdefault("поздняя волна: в основной анализ не идёт, только в описание", []).append(f"E{i}")
        if e["stat_type"] in ("converted_or", "converted_d", "beta_single_predictor"):
            groups.setdefault("не корреляция, а пересчёт: проверьте, что β с одним предиктором или что группы сравнения верны", []).append(f"E{i}")
    missed = sorted(v for v in ft - drafted if v != 0)
    if missed and s["effects"]:
        groups.setdefault("в независимом проходе были ещё числа: " + ", ".join(f"{v:.2f}" for v in missed[:12])
                          + (" …" if len(missed) > 12 else "") + " — нет ли пропущенных эффектов (они могут быть и не про эту выборку)", [])
    return [f"{', '.join(v)}: {k}" if v else k for k, v in groups.items()]


def render_sample(key: str, s: dict, recs: list[str]) -> list[str]:
    L = [f"### {key} · {clip(s['label'], 160)}", f"Отчёты: {s['reports']}", ""]
    L.append("**Эффекты — ключевые числа сверить по таблице статьи:**")
    L.append("")
    L.append("| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |")
    L.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    extra = []
    for i, e in enumerate(s["effects"], 1):
        t = TYPES.get((e["exposure_family"], canon_part(e["exposure_family"], e["exposure_part"]) or ""), "?")
        L.append(f"| E{i} | {cell(e['exposure_family'])} · {cell(clip(e['exposure_part'], 50))} ({t}) | "
                 f"**{e['correlate_construct']}** · {cell(clip(e['correlate_instrument'], 60))} | {e['stat_type']} | "
                 f"**{cell(e['value'])}** | **{cell(e['n'])}** | {cell(e['wave'])} | {cell(clip(e['location'], 50))} | "
                 f"«{cell(clip(e['quote'], 200))}» |")
        bits = []
        if e["direction_note"] and e["direction_note"].strip().lower() != "as named":
            bits.append(f"**направление: {clip(e['direction_note'], 160)}**")
        if e["exposure_alpha"] not in ("", "NR", "NA") or e["correlate_alpha"] not in ("", "NR", "NA"):
            bits.append(f"α ИИ {e['exposure_alpha']}, α коррелята {e['correlate_alpha']}")
        if e["ci_or_se"] not in ("", "NA", "NR"):
            bits.append(f"для пересчёта: {clip(e['ci_or_se'], 120)}")
        if e["note"]:
            bits.append(f"заметка: {clip(e['note'], 300)}")
        if bits:
            extra.append(f"- E{i}: " + "; ".join(bits))
    if not s["effects"]:
        L.append("| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |")
    L += [""] + extra
    fl = flags(s, recs)
    if fl:
        L += ["", "**⚠ Проверка скриптом (обратите внимание):**"] + [f"- {x}" for x in fl]
    L += ["", "**Ключевые поля выборки:**"]
    for f in KEY_SAMPLE:
        v = s[f]
        L.append(f"- **{f}: {v['value']}** — {clip(v['loc'], 80)} — «{clip(v['quote'], 260)}»")
    L += ["", "**Остальные поля:**"]
    for f in OTHER_SAMPLE:
        v = s[f]
        q = f" — «{clip(v['quote'], 160)}»" if v["quote"] else ""
        loc = f" — {clip(v['loc'], 60)}" if v["loc"] else ""
        L.append(f"- {f}: {clip(v['value'], 300)}{loc}{q}")
    if s.get("notes"):
        L.append(f"- notes: {clip(s['notes'], 600)}")
    L += ["", "**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**"]
    for i in range(1, 7):
        b = s["rob"][f"rob_{i}"]
        q = f" — «{clip(b['quote'], 160)}»" if b["quote"] else ""
        L.append(f"{i}. {ROB_Q[i]}: **{b['rating']}** — {clip(b['reason'], 220)} — {clip(b['loc'], 60)}{q}")
    L += ["", "Правки:", "- ", "", "Проверено: ", ""]
    return L


def load_reference() -> None:
    for f in sorted((PAPER / "fulltext" / "llm").glob("ft_*.jsonl")):   # independent AI pass over the same full texts
        if ".errors." in f.name:
            continue
        for line in f.open(encoding="utf-8"):
            if line.strip():
                p = json.loads(line)
                FT_PROPOSALS[p["conv_id"]] = p
    for r in csv.DictReader((HERE / "instruments.csv").open(encoding="utf-8")):
        TYPES[(r["family"], r["part"])] = r["type"]
        PARTS[r["family"]].append(r["part"])


def make(a):
    recs, jobs, drafts = load(a.run, a.draft)
    load_reference()
    missing = [j["job_id"] for j in jobs if j["job_id"] not in drafts]
    if missing and not a.allow_missing:
        raise SystemExit(f"no draft for {len(missing)} jobs: {', '.join(missing)}")
    keyed = sample_keys(jobs, drafts)
    by_study: dict[str, list] = {}
    for key, j, i, s in keyed:
        by_study.setdefault(j["study_id"], []).append((key, j, s))
    studies = sorted(by_study)
    if a.studies:   # only these studies, in new files numbered from --first-file (files of R1 are never touched)
        studies = [s for s in studies if s in set(a.studies)]
    chunks = [studies[i:i + STUDIES_PER_FILE] for i in range(0, len(studies), STUDIES_PER_FILE)]
    outdir = Path(a.out) if a.out else VERIFY
    outdir.mkdir(exist_ok=True)
    first = a.first_file
    names = [outdir / f"verify_R1_{fi:02d}.md" for fi in range(first, first + len(chunks))]
    clash = [p for p in names if p.exists()]
    if a.studies and clash:
        raise SystemExit(f"refusing to overwrite: {', '.join(p.name for p in clash)}")
    existing = sorted(outdir.glob("verify_R1_*.md"))
    if existing and not a.force and not a.studies:
        raise SystemExit(f"{len(existing)} verification files exist; use --force to overwrite")
    n_samples = n_eff = 0
    for fi, chunk in enumerate(chunks, first):
        L = [HEADER.format(i=fi, n=first - 1 + len(chunks))]
        for st in chunk:
            jobs_here = sorted({j["job_id"] for _, j, _ in by_study[st]})
            u0 = recs[jobs_here[0]]
            L += ["---", "", f"## {st} · {u0.get('first_author') or ''} {u0.get('year') or ''} · "
                             f"{clip(u0.get('venue') or '', 80)}", ""]
            for jid in jobs_here:
                j = next(x for x in jobs if x["job_id"] == jid)
                d = drafts[jid]["codes"]
                u = recs[jid]
                L.append(link(jid, "Основной отчёт") + f" — «{clip(u['title'], 160)}»" +
                         (f" — [DOI](https://doi.org/{u['doi']})" if u.get("doi") else ""))
                for e in j["attached"]:
                    L.append(link(e, "Приложен") + f" — «{clip(recs[e]['title'], 120)}»")
                for e in j["listed_only"]:
                    L.append(link(e, "Не приложен (длинный)") + f" — «{clip(recs[e]['title'], 120)}»")
                if j["link_reason"]:
                    L.append(f"Связь отчётов: {j['link_reason']}")
                for po in j["possible_overlap"]:
                    L.append(f"⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): {po}")
                if d["excluded_samples"] and d["excluded_samples"].strip().upper() not in ("NA", "NONE", "NR") \
                        and not d["excluded_samples"].lower().startswith("none"):
                    L.append(f"Не выписано ИИ: {clip(d['excluded_samples'], 700)}")
                if d["longitudinal_note"] and d["longitudinal_note"].strip().upper() != "NA":
                    L.append(f"Лонгитюд (для описания): {clip(d['longitudinal_note'], 900)}")
                if d["consistency_notes"] and d["consistency_notes"].strip().upper() not in ("NA", "NONE"):
                    L.append(f"Расхождения в тексте: {clip(d['consistency_notes'], 900)}")
                if d["note"] and d["note"].strip().upper() not in ("NA", "NONE"):
                    L.append(f"Заметка ИИ: {clip(d['note'], 600)}")
                L.append("")
            for key, j, s in by_study[st]:
                L += render_sample(key, s, [j["main"], *j["attached"]])
                n_samples += 1
                n_eff += len(s["effects"])
        out = outdir / f"verify_R1_{fi:02d}.md"
        out.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(studies)} studies, {n_samples} samples, {n_eff} effects -> {len(chunks)} files in {outdir}")
    if missing:
        print(f"WARNING: no draft yet for {len(missing)} jobs: {', '.join(missing)}")


EFF_RE = re.compile(r"^E(\d+)\.(\w+)\s*=\s*(.*)$")
DEL_RE = re.compile(r"^E(\d+)\s+удалить\b(.*)$", re.I)
ADD_RE = re.compile(r"^\+\s*эффект\s*:\s*(.*)$", re.I)
ROB_RE = re.compile(r"^rob_([1-6])\s*=\s*(yes|no|unclear)\b(.*)$", re.I)
DROP_RE = re.compile(r"^выборка\s+удалить\b[:\s]*(.*)$", re.I)
FIELD_RE = re.compile(r"^(\w+)\s*=\s*(.*)$")


def parse(a):
    recs, jobs, drafts = load(a.run, a.draft)
    keyed = {key: (j, s) for key, j, i, s in sample_keys(jobs, drafts)}
    blocks = {}
    for p in sorted((Path(a.out) if a.out else VERIFY).glob("verify_R1_*.md")):
        text = p.read_text(encoding="utf-8")
        for m in re.finditer(r"^### (ST\d{3}-\d+) .*?(?=^### |^---|\Z)", text, re.S | re.M):
            blocks[m.group(1)] = (p.name, m.group(0))
    samples_out, eff_out, corr, problems, unverified = [], [], [], [], []
    for key, (j, s) in keyed.items():
        if key not in blocks:
            problems.append(f"{key}: block not found")
            continue
        fname, body = blocks[key]
        pr = re.search(r"^Правки:\s*\n(.*?)^Проверено:(.*)$", body, re.S | re.M)
        if not pr:
            problems.append(f"{fname} {key}: no 'Правки'/'Проверено' lines")
            continue
        ver = pr.group(2).strip().lower()
        if ver not in VERIFIED:
            unverified.append(key)
        fields = {f: s[f]["value"] for f in SAMPLE_FIELDS}
        effs = {i: dict(e) for i, e in enumerate(s["effects"], 1)}
        rob = {i: s["rob"][f"rob_{i}"]["rating"] for i in range(1, 7)}
        dropped, added, comments = "", [], []
        for raw in pr.group(1).splitlines():
            line = raw.strip().lstrip("-").strip()
            if not line:
                continue
            line, _, comment = line.partition("#")
            line = line.strip()
            if comment.strip():
                comments.append(comment.strip())
            if not line:
                continue
            if m := DEL_RE.match(line):
                k = int(m.group(1))
                if k in effs:
                    corr.append({"sample_key": key, "target": f"E{k}", "field": "*", "ai_value": "effect",
                                 "r1_value": "deleted", "key_field": "yes"})
                    effs.pop(k)
                else:
                    problems.append(f"{fname} {key}: no effect E{k}: {raw}")
            elif m := EFF_RE.match(line):
                k, f, v = int(m.group(1)), m.group(2), m.group(3).strip()
                if k not in effs or f not in EFF_FIELDS:
                    problems.append(f"{fname} {key}: unknown effect field: {raw}")
                    continue
                corr.append({"sample_key": key, "target": f"E{k}", "field": f, "ai_value": effs[k][f], "r1_value": v,
                             "key_field": "yes" if f in KEY_EFF else "no"})
                effs[k][f] = v
            elif m := ADD_RE.match(line):
                e = {f: "" for f in EFF_FIELDS}
                for part in m.group(1).split(";"):
                    if "=" in part:
                        f, v = part.split("=", 1)
                        if f.strip() in EFF_FIELDS:
                            e[f.strip()] = v.strip()
                        else:
                            problems.append(f"{fname} {key}: unknown field in added effect: {f.strip()}")
                added.append(e)
                corr.append({"sample_key": key, "target": "new", "field": "*", "ai_value": "", "r1_value": m.group(1),
                             "key_field": "yes"})
            elif m := ROB_RE.match(line):
                i, v = int(m.group(1)), m.group(2).lower()
                corr.append({"sample_key": key, "target": f"rob_{i}", "field": "rating", "ai_value": rob[i],
                             "r1_value": v, "key_field": "no"})
                rob[i] = v
            elif m := DROP_RE.match(line):
                dropped = m.group(1).strip() or "R1"
            elif (m := FIELD_RE.match(line)) and m.group(1) in SAMPLE_FIELDS:
                f, v = m.group(1), m.group(2).strip()
                corr.append({"sample_key": key, "target": "sample", "field": f, "ai_value": fields[f], "r1_value": v,
                             "key_field": "yes" if f in KEY_SAMPLE else "no"})
                fields[f] = v
            else:
                problems.append(f"{fname} {key}: unreadable correction: {raw.strip()}")
        samples_out.append({"sample_key": key, "study_id": j["study_id"], "job_id": j["job_id"], "label": s["label"],
                            "reports": s["reports"], **fields,
                            **{f"rob_{i}": rob[i] for i in range(1, 7)},
                            "verified": "yes" if ver in VERIFIED else "no", "dropped": dropped,
                            "r1_comments": " | ".join(comments)})
        for i, e in list(effs.items()) + [(f"new{n}", e) for n, e in enumerate(added, 1)]:
            eff_out.append({"sample_key": key, "eff": f"E{i}" if isinstance(i, int) else i, **e})
    dec = Path(a.dec) if a.dec else HERE / "decisions"
    dec.mkdir(parents=True, exist_ok=True)
    for name, rows in (("samples_R1.csv", samples_out), ("effects_R1.csv", eff_out), ("corrections_R1.csv", corr)):
        if rows:
            with (dec / name).open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
                w.writeheader()
                w.writerows(rows)
    n_vals = sum(len(SAMPLE_FIELDS) + 6 + len(s["effects"]) * len(EFF_FIELDS) for j, s in keyed.values())
    print(f"samples {len(samples_out)} (unverified {len(unverified)}), effects {len(eff_out)}, corrections {len(corr)} "
          f"of about {n_vals} drafted values")
    if unverified:
        print("unverified:", ", ".join(unverified))
    for p in problems:
        print("PROBLEM:", p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["make", "parse"])
    ap.add_argument("--run", required=True)
    ap.add_argument("--draft", required=True)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--studies", nargs="*", help="make: only these study IDs, into new files")
    ap.add_argument("--first-file", type=int, default=1, help="make: number of the first file")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--out", help="folder of the verification files (default extraction/verify)")
    ap.add_argument("--dec", help="output folder for parse (default extraction/decisions)")
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
