"""Manuscript tables from the verified tables and the analysis results, so that the text never retypes a number.

Table 1 - characteristics of the included samples (forms/samples.csv, forms/effects.csv);
Table 2 - pooled correlations: primary correlates and secondary correlates with k >= 3 samples (analysis/results/pooled.csv);
Table 3 - pooled correlations by type of AI-dependence scale for the primary correlates (by_type.csv), with the
          registered contrast (type_tests.csv) and the post hoc contrast including T4 (posthoc_type_tests.csv, D6);
Table 4 - summary of findings with the GRADE rating (protocol section 17; thresholds in deviations.md D7 and the note).
Writes manuscript/tables.md and analysis/results/grade.csv.
Template: papers/misophonia-prevalence/manuscript/make_tables.py.

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/manuscript/make_tables.py
"""
from __future__ import annotations

import csv
import statistics
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
RES = PAPER / "analysis" / "results"
PRIMARY = ["depression", "anxiety", "stress", "loneliness", "social_anxiety", "self_esteem", "procrastination"]
LABEL = {"depression": "Depression", "anxiety": "Anxiety", "stress": "Stress", "loneliness": "Loneliness",
         "social_anxiety": "Social anxiety", "self_esteem": "Self-esteem", "procrastination": "Procrastination",
         "self_efficacy": "Self-efficacy", "academic_stress": "Academic stress", "ai_anxiety": "AI anxiety",
         "self_control": "Self-control", "extraversion": "Extraversion", "conscientiousness": "Conscientiousness",
         "neuroticism": "Neuroticism", "openness": "Openness", "agreeableness": "Agreeableness",
         "social_support": "Social support", "distress": "Psychological distress", "escapism_motive": "Escapism motive",
         "wellbeing": "Well-being", "problematic_internet_use": "Problematic internet use",
         "sleep_quality": "Sleep quality", "attachment_anxiety": "Attachment anxiety", "fomo": "Fear of missing out",
         "impulsivity": "Impulsivity", "problematic_social_media_use": "Problematic social media use",
         "problematic_smartphone_use": "Problematic smartphone use", "attachment_avoidance": "Attachment avoidance",
         "boredom": "Boredom proneness", "mindfulness": "Mindfulness"}
DESIGN = {"cross-sectional": "Cross-sectional", "validation study": "Scale validation study",
          "panel": "Panel (first wave)", "other": "Other"}
PUB = {"journal": "Journal article", "preprint": "Preprint", "conference": "Conference paper", "other": "Other"}
POP = {"university_students": "University students", "general_adults": "General adults", "employees": "Employees",
       "adolescents": "Adolescents (<18 years)", "mixed": "Mixed", "clinical": "Clinical"}
REGION = {"mainland_China": "Mainland China", "South_Southeast_Asia": "South and Southeast Asia",
          "MENA_Turkiye": "Middle East, North Africa and Türkiye", "Americas": "Americas", "Europe": "Europe",
          "other_East_Asia": "Other East Asia", "other": "Other", "multi": "Several countries", "": "Not reported"}
AI = {"general_chatbot": "General chatbot (e.g., ChatGPT)", "ai_unspecified": "AI tools, unspecified",
      "ai_companion": "AI companion", "mixed": "Mixed", "task_assistant": "Task assistant"}
TYPE = {"T1": "T1 addiction-type", "T2": "T2 functional", "T3": "T3 emotional", "T4": "T4 mixed or unclear"}


def rd(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open(encoding="utf-8")))


def f2(x: str) -> str:
    return f"{float(x):.2f}".replace("-", "−")


NB = " "   # non-breaking space: an interval stays on one line in the Word tables


def ci(r: dict) -> str:
    return f"{f2(r['r'])}{NB}({f2(r['ci.lb'])},{NB}{f2(r['ci.ub'])})"


def pi(r: dict) -> str:
    return f"{f2(r['pi.lb'])},{NB}{f2(r['pi.ub'])}"


def p_cell(p: float) -> str:
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def p_txt(p: float) -> str:
    return "p < 0.001" if p < 0.001 else f"p = {p:.3f}"


def lab(c: str) -> str:
    return LABEL.get(c, c)


def count_rows(title: str, counter: Counter, names: dict, n: int) -> list[str]:
    out = [f"| **{title}** | |"]
    for k, v in sorted(counter.items(), key=lambda kv: -kv[1]):
        out.append(f"| {names.get(k, k)} | {v} ({100 * v / n:.0f}) |")
    return out


