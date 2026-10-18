# Проверка выписывания — файл 4 из 13

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

## ST031 · Iltaf 2026 · Insights (Bhalwal) International Journal of Humanities Management and Social Sc…

Основной отчёт R1060: [текст](../../fulltext/text/R1060.txt) · [PDF](../../fulltext/pdf/R1060.pdf) — «MEDIATING ROLE OF AI DEPENDENCY IN THE RELATIONSHIP BETWEEN AI LITERACY AND ACADEMIC PROCRASTINATION AMONG UNIVERSITY STUDENTS» — [DOI](https://doi.org/10.68156/m7qp7493)
Расхождения в тексте: (1) GAIDS–procrastination r: Table 4 gives .03, the text gives .034. The table value was extracted. (2) Table 4 marks the AI literacy–procrastination r as .45*, but the note says p<.01 and the text gives r = .457, p < .01. (3) Alphas: Table 2 gives .98/.97/.92, the text gives .982/.978/.929. Table values were used. (4) The text cites GAIDS as Goh et al. (2015); the reference list gives Goh, Hartanto & Majeed (2025). (5) The text calls the descriptive table 'table 2', but it is Table 3. (6) Data analysis section says 'moderating effect' where mediation is meant. (7) Table 7 gives R = 0.34 with R² = .001, which is inconsistent (R should be about .034). (8) Mediation: the direct effect (0.34) is larger than the total effect (0.31) and the indirect effect is negative (-0.026). The text's reading of this ('positively correlated with decrease in academic procrastination') is internally confus…
Заметка ИИ: I extracted one sample with one eligible effect: GAIDS total × academic procrastination. AI literacy is outside the construct dictionary, so it was not extracted. Funding, COI, data-collection years and mean age are not reported.

### ST031-1 · University students, Islamabad universities, Pakistan, n=300
Отчёты: R1060 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **procrastination** · Academic Procrastination Scale (APS; McCloskey & Scielzo), … | pearson | **.03** | **300** | 1 | p. 10, Table 4 | «AI Dependency .31** - - Academic Procrastination .45* .03 -» |

- E1: α ИИ .97, α коррелята .92; заметка: Table gives two decimals (.03). Text gives r = .034, p > .05. Alphas from Table 2 (text: .978 and .929).

**Ключевые поля выборки:**
- **n_analysed: 300** — p. 10, Table 4 — «Pearson Correlation Matrix of study Variables (N= 300)»
- **population: university_students** — p. 6, 3.2 Participants — «they were from different undergraduate and postgraduate degree programs in various fields of study.»
- **sampling: convenience** — p. 6, 3.2 Participants — «Data were collected through a convenience sampling technique, and online and face-to-face survey administration.»
- **ai_system: mixed** — p. 8, Table 1; p. 6 — «Most Used AI Tool ChatGPT 153 51 Google Gemini 47 15.7 Quillbot 22 7.3 Microsoft Copilot 22 7.3 Grammarly AI 21 7.0 Claude 19 6.3 Other 16 5.3»

**Остальные поля:**
- country: PAK — p. 6, 3.2 Participants — «A total of 300 University Students (150 males and 150 females) were selected from different Universities of Islamabad.»
- data_years: NR — NA — «NR»
- design: cross-sectional — p. 5, 3.1 Research Design — «The present study used a quantitative research approach with a cross-sectional correlational research design.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: 18 — p. 6, 3.2 Participants — «The age of participants was from 18 to 40 years»
- age_max: 40 — p. 6, 3.2 Participants — «The age of participants was from 18 to 40 years»
- pct_female: 50 — p. 8, Table 1 — «Gender Male 150 50 Female 150 50»
- mode: mixed — p. 6, 3.2 Participants — «Data were collected through a convenience sampling technique, and online and face-to-face survey administration.»
- attention_checks: NR — p. 6, 3.2; p. 7, 4.7 — «filled the questionnaires with incomplete information were excluded. ... The data set went through a screening process for data entry errors, outliers and miss…»
- pub_status: journal — p. 1 (header) — «INSIGHTS: INTERNATIONAL JOURNAL OF HUMANITIES, MANAGEMENT, AND SOCIAL SCIENCES (IIJHMSS) VOLUME 3, ISSUE 5, 2026»
- language: English — Full text — «MEDIATING ROLE OF AI DEPENDENCY IN THE RELATIONSHIP BETWEEN AI LITERACY AND ACADEMIC PROCRASTINATION AMONG UNIVERSITY STUDENTS»
- funding_coi: NR — NA — «NR»
- notes: Only one eligible correlate (academic procrastination, APS). AI literacy is not in the construct dictionary. GAIDS used as a total score only; no subscale correlations reported. AI system coded mixed: the scale targets generative AI, but the tools participants reported using include chatbots (ChatGPT, Gemini, Copilot, Claude) and writing tools (Quillbot, Grammarly). Attention checks coded NR: the report only says incomplete questionnaires were excluded and data were screened for entry errors/outliers/missing values; there are no attention-check items and no careless-responding screen. Reviewe…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample of students from Islamabad universities. — p. 6, 3.2 Participants — «Data were collected through a convenience sampling technique»
2. отклик: **unclear** — Response rate not reported. — NA — «NR»
3. валидная шкала зависимости от ИИ: **yes** — GAIDS has a published development and validation study (Goh, Hartanto & Majeed, 2025). The text cites it as 'Goh et al. (2015)', but the reference list gives 2025. — p. 7, 4.3; p. 18, References — «Generative AI Dependency Scale (GAIDS) created by Goh et al. (2015)... Good psychometric properties were reported by the developers»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .97 (Table 2) / .978 (text) in this sample. — p. 9, Table 2 — «AI Dependency 11 .97»
5. валидные шкалы коррелятов: **yes** — Academic procrastination measured with the published Academic Procrastination Scale (McCloskey & Scielzo). — p. 7, 4.4 — «Academic procrastination was assessed by a scale of academic procrastination (APS) created by McCloskey and Scielzo (2015). The APS includes 25 items»
6. качество данных: **unclear** — No attention checks or careless-responding screen reported. Only incomplete questionnaires were excluded and data were screened for entry errors, outliers and missing values. — p. 7, 4.7 — «The data set went through a screening process for data entry errors, outliers and missing values before hypothesis testing.»

Правки:
- 

Проверено: да

---

## ST032 · Jiang 2026 · Frontiers in psychology

Основной отчёт R1120: [текст](../../fulltext/text/R1120.txt) — «Addicted to AI? Prevalence and psychological drivers of generative AI dependency among pre-service teachers.» — [DOI](https://doi.org/10.3389/fpsyg.2026.1922716)
Не выписано ИИ: Independent cross-validation sample (N = 144): used only for CFA and reliability; no correlations of dependency with correlates are reported. Initial development sample: used for item screening. It is unclear whether this is a separate sample or the primary N = 565. Its only reported correlations are item-level (a dropped impulsivity item r = 0.28 and a dropped social-norms item r = 0.51 with dependency), not scale scores, so they were not extracted. Five interviewees: qualitative only.
Расхождения в тексте: The zero-order r values in Table 1 match Table 4 (IMP 0.58, ANX 0.49, TRU 0.41, ANTH 0.45, LIT −0.14, NORM 0.13). The text cites the same values (dependency–impulsivity r = 0.58, dependency–literacy r = −0.14). Some other correlates were not extracted because they fit no dictionary key: trust in AI, anthropomorphic attachment, perceived AI literacy, and social norms (norms about peers' AI use are not perceived social support). The text is unclear on whether the 'development sample' is the primary sample or a separate one. The NCA ceiling plots (Figure 2) and the SEM figure (Figure 1) are not extracted.
Заметка ИИ: There is one eligible sample. Both correlates were measured with scales built for this study. The ANX construct mixes AI anxiety and FOMO; it is coded ai_anxiety, and the reviewer should check this against Appendix A. The report gives no age or data-collection year, and the supplied text has no funding or COI statement.

### ST032-1 · Pre-service teachers (education majors), China (mainly Shandong), online survey, N=565
Отчёты: R1120 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1120_1 · total (T4) | **impulsivity** · Impulsivity (IMP), study-developed 2-item scale | pearson | **0.58** | **565** | 1 | Table 4 | «DEP / 0.58 / 0.49 / 0.41 / 0.45 / −0.14 / 0.13 / 1» |
| E2 | ADHOC_R1120_1 · total (T4) | **ai_anxiety** · AI anxiety/FOMO (ANX), study-developed 6-item scale | pearson | **0.49** | **565** | 1 | Table 4 | «DEP / 0.58 / 0.49 / 0.41 / 0.45 / −0.14 / 0.13 / 1» |

- E1: α ИИ 0.91, α коррелята 0.79 (Spearman-Brown); заметка: The impulsivity scale is ad hoc: 2 items, after a reverse-worded item was dropped. Table 1 gives the same zero-order r = 0.58. The report does not say whether Table 4 correlations are observed composite or latent; coded as Pearson.
- E2: α ИИ 0.91, α коррелята 0.90; заметка: The construct is labelled 'AI anxiety/FOMO' and mixes AI-related anxiety with FOMO; the reviewer may prefer fomo. Item wording is in Appendix A, which was not supplied. Table 1 gives the same zero-order r = 0.49.

**Ключевые поля выборки:**
- **n_analysed: 565** — Table 4 — «Table 4: Means, SDs, and correlations (N = 565).»
- **population: university_students** — Abstract — «565 education-major students in Chinese teacher-preparation programs completed an online survey»
- **sampling: convenience** — Method, Participants and procedure — «using an anonymous convenience and peer-referral (snowball) sampling strategy, from university students enrolled in education-related majors within teacher-preparation tracks»
- **ai_system: general_chatbot** — Introduction; Method — «The rapid diffusion of generative artificial intelligence (GenAI) tools—such as ChatGPT, DeepSeek, and Doubao»

**Остальные поля:**
- country: CHN — Method, Participants and procedure — «Respondents' IP addresses resolved to 12 provincial-level regions but were predominantly in Shandong (96.1%), concentrated in Jinan (50.4%) and Qingdao (37.0%)»
- data_years: NR — Method, Participants and procedure — «Data were collected via an online questionnaire distributed through WeChat»
- design: cross-sectional — Limitations and future research — «The design was cross-sectional and cannot establish temporal ordering or rule out reverse causality»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Method, Participants and procedure — «comprised first-year (60.5%), second-year (3.7%), third-year (28.7%), and fourth-year (7.1%) students»
- age_sd: NR — Method, Participants and procedure — «NR»
- age_min: NR — Method, Participants and procedure — «NR»
- age_max: NR — Method, Participants and procedure — «NR»
- pct_female: 76.8 — Method, Participants and procedure — «It was predominantly female (76.8%, n = 434)»
- mode: online — Method, Participants and procedure — «Data were collected via an online questionnaire distributed through WeChat»
- attention_checks: yes — Method, Participants and procedure — «we removed 31 (5.2%): 29 who reported never having used GenAI—20 of whom also completed the survey in under 60 s—and 2 further respondents who completed in und…»
- pub_status: journal — Venue: Frontiers in Psychology — «Frontiers in psychology; DOI: 10.3389/fpsyg.2026.1922716»
- language: English — Full text — «Addicted to AI? Prevalence and psychological drivers of generative AI dependency among pre-service teachers»
- funding_coi: NR (no funding or conflict-of-interest statement in the supplied text) — Full text — «NR»
- notes: The dependency scale (4 behavioural items) was developed for this study and validated in this report. GenAI non-users were excluded. Year of study was skewed: 60.5% first-year.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience and snowball sampling via WeChat — Method, Participants and procedure — «using an anonymous convenience and peer-referral (snowball) sampling strategy»
2. отклик: **unclear** — Only the number of responses collected (596) is given; no response rate and no comparison of non-responders — Method, Participants and procedure — «From 596 responses collected, we removed 31 (5.2%)»
3. валидная шкала зависимости от ИИ: **yes** — Ad hoc 4-item scale built for this study, but this report gives a validation: CFA, CR, AVE, discriminant validity and cross-validation in an independent sample — Method, Measures; Table 3 — «all scales were developed for this study following suggestions of Du (2024), such as item development informed by established conceptualizations, expert conten…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.91 in this sample — Table 3 — «AI dependency (DEP) | 4 | 3.89 (1.46) | 0.91 | 0.91 | 0.71»
5. валидные шкалы коррелятов: **no** — Impulsivity (2 items) and AI anxiety/FOMO (6 items) were scales developed for this study, not published instruments. The report does give psychometric evidence for them. — Method, Measures — «all scales were developed for this study»
6. качество данных: **yes** — A stated rule removed non-users and anyone who finished in under 60 s — Method, Participants and procedure — «yielding a clean analytic sample of N = 565 in which no respondent was a non-user or sub-60-s completer»

Правки:
- 

Проверено: да

---

## ST033 · Jiang 2026 · Psychology research and behavior management

Основной отчёт R1122: [текст](../../fulltext/text/R1122.txt) — «Is Higher Academic Workload Associated with AI Dependency? Investigating the Roles of Academic Anxiety, Procrastination, and Satisfaction with AI.» — [DOI](https://doi.org/10.2147/prbm.s634780)
Расхождения в тексте: (1) Recruitment: the Methods say the link was spread via WeChat/QQ to undergraduates from Suzhou, but the Limitations say participants came from 'one university in Suzhou'. (2) The abstract and Table 3 give a total β = 0.35, while the separate direct-effect model in the text gives β = 0.34. (3) Some numbers in the Figure 3 description do not match Table 4. The figure text says AA→AID = .24 and AP→AID = .18 (and also labels AP→AID .23), while Table 4 gives AA→AID = 0.18, AP→AID = 0.23 and AA→AP = 0.35. These are SEM paths and were not extracted. (4) The text calls the 91.5% rate a 'valid-response rate', but it is based on completers, not on everyone invited.
Заметка ИИ: One cross-sectional sample (n = 690). Three zero-order Pearson correlations come from Table 2. SEM paths and moderation and indirect effects were not extracted. Satisfaction with AI and prior AI experience are not dictionary constructs.

### ST033-1 · Undergraduate students, Suzhou, China, online survey (n=690)
Отчёты: R1122 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1122_1 · total (T1) | **procrastination** · Academic procrastination scale (Wohl et al., 3 items) | pearson | **0.36** | **690** | 1 | Table 2 | «8. AID / 2.90 / 0.68 / −0.07 / 0.17** / 0.19*** / 0.12** / 0.32*** / 0.35*** / 0.36*** / –» |
| E2 | ADHOC_R1122_1 · total (T1) | **academic_stress** · Academic Anxiety Scale (Cassady et al., 11 items) | pearson | **0.35** | **690** | 1 | Table 2 | «8. AID / 2.90 / 0.68 / −0.07 / 0.17** / 0.19*** / 0.12** / 0.32*** / 0.35*** / 0.36*** / –» |
| E3 | ADHOC_R1122_1 · total (T1) | **academic_stress** · Perceived academic workload scale (adapted from Peterson et… | pearson | **0.32** | **690** | 1 | Table 2 | «8. AID / 2.90 / 0.68 / −0.07 / 0.17** / 0.19*** / 0.12** / 0.32*** / 0.35*** / 0.36*** / –» |

- E1: α ИИ 0.94, α коррелята 0.89; заметка: AID x AP (column 7).
- E2: α ИИ 0.94, α коррелята 0.88; заметка: AID x AA (column 6). Academic anxiety is coded as academic_stress because the dictionary routes test/academic anxiety there, not to anxiety.
- E3: α ИИ 0.94, α коррелята 0.93; заметка: AID x AW (column 5). Whether this fits academic_stress is a judgement call: perceived academic workload/overburden is treated as academic pressure. Reviewer should confirm, and avoid double-counting with the academic anxiety row in the same sample.

**Ключевые поля выборки:**
- **n_analysed: 690** — Methods, Data Collection — «690 valid responses were retained for analysis, yielding a valid-response rate of 91.5%»
- **population: university_students** — Methods, Data Collection — «The target population consisted of undergraduate students from Suzhou, China.»
- **sampling: convenience** — Methods, Data Collection — «Participants were recruited using convenience sampling»
- **ai_system: general_chatbot** — Methods, Data Collection — «eligibility was limited to individuals with prior experience using AI tools (eg, ChatGPT, DeepSeek, Kimi, Doubao, Wenxin Yiyan)»

**Остальные поля:**
- country: CHN — Methods, Data Collection — «The target population consisted of undergraduate students from Suzhou, China.»
- data_years: 2025 — Methods, Data Collection — «data were collected through an online survey administered over three weeks from January to February 2025»
- design: cross-sectional — Limitations — «although the cross-sectional design allowed us to examine the associations among key variables»
- clinical_group: NA — NA — «NA»
- age_mean: 19.55 — Table 2 — «2. Age | 19.55 | 1.24»
- age_sd: 1.24 — Table 2 — «2. Age | 19.55 | 1.24»
- age_min: 17 — Table 1 — «Age | 17-18 | 307 | 44.4%»
- age_max: 25 — Table 1 — «23-25 | 28 | 4.1%»
- pct_female: 69.1 — Table 1 — «Female | 477 | 69.1%»
- mode: online — Methods, Data Collection — «The questionnaire was distributed via Wenjuanxing (https://www.wjx.cn/)»
- attention_checks: yes — Methods, Data Collection — «After excluding responses with excessively short completion times or invariant response patterns, 690 valid responses were retained»
- pub_status: journal — Header — «venue: Psychology research and behavior management; DOI: 10.2147/prbm.s634780»
- language: English — Full text — «Is Higher Academic Workload Associated with AI Dependency? Investigating the Roles of Academic Anxiety, Procrastination, and Satisfaction with AI»
- funding_coi: NR — NA — «NR»
- notes: Single sample. AI dependency measured with Zhang et al. AI dependency scale (symptom-based), α = 0.94. Some participants aged 17 (parental consent obtained). Satisfaction with AI and prior AI experience are not dictionary constructs and were not extracted. Academic workload coded as academic_stress (perceived overburden from studies, comparable to workload/pressure subscales of academic-stress scales); reviewer should confirm eligibility.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online via Wenjuanxing and social media. — Methods, Data Collection — «Participants were recruited using convenience sampling... The questionnaire was distributed via Wenjuanxing»
2. отклик: **unclear** — Only a valid-response rate among completers (91.5%) is given; the number invited or reached through social media is not reported, so the true response rate is unknown. — Methods, Data Collection — «A total of 754 eligible respondents completed the survey... yielding a valid-response rate of 91.5%»
3. валидная шкала зависимости от ИИ: **yes** — Published scale (Zhang et al.) with CFA reported in this sample. — Measures, AI Dependency — «AI dependency was measured using the AI dependency scale developed by Zhang et al9... CFA demonstrated good model fit: χ2/df = 4.11, CFI = 0.979, TLI = 0.961, …»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.94 in this sample. — Measures, AI Dependency — «The scale demonstrated great internal consistency (Cronbach’s α = 0.94).»
5. валидные шкалы коррелятов: **yes** — Correlates measured with published scales: academic anxiety (Cassady et al.), academic procrastination (Wohl et al.), academic workload (adapted from Peterson et al., previously validated). — Measures — «Academic anxiety was assessed using an 11-item scale developed by Cassady et al24... measured using a three-item scale developed by Wohl et al.45»
6. качество данных: **yes** — Responses with very short completion times or invariant patterns were excluded. — Methods, Data Collection — «After excluding responses with excessively short completion times or invariant response patterns»

Правки:
- 

Проверено: да

---

## ST034 · Jingjing 2026 · Scientific reports

Основной отчёт R1130: [текст](../../fulltext/text/R1130.txt) — «The impact of technostress and generative AI on EFL mathematic metacognitive reading strategies and digital classroom burnout in SDG-aligned education.» — [DOI](https://doi.org/10.1038/s41598-026-47683-4)
Не выписано ИИ: Pilot group of EFL students (n = 30) used only to check the wording of the instrument; it has no AI-dependence correlations. Correlates not extracted because no dictionary key fits them: technostress (the dictionary excludes it from stress), generative AI usage, reading motivation, metacognitive reading strategies and SDG integration. The marker variable General Technology Anxiety (3 items) is technology anxiety, not AI anxiety, and no correlation with AI dependence is reported for it.
Расхождения в тексте: Table 2 (described as SPSS Pearson correlations "between all seven latent constructs") and Table 5 (Fornell-Larcker latent correlations) give identical off-diagonal values. So it is not clear whether the observed and latent coefficients really differ. Both rows are extracted as the rules require. Figure 3 (radar plot) shows the same correlations graphically; nothing was extracted from it. The text refers to Table 6 for the path results and to Table 7 for the HTMT and mediation results, but the HTMT is in Table 6, the paths in Table 7 and the mediation in Table 8. Simple slope at low self-efficacy: the text gives p = 0.001, Table 8 gives p < 0.001. The sample is called "EFL mathematic" students, but the reported majors are English (58%), Business English (24%) and Translation (18%).
Заметка ИИ: Only one eligible pair was found: perceived AI dependency with reading self-efficacy. It is extracted twice, as an observed (Pearson) row and a latent (Fornell-Larcker) row. Age, sex and data years are not reported.

### ST034-1 · EFL (mathematics context) undergraduates, three public universities, Eastern/Southern China, n=392
Отчёты: R1130 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1130_1 · total (T4) | **self_efficacy** · Reading Self-Efficacy (adapted from Pei & O'Brien; total of… | pearson | **-0.21** | **392** | 1 | Table 2 | «5. Reading self-efficacy / − 0.42** / − 0.21** / 0.05 / 0.61** / 1» |
| E2 | ADHOC_R1130_1 · total (T4) | **self_efficacy** · Reading Self-Efficacy (adapted from Pei & O'Brien) | latent | **-0.21** | **392** | 1 | Table 5 (Fornell-Larcker) | «(5) Reading self-efficacy / -0.42 / -0.21 / 0.05 / 0.61 / 0.77» |

- E1: **направление: as named (Perceived Difficulty items reverse-coded so that higher = higher self-efficacy)**; α ИИ 0.9, α коррелята 0.95; заметка: Reading self-efficacy is domain-specific academic self-efficacy; reviewer to confirm eligibility. The text calls the Table 2 values Pearson correlations between latent constructs, computed in SPSS. Two decimals only.
- E2: α ИИ 0.9, α коррелята 0.95; заметка: Identical to the Table 2 value; it may be the same coefficient reported twice.

**⚠ Проверка скриптом (обратите внимание):**
- E1: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление
- в независимом проходе были ещё числа: 0.38 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 392** — Findings, Table 2 description — «Correlations were computed using SPSS version 28 based on data from 392 respondents»
- **population: university_students** — Abstract — «collecting data via an online survey from n = 392 EFL mathematic university students»
- **sampling: convenience** — Methodology, Data and sampling — «a purposive sampling strategy was employed... Participants were recruited over eight weeks via institutional channels (e.g., university learning management systems and instructor referrals)»
- **ai_system: general_chatbot** — Methodology, Data and sampling — «self-reported, practical experience using generative AI tools (ChatGPT, ERNIE Bot, or similar platforms) for academic tasks»

**Остальные поля:**
- country: CHN — Methodology, Data and sampling — «from three public universities in Eastern and Southern China»
- data_years: NR — Methodology, Data and sampling — «Participants were recruited over eight weeks via institutional channels»
- design: cross-sectional — Methodology, Research design — «This study employed a quantitative research design using a cross-sectional survey»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Methodology, Data and sampling — «61% were in their second or third year of undergraduate study»
- age_sd: NR — Methodology, Data and sampling — «NR»
- age_min: NR — Methodology, Data and sampling — «NR»
- age_max: NR — Methodology, Data and sampling — «NR»
- pct_female: NR — Methodology, Data and sampling — «NR»
- mode: online — Methodology, Data collection procedure — «Data were collected through a structured online questionnaire hosted on the Qualtrics XM platform»
- attention_checks: yes — Methodology, Data collection procedure — «removing responses completed in an implausibly short time (under 4 min), identifying and eliminating straight-lining patterns in Likert-scale sections»
- pub_status: journal — Header (Scientific Reports, 2026) — «Year: 2026; venue: Scientific reports; DOI: 10.1038/s41598-026-47683-4»
- language: English — Full text — «The impact of technostress and generative AI on EFL mathematic metacognitive reading strategies and digital classroom burnout in SDG-aligned education»
- funding_coi: No funding; authors declare no competing interests — Funding; Competing interests — «This article did not receive funding. ... The authors declare no competing interests.»
- notes: The sample was screened for active generative AI use: 82% used AI at least weekly and 45% daily. The instrument was given in English only. AI dependence: 8-item scale adapted from Zhang et al. (M = 3.82, SD = 0.91).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive/convenience recruitment via institutional channels and instructor referrals at three universities. — Methodology, Data and sampling — «a purposive sampling strategy was employed... recruited over eight weeks via institutional channels (e.g., university learning management systems and instructo…»
2. отклик: **unclear** — Number invited not reported; only a recruitment funnel (605 views, 470 entries, 415 completions, 392 valid) is given; no non-responder comparison. — Methodology, Data and sampling — «392 complete and valid responses from a recruitment funnel with approximately 605 survey views, 470 entries, and 415 completions»
3. валидная шкала зависимости от ИИ: **yes** — 8-item scale adapted from Zhang et al. (published source); psychometric evidence in this sample (alpha .90, CR .92, AVE .59, Fornell-Larcker, HTMT). Reviewer to confirm, as the job codes the instrument as study-specific. — Measurement tools; Table 3 — «Perceived AI Dependency, another independent variable, was assessed with an 8-item scale adapted from Zhang et al.,41.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.90 for Perceived AI dependency in this sample. — Table 3 — «Perceived AI dependency | 0.9 | 0.92 | 0.59»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (reading self-efficacy) was adapted from a published scale (Pei and O'Brien). — Measurement tools — «The moderating variable, Reading Self-Efficacy, was adapted from Pei and O'Brien43 and comprised three dimensions: Perceived Difficulty (5 items), Enjoyment (5…»
6. качество данных: **yes** — Responses were screened for completion time, straight-lining and missing data. — Methodology, Data collection procedure — «removing responses completed in an implausibly short time (under 4 min), identifying and eliminating straight-lining patterns in Likert-scale sections, and fil…»

Правки:
- 

Проверено: да

---

## ST035 · Kaur 2026 · International Journal of Science and Research (IJSR)

Основной отчёт R1201: [текст](../../fulltext/text/R1201.txt) · [PDF](../../fulltext/pdf/R1201.pdf) — «The Effect of AI Dependence on Self Esteem and Attention Span among University Students» — [DOI](https://doi.org/10.21275/mr251202200657)
Расхождения в тексте: 1) The abstract reports correlations 'ranging from -.15 to -.33' between self-esteem and 'AI opinion, AI study, and AI creativity'. No such subscale correlations appear in any table, and these labels do not match the GAIDS subscales. Only the total-score correlation (r = -.169, Table 4) is reported, and only that value was extracted. 2) The interpretation of Table 5 says higher AI dependence goes with 'slightly better attention scores'. This contradicts the MWQ scoring (higher = more mind-wandering) and the Discussion, which reads it as less attention. The coefficient (.231) itself is the same in the table and the text. 3) Age: the Methods say ages 18–30, Table 1 uses bands 18-24 and 25-31, and Table 3 gives min 18, max 28. Table 3 was used. 4) The scale is called 'Generative AI Dependence Scale (GAIDS)' in the Methods and 'General AI Dependence Scale'/'GAI' in the Results. 5) The Resul…
Заметка ИИ: One sample, one eligible effect: GAIDS total × RSES self-esteem, r = -.169, n = 208. The report is thin on methods: no reliability values, no data years, no funding statement, and the claim of random sampling is not supported by the recruitment description.

### ST035-1 · University students, India (Lovely Professional University author), online survey, n=208
Отчёты: R1201 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **self_esteem** · Rosenberg Self-Esteem Scale (RSES; labelled RES in table) | pearson | **-.169** | **208** | 1 | Page 4, Table 4 | «GAI Pearson Correlation 1 -.169* Sig. (2-tailed) .015 N 208 208» |

- E1: заметка: Exposure is labelled 'GAI' (General AI Dependence Scale) in the results; it is the GAIDS total score.

**Ключевые поля выборки:**
- **n_analysed: 208** — Page 4, Table 4 — «GAI Pearson Correlation 1 -.169* Sig. (2-tailed) .015 N 208 208»
- **population: university_students** — Page 4, Result — «The analysis was based on responses from N = 208 university students.»
- **sampling: convenience** — Page 3, Sample and sampling technique; Page 4, Procedure — «The researchers used random sampling to select university students aged 18–30 years. ... An online survey that was sent out through institutional email, pages of social media and academic group chats»
- **ai_system: ai_unspecified** — Page 3, Inclusion criteria; Tools (a) — «students aged 18 years and above who actively utilize AI tools for academic tasks such as writing, research, or editing ... reliance on generative AI tools for academic and cognitive tasks»

**Остальные поля:**
- country: IND — Page 1, author affiliation — «Lovely Professional University, Jalandhar, Punjab, India»
- data_years: NR — Page 4, Procedure — «An online survey that was sent out through institutional email, pages of social media and academic group chats was used for data collection.»
- design: cross-sectional — Page 3, Research Design; Page 5, Limitations — «Study examines data at one point in time, doesn't give cause-and-effect relationships.»
- clinical_group: NA — NA — «NA»
- age_mean: 21.260 — Page 4, Table 3 — «Age 208 18.0 28.0 21.260 1.7720»
- age_sd: 1.7720 — Page 4, Table 3 — «Age 208 18.0 28.0 21.260 1.7720»
- age_min: 18 — Page 4, Table 3 — «Age 208 18.0 28.0 21.260 1.7720»
- age_max: 28 — Page 4, Table 3 — «Age 208 18.0 28.0 21.260 1.7720»
- pct_female: 79.8 — Page 4, Table 2 — «Female 166 79.8 79.8 100.0»
- mode: online — Page 4, Procedure — «An online survey that was sent out through institutional email, pages of social media and academic group chats was used for data collection.»
- attention_checks: NR — Page 4, Procedure; Page 3, Exclusions — «The responses were recorded automatically and screened for completeness before being prepared for analysis.»
- pub_status: journal — Page 1, header — «International Journal of Science and Research (IJSR) ... Fully Refereed | Open Access | Double Blind Peer Reviewed Journal»
- language: English — Full text — «The Effect of AI Dependence on Self Esteem and Attention Span among University Students»
- funding_coi: NR (no funding or conflict-of-interest statement) — Full text — «NR»
- notes: Sampling is called 'random sampling', but recruitment was an open online survey sent by email, social media and group chats, so I coded it as convenience. The reviewer should confirm this. The report does not cite GAIDS and does not report its items or response format. GAI scores range from 11 to 55, which fits 11 items on a 5-point scale. No reliability coefficients are given for any scale. The country is taken from the author's affiliation; the report never states where the sample came from. AI system: 'AI tools' / 'generative AI tools' for academic tasks; coded ai_unspecified (general_chat…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Called 'random sampling', but no sampling frame is described and the survey was spread through email, social media and academic group chats. This is online convenience recruitment. — Page 3, Sample; Page 4, Procedure — «The researchers used random sampling ... An online survey that was sent out through institutional email, pages of social media and academic group chats»
2. отклик: **unclear** — No response rate is reported and non-responders are not described. — Page 3, Sample — «A grand total of respondents voluntarily filled the questionnaires.»
3. валидная шкала зависимости от ИИ: **yes** — GAIDS has a published validation study (Goh, Hartanto & Majeed, 2025, per the job's instrument list). The report names the scale but gives no citation. — Page 3, Tools (a) — «Generative AI Dependence Scale (GAIDS): This scale measured the extent of participants' reliance on generative AI tools for academic and cognitive tasks.»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega is reported for GAIDS, even though the Results say a reliability analysis is included. — Page 4, Result — «The descriptive statistics, reliability analysis, and correlation results for the variables under study»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, self-esteem, was measured with the published Rosenberg Self-Esteem Scale. — Page 3, Tools (b) — «Rosenberg Self-Esteem Scale (RSES; Rosenberg, 1965): The RSES is a 10-item scale widely used to measure global self-esteem.»
6. качество данных: **unclear** — Only completeness screening is reported: incomplete questionnaires were excluded. There were no attention checks and no careless-responding screening. — Page 4, Procedure; Page 3, Exclusions — «The responses were recorded automatically and screened for completeness before being prepared for analysis.»

Правки:
- 

Проверено: да

---

## ST036 · Kim 2026 · Humanities and Social Sciences Communications

Основной отчёт R1277: [текст](../../fulltext/text/R1277.txt) · [PDF](../../fulltext/pdf/R1277.pdf) — «“Overdependence on algorithms?”: how artificial intelligence ethical leadership can safeguard self-efficacy and spur innovation» — [DOI](https://doi.org/10.1057/s41599-026-08430-2)
Не выписано ИИ: Pilot sample of 200 employees from technology-intensive firms (used only for validating the adapted AI ethical leadership scale; no AI-dependence correlations reported). The T1 (963) and T2 (659) respondents who dropped out were not analysed separately.
Лонгитюд (для описания): Three-wave time-lagged design (8–9 weeks between waves): AI dependence and AI ethical leadership at T1, self-efficacy at T2, innovative behavior at T3. Each construct was measured only once, so there are no cross-lagged or autoregressive paths. SEM (controls: gender, education, tenure, position): AI dependence T1 -> self-efficacy T2 β = -0.310 (p < .001); self-efficacy T2 -> innovative behavior T3 β = 0.361 (p < .001); direct AI dependence T1 -> innovative behavior T3 β = -0.074 (ns); indirect effect -0.112, 95% CI [-0.166, -0.067]. AI dependence × AI ethical leadership on self-efficacy β = 0.257 (p < .001); simple slopes -0.407 (low leadership) and -0.041 (high leadership, ns).
Расхождения в тексте: (1) The text gives the total effect of AI dependence on innovative behavior without the mediator as β = 0.006 (p = .915), but Table 4 gives a total effect of -0.186 (direct -0.074 + indirect -0.112). (2) The text describes the intervals as 'eight to nine weeks' (pp. 16-17) and also as 'eight-week intervals' (p. 27). (3) The text says marker-variable correlations (r = -.02, -.03, .04, .06) are 'presented in the correlation matrix', but Table 2 does not contain the marker variable. (4) The Table 3 note says 'Estimate indicates standardized coefficients', but the table has both unstandardized and standardized columns. (5) The Table 2 education coding skips code 4 (1, 2, 3, 5). (6) The Table 2 AI dependence–innovative behavior correlation (-0.02) matches the non-significant direct effect. No figures contain coefficients that are not also given in text or tables.
Заметка ИИ: There is one sample. The only correlate that fits the dictionary is general self-efficacy (T2). AI ethical leadership and innovative behavior are not dictionary constructs and were not extracted. The AI dependence–self-efficacy correlation crosses occasions (T1–T2).

### ST036-1 · South Korean full-time employees, online panel, three-wave time-lagged (n=421)
Отчёты: R1277 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | TANG3 · total (T2) | **self_efficacy** · General Self-Efficacy Scale (Chen, Gully & Eden, 2001), 5 i… | pearson | **-0.16** | **421** | lagged: T1-T2 | Table 2, p. 49 | «7. SE_T2 3.76 0.69 .671 .911 -0.04 0.08 0.11* 0.12* -0.16** 0.23** .819» |

- E1: α ИИ 0.811, α коррелята 0.910; заметка: AI dependence measured at T1, self-efficacy at T2 (8–9 weeks later); no same-occasion correlation exists. Table 2 is a correlation matrix with sqrt(AVE) on the diagonal (Fornell-Larcker); because it also contains observed demographics it is coded as observed Pearson — reviewer to confirm it is not …

**⚠ Проверка скриптом (обратите внимание):**
- E1: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: 421** — Method, p. 17; Table 5 notes — «The final dataset comprised 421 complete responses across all three time points.»
- **population: employees** — Method, p. 16 — «The sample was comprised of a heterogeneous set of working professionals who were at least 20 years old and derived from numerous organizations situated throughout South Korea.»
- **sampling: quota or online panel** — Method, pp. 17-18 — «Data collection was facilitated through a reputable online research platform possessing a vast panel of approximately 6.05 million potential respondents.»
- **ai_system: ai_unspecified** — Measures, p. 20 — «I depended on AI to handle or help with work-related activities ... reflecting the extent to which employees incorporate AI tools into their daily tasks»

**Остальные поля:**
- country: KOR — Abstract, p. 2 — «data collected from 421 full-time employees in South Korea via a three-wave time-lagged research design»
- data_years: NR — Method, pp. 16-17 — «Approximately eight to nine weeks after the first wave, the second phase (T2) was administered»
- design: panel — Method, p. 15 — «this study adopted a three-wave time-lagged research design»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1, p. 48 — «Age (years) 20–29 21.6% 30–39 23.2% 40–49 27.6% 50–59 27.6%»
- age_sd: NR — Table 1, p. 48 — «Age (years) 20–29 21.6% 30–39 23.2% 40–49 27.6% 50–59 27.6%»
- age_min: 20 (eligibility criterion; youngest category 20–29) — Method, p. 16; Table 1 — «working professionals who were at least 20 years old»
- age_max: NR (oldest age category reported is 50–59) — Table 1, p. 48 — «50–59 27.6%»
- pct_female: 48.0 — Table 1, p. 48 — «Gender Men 52.0% Women 48.0%»
- mode: online — Method, p. 17 — «Data collection was facilitated through a reputable online research platform»
- attention_checks: yes — Method, pp. 17-18 — «monitoring of response times to identify rapid guessers ... analyzing response patterns for invariance, and verifying that survey completion times fell within …»
- pub_status: journal — Page 1 — «Humanities and Social Sciences Communications Article in Press»
- language: English — Full text — «We tested our hypotheses using data collected from 421 full-time employees in South Korea»
- funding_coi: Korea Institute for Advancement of Technology (KIAT) grant funded by Korea Government (MOTIE) (RS-2024-00415520); authors declare no competing interests — Ethics declarations / Funding, pp. 46-47 — «This paper was supported by Korea Institute for Advancement of Technology (KIAT) grant funded by the Korea Government (MOTIE) (RS-2024-00415520, HRD Program fo…»
- notes: Stratified random sampling was used within an online panel. Participants were paid about $10–11. The IRB approval number (202208-HR-2975-01) suggests approval in 2022, but the data collection years are not reported. Retention from T1 to T3 was 43.72% (421 of 963).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online research panel; stratified sampling from a commercial online panel, not a probability sample of a defined population. — Method, pp. 17-18 — «Data collection was facilitated through a reputable online research platform possessing a vast panel of approximately 6.05 million potential respondents.»
2. отклик: **yes** — Retention 43.72% (<60%), but completers and dropouts were compared (attrition analysis, no significant differences). Initial panel response rate not reported. — Method, pp. 17-18 — «We conducted a systematic attrition analysis ... no statistically significant differences in key demographic characteristics or focal variables between those w…»
3. валидная шкала зависимости от ИИ: **yes** — Published 3-item scale from Tang et al. (2023); CFA-based CR and AVE reported in this report. — Measures, p. 20; Measurement Model, p. 25 — «AI dependence was measured using a three‐item scale drawn from Tang, Koopman, Yam, De Cremer, Zhang, and Reynders (2023)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .811 in this sample. — Measures, p. 20 — «The reliability of this scale, as indicated by Cronbach’s alpha, was 0.811.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (self-efficacy) was measured with the published, validated general self-efficacy scale of Chen, Gully & Eden (2001), 5 items used. — Measures, p. 21 — «Self‐efficacy was evaluated utilizing the general self‐efficacy scale developed and validated by Chen, Gully, and Eden (2001).»
6. качество данных: **yes** — Response-latency screening, detection of unconscientious response patterns, invariance screening and completion-time checks. — Method, pp. 17-18 — «This wave included further verification steps to confirm participant eligibility and detect unconscientious response patterns.»

Правки:
- 

Проверено: да

---

## ST037 · Kong 2026 · Frontiers in psychology

Основной отчёт R1298: [текст](../../fulltext/text/R1298.txt) — «From cognitive need to problematic use: a chained mediation path moderated by academic stress and AI literacy.» — [DOI](https://doi.org/10.3389/fpsyg.2026.1767454)
Лонгитюд (для описания): This is a two-wave, time-lagged design with a 4-week interval. Problematic GenAI use was measured only at T2, so there are no cross-lagged or autoregressive paths. SEM paths (not extracted): NFC(T1) -> positive affect(T1) β = −0.41; positive affect(T1) -> avoidance motivation(T2) β = 0.45; positive affect(T1) -> problematic use(T2) β = 0.25; avoidance motivation(T2) -> problematic use(T2) β = 0.30. Academic stress × avoidance motivation interaction β = 0.15. AI literacy × avoidance motivation interaction β = −0.12. Conditional serial indirect effects are given in Table 2.
Расхождения в тексте: 1. The text says the highest inter-construct correlation is 0.56, but the largest value in Table 1 is 0.55. 2. The text says all correlations were statistically significant, but Table 1 shows academic stress–AI literacy = −0.05 without a star. 3. Table 1 mixes formats: the diagonal holds sqrt(AVE) (Fornell-Larcker), while the data-analysis section says the correlations were run in SPSS. It is unclear whether the off-diagonal values are observed or latent correlations. 4. No Cronbach's alpha is reported for Avoidance-Oriented GenAI Motivation, although the analysis plan says alphas were computed for all scales. 5. Excluding questionnaires with significant missing data conflicts with the stated use of FIML. 6. In Table 2, the index of moderated mediation for academic stress (−0.028) is identical to the low-stress conditional indirect effect, which may be a reporting error. 7. The Figure 2…
Заметка ИИ: Funding and conflict-of-interest statements are absent from the supplied text. Data-collection years are not reported. Both effects come from Table 1, and both measures in each pair were taken at T2.

### ST037-1 · University students, one large comprehensive university, China, two-wave (N = 452)
Отчёты: R1298 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1298_1 · total (T1) | **academic_stress** · Perceived Academic Stress (5-item, adapted from PSS, academ… | pearson | **0.30** | **452** | 2 | Table 1 | «6. Problematic use of GenAI (T2) / 3.48 / 0.85 / −0.28** / 0.35** / 0.55** / 0.30** / −0.25** / (0.79)» |
| E2 | ADHOC_R1298_1 · total (T1) | **escapism_motive** · Avoidance-Oriented GenAI Motivation (adapted from AGQ-R per… | pearson | **0.55** | **452** | 2 | Table 1 | «6. Problematic use of GenAI (T2) / 3.48 / 0.85 / −0.28** / 0.35** / 0.55** / 0.30** / −0.25** / (0.79)» |

- E1: α ИИ 0.90, α коррелята 0.87; заметка: Both measures are from T2, the only occasion problematic use was measured, so this is the only same-occasion r; the reviewer decides whether to treat it as primary. Table 1 has sqrt-AVE on its diagonal (Fornell-Larcker format), but the text says r was computed in SPSS. Coded Pearson; may be latent.
- E2: α ИИ 0.90, α коррелята NR; заметка: Borderline fit to escapism_motive: a GenAI-specific motive to avoid difficult tasks, adapted from an achievement-goal scale and framed by the authors as an escape or coping route. The reviewer should confirm eligibility. No alpha (CR = 0.86). Both measures at T2. Pearson vs latent status is ambiguo…

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2: поздняя волна: в основной анализ не идёт, только в описание
- E2: этого числа нет в независимом проходе ИИ по полному тексту — сверьте с таблицей

**Ключевые поля выборки:**
- **n_analysed: 452** — Table 1 note — «N = 452. T1, Time 1; T2, Time 2.»
- **population: university_students** — Method, Participants and procedure — «The sample included 315 undergraduate students (69.7%) and 137 graduate students (30.3%).»
- **sampling: convenience** — Method, Participants and procedure — «Participants were recruited through university-wide email lists and course announcements, with participation being voluntary.»
- **ai_system: general_chatbot** — Method, Participants and procedure; Introduction — «All participants reported using Generative AI tools for academic purposes at least once a week. [Intro: Generative Artificial Intelligence (GenAI), exemplified by models like ChatGPT]»

**Остальные поля:**
- country: CHN — Method, Participants and procedure — «The target population consisted of undergraduate and graduate students from a large, comprehensive university in China.»
- data_years: NR — Method, Participants and procedure — «The initial online survey was administered at the beginning of the academic semester.»
- design: panel — Method, Participants and procedure — «This study employed a two-wave, time-lagged survey design»
- clinical_group: NA — NA — «NA»
- age_mean: 21.4 — Method, Participants and procedure — «with a mean age of 21.4 years (SD = 2.8)»
- age_sd: 2.8 — Method, Participants and procedure — «with a mean age of 21.4 years (SD = 2.8)»
- age_min: 18 — Method, Participants and procedure — «The age of the participants ranged from 18 to 28 years»
- age_max: 28 — Method, Participants and procedure — «The age of the participants ranged from 18 to 28 years»
- pct_female: 58.0 — Method, Participants and procedure — «The final sample consisted of 262 females (58.0%) and 190 males (42.0%).»
- mode: online — Method, Participants and procedure — «Time 1 (T1): The initial online survey was administered at the beginning of the academic semester.»
- attention_checks: yes — Method, Participants and procedure — «Questionnaires with significant missing data or from participants who failed an attention-check item were excluded.»
- pub_status: journal — Header — «venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2026.1767454»
- language: English — Full text — «From cognitive need to problematic use: a chained mediation path moderated by academic stress and AI literacy»
- funding_coi: NR — NA — «NA»
- notes: This is a two-wave design, and problematic GenAI use was measured only at T2 (4 weeks after T1). The 452 analysed students are the matched T1+T2 completers from 580 T1 respondents. The eligible correlates were both measured at T2 alongside the exposure. Funding and COI statements are not in the supplied text.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Voluntary convenience sample from one university recruited via email lists and course announcements. — Method, Participants and procedure — «Participants were recruited through university-wide email lists and course announcements, with participation being voluntary.»
2. отклик: **unclear** — Initial response rate to invitations not reported; T1 to T2 retention 77.9% (452/580), but T2 completers were not compared with dropouts. — Method, Participants and procedure — «This resulted in a final matched sample of 452 students (77.9% retention rate)»
3. валидная шкала зависимости от ИИ: **yes** — 7-item scale adapted from PIUQ (Demetrovics et al., 2008) for GenAI; validity evidence from CFA in this report (CR = 0.91, AVE = 0.63). The reviewer may want to downgrade, since the GenAI adaptation has no separate vali… — Measures; Measurement model — «measured using a 7-item scale adapted from the Problematic Internet Use Questionnaire (PIUQ; Demetrovics et al., 2008)... Problematic Use of GenAI: CR = 0.91, …»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.90 in this sample. — Measures — «The scale demonstrated excellent internal consistency (α = 0.90).»
5. валидные шкалы коррелятов: **yes** — Both extracted correlates are adapted from published instruments (academic stress from the PSS; avoidance motivation from the AGQ-R), and this report gives CFA validity evidence (CR/AVE). However, both are contextualise… — Measures; Measurement model — «5-item scale adapted from the Perceived Stress Scale (PSS; Cohen et al., 1983) and contextualized for the academic environment»
6. качество данных: **yes** — Attention-check item used; failing responses excluded. — Method, Participants and procedure — «from participants who failed an attention-check item were excluded»

Правки:
- 

Проверено: да

---

## ST038 · Korkmaz 2026 · BMC medical education

Основной отчёт R1299: [текст](../../fulltext/text/R1299.txt) — «Untold stories of digital transformation in medical education: AI overdependence and nomophobia among medical students.» — [DOI](https://doi.org/10.1186/s12909-026-08675-0)
Расхождения в тексте: (1) DAI CFA reports χ²=148.549 with df=43. A one-factor model with 5 items has only 5 df, so the reported df does not fit the 5-item scale. NMP-Q CFA in this sample reports df=125; the original pretest reports df=164 for 20 items in 4 factors. (2) Year 2 percentage: the Participants text gives 28.7%, Table 1 gives 28.2% (275/958 = 28.7%). (3) The text says students 'have low levels of nomophobia', but Table 5 puts most students (552/958) at a moderate level. The nomophobia cut-offs in the text leave a gap between 50.99 and 60. (4) The Discussion refers to 'losing convenience'; Table 4 labels the subscale 'Giving Up Convenience'. (5) Table 5 labels the significant difference 'Light < Middle, Light < High' while its rows are labelled Low/Moderate/High. (6) The nomophobia B in the multiple regression (0.012, Table 7) is a multivariable coefficient and was not extracted. Fig. 1 (interaction…
Заметка ИИ: Nomophobia (NMP-Q) is the only correlate. It is not named in the construct dictionary. I coded it provisionally as problematic_smartphone_use, and the reviewer should decide whether it is eligible. NMP-Q subscale correlations are extracted alongside the total score, so the reviewer should guard against double counting. Age and data-collection years are not reported.

### ST038-1 · Medical students, six universities, Turkey (n=958)
Отчёты: R1299 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **problematic_smartphone_use** · Nomophobia Questionnaire (NMP-Q), total | pearson | **0.127** | **958** | 1 | Table 4 | «AI Dependence*Nomophobia / 958 / 0.127 / < 0.001» |
| E2 | DAI · total (T4) | **problematic_smartphone_use** · NMP-Q Not Being Able to Access Information subscale | pearson | **0.172** | **958** | 1 | Table 4 | «AI Dependence*Not being able to Access Information / 958 / 0.172 / < 0.001» |
| E3 | DAI · total (T4) | **problematic_smartphone_use** · NMP-Q Giving Up Convenience subscale | pearson | **0.136** | **958** | 1 | Table 4 | «AI Dependence* Giving Up Convenience / 958 / 0.136 / < 0.001» |
| E4 | DAI · total (T4) | **problematic_smartphone_use** · NMP-Q Not Being Able to Communicate subscale | pearson | **0.009** | **958** | 1 | Table 4 | «AI Dependence* Not Being Able to Communicate / 958 / 0.009 / 0.776» |
| E5 | DAI · total (T4) | **problematic_smartphone_use** · NMP-Q Losing Connectedness subscale | pearson | **0.153** | **958** | 1 | Table 4 | «AI Dependence* Losing Connectedness / 958 / 0.153 / < 0.001» |

- E1: α ИИ 0.817 (omega 0.806), α коррелята 0.932 (omega 0.923); заметка: Mapping of nomophobia to problematic_smartphone_use is a judgement call (nomophobia not listed in the dictionary; the abstract describes it as signs of smartphone addiction). Reviewer to confirm eligibility.
- E2: α ИИ 0.817 (omega 0.806), α коррелята NR; заметка: NMP-Q subscale; same mapping caveat. Subscale alphas given in the text (0.90, 0.74, 0.94, 0.91) come from the original pretest, not this sample.
- E3: α ИИ 0.817 (omega 0.806), α коррелята NR; заметка: NMP-Q subscale; same mapping caveat.
- E4: α ИИ 0.817 (omega 0.806), α коррелята NR; заметка: NMP-Q subscale; same mapping caveat.
- E5: α ИИ 0.817 (omega 0.806), α коррелята NR; заметка: NMP-Q subscale; same mapping caveat.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 14.61 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 958** — Table 4 — «AI Dependence*Nomophobia | 958 | 0.127 | < 0.001»
- **population: university_students** — Participants — «The inclusion criteria were being a student enrolled in a medical school in Turkey and willing to participate in this study voluntarily.»
- **sampling: convenience** — Data collection process — «Medical educators from various medical schools were contacted by the researchers, and the students representatives from those medical schools assisted in disseminating the Google Forms link to ensure broad participation.»
- **ai_system: general_chatbot** — Table 1 — «What AI tools do you use? | ChatGPT, Google GeminiFlash, Deep Seek | 58(6.1) ... ChatGPT, Copilot | 31(3.2) ChatGPT | 708(73.9) Google GeminiFlash | 38(4)»

**Остальные поля:**
- country: TUR — Participants — «The participants consisted of medical students from six different universities (four public and two foundation universities) in Turkey.»
- data_years: NR — Ethics committee approval — «approval of the İstanbul Medeniyet University Scientific Research Ethics Committee (Date of Approval: 22.01.2025/No: 2025/02–04)»
- design: cross-sectional — Methods — «This study, which adopted a quantitative correlational research design»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 57 — Participants; Table 1 — «Of the 958 participating students, 546 (57%) are female and 412 (43%) are male.»
- mode: online — Data collection process — «Data were collected online via Google Forms.»
- attention_checks: NR — Data collection process; Data analysis — «Participation was voluntary, and responses remained anonymous to protect confidentiality.»
- pub_status: journal — Header — «BMC medical education; DOI: 10.1186/s12909-026-08675-0»
- language: English — Full text — «Untold stories of digital transformation in medical education: AI overdependence and nomophobia among medical students»
- funding_coi: No funding; authors declare no competing interests — Funding; Competing interests — «This study was not funded by any organizations or institutions. ... The authors declare no competing interests.»
- notes: Data-collection years are not reported; ethics approval is dated 22.01.2025. The DAI was administered in its Turkish adaptation (Savaş). Age is not reported. The only correlate, nomophobia, is mapped provisionally to problematic_smartphone_use.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample; online Google Forms link distributed by student representatives. — Data collection process — «the students representatives from those medical schools assisted in disseminating the Google Forms link to ensure broad participation»
2. отклик: **unclear** — Response rate and number invited not reported. — Participants — «Of the 958 participating students, 546 (57%) are female»
3. валидная шкала зависимости от ИИ: **yes** — DAI is a published scale (Morales-García et al., 2024) with Turkish adaptation; CFA also reported in this sample. — Dependence on artificial intelligence scale (DAI) — «This five-item Likert scale was developed by Morales-García et al. [31] and adapted into Turkish by Savaş [32]»
4. надёжность шкалы ИИ в выборке: **yes** — Alpha .817 and omega .806 in this sample. — Dependence on artificial intelligence scale (DAI) — «Cronbach’s Alpha was found to be 0.817 and McDonald’s Omega was 0.806.»
5. валидные шкалы коррелятов: **yes** — Nomophobia measured with the published NMP-Q (Yıldırım & Correia), Turkish adaptation. — Nomophobia questionnaire (NMP-Q) — «Nomophobia questionnaire was developed by Yıldırım and Correia [23] and adapted into Turkish by Yıldırım et al. [36].»
6. качество данных: **unclear** — No attention checks, careless-responding screening or exclusion rule reported. — Data collection process; Data analysis — «Data were collected online via Google Forms.»

Правки:
- 

Проверено: да

---

## ST039 · Li 2026 · Frontiers in psychology

Основной отчёт R1431: [текст](../../fulltext/text/R1431.txt) · [PDF](../../fulltext/pdf/R1431.pdf) — «Loneliness and problematic use of conversational artificial intelligence among college students: the serial mediating roles of social anxiety and self-control.» — [DOI](https://doi.org/10.3389/fpsyg.2026.1950646)
Расхождения в тексте: The correlations in the text (3.2) match Table 3. Other issues for the reviewer: (1) Figure 1 is a placeholder ("FIGURE 1 XXX."), so no figure content can be checked. (2) Table 1 gives the first PUCAI equation F = 28.666 without significance stars, while the other F values have stars. (3) Table 2 is described as unstandardized (b), but the total effect (0.422) is close to the standardized β (0.410). Table 2 reports a significant indirect effect through social anxiety (0.025, CI [0.010, 0.061]), yet the social anxiety→PUCAI path is nonsignificant (β = 0.074, p > 0.05). That CI also looks asymmetric relative to the Boot SE of 0.018. (4) The ethics statement mentions written informed consent, while consent was given in an online questionnaire. (5) The "valid response rate of 95.0%" is relative to completed questionnaires, not to students invited. Mediation betas and path coefficients were …
Заметка ИИ: There is one sample with three zero-order Pearson correlations between the PUCAI total and loneliness, social anxiety and self-control (Table 3).

### ST039-1 · Undergraduates, one university in western China, n=400
Отчёты: R1431 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PUCAI · total (T1) | **loneliness** · UCLA Loneliness Scale (ULS-8), Chinese version | pearson | **0.411** | **400** | 1 | Page 5, Table 3 | «PUCAI / 18.198 / 4.091 / 0.411** / 0.276** / −0.346** / 1» |
| E2 | PUCAI · total (T1) | **social_anxiety** · Interaction Anxiousness Scale (IAS), Chinese adaptation | pearson | **0.276** | **400** | 1 | Page 5, Table 3 | «PUCAI / 18.198 / 4.091 / 0.411** / 0.276** / −0.346** / 1» |
| E3 | PUCAI · total (T1) | **self_control** · Self-Control Scale (SCS), Chinese revision by Tan & Guo (20… | pearson | **−0.346** | **400** | 1 | Page 5, Table 3 | «PUCAI / 18.198 / 4.091 / 0.411** / 0.276** / −0.346** / 1» |

- E1: α ИИ 0.82, α коррелята 0.81; заметка: Value matches the text in 3.2 (r = 0.411).
- E2: α ИИ 0.82, α коррелята 0.86; заметка: Value matches the text in 3.2 (r = 0.276).
- E3: α ИИ 0.82, α коррелята 0.86; заметка: Value matches the text in 3.2 (r = −0.346).

**Ключевые поля выборки:**
- **n_analysed: 400** — Page 5, Table 3 — «TABLE 3 Descriptive statistics and correlations among the study variables (n = 400).»
- **population: university_students** — Page 3, 2.1 Participants — «The survey participants included students from freshman through senior year.»
- **sampling: convenience** — Page 3, 2.1 Participants — «Using convenience sampling, undergraduate students from a university in western China were recruited»
- **ai_system: general_chatbot** — Page 2, 1 Introduction; Page 3, 2.2.2 — «Such technologies are commonly referred to as conversational artificial intelligence (CAI). ... Common examples include chatbots and smart assistants»

**Остальные поля:**
- country: CHN — Page 3, 2.1 Participants — «undergraduate students from a university in western China were recruited to complete an online questionnaire»
- data_years: NR — NR — «NR»
- design: cross-sectional — Page 1, Abstract (Methods) — «Using convenience sampling, this cross-sectional study analyzed data from 400 undergraduate students»
- clinical_group: NA — NA — «NA»
- age_mean: 20.36 — Page 3, 2.1 Participants — «Participants had a mean age of 20.36 years (SD = 1.73)»
- age_sd: 1.73 — Page 3, 2.1 Participants — «Participants had a mean age of 20.36 years (SD = 1.73)»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 30.0 — Page 3, 2.1 Participants — «with 280 identifying as male (70.0%) and 120 as female (30.0%)»
- mode: online — Page 3, 2.1 Participants — «The online questionnaire was administered through Wenjuanxing»
- attention_checks: yes — Page 3, 2.1 Participants — «(c) failure to pass attention-check questions randomly inserted by the Wenjuanxing system; and (d) abnormally short or long response times»
- pub_status: journal — Page 1, header — «Frontiers in Psychology ... TYPE Original Research PUBLISHED 30 September 2026»
- language: English — Full text — «Loneliness and problematic use of conversational artificial intelligence among college students»
- funding_coi: No funding received; authors declare no conflicts of interest — Page 8, Funding; Conflict of interest — «The author(s) declared that financial support was not received for this work and/or its publication. ... in the absence of any commercial or financial relation…»
- notes: The specific CAI systems used by participants are not named. CAI is defined broadly (chatbots and smart assistants), so ai_system = general_chatbot is a judgement call; ai_unspecified is the alternative. The university is not named in the Methods; the authors' affiliation is Xinjiang Normal University. Data collection years are not reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample from one university recruited online via Wenjuanxing through course instructors. — Page 3, 2.1 Participants — «Using convenience sampling ... The online questionnaire was administered through Wenjuanxing»
2. отклик: **unclear** — The 95.0% is the share of valid questionnaires among 421 completed ones, not a response rate among students invited; the number invited is not reported. — Page 3, 2.1 Participants — «A total of 421 completed questionnaires were obtained. ... 21 invalid responses were removed, leaving a final analytic sample of 400 and a valid response rate …»
3. валидная шкала зависимости от ИИ: **yes** — Six-item PUCAI measure from a published study (Hu et al., 2023), adapted from the validated BSMAS. The reviewer should confirm that Hu et al. reported psychometric evidence. — Page 3, 2.2.2 PUCAI scale — «PUCAI was assessed using the six-item measure reported by Hu et al. (2023). This measure was derived from the Bergen Social Media Addiction Scale»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.82 in this sample. — Page 4, 2.2.2 — «Total scores range between 6 and 30, with higher scores reflecting greater PUCAI. In this study, Cronbach's α was 0.82.»
5. валидные шкалы коррелятов: **yes** — All correlates were measured with published instruments: ULS-8, Chinese IAS (Peng et al., 2004) and Chinese SCS (Tan & Guo, 2008). — Page 3-4, 2.2.1-2.2.4 — «Loneliness was measured using the UCLA Loneliness Scale (ULS-8) ... Chinese adaptation of the Interaction Anxiousness Scale (IAS) ... Chinese Self-Control Scal…»
6. качество данных: **yes** — Attention-check items, logical-consistency screening and response-time rules were applied; 21 cases were excluded. — Page 3, 2.1 Participants — «(b) careless responses with obvious logical inconsistencies ... (c) failure to pass attention-check questions randomly inserted by the Wenjuanxing system»

Правки:
- 

Проверено: да

---

## ST040 · Li 2026 · Artificial Intelligence and Applications

Основной отчёт R1433: [текст](../../fulltext/text/R1433.txt) · [PDF](../../fulltext/pdf/R1433.pdf) — «Modeling the Double-Edged Effects of AI Companions on Chinese Generation Z: A Dual-Pathway Analysis of Risk and Protection» — [DOI](https://doi.org/10.47852/bonviewaia62027719)
Расхождения в тексте: The text example 'PHQ-9 r = 0.40; SWB r = −0.40' for the risk factors matches the BPS-9 row of Table 3, not BSMAS-6 (0.36; -0.37). The text says standardized β are reported 'with 95% confidence intervals', but Table 4 gives no CIs, and Table 3 shows no significance levels. Section 4.4 cites Table 5 for regression effects, but Table 5 is a robustness check of anthropomorphism correlations. The abstract says 'descriptive statistics as the data analysis method', yet correlations and regressions are reported. PHQ-9 and GAD-7 observed ranges are 1.00–3.00 on mean scoring, which is unusual for the 0–3 item format. Loneliness is called '8-item short form' in Measures and 'UCLA8' in the tables. No figure-only coefficients.
Заметка ИИ: One sample, five effects (BSMAS-6 adapted to the AI companion x depression, anxiety, loneliness, well-being, sleep disturbance). The reviewer should check the rob_3 rating (AI-adapted Bergen scale without its own validation) and the ad hoc sleep measure.

### ST040-1 · Xingye AI active users, Chinese Gen Z, online survey (CHN), n=402
Отчёты: R1433 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | BERGEN_ADAPTED · total (T1) | **depression** · PHQ-9 | pearson | **0.36** | **402** | 1 | p.5, Table 3 | «Predictor/outcome PHQ-9 GAD-7 UCLA8 SWB-3 Sleep3 ... BSMAS-6 0.36 0.44 0.41 -0.37 0.40» |
| E2 | BERGEN_ADAPTED · total (T1) | **anxiety** · GAD-7 | pearson | **0.44** | **402** | 1 | p.5, Table 3 | «Predictor/outcome PHQ-9 GAD-7 UCLA8 SWB-3 Sleep3 ... BSMAS-6 0.36 0.44 0.41 -0.37 0.40» |
| E3 | BERGEN_ADAPTED · total (T1) | **loneliness** · Loneliness 8-item short form (UCLA8) | pearson | **0.41** | **402** | 1 | p.5, Table 3 | «Predictor/outcome PHQ-9 GAD-7 UCLA8 SWB-3 Sleep3 ... BSMAS-6 0.36 0.44 0.41 -0.37 0.40» |
| E4 | BERGEN_ADAPTED · total (T1) | **wellbeing** · Subjective well-being, 3 life-evaluation items (SWB-3) | pearson | **-0.37** | **402** | 1 | p.5, Table 3 | «Predictor/outcome PHQ-9 GAD-7 UCLA8 SWB-3 Sleep3 ... BSMAS-6 0.36 0.44 0.41 -0.37 0.40» |
| E5 | BERGEN_ADAPTED · total (T1) | **sleep_quality** · Sleep disturbance (3 items; Sleep3) | pearson | **0.40** | **402** | 1 | p.5, Table 3 | «Predictor/outcome PHQ-9 GAD-7 UCLA8 SWB-3 Sleep3 ... BSMAS-6 0.36 0.44 0.41 -0.37 0.40» |

- E1: α ИИ 0.904, α коррелята 0.930; заметка: Zero-order correlation; type (Pearson) assumed from 'zero-order correlations', not explicitly stated. Two decimals; no significance shown.
- E2: α ИИ 0.904, α коррелята 0.898; заметка: Zero-order correlation; Pearson assumed.
- E3: α ИИ 0.904, α коррелята 0.936; заметка: Measures section says only '8-item short form'; tables label it UCLA8.
- E4: α ИИ 0.904, α коррелята 0.820; заметка: Items cited to SWLS (Diener et al., 1985) but only 3 items.
- E5: **направление: reversed (higher = more sleep disturbance)**; α ИИ 0.904, α коррелята 0.824; заметка: Ad hoc 3-item sleep disturbance measure; sign reflects disturbance, not quality.

**⚠ Проверка скриптом (обратите внимание):**
- E5: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление

**Ключевые поля выборки:**
- **n_analysed: 402** — p.4, Table 2; p.3, Table 1 — «Problematic use (BSMAS-6) 6 1.00–5.00 3.44 1.17 0.904 402»
- **population: mixed** — p.3, Table 1 — «Status Undergraduate 175 (43.5%) Status Employed 146 (36.3%) Status Unemployed/Intern 45 (11.2%) Status Graduate 36 (9.0%)»
- **sampling: NR** — p.3, 3.2 — «We ran an online survey with N = 402 active users of Xingye AI (星野·AI皆你所见) who reported use within the past month. Participation was voluntary and anonymous»
- **ai_system: ai_companion** — p.1, Abstract — «We study Xingye AI (星野·AI皆你所见), a generative emotional companion used by Chinese Gen Z.»

**Остальные поля:**
- country: CHN — p.1, Abstract; p.3, 3.2 — «We study Xingye AI (星野·AI皆你所见), a generative emotional companion used by Chinese Gen Z.»
- data_years: NR — NR — «NR»
- design: cross-sectional — p.8, Conclusion — «The data are cross-sectional and self-report, drawn from one product context; causal claims cannot be made.»
- clinical_group: NA — NA — «NA»
- age_mean: 21.51 — p.3, Table 1 — «Age (years) Mean (SD) 21.51 (2.11)»
- age_sd: 2.11 — p.3, Table 1 — «Age (years) Mean (SD) 21.51 (2.11)»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 53.5 — p.3, Table 1 — «Gender Female 215 (53.5%)»
- mode: online — p.3, 3.2 — «We ran an online survey with N = 402 active users of Xingye AI»
- attention_checks: yes — p.3, 3.2 — «standard quality checks (attention checks, excessive speed, and straight-lining) were applied before analysis.»
- pub_status: journal — p.1, header — «RESEARCH ARTICLE Artificial Intelligence and Applications 2026, Vol. 00(00) 1–10»
- language: English — whole text — «Modeling the Double-Edged Effects of AI Companions on Chinese Generation Z»
- funding_coi: Funding NR; authors declare no conflicts of interest — p.8, Conflicts of Interest — «The authors declare that they have no conflicts of interest to this work.»
- notes: Single cross-sectional sample. AI-dependence measure = 'problematic use (BSMAS-6) adapted from social/smartphone contexts'; exact AI-specific item wording not reported. Scales scored as means. Table 3 reports only predictor x outcome correlations; BSMAS-6 x bedtime procrastination (BPS-9) correlation not reported, so procrastination not extracted. Attachment, digital boundary and peer/school support measured (Table 2) but no correlations reported. No significance levels or CIs given for Table 3. Data openly available on Zenodo (doi 10.5281/zenodo.18279792).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Online survey of active users; recruitment channel/method not described (likely non-probability, but not stated). — p.3, 3.2 — «We ran an online survey with N = 402 active users of Xingye AI (星野·AI皆你所见) who reported use within the past month.»
2. отклик: **unclear** — No response rate or non-responder information reported. — p.3, 3.2 — «Participation was voluntary and anonymous; respondents gave informed consent and completed the questionnaire in one sitting.»
3. валидная шкала зависимости от ИИ: **unclear** — Named instrument (BSMAS-6) adapted to the AI companion; the parent Bergen scale has published validation, but no validation of the AI-adapted version is cited or reported (only alpha), and adapted wording is not given. … — p.3, 3.3 — «problematic use (BSMAS-6) adapted from social/smartphone contexts [35]»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.904 in this sample. — p.4, Table 2 — «Problematic use (BSMAS-6) 6 1.00–5.00 3.44 1.17 0.904 402»
5. валидные шкалы коррелятов: **no** — Sleep disturbance measured with three brief ad hoc items; well-being with 3 life-evaluation items (SWB-3, not a full published scale); loneliness '8-item short form' only partly named. — p.3, 3.3 — «loneliness (8-item short form), sleep disturbance (three brief items consistent with sleep-risk work [2]), and subjective well-being (life-evaluation items [37…»
6. качество данных: **yes** — Attention checks, speeding and straight-lining screening applied. — p.3, 3.2 — «standard quality checks (attention checks, excessive speed, and straight-lining) were applied before analysis.»

Правки:
- 

Проверено: да

