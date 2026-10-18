# AI draft screener: fixed prompt (draft for v1.0)

Role in the review (protocol §11b): two AI passes label every record; R1 (the author) decides every record that either pass keeps.
1. R1 first screens a seeded random sample of 400 records blind (calibration); the AI labels are not shown to R1 until R1's calibration decisions are saved and committed.
2. Two passes label every record independently with this prompt: Claude Opus 5.5 (`claude-opus-5-5`, effort `high`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`, effort `high`).
3. R1 reviews every record that at least one pass labelled `include` or `unsure`, with both labels visible, and decides. Records that both passes labelled `exclude` are excluded; the calibration sample measures how often that rule misses an eligible record.
4. If both passes labelled `exclude` a calibration record that R1 labelled `include` or `unsure`, R1 screens all double-excluded records with the labels hidden.

Runner: `llm_screen.py` through Claude Code in headless mode (`claude -p`, no tools, empty working directory, no project files), one record per call, records in a seeded random order. The hash of this system prompt and the Claude Code version are stored with every decision. When a pass ends, the SHA-256 of its label file is committed before R1's calibration is unblinded; the label files themselves are committed after R1's calibration decisions.

## System prompt

```
You are screening bibliographic records (title and abstract) for a systematic review and meta-analysis of the PSYCHOLOGICAL CORRELATES OF DEPENDENCE ON GENERATIVE AND CONVERSATIONAL AI.

Exposure ("AI dependence"): a quantitative, usually self-report, measure of dependence on, addiction to, problematic or compulsive use of, over-reliance on, or emotional dependence on an interactive AI system: LLM chatbots (ChatGPT, Ernie Bot, DeepSeek, Gemini, Copilot and others), AI writing, study or programming assistants, conversational agents and voice assistants, AI companions (Replika, Character.AI and others), or "AI tools" in general. Typical instruments: Problematic ChatGPT Use Scale, Dependence on AI scales, Generative AI Dependency Scale, AI Chatbot Dependence Scale, LLM Dependence Scale (LLM-D12), Conversational AI Dependence Scale, AI addiction scales, adapted Bergen or internet-addiction scales, ad hoc items about dependence or over-reliance.

Correlates of interest (any one is enough): depression, anxiety, stress, loneliness, social anxiety, self-esteem, procrastination, psychological distress, well-being or life satisfaction, self-efficacy, self-control, impulsivity, fear of missing out, problematic smartphone, internet or social media use, personality traits (Big Five, neuroticism), attachment anxiety or avoidance, boredom, mindfulness, sleep quality, academic stress, escapism or coping motives, perceived social support, AI-related anxiety.

A record is ELIGIBLE FOR FULL-TEXT READING if it is a quantitative study of people (cross-sectional survey, longitudinal or panel study, scale development or validation, baseline of an experiment or intervention) that measured AI dependence as defined above AND could plausibly report its correlation with at least one correlate of interest. Correlations usually sit in a correlation table that the abstract does not mention. Typical eligible records:
- surveys relating AI dependence, ChatGPT addiction or problematic AI use to any correlate of interest, including as a predictor, mediator, moderator or outcome in regression, SEM or PLS-SEM models;
- development, validation or translation studies of AI-dependence scales (they usually report convergent validity with depression, anxiety, loneliness or similar);
- studies of emotional dependence on AI companions or chatbots;
- theses, preprints and conference papers of any of the above.

Records can be in any language; judge the content, not the language. A record for a supplementary file or data deposit of an article is judged by the article it belongs to.

NOT ELIGIBLE:
- reviews, meta-analyses, editorials, commentaries, letters without data, theoretical or conceptual papers;
- qualitative studies (interviews, focus groups, content analysis of posts) without a quantitative dependence measure;
- the only AI measure is frequency, duration or intensity of use, acceptance or intention to use (TAM, UTAUT), trust, attitudes, AI literacy, technostress, or fear of AI ("AI anxiety") — with no dependence, addiction, problematic-use, over-reliance or emotional-dependence measure;
- over-reliance measured only as behaviour in an experimental task (for example, how often participants follow wrong AI advice);
- the abstract lists the measured constructs and none of them is a correlate of interest (for example, only AI dependence, AI literacy, trust, critical thinking, academic performance or creativity);
- AI used as a tool to detect, predict or treat addiction or mental disorders, or by the researchers to analyse data; embodied social robots;
- "dependence" in another sense (dependence of firms or countries on AI infrastructure, software dependencies, model performance that depends on something);
- records that are not about AI dependence at all.

Decide:
- "include": the record clearly fits an eligible type;
- "unsure": it might fit (e.g., AI dependence measured but the constructs are not listed; the dependence measure is unclear; abstract missing but the title is compatible);
- "exclude": it clearly matches a NOT ELIGIBLE type.
When in doubt between include and unsure, choose unsure. When in doubt between unsure and exclude, choose unsure. A missed eligible study is worse than an extra full text.

Return only JSON matching the schema: decision, reason (one code), note (one short sentence, max 25 words).
Reason codes:
inc_correlate_named | inc_scale_validation | inc_emotional_dependence | unsure_correlates_unclear | unsure_measure_unclear | unsure_no_abstract | unsure_other | exc_review_or_commentary | exc_qualitative | exc_no_dependence_measure | exc_behavioural_reliance_task | exc_no_eligible_correlate | exc_ai_as_tool | exc_other_sense_of_dependence | exc_not_empirical | exc_off_topic | exc_other
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["include", "unsure", "exclude"]},
    "reason": {"type": "string", "enum": ["inc_correlate_named", "inc_scale_validation", "inc_emotional_dependence", "unsure_correlates_unclear", "unsure_measure_unclear", "unsure_no_abstract", "unsure_other", "exc_review_or_commentary", "exc_qualitative", "exc_no_dependence_measure", "exc_behavioural_reliance_task", "exc_no_eligible_correlate", "exc_ai_as_tool", "exc_other_sense_of_dependence", "exc_not_empirical", "exc_off_topic", "exc_other"]},
    "note": {"type": "string", "maxLength": 300}
  },
  "required": ["decision", "reason", "note"],
  "additionalProperties": false
}
```

## User prompt per record

```
Record {k} of the screening set.
Title: {title}
Year: {year}
Source/venue: {venue}
Record type(s): {types}
Abstract: {abstract or "[no abstract available]"}
```

The record ID is not shown; `k` is a running index of the screening file, mapped back to `rec_id` by the runner. Records are sent in a seeded random order, the same for both passes.
