# Проверка выписывания — файл 11 из 13

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

## ST101 · Heng 2025 · Psychology research and behavior management

Основной отчёт R3548: [текст](../../fulltext/text/R3548.txt) — «Attachment Anxiety and Problematic Use of Conversational Artificial Intelligence: Mediation of Emotional Attachment and Moderation of Anthropomorphic Tendencie…» — [DOI](https://doi.org/10.2147/prbm.s531805)
Расхождения в тексте: 1) The abstract says 'Fifty-four Chinese adults', but the Participants section and analyses use 504. The abstract figure is probably a typo. 2) The sex counts do not add up: 248 male + 261 female = 509, not 504, and 49.206% + 51.785% > 100%. Each percentage is the count divided by 504. The education counts (180 + 198 + 131) also sum to 509. pct_female is recorded as printed (51.785). 3) Table 2 columns are labelled β, but they are PROCESS regression coefficients with covariates; they were not extracted. 4) Correlations of PUCAI with emotional attachment (0.799) and anthropomorphic tendency (0.681) are reported but not extracted, because neither construct is in the construct dictionary.
Заметка ИИ: One sample, one eligible effect (PUCAI total with ECR attachment anxiety). The age range includes 17-year-olds, but the mean age is 22.5, so the sample was coded general_adults. The report does not say whether participants were students.

### ST101-1 · Chinese adult CAI users, Wenjuanxing online survey, CHN, n=504
Отчёты: R3548 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PUCAI · total (T1) | **attachment_anxiety** · Short version of Experiences in Close Relationships (ECR) s… | pearson | **0.475** | **504** | 1 | Table 1 | «4 PUCAI / 2.122 / 1.025 / 0.475*** / 0.799*** / 0.681*** / –» |

- E1: α ИИ 0.934, α коррелята 0.726; заметка: Correlation type not stated; assumed Pearson (SPSS correlation analysis). The abstract gives N = 54, but the Methods give 504.

**Ключевые поля выборки:**
- **n_analysed: 504** — Participants — «504 participants were included in the data analysis, resulting in a valid recovery rate of 88.11%»
- **population: general_adults** — Participants — «The participants' ages ranged from 17 to 54 years (M = 22.540, SD = 5.146).»
- **sampling: quota or online panel** — Participants — «A total of 572 participants were recruited via the Wenjuanxing platform using random sampling methods.»
- **ai_system: general_chatbot** — Abstract; Participants — «Chinese adults who used conversational artificial intelligence ... After excluding those who had never used CAI»

**Остальные поля:**
- country: CHN — Abstract; Participants — «Fifty-four Chinese adults who used conversational artificial intelligence were randomly selected»
- data_years: 2024 — Participants — «The questionnaire collection period was from March to April 2024.»
- design: cross-sectional — Research Significance and Future Directions — «First, this was a cross-sectional study, thus preventing the inference of causality between variables.»
- clinical_group: NA — NA — «NA»
- age_mean: 22.540 — Participants — «(M = 22.540, SD = 5.146)»
- age_sd: 5.146 — Participants — «(M = 22.540, SD = 5.146)»
- age_min: 17 — Participants — «The participants' ages ranged from 17 to 54 years»
- age_max: 54 — Participants — «The participants' ages ranged from 17 to 54 years»
- pct_female: 51.785 — Participants — «248 were male (49.206%) and 261 were female (51.785%)»
- mode: online — Participants — «recruited via the Wenjuanxing platform»
- attention_checks: yes — Participants — «those who filled out the questionnaires carelessly (eg, the attention detection question was answered incorrectly)»
- pub_status: journal — Header (venue) — «Psychology research and behavior management»
- language: English — Full text — «Attachment Anxiety and Problematic Use of Conversational Artificial Intelligence»
- funding_coi: Funded by Henan Provincial Education Science Planning, Henan Normal University and Xinxiang/Henan Federation of Social Sciences projects; authors declare no competing interests. — Funding Statement; Disclosure — «Key Project of Henan Provincial Education Science Planning in 2025 (2025JKZD13) ... The authors declare that they have no known competing financial interests»
- notes: The CAI type is not specified; the report covers chatbots, virtual assistants and embedded robots, and was coded general_chatbot. The report does not say whether participants were students. The sex counts sum to 509 (see consistency_notes). Open data: DOI 10.17632/jgpmrmmz8t.1.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online recruitment via the Wenjuanxing crowdsourcing platform. The report calls it 'random sampling', but no sampling frame is described. — Participants — «A total of 572 participants were recruited via the Wenjuanxing platform using random sampling methods.»
2. отклик: **unclear** — The 88.11% 'valid recovery rate' is the share of recruited respondents kept after exclusions (504/572). The response rate among people invited is not reported. — Participants — «504 participants were included in the data analysis, resulting in a valid recovery rate of 88.11%»
3. валидная шкала зависимости от ИИ: **yes** — Published PUCAI scale (Hu et al.), with an existing Chinese version. — Measures, PUCAI — «The PUCAI scale developed by Hu et al was adopted. This scale consists of six items»
4. надёжность шкалы ИИ в выборке: **yes** — Alpha = 0.934 in this sample. — Measures, PUCAI — «The Cronbach's α for this study was 0.934.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, attachment anxiety, was measured with a published short version of the ECR (adapted by Chen). — Measures, Attachment Anxiety Scale — «A short version of the Experiences in Close Relationships (ECR) scale adapted by Chen was used.»
6. качество данных: **yes** — Respondents who failed the attention-check question were excluded. — Participants — «those who filled out the questionnaires carelessly (eg, the attention detection question was answered incorrectly)»

Правки:
- 

Проверено: да

---

## ST102 · Jia 2025 · Behavioral sciences (Basel, Switzerland)

Основной отчёт R3627: [текст](../../fulltext/text/R3627.txt) — «Effect of GenAI Dependency on University Students' Academic Achievement: The Mediating Role of Self-Efficacy and Moderating Role of Perceived Teacher Caring.» — [DOI](https://doi.org/10.3390/bs15101348)
Расхождения в тексте: 1. The GenAID-SE correlation agrees in text and Table 2 (0.224). 2. The simple-slope text says there is a 'negative effect of GenAI dependency on self-efficacy', but Table 2 and Table 3 show a positive association. 3. Table 2 has implausible values: gender-grade 0.504 and gender-major -0.599 have no stars; grade correlates 0.779 with both AA and SE (identical values) and 0.838 with PTC. 4. Table 3 column order is ambiguous. The text says total effect -0.281 and direct effect -0.239, but the first column reports β = -0.239 with SE included. 5. Table 5 marks SE t = -2.019 as ** although the CI is close to 0. PTC t = -4.183 has no star. 6. Academic achievement is described as self-reported NSSE outcomes plus GPA, which mixes measurement sources. 7. No coefficients are shown only in figures. Figure 2 (simple slopes) shows no correlations.
Заметка ИИ: One sample and one eligible effect: GenAIDS total x academic self-efficacy. Perceived teacher caring and academic achievement do not fit any construct in the dictionary.

