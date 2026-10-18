# AI-dependence instruments in the included reports: fixed prompt (protocol §13, "Type of dependence measure")

Role: before effect sizes are extracted, every AI-dependence instrument (and subscale) used in the included reports is typed T1–T4 from its item content (protocol §13). This pass only collects, from each included report, what the instrument is and the item text the report prints. Typing is drafted later, per instrument, and R1 decides. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high), headless Claude Code, one report per call (`instr_pass.py`).

## System prompt

```
You are reading the FULL TEXT of one report included in a meta-analysis of the psychological correlates of DEPENDENCE ON GENERATIVE AND CONVERSATIONAL AI. Your only task: describe the AI-dependence instrument(s) the report used — the measure of dependence on, addiction to, problematic or compulsive use of, over-reliance on, or emotional dependence on an AI system. Do not report correlates or results.

For each AI-dependence instrument (usually one):
- name as the report gives it, and the citation of its development or source paper as printed (authors, year, and DOI if printed);
- number of items, response scale, total score and subscales (names and number of items each);
- what it was adapted from, if the report says so (e.g., Bergen Social Media Addiction Scale, Internet Addiction Test, Smartphone Addiction Scale);
- the item texts the report prints, verbatim, in the language printed (up to 30 items; if more, the first 30). If the report prints no items, say so and leave the list empty;
- the location of the items (table, appendix, page from the "=== Page N ===" markers).

Return only JSON matching the schema. Never invent item texts: copy only what the text shows.
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "instruments": {
      "type": "array",
      "maxItems": 4,
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string", "maxLength": 200},
          "source_citation": {"type": "string", "maxLength": 300},
          "n_items": {"type": "string", "maxLength": 20},
          "response_scale": {"type": "string", "maxLength": 100},
          "subscales": {"type": "string", "maxLength": 400},
          "adapted_from": {"type": "string", "maxLength": 200},
          "items_location": {"type": "string", "maxLength": 100},
          "items": {"type": "array", "maxItems": 30, "items": {"type": "string", "maxLength": 300}}
        },
        "required": ["name", "source_citation", "n_items", "response_scale", "subscales", "adapted_from", "items_location", "items"],
        "additionalProperties": false
      }
    },
    "note": {"type": "string", "maxLength": 300}
  },
  "required": ["instruments", "note"],
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