def num(x: str) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def table1() -> list[str]:
    s = rd(PAPER / "forms" / "samples.csv")
    e = rd(PAPER / "forms" / "effects.csv")
    n = len(s)
    ns = [num(x["n_analysed"]) for x in s if num(x["n_analysed"])]
    ages = [num(x["age_mean"]) for x in s if num(x["age_mean"])]
    fem = [num(x["pct_female"]) for x in s if num(x["pct_female"]) is not None]
    years = Counter(x["year"] for x in s)
    types = Counter()
    for sid in {x["sample_id"] for x in s}:
        for t in sorted({x["exposure_type"] for x in e if x["sample_id"] == sid}):
            types[t] += 1
    q = statistics.quantiles(ns, n=4)
    L = [f"**Table 1.** Characteristics of the included samples (k = {n} samples from {len({x['study_id'] for x in s})} studies).", "",
         "| Characteristic | Samples, n (%) |", "| --- | --- |",
         f"| Participants analysed, total | {int(sum(ns)):,} (n reported in {len(ns)} samples) |",
         f"| Sample size, median (IQR) | {statistics.median(ns):.0f} ({q[0]:.0f}–{q[2]:.0f}) |",
         f"| Mean age, median of sample means (range) | {statistics.median(ages):.1f} ({min(ages):.1f}–{max(ages):.1f}; reported in {len(ages)}) |",
         f"| Female, median % (range) | {statistics.median(fem):.0f} ({min(fem):.0f}–{max(fem):.0f}; reported in {len(fem)}) |",
         f"| Publication year | " + ", ".join(f"{y}: {c}" for y, c in sorted(years.items())) + " |"]
    L += count_rows("Population", Counter(x["population"] for x in s), POP, n)
    L += count_rows("Region", Counter(x["region"] for x in s), REGION, n)
    L += count_rows("AI system", Counter(x["ai_system"] for x in s), AI, n)
    L += count_rows("Type of AI-dependence scale (a sample may use several)", types, TYPE, n)
    L += count_rows("Design", Counter(x["design"] for x in s), DESIGN, n)
    L += count_rows("Publication status", Counter(x["pub_status"] for x in s), PUB, n)
    L += ["| **Risk of bias (AXIS item): yes / no / unclear** | |"]
    for k, name in ((1, "1 Probability or census sampling"), (3, "3 Validated AI-dependence scale"),
                    (6, "6 Data-quality checks")):
        c = Counter(x[f"rob_{k}"] for x in s)
        L.append(f"| {name} | {c['yes']} / {c['no']} / {c['unclear']} |")
    L += ["", f"Samples without any eligible zero-order correlation: {n - len({x['sample_id'] for x in e})} "
              "(correlations shown only in figures, correlates outside the dictionary, or only multivariable coefficients)."]
    return L


