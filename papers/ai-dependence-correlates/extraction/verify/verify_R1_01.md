# Проверка выписывания — файл 1 из 13

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

---

## ST001 · 3 2026 · Zenodo (CERN European Organization for Nuclear Research)

Основной отчёт R0027: [текст](../../fulltext/text/R0027.txt) · [PDF](../../fulltext/pdf/R0027.pdf) — «TALKING TO MACHINES: A CORRELATIONAL STUDY OF EXTRAVERSION AND EMOTIONAL ATTACHMENT TO AI CHATBOTS» — [DOI](https://doi.org/10.5281/zenodo.21992284)
Расхождения в тексте: The Results cite 'Table 1', but no table appears in the full text, so the correlation comes from the text. The abstract uses the future tense ('The collected data will be analyzed'), although results are reported. The keywords (AI Dependency, Academic Performance, Technostress) and the review of literature do not match the study topic (extraversion and AI attachment). Section 3.2 calls the sample 'large', but n = 63. The ethics statement says the study 'did not involve human/animal subjects' and that 'informed written consent was obtained', which contradicts the anonymous online Google Forms procedure.
Заметка ИИ: There is one effect: emotional attachment to AI chatbots (ad hoc 15-item scale) with BFI extraversion, Pearson r = .22, n = 63. No reliability coefficients are reported for either measure.

### ST001-1 · Undergraduate AI-chatbot users aged 18-25, recruited online (Instagram/Discord), presumably India (Bangalore authors), n=63
Отчёты: R0027 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0027_1 · total (T3) | **extraversion** · Big Five Inventory (BFI) Extraversion, 8 selected items | pearson | **.22** | **63** | 1 | Page 12, Results | «The analysis revealed a weak positive correlation between participants’ extraversion scores and their emotional attachment scores toward AI chatbots, r (61) = .22, p > .05.» |

- E1: заметка: Value from the text; Table 1 is cited but not reproduced in the full text. df = 61 is consistent with n = 63. Exact p not reported.

**Ключевые поля выборки:**
- **n_analysed: 63** — Page 9, 3.1 Participants; Page 12, Results — «A total of 63 participants participated in the study.»
- **population: university_students** — Page 9, 3.1 Participants — «Participants were recruited from colleges, specifically undergraduate students.»
- **sampling: convenience** — Page 9, 3.1 Participants — «They were selected using convenience sampling through digital platforms like social media, such as Instagram and Discord»
- **ai_system: general_chatbot** — Page 9, 3.1 Participants — «who had previous experience interacting with AI chatbots for different purposes»

**Остальные поля:**
- country: NR — Page 1, Affiliation; Page 9, 3.1 Participants — «Student, B.Sc Psychology, St. Claret College, Bangalore»
- data_years: NR — Page 9-11, Methodology — «A total of 63 participants participated in the study.»
- design: cross-sectional — Page 10, 3.2 Research Design — «This study uses a quantitative, cross-sectional research design to explore the relationship between extraversion and emotional attachment to AI chatbots.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 9, 3.1 Participants — «The study included young adults aged 18 to 25 years»
- age_sd: NR — Page 9, 3.1 Participants — «The study included young adults aged 18 to 25 years»
- age_min: 18 (inclusion criterion) — Page 9, 3.1 Participants — «1. Aged between 18 and 25 years»
- age_max: 25 (inclusion criterion) — Page 9, 3.1 Participants — «1. Aged between 18 and 25 years»
- pct_female: NR — Methodology — «A total of 63 participants participated in the study.»
- mode: online — Page 11, 3.4 Instrumentation — «The questionnaire was distributed through Google Forms»
- attention_checks: NR — Page 11, 3.5 Procedure — «They were instructed to answer honestly based on their experiences with AI chatbots.»
- pub_status: journal — Page 1, How to Cite — «Seshadripuram Journal of Social Sciences (SJSS), 7(1), 222–236.»
- language: English — Full text — «Ability to understand and complete an English-language questionnaire»
- funding_coi: No specific grant; authors declare no conflict of interest — Page 13, Funding statements; Conflict of Interest Statement — «This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors ... The authors declare no conflict of in…»
- notes: Participant country not stated; authors are at St. Claret College, Bangalore (India likely, but recruitment was via Instagram/Discord, so country left NR). Age range is from the inclusion criteria only; no descriptives of age or gender given. The exposure is a 15-item study-specific 'Emotional Attachment to AI Scale' (Part B) covering emotional reliance, comfort and perceived connection; no reliability or validation reported. Descriptives: Extraversion M = 25.32, SD = 5.66; Attachment M = 38.90, SD = 11.46. Table 1 is cited but not included in the full text.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited through social media. — Page 9, 3.1 Participants — «They were selected using convenience sampling through digital platforms like social media, such as Instagram and Discord»
2. отклик: **unclear** — Response rate not reported (open online link). — Page 11, 3.5 Procedure — «The questionnaire was shared online through digital platforms like social media.»
3. валидная шкала зависимости от ИИ: **no** — Study-specific 15-item scale. No source instrument is cited and no psychometric evidence is reported. The items are said to reflect the dimensions of Sandeeshwara & Hartanto's AI Attachment Scale, but the paper does not… — Page 11, 3.4 Instrumentation — «Emotional Attachment to AI Scale: This section evaluated the level of emotional attachment participants feel toward AI chatbots. It contained items related to …»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega reported for the attachment scale. — Page 11-12, Instrumentation and Results — «the mean emotional attachment score was M = 38.90, SD = 11.46.»
5. валидные шкалы коррелятов: **yes** — Extraversion was measured with items from the published BFI. Only 'relevant items' were selected; the 8 items match the length of the BFI extraversion subscale, but the reviewer should check whether the subscale was mod… — Page 11, 3.4 Instrumentation — «Items assessing extraversion were taken from the Big Five Inventory, with only relevant items selected for this study. Therefore, the extraversion section incl…»
6. качество данных: **unclear** — No attention checks or screening for invalid responses reported. — Page 11, 3.5 Procedure — «They were instructed to answer honestly based on their experiences with AI chatbots.»

Правки:
- 

Проверено: да

---

## ST002 · Akinwale 2026 · International Journal of Studies in Psychology

Основной отчёт R0111: [текст](../../fulltext/text/R0111.txt) · [PDF](../../fulltext/pdf/R0111.pdf) — «Exploring the relationship between artificial intelligence dependency and academic outcomes: Roles of academic self-efficacy and motivation among final year st…» — [DOI](https://doi.org/10.66434/ijspsy.v6i2.520)
Расхождения в тексте: (1) Sampling and setting: the abstract says stratified random sampling at 'selected universities in Lagos', but the Methods describe final-year undergraduates from the University of Lagos only. (2) AIDQ is described as 13 items and then as 12 items. (3) Correlate instrument sources: the Methods cite Chemers et al. (2001) for academic self-efficacy and Vallerand et al. (1993) for the AMS, while the Discussion cites Nielsen et al. (2018) and Stover et al. (2012). (4) Table 1 marks r = -.107 with '*', but its footnote uses '**' with 'significant at the 0.05 level'. (5) Age categories in the instrument section (16-20, 21-25, 26-30, 31+) differ from those reported for the sample (20-22, 23-25, 26+). (6) The moderation text has F(1, 562), which does not fit n=400. The R² values in the text (.068, .027; ΔR² .039) do not match the tables (R² .0207/.198; ΔR² .0061/.0072). The text calls age 'sig…
Заметка ИИ: One sample and one eligible effect: AIDQ total × academic self-efficacy, r = -.107. The AIDQ–academic motivation correlation (r = .436) was not extracted because academic motivation has no key in the construct dictionary. Regression coefficients were not extracted.

### ST002-1 · University of Lagos final-year undergraduates, Nigeria, n=400
Отчёты: R0111 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AIDQ · total (T2) | **self_efficacy** · Academic Self-Efficacy Scale (Chemers et al., 2001) | pearson | **-.107** | **400** | 1 | Page 4, Table 1 | «1 Ai Dependency 43.25 4.66 1 / 2 Academic Self-Efficacy 22.97 3.04 -.107* 1» |

- E1: заметка: Table gives no n; n=400 assumed from total participants. AIDQ alpha .85 is from a pilot, not this sample. The Discussion names the ASE source as Nielsen et al. (2018), not Chemers et al. (2001).

**Ключевые поля выборки:**
- **n_analysed: 400** — Pages 3-4, Research site; Table 1 gives no n — «A total of 400 final year undergraduate students participated in the study.»
- **population: university_students** — Page 3, Research site — «A total of 400 final year undergraduate students participated in the study.»
- **sampling: probability** — Page 1, Abstract — «A cross-sectional survey design was used to collect data from 400 undergraduates through stratified random sampling at the selected universities in Lagos, Nigeria»
- **ai_system: ai_unspecified** — Page 1, Abstract; Page 4, AI dependency questionnaire — «This study examined the relationship between dependency on AI, academic motivation, and academic self-efficacy among undergraduate students»

**Остальные поля:**
- country: NGA — Page 3, Research site — «This study was conducted at the University of Lagos, located in the south-west region of Nigeria.»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 3, Research design — «A cross-sectional research design was deemed the most suitable method for this research»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 4, Research site — «Age of respondent: 20 - 22 years, 117 (29.3%); 23 - 25 years, 193 (48.3%); and 26 years and above, 90 (22.4%).»
- age_sd: NR — NA — «NR»
- age_min: 20 (lowest reported age category 20-22 years) — Page 4, Research site — «Age of respondent: 20 - 22 years, 117 (29.3%)»
- age_max: NR (open top category: 26 years and above) — Page 4, Research site — «and 26 years and above, 90 (22.4%)»
- pct_female: 56.0 — Page 4, Research site — «Sex of respondents: Male, 176 (44.0%), and female, 224 (56.0%).»
- mode: NR — Page 4, Procedure — «Primary consent was obtained from all respondents, who signed consent forms to participate in the research.»
- attention_checks: NR — Page 4, Procedure — «Respondents were also encouraged to be honest in their responses.»
- pub_status: journal — Page 1, header — «International Journal of Studies in Psychology ... Vol. 6, No. 2, pp. 24-31.»
- language: English — Full text — «Exploring the relationship between artificial intelligence dependency and academic outcomes»
- funding_coi: Funding NR; authors declare no conflicts of interest — Page 6, XI. Conflict of interest — «There are no conflicts of interest in this article.»
- notes: Abstract claims stratified random sampling at 'selected universities in Lagos', while Methods describe recruiting only final-year undergraduates from the University of Lagos and give no sampling procedure. The AIDQ is described as having both 13 and 12 items. Reliability (alpha .85) comes from a pilot study only, not this sample. Academic motivation (AMS total) was also correlated with AIDQ (r = .436) but has no key in the construct dictionary, so it was not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Only the abstract says 'stratified random sampling'. The Methods describe no sampling frame or procedure and mention one university, not several, so we can't tell whether this was a true probability sample. — Page 1 Abstract; Page 4 Procedure — «The researchers recruited only final year undergraduates from the University of Lagos, Nigeria, to participate in the study.»
2. отклик: **unclear** — Response rate not reported. — Page 3, Research site — «A total of 400 final year undergraduate students participated in the study.»
3. валидная шкала зависимости от ИИ: **yes** — AIDQ has a published development/validation study (Akinwale et al., 2025, IJSPSY 5(3)). — Page 4, AI dependency questionnaire; Page 6, References — «Akinwale, G. A., Ojakorotu, V., & Oloko, T. O. (2025). Developing and validating an Artificial Intelligence Dependence Questionnaire (AIDQ) for undergraduate s…»
4. надёжность шкалы ИИ в выборке: **unclear** — Alpha reported only for a pilot study, not for the analysed sample. — Page 4, AI dependency questionnaire — «A pilot study was conducted to assess the reliability of the AI dependency questionnaire, yielding a Cronbach's alpha of 0.85»
5. валидные шкалы коррелятов: **yes** — Academic self-efficacy measured with a published scale (Chemers et al., 2001). The Discussion names a different source (Nielsen et al., 2018), but both are published instruments. — Page 4, Academic self-efficacy scale — «measured using the Academic Self-Efficacy Scale, developed and validated by Chemers et al. (2001).»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported. — Page 4, Procedure — «Respondents were also encouraged to be honest in their responses.»

Правки:
- 

Проверено: да

---

## ST003 · Antogop 2026 · International Journal of Research and Innovation in Social Science

Основной отчёт R0204: [текст](../../fulltext/text/R0204.txt) · [PDF](../../fulltext/pdf/R0204.pdf) — «Exploring the Relationship Between Self-Efficacy, Digital Competence, and AI Dependence among Senior College Students in a Private University in Cebu, Philippi…» — [DOI](https://doi.org/10.47772/ijriss.2026.100300483)
Расхождения в тексте: The text (p. 14) and Table 15 agree: r = -0.005, p = 0.926. Two oddities: the DAI reliability is printed as 'α and ω=87', which is presumably .87, and it does not say which sample it comes from. The paper calls r = 0.444 between self-efficacy and digital competence 'weak'; that is a label only, not an inconsistency in the data. There are no figures with coefficients.
Заметка ИИ: The draft has one sample and one eligible effect: DAI total with academic self-efficacy (SSE). The reviewer should check whether 'universal sampling' counts as a census for rob_1, and whether the reliabilities reported come from this sample.

### ST003-1 · Senior College of Teacher Education students, private university, Cebu, Philippines (n=320)
Отчёты: R0204 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **self_efficacy** · Student Self-Efficacy (SSE) Scale (self-efficacy in academi… | pearson | **-0.005** | **320** | 1 | Table 15, Page 15 | «Self-efficacy and Dependence on Artificial Intelligence / -0.005 / Negligible Negative 0.926 / Do not reject Ho / Not Significant» |

- E1: заметка: p = 0.926 (two-tailed). The alphas in the methods (SSE 0.84; DAI .87) seem to come from the instruments' sources, not this sample, so they are recorded as NR.

**Ключевые поля выборки:**
- **n_analysed: 320** — Page 3; Table 1 (Page 4) — «a total of 320 respondents answered the survey questionnaires»
- **population: university_students** — Pages 2-3, Respondents of the Study — «The respondents of this study are the senior college students in a private university in Cebu, Philippines specifically from the College of Teacher Education»
- **sampling: census** — Page 3, Respondents of the Study — «Using the universal sampling, a total of 320 respondents answered the survey questionnaires from the different programs.»
- **ai_system: ai_unspecified** — Table 13, Page 13 — «I feel unprotected when I do not have access to AI. ... I constantly need validation or feedback from AI systems to feel confident in my decisions.»

**Остальные поля:**
- country: PHL — Page 1, Abstract — «senior college students in a private university in Cebu, Philippines, during the academic year 2024–2025»
- data_years: 2024-2025 (academic year; exact months NR) — Page 2, Research Design — «senior college students in a private university in Cebu, Philippines, during the academic year 2024-2025»
- design: cross-sectional — Page 4, Scope and Limitations — «the cross-sectional research design limits the ability to establish causal relationships, as data were collected at a single point in time»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1, Page 4 — «Age (in years) ... 26 and above | 23-25 | 20-22»
- age_sd: NR — Table 1, Page 4 — «Age (in years) ... 26 and above | 23-25 | 20-22»
- age_min: NR (lowest age category reported: 20-22) — Table 1, Page 4 — «20-22 | 174 | 54.38 | 42 | 13.13 | 216 | 67.50»
- age_max: NR (highest age category: 26 and above) — Table 1, Page 4 — «26 and above | 6 | 1.88 | 1 | 0.31 | 7 | 2.19»
- pct_female: 78.75 — Table 1, Page 4 — «most of the respondents are females constituting 252 or 78.75%, while males account for only 68 or 21.25%»
- mode: paper — Page 3, Research Instrument — «the survey questionnaires were distributed, along with clear instructions on how to answer them... the researchers then reviewed the submitted questionnaires e…»
- attention_checks: NR — Page 3, Research Instrument — «the researchers then reviewed the submitted questionnaires ensuring all parts are complete»
- pub_status: journal — Page 1, header — «INTERNATIONAL JOURNAL OF RESEARCH AND INNOVATION IN SOCIAL SCIENCE (IJRISS) ISSN No. 2454-6186»
- language: English — Full text — «Exploring the Relationship Between Self-Efficacy, Digital Competence, and AI Dependence among Senior College Students»
- funding_coi: Funding NR; authors declare no conflict of interest — Page 16, Conflict of Interest — «The researchers disclose and confirm that there is no occurrence of conflict of interest in the conduct of this study.»
- notes: Single sample of 320 senior College of Teacher Education students. The paper calls the sampling 'universal sampling' (a census), but it gives no number of eligible students and no response rate. Paper questionnaires were handed out in class (mode coded 'paper' by inference). The reliabilities in the methods (SSE alpha = 0.84; DAI 'α and ω=87') seem to be values from the instruments' sources, not from this sample. Age is given only in categories. Digital competence (SDiCoS) is also correlated with self-efficacy, but it is not an AI-dependence pair and fits no dictionary key, so it was not extr…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **yes** — Described as universal sampling (census) of senior College of Teacher Education students in AY 2024-2025. The number eligible is not given, so the reviewer should check whether this counts as a true census. — Page 3, Respondents of the Study — «Using the universal sampling, a total of 320 respondents answered the survey questionnaires from the different programs.»
2. отклик: **unclear** — No response rate or eligible population size reported; no comparison of non-responders. — Page 3, Respondents of the Study — «a total of 320 respondents answered the survey questionnaires»
3. валидная шкала зависимости от ИИ: **yes** — The paper uses the published Dependence on Artificial Intelligence (DAI) Scale and calls it a standardized instrument with reported internal consistency. Its development study is not cited in the reference list. — Page 3, Research Instrument — «adopted standardized instruments namely: ... Dependence on Artificial Intelligence (DAI) Scale with internal consistency (α and ω=87)»
4. надёжность шкалы ИИ в выборке: **unclear** — The reported α/ω (.87) seems to describe the instrument in general, not this sample. No reliability is reported for this sample. — Page 3, Research Instrument — «Dependence on Artificial Intelligence (DAI) Scale with internal consistency (α and ω=87)»
5. валидные шкалы коррелятов: **yes** — Self-efficacy was measured with the named Student Self-Efficacy (SSE) Scale, described as a standardized instrument. No citation is given in the references. — Page 3, Research Instrument — «adopted standardized instruments namely: Student Self-Efficacy (SSE) Scale with an internal consistency of α = 0.84»
6. качество данных: **unclear** — Only a completeness check of the returned questionnaires is described. There were no attention checks, no careless-responding screening and no stated rule for invalid responses. — Page 3, Research Instrument — «the researchers then reviewed the submitted questionnaires ensuring all parts are complete»

Правки:
- 

Проверено: да

---

## ST004 · Ashraf 2026 · Asia Pacific Journal of Medical Innovations

Основной отчёт R0247: [текст](../../fulltext/text/R0247.txt) · [PDF](../../fulltext/pdf/R0247.pdf) — «Generative AI Use, Academic Dependence, and Psychological Distress among University Students in Bangladesh: A Cross-Sectional Study» — [DOI](https://doi.org/10.70818/apjmi.v03i02.052)
Расхождения в тексте: The correlations in the abstract and text (r = 0.37, 0.36, 0.29, 0.38) match Table 5. The DASS subscale means add up to the reported total (13.36+17.06+11.54=41.96). The adjusted B = 1.336 (Table 6) fits r = 0.38 given SD(dependence) 8.31 and SD(DASS total) 29.04. The dependence measure has a score range of 10-50, which suggests 10 items, but the number of items and its reliability are never stated. Table 6 labels academic year as '1st-5th/Masters', while Table 1 lists 1st-4th year and Masters only. Figure 1 (DASS severity distribution) and Figure 2 (% with moderate+ distress by dependence level) are figures. Figure 2's percentages are given only in the text and are not effects to extract.
Заметка ИИ: There is one eligible sample with four Pearson correlations: the AI academic dependence total score with DASS-21 depression, anxiety, stress and total. No reliability coefficients are reported for any measure.

### ST004-1 · Four private universities, Dhaka, Bangladesh (n=480)
Отчёты: R0247 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0247_1 · total (T4) | **depression** · DASS-21 Depression | pearson | **0.37** | **480** | 1 | Page 6, Table 5 | «AI Dependence / - / 0.37** / 0.36** / 0.29** / 0.38**» |
| E2 | ADHOC_R0247_1 · total (T4) | **anxiety** · DASS-21 Anxiety | pearson | **0.36** | **480** | 1 | Page 6, Table 5 | «AI Dependence / - / 0.37** / 0.36** / 0.29** / 0.38**» |
| E3 | ADHOC_R0247_1 · total (T4) | **stress** · DASS-21 Stress | pearson | **0.29** | **480** | 1 | Page 6, Table 5 | «AI Dependence / - / 0.37** / 0.36** / 0.29** / 0.38**» |
| E4 | ADHOC_R0247_1 · total (T4) | **distress** · DASS-21 total | pearson | **0.38** | **480** | 1 | Page 6, Table 5 | «AI Dependence / - / 0.37** / 0.36** / 0.29** / 0.38**» |

- E1: заметка: Matrix gives two decimals only
- E2: заметка: Matrix gives two decimals only
- E3: заметка: Matrix gives two decimals only
- E4: заметка: Matrix gives two decimals only. DASS-21 total score

**Ключевые поля выборки:**
- **n_analysed: 480** — Page 6, Table 5 — «Table 5: Pearson Correlation Matrix among Academic Dependence Score and DASS-21 Subscale/Total Scores (N = 480)»
- **population: university_students** — Page 2, Methodology — «A total of 480 currently enrolled undergraduate and graduate students were included»
- **sampling: convenience** — Page 2, Methodology — «Four private universities were purposively selected ... students were approached across broad disciplinary groups using stratified convenience sampling»
- **ai_system: general_chatbot** — Page 4, Table 2 — «Platforms Used (Multiple Response) ChatGPT 442 92.1% Google Gemini 148 30.8% Microsoft Copilot 88 18.3% Other tools (Claude, DeepSeek, etc.) 47 9.8%»

**Остальные поля:**
- country: BGD — Page 2, Methodology — «conducted from July to December 2025 among university students in Dhaka, Bangladesh.»
- data_years: 2025 — Page 2, Methodology — «This multi-institutional quantitative cross-sectional study was conducted from July to December 2025»
- design: cross-sectional — Page 2, Methodology — «This multi-institutional quantitative cross-sectional study»
- clinical_group: NA — NA — «NA»
- age_mean: 21.6 — Page 3, Table 1 — «Age (years) Mean = 21.6 (SD 1.9); Range 18-27»
- age_sd: 1.9 — Page 3, Table 1 — «Age (years) Mean = 21.6 (SD 1.9); Range 18-27»
- age_min: 18 — Page 3, Table 1 — «Age (years) Mean = 21.6 (SD 1.9); Range 18-27»
- age_max: 27 — Page 3, Table 1 — «Age (years) Mean = 21.6 (SD 1.9); Range 18-27»
- pct_female: 57.1 — Page 3, Table 1 — «Female 274 57.1%»
- mode: NR — Page 2-3, Methodology — «Data were collected using a structured, self-administered questionnaire ... Written or electronic informed consent was obtained from all participants.»
- attention_checks: yes — Page 2, Methodology — «Questionnaires with more than 10% missing responses were excluded. ... Completed questionnaires were checked for completeness and consistency»
- pub_status: journal — Page 1, header — «Asia Pacific Journal of Medical Innovations ... Research Article DOI: https://doi.org/10.70818/apjmi.v03i02.052»
- language: English — Full text — «Generative AI Use, Academic Dependence, and Psychological Distress among University Students in Bangladesh: A Cross-Sectional Study»
- funding_coi: No specific funding; authors declare no conflicts of interest — Page 8, Fundings / Conflict of Interest — «This study did not receive any specific funding from public, commercial, or not-for-profit funding agencies. Conflict of Interest: The authors declare that the…»
- notes: The dependence measure is study-specific: 5-point Likert, total range 10-50, pilot-tested in 30 students, item count not stated. Mean dependence score 27.47 (SD 8.31). attention_checks = yes rests only on the missing-data exclusion rule and completeness/consistency check; there are no attention-check items. Survey mode (paper vs online) is not stated; consent was 'written or electronic'.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Universities chosen purposively; students recruited by stratified convenience sampling with fixed quotas of 120 per university. — Page 2, Methodology; Page 8, Limitations — «students were approached across broad disciplinary groups using stratified convenience sampling»
2. отклик: **unclear** — Neither a response rate nor the number approached or excluded is reported. — Page 3, Results — «A total of 480 students participated in the study, with equal representation (n = 120, 25.0% each)»
3. валидная шкала зависимости от ИИ: **no** — Ad hoc dependence measure, adapted for this study. It was pilot-tested, but no validity or factor-structure evidence is reported. — Page 2, Methodology; Page 8, Limitations — «the academic dependence measure was adapted for this study ... Longitudinal and multi-centre studies using validated AI-dependence instruments are needed»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega is reported for the dependence measure in this sample. — Page 2, Methodology — «Academic dependence was assessed using a 5-point Likert-type measure of reliance on AI for academic task completion»
5. валидные шкалы коррелятов: **yes** — All correlates come from the DASS-21, a published instrument. — Page 2, Methodology — «Psychological distress was assessed using the 21-item Depression Anxiety Stress Scale (DASS-21).»
6. качество данных: **yes** — There is a stated rule for invalid responses (>10% missing excluded) and a completeness/consistency check. There are no attention-check items, so the reviewer should confirm that this rule is enough. — Page 2, Methodology — «Questionnaires with more than 10% missing responses were excluded. ... Completed questionnaires were checked for completeness and consistency»

Правки:
- 

Проверено: да

---

## ST005 · AYNACI 2026 · İstanbul Ticaret Üniversitesi Sosyal Bilimler Dergisi

Основной отчёт R0273: [текст](../../fulltext/text/R0273.txt) · [PDF](../../fulltext/pdf/R0273.pdf) — «Beliren Yetişkinlerde Depresyon ve Yapay Zekâ Sohbet Botlarına Bağımlılık İlişkisinde Yalnızlığın Aracı Rolü» — [DOI](https://doi.org/10.46928/iticusbe.1957632)
Расхождения в тексте: The bootstrap CI for the indirect effect differs between text and table. The text (p. 16) gives 95% CI [.0120, .1910]; Table 4 (p. 17) gives LLCI .0149 and ULCI .1907. The extracted correlations are the same in the Table 2 text and in the R values of Table 3 (.203, .149). The Table 2 footnote is printed as 'p < .05, p < .01' with the stars missing; the ** marks in the table are read as p < .01, which the text confirms. The method says 'four data collection tools' (dört farklı veri toplama aracı); this count includes the socio-demographic form and three scales. No figure-only coefficients.
Заметка ИИ: One cross-sectional sample. The AICD total score has zero-order Pearson correlations with two eligible correlates: depression (Short BDI) and loneliness (ULS-8). The depression–loneliness correlation (.358) doesn't involve AI dependence and was not extracted. Regression and PROCESS mediation estimates were not extracted.

### ST005-1 · Emerging adults aged 18-25 recruited via social media, Türkiye, n=830
Отчёты: R0273 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **depression** · Kısa Beck Depresyon Envanteri (Short Beck Depression Invent… | pearson | **.203** | **830** | 1 | Page 14, Table 2 | «2. Depresyon 3,91 3,12 0,995 0,771 .358** — / 3. Yapay Zekâ Bağımlılığı 20,05 10,06 0,759 -0,125 .149** .203** —» |
| E2 | AICD · total (T4) | **loneliness** · UCLA Yalnızlık Ölçeği Kısa Formu (ULS-8), Turkish adaptatio… | pearson | **.149** | **830** | 1 | Page 14, Table 2 | «1. Yalnızlık 11,98 3,13 0,750 0,023 — / 3. Yapay Zekâ Bağımlılığı 20,05 10,06 0,759 -0,125 .149** .203** —» |

- E1: α ИИ .901, α коррелята .76; заметка: Row 3 (AI dependence), column 2 (depression). The text gives the same value (r = .203, p < .01), and so does the simple regression R in Table 3.
- E2: α ИИ .901, α коррелята .75; заметка: Row 3 (AI dependence), column 1 (loneliness). The text gives the same value (r = .149, p < .01), and so does the regression R in Table 3.

**Ключевые поля выборки:**
- **n_analysed: 830** — Page 12, Verilerin Toplanması ve Analizi — «eksik veya hatalı doldurulan formlar çıkarılarak analizler 830 geçerli veri üzerinden gerçekleştirilmiştir. [after removing incomplete or incorrectly completed forms, analyses were conducted on 830 valid cases.]»
- **population: general_adults** — Page 10, Çalışma Grubu — «Araştırmanın çalışma grubunu 18–25 yaş aralığındaki (Ort: 22,06; Std. Sapma: 1,98) 830 beliren yetişkin birey oluşturmaktadır [The study group consists of 830 emerging adults aged 18–25]»
- **sampling: convenience** — Page 12, Verilerin Toplanması ve Analizi — «Anket formu ve karekodlar sosyal medya platformları üzerinden katılımcılara ulaştırılmıştır. [The survey form and QR codes were delivered to participants via social media platforms.]»
- **ai_system: general_chatbot** — Page 10, Table 1 — «En Sık Kullanılan Yapay Zekâ Sohbet Botu: ChatGPT 582 70,1; Gemini 229 27,6; Twitter Grok 12 1,4; DeepSeek 7 0,8 [Most frequently used AI chatbot]»

**Остальные поля:**
- country: TUR — Page 7, Introduction — «Bu durum, söz konusu ilişkilerin Türkiye örneklemi üzerinde incelenmesini özgün bir gereklilik olarak öne çıkarmaktadır. [This makes examining these relationsh…»
- data_years: 2026 — Page 12, Verilerin Toplanması ve Analizi — «Araştırma verileri, 20.02.2026–15.05.2026 tarihleri arasında çevrim içi anket bağlantısı aracılığıyla toplanmıştır. [Data were collected between 20.02.2026 and…»
- design: cross-sectional — Page 9, Araştırmanın Modeli — «nicel araştırma yöntemi, ilişkisel tarama modeli ve kesitsel desenle yürütülmüştür. [conducted with a quantitative, correlational survey model and cross-sectio…»
- clinical_group: NA — NA — «NA»
- age_mean: 22.06 — Page 10, Çalışma Grubu — «18–25 yaş aralığındaki (Ort: 22,06; Std. Sapma: 1,98)»
- age_sd: 1.98 — Page 10, Çalışma Grubu — «(Ort: 22,06; Std. Sapma: 1,98)»
- age_min: 18 — Page 10, Çalışma Grubu — «18–25 yaş aralığındaki [aged 18–25]»
- age_max: 25 — Page 10, Çalışma Grubu — «18–25 yaş aralığındaki [aged 18–25]»
- pct_female: 69.5 — Page 10, Table 1 — «Kadın 577 69,5 [Female 577 69.5%]»
- mode: online — Page 12, Verilerin Toplanması ve Analizi — «çevrim içi anket bağlantısı aracılığıyla toplanmıştır [collected via an online survey link]»
- attention_checks: yes — Page 12, Verilerin Toplanması ve Analizi — «eksik veya hatalı doldurulan formlar çıkarılarak analizler 830 geçerli veri üzerinden gerçekleştirilmiştir [incomplete or incorrectly completed forms were remo…»
- pub_status: journal — Page 1 — «İstanbul Ticaret Üniversitesi Sosyal Bilimler Dergisi, 25(56), 881-913, doi: 10.46928/iticusbe.1957632»
- language: Turkish (with English abstract) — Pages 2-3 — «Beliren Yetişkinlerde Depresyon ve Yapay Zekâ Sohbet Botlarına Bağımlılık İlişkisinde Yalnızlığın Aracı Rolü»
- funding_coi: Funding NR; author declares no financial interests or personal relationships (no COI). — Page 25, Çıkar Çatışması Beyanı — «Çalışmayı etkileyebilecek herhangi bir finansal çıkar veya kişisel ilişki bulunmamaktadır. [There are no financial interests or personal relationships that cou…»
- notes: Single-author study. Country isn't stated explicitly for the data collection; TUR is inferred from the introduction's 'Türkiye örneklemi' wording, Turkish adaptations of the scales and a Turkish university ethics board. The sample is not limited to students (60.5% not working; 26.4% in permanent jobs). AI dependence measured with the Turkish adaptation (Yıldız Durak & Balıkçı, 2025) of Zhang et al. (2025) AICD, 8 items, 7-point scale. Depression was measured with the 7-item Short Beck Depression Inventory (Özdemir & Dağdeviren, 2024).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample: online survey shared on social media platforms. — Page 12, Verilerin Toplanması ve Analizi — «Anket formu ve karekodlar sosyal medya platformları üzerinden katılımcılara ulaştırılmıştır.»
2. отклик: **unclear** — No response rate, no number of people invited and no count of excluded forms reported. — Page 12 — «eksik veya hatalı doldurulan formlar çıkarılarak analizler 830 geçerli veri üzerinden gerçekleştirilmiştir.»
3. валидная шкала зависимости от ИИ: **yes** — AICD has a published development/validation study (Zhang et al., 2025, CBSN) and a Turkish adaptation (Yıldız Durak & Balıkçı, 2025, conference proceeding). — Page 12, Yapay Zekâ Sohbet Botlarına Bağımlılık Ölçeği — «Yapay Zekâ Sohbet Botlarına Bağımlılık Ölçeği Zhang vd. (2025: 126) tarafından geliştirilmiş, Yıldız Durak ve Balıkçı (2025: 1) tarafından uyarlamıştır.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .901 in this sample. — Page 12 — «Bu çalışmada ise Cronbach alfa katsayısı .901 şeklinde hesaplanmıştır.»
5. валидные шкалы коррелятов: **yes** — Both correlates use published Turkish-adapted instruments: Short BDI (Özdemir & Dağdeviren, 2024) and ULS-8 (Doğan et al., 2011). — Pages 11-12, Veri Toplama Araçları — «Kısa Beck Depresyon Envanteri, Özdemir ve Dağdeviren (2024: 61) tarafından uyarlanan, 7 maddelik bir ölçektir. ... UCLA Yalnızlık Ölçeği Kısa Formu (ULS-8), uy…»
6. качество данных: **yes** — Stated rule for invalid responses: incomplete or incorrectly completed forms were removed. No attention-check items reported. — Page 12, Verilerin Toplanması ve Analizi — «eksik veya hatalı doldurulan formlar çıkarılarak»

Правки:
- 

Проверено: да

---

## ST006 · AzZahra 2026 · Universitas Airlangga Repository (Universitas Airlangga)

Основной отчёт R0285: [текст](../../fulltext/text/R0285.txt) — «Pengaruh Stres Akademik terhadap AI Dependency pada Mahasiswa»
Расхождения в тексте: The abstract names IBM SPSS Statistics 31 as the analysis software, but the Analysis section names both Jamovi 2.6.26 and SPSS 31. The internal statistics agree: r = 0.288 gives r² ≈ 0.083, matching the reported R² = 0.083. The unstandardized B = 0.228 × SD ratio (4.71/3.72) ≈ 0.289, which matches r. Several of the PASS CFA fit indices miss the thresholds the authors cite (TLI 0.848 < 0.9; RMSEA 0.105 > 0.08), yet the scale is treated as valid. The scale is called 'Dependence of Artificial Intelligence Scale' once (a typo for 'Dependence on'). There is a typo 'darinrgr' in the abstract. The DAI response labels are given as 1 = 'sangat tidak sesuai' to 5 = 'sangat sesuai'. There are no figures or heatmaps.
Заметка ИИ: One sample and one effect: the DAI total correlates with PASS academic stress at r = 0.288 (n = 266). There are no page markers, so locations are given as section headings. Quotes are in Indonesian with English translations in square brackets.

### ST006-1 · Indonesian university students, active Generative AI users, online survey (n=266)
Отчёты: R0285 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **academic_stress** · Perception of Academic Stress Scale (PASS; Bedewy & Gabriel… | pearson | **0.288** | **266** | 1 | HASIL PENELITIAN | «terdapat hubungan antara stres akademik dan AI Dependency dengan tingkat rendah menuju sedang (r = 0,288; p < 0,001) [a low-to-moderate relationship between academic stress and AI dependency]» |

- E1: α ИИ 0.710, α коррелята 0.942; заметка: Correlation given in the text only; there is no correlation table. Decimal comma in the original (0,288).

**Ключевые поля выборки:**
- **n_analysed: 266** — HASIL PENELITIAN — «responden sebanyak 279 responden, namun penulis mengeliminasi 13 sampel karena tidak lolos attention check sehingga jumlah sampel akhir sebanyak 266 sampel [279 respondents; 13 eliminated for failing attention check; final sample 266]»
- **population: university_students** — METODE, Partisipan — «Kriteria responden penelitian adalah mahasiswa dengan rentang usia 18-25 tahun yang merupakan pengguna aktif Generative AI. [university students aged 18-25 who are active Generative AI users]»
- **sampling: convenience** — METODE, Desain Penelitian; Partisipan — «menyebarkan link kuesioner melalui media sosial Instagram, TikTok, WhatsApp, dan X (Twitter) ... teknik non-probability sampling melalui metode purposive sampling [distributed via social media; non-probability purposive sampling]»
- **ai_system: general_chatbot** — METODE, Partisipan; Abstract — «mahasiswa ... yang merupakan pengguna aktif Generative AI [students who are active users of Generative AI]»

**Остальные поля:**
- country: IDN — PENDAHULUAN (last paragraph) — «khususnya di Indonesia dimana penelitian mengenai faktor psikologis yang dapat berkontribusi terhadap AI Dependency masih terbatas [particularly in Indonesia, …»
- data_years: NR — METODE — «NR»
- design: cross-sectional — METODE, Desain Penelitian — «Penelitian ini menggunakan pendekatan kuantitatif dengan desain penelitian cross-sectional melalui metode pengumpulan data survey kuesioner daring. [quantitati…»
- clinical_group: NA — NA — «NA»
- age_mean: NR — HASIL PENELITIAN — «NR»
- age_sd: NR — HASIL PENELITIAN — «NR»
- age_min: 18 (inclusion criterion) — METODE, Partisipan; Abstract — «266 mahasiswa berusia 18–25 tahun yang aktif menggunakan Generative AI [266 students aged 18–25 who actively use Generative AI]»
- age_max: 25 (inclusion criterion) — METODE, Partisipan; Abstract — «266 mahasiswa berusia 18–25 tahun yang aktif menggunakan Generative AI [266 students aged 18–25 who actively use Generative AI]»
- pct_female: 81.6 — HASIL PENELITIAN — «Responden terdiri dari 217 mahasiswa perempuan (81,6%) dan 49 mahasiswa laki-laki (18,4%). [217 female students (81.6%) and 49 male (18.4%)]»
- mode: online — METODE, Desain Penelitian — «Penulis membuat kuesioner menggunakan Google Form dan menyebarkan link kuesioner melalui media sosial [questionnaire created with Google Form, link shared via …»
- attention_checks: yes — HASIL PENELITIAN — «penulis mengeliminasi 13 sampel karena tidak lolos attention check [the author eliminated 13 cases for failing the attention check]»
- pub_status: other — Header; UCAPAN TERIMA KASIH — «ARTIKEL PENELITIAN ... Ibu Listyati Setyo Palupi, S.Psi., M.DevPract selaku dosen pembimbing [... as supervising lecturer]»
- language: Indonesian (abstract also in English) — Whole text — «Pengaruh Stres Akademik terhadap AI Dependency pada Mahasiswa [The Effect of Academic Stress on AI Dependency among University Students]»
- funding_coi: Funding NR; authors declare no employment, consultancy, shares or funding from any organisation that could benefit (no COI). — DEKLARASI POTENSI TERJADINYA KONFLIK KEPENTINGAN — «tidak bekerja, menjadi konsultan, memiliki saham, atau menerima dana dari perusahaan atau organisasi mana pun yang mungkin akan mengambil keuntungan [do not wo…»
- notes: No page markers in the text; locations are section headings. pub_status coded 'other': the document is a 'research article' in the Universitas Airlangga repository that thanks a 'dosen pembimbing' (supervisor), so it is probably based on a student thesis. Please check whether 'thesis' fits better. Only the age range from the inclusion criteria is given; no age mean or SD. Simple regression: B = 0.228 (unstandardized), SE = 0.047, R² = 0.083. This was not extracted as an effect because the Pearson r is reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability purposive sampling with recruitment on social media. — METODE, Partisipan — «Penelitian menggunakan teknik non-probability sampling melalui metode purposive sampling. [non-probability purposive sampling]»
2. отклик: **unclear** — No response rate is reported (open social-media link); only 279 completed responses are mentioned. — HASIL PENELITIAN — «Hasil penelitian dengan responden sebanyak 279 responden [279 respondents]»
3. валидная шкала зависимости от ИИ: **yes** — The DAI is a published scale (Morales-García et al., 2024, development and validation), and this report also gives CVI and CFA results. — METODE, Pengukuran — «Dependence on Artificial Intelligence Scale yang dikembangkan oleh Morales-García dkk., (2024) ... CFA menunjukkan hasil fit indices CFI 0,987 (>0,9), TLI 0,97…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.710 in this sample (≥ .70). — METODE, Pengukuran — «Hasil analisis reliabilitas menggunakan teknik Cronbach's Alpha dengan reliabilitas yang cukup baik (α = 0,710). [fairly good reliability]»
5. валидные шкалы коррелятов: **yes** — Academic stress was measured with the published Perception of Academic Stress Scale (Bedewy & Gabriel, 2015) in the Indonesian adaptation by Dewi et al. (2022). — METODE, Pengukuran — «Perception of Academic Stress Scale oleh Bedewy dan Gabriel (2015) yang telah diadaptasi oleh Dewi dkk., (2022) ke Bahasa Indonesia.»
6. качество данных: **yes** — An attention check was used, and 13 cases that failed it were excluded. — HASIL PENELITIAN — «penulis mengeliminasi 13 sampel karena tidak lolos attention check [13 cases eliminated for failing attention check]»

Правки:
- 

Проверено: да

---

## ST007 · Barrios 2026 · Alpha psychiatry

Основной отчёт R0332: [текст](../../fulltext/text/R0332.txt) — «Artificial Intelligence Chatbot Dependence, Anxiety, and Depressive Symptoms in University Students: Initial Psychometric Evaluation of the Artificial Intellig…» — [DOI](https://doi.org/10.31083/ap53298)
Расхождения в тексте: The anxiety group comparison has an odd sign. The text says students who screened positive had higher AICDS scores (M = 23.77 vs 20.68), but it gives Cohen's d = −0.29 and explains the minus sign as reflecting group order. For depression, t = −1.80 and mean difference = −2.72, and the direction of the group means is not stated. Not extracted (continuous Pearson r available). The adjusted Model 1/Model 2 βs in the text (GAD-7 β = 0.08; PHQ-2 β = 0.10) differ from Table 4 Model 3 βs (0.03; 0.09). This is expected because the models are different; none of these were extracted. Figs. 1–5 (loadings, polychoric item correlations, group comparisons, scatter plots) are not extracted. The text calls the mediation analysis 'anxiety mediating chatbot dependence → depressive symptoms', while Section 2.6 describes GAD-7/PHQ-2 as predictors of AICDS. The direction of the models is inconsistent, but n…
Заметка ИИ: There is one sample (n = 200) with two Pearson correlations: AICDS total with GAD-7 and with PHQ-2. Spearman values are recorded in the effect notes. The attention_checks/rob_6 rating of 'yes' rests only on a missing-data rule (more than 20% missing = ineligible). Please check this rating.

### ST007-1 · University students, Santa Rosa del Aguaray, Paraguay, n=200
Отчёты: R0332 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **anxiety** · GAD-7 (Spanish version), continuous score | pearson | **0.073** | **200** | 1 | Section 3.2 | «Pearson correlations were positive but small and non-significant: r = 0.073 (95% CI: −0.066 to 0.210, p = 0.304) with GAD-7» |
| E2 | AICD · total (T4) | **depression** · PHQ-2 (Spanish version), continuous score | pearson | **0.099** | **200** | 1 | Section 3.2 | «r = 0.099 (95% CI: −0.040 to 0.235, p = 0.162) with PHQ-2. Spearman rank correlations were consistent: ρ = 0.059 (p = 0.404) and ρ = 0.085 (p = 0.234)» |

- E1: α ИИ 0.833 (omega 0.903), α коррелята 0.905; для пересчёта: 95% CI: −0.066 to 0.210; заметка: Spearman ρ = 0.059 (p = 0.404) also reported for this pair.
- E2: α ИИ 0.833 (omega 0.903), α коррелята 0.746; для пересчёта: 95% CI: −0.040 to 0.235; заметка: Spearman ρ = 0.085 (p = 0.234) also reported for this pair.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: -0.26, 0.06, 0.09, 23.77 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 200** — Section 3.1; Table 1 — «A total of 200 university students were included in the study.»
- **population: university_students** — Section 2.2 — «Eligibility criteria included being 18 years or older, currently enrolled in an undergraduate university program in Santa Rosa del Aguaray»
- **sampling: convenience** — Section 2.2 — «Participants were recruited using a non-probabilistic consecutive sampling strategy based on an open invitation extended to students.»
- **ai_system: general_chatbot** — Section 2.2; Section 2.4.1 — «The accessible population included students who had used an artificial intelligence chatbot within the previous four weeks.»

**Остальные поля:**
- country: PRY — Section 2.2 — «The target population comprised university students enrolled in undergraduate programs in Santa Rosa del Aguaray, Paraguay.»
- data_years: 2025 — Section 2.2 — «The survey remained open from October to December 2025.»
- design: validation study — Abstract; Section 2.1 — «This study aimed to conduct an initial psychometric evaluation of the Spanish version of the Artificial Intelligence Chatbot Dependence Scale (AICDS)... A cros…»
- clinical_group: NA — NA — «NA»
- age_mean: 23.7 — Section 3.1 — «Participants ranged in age from 18 to 55 years, with a mean age of 23.7 ± 6.1 years.»
- age_sd: 6.1 — Section 3.1 — «with a mean age of 23.7 ± 6.1 years»
- age_min: 18 — Section 3.1 — «Participants ranged in age from 18 to 55 years»
- age_max: 55 — Section 3.1 — «Participants ranged in age from 18 to 55 years»
- pct_female: 60.5 — Section 3.1; Table 1 — «Women represented 60.5% of the sample.»
- mode: online — Section 2.2 — «Data collection was carried out through an online questionnaire hosted on a freely accessible digital platform»
- attention_checks: yes — Section 2.2 — «Questionnaires with more than 20% missing responses were defined as ineligible; however, in practice all questionnaires were fully completed, and all collected…»
- pub_status: journal — Header — «venue: Alpha psychiatry; DOI: 10.31083/ap53298»
- language: English (instrument administered in Spanish) — Table 2 note — «Items were administered in Spanish and rated on a 7-point Likert scale»
- funding_coi: No external funding; authors declare no conflicts of interest (two authors are journal Guest Editors/Editorial Board members, not involved in handling). — Funding Statement; Conflicts of Interest — «This research received no external funding. ... The authors declare no conflicts of interest. Antonio Ventriglio and Julio Torales serve as Guest Editors and a…»
- notes: Single sample; Spanish adaptation of AICDS (8 items, 7-point, total score). Spearman correlations also reported (GAD-7 ρ = 0.059; PHQ-2 ρ = 0.085); Pearson extracted as the effect rows. Group comparisons by screening status (t-tests, Cohen's d) and adjusted regressions were not extracted because zero-order continuous correlations are available. The only data-quality rule is a missingness rule (>20% missing = ineligible), not attention checks; reviewer should confirm that attention_checks/rob_6 = yes is appropriate.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probabilistic consecutive sampling via open invitation online (institutional channels, social media, WhatsApp/Telegram). — Section 2.2 — «Participants were recruited using a non-probabilistic consecutive sampling strategy based on an open invitation extended to students.»
2. отклик: **unclear** — No response rate or comparison of non-responders reported. — Section 2.2 — «reminder messages were disseminated biweekly through the same institutional channels and social media platforms to encourage survey completion.»
3. валидная шкала зависимости от ИИ: **yes** — AICDS has a published development/validation study (ref 25) and the Spanish version was validated by CFA in this report. — Section 2.4.1; Section 3.2 — «Previous validation studies have reported adequate psychometric properties for the instrument, including a stable factor structure and approximately 58% of exp…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.833 and omega 0.903 in this sample. — Section 3.2 — «Internal consistency of the AICDS was high, with a Cronbach's alpha coefficient of 0.833.»
5. валидные шкалы коррелятов: **yes** — GAD-7 and PHQ-2 are published, validated instruments (validated Spanish versions). — Sections 2.4.2-2.4.3 — «The validated Spanish version of the GAD-7 was used in this study»
6. качество данных: **yes** — Stated rule for invalid responses (>20% missing = ineligible); no attention checks or careless-responding screening. Borderline; reviewer to confirm. — Section 2.2 — «Questionnaires with more than 20% missing responses were defined as ineligible»

Правки:
- 

Проверено: да

---

## ST008 · Beni 2026 · Zenodo (CERN European Organization for Nuclear Research)

Основной отчёт R0344: [текст](../../fulltext/text/R0344.txt) · [PDF](../../fulltext/pdf/R0344.pdf) — «The Impact of AI Companion Use on Loneliness, Emotional Attachment, and Interpersonal Communication Skills among Young Adults» — [DOI](https://doi.org/10.5281/zenodo.21876606)
Расхождения в тексте: 1) The regression and moderation betas (loneliness β=.254, burnout β=.238) are identical to values the Literature Review credits to Effendy et al. (2026). The sampling ('as per the sampling strategy from Effendy et al.'), the Palembang, Indonesia setting and the analyses also mirror that study, while the authors are affiliated in Iran. Possible data duplication: the reviewer should check. 2) Table 2 gives identical t (7.67) for burnout and loneliness despite different β. Loneliness has the same β and t in Table 4 (.254, 7.67) under a different model. 3) Table 3 gives the indirect-effect CI as (.13, .19); the text gives [.132, .191]. 4) Table 2 note says the model 'explains 48%' but reports Adjusted R²=.486. 5) The abstract says loneliness relief is β=0.254, but in the results this is loneliness predicting attachment. 6) The UCLA-3 (normally a 1-4 scale) is reported on a 1-7 metric (M=3.…
Заметка ИИ: There is one effect: emotional attachment to AI (AIAS) with UCLA loneliness, r=.38, N=1,200. Several features suggest possible data fabrication or duplication from Effendy et al. (2026); see consistency_notes. The reviewer should consider an integrity check before this study is included.

### ST008-1 · University students, Palembang, Indonesia (n=1,200)
Отчёты: R0344 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0344_1 · total (T4) | **loneliness** · UCLA Loneliness Scale (Version 3) | pearson | **.38** | **1200** | 1 | Page 4, Table 1 | «2. Subjective Loneliness / 3.89 / 1.67 / .41** / 1.00 / .49** / .38** / -.35**» |

- E1: α ИИ .90, α коррелята .91; заметка: Matrix gives two decimals only. Text agrees (r=.38). Only 48% reported using an AI companion, yet the correlation uses N=1,200.

**Ключевые поля выборки:**
- **n_analysed: 1200** — Page 4, Table 1 note — «Note: N=1,200. ** p<.01 (two-tailed).»
- **population: university_students** — Page 3, Method, Study Design and Participants — «a convenience sample of 1,200 university students (aged 18-30; M=21.4, SD=2.7)»
- **sampling: convenience** — Page 3, Method, Study Design and Participants — «Participants were a convenience sample of 1,200 university students»
- **ai_system: ai_companion** — Page 3, Method — «48% of participants reporting use of at least one AI companion platform, including Replika (22.61%), Character. AI (30.39%), and Snapchat MyAI (31.63%) (Folk et al.,2024).»

**Остальные поля:**
- country: IDN — Page 3, Method, Study Design and Participants — «recruited through university mailing lists, social media, and a public organization in Palembang, Indonesia, as per the sampling strategy from Effendy et al. (…»
- data_years: 2025 — Page 4, Procedure and Data Analysis — «Data were collected over four months in 2025.»
- design: cross-sectional — Page 3, Method, Study Design and Participants — «This study employed a cross-sectional, correlational survey design»
- clinical_group: NA — NA — «NA»
- age_mean: 21.4 — Page 3, Method — «(aged 18-30; M=21.4, SD=2.7)»
- age_sd: 2.7 — Page 3, Method — «(aged 18-30; M=21.4, SD=2.7)»
- age_min: 18 — Page 3, Method — «(aged 18-30; M=21.4, SD=2.7)»
- age_max: 30 — Page 3, Method — «(aged 18-30; M=21.4, SD=2.7)»
- pct_female: 58 — Page 3, Method — «The sample was 58% female (n=696)»
- mode: online — Pages 3-4, Measures; Procedure — «All participants completed a standardized, anonymous online questionnaire. ... The survey was administered via Qualtrics»
- attention_checks: NR — Page 4, Procedure and Data Analysis — «All scales were checked for reliability using Cronbach's alpha.»
- pub_status: journal — Page 1, header — «Adv. J. Manag. Humanit. Soc. Sci. (2026), Volume 2, Issue 4, 306-315»
- language: English — Full text — «The Impact of AI Companion Use on Loneliness, Emotional Attachment, and Interpersonal Communication Skills among Young Adults»
- funding_coi: No specific funding; no conflict of interest reported — Page 9, Disclosure Statement; Funding — «No potential conflict of interest reported by the authors. ... This research did not receive any specific grant from funding agencies»
- notes: Only 48% reported using an AI companion, yet all N=1,200 have AIAS scores. The design and statistics closely mirror Effendy et al. (2026), with identical betas; possible duplication (see consistency_notes).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited via mailing lists, social media and a public organization. — Page 3, Method — «Participants were a convenience sample of 1,200 university students»
2. отклик: **unclear** — No response rate or comparison of non-responders reported. — Page 3, Method — «recruited through university mailing lists, social media, and a public organization»
3. валидная шкала зависимости от ИИ: **unclear** — The AIAS is named and cited to Xie & Pentina (2022) and Effendy et al. (2026), but neither is in the reference list and neither is clearly a validation study. Items were 'adapted', no validation is reported here, and th… — Page 4, Measures — «Emotional Attachment to AI: Measured via the AI Attachment Scale (AIAS), which evaluates feelings of closeness, dependence, and emotional investment in the AI …»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .90 in this sample. — Page 4, Measures — «The scale was highly reliable (α=0.90).»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, loneliness, was measured with the published UCLA Loneliness Scale Version 3. — Page 4, Measures — «Subjective Loneliness: Measured using the UCLA Loneliness Scale (Version 3), a widely used 20-item measure of global loneliness (Russell,1996).»
6. качество данных: **unclear** — No attention checks, careless-responding screening or rule for invalid responses is reported. — Page 4, Procedure and Data Analysis — «Participants were briefed on the study's purpose, provided informed consent, and completed the survey in a single session.»

Правки:
- 

Проверено: да

---

## ST009 · Benites-Rodriguez 2026 · Proceedings of the LACCEI international multi-conference for engineering, educa…

Основной отчёт R0345: [текст](../../fulltext/text/R0345.txt) · [PDF](../../fulltext/pdf/R0345.pdf) — «Classification of Student Profiles Based on Generative AI Dependency and Complex Problem-Solving Capacity: A Machine Learning Approach Using K-Means Clustering» — [DOI](https://doi.org/10.18687/laccei2026.1.1.2413)
Расхождения в тексте: (1) The abstract says AI dependence mediates the frequency → problem-solving relationship with β=-0.43. Table V and the text give an indirect effect of β=-0.30 and a dependence → problem-solving path of β=-0.56; -0.43 appears nowhere in the results. (2) Profile 1 text says 78.3% critically evaluate AI outputs, but in Table IV 78.3% is 'Edición de outputs' and 'Evaluación crítica outputs' is 82.4%. (3) The conclusions mention profile differences in 'bienestar' (wellbeing), but no wellbeing measure is reported. (4) Table II marks significance as **p<.01, while Tables III and IV use **p<.001. (5) Several references are duplicated ([6]=[12], [17]=[22], [39]=[45], [40]=[46]), and ref [8] is an unverifiable 'Anthropic Technical Report'. (6) The data-collection universities (UNI, UTN, Uniandes) are not the authors' affiliations (UNAC, URP), yet ethics approval by all three is claimed. The revi…
Заметка ИИ: One pooled sample (N=847). Two eligible zero-order Pearson correlations come from Table II, both with the EDIAU-15 total score: academic self-efficacy -.38 and academic stress .41. SEM betas (Table V) were not extracted. The total-score alpha is not reported; only subscale alphas are.

### ST009-1 · Engineering undergraduates, 3 Latin American universities (PER, ARG, COL), n=847
Отчёты: R0345 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0345_1 · total (T4) | **self_efficacy** · Escala de Autoeficacia Académica General (Academic Self-Eff… | pearson | **-.38** | **847** | 1 | Page 5, Table II (row 4, column 1) | «4. Autoeficacia académica 3.68 0.72 -.38** .54** -.22** —» |
| E2 | ADHOC_R0345_1 · total (T4) | **academic_stress** · Escala de Estrés Académico (Academic Stress Scale, ref [49]) | pearson | **.41** | **847** | 1 | Page 5, Table II (row 6, column 1) | «6. Estrés académico 3.12 0.89 .41** -.35** .33** -.42** -.39** —» |

- E1: α ИИ NR, α коррелята 0.86; заметка: Matrix gives two decimals; text also reports r=-0.38. Exposure is the total 'Dependencia a IA' score; subscale correlations not reported. EDIAU-15 total alpha NR (subscale alphas .87/.84/.89).
- E2: α ИИ NR, α коррелята 0.84; заметка: Matrix gives two decimals; this value does not appear in the text. Exposure is the total 'Dependencia a IA' score.

**Ключевые поля выборки:**
- **n_analysed: 847** — Page 5, Table I and Table II — «CARACTERÍSTICAS DEMOGRÁFICAS DE LA MUESTRA (N=847)»
- **population: university_students** — Page 4, III.B Participantes — «La muestra incluyó 847 estudiantes de pregrado en programas de ingeniería [The sample included 847 undergraduate engineering students]»
- **sampling: convenience** — Page 4, III.B Participantes — «El muestreo fue no probabilístico por conveniencia con cuotas por universidad y especialidad. [Sampling was non-probabilistic convenience with quotas by university and specialty.]»
- **ai_system: general_chatbot** — Page 4, III.B Participantes; Page 1 Abstract — «(b) haber utilizado ChatGPT al menos una vez en los últimos 3 meses [(b) having used ChatGPT at least once in the last 3 months]»

**Остальные поля:**
- country: MULTI: PER, ARG, COL — Page 4, III.B Participantes — «Universidad Nacional de Ingeniería (Perú, n=312), Universidad Tecnológica Nacional (Argentina, n=287), y Universidad de los Andes (Colombia, n=248)»
- data_years: 2025 — Page 4-5, III.D Procedimiento — «La recolección de datos se realizó entre marzo y mayo de 2025 [Data collection took place between March and May 2025]»
- design: cross-sectional — Page 4, III.A Diseño del Estudio — «Se utilizó un diseño de investigación transversal con componentes de validación psicométrica y análisis de clustering. [A cross-sectional design with psychomet…»
- clinical_group: NA — NA — «NA»
- age_mean: 21.4 — Page 4, III.B Participantes — «edad media 21.4 años (DE=2.3) [mean age 21.4 years (SD=2.3)]»
- age_sd: 2.3 — Page 4, III.B Participantes — «edad media 21.4 años (DE=2.3)»
- age_min: NR (lowest age band reported: 18-20) — Page 5, Table I — «Edad (años) 18-20 287 33.9%»
- age_max: NR (highest age band reported: 24+) — Page 5, Table I — «24+ 148 17.5%»
- pct_female: 37.7 — Page 5, Table I — «Femenino 319 37.7%»
- mode: online — Page 4-5, III.D Procedimiento — «mediante cuestionarios en línea administrados a través de Qualtrics [through online questionnaires administered via Qualtrics]»
- attention_checks: yes — Page 5, III.D Procedimiento — «Se implementaron verificaciones de atención y se excluyeron respuestas con patrones sospechosos (n=43, 4.8%). [Attention checks were implemented and responses …»
- pub_status: conference — Page 1, header — «24th LACCEI International Multi-Conference for Engineering, Education, and Technology»
- language: Spanish (English abstract on page 1) — Page 2 — «Clasificación de Perfiles de Estudiantes según su Dependencia a la IA Generativa»
- funding_coi: Funding NR; conflicts of interest NR (acknowledgement thanks university authorities and research teams only) — Page 8, Agradecimiento — «Los autores agradecen a las autoridades de las universidades participantes por facilitar el acceso a poblaciones estudiantiles.»
- notes: The three university subsamples are pooled in all analyses. EDIAU-15 is study-specific: adapted from Morales-García et al. and Yu et al. and validated by CFA in this report. Only the total 'Dependencia a IA' score is correlated with other variables (Table II); subscales appear only in the cluster centroids. The reviewer may want to check data integrity (see consistency_notes).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability convenience sampling with quotas; recruitment via institutional announcements. — Page 4, III.B; Page 5, III.D — «El muestreo fue no probabilístico por conveniencia con cuotas por universidad y especialidad.»
2. отклик: **unclear** — No response rate reported; only 43 exclusions for suspicious patterns are reported. — Page 5, III.D Procedimiento — «Los participantes fueron reclutados mediante anuncios en plataformas institucionales y aulas virtuales.»
3. валидная шкала зависимости от ИИ: **yes** — EDIAU-15 was adapted from published scales and its three-factor structure was validated by CFA in this report. — Page 4, III.C.1 — «El AFC confirmó la estructura trifactorial (χ²/df=2.34, CFI=0.94, TLI=0.92, RMSEA=0.052, SRMR=0.048).»
4. надёжность шкалы ИИ в выборке: **yes** — Subscale alphas in this sample are .84-.89. The alpha of the total score, which is the score correlated in Table II, is not reported. The reviewer may prefer 'unclear'. — Page 4, III.C.1 — «Dependencia Funcional (5 ítems, α=0.87), Dependencia Emocional (5 ítems, α=0.84), y Dependencia Cognitiva (5 ítems, α=0.89)»
5. валидные шкалы коррелятов: **unclear** — Academic self-efficacy is cited to a published scale (Nielsen et al., Assessment 2018). The academic stress scale is cited to Akanni & Oduaran (2018), a substantive study rather than an identifiable instrument-developme… — Page 4, III.C.3; Page 9, refs [48],[49] — «Escala de Autoeficacia Académica General (α=0.86) [48], Escala de Estrés Académico (α=0.84) [49]»
6. качество данных: **yes** — Attention checks were used and suspicious response patterns were excluded. — Page 5, III.D Procedimiento — «Se implementaron verificaciones de atención y se excluyeron respuestas con patrones sospechosos (n=43, 4.8%).»

Правки:
- 

Проверено: да

---

## ST010 · Buniel 2026 · International Journal of Information and Education Technology

Основной отчёт R0416: [текст](../../fulltext/text/R0416.txt) · [PDF](../../fulltext/pdf/R0416.pdf) — «The Efficiency Paradox: Modeling Student Engagement and AI Dependence on STEM Productivity in a Philippine State University» — [DOI](https://doi.org/10.18178/ijiet.2026.16.7.2657)
Расхождения в тексте: 1) Mismatch between hypotheses and decisions: H7 states that Intrinsic Motivation positively influences AI Dependence, but Table 4 marks H7 'Supported' for β = –0.460. 2) The latent correlation AD–SE is positive (0.524), and the SEM path SE→AD is also positive (0.258). The text treats this as rejecting H5. 3) Harman's single factor explains 56.12% of variance, which exceeds the 50% threshold, so common-method bias is possible. 4) Fig. 2 (structural model) and Fig. 3 (IPMA map) show path coefficients and importance values only. They contain no zero-order correlations, so nothing was extracted from them. 5) The text says the highest inter-construct correlation is 0.852 (DL–PU), which matches Table 3.
Заметка ИИ: One eligible effect: AD total with academic self-efficacy, a latent Fornell-Larcker correlation of 0.524 (n = 915). The other constructs (digital literacy, perceived usefulness, intrinsic motivation, time management, output productivity) have no dictionary key. Age, gender, data year and response rate are not reported.

### ST010-1 · STEM undergraduates, state university in southern Philippines (NEMSU), n=915
Отчёты: R0416 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0416_1 · total (T2) | **self_efficacy** · Self-Efficacy (SE), ad hoc 10-item academic self-efficacy s… | latent | **0.524** | **915** | 1 | Page 4, Table 3 (Fornell-Larcker) | «SE / 0.524 / 0.698 / 0.826 / 0.667 / 0.662 / 0.875» |

- E1: α ИИ 0.984, α коррелята 0.966; заметка: Latent correlation between PLS constructs from the Fornell-Larcker table (first column = AD). Some SE items refer to AI ('without AI assistance', 'without relying heavily on AI'), so content may overlap with AD. No observed Pearson matrix is reported.

**Ключевые поля выборки:**
- **n_analysed: 915** — Page 3, Table 1 — «Table 1. Demographic profile of respondents (N = 915)»
- **population: university_students** — Page 3, Participants and sampling — «The study involved a total of 915 undergraduate students enrolled in STEM-aligned programs»
- **sampling: convenience** — Page 3, Participants and sampling — «The sampling utilized a purposive-convenience strategy.»
- **ai_system: ai_unspecified** — Page 8, Table A1 (AD items); Page 1, Abstract — «AD1. I feel anxious when I cannot access AI tools for my assignments.»

**Остальные поля:**
- country: PHL — Page 3, Participants and sampling — «undergraduate students enrolled in STEM-aligned programs at a state university in the southern Philippines»
- data_years: NR — Page 4, Research instrument — «Ethical approval was granted by the Research Ethics Committee of the host university (Protocol/Ref: NEMSU-RDO-2025-08).»
- design: cross-sectional — Page 4, Measurement Model Assessment — «Given the reliance on cross-sectional self-reported data, the potential for Common Method Bias (CMB) was assessed.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 3, Table 1 — «Table 1 reports degree program and year level only»
- age_sd: NR — Page 3, Table 1 — «Table 1 reports degree program and year level only»
- age_min: NR — Page 3, Table 1 — «Table 1 reports degree program and year level only»
- age_max: NR — Page 3, Table 1 — «Table 1 reports degree program and year level only»
- pct_female: NR — Page 3, Table 1 — «Table 1 reports degree program and year level only»
- mode: online — Pages 3-4, Research instrument — «Data were collected using a structured, web-based questionnaire divided into seven sections»
- attention_checks: NR — Pages 3-4, Methods — «No attention checks or careless-responding screening are described.»
- pub_status: journal — Page 1, header/footer — «International Journal of Information and Education Technology, Vol. 16, No. 7, 2026»
- language: English — Full text — «The Efficiency Paradox: Modeling Student Engagement and AI Dependence on STEM Productivity in a Philippine State University»
- funding_coi: Funding NR; authors declare no conflict of interest — Page 8, Conflict of Interest — «The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict…»
- notes: The AI tools are described generically ('AI tools'; GenAI in the abstract and introduction), so ai_system is coded ai_unspecified. Data collection year is not stated; the ethics protocol is numbered 2025. All constructs are ad hoc 10-item, 5-point Likert scales 'adapted from established scales'. Analysis used PLS-SEM in SmartPLS 4. Only the AD–Self-Efficacy pair maps to the dictionary. Digital Literacy, Perceived Usefulness, Intrinsic Motivation, Time Management (excluded from procrastination) and Output Productivity are not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive-convenience sample from one university — Page 3, Participants and sampling — «The sampling utilized a purposive-convenience strategy.»
2. отклик: **unclear** — No response rate or comparison with non-responders is reported — Page 3, Participants and sampling — «convenience sampling was employed to maximize participation rates within available course sections during the data collection period»
3. валидная шкала зависимости от ИИ: **yes** — The 10 AD items are ad hoc, but this report gives validation evidence: expert content validity, a pilot alpha, and in-sample CR, AVE and Fornell-Larcker discriminant validity. The reviewer may judge this too weak and ra… — Page 4, Research instrument; Table 2; Table 3 — «content validity was assessed by three educational technology experts ... a pilot test was conducted with 50 non-participant students.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha for AD in this sample = 0.984 — Page 4, Table 2 — «AI Dependence (AD) 0.984 0.985 0.878»
5. валидные шкалы коррелятов: **no** — Self-efficacy is measured with ad hoc 10 items adapted from the literature, not a named published instrument — Page 7, Table A1 — «SE1. I am confident in completing academic tasks even without AI assistance. ... 10 [10, 26, 27, 53]»
6. качество данных: **unclear** — No attention checks or invalid-response rules are reported — Pages 3-4, Methods — «Informed consent was obtained digitally from all participants, ensuring anonymity and the right to withdraw.»

Правки:
- 

Проверено: да

