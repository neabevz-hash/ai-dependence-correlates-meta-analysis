# Supplementary File S1. Search strategies (PRISMA-S)

Final search started 2026-10-16T14:52:07Z, after the protocol was deposited (Zenodo, 10.5281/zenodo.23420672). No date, language or publication-type limits. Code: `search/search.py`; every query exactly as run, with its count, is in `search/runs/2026-10-16/search_log.json` of the data release.

| Source | Interface and query form | Searched (UTC) | Queries | Records |
| --- | --- | --- | --- | --- |
| PubMed | NCBI E-utilities; phrase pairs within three words in title or abstract ([tiab:~3]) | 2026-10-16 14:52 | 7 | 346 |
| Europe PMC | REST API, searchPOST, TITLE_ABS phrases | 2026-10-16 14:52 | 15 | 281 |
| OpenAlex | API, title_and_abstract.search, phrases joined by OR | 2026-10-16 14:53 | 15 | 3,925 |
| OpenAlex, other languages | API, title_and_abstract.search, Chinese, Spanish, Portuguese, Turkish, Korean, Japanese, Russian and other phrases | 2026-10-16 14:53 | 26 | 69 |
| Semantic Scholar | Graph API, bulk search, phrases joined by the OR operator (pipe) | 2026-10-16 14:59 | 20 | 2,113 |
| Crossref | REST API, query.bibliographic, sorted by relevance (offset), records kept only with the phrase in title or abstract | 2026-10-16 15:01 | 18 | 1,168 |
| DataCite | REST API, titles and descriptions | 2026-10-16 15:01 | 15 | 1,632 |
| OpenAIRE Graph | API, research products of type publication, at most four OR operators per query | 2026-10-16 15:02 | 5 | 1,001 |
| CORE | API v3, title or abstract, one query per phrase; early stop at a page of 100 with fewer than five phrase matches | 2026-10-16 15:13 | 24 | 444 |
| Instrument citations | OpenAlex, works citing the development papers of 7 instruments | 2026-10-16 15:13 | 7 | 400 |

## Phrase sets

**AI terms (21):** AI; artificial intelligence; ChatGPT; GenAI; generative AI; generative artificial intelligence; chatbot; chatbots; AI chatbots; conversational agent; conversational agents; conversational AI; LLM; LLMs; large language model; large language models; AI companion; AI companions; AI tools; AI technology; Replika.

**Dependence forms (19), with {a} for each AI term:** {a} addiction; {a} dependence; {a} dependency; dependence on {a}; dependency on {a}; addiction to {a}; problematic {a} use; problematic use of {a}; excessive {a} use; excessive use of {a}; compulsive {a} use; compulsive use of {a}; addictive {a} use; addictive use of {a}; {a} use disorder; problematic {a} usage; excessive {a} usage; compulsive {a} usage; addictive {a} usage.

**Over-reliance forms (6):** overreliance on {a}; over-reliance on {a}; {a} overreliance; {a} over-reliance; {a} overuse; overuse of {a}. Over-reliance phrases were kept only with a measurement word in the title or abstract: scale, questionnaire, survey, inventory, respondents, self-report.

Distinct phrases after removing duplicates: 399 dependence and 126 over-reliance (525 in all).

**AI companions (Boolean):** ("AI friend" OR "AI friends" OR "AI friendship" OR "AI companion" OR "AI companions" OR "social chatbot" OR "social chatbots" OR "companion chatbot" OR "companion chatbots" OR "Replika" OR "Character.AI" OR "Xiaoice" OR "AI girlfriend" OR "AI boyfriend") AND (addiction OR addicted OR addictive OR dependence OR dependency OR compulsive OR problematic).

**PubMed proximity pairs:** each of AI; artificial intelligence; ChatGPT; GenAI; generative AI; chatbot; chatbots; conversational agent; conversational agents; LLM; large language model; large language models; AI companion; AI companions; Replika with each of addiction; dependence; dependency; addictive; problematic use; compulsive use; excessive use; problematic usage; compulsive usage; excessive usage within three words ([tiab:~3]).

**Crossref queries:** AI dependence; AI dependency; AI addiction; ChatGPT addiction; ChatGPT dependence; problematic ChatGPT use; problematic AI use; generative AI dependence; generative AI addiction; chatbot addiction; chatbot dependence; artificial intelligence dependence; artificial intelligence addiction; dependence on artificial intelligence; AI companion dependence; emotional dependence on AI; large language model dependence; conversational AI dependence.

**CORE and OpenAIRE phrases:** AI dependence; AI dependency; AI addiction; artificial intelligence dependence; artificial intelligence addiction; ChatGPT addiction; ChatGPT dependence; ChatGPT dependency; problematic ChatGPT use; problematic AI use; problematic use of AI; generative AI addiction; generative AI dependence; chatbot addiction; chatbot dependence; dependence on AI; dependence on ChatGPT; addiction to AI; AI companion addiction; emotional dependence on AI; conversational AI dependence; LLM dependence; large language model dependence; AI use disorder.

**Instrument papers (citing works through OpenAlex):** Dependence on AI, university students (Morales-García et al., 2024) (10.3389/feduc.2024.1323898; 140 citing); Problematic ChatGPT Use Scale (Yu et al., 2024) (10.1007/s12144-024-06259-z; 63 citing); Generative AI Dependency Scale (Goh et al., 2025) (10.1016/j.chbr.2025.100845; 58 citing); AI Chatbot Dependence Scale (Zhang et al., 2025) (10.1089/cyber.2024.0240; 52 citing); LLM Dependence Scale (Li et al., 2025) (10.1016/j.ijinfomgt.2025.102888; 40 citing); Conversational AI Dependence Scale (Chen et al., 2025) (10.3389/fpsyg.2025.1621540; 24 citing); AI dependence scale, Chinese undergraduates (Wu et al., 2026) (10.3389/fpsyg.2025.1725393; 23 citing).

## De-duplication and recall

- Records retrieved: 11,379; unique: 5,260; duplicates removed: 6,119 (of which 961 pointer or component records attached to their database record).
- Removed automatically as non-study records (datasets, peer-review reports, paratext, software, registrations or figures as typed by the source): 204. Records screened: 5,056.
- Recall on the seed set (the 37 empirical studies of Dagnino et al., 2026): 35 of 37; not found: Zhang Y. et al. (2025); Biswas and Murray (2024) (no quantitative measure of AI dependence).

## Citation searching (deviations.md, D2)

Run on 2026-10-17 10:43 UTC through OpenAlex (`search/citation_chase.py`); seeds: the 124 included reports and seven reviews; 131 found in OpenAlex.
- Backward: 3,003 cited works, 168 already in the record set. Forward: 1,379 citing links, 622 already in the set.
- New records: 3,523; with an AI term within 60 characters of a dependence term in the title or abstract: 33 (assessed at full text); included: 0.