### ST102-1 · Undergraduates, multiple universities in Liaoning Province, China, n=418
Отчёты: R3627 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R3627_1 · total (T2) | **self_efficacy** · Self-efficacy Scale (Pintrich & De Groot, 1990; Chinese ver… | pearson | **0.224** | **418** | 1 | Table 2; 4.2. Descriptive Statistics and Correlat… | «6. SE / 2.22 / 0.61 / 0.415 ** / 0.779 ** / −0.333 ** / 0.224 ** / 0.222 ** / 1» |

- E1: α ИИ 0.91, α коррелята 0.923; заметка: Value matches the text (r = 0.224, p < 0.01). The SE mean is low (2.22 on a 1-5 scale), and SE correlates negatively with teacher caring, which the authors call counterintuitive.

**Ключевые поля выборки:**
- **n_analysed: 418** — 3.1. Participants; Table 1 — «A total of 418 valid questionnaires were retained, yielding a valid response rate of 83.6%.»
- **population: university_students** — 3.1. Participants — «full-time undergraduate students from multiple universities in Liaoning Province, China, who frequently utilized generative GenAI in their studies»
- **sampling: probability** — 3.1. Participants — «Stratified random sampling was used to select participants across diverse genders, academic years, and disciplinary backgrounds to ensure sample representativeness.»
- **ai_system: general_chatbot** — 3.1. Participants; Appendix A — «who frequently utilized generative GenAI in their studies; I feel noticeably anxious or unsettled when I am unable to use Generative AI.»

**Остальные поля:**
- country: CHN — 3.1. Participants — «full-time undergraduate students from multiple universities in Liaoning Province, China»
- data_years: NR — Institutional Review Board Statement — «approved by the Ethics Committee of Liaoning Normal University (protocol code LL2025196 and approved on 20 May 2025)»
- design: cross-sectional — 5.3. Limitations and Future Directions — «this study employed a cross-sectional data analysis»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Table 1 presents the distributions of gender, academic year, and disciplinary specialization among participants.»
- age_sd: NR — Table 1 — «NR»
- age_min: NR — Table 1 — «NR»
- age_max: NR — Table 1 — «NR»
- pct_female: 58.1 — Table 1 — «Female | 243 | 58.1»
- mode: mixed — 3.1. Participants — «Questionnaires were administered through combined online and offline methods. The online survey was distributed via Wenjuanxing ... while the offline survey wa…»
- attention_checks: yes — 3.1. Participants — «Data cleaning was conducted to exclude invalid responses exhibiting straight-line patterns, internal inconsistencies, or implausibly short completion times.»
- pub_status: journal — Header — «Behavioral sciences (Basel, Switzerland); DOI: 10.3390/bs15101348»
- language: English — Full text — «Effect of GenAI Dependency on University Students' Academic Achievement»
- funding_coi: National Social Science Fund of China (BIA210162); authors declare no conflicts of interest — Funding Statement; Conflicts of Interest — «This research was funded by the National Social Science Fund of China, grant number BIA210162. The authors declare no conflicts of interest.»
- notes: Data collection year not stated (ethics approval 20 May 2025, so collection was probably in 2025, but this is not reported). The sample was limited to students who frequently use GenAI. Correlates in Table 2 not extracted: academic achievement (NSSE-China outcomes + GPA) and perceived teacher caring (Teacher Caring Behaviour Questionnaire, adapted). Teacher caring is not general perceived social support, so it was not coded as social_support; the reviewer may want to check this. Only the GenAIDS total is correlated with correlates. Subscales are reported only as inter-dimension correlations (…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The report says stratified random sampling was used, but gives no sampling frame or selection procedure. Eligibility was limited to frequent GenAI users, and part of the data was collected via Wenjuanxing, so it is uncl… — 3.1. Participants — «Stratified random sampling was used to select participants ... The online survey was distributed via Wenjuanxing»
2. отклик: **yes** — Valid response rate is 83.6%, above 60%. — 3.1. Participants — «A total of 418 valid questionnaires were retained, yielding a valid response rate of 83.6%.»
3. валидная шкала зависимости от ИИ: **yes** — GenAIDS was developed and validated in this report (expert review, interviews, pilot item analysis, CFA, CR/AVE). — 3.2.1. GenAI Dependency — «The confirmatory factor analysis results indicated a good fit (X2/df = 2.68, RMSEA = 0.055, GFI = 0.905, CFI = 0.924, TLI = 0.912, and IFI = 0.923).»
4. надёжность шкалы ИИ в выборке: **yes** — Total alpha is .91; subscale alphas are .82-.87. — 3.2.1. GenAI Dependency — «the overall internal consistency reliability of the scale was 0.91, with α coefficients for each dimension being 0.87 for affective dependency, 0.84 for behavi…»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (academic self-efficacy) was measured with the published Chinese version of the Pintrich & De Groot scale. — 3.2.2. Self-Efficacy — «This study employed the Chinese version (Y. Liang, 2000) of the Self-efficacy Scale, developed by Pintrich and De Groot (1990)»
6. качество данных: **yes** — Rules for invalid responses were stated: straight-lining, inconsistencies, too-short completion times. — 3.1. Participants — «Data cleaning was conducted to exclude invalid responses exhibiting straight-line patterns, internal inconsistencies, or implausibly short completion times.»

Правки:
- 

Проверено: да

---

## ST103 · Li 2025 · Research Square

Основной отчёт R3772: [текст](../../fulltext/text/R3772.txt) · [PDF](../../fulltext/pdf/R3772.pdf) — «The Influence of Attachment Style Variations on Problematic Use of AI Chatbots: A Mediation Study of Social Anxiety and Human-Robot Empathy» — [DOI](https://doi.org/10.21203/rs.3.rs-7437820/v1)
Расхождения в тексте: 1) Table 3 note says the diagonal shows the AVE and the lower triangle shows squared correlations. The text says the diagonal shows square roots of the AVE (consistent with the values, e.g. 0.758 = √0.574, 0.844 = √0.712). It is therefore unclear whether the off-diagonal values are r or r². The social anxiety diagonal (0.704) does not match √AVE 0.696 (= 0.834). 2) Text gives Cronbach's α 'from 0.741 to 0.899', but the lowest α in Table 2 is 0.742 (social anxiety). For avoidant attachment, α 0.899 is higher than CR 0.889. 3) Text gives p = 0.122 for avoidant attachment → empathy, but Table 4 gives 0.086. Several p cells in Tables 4/5 simply repeat the coefficient. The text says H4 is supported, but Table 4 says 'Rejected'. 4) Table 2 lists one human-robot empathy item twice. 5) Limitations describe the sample as 'primarily Chinese college students', while the Methods describe AI chatbot…
Заметка ИИ: Single PLS-SEM study. No Pearson matrix; only Fornell-Larcker latent values were extracted. Table 4/5 path coefficients were not extracted.

### ST103-1 · Online survey of AI chatbot users, mainland China, n=534
Отчёты: R3772 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | BERGEN_ADAPTED · total (T1) | **social_anxiety** · Study-specific 9-item social anxiety scale (integrated from… | latent | **0.436** | **534** | 1 | Page 27, Table 3 (Fornell-Larcker) | «Problematic use of AI chatbots / 0.538 / 0.298 / 0.289 / 0.436 / 0.844 (columns: human-robot empathy, Avoidant attachment, Anxious attachment, Social anxiety, Problematic use)» |
| E2 | BERGEN_ADAPTED · total (T1) | **attachment_anxiety** · Anxious attachment (6 items selected from ECR-RS and MPAS) | latent | **0.289** | **534** | 1 | Page 27, Table 3 (Fornell-Larcker) | «Problematic use of AI chatbots / 0.538 / 0.298 / 0.289 / 0.436 / 0.844» |
| E3 | BERGEN_ADAPTED · total (T1) | **attachment_avoidance** · Avoidant attachment (6 items selected from ECR-RS and MPAS) | latent | **0.298** | **534** | 1 | Page 27, Table 3 (Fornell-Larcker) | «Problematic use of AI chatbots / 0.538 / 0.298 / 0.289 / 0.436 / 0.844» |

- E1: α ИИ 0.775, α коррелята 0.742; заметка: PLS-SEM Fornell-Larcker matrix. The table note says the lower triangle shows 'squared correlation coefficients', but the text treats them as correlations under the Fornell-Larcker criterion. The reviewer should check whether the value is r or r².
- E2: α ИИ 0.775, α коррелята 0.806; заметка: Possible r² (see table note). The attachment target is unclear: the Methods say the scale assesses attachment 'toward impersonal media objects', but the items refer to 'the other person'. The reviewer should check that this is not attachment to AI, which the dictionary excludes.
- E3: α ИИ 0.775, α коррелята 0.899; заметка: Possible r² (see table note). The attachment target is unclear (Methods: 'toward impersonal media objects'; items: 'the other person'). Reported alpha (0.899) is higher than CR (0.889), which is unusual.

**Ключевые поля выборки:**
- **n_analysed: 534** — Page 20 — «After excluding invalid responses, 534 valid responses remained, comprising 235 males and 299 females.»
- **population: general_adults** — Page 20, Table 1; Page 41 — «Most participants were aged between 18 and 30 and held a bachelor's degree.»
- **sampling: snowball** — Page 19, Data Collection and Sample Situation — «employed an online questionnaire distributed through the Wenjuanxing platform using snowball and convenience sampling»
- **ai_system: general_chatbot** — Page 17; Page 19 — «Participants were instructed to respond based on their recent real-world interaction experiences with chatbots. ... This study focused on AI chatbot users in mainland China»

**Остальные поля:**
- country: CHN — Page 19, Data Collection and Sample Situation — «This study focused on AI chatbot users in mainland China»
- data_years: NR — Page 52, Ethical approval — «(Approval number: cqjtu20241022, Approval date: 2024-10-22)»
- design: cross-sectional — Page 17, Questionnaire design — «This study employs a cross-sectional survey method, collecting data through online questionnaires»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 20, Table 1 — «Age 18-30 years old 463 86.7%»
- age_sd: NR — Page 20, Table 1 — «Age 18-30 years old 463 86.7%»
- age_min: 18 (lowest reported age category 18-30 years) — Page 20, Table 1 — «Age 18-30 years old 463 86.7%»
- age_max: NR (highest category: over 60 years) — Page 20, Table 1 — «Over 60 years old 7 1.31%»
- pct_female: 55.99 — Page 20, Table 1 — «Female 299 55.99%»
- mode: online — Page 17 — «The questionnaire was distributed via an online platform, and participation was completely anonymous.»
- attention_checks: NR — Page 19-20 — «A total of 550 responses were collected ... After excluding invalid responses, 534 valid responses remained»
- pub_status: preprint — Page 1 — «Research Article ... Posted Date: September 5th, 2025 DOI: https://doi.org/10.21203/rs.3.rs-7437820/v1»
- language: English — Full text — «The Influence of Attachment Style Variations on Problematic Use of AI Chatbots: A Mediation Study of Social Anxiety and Human-Robot Empathy»
- funding_coi: Funded by Chongqing Municipal Education Commission Language Committee Project (yyk25215), China Traffic Education Research Association (T2024YB421), Chongqing Education Science Planning Project (K24YY2070044); no conflicts of interest declared. — Page 51-52, Competing interests; Funding — «The author(s) declared no potential conflicts of interest ... This article is supported by the following project: The 2025 Chongqing Municipal Education Commis…»
- notes: The limitations section calls the sample 'primarily Chinese college students', while the Methods recruited AI chatbot users in general (86.7% aged 18-30, 78% undergraduate). Population was coded general_adults; the reviewer should confirm. 16 of 550 responses were excluded as invalid, with no criteria given.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Snowball and convenience sampling through Wenjuanxing, with recruitment via social media. — Page 19-20 — «distributed through the Wenjuanxing platform using snowball and convenience sampling ... collected via social media platforms (e.g., WeChat, Xiaohongshu)»
2. отклик: **unclear** — No response rate (snowball distribution); only 550 collected / 534 valid reported. — Page 19-20 — «A total of 550 responses were collected ... 534 valid responses remained»
3. валидная шкала зависимости от ИИ: **yes** — 6 items adapted from the Bergen Facebook Addiction Scale (Andreassen 2012) to AI chatbots; this report gives measurement-model evidence (loadings 0.804-0.873, CR 0.925, AVE 0.712). The adapted version has no separate pu… — Page 19; Page 26, Table 2 — «this study adapts the "Facebook Addiction Scale" [55] ... Items were contextually modified ... The scale consists of 6 items»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.775 in this sample. — Page 26, Table 2 — «Problematic use of AI chatbots ... 0.847 0.925 0.712 0.775»
5. валидные шкалы коррелятов: **no** — Social anxiety was measured with a new 9-item scale that combines adapted items from the SCAS and the Social Anxiety Scale for Social Media Users. The attachment items were chosen from the ECR-RS and the MPAS. Neither c… — Page 18 — «A 9-item scale was developed for the general population by integrating items from Spence et al.'s Spence Children's Anxiety Scale [49] and Alkis et al.'s Socia…»
6. качество данных: **unclear** — Invalid responses were excluded (16), but the criteria are not stated and no attention checks are reported. — Page 20 — «After excluding invalid responses, 534 valid responses remained»

Правки:
- 

Проверено: да

---

## ST104 · Liu 2025 · Communications in Humanities Research

Основной отчёт R3790: [текст](../../fulltext/text/R3790.txt) · [PDF](../../fulltext/pdf/R3790.pdf) — «Exploring the Behavioral Differentiation and Psychological Impact of Different Attachment Types of Users Interacting with AI» — [DOI](https://doi.org/10.54254/2753-7064/2025.lc25585)
Расхождения в тексте: 1. In Table 1 the PUCAI measure is labelled 'BSMAS' (6 items, α = 0.875); the text calls it the PUCAI scale. 2. Table 2 group ns (76 + 48 + 37 + 40 = 201) do not match N = 203. 3. In Tables 3 and 5 the 'R2' rows look like multiple R: Adj.R2 equals the square of 'R2' (0.3496² ≈ 0.1222; 0.5492² ≈ 0.3016). 4. Table 5 prints the HARS → PA coefficient as 0.5767 with t = -32.1862, while the text gives β = –0.5767. This does not involve PUCAI and was not extracted. 5. In Table 6 the indirect-effect BootSE equals the effect value (0.6004), which is probably a typo. 6. The text says 'all scales demonstrated high reliability (α > 0.85), except for the PANAS' (PANAS α = 0.671). 7. No correlation matrix is reported. PANAS positive/negative affect (wellbeing) is analysed only against attachment and HARS, not against PUCAI.
Заметка ИИ: There is only one candidate effect, and it is of doubtful eligibility: a single-predictor regression of PUCAI on an anxious attachment-type dummy. Several demographic and method fields are not reported. The reviewer should decide whether to keep the effect row.

### ST104-1 · AI users, country NR (author affiliation Japan), n=203
Отчёты: R3790 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PUCAI · total (T1) | **attachment_anxiety** · ECR-S, anxious attachment type (dummy from median split; An… | beta_single_predictor | **0.6759** | **203** | 1 | Page 5, Table 3 | «Anxious / 0.6759 / 5.2763** ... R2 / 0.3496 ... Adj.R2 / 0.1222 ... F / 27.8396**» |

- E1: **направление: as named (anxious-type membership; contrast group appears to include fearful, secure and avoidant)**; α ИИ 0.875, α коррелята 0.888 (full ECR-S; subscale NR); заметка: ELIGIBILITY DOUBTFUL: predictor is a categorical attachment-type dummy, not the continuous anxiety dimension; fearful (high-anxiety) type seems to be in the reference group. β looks unstandardised. The 'R2' row (0.3496) seems to be multiple R (0.3496² = Adj.R2 0.1222), so |r| ≈ .35, consistent with…

**⚠ Проверка скриптом (обратите внимание):**
- E1: этого числа нет в независимом проходе ИИ по полному тексту — сверьте с таблицей
- E1: не корреляция, а пересчёт: проверьте, что β с одним предиктором или что группы сравнения верны
- в независимом проходе были ещё числа: 0.35 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 203** — Page 8, Section 4 — «although the sample (N = 203) satisfied the basic threshold for regression procedures»
- **population: general_adults** — Page 1, Abstract — «A total of 203 users were surveyed»
- **sampling: NR** — NA — «NA»
- **ai_system: ai_unspecified** — Page 3, Section 2.1 — «by replacing references to “social media” with “AI interaction,” thereby creating the PUCAI scale, which captures addiction-like usage patterns of AI»

**Остальные поля:**
- country: NR — Page 1, affiliation — «Psychological and Sociological Studies, TOKAI University, Japan»
- data_years: NR — NA — «NA»
- design: cross-sectional — Page 1, Abstract — «A total of 203 users were surveyed, and the ECR-S, PSI, PANAS and adapted PUCAI scales were used to measure the variables.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NA»
- age_sd: NR — NA — «NA»
- age_min: NR — NA — «NA»
- age_max: NR — NA — «NA»
- pct_female: NR — NA — «NA»
- mode: NR — NA — «NA»
- attention_checks: NR — NA — «NA»
- pub_status: conference — Page 1, header — «Proceedings of ICADSS 2025 Symposium: Art, Identity, and Society: Interdisciplinary Dialogues»
- language: English — Page 1 — «Exploring the Behavioral Differentiation and Psychological Impact of Different Attachment Types of Users Interacting with AI»
- funding_coi: NR — NA — «NA»
- notes: Population is described only as 'users'; coded general_adults by default. Age, sex, country, recruitment and mode are not reported. The paper frames the AI as affective/social AI (keyword 'social AI'), but the specific AI systems participants used are not named, so it is coded ai_unspecified. Attachment style comes from an ECR-S median split into four types. Table 2 group ns sum to 201, not 203. The only PUCAI-correlate association reported is a single-predictor regression of emotional addiction on an 'Anxious' attachment-type dummy (Table 3).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Recruitment and sampling are not described. — Page 1, Abstract — «A total of 203 users were surveyed»
2. отклик: **unclear** — No response rate is reported. — NA — «NA»
3. валидная шкала зависимости от ИИ: **yes** — The instrument is a BSMAS adaptation following Hu, Mao & Kim (2023), which is a published PUCAI source. However, the author says its structural validity in non-social-media contexts warrants further investigation. — Page 3, Section 2.1; Page 8 — «employs a modified version of the Bergen Social Media Addiction Scale (BSMAS), with adjustments based on some scholars ... thereby creating the PUCAI scale»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha is 0.875 in this sample. — Page 4, Table 1 — «BSMAS | 6 | 0.875»
5. валидные шкалы коррелятов: **yes** — Attachment is measured with the published ECR-S, but it was dichotomised into types by median split. — Page 3, Section 2.1 — «this research utilizes the short-form version of the Experiences in Close Relationships scale (ECR-S)... classifies participants into four types based on the m…»
6. качество данных: **unclear** — No data-quality screening is reported. — NA — «NA»

Правки:
- 

Проверено: да

---

## ST105 · Maral 2025 · International Journal of Mental Health and Addiction

Основной отчёт R3828: [текст](../../fulltext/text/R3828.txt) · [PDF](../../fulltext/pdf/R3828.pdf) — «Problematic ChatGPT Use Scale: AI-Human Collaboration or Unraveling the Dark Side of ChatGPT» — [DOI](https://doi.org/10.1007/s11469-025-01509-y)
Не выписано ИИ: Pilot sample (n = 25, convenience): used only to check the clarity of the translated items; no correlations reported. DAIS (Dependence to AI Scale, Study I): its only reported correlation is with the PCGUS (r = .425), which is AI dependence with AI dependence, not a dictionary correlate, so no DAIS effects were extracted.
Расхождения в тексте: 1. PCGUS scoring: the text calls it a 4-point scale (1–4) with 11 items but gives a total range of 11–55, which would need a 5-point scale. Table 2 also still lists loadings for items 1 and 4, which were removed. The alpha of .88 is said to be for 'the original scale'; the 9-item alphas are .903 (Study I) and .877 (Study II). 2. Study II mediation: t(334) implies about 337 cases, not N = 473, so the n of the Table 3 correlations is uncertain. 3. Bootstrap samples: the text gives 10,000 in one place and 5,000 in another. 4. Path a2: Table 6 prints the estimate as .207 (positive) with t = −3.42 and CI [−.32, −.886]. The text gives B = −0.21. The CI upper limit looks erroneous. 5. The Discussion says 'partially mediated', but the total effect was non-significant (suppression). 6. Study II Table 1 education counts (158+249+76 = 483, plus 4 in the text) exceed N = 473. 249 is printed as 50.6…
Заметка ИИ: Two samples extracted (Study I n=391; Study II n=473), both using the Turkish 9-item PCGUS total score. The BFI-10 alphas given in the report seem to come from earlier studies, so correlate_alpha is NR. Not extracted: the IGDS9-SF gaming correlation (not in the construct dictionary) and the DAIS–PCGUS correlation (exposure with exposure).

### ST105-1 · Study I: Turkish adults (ChatGPT users), PCGUS validation, TUR, n=391
Отчёты: R3828 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PCUS · total (T1) | **problematic_internet_use** · Young Internet Addiction Test – Short Form (YIBT-SF) | pearson | **.228** | **391** | 1 | Table 3, Study I | «YIBT-SF / 27.86 / 8.53 / .468 / .126 / .228 / < .001» |
| E2 | PCUS · total (T1) | **openness** · BFI-10 Openness | pearson | **-.080** | **391** | 1 | Table 3, Study I | «Openness / 7.68 / 1.77 / − .307 / − .785 / − .080 / .116» |
| E3 | PCUS · total (T1) | **conscientiousness** · BFI-10 Conscientiousness | pearson | **-.163** | **391** | 1 | Table 3, Study I | «Conscientiousness / 7.43 / 1.79 / − .137 / − .722 / − .163 / < .001» |
| E4 | PCUS · total (T1) | **extraversion** · BFI-10 Extraversion | pearson | **-.059** | **391** | 1 | Table 3, Study I | «Extraversion / 7.28 / 2.20 / − .510 / − .726 / − .059 / .248» |
| E5 | PCUS · total (T1) | **agreeableness** · BFI-10 Agreeableness | pearson | **-.091** | **391** | 1 | Table 3, Study I | «Agreeableness / 8.10 / 1.50 / − .514 / − .141 / − .091 / .072» |
| E6 | PCUS · total (T1) | **neuroticism** · BFI-10 Neuroticism | pearson | **.037** | **391** | 1 | Table 3, Study I | «Neuroticism / 5.71 / 1.87 / .047 / − .403 / .037 / .467» |

- E1: α ИИ .903, α коррелята .88; заметка: Exposure is the Turkish 9-item PCGUS total score
- E2: α ИИ .903, α коррелята NR; заметка: The BFI alphas (.68–.73) are described as 'reported' and seem to come from earlier studies, not this sample; two items per trait
- E3: α ИИ .903, α коррелята NR; заметка: Two-item subscale
- E4: α ИИ .903, α коррелята NR; заметка: Two-item subscale
- E5: α ИИ .903, α коррелята NR; заметка: Two-item subscale
- E6: α ИИ .903, α коррелята NR; заметка: Two-item subscale

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: -0.17, 0.30 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 391** — Table 2 note; p.8 — «A total of 391 participants, aged between 18 and 59 years (M = 30.89, SD = 8.22)»
- **population: general_adults** — p.8 Participants and Procedure — «25.6% employed in the public sector, 39.1% in the private sector, 10.2% unemployed, and 25.1% students»
- **sampling: convenience** — p.7 Participants and Procedure — «The study employed data collection tools created through Google Forms, and participants were selected using a convenience sampling method.»
- **ai_system: general_chatbot** — p.8 — «ChatGPT usage was a requirement for inclusion in the study, with 62.7% (n = 245) of participants reporting frequent use.»

**Остальные поля:**
- country: TUR — p.3-4; p.7 Methods — «evaluate its psychometric properties ... within a Turkish sample»
- data_years: NR — p.8 Ethics — «Approval for the study was granted by the Yıldız Technical University Ethics Committee prior to data collection (Report Number: 20241003413).»
- design: validation study — p.4 Study 1 — «This study aims to adapt the PCGUS (Yu et al., 2024) for the Turkish context and thoroughly evaluate its psychometric properties.»
- clinical_group: NA — p.21 Limitations — «this study was conducted with a non-clinical sample drawn from various cities in Türkiye»
- age_mean: 30.89 — p.8; Table 3 — «aged between 18 and 59 years (M = 30.89, SD = 8.22)»
- age_sd: 8.22 — p.8 — «aged between 18 and 59 years (M = 30.89, SD = 8.22)»
- age_min: 18 — p.8 — «aged between 18 and 59 years»
- age_max: 59 — p.8 — «aged between 18 and 59 years»
- pct_female: 61.4 — p.8; Table 1 — «with 240 females (61.4%) and 151 males (38.6%)»
- mode: online — p.5; p.7 — «the scale was administered online to a broader sample ... data collection tools created through Google Forms»
- attention_checks: NR — p.7-8 Methods — «participants were selected using a convenience sampling method»
- pub_status: journal — p.1 — «International Journal of Mental Health and Addiction (2026) 24:2369–2395 ... ORIGINAL ARTICLE»
- language: English — p.1 — «Problematic ChatGPT Use Scale: AI‑Human Collaboration or Unraveling the Dark Side of ChatGPT»
- funding_coi: Open access funding by TÜBİTAK; authors received no financial support for the research; no competing interests declared — p.22 Funding; Declarations — «Open access funding provided by the Scientific and Technological Research Council of Türkiye (TÜBİTAK). The authors received no financial support for the resea…»
- notes: Turkish 9-item PCGUS (items 1 and 4 of the original 11 removed; error covariances added). The DAIS (Dependence to AI Scale) was also given (alpha .80), but the report only gives its correlation with the PCGUS (r = .425), so no DAIS × correlate effects are available. The IGDS9-SF (gaming disorder, r = .225) is not in the construct dictionary and was not extracted. Age, gender and SES were not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online via Google Forms — p.7 — «participants were selected using a convenience sampling method»
2. отклик: **unclear** — Response rate not reported — p.7-8 — «A total of 391 participants, aged between 18 and 59 years»
3. валидная шкала зависимости от ИИ: **yes** — PCGUS has a published development study (Yu et al., 2024), and the Turkish version was validated in this report (CFA, IRT, invariance) — p.8 Measures; p.10 Result — «The scale, developed by Yu et al. (2024)... model fit improved substantially (χ2/df = 3.42, GFI = 0.924, NFI = 0.942, CFI = 0.951, SRMR = 0.047)»
4. надёжность шкалы ИИ в выборке: **yes** — alpha .903 and omega .896 for the 9-item score in Study I — p.12 Reliability — «In study I (N = 391), the scale demonstrated excellent reliability, with Cronbach's Alpha (α = 0.903), McDonald's Omega (ω = 0.896)»
5. валидные шкалы коррелятов: **yes** — Correlates measured with published instruments (YIAT-SF with its Turkish adaptation; BFI-10 with its Turkish adaptation) — p.9 Measures — «The Five Factor Personality Inventory, developed by Rammstedt and John (2007)... The Turkish adaptation of the scale was performed by Türküm et al. (2016).»
6. качество данных: **unclear** — No attention checks or invalid-response screening reported — p.7-8 Methods — «NR»

Правки:
- 

Проверено: да

### ST105-2 · Study II: Turkish adults, PCGU, distress, self-control and well-being, TUR, n=473
Отчёты: R3828 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PCUS · total (T1) | **distress** · DASS-21 total | pearson | **.301** | **473** | 1 | Table 3, Study II | «DASS-21 / 16.98 / 14.23 / .865 / .212 / .301 / < .001» |
| E2 | PCUS · total (T1) | **wellbeing** · General Well-Being Scale – Short Form (GWB-SF) | pearson | **-.174** | **473** | 1 | Table 3, Study II | «GWB-SF / 48.94 / 10.39 / − .524 / .476 / − .174 / < .001» |
| E3 | PCUS · total (T1) | **self_control** · Brief Multidimensional Self-Control Scale (BMSCS) | pearson | **-.156** | **473** | 1 | Table 3, Study II | «BMSCS / 25.59 / 5.55 / − .033 / .289 / − .156 / < .001» |

- E1: α ИИ .877, α коррелята NR; заметка: Only subscale alphas are reported (Depression .93, Anxiety .91, Stress .94); no alpha for the total score. n assumed to be the sample N; the mediation df suggests about 337 complete cases
- E2: α ИИ .877, α коррелята .91; заметка: n assumed to be the sample N; see consistency notes
- E3: α ИИ .877, α коррелята .72; заметка: n assumed to be the sample N; see consistency notes

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: -0.09, -0.08, -0.06, 0.04, 0.23 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 473** — p.15; p.12 Reliability — «Study II included a sample of 473 adults from Türkiye»
- **population: general_adults** — p.15; Table 1 — «Study II included a sample of 473 adults from Türkiye ... with ages ranging from 18 to 75 years»
- **sampling: convenience** — p.21 Limitations — «Second, the use of convenience sampling may limit the generalizability of the results to broader populations.»
- **ai_system: general_chatbot** — Table 1; Table 3 — «ChatGPT usage frequency ... PCGUS (9 Items Total Score) 11.69»

**Остальные поля:**
- country: TUR — p.15 Participants and Procedure — «Study II included a sample of 473 adults from Türkiye»
- data_years: NR — p.8 Ethics — «Approval ... prior to data collection (Report Number: 20241003413)»
- design: cross-sectional — p.21 Limitations — «the mediation analysis in study 2 was based on cross-sectional data»
- clinical_group: NA — p.21 Limitations — «this study was conducted with a non-clinical sample»
- age_mean: 28.25 — Abstract, p.1 — «study II involved 473 participants (74.4% male, mean age = 28.25)»
- age_sd: NR — p.15 — «with ages ranging from 18 to 75 years»
- age_min: 18 — p.15 — «with ages ranging from 18 to 75 years»
- age_max: 75 — p.15 — «with ages ranging from 18 to 75 years»
- pct_female: 25.6 — p.15; Table 1 — «consisting of 352 males (74.4%) and 121 females (25.6%)»
- mode: online — p.15 — «Data were collected online using a researcher-designed questionnaire»
- attention_checks: NR — p.15 Method — «Data were collected online using a researcher-designed questionnaire»
- pub_status: journal — p.1 — «International Journal of Mental Health and Addiction (2026) 24:2369–2395 ... ORIGINAL ARTICLE»
- language: English — p.1 — «Problematic ChatGPT Use Scale: AI‑Human Collaboration or Unraveling the Dark Side of ChatGPT»
- funding_coi: Open access funding by TÜBİTAK; authors received no financial support for the research; no competing interests declared — p.22 — «The authors received no financial support for the research... The authors declare no competing interests.»
- notes: Uses the 9-item Turkish PCGUS. DASS-21 is correlated only as a total score (psychological distress); subscale correlations are not reported. Whether ChatGPT use was an inclusion criterion is stated only for Study I. Mean age comes from the abstract only. The mediation df (t(334)) suggests that fewer than 473 cases were analysed; the n of the correlations is unclear.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample collected online — p.15; p.21 — «Data were collected online ... the use of convenience sampling may limit the generalizability»
2. отклик: **unclear** — Response rate not reported — p.15 — «Study II included a sample of 473 adults from Türkiye»
3. валидная шкала зависимости от ИИ: **yes** — PCGUS has a published development study (Yu et al., 2024), and the Turkish 9-item version was validated in Study I of this report — p.8; p.10 — «The scale, developed by Yu et al. (2024)»
4. надёжность шкалы ИИ в выборке: **yes** — alpha .877 and omega .875 in Study II — p.12 Reliability — «In study II (N = 473), the corresponding reliability values were also robust, with α = 0.877, ω = 0.875»
5. валидные шкалы коррелятов: **yes** — DASS-21, GWB-SF and BMSCS are published instruments with Turkish adaptations — p.15-16 Measurements — «The BMSCS, developed by Nilsen et al. (2020)... The Turkish version of the scale was adapted by Koç et al. (2023)»
6. качество данных: **unclear** — No screening reported — p.15-16 — «NR»

Правки:
- 

Проверено: да

---

## ST106 · Morales-García 2025 · Data & Metadata

Основной отчёт R3880: [текст](../../fulltext/text/R3880.txt) · [PDF](../../fulltext/pdf/R3880.pdf) — «Influence of Self-Efficacy in the Use of Artificial Intelligence (AI) and Anxiety Toward AI Use on AI Dependence Among Peruvian University Students» — [DOI](https://doi.org/10.56294/dm2025210)
Расхождения в тексте: The means and SDs in Table 2 do not match Table 1. Table 2 gives 'Self-efficacy with AI' M=1,82, SD=1,73, which matches the anxiety values in Table 1 (about 1,85 ± 1,73 / 1,79 ± 1,75). Table 2 gives 'Anxiety toward AI use' M=14,77, SD=4,22. This is impossible for a 2-item scale scored 0-3 (maximum 6) and does not match the self-efficacy values in Table 1 (about 3,0-3,1). So the row labels or descriptives in Table 2 appear swapped or wrong. The correlations are consistent across the abstract, the text and Table 2: self-efficacy-anxiety 0,43, self-efficacy-dependence 0,61, anxiety-dependence 0,71. The text says students in administration and nursing showed higher dependence, while the regression shows only Administration (+) and Medicine (−) as significant. The sex comparison reports W-KW values (3408, 355, 353) that look inconsistent with one another. The reliability values (DAI α/ω=.87,…
Заметка ИИ: I extracted one sample and one eligible effect: DAI total with AI anxiety, r = 0,71, n = 528. AI anxiety was measured with an ad hoc 2-item scale. The reviewer should check two things: whether the DAI reliability (.87) comes from this sample, and the apparently mislabelled descriptives in Table 2.

### ST106-1 · Peruvian university students, online survey, PER, n=528
Отчёты: R3880 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **ai_anxiety** · Anxiety Toward the Use of Artificial Intelligence Scale (ad… | pearson | **0,71** | **528** | 1 | Page 5, Table 2 | «Dependence on AI 12,99 4,91 0,61** 0,71** -» |

- E1: α ИИ 0,87 (sample unclear), α коррелята 0,85; заметка: Matrix gives two decimals only. The DAI alpha (0,87; omega 0,87) may come from the validation study rather than this sample. The correlate is an ad hoc 2-item scale (GAD-2-style items about AI). The M/SD columns of Table 2 appear mislabelled (see consistency_notes); the correlation itself also matc…

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.61 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 528** — Page 3, Study Design — «A total of 528 valid responses were analyzed, with 3 surveys excluded due to incomplete answers.»
- **population: university_students** — Page 3, Study Design — «The study participants were Peruvian university students.»
- **sampling: convenience** — Page 3, Procedure — «The questionnaires were sent to university students via a Google Forms link, which was distributed through WhatsApp groups, following an internet-based methodology»
- **ai_system: ai_unspecified** — Page 3, Study Design — «students with access to artificial intelligence (AI) tools and a minimum of 3 to 6 months of experience using them for academic purposes»

**Остальные поля:**
- country: PER — Page 3, Method — «The study participants were Peruvian university students.»
- data_years: 2024 — Page 3, Procedure — «Data were collected between April and May 2024.»
- design: cross-sectional — Page 3, Study Design — «This study employed a descriptive cross-sectional.»
- clinical_group: NA — NA — «NA»
- age_mean: 19.00 — Page 4, Preliminary analysis — «The university students' ages ranged from 18 to 37 years (M = 19,00, SD = 3,84).»
- age_sd: 3.84 — Page 4, Preliminary analysis — «(M = 19,00, SD = 3,84)»
- age_min: 18 — Page 4, Preliminary analysis — «ages ranged from 18 to 37 years»
- age_max: 37 — Page 4, Preliminary analysis — «ages ranged from 18 to 37 years»
- pct_female: 53 — Page 4, Table 1 — «Sex Female 280 53 ... Male 248 47»
- mode: online — Page 3, Study Design — «surveys were distributed via a Google Forms questionnaire, shared through social media platforms like WhatsApp»
- attention_checks: NR — Page 3, Study Design — «A total of 528 valid responses were analyzed, with 3 surveys excluded due to incomplete answers.»
- pub_status: journal — Page 1 — «Data and Metadata. 2025; 4:210 doi: 10.56294/dm2025210 ORIGINAL»
- language: English (abstract also in Spanish) — Page 1-2 — «Influence of Self-Efficacy in the Use of Artificial Intelligence (AI) and Anxiety Toward AI Use on AI Dependence Among Peruvian University Students»
- funding_coi: No financing; authors declare no conflicts of interest — Page 11, Financing / Conflict of interest — «FINANCING No financing. CONFLICT OF INTEREST The authors declare no potential conflicts of interest.»
- notes: Only incomplete surveys were excluded (n=3); there were no attention checks and no careless-responding screening, so attention_checks is coded NR (the reviewer may treat the incomplete-response rule as a validity rule). The AI self-efficacy correlate (GSE-6AI; r=0,61 with the DAI) was not extracted because AI self-efficacy is out of scope. The regression coefficients described as 'β' are unstandardized multivariable estimates and were not extracted. The DAI's first author also wrote this report.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience online sample recruited through WhatsApp groups with Google Forms — Page 3, Procedure — «The questionnaires were sent to university students via a Google Forms link, which was distributed through WhatsApp groups»
2. отклик: **unclear** — No response rate reported; only that 3 incomplete surveys were excluded — Page 3, Study Design — «A total of 528 valid responses were analyzed, with 3 surveys excluded due to incomplete answers.»
3. валидная шкала зависимости от ИИ: **yes** — The DAI has a published development/validation study (Morales-García et al., 2024c) — Page 4, Instruments; Page 10, ref 32 — «The Artificial Intelligence Dependence Scale (DAI) was validated among university students in Peru (Morales-García et al., 2024c).»
4. надёжность шкалы ИИ в выборке: **unclear** — Alpha/omega of .87 is reported in the sentence right after the citation of the validation study. It is unclear whether these values come from this sample or from the validation study. If they are from this sample, rate … — Page 4, Instruments — «Reliability was assessed through Cronbach's Alpha (α = 0,87) and McDonald's Omega (ω = 0,87), indicating high internal consistency.»
5. валидные шкалы коррелятов: **no** — The only eligible correlate (anxiety toward AI) was measured with an ad hoc 2-item scale developed for this study, with no validation evidence — Page 4, Instruments — «The Anxiety Toward the Use of Artificial Intelligence Scale was developed and used, consisting of 2 items»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported; only incomplete surveys were excluded — Page 3, Study Design — «with 3 surveys excluded due to incomplete answers»

Правки:
- 

Проверено: да

---

## ST107 · Muhammad Qasim Arif,Nimra Munawar,Eza Rabab 2025 · Zenodo

Основной отчёт R3886: [текст](../../fulltext/text/R3886.txt) · [PDF](../../fulltext/pdf/R3886.pdf) — «FROM AI DEPENDENCE TO IMPOSTOR SYNDROME: THE MEDIATING ROLE OF FEAR OF NEGATIVE EVALUATION» — [DOI](https://doi.org/10.5281/zenodo.17042830)
Расхождения в тексте: The correlation in the text (r = .36, pp. 4-5) matches Table 2. Subscale alphas are reported (Reading .78, Writing .83, Numeracy/Arithmetic .88), but no correlations for the subscales are given, so only the total score is extracted. Degrees of freedom do not match: the AID→FNE regression gives F(1, 198), consistent with N = 200, but the FNE→IS regression gives F(1, 197), which implies n = 199. The two DOIs differ slightly: the article header gives 10.5281/zenodo.17042831, while the job metadata gives 10.5281/zenodo.17042830.
Заметка ИИ: ai_system was coded ai_unspecified because participants were required to use 'AI-based academic tools', and the introduction names examples such as ChatGPT, Grammarly and paraphrasing software. The reviewer may prefer task_assistant, since the tools were academic/study tools and the instrument covers writing, reading and numeracy. pub_status is journal (Journal of Media Horizons); the full text was deposited on Zenodo. Age mean and SD are not reported; age is given only in brackets.

### ST107-1 · Undergraduate students using AI tools, various universities, Pakistan (n=200)
Отчёты: R3886 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | CAPINDING · total (T2) | **social_anxiety** · Brief Fear of Negative Evaluation Scale (BFNE; Leary, 1983)… | pearson | **.36** | **200** | 1 | Page 5, Table 2 | «1. AI Dependence / - / .36*** / .37***» |

- E1: α ИИ .91, α коррелята .81; заметка: Matrix gives two decimals only. Text (p. 4 and 5) also reports r = .36, p < .001.

**Ключевые поля выборки:**
- **n_analysed: 200** — Page 4, Table 1; Page 6, Table 3 note — «Descriptive Statistics and Reliability Coefficients for AI Dependence, Fear of Negative Evaluation and Impostor Syndrome (N = 200)»
- **population: university_students** — Page 3, Participants — «The study involved 200 undergraduate students from various universities throughout Pakistan»
- **sampling: convenience** — Page 3, Participants — «A non-probability convenience sampling method was used. Online resources such as social media networks, student WhatsApp groups, and university discussion forums were used to attract participants.»
- **ai_system: ai_unspecified** — Page 3, Participants; Page 1, Introduction — «the criteria for inclusion required them to use AI-based academic tools at least three times a week»

**Остальные поля:**
- country: PAK — Page 3, Participants — «200 undergraduate students from various universities throughout Pakistan»
- data_years: NR — Page 1, Article History — «Received on 11 June 2025»
- design: cross-sectional — Page 6-7, Limitations — «First, the study's cross-sectional design restricts causal interpretations.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 3, Participants — «the majority falling in the 18–22 age bracket (55.5%), followed by those aged 23–27 years (37.5%); only 7% were older than 27.»
- age_sd: NR — Page 3, Participants — «NR»
- age_min: 18 — Page 3, Participants — «The ages of the participants ranged from 18 to over 37 years»
- age_max: NR (reported only as 'over 37') — Page 3, Participants — «The ages of the participants ranged from 18 to over 37 years»
- pct_female: 50 — Page 3, Participants — «evenly split between 100 males and 100 females»
- mode: online — Page 3, Participants — «Data were gathered using forms for online surveys posted on Google Forms.»
- attention_checks: NR — Page 4, Procedure — «After submission, responses were automatically saved and securely stored for analysis.»
- pub_status: journal — Page 1, header — «Journal of Media Horizons ISSN: 2710-4060 2710-4052 Volume 6, Issue 4, 2025»
- language: English — Full text — «FROM AI DEPENDENCE TO IMPOSTOR SYNDROME: THE MEDIATING ROLE OF FEAR OF NEGATIVE EVALUATION»
- funding_coi: NR (no funding or conflict-of-interest statement) — Full text — «NR»
- notes: Inclusion required AI-based academic tool use at least 3 times/week (54.5% frequent, 45.5% very frequent). 75% Bachelor's, 25% Master's. AI dependence was scored as the mean of 33 items on a 1-4 scale (M = 2.83, SD = 0.41). Impostor Syndrome (CIPS) is not a dictionary construct and was not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability convenience sample recruited online via social media, WhatsApp groups and forums. — Page 3, Participants — «A non-probability convenience sampling method was used.»
2. отклик: **unclear** — No response rate and no comparison of non-responders reported (open online recruitment). — Page 4, Procedure — «The survey forms were shared in online resources including social media platforms, student WhatsApp groups and university discussion forums.»
3. валидная шкала зависимости от ИИ: **yes** — Students' AI Dependency in 3R's Questionnaire has a published development and validation study (Capinding, 2024). — Page 3, Measurement Scales; Page 7, References — «introduced and validated by Capinding (2024)»
4. надёжность шкалы ИИ в выборке: **yes** — Total-scale alpha = .91 in this sample (subscales .78-.88). — Page 3-4, Measurement Scales — «internal consistency for the overall scale was excellent (α = .91).»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (fear of negative evaluation) was measured with the published BFNE (Leary, 1983). — Page 4, Measurement Scales — «The Brief Fear of Negative Evaluation Scale (Leary, 1983) was employed»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported. — Page 4, Procedure — «Participants were requested to respond truthfully keeping in view their recent academic experiences.»

Правки:
- 

Проверено: да

---

## ST108 · Sanjaya 2025 · PAEDAGOGY Jurnal Ilmu Pendidikan dan Psikologi

Основной отчёт R4124: [текст](../../fulltext/text/R4124.txt) · [PDF](../../fulltext/pdf/R4124.pdf) — «HUBUNGAN KETERGANTUNGAN PADA CHATGPT DAN SELF-EFFICACY PADA MAHASISWA AKTIF DI UNIVERSITAS» — [DOI](https://doi.org/10.51878/paedagogy.v5i3.7659)
Расхождения в тексте: (1) Self-efficacy reliability is reported three ways. Methods give alpha .89 for ASES. Table 2 text gives .831 for 21 items, and the self-efficacy scale is assumed to be the 21-item scale. Page 7 gives 'GSES α = 0.916'. PCUS alpha is .86 in Methods and .858 in Table 4 (11 items). (2) The self-efficacy instrument has three names: Academic Self-Efficacy Scale (ASES), Self-Efficacy Scale (SES) and GSES. (3) Methods list 5 faculties, but Results say participants came from eight faculties. (4) Table 6 is titled 'Statistik Item-Total untuk Skala Ketergantungan ChatGPT (PCUS)' [item-total statistics for the PCUS], but it actually reports the Kolmogorov-Smirnov normality test. (5) The texts on Tables 2–7 describe tables that are images and are not in the extracted text. The Spearman value -0.128 is the same in the abstract, the Results and the Discussion. (6) Methods report a CFA (CFI = 0.92, R…
Заметка ИИ: There is one effect: PCUS total with academic self-efficacy (Spearman). No subscale correlations are reported. The reviewer should check the Table 7 image to confirm the value and n.

### ST108-1 · University X students (multiple faculties), Indonesia, n=76
Отчёты: R4124 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PCUS · total (T1) | **self_efficacy** · Academic Self-Efficacy Scale (ASES; also called SES/GSES in… | spearman | **-0.128** | **76** | 1 | Page 8–9 (text on Table 7); Page 9, Pembahasan | «nilai korelasi Spearman rs = -0.128 dan p = 0.271 [Spearman correlation rs = -0.128 and p = 0.271]» |

- E1: α ИИ .858, α коррелята unclear: .89 / .831 / .916; заметка: Table 7 is an image not present in the extracted text; the value is taken from the text (also in the abstract). Academic self-efficacy, not AI self-efficacy. Correlate alpha is reported three ways: .89 (Methods), .831 (Table 2), .916 (p.7).

**Ключевые поля выборки:**
- **n_analysed: 76** — Page 5, Hasil — «terdapat 76 peserta mahasiswa Universitas X [there were 76 participating University X students]»
- **population: university_students** — Page 4, Metode — «Populasi dalam penelitian ini adalah mahasiswa aktif Universitas X yang telah menggunakan ChatGPT dalam konteks akademik mereka [The population was active University X students who had used ChatGPT in their academic work]»
- **sampling: convenience** — Page 4, Metode — «Teknik pengambilan sampel yang digunakan adalah purposive sampling [The sampling technique used was purposive sampling]»
- **ai_system: general_chatbot** — Page 4, Metode — «telah menggunakan ChatGPT atau platform AI serupa dalam kegiatan akademik mereka [had used ChatGPT or similar AI platforms in their academic activities]»

**Остальные поля:**
- country: IDN — Page 3; Page 1 affiliation — «mahasiswa aktif di Universitas X, yang menghadapi tantangan akademik dalam konteks budaya dan pendidikan Indonesia [active students at University X facing acad…»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 3, Metode Penelitian — «Penelitian ini menggunakan desain kuantitatif korelasional [This study used a quantitative correlational design]»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 5, Hasil — «Usia partisipan berkisar antara 18 hingga 25 tahun, dengan mayoritas berusia 21 tahun [Participants' ages ranged from 18 to 25 years; most were 21]»
- age_sd: NR — NA — «NR»
- age_min: 18 — Page 5, Hasil — «Usia partisipan berkisar antara 18 hingga 25 tahun [Participants' ages ranged from 18 to 25 years]»
- age_max: 25 — Page 5, Hasil — «Usia partisipan berkisar antara 18 hingga 25 tahun [Participants' ages ranged from 18 to 25 years]»
- pct_female: 64.5 — Page 5, Hasil — «Jenis gender partisipan yang didominasi oleh perempuan sebanyak 64,5% [Most participants were female: 64.5%]»
- mode: online — Page 4, Metode — «Data dikumpulkan melalui kuesioner daring [Data were collected through an online questionnaire]»
- attention_checks: NR — NA — «NR»
- pub_status: journal — Page 1, header — «PAEDAGOGY : Jurnal Ilmu Pendidikan dan Psikologi Vol. 5, No. 3, September 2025»
- language: Indonesian (with English abstract) — Page 1 — «HUBUNGAN KETERGANTUNGAN PADA CHATGPT DAN SELF-EFFICACY PADA MAHASISWA AKTIF DI UNIVERSITAS»
- funding_coi: NR — NA — «NR»
- notes: Only a single-pair correlation (PCUS total with academic self-efficacy) is reported. The mean score is Tot_GPT M = 1.7033, SD = 0.50132, and the scale was not normally distributed (KS p = .034). Methods report one CFA covering both scales (CFI = .92, RMSEA = .05).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive (non-probability) sample from one university. — Page 4, Metode — «Teknik pengambilan sampel yang digunakan adalah purposive sampling [The sampling technique used was purposive sampling]»
2. отклик: **unclear** — No response rate is reported. — NA — «NR»
3. валидная шкала зависимости от ИИ: **yes** — The PCUS has a published development and validation study (Yu et al., 2024). — Page 3; Page 12, references — «Problematic ChatGPT Use Scale (PCUS) yang dikembangkan oleh Yu et al. (2024)»
4. надёжность шкалы ИИ в выборке: **yes** — PCUS alpha in this sample is .858 (Table 4); .86 in Methods. — Page 7 — «PCUS memiliki α = 0.858 > 0.6»
5. валидные шкалы коррелятов: **unclear** — The self-efficacy instrument is named inconsistently (ASES, SES, GSES) and no source citation is given for it. — Page 4; Page 7 — «Academic Self-Efficacy Scale (ASES)... Kedua alat ukur terbukti reliabel dengan GSES memiliki α = 0.916»
6. качество данных: **unclear** — No attention checks or screening of invalid responses are reported. — NA — «NR»

Правки:
- 

Проверено: да

---

## ST109 · Sun 2025 · Computers in Human Behavior

Основной отчёт R4232: [текст](../../fulltext/text/R4232.txt) · [PDF](../../fulltext/pdf/R4232.pdf) — «Emotionally Vulnerable Subtype of Internet Gaming Disorder: Measuring and Exploring the Pathology of Problematic Generative AI Use» — [DOI](https://doi.org/10.48550/arxiv.2510.06908)
Не выписано ИИ: Development/exploratory sample (Wave 1, Credamo + Prolific, N = 1,508): used for the PUGenAI-31 CFA, LPA and network replication only. No correlations with eligible correlates are reported, so there was nothing to extract. Qualitative interview sample (n = 12) and focus groups: not survey data. Validation-sample correlates not extracted because they are outside the dictionary: ADHD symptoms (the impulsivity key excludes ADHD), rumination, self-construal, outgroup trust, technology readiness (including discomfort and insecurity, which concern technology in general rather than AI anxiety), technology acceptance, trust in GenAI, GenAI literacy, use frequency, use types and information sources.
Расхождения в тексте: 1) Gender: the text gives 47.4% women in the validation sample, but Table 4 counts sum to 568 women out of 1,426 (about 39.8%), and male + female = 1,417. 2) Age: the text gives M = 41.71, SD = 20.06, while Table 4 class means are 32.96 to 40.96 and Class 2 has an implausible SD of 36.24. 3) It is unclear whether n = 1,426 is before or after excluding the 35 attention-check failures; the Table 4 class sizes sum to 1,426. 4) Table 1 alphas (Rosenberg .864, UCLA-8 .861, PSS-4 .763) are not tied to a wave; they are assumed to be from Wave 2, where the criterion measures were added. No alpha/omega is printed for the PUGenAIS-9 (only CITC values). 5) The scale is called both 'PUGenAIS-9' and 'PUGenAI-9'. 6) Figure 4 (GGM network edges among the 9 PUGenAI items) is shown only graphically and contains only exposure items, so it was not extracted. 7) The Present Study section refers to 'Figure …
Заметка ИИ: I extracted one sample: the pooled China + US Wave 2 validation sample. It has 3 correlations, taken from the 'Correlation' column of Table 4. The reliability of the PUGenAIS-9 in this sample is not reported (it may be in the supplementary material, which was not provided). Funding and conflicts of interest are not reported in the text provided.

### ST109-1 · Validation sample (Wave 2), Credamo (China) + Prolific (USA) adults, n=1,426
Отчёты: R4232 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R4232_1 · total (T1) | **self_esteem** · Rosenberg Self-Esteem Scale | pearson | **-0.24** | **1426** | 1 | Table 4 (p.14) | «Self-esteem / -0.24*** / 3.88 / 48.54 ± 10.12 / 42.61 ± 8.11» |
| E2 | ADHOC_R4232_1 · total (T1) | **loneliness** · UCLA Loneliness Scale (UCLA-8) | pearson | **0.24** | **1426** | 1 | Table 4 (p.14) | «Loneliness / 0.24*** / 2.49 / 18.50 ± 8.93 / 23.54 ± 7.48» |
| E3 | ADHOC_R4232_1 · total (T1) | **stress** · Perceived Stress Scale, 4 items (PSS-4) | pearson | **0.30** | **1426** | 1 | Table 4 (p.14) | «Stress / 0.30*** / 8.39* / 8.82 ± 3.54 / 11.05 ± 2.63» |

- E1: α ИИ NR, α коррелята 0.864; заметка: Type of correlation not stated (assumed Pearson). Two decimals only. Alpha from Table 1; the wave it refers to is not stated.
- E2: α ИИ NR, α коррелята 0.861; заметка: Type of correlation not stated (assumed Pearson). Two decimals only.
- E3: α ИИ NR, α коррелята 0.763; заметка: Type of correlation not stated (assumed Pearson). Two decimals only.

**Ключевые поля выборки:**
- **n_analysed: 1426** — p.8; Table 4 (p.14) — «In the validation phase (n = 1,426, Mean age = 41.71, SD = 20.06; 47.4% women)»
- **population: general_adults** — p.8, Participants — «Chinese participants (aged 18 years or older) ... U.S. participants (aged 18 years or older)»
- **sampling: quota or online panel** — p.8, Participants — «recruited via Credamo ... recruited through Prolific»
- **ai_system: general_chatbot** — p.1 Abstract; Table 2 (p.10) — «This study developed and validated the PUGenAIS-9 (Problematic Use of Generative Artificial Intelligence Scale-9 items) ... often felt insecure if you couldn't access GenAI?»

**Остальные поля:**
- country: MULTI: CHN, USA — p.8, Participants — «Chinese participants (aged 18 years or older) were recruited via Credamo between November 2024 and April 2025. U.S. participants (aged 18 years or older) were …»
- data_years: 2024-2025 — p.8, Participants — «recruited via Credamo between November 2024 and April 2025. U.S. participants ... were recruited through Prolific during the same period.»
- design: validation study — p.3 — «In study 3, we conducted a second large-scale survey with an independent validation sample (Wave 2) and validated the PUGenAI short form's psychometric propert…»
- clinical_group: NA — NA — «NA»
- age_mean: 41.71 — p.8, Participants — «In the validation phase (n = 1,426, Mean age = 41.71, SD = 20.06; 47.4% women)»
- age_sd: 20.06 — p.8, Participants — «Mean age = 41.71, SD = 20.06»
- age_min: 18 (eligibility criterion; observed minimum NR) — p.8, Participants — «(aged 18 years or older)»
- age_max: NR — NR — «NR»
- pct_female: 47.4 — p.8, Participants — «47.4% women»
- mode: online — p.8, Participants — «recruited via Credamo ... recruited through Prolific»
- attention_checks: yes — p.8, Participants — «35 were excluded due to failed attention checks (e.g., reporting never using GenAI).»
- pub_status: preprint — Job metadata; p.1 — «DOI: 10.48550/arxiv.2510.06908»
- language: English — p.1 — «Emotionally Vulnerable Subtype of Internet Gaming Disorder: Measuring and Exploring the Pathology of Problematic Generative AI Use»
- funding_coi: NR — NR — «NR»
- notes: Correlations come from the 'Correlation' column of Table 4 (sum score of the PUGenAIS-9 correlated with other variables) in the validation dataset; class sizes 491+140+359+436 = 1,426. The China and US subsamples were recruited on separate platforms but analysed pooled; no country-specific correlations are reported. It is unclear whether n = 1,426 is before or after excluding the 35 attention-check failures. pub_status: the text is the arXiv version, while job metadata lists Computers in Human Behavior as the venue; check whether a journal version exists. Mode online is inferred from the recr…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online crowdsourcing panels (Credamo, Prolific). — p.8, Participants — «Chinese participants ... were recruited via Credamo ... U.S. participants ... were recruited through Prolific»
2. отклик: **unclear** — No response rate reported. — p.8 — «In the validation phase (n = 1,426 ...), 35 were excluded due to failed attention checks»
3. валидная шкала зависимости от ИИ: **yes** — PUGenAIS-9 developed and validated in this report (CFA, measurement invariance, criterion validity). — p.10, Result — «The CFA of the PUGenAIS-9 model demonstrated acceptable to good model fit: CFI = 0.948, TLI = 0.931, RMSEA = 0.045, SRMR = 0.038.»
4. надёжность шкалы ИИ в выборке: **unclear** — The report says alpha and omega were computed, but no value is printed for the PUGenAIS-9 in this sample (only CITC values and a general claim of 'strong reliability'). — p.10; p.11 — «We simultaneously computed both alpha and omega (composite reliability) as measures of scale reliability»
5. валидные шкалы коррелятов: **yes** — Extracted correlates measured with published instruments (Rosenberg SES, UCLA-8, PSS-4). — Table 1 (p.9) — «Rosenberg Self-Esteem Scale (Rosenberg, 1965) ... UCLA Loneliness Scale (UCLA-8; Hays & DiMatteo, 1987) ... Perceived Stress Scale, 4 items (Cohen et al., 1983)»
6. качество данных: **yes** — Attention checks used; failing respondents excluded. — p.8, Participants — «35 were excluded due to failed attention checks (e.g., reporting never using GenAI).»

Правки:
- 

Проверено: да

---

## ST110 · Wen 2025 · Behavioral sciences (Basel, Switzerland)

Основной отчёт R4323: [текст](../../fulltext/text/R4323.txt) — «A One-Year Longitudinal Study Examining the Direct and Indirect Effects of AI Dependence on Work Engagement and Gender Differences.» — [DOI](https://doi.org/10.3390/bs16010044)
Лонгитюд (для описания): Three waves: T1 (June 2024; AI dependence and work engagement), T2 (December 2024; work self-efficacy) and T3 (June 2025; work engagement). No cross-lagged panel model was fitted, because the constructs were not measured at every wave. In PROCESS mediation models controlling for gender, age, AI use intensity, industry, job role and T1 work engagement: T1 AI dependence predicted T2 work self-efficacy (β = −0.38, 95% CI [−0.44, −0.32]). T2 self-efficacy predicted T3 work engagement (β = 0.38). The total effect of T1 AI dependence on T3 engagement was β = −0.36 and the direct effect was β = −0.22. The indirect effect was −0.14, 95% CI [−0.18, −0.11]. Gender moderated the direct path (interaction β = 0.14; males −0.27, females −0.14) but not the path to self-efficacy (β = 0.07, ns). Conditional indirect effects were −0.15 for males and −0.13 for females.
Расхождения в тексте: (1) Table 1 gives separate correlations for male and female groups (per the text) in the two triangles, but does not label which is which, and its note states N = 1108. (2) The Table 1 note reads '*** p < 0.01', while other tables use *** for p < 0.001. (3) The UWES alpha is reported as '0.94 at Time 2', but work engagement was measured at T1 and T3. (4) Text: T1 AI dependence × gender on T2 self-efficacy 'p = 0.34'; Table 4: p = 0.30. (5) Text: the interaction predicting T3 engagement is 'p < 0.05'; Table 4: ** p < 0.01. (6) Text: the conditional direct effect for females is p < 0.001; Table 5: **. (7) Text: total effect CI [−0.42, −0.31] (Table 2); Table 3: [−0.41, −0.31]. (8) Table 2: industry category on T3 engagement (−0.07, p < 0.001) has no stars.
Заметка ИИ: Country was inferred as China from the Chinese UWES version, the Beijing Normal University ethics approval and the Chinese funding; it is not stated explicitly. Work engagement is not an eligible construct. The only extractable pair is T1 AI dependence × T2 work self-efficacy, as a gender-split lagged correlation.

### ST110-1 · Employees of six companies, three-wave panel, China (inferred), n=1108
Отчёты: R4323 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R4323_1 · total (T1) | **self_efficacy** · Work self-efficacy (6 items adapted from General Self-Effic… | pearson | **−0.33** | **618 or 490 (unlabeled; note N=1108)** | lagged: T1-T2 | Table 1 (upper triangle, row 1, column 3) | «1. T1 AI dependence / 19.77 (5.43) / 19.97 (4.81) / — / −0.14 *** / −0.33 *** / −0.29 ***» |
| E2 | ADHOC_R4323_1 · total (T1) | **self_efficacy** · Work self-efficacy (6 items adapted from General Self-Effic… | pearson | **−0.47** | **618 or 490 (unlabeled; note N=1108)** | lagged: T1-T2 | Table 1 (lower triangle, row 3, column 1) | «3. T2 Work self-efficacy / 18.86 (3.77) / 18.85 (3.65) / −0.47 *** / 0.36 *** / — / 0.50 ***» |

- E1: α ИИ 0.90, α коррелята 0.93; заметка: Upper-triangle value. Table 1 reports correlations separately for males and females, but which triangle belongs to which gender is not labeled. AI dependence was measured only at T1, so no same-occasion correlation is available.
- E2: α ИИ 0.90, α коррелята 0.93; заметка: Lower-triangle value, the other gender subgroup. The triangle-to-gender assignment is not labeled. No pooled correlation is reported.

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: 1108** — Table 1 note — «Note. N = 1108.»
- **population: employees** — 2.1 Participants — «We invited full-time employees with experience in using AI products to participate in the study.»
- **sampling: convenience** — 2.1 Participants — «Participants were recruited through the human resources departments of six companies, which distributed the recruitment notice across their respective subsidiaries.»
- **ai_system: ai_unspecified** — 2.1 Participants; 2.2.1 — «full-time employees with experience in using AI products ... "I rely too much on AI,"»

**Остальные поля:**
- country: CHN (inferred; country not stated explicitly) — 2.2.3 Work Engagement; Institutional Review Board Statement… — «work engagement was evaluated using the Chinese version (Fong & Ng, 2012) of the nine-item Utrecht Work Engagement Scale ... Faculty of Psychology, Beijing Nor…»
- data_years: 2024-2025 — 2.1 Participants — «Time 1 (T1, June 2024)... Time 2 (T2, December 2024)... Time 3 (T3, June 2025)»
- design: panel — 2.1 Participants — «Data were collected through three surveys conducted over the course of one year.»
- clinical_group: NA — NA — «NA»
- age_mean: 40.63 — 2.1 Participants — «with a mean age of 40.63 years (SD = 9.54)»
- age_sd: 9.54 — 2.1 Participants — «with a mean age of 40.63 years (SD = 9.54)»
- age_min: 21 — 2.1 Participants — «The age of participants ranged from 21 to 60 years»
- age_max: 60 — 2.1 Participants — «The age of participants ranged from 21 to 60 years»
- pct_female: 44.2 (computed: 490/1108) — 2.1 Participants — «Among the 1108 participants included in the formal analysis, 618 were male and 490 were female.»
- mode: NR — 2.1 Participants — «Data were collected through three surveys conducted over the course of one year.»
- attention_checks: NR — 2.1 Participants — «NR»
- pub_status: journal — Header — «Behavioral sciences (Basel, Switzerland); DOI: 10.3390/bs16010044»
- language: English — Full text — «A One-Year Longitudinal Study Examining the Direct and Indirect Effects of AI Dependence on Work Engagement and Gender Differences»
- funding_coi: National Social Science Fund of China (CBA200241); Guangdong educational science and philosophy/social science planning grants; authors declare no conflicts of interest — Funding Statement; Conflicts of Interest — «This work was supported by the Youth Research Project in Education of the National Social Science Fund of China (Grant No. CBA200241)... The authors declare no…»
- notes: The only eligible correlate is work self-efficacy (T2; six items adapted from the GSES to fit the workplace), coded as self_efficacy. Work engagement (UWES-9) is not in the construct dictionary, so it was not extracted. AI dependence was measured only at T1, so no same-occasion correlation exists and the T1-T2 cross-occasion correlation is extracted. Table 1 gives separate correlations for males and females above and below the diagonal, but it does not say which triangle is which group, and the note gives N = 1108. Both values are extracted. No pooled correlation is reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience recruitment through company HR departments — 2.1 Participants — «Participants were recruited through the human resources departments of six companies»
2. отклик: **yes** — The baseline response rate is not reported. Retention was 1108/1212 (91%), and dropouts were compared with completers on T1 AI dependence and work engagement with no significant differences. — 2.1 Participants — «Comparisons between participants who completed all three waves and those who dropped out after T1 revealed no significant differences in T1 AI dependence (t = …»
3. валидная шкала зависимости от ИИ: **no** — Ad hoc adaptation of SAS-SV items to AI. The authors cite prior use of such an adaptation, but this report gives no validation evidence, and the authors list this as a limitation. — 2.2.1; 4. Discussion (limitations) — «the lack of reported evidence for its dimensionality, measurement invariance across gender, test–retest reliability, and discriminant validity is a notable lim…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.90 in this sample — 2.2.1 AI Dependence — «In our study, the Cronbach's alpha coefficient for the scale was 0.90»
5. валидные шкалы коррелятов: **yes** — Work self-efficacy was measured with items adapted from the published GSES, with wording tailored to work contexts; alpha 0.93. The reviewer may judge the adaptation as reducing validity. — 2.2.2 Work Self-Efficacy — «work self-efficacy was assessed using six items adapted from the General Self-Efficacy Scale (Schwarzer & Jerusalem, 1995)»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported — 2.1 Participants; 2.3 — «NR»

Правки:
- 

Проверено: да

