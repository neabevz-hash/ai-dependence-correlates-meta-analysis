"""Group the AI-dependence instruments of the included reports into families (protocol §13, instruments.csv).

Input: extraction/llm/instr_<date>.jsonl (instr_pass.py): every report's instrument name, source citation, items and
subscales. A family is one instrument and its translations and adaptations (e.g., the Turkish DAI is family DAI);
modified or study-specific scales are their own families unless the report says they are the original instrument.
Rules match the source citation first, then the name. Unmatched instruments become study-specific families "ADHOC_<rec_id>".

Writes extraction/instrument_mentions.csv (one row per report x instrument) and prints the families with their counts.
The type T1-T4 is drafted per family later (instrument_types.py) and decided by R1.
Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/instrument_families.py --name instr_2026-10-17
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (family id, label, development reference, pattern on "source citation | name"); first match wins.
FAMILIES = [
    ("DAI", "Dependence on AI scale (Morales-García et al., 2024), 5 items", "10.3389/feduc.2024.1323898",
     r"morales|\bDAI\b|\bDAIS\b|\bDIA\b|YZBÖ|dependencia hacia la inteligencia"),
    ("AICD", "AI Chatbot Dependence Scale (Zhang, Yin et al., 2024), 8 items", "10.1089/cyber.2024.0240",
     r"zhang,? x\.?,? yin|yin m|AICD|chatbot dependen|chatbot addiction scale|sohbet botlar"),
    ("GAIDS", "Generative AI Dependency Scale (Goh, Hartanto & Majeed, 2025), 11 items", "10.1016/j.chbr.2025.100845",
     r"goh|GAIDS|generative a\.?i\.? dependency scale|\bGAD\b"),
    ("PCUS", "Problematic ChatGPT Use Scale (Yu, Chen & Yang, 2024), 11 items", "10.1007/s12144-024-06259-z",
     r"\byu\b.*\b2024\b|yu,? s|PCUS|PCGUS|problematic chatgpt use"),
    ("PUCAI", "Problematic Use of Conversational AI (Hu, Mao & Kim, 2023; adapted Bergen), 6 items", "10.1016/j.chb.2023.107760",
     r"\bhu,? b|hu et al|PUCAI|PGAIU|generative ai addiction \(ga\)"),
    ("ZHANG5", "AI dependency, 5 items (Zhang, Zhao, Zhou & Kim, 2024)", "10.1186/s41239-024-00467-0",
     r"zhang,? s\.?,? zhao|zhang et al\.? \(2024\)|zhang et al \(2024\)|do you have ai dependency"),
    ("HUANG5", "AI dependence, 5 items (Huang et al., 2024, adolescents)", "10.2147/PRBM.S440889",
     r"huang et al|huang \(2024\)"),
    ("ACOSTA5", "AI dependence, 5 items (Acosta-Enriquez et al., 2025)", "10.1016/j.caeai.2025.100381",
     r"acosta"),
    ("AIDEP22", "AI Dependence Scale for Chinese Undergraduates, AIDep-22 (Wu et al., 2026)", "10.3389/fpsyg.2025.1725393",
     r"AIDep|wu et al\.? \(2026\)"),
    ("CAIDS", "Conversational AI Dependence Scale for Chinese college students (Chen et al., 2025)", "10.3389/fpsyg.2025.1621540",
     r"chen et al\.?,? 2025|CAIDS|1621540"),
    ("CAID", "Conversational AI Dependence Scale, CAID (Li, Wang et al., 2026)", "10.1080/10447318.2026.2618563",
     r"\bCAID\b|li,? l\.?,? wang"),
    ("LLMD12", "LLM Dependency scale, LLM-D12", "10.1016/j.ijinfomgt.2025.102888",
     r"LLM-D12|large language model dependency questionnaire|yankouskaya"),
    ("YE_CHATGPT", "ChatGPT dependency (Ye et al., 2024)", "",
     r"\bye,? j|ye et al"),
    ("AIDQ", "Artificial Intelligence Dependence Questionnaire, AIDQ (Akinwale et al., 2025)", "10.38140/ijspsy.v5i3.2106",
     r"akinwale|AIDQ"),
    ("TANG3", "AI dependence, 3 items (Tang et al.)", "",
     r"\btang\b"),
    ("SIRVENT", "Affective dependence, craving items (Sirvent-Ruiz et al., 2022), adapted to AI", "",
     r"sirvent"),
    ("BERGEN_ADAPTED", "Bergen addiction scale adapted to AI (Andreassen et al., 2012), study-specific wording", "",
     r"andreassen|bergen|BSMAS"),
    ("IAT_ADAPTED", "Internet Addiction Test adapted to AI (Young, 1998), study-specific wording", "",
     r"young,? k|young \(1998\)|internet addiction test|AIAT|CIAT"),
    ("CAPINDING", "Students' AI Dependency in 3R's Questionnaire (Capinding, 2024)", "10.18178/ijiet.2024.14.11.2184",
     r"capinding"),
]


# Checked by hand (2026-10-17): mentions the rules put in the wrong family. Value "" = study-specific (ADHOC_*).
OVERRIDES = {
    ("R2459", 1): "BERGEN_ADAPTED",  # 24 items written for the study, adapted from Andreassen et al.
    ("R2320", 1): "",                # DAI-MH, 10 items built for the study
    ("R0345", 1): "",                # 15 items, three subscales, only based on the DAI
    ("R2325", 1): "",                # 7-item reliance scale adapted from the DAI
    ("R2934", 1): "",                # 7 items adapted from the DAI
    ("R1498", 1): "BERGEN_ADAPTED",  # problematic emotional dependence, adapted from Andreassen et al.
    ("R4365", 1): "BERGEN_ADAPTED",  # PACU, adapted from Andreassen et al.
    ("R3627", 1): "",                # GenAIDS developed in this report (media system dependency)
    ("R4323", 1): "",                # 8 items adapted from the smartphone addiction scale SV (Kwon et al.)
    ("R1490", 1): "",                # problematic reliance, 4 items (Du et al., 2026), not Tang et al.
}


def family_of(ins: dict) -> str:
    text = f"{ins['source_citation']} | {ins['name']}"
    for fid, _, _, pat in FAMILIES:
        if re.search(pat, text, re.I):
            return fid
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    rows = []
    for line in (HERE / "llm" / f"{a.name}.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        for j, ins in enumerate(d["codes"]["instruments"], 1):
            fam = OVERRIDES.get((d["conv_id"], j), family_of(ins)) or f"ADHOC_{d['conv_id']}_{j}"
            rows.append({"rec_id": d["conv_id"], "n": j, "family": fam, "name": ins["name"],
                         "source_citation": ins["source_citation"], "n_items": ins["n_items"],
                         "subscales": ins["subscales"], "adapted_from": ins["adapted_from"],
                         "items_location": ins["items_location"], "n_items_printed": len(ins["items"]),
                         "items": " || ".join(ins["items"])})
    with (HERE / "instrument_mentions.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    c = Counter(r["family"] for r in rows if not r["family"].startswith("ADHOC_"))
    for fid, label, _, _ in FAMILIES:
        print(f"{c.get(fid, 0):3d}  {fid:15s} {label}")
    adhoc = [r for r in rows if r["family"].startswith("ADHOC_")]
    print(f"{len(adhoc):3d}  study-specific (ADHOC_*)")
    for r in adhoc:
        print(f"      {r['family']:16s} {r['name'][:70]} | {r['source_citation'][:60]}")


if __name__ == "__main__":
    main()
