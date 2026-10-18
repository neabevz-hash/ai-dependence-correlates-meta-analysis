# Supplementary File S4. Use of an AI assistant

Claude Opus 5.5 (`claude-opus-5-5`) and, for the second screening pass, Claude Sonnet 5.5 (`claude-sonnet-5-5`), both at reasoning effort high, ran through Claude Code in headless mode (`claude -p`) with a fixed system prompt, a JSON output schema and no tools; one item per call. Every output is stored with the hash of the system prompt and of the rendered prompt, the model actually used and the Claude Code version. Every label, proposal, type, extracted value and rating was a draft that the reviewer (R1) accepted or corrected.

| Task | Prompt | Items | Run (UTC) | System prompt SHA-256 (first 16) | Claude Code | Models used |
| --- | --- | --- | --- | --- | --- | --- |
| Title and abstract labels, pass 1 | `screening/llm_screener_prompt.md` | 5,056 | 2026-10-16 15:15 to 2026-10-17 05:05 | a90854b93adad579 | 2.1.289 | claude-opus-5-5 |
| Title and abstract labels, pass 2 | `screening/llm_screener_prompt.md` | 5,056 | 2026-10-16 15:15 to 2026-10-17 05:08 | a90854b93adad579 | 2.1.289 | claude-sonnet-5-5 |
| Full-text proposals | `fulltext/ft_prompt.md (tag ai-dependence-ft-prompt-v1.0)` | 451 | 2026-10-17 06:52 to 2026-10-17 10:00 | ac4d1f68d61cbe3c | 2.1.289 | claude-opus-5-5 |
| Full-text proposals, citation searching | `fulltext/ft_prompt.md (same)` | 22 | 2026-10-17 10:55 to 2026-10-17 10:55 | ac4d1f68d61cbe3c | 2.1.289 | claude-opus-5-5 |
| Full-text proposal, late retrieval (D3) | `fulltext/ft_prompt.md (same)` | 1 | 2026-10-17 10:55 to 2026-10-17 10:55 | ac4d1f68d61cbe3c | 2.1.289 | claude-opus-5-5 |
| Instruments of the included reports | `extraction/instr_prompt.md` | 124 | 2026-10-17 10:57 to 2026-10-17 11:00 | 2ff14de2b089022c | 2.1.289 | claude-opus-5-5 |
| Instrument types (drafts) | `extraction/instrument_types.py (system prompt in the script)` | 67 | 2026-10-17 11:04 to 2026-10-17 11:07 | c56ca437242a6a89 | 2.1.289 | claude-opus-5-5 |
| Extraction and risk-of-bias drafts | `extraction/extract_prompt.md (tag ai-dependence-extraction-prompt-v1.0)` | 121 | 2026-10-17 11:32 to 2026-10-17 18:54 | e61d8dd366b7f26b | 2.1.289 | claude-opus-5-5 |

## Agreement with the reviewer

- Title and abstract, blind calibration sample (n = 400, labels hidden from R1): the rule "full text unless both passes exclude" had sensitivity 0.91 (95% CI 0.82–0.97), specificity 0.97 (0.95–0.99), κ 0.87, Gwet's AC1 0.95. It missed 6 records R1 marked unsure and none marked include; the safeguard was triggered, and R1 screened all double exclusions blind (3,834 records; 252 returned to full text).
- Verification with labels shown: 822 records kept by at least one pass; R1 accepted the AI label for 641 and excluded 64.
- Full text: R1 accepted the AI proposal for 429 of 449 reports; no report changed from eligible to not eligible or back.
- Extraction: R1 verified 6,984 drafted values (124 samples, 334 effects) and corrected 1 (1 of 3,168 key values); effects added by R1: 0.
- Supporting quotes found verbatim in the source by script: 332 of 334 for effects and 466 of 485 for key sample fields (`extraction/quote_check.py`).
