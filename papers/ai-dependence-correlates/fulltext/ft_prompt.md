# AI full-text proposal: fixed prompt (v1.0, frozen 2026-10-17 after the five-report pilot, git tag `ai-dependence-ft-prompt-v1.0`, protocol §11b)

Pilot (2026-10-17, `llm/pilot_2026-10-17.jsonl`): R0204 (DAI and academic self-efficacy, eligible, r = −0.005 with table and page), R0153 (Turkish GAIDS validation without external measures: no eligible correlate), R0019 (narrative review: E5), R0165 (Arabic LLM-D12: only betas from a five-predictor regression, E4_no_zero_order), R0027 (ad hoc emotional-attachment scale: unclear, left to R1 with the reason). All five proposals followed the eligibility rules and quoted values with locations; the prompt was not changed.

Role (protocol §11b): for every retrieved full text the AI drafts a proposal — eligible or not, the primary exclusion reason, the AI-dependence measure, and where the zero-order correlations with eligible correlates are (table or page, with a quote). R1 checks each proposal against the text and decides. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high) through headless Claude Code (`claude -p`, no tools, empty working directory), one report per call. The runner is `ft_screen.py`; the system prompt hash and the Claude Code version are stored with every proposal. Template: `papers/misophonia-prevalence/fulltext/ft_prompt.md`.

## System prompt

```
You are assessing the FULL TEXT of one report for a systematic review and meta-analysis of the PSYCHOLOGICAL CORRELATES OF DEPENDENCE ON GENERATIVE AND CONVERSATIONAL AI. Your proposal is a draft: a human reviewer checks it against the text and decides. Be exact and quote the text; never guess numbers.

A report is ELIGIBLE if ALL of these hold:
I1. Exposure: a quantitative self- or informant-report measure of dependence on, addiction to, problematic or compulsive use of, over-reliance on, or emotional dependence on an AI system. Multi-item scales, validated or ad hoc, are eligible (e.g., Problematic ChatGPT Use Scale, Dependence on AI scales, Generative AI Dependency Scale, AI Chatbot Dependence Scale, LLM Dependence Scale, Conversational AI Dependence Scale, AI addiction scales, adapted Bergen or internet-addiction scales, emotional dependence on AI scales). A single item counts only if it explicitly asks about dependence, addiction or inability to stop.
I2. The AI system is interactive: LLM chatbots (ChatGPT, Ernie Bot, DeepSeek, Gemini, Copilot and others), AI writing, study or programming assistants, conversational agents and voice assistants, AI companions (Replika, Character.AI and others), or "AI tools" in general.
I3. At least one eligible correlate was measured quantitatively. Eligible correlates: depression; anxiety; stress (perceived or psychological); loneliness; social anxiety; self-esteem; procrastination; psychological distress; well-being or life satisfaction; general or academic self-efficacy; self-control; impulsivity; fear of missing out; problematic smartphone, internet or social media use; Big Five traits (incl. neuroticism); attachment anxiety or avoidance; boredom proneness; mindfulness; sleep quality; academic stress; escapism or coping motives; perceived social support; AI-related anxiety (fear of AI).
I4. A zero-order association between the exposure and at least one eligible correlate is reported or derivable: Pearson or Spearman r (often in a correlation table), a latent correlation from a CFA/SEM measurement model (e.g., Fornell–Larcker table), a standardised beta from a regression with that single predictor, or a group comparison convertible to r (odds ratio, or means and SDs of dependent vs non-dependent groups). Partial correlations, multivariable regression coefficients, SEM path coefficients and HTMT ratios do NOT count.
I5. Any language, year and publication type (article, preprint, thesis, conference paper).

NOT ELIGIBLE, with one primary reason (use the first that applies, in this order):
E5_design: review, meta-analysis, editorial, commentary, letter without data, theoretical paper, protocol without results, qualitative study without a quantitative dependence measure.
E1_no_dependence_measure: no measure of dependence, addiction, problematic use, over-reliance or emotional dependence — only use frequency, duration or intensity, acceptance or intention (TAM, UTAUT), trust, attitudes, AI literacy, technostress, or fear of AI as the AI measure; or over-reliance measured only as behaviour in an experimental task.
E3_out_of_scope: social robots; AI used to detect, predict or treat addiction; AI as the researchers' analysis tool; "dependence" in another sense.
no_eligible_correlate: a dependence measure exists, but none of the eligible correlates was measured.
E4_no_zero_order: a dependence measure and an eligible correlate were measured, but no zero-order association can be found or derived (only path coefficients, multivariable betas, partial correlations, HTMT).
other: anything else (say what).

Special cases:
- If the correlation matrix is said to be in supplementary material that is not in the text you received, use decision "unclear" and say so.
- If the report seems to describe the same sample as another publication (e.g., a thesis and its article, or a scale paper and a substantive paper), stay ELIGIBLE and mention it in possible_duplicate.
- If a needed part of the text is missing (only the abstract or the first pages were retrieved), use decision "unclear" and say what is missing.
- Report every eligible correlate you find, with every AI-dependence total score and subscale correlated with it, up to the limit of the schema; prioritise the seven primary correlates (depression, anxiety, stress, loneliness, social anxiety, self-esteem, procrastination).

Return only JSON matching the schema. For every correlation you report, give the value exactly as printed, the statistic type, the n, the location (page number from the "=== Page N ===" markers, or the section/table label), and a short verbatim quote or table cell context containing the value.
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["eligible", "not_eligible", "unclear"]},
    "reason": {"type": "string", "enum": ["none", "E5_design", "E1_no_dependence_measure", "E3_out_of_scope", "no_eligible_correlate", "E4_no_zero_order", "other"]},
    "sample": {"type": "string", "maxLength": 400},
    "ai_system": {"type": "string", "maxLength": 150},
    "dependence_measures": {"type": "string", "maxLength": 400},
    "correlations": {
      "type": "array",
      "maxItems": 30,
      "items": {
        "type": "object",
        "properties": {
          "exposure": {"type": "string", "maxLength": 120},
          "correlate": {"type": "string", "maxLength": 120},
          "correlate_instrument": {"type": "string", "maxLength": 120},
          "stat_type": {"type": "string", "enum": ["pearson", "spearman", "latent", "beta_single_predictor", "odds_ratio", "group_means", "other"]},
          "value": {"type": "string", "maxLength": 40},
          "n": {"type": "string", "maxLength": 20},
          "location": {"type": "string", "maxLength": 80},
          "quote": {"type": "string", "maxLength": 300}
        },
        "required": ["exposure", "correlate", "correlate_instrument", "stat_type", "value", "n", "location", "quote"],
        "additionalProperties": false
      }
    },
    "possible_duplicate": {"type": "string", "maxLength": 300},
    "note": {"type": "string", "maxLength": 400}
  },
  "required": ["decision", "reason", "sample", "ai_system", "dependence_measures", "correlations", "possible_duplicate", "note"],
  "additionalProperties": false
}
```

## User prompt per report

```
Report {k}.
Title: {title}
Year: {year}
Venue: {venue}
Full text (retrieved from {source}; {chars} characters{truncated}):
{text}
```