def table2() -> list[str]:
    pooled = [r for r in rd(RES / "pooled.csv") if r["r"] not in ("", "NA")]
    L = ["**Table 2.** Pooled correlations between AI dependence and its correlates (CHE model, Fisher's z, CR2 "
         "cluster-robust inference; correlates with at least three independent samples).", "",
         "| Correlate | Studies / samples / effects | Participants | r (95% CI) | 95% PI | p | I² samples / effects, % |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    for grp in ("primary", "secondary"):
        L.append(f"| **{'Primary' if grp == 'primary' else 'Secondary'}** | | | | | | |")
        rows = [r for r in pooled if r["role"] == grp]
        rows.sort(key=lambda r: PRIMARY.index(r["analysis"]) if grp == "primary" else -float(r["r"]))
        for r in rows:
            L.append(f"| {lab(r['analysis'])} | {r['k_studies']}{NB}/{NB}{r['k_samples']}{NB}/{NB}{r['k_effects']} | "
                     f"{int(float(r['n_total'])):,} | {ci(r)} | {pi(r)} | {p_cell(float(r['p']))} | "
                     f"{float(r['I2_sample']):.0f} / {float(r['I2_effect']):.0f} |")
    not_pooled = [r for r in rd(RES / "pooled.csv") if r["r"] in ("", "NA")]
    L += ["", "PI, prediction interval. Positive r: more AI dependence goes with more of the correlate (scores recoded "
              "where a scale measures the opposite pole). Not pooled (fewer than three samples): "
              + "; ".join(f"{lab(r['analysis'])} (k = {r['k_samples']})" for r in not_pooled) + "."]
    return L


def table3() -> list[str]:
    bt = rd(RES / "by_type.csv")
    tt = {r["correlate"]: r for r in rd(RES / "type_tests.csv")}
    ph = {r["correlate"]: r for r in rd(RES / "posthoc_type_tests.csv")}
    L = ["**Table 3.** Pooled correlations of the primary correlates by type of AI-dependence scale.", "",
         "| Correlate | T1 addiction-type | T2 functional | T3 emotional | T4 mixed or unclear | Post hoc test, p (D6) |",
         "| --- | --- | --- | --- | --- | --- |"]
    for c in PRIMARY:
        cells = []
        for t in ("T1", "T2", "T3", "T4"):
            r = next((x for x in bt if x["analysis"] == c and x["type"] == t), None)
            k = int(r["k_samples"]) if r else 0
            cells.append("—" if k == 0 else (f"k{NB}={NB}{k}" if r["r"] in ("", "NA") else f"{ci(r)}, k{NB}={NB}{k}"))
        p = ph.get(c)
        test = p_cell(float(p["p"])) if p else "n.e."
        L.append(f"| {lab(c)} | " + " | ".join(cells) + f" | {test} |")
    sec = [r for c, r in ph.items() if c not in PRIMARY]
    L += ["", "The registered contrast of T1, T2 and T3 (protocol §15b) was not estimable for any primary correlate: "
              "fewer than two of these types had three or more samples (" +
              "; ".join(f"{lab(c)}: {tt[c]['types'] or 'none'}" for c in PRIMARY if c in tt) + " with k ≥ 3). "
              "The post hoc contrast adds T4 (deviations.md D6): CHE model, HTZ Wald test of T1 vs T4, run when the "
              "correlate had k ≥ 10 samples and both types k ≥ 3 (F statistics: Supplementary File S9); n.e., not "
              "estimable. Secondary correlates with k ≥ 10: " +
              "; ".join(f"{lab(r['correlate'])} ({r['r_by_type'].replace('-', '−')}; {p_txt(float(r['p']))})" for r in sec) + "."]
    return L


def grade() -> tuple[list[str], list[dict]]:
    """Start high; one level down per serious domain (deviations.md D7)."""
    gi = {r["correlate"]: r for r in rd(RES / "grade_inputs.csv")}
    pooled = {r["analysis"]: r for r in rd(RES / "pooled.csv")}
    bias = {r["correlate"]: r for r in rd(RES / "publication_bias.csv")}
    levels = ["High", "Moderate", "Low", "Very low"]
    L = ["**Table 4.** Summary of findings and certainty of evidence (GRADE) for the primary correlates.", "",
         "| Correlate | Samples (participants) | r (95% CI) | Certainty | Downgraded for |",
         "| --- | --- | --- | --- | --- |"]
    out = []
    for c in PRIMARY:
        g, p = gi[c], pooled[c]
        r, lo, hi = float(g["r"]), float(g["ci.lb"]), float(g["ci.ub"])
        alo, ahi = (lo, hi) if r >= 0 else (-hi, -lo)   # CI of |r| direction
        why, short = [], []
        w = float(g["weight_share_rob_no"])
        if w > 0.5:
            why.append(f"risk of bias ({100 * w:.0f}% of weight from samples rated no on item 1, 3 or 6)")
            short.append(f"risk of bias ({100 * w:.0f}%)")
        if float(g["pi.lb"]) < 0 < float(g["pi.ub"]):
            why.append(f"inconsistency (PI {pi(g)})")
            short.append("inconsistency")
        if alo < 0.10 and ahi > 0.30:
            why.append("imprecision (CI includes |r| < .10 and > .30)")
            short.append("imprecision")
        if int(g["n_regions"]) < 3 or float(g["share_students"]) > 0.75:
            why.append(f"indirectness ({int(g['n_regions'])} regions; {100 * float(g['share_students']):.0f}% student samples)")
            short.append(f"indirectness ({100 * float(g['share_students']):.0f}% students)")
        b = bias.get(c, {})
        ps = [float(b[k]) for k in ("egger_p", "selection_lrt_p") if b.get(k) not in (None, "", "NA")]
        if ps and min(ps) < 0.10:
            why.append(f"publication bias (p = {min(ps):.2f})")
            short.append("publication bias")
        cert = levels[min(len(why), 3)]
        out.append({"correlate": c, "certainty": cert, "downgrades": len(why), "reasons": "; ".join(why)})
        L.append(f"| {lab(c)} | {p['k_samples']} ({int(float(p['n_total'])):,}) | {ci(p)} | {cert} | "
                 f"{'; '.join(short) or 'none'} |")
    L += ["", "Prediction intervals: Table 2. Start: high certainty, as for prognostic-factor associations from observational studies (Foroutan et al., "
              "2020); one level down for each serious domain. Risk of bias: more than half of the inverse-variance weight "
              "from samples rated no on item 1 (sampling), 3 (validated scale) or 6 (data quality); the share is given in brackets. Inconsistency: 95% PI "
              "crossing zero. Imprecision: 95% CI including both |r| < .10 and |r| > .30. Indirectness: fewer than three "
              "regions or more than 75% student samples. Publication bias (k ≥ 10): Egger-type test or selection model "
              "p < .10. Thresholds set when rating (deviations.md D7)."]
    return L, out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t4, g = grade()
    parts = [table1(), table2(), table3(), t4]
    text = "# Tables\n\nGenerated by `manuscript/make_tables.py` from `forms/` and `analysis/results/`; do not edit by hand.\n\n" \
           + "\n\n".join("\n".join(p) for p in parts) + "\n"
    (HERE / "tables.md").write_text(text, encoding="utf-8", newline="\n")
    with (RES / "grade.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(g[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(g)
    for r in g:
        print(f"{r['correlate']:16s} {r['certainty']:9s} {r['reasons']}")


if __name__ == "__main__":
    main()
