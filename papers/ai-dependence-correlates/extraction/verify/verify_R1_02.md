# Проверка выписывания — файл 2 из 13

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

## ST011 · Buntaran 2026 · Bulletin of Counseling and Psychotherapy

Основной отчёт R0417: [текст](../../fulltext/text/R0417.txt) · [PDF](../../fulltext/pdf/R0417.pdf) — «Does AI Dependency Hinder or Enhance Critical Thinking? Examining the Role of Self-Regulation» — [DOI](https://doi.org/10.51214/002026081616000)
Расхождения в тексте: (1) The abstract says SR "partially" mediates the AID–CTh link, but the Discussion and Implications say SR "fully mediates" it. (2) The text gives the AID–CTh correlation as "r =-.036, .036", while Table 4 shows -.036. (3) Table 4 shows SR–CTh = -.345 (negative), but the Discussion says SR shows "a strong correlation with critical thinking" and that good self-regulation goes with higher critical thinking. The path SR→CTh is also negative (-0.371). (4) Table 3 shows higher SR in females (M=20.83) than males (M=18.49), but the Discussion says the male SR mean was higher. (5) The CTh scale is described as a "5-point Likert scale from 1 (strongly disagree) to 4 (strongly agree)". (6) The Sobel test is reported with p < .001 at z = -2.66, which is inconsistent (z = -2.66 implies p ≈ .008). (7) The job instrument list codes the AID scale as study-specific, but the report attributes it to the …
Заметка ИИ: One sample and one eligible effect: AI dependency with self-regulation (r = .317, n = 112). The sampling method and data-collection years are not reported.

### ST011-1 · Private university students, West Jakarta, Indonesia (n=112)
Отчёты: R0417 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0417_1 · total (T4) | **self_control** · Self-Regulation Questionnaire short form (Brown et al., 199… | pearson | **.317** | **112** | 1 | Page 5, Table 4 | «AID / 1 / .317** / -.036» |

- E1: α ИИ .724, α коррелята .890; заметка: Self-regulation coded as self_control (dictionary includes self-regulation). Note SR correlates -.345 with critical thinking, which goes against the authors' interpretation that SR relates to higher critical thinking. Reviewer should check whether SR scoring may be reversed (not stated).

**Ключевые поля выборки:**
- **n_analysed: 112** — Page 5, Table 2 / text — «The total number of respondents in this study was 112»
- **population: university_students** — Page 3, Participants — «active students at a private campus in West Jakarta»
- **sampling: NR** — Page 3, Participants — «with a target population of active students at a private campus in West Jakarta, with a total of 112 participants»
- **ai_system: general_chatbot** — Page 3, Participants — «actively using the internet and AI in the learning process (ChatGPT, Perplexity, Gemini, Gbt)»

**Остальные поля:**
- country: IDN — Page 3, Participants — «active students at a private campus in West Jakarta»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 3, Participants — «This study uses a survey method for quantitative data collection with a cross-sectional design»
- clinical_group: NA — NA — «NA»
- age_mean: 24 — Page 5, text — «The average age of the respondents in this study was 24 years old.»
- age_sd: NR — NA — «NR»
- age_min: 19 — Page 3, Participants — «with an age range of 19 to 26 years»
- age_max: 26 — Page 3, Participants — «with an age range of 19 to 26 years»
- pct_female: 68.75 (computed: 77/112) — Page 5, text — «consisting of 77 female respondents and 35 male respondents»
- mode: online — Page 3, Design — «After the data were obtained through an online questionnaire»
- attention_checks: NR — NA — «NR»
- pub_status: journal — Page 1, header — «Bulletin of Counseling and Psychotherapy | Vol 8, No 2»
- language: English (one sentence in Indonesian in the Instruments section) — Page 4, Instruments — «Uji reliabilitas yang dilakukan oleh Hoffman et al., (2024) mendapati nilai α = 0.898 [The reliability test conducted by Hoffman et al. (2024) found α = 0.898]»
- funding_coi: Funded by Mercu Buana University; conflicts of interest not reported — Page 9, Acknowledgments — «We gratefully acknowledge the full financial support for this research provided by Mercu Buana University.»
- notes: Single-campus sample. The sampling method is not described. Participants were students using AI tools (ChatGPT, Perplexity, Gemini) for learning. AID scale: 5 items, adapted into Indonesian per ITC guidelines.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Sampling method not described; single private campus, online questionnaire (likely convenience but not stated). — Page 3, Participants — «with a target population of active students at a private campus in West Jakarta, with a total of 112 participants»
2. отклик: **unclear** — No response rate or non-responder information reported. — Page 3, Participants — «with a total of 112 participants»
3. валидная шкала зависимости от ИИ: **yes** — AI Dependency Scale from a published scale development study (Hoffmann et al., 2024), adapted into Indonesian following ITC guidelines. The job list codes it as study-specific (ADHOC); reviewer to confirm. — Page 4, Instruments — «AI Dependency, AI Dependency Scale by Hoffmann et al. (2024). The AI Dependency scale is a psychometric instrument designed to measure an individual's psycholo…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .724 in this sample (5 items). — Page 4, Table 1 — «AID | .724 | 5»
5. валидные шкалы коррелятов: **yes** — Self-regulation measured with the published short-form Self-Regulation Questionnaire validated in Indonesia (Tresnadiani & Taufik, 2020). — Page 4, Instruments — «The instrument utilized in this study was the short-form adaptation validated by Tresnadiani and Taufik (2020) in Indonesia.»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported. — Page 3-4, Methods — «After the data were obtained through an online questionnaire, descriptive analysis was conducted using SPSS»

Правки:
- 

Проверено: да

---

## ST012 · Chavez Sosa 2026 · JMIR formative research

Основной отчёт R0474: [текст](../../fulltext/text/R0474.txt) — «Anxiety and Depression Associated With the Dependent Use of Generative AI in Medical Students: Cross-Sectional Study.» — [DOI](https://doi.org/10.2196/82667)
Расхождения в тексте: Spearman coefficients in the abstract, the results text and Table 4 agree. The Statistical Analysis Plan lists the adjustment covariates as "sex, age, and year of study", but the abstract and Table 5 also include income. The DIA is cited as Morales-García et al [21] in Instruments and as [7] in the Introduction. No correlation between AI dependence and the DASS-21 total score is reported. Adjusted negative binomial RRs (Table 5) are multivariable and were not extracted.
Заметка ИИ: There are no page markers, so locations are given as sections and tables. Age is reported only as median (IQR) 22 (19-24).

### ST012-1 · Medical students, private university in Lima, Peru (n=187)
Отчёты: R0474 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **stress** · DASS-21 Stress | spearman | **0.277** | **187** | 1 | Table 4 | «AI dependence × stress / 0.277 (0.16 to 0.39) / <.001 / Small» |
| E2 | DAI · total (T4) | **anxiety** · DASS-21 Anxiety | spearman | **0.336** | **187** | 1 | Table 4 | «AI dependence × anxiety / 0.336 (0.22 to 0.44) / <.001 / Moderate» |
| E3 | DAI · total (T4) | **depression** · DASS-21 Depression | spearman | **0.316** | **187** | 1 | Table 4 | «AI dependence × depression / 0.316 (0.20 to 0.43) / <.001 / Moderate» |

- E1: α ИИ 0.859, α коррелята 0.901; заметка: 95% CI 0.16 to 0.39 reported
- E2: α ИИ 0.859, α коррелята 0.855; заметка: 95% CI 0.22 to 0.44 reported
- E3: α ИИ 0.859, α коррелята 0.887; заметка: 95% CI 0.20 to 0.43 reported

**Ключевые поля выборки:**
- **n_analysed: 187** — Results; Table 1 — «A total of 187 medical students participated in the study.»
- **population: university_students** — Abstract, Methods — «A cross-sectional study was conducted with 187 human medicine students from a Peruvian university»
- **sampling: quota or online panel** — Methods, Design, Population, and Sample — «A nonprobabilistic quota sampling was used, distributed proportionally according to the year of study (from first to sixth year)»
- **ai_system: general_chatbot** — Methods, Instruments; Introduction — «explore students’ main motivations for interacting with generative AI tools in academic and personal contexts; [Intro:] AI-powered chatbots such as ChatGPT, Copilot, or Gemini»

**Остальные поля:**
- country: PER — Methods, Design, Population, and Sample — «The population consisted of 747 human medicine students enrolled in a private university in Lima during the first academic semester of 2025.»
- data_years: 2025 — Methods, Procedure — «Data collection was carried out between March 2025 and June 2025 using an online self-administered questionnaire through Google Forms.»
- design: cross-sectional — Methods, Design, Population, and Sample — «This study had an observational and cross-sectional design.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age (y), median (IQR) | 22 (19-24)»
- age_sd: NR — Table 1 — «Age (y), median (IQR) | 22 (19-24)»
- age_min: NR — Methods, Design, Population, and Sample — «The inclusion criteria were adults over 18 years of age enrolled and with a full academic load in the current semester»
- age_max: NR — Table 1 — «Age (y), median (IQR) | 22 (19-24)»
- pct_female: 58.8 — Table 1 — «Female | 110 (58.8)»
- mode: online — Methods, Procedure — «using an online self-administered questionnaire through Google Forms»
- attention_checks: NR — Methods, Statistical Analysis Plan — «First, the database was debugged to identify and correct lost or inconsistent values or outliers.»
- pub_status: journal — Header — «JMIR formative research»
- language: English — Full text — «Anxiety and Depression Associated With the Dependent Use of Generative AI in Medical Students: Cross-Sectional Study»
- funding_coi: No funding; no conflicts of interest declared — Footnotes — «Funding: The authors declared no financial support was received for this work. ... Conflicts of Interest: None declared.»
- notes: Students with a self-declared diagnosis of a mental disorder or taking psychotropics were excluded. Seventh-year interns were excluded. Age is reported only as a median (IQR). The DIA measures dependence on AI in general; participants' AI use is described as generative AI tools (chatbots).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Nonprobabilistic quota sampling; link disseminated via institutional channels; participation voluntary. — Methods, Design, Population, and Sample — «A nonprobabilistic quota sampling was used»
2. отклик: **unclear** — No response rate reported; 187 achieved vs 224 projected (83%), but number invited/reached via the online link is unknown (population 747). — Methods, Design, Population, and Sample — «a sample of 224 students was projected... effective data collection was determined by participants’ voluntary acceptance and availability, resulting in a final…»
3. валидная шкала зависимости от ИИ: **yes** — DIA developed and validated by Morales-García et al (2024) with reported CFA fit and reliability. — Methods, Instruments — «the DIA was used, developed by Morales-García et al [21] in 2024 in Peru... This instrument has demonstrated good construct validity (comparative fit index=0.9…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach alpha = 0.859 in this sample. — Methods, Instruments — «The DIA showed good reliability (Cronbach α=0.859).»
5. валидные шкалы коррелятов: **yes** — All correlates from DASS-21, a published validated instrument. — Methods, Instruments — «the Depression, Anxiety, and Stress Scale–21 (DASS-21) was used, developed by Lovibond and Lovibond [24] in 1995»
6. качество данных: **unclear** — Only generic data cleaning of lost/inconsistent values or outliers described; no attention checks or careless-responding screening rule stated. — Methods, Statistical Analysis Plan — «the database was debugged to identify and correct lost or inconsistent values or outliers.»

Правки:
- 

Проверено: да

---

## ST013 · Chen 2026 · Scientific Journal Of Humanities and Social Sciences

Основной отчёт R0490: [текст](../../fulltext/text/R0490.txt) · [PDF](../../fulltext/pdf/R0490.pdf) — «Study on the Negative Impact of AI Social Compensation on Depression Tendencies: The More You Use It, The Lonelier You Get» — [DOI](https://doi.org/10.54691/ff7khk88)
Расхождения в тексте: The correlations in the text (p.3) match Table 1. The Method section says all core variables were z-standardized before the correlation and regression analyses. However, Table 1 reports raw means (AI social compensation M = 3.21; PHQ-9 total M = 9.85), and Table 2 calls its coefficients non-standardized (e.g., 2.644, 4.160). Table 2 Model 2 and Table 4 Model 1 have the same coefficients but different constants (1.275 vs 2.192); the Table 4 note says variables were mean-centered. The 'Robot Social Presence Scale' correlate (social presence) does not fit any dictionary key and was not extracted. Sample country is not stated; only the author affiliation (Fuzhou, China) is given.
Заметка ИИ: The AI Attachment Scale (Kasturiratna & Hartanto, 2026) is used here to measure 'AI social compensation'. It was coded as the job family ADHOC_R0490_1. Percent female was derived from the mean of the gender code, so the reviewer should check it.

### ST013-1 · College students recruited online (country not stated; author affiliated in Fujian, China), n=328
Отчёты: R0490 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0490_1 · total (T4) | **loneliness** · UCLA Loneliness Scale short form (ULS-6) | pearson | **0.353** | **328** | 1 | Page 4, Table 1 | «2. Loneliness 2.20 0.48 0.353 * * * —» |
| E2 | ADHOC_R0490_1 · total (T4) | **depression** · PHQ-9 total score | pearson | **0.426** | **328** | 1 | Page 4, Table 1 | «3. Tendency towards depression 9.85 3.63 0.426 * * * 0.634 * * * —» |

- E1: заметка: Matches text on p.3 (r = 0.353). The exposure is labelled 'AI social compensation' but is measured with the AI Attachment Scale.
- E2: заметка: Matches text on p.3 (r = 0.426).

**Ключевые поля выборки:**
- **n_analysed: 328** — Page 4, Table 1 — «Table 1. Descriptive statistics of each study variable and Pearson correlation coefficient matrix (N = 328)»
- **population: university_students** — Page 3, Section 3 Method — «The study participants were college students recruited online»
- **sampling: convenience** — Page 3, Section 3 Method — «college students recruited online using convenience sampling and snowball sampling; a total of 328 valid questionnaires were obtained.»
- **ai_system: ai_unspecified** — Pages 1 and 3 — «they turn to AI with human-like qualities for communicative support, using it as a substitute or supplement for genuine relationships»

**Остальные поля:**
- country: NR — Page 1, affiliation; Page 3, Method — «1School of Art, Yango University, Fuzhou, Fujian, 350015, China»
- data_years: NR — Page 3, Method — «The study participants were college students recruited online using convenience sampling and snowball sampling»
- design: cross-sectional — Page 3, Section 3 Method — «This study employed a cross-sectional research design and collected data through a questionnaire survey.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 61 (derived from gender mean 1.61, coded 1 = male, 2 = female; not reported directly) — Page 4, Table 1 and note — «5. Gender 1.61 0.49 ... Gender: 1 = male, 2 = female»
- mode: online — Page 3, Section 3 Method — «college students recruited online using convenience sampling and snowball sampling»
- attention_checks: NR — Page 3, Section 3 Method — «a total of 328 valid questionnaires were obtained.»
- pub_status: journal — Page 1, header — «Scientific Journal Of Humanities and Social Sciences Volume 8 Issue 7, 2026 ISSN: 2688‐8653»
- language: English — Full text — «Study on the Negative Impact of AI Social Compensation on Depression Tendencies: The More You Use It, The Lonelier You Get»
- funding_coi: NR — NR — «NR»
- notes: Country of the sample is not stated (only the author affiliation in China is given). Mode was coded online from the online recruitment; the survey platform is not named. Age, data years, funding and reliabilities are not reported. The exposure is labelled 'AI social compensation' but is measured with the 15-item AI Attachment Scale (5-point Likert).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience and snowball sampling with online recruitment. — Page 3, Section 3 Method — «recruited online using convenience sampling and snowball sampling»
2. отклик: **unclear** — Response rate and number of invalid or excluded questionnaires are not reported. — Page 3, Section 3 Method — «a total of 328 valid questionnaires were obtained.»
3. валидная шкала зависимости от ИИ: **yes** — Uses the AI Attachment Scale, which has a published development and validation study (Kasturiratna & Hartanto, 2026). The study uses it to stand for 'AI social compensation', which is a reinterpretation of the construct. — Page 3, Method; Page 8, Ref [12] — «the AI Attachment Scale (15 items, 5-point Likert) was used to measure AI social compensation [12]»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega reported for this sample. — Page 3, Section 3 Method — «The study employed well-established scales for measurement»
5. валидные шкалы коррелятов: **yes** — Loneliness (ULS-6) and depression (PHQ-9) are both published instruments. — Page 3, Section 3 Method — «the short-form UCLA Loneliness Scale (ULS-6, 6 items, 4-point) was used to measure loneliness [13]; the PHQ-9 (9 items, 4-point) was used to assess depressive …»
6. качество данных: **unclear** — Only 'valid questionnaires' are mentioned; no attention checks or rule for invalid responses are described. — Page 3, Section 3 Method — «a total of 328 valid questionnaires were obtained.»

Правки:
- 

Проверено: да

---

## ST014 · Chen 2026 · Behavioral sciences (Basel, Switzerland)

Основной отчёт R0493: [текст](../../fulltext/text/R0493.txt) — «Using Machine-Learning and Network Analysis to Investigate the Risk Factors of AI Dependence: The Crucial Role of Escape and Social Motivation.» — [DOI](https://doi.org/10.3390/bs16050772)
Расхождения в тексте: 1. The zero-order Pearson correlations of AI dependence with neuroticism, extraversion, openness, agreeableness, conscientiousness, self-efficacy, depression (PHQ-9), social anxiety and AI escape motivation are shown only in Figure 1, which is a figure (probably a heatmap). They are not extracted, and the text gives no values. The text says only the direction: "AI dependence was significantly positively correlated with neuroticism, depression, social anxiety, AI use motivations, and ACE. AI dependence was negatively correlated with extraversion, age, and grade." The Discussion says self-efficacy was not significantly correlated. 2. The network partial correlations in Figure 4a are also not extracted (they are not zero-order, and they are figure-only). 3. The ethics statement gives protocol code JSPSY2025YB005 (the same as the 2025 grant number) but an approval date of 18 March 2021. The…
Заметка ИИ: There is one sample (n = 1258) and no extractable effects: the correlation matrix is published only as Figure 1. The reviewer should check the original PDF figure for printed coefficients.

### ST014-1 · Chinese university students, Naodao online platform, CHN, n=1258
Отчёты: R0493 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |


**Ключевые поля выборки:**
- **n_analysed: 1258** — Table 2 note — «Note. N = 1258.»
- **population: university_students** — 2.1. Participants — «1258 participants were included in the present study (942 females and 316 males).»
- **sampling: quota or online panel** — 2.1. Participants; 2.3. Procedure — «recruited 1344 Chinese university students through the survey platform www.naodao.com ... Upon completing the survey, participants received a 1 CNY reward.»
- **ai_system: ai_unspecified** — 2.2.1. AI Dependence; Abstract — «"I feel anxious when I am unable to use artificial intelligence"; People have become accustomed to studying or working with the guidance of artificial intelligence (AI)»

**Остальные поля:**
- country: CHN — 2.1. Participants — «The study recruited 1344 Chinese university students through the survey platform www.naodao.com.»
- data_years: NR — Institutional Review Board Statement — «approved by the Ethics Committee of Soochow University (protocol code: JSPSY2025YB005, 18 March 2021).»
- design: cross-sectional — 4.2. Theoretical and Practical Implications — «as the present study employed only a cross-sectional design.»
- clinical_group: NA — NA — «NA»
- age_mean: 22.11 — 2.1. Participants — «The average age of all participants was 22.11 years (SD = 2.69).»
- age_sd: 2.69 — 2.1. Participants — «The average age of all participants was 22.11 years (SD = 2.69).»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 74.9 — Table 1 — «Female | 942 | 74.9»
- mode: online — 2.3. Procedure — «Data were collected via the Naodao platform (www.naodao.com).»
- attention_checks: yes — 2.1. Participants — «After excluding responses with patterned responses (i.e., responding with the same response for all questions) and those that failed the attention check, 1258 …»
- pub_status: journal — Header (venue) — «Behavioral sciences (Basel, Switzerland); DOI: 10.3390/bs16050772»
- language: English — Full text — «Using Machine-Learning and Network Analysis to Investigate the Risk Factors of AI Dependence»
- funding_coi: National Social Science Fund of China (22CSH077) and Fund of Jiangsu Psychological Society (JSPSY2025YB005); authors declare no conflicts of interest. — Funding Statement; Conflicts of Interest — «This research was funded by the National Social Science Fund of China (grant number: 22CSH077) and the Fund of Jiangsu Psychological Society (grant number: JSP…»
- notes: Zero-order Pearson correlations are given only in Figure 1 (a figure; the text gives no numbers), so no effect rows can be extracted from the text. Table 3 gives multivariable regression betas and Figure 4 gives a network of regularised partial correlations (EBICglasso). Neither is eligible. Correlates measured: CBF-PI-B Big Five (Conscientiousness alpha 0.67), GSES, PHQ-9, Social Anxiety Scale (4 items after dropping one), ACEs, AI Use Motivation Scale (includes escape motivation, alpha 0.82). The reviewer should look at Figure 1 in the PDF: if it prints the coefficients as numbers, they can…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Recruited through an online survey/participant platform (Naodao) with a small payment; not a probability sample. — 2.1. Participants — «The study recruited 1344 Chinese university students through the survey platform www.naodao.com.»
2. отклик: **unclear** — No response rate reported; 1344 is the number of responses collected, not the number invited. — 2.1. Participants — «Initially, a total of 1344 questionnaire responses were collected.»
3. валидная шкала зависимости от ИИ: **yes** — Uses the published AI dependence scale developed by Huang et al. (2024). — 2.2.1. AI Dependence — «The AI dependence scale developed by Huang et al. (2024) was used to assess the participants' AI dependence. The scale includes five items»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.78 in this sample. — 2.2.1. AI Dependence; Table 2 — «The Cronbach's alpha was 0.78.»
5. валидные шкалы коррелятов: **yes** — All eligible correlates use published instruments (CBF-PI-B, GSES Chinese version, PHQ-9, Chinese Social Anxiety Scale). However, one Social Anxiety Scale item was dropped after the data were inspected, and no correlate… — 2.2.2-2.2.5 — «The Chinese version of the Social Anxiety Scale, revised by J.-L. Wang et al. (2011) was used ... Consequently, this item was excluded from the final analysis.»
6. качество данных: **yes** — Attention check and patterned-response screening applied. — 2.1. Participants — «After excluding responses with patterned responses ... and those that failed the attention check, 1258 participants were included»

Правки:
- 

Проверено: да

---

## ST015 · Ching-Tsung 2026 · Research Square

Основной отчёт R0506: [текст](../../fulltext/text/R0506.txt) · [PDF](../../fulltext/pdf/R0506.pdf) — «AI Dependency and Work Engagement: The Dual Roles of Cognitive Vigilance and Offloading under AI Hallucinations, evidence from Vietnam’s MNC Employee. Applying…» — [DOI](https://doi.org/10.21203/rs.3.rs-10421674/v1)
Не выписано ИИ: Pilot sample (n = 30) used only to check questionnaire clarity; no data reported. 41 of 277 responses were excluded during eligibility screening and data cleaning.
Расхождения в тексте: Text gives 62.0% female and 38% male; Table 1 gives 62.3% and 37.7% (147/89). The text gives the oldest age band as 35–44 and Table 1 gives it as "From 34 to 44". The note under Table 2 says "ED2, CO4 was removed (<0.70)", but ED2 is listed with a loading of 0.879 and ID1 is missing, so ID1 was probably the item removed. The text says "six constructs" but lists seven. Table 4 (Fornell-Larcker, off-diagonal) and Table 6 (latent variable correlations) report identical values; each pair was extracted once, from Table 6. HTMT values (Table 3; ID–WS 0.480, ED–WS 0.283) were not extracted. The structural paths WS→ID (0.432) and WS→ED (0.269) equal the latent correlations because each has a single predictor. No observed (Pearson) correlation matrix is reported.
Заметка ИИ: One sample. Only two effects qualify: the ID and ED dimensions of CAID, each correlated with work stress (coded as stress), both latent correlations. No CAID total score was reported. Whether job stress counts under the 'stress' construct needs the reviewer's decision.

### ST015-1 · Vietnam MNC employees using conversational AI for work, n=236
Отчёты: R0506 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | CAID · Instrumental Dependence (ID) (T2) | **stress** · Work Stress (6 items adapted from Paoline et al., 2015) | latent | **0.432** | **236** | 1 | Page 32, Table 6 (Latent variable correlations) | «WS 0.314 0.420 0.269 0.432 0.589 0.112 1.000 (columns CO CV ED ID PHAI WE WS)» |
| E2 | CAID · Emotional Dependence (ED) (T3) | **stress** · Work Stress (6 items adapted from Paoline et al., 2015) | latent | **0.269** | **236** | 1 | Page 32, Table 6 (Latent variable correlations) | «WS 0.314 0.420 0.269 0.432 0.589 0.112 1.000 (columns CO CV ED ID PHAI WE WS)» |

- E1: α ИИ 0.858, α коррелята 0.891; заметка: Same value appears off-diagonal in Table 4 (Fornell-Larcker). Work stress = job stress; reviewer to confirm fit with 'stress' construct. Equals WS→ID path (single predictor).
- E2: α ИИ 0.952, α коррелята 0.891; заметка: Same value appears off-diagonal in Table 4 (Fornell-Larcker). Work stress = job stress; reviewer to confirm fit with 'stress' construct. Equals WS→ED path (single predictor).

**Ключевые поля выборки:**
- **n_analysed: 236** — Page 18, 4.1 — «Consequently, 236 valid responses were retained for further analysis.»
- **population: employees** — Page 2, Abstract — «236 employees working in multinational corporations (MNCs) in Vietnam»
- **sampling: convenience** — Page 18, 4.1 — «The study relied on a non-probability sampling strategy, specifically purposive sampling, to recruit participants who possessed relevant experience with conversational artificial intelligence (AI) tools»
- **ai_system: general_chatbot** — Page 18, 4.1 — «“Have you ever used conversational AI tools (e.g., ChatGPT, Gemini, Copilot, or Claude) for work-related purposes?”»

**Остальные поля:**
- country: VNM — Page 2, Abstract — «data were collected from 236 employees working in multinational corporations (MNCs) in Vietnam.»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 2, Abstract — «Adopting a cross-sectional quantitative design, data were collected from 236 employees»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: 18 (lower bound of youngest age category) — Page 20, Table 1 — «From 18 to 24 years old 142 60»
- age_max: 44 (upper bound of oldest age category) — Page 21, Table 1 — «From 34 to 44 years old 17 7»
- pct_female: 62.3 — Page 20, Table 1 — «Female 147 62.3»
- mode: online — Page 18, 4.1 — «Prior to the online questionnaire, participants first received a short explanation about the research purpose»
- attention_checks: NR — Page 18, 4.1 — «Following eligibility screening and data cleaning, forty-one questionnaires were excluded because they failed to meet the inclusion criteria.»
- pub_status: preprint — Page 1 — «Article ... Posted Date: July 30th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-10421674/v1»
- language: English (questionnaire administered in Vietnamese) — Page 19, 4.2 Measurement — «All measurement items were translated from English into Vietnamese and underwent minor wording modifications»
- funding_coi: No funding received; no competing interests declared. — Pages 57-58, Declarations/Funding — «The authors declare that no funds, grants, or other support were received during the preparation of this manuscript.»
- notes: CAID (Li et al., 2026) 14 items adapted, 7-point Likert; ID modelled with 6 items (ID2-ID7), ED with 7 items. No CAID total score reported. Only correlate fitting the dictionary is Work Stress (Paoline et al., 2015), coded as 'stress' — reviewer should confirm that job/work stress belongs under the stress construct. Cognitive vigilance, cognitive offloading, perceived AI hallucination and work engagement do not fit dictionary keys and were not extracted. Correlations are latent (PLS-SEM latent variable correlations).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability purposive sampling via online questionnaire. — Page 18, 4.1 — «The study relied on a non-probability sampling strategy, specifically purposive sampling»
2. отклик: **unclear** — No response rate reported; only 277 responses received, of which 236 retained. — Page 18, 4.1 — «The data collection process yielded 277 responses in total.»
3. валидная шкала зависимости от ИИ: **yes** — Adapted from the published CAID development/validation study (Li et al., 2026); CFA-type loadings, AVE, CR also reported here. — Page 19, 4.2; Page 68 references — «AI Dependency, encompassing both Instrumental Dependence and Emotional Dependence dimensions, was measured using fourteen items adapted from Li et al. (2026).»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha ID = 0.858, ED = 0.952 in this sample. — Pages 26-27, Table 2 — «Emotional Dependence 0.952 0.960 0.776 ... Instrumental Dependence 0.858 0.894 0.586»
5. валидные шкалы коррелятов: **yes** — Work stress measured with items adapted from a published job stress scale (Paoline et al., 2015). — Page 20, 4.2 — «Work Stress was measured using six items adapted from Paoline et al. (2015).»
6. качество данных: **unclear** — 'Data cleaning' mentioned but no attention checks or explicit rule for invalid/careless responses described; exclusions attributed to inclusion criteria. — Page 18, 4.1 — «Following eligibility screening and data cleaning, forty-one questionnaires were excluded because they failed to meet the inclusion criteria.»

Правки:
- 

Проверено: да

---

## ST016 · Demirhan 2026 · International Journal of Mental Health and Addiction

Основной отчёт R0579: [текст](../../fulltext/text/R0579.txt) · [PDF](../../fulltext/pdf/R0579.pdf) — «The Role of Biological Rhythms in Generative AI Addiction: Associations with Chronotype and Sleep Quality» — [DOI](https://doi.org/10.1007/s11469-026-01679-3)
Расхождения в тексте: The text and Table 2 agree for AI-AS total with PSQI (.204) and with CSM (-.146). (1) The Discussion says chronotype and sleep quality "accounted for only 5.0% of the variance", but Table 4 gives R2 = .054 (adjusted R2 = .050), and the Results text says 5.4%. (2) The Discussion says evening types scored higher than "morning and intermediate types", but the ANCOVA post hoc in Table 3 shows only E > M and N > M (no E > N). (3) In Table 1 the gender-specific PSQI means (female 6.78, n=500; male 6.92, n=368) give a weighted mean of about 6.84, while the reported total is 6.89 (minor discrepancy). (4) In Table 3 the df are printed as "1.855" / "2.855", which presumably means 1,855 / 2,855. (5) The PSQI threshold of >5 classes most of the sample as poor sleepers (mean 6.89). (6) The PSQI correlations with the subscales and PSQI components are said to appear in Supplementary Table S1, which wa…
Заметка ИИ: There is one cross-sectional sample with 5 effects: the AI-AS total and its 4 subscales, each correlated with the PSQI global score. Please check rob_3. The AI-AS validation is cited as "Authors (under review)", so it is unpublished. I rated it "no", but this is a borderline call.

### ST016-1 · Undergraduate students, state university (Sakarya), Türkiye, n=868
Отчёты: R0579 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0579_1 · total (T1) | **sleep_quality** · Pittsburgh Sleep Quality Index (PSQI) global score, Turkish… | pearson | **.204** | **868** | 1 | Page 9, Table 2 | «AI-AS Total / 1 / .204** / -.146**» |
| E2 | ADHOC_R0579_1 · Functional Impairment (T1) | **sleep_quality** · Pittsburgh Sleep Quality Index (PSQI) global score, Turkish… | pearson | **.186** | **868** | 1 | Page 9, Table 2 | «I. Impairment / 1 / .570** .409** .591** .790** / .186** / -.102**» |
| E3 | ADHOC_R0579_1 · Mood Modification (T1) | **sleep_quality** · Pittsburgh Sleep Quality Index (PSQI) global score, Turkish… | pearson | **.148** | **868** | 1 | Page 9, Table 2 | «II. Mood / 1 / .592** .589** .834** / .148** / -.096**» |
| E4 | ADHOC_R0579_1 · Excessive Dependency (T4) | **sleep_quality** · Pittsburgh Sleep Quality Index (PSQI) global score, Turkish… | pearson | **.138** | **868** | 1 | Page 9, Table 2 | «III. Excessive Dependency / 1 / .602** .791** / .138** / -.120**» |
| E5 | ADHOC_R0579_1 · Salience (T1) | **sleep_quality** · Pittsburgh Sleep Quality Index (PSQI) global score, Turkish… | pearson | **.193** | **868** | 1 | Page 9, Table 2 | «IV. Salience / 1 / .857** / .193** / -.158**» |

- E1: **направление: reversed (higher PSQI = poorer sleep quality)**; α ИИ .93, α коррелята .76; заметка: Also given in the text as r =.204, p <.001
- E2: **направление: reversed (higher PSQI = poorer sleep quality)**; α ИИ NR, α коррелята .76; заметка: Table label is 'I. Impairment', mapped to the Functional Impairment subscale
- E3: **направление: reversed (higher PSQI = poorer sleep quality)**; α ИИ NR, α коррелята .76; заметка: Table label is 'II. Mood', mapped to the Mood Modification subscale
- E4: **направление: reversed (higher PSQI = poorer sleep quality)**; α ИИ NR, α коррелята .76
- E5: **направление: reversed (higher PSQI = poorer sleep quality)**; α ИИ NR, α коррелята .76

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2, E3, E4, E5: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление

**Ключевые поля выборки:**
- **n_analysed: 868** — Page 8, Table 1; Page 9, Table 2 — «Total 868 40.16 ± 13.48 6.89 ± 2.04 32.38 ± 6.17»
- **population: university_students** — Page 6, Participants — «868 university students enrolled in various departments at a state university in Turkey»
- **sampling: convenience** — Page 6, Participants — «Convenience sampling was employed to select undergraduate students for participation in the study.»
- **ai_system: general_chatbot** — Page 1 Abstract; Page 14, Limitations — «Generative Artificial Intelligence (GenAI) technologies ... specific platforms (e.g., ChatGPT, Midjourney) was not collected»

**Остальные поля:**
- country: TUR — Page 6, Participants — «The study sample comprised 868 university students enrolled in various departments at a state university in Turkey.»
- data_years: 2025 — Page 7, Data Collection and Analysis — «the data were gathered via paper-and-pencil administration and an online survey platform between September and December 2025»
- design: cross-sectional — Page 5, Method — «The research was conducted using a cross-sectional survey design, whereby all variables were assessed concurrently at a single time point via self-report instr…»
- clinical_group: NA — NA — «NA»
- age_mean: 20.82 — Page 6, Participants — «The mean age of the overall sample was 20.82 ± 2.23 years and ages ranged between 17 and 38 years.»
- age_sd: 2.23 — Page 6, Participants — «The mean age of the overall sample was 20.82 ± 2.23 years»
- age_min: 17 — Page 6, Participants — «ages ranged between 17 and 38 years»
- age_max: 38 — Page 6, Participants — «ages ranged between 17 and 38 years»
- pct_female: 57.6 — Page 6, Participants — «57.6% (N = 500) of the participants were female and 42.4% (N = 368) were male»
- mode: mixed — Page 7, Data Collection and Analysis — «the data were gathered via paper-and-pencil administration and an online survey platform»
- attention_checks: NR — Page 7, Data Collection and Analysis — «Prior to the main analyses, preliminary tests were conducted to examine statistical assumptions.»
- pub_status: journal — Page 1 — «International Journal of Mental Health and Addiction ... ORIGINAL ARTICLE»
- language: English — Full text — «The Role of Biological Rhythms in Generative AI Addiction: Associations with Chronotype and Sleep Quality»
- funding_coi: Open access funding by TÜBİTAK; participation without financial support; no conflicts of interest reported — Page 14, Funding; Page 15, Conflict of Interest — «Open access funding provided by the Scientific and Technological Research Council of Türkiye (TÜBİTAK). ... No potential conflict of interest was reported by t…»
- notes: AI system coded general_chatbot because exposure is 'Generative AI' generically; platforms not recorded (authors mention ChatGPT, Midjourney as examples) – reviewer may prefer ai_unspecified. The only eligible correlate is the PSQI global score (sleep_quality; higher = poorer sleep, so reversed). Chronotype (CSM) is not in the construct dictionary and is not extracted. PSQI: the five items needing a bed partner were excluded. Subscale reliabilities are not reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample from a single state university — Page 6, Participants — «Convenience sampling was employed to select undergraduate students for participation in the study.»
2. отклик: **unclear** — Response rate is not reported — Page 6, Participants — «Participation in the study was entirely voluntary, with no financial support provided, and responses were collected anonymously.»
3. валидная шкала зависимости от ИИ: **no** — The AI-AS was developed by the authors and its validation is 'under review' (not published). This report does not contain a validation; it gives only the original alpha/omega. Borderline: please check whether the valida… — Page 7, AI-AS section — «the Artificial Intelligence Addiction Scale (AI-AS), developed by Authors (under review), was administered. ... The original form of the AI-AS demonstrated exc…»
4. надёжность шкалы ИИ в выборке: **yes** — Internal consistency of the total score in this sample = .93 — Page 7, AI-AS section — «in the current study, the AI-AS' internal consistency coefficient was calculated as.93»
5. валидные шкалы коррелятов: **yes** — The extracted correlate (PSQI) is a published instrument with a Turkish adaptation — Page 7, PSQI section — «Sleep quality was measured using the Pittsburgh Sleep Quality Index (Buysse et al., 1989), which was adapted into Turkish by Ağargün et al. (1996).»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule is reported — Page 7, Data Collection and Analysis — «Prior to the main analyses, preliminary tests were conducted to examine statistical assumptions. Normality was assessed using skewness and kurtosis statistics»

Правки:
- 

Проверено: да

---

## ST017 · Elsayed 2026 · Research Square

Основной отчёт R0691: [текст](../../fulltext/text/R0691.txt) · [PDF](../../fulltext/pdf/R0691.pdf) — «AI-Dependency and Its Relationships with Anxiety, Quality of Life, and Digital Stress» — [DOI](https://doi.org/10.21203/rs.3.rs-8870746/v1)
Приложен R0690: [текст](../../fulltext/text/R0690.txt) · [PDF](../../fulltext/pdf/R0690.pdf) — «AI dependency and its relationships with anxiety, quality of life, and digital stress»
Связь отчётов: Two Research Square versions of one preprint (King Abdulaziz University, N = 521, 15-item AI-Dependency Scale); the version of record is BMC Psychology 10.1186/s40359-026-05496-0
Расхождения в тексте: 1. The R0690 text attached here is word-for-word the same as R0691. It is the Research Square preprint text, not the BMC Psychology version of record, so no differences can be checked. 2. Correlations not extracted because no dictionary key fits: Availability Pressure, Digital Overconnectivity, Digital Vigilance and the total digital stress score. These are digital stress/technostress, which the dictionary excludes from stress. 3. Table 3 shows only the rows for Anxiety, QoL, DIR, PAD, CAR and Ai-Dep. The rows for the digital stress subscales are missing, although the text reports r = 0.63–0.87 between those subscales and the total. 4. The text says AI dependency is 'closely linked to digital stressors, including digital vigilance and fear of missing out'. Table 3 does not support this: the zero-order r values are about 0 (e.g., Ai-Dep–FoMO 0.030, Ai-Dep–DV -0.017). The claim may come f…
Заметка ИИ: I extracted 16 effects: 4 AI-dependence scores (total, DIR, PAD, CAR) × 4 correlates. The correlates are AI-related anxiety (coded ai_anxiety), the self-developed quality-of-life scale (coded wellbeing), the digital-stress FoMO subscale (coded fomo) and the digital-stress Social Acceptance Anxiety subscale (coded social_anxiety, tentative). n = 521 is assumed for Table 3 because the table does not state its n.

### ST017-1 · King Abdulaziz University students and staff, Saudi Arabia, n=521
Отчёты: R0691 (main); R0690

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0691_1 · total (T4) | **ai_anxiety** · AI-Related General Anxiety Scale | pearson | **0.228** | **521** | 1 | Page 13, Table 3 | «Anxiety / 1 / 0.343 / 0.064 / 0.246 / 0.302 / 0.228 / -0.170» |
| E2 | ADHOC_R0691_1 · Direct Interaction Reliance (DIR; Q2, Q3, Q4, Q5,… (T4) | **ai_anxiety** · AI-Related General Anxiety Scale | pearson | **0.064** | **521** | 1 | Page 13, Table 3 | «Anxiety / 1 / 0.343 / 0.064 / 0.246 / 0.302 / 0.228» |
| E3 | ADHOC_R0691_1 · Practical/Applied Dependency (PAD; Q6–Q10) (T2) | **ai_anxiety** · AI-Related General Anxiety Scale | pearson | **0.246** | **521** | 1 | Page 13, Table 3 | «Anxiety / 1 / 0.343 / 0.064 / 0.246 / 0.302 / 0.228» |
| E4 | ADHOC_R0691_1 · Cognitive/Affective Reliance (CAR; Q1, Q11, Q13–Q… (T4) | **ai_anxiety** · AI-Related General Anxiety Scale | pearson | **0.302** | **521** | 1 | Page 13, Table 3 | «Anxiety / 1 / 0.343 / 0.064 / 0.246 / 0.302 / 0.228» |
| E5 | ADHOC_R0691_1 · total (T4) | **wellbeing** · Quality of Life scale (self-developed, 12 items) | pearson | **0.283** | **521** | 1 | Page 13, Table 3 | «QoL / 1 / 0.237 / 0.249 / 0.279 / 0.283 / -0.079» |
| E6 | ADHOC_R0691_1 · Direct Interaction Reliance (DIR; Q2, Q3, Q4, Q5,… (T4) | **wellbeing** · Quality of Life scale (self-developed, 12 items) | pearson | **0.237** | **521** | 1 | Page 13, Table 3 | «QoL / 1 / 0.237 / 0.249 / 0.279 / 0.283» |
| E7 | ADHOC_R0691_1 · Practical/Applied Dependency (PAD; Q6–Q10) (T2) | **wellbeing** · Quality of Life scale (self-developed, 12 items) | pearson | **0.249** | **521** | 1 | Page 13, Table 3 | «QoL / 1 / 0.237 / 0.249 / 0.279 / 0.283» |
| E8 | ADHOC_R0691_1 · Cognitive/Affective Reliance (CAR; Q1, Q11, Q13–Q… (T4) | **wellbeing** · Quality of Life scale (self-developed, 12 items) | pearson | **0.279** | **521** | 1 | Page 13, Table 3 | «QoL / 1 / 0.237 / 0.249 / 0.279 / 0.283» |
| E9 | ADHOC_R0691_1 · total (T4) | **fomo** · Digital stress test – Fear of Missing Out subscale | pearson | **0.030** | **521** | 1 | Page 13, Table 3 | «Ai-Dep / 1 / 0.000 / -0.016 / 0.030 / 0.035 / -0.017 / 0.009» |
| E10 | ADHOC_R0691_1 · Direct Interaction Reliance (DIR; Q2, Q3, Q4, Q5,… (T4) | **fomo** · Digital stress test – Fear of Missing Out subscale | pearson | **0.032** | **521** | 1 | Page 13, Table 3 | «DIR / 1 / 0.712 / 0.649 / 0.876 / -0.005 / -0.011 / 0.032 / 0.080» |
| E11 | ADHOC_R0691_1 · Practical/Applied Dependency (PAD; Q6–Q10) (T2) | **fomo** · Digital stress test – Fear of Missing Out subscale | pearson | **0.045** | **521** | 1 | Page 13, Table 3 | «PAD / 1 / 0.745 / 0.928 / 0.002 / 0.002 / 0.045 / 0.008» |
| E12 | ADHOC_R0691_1 · Cognitive/Affective Reliance (CAR; Q1, Q11, Q13–Q… (T4) | **fomo** · Digital stress test – Fear of Missing Out subscale | pearson | **-0.003** | **521** | 1 | Page 13, Table 3 | «CAR / 1 / 0.880 / 0.005 / -0.038 / -0.003 / 0.010» |
| E13 | ADHOC_R0691_1 · total (T4) | **social_anxiety** · Digital stress test – Social Acceptance Anxiety subscale | pearson | **-0.016** | **521** | 1 | Page 13, Table 3 | «Ai-Dep / 1 / 0.000 / -0.016 / 0.030 / 0.035» |
| E14 | ADHOC_R0691_1 · Direct Interaction Reliance (DIR; Q2, Q3, Q4, Q5,… (T4) | **social_anxiety** · Digital stress test – Social Acceptance Anxiety subscale | pearson | **-0.011** | **521** | 1 | Page 13, Table 3 | «DIR / 1 / 0.712 / 0.649 / 0.876 / -0.005 / -0.011 / 0.032» |
| E15 | ADHOC_R0691_1 · Practical/Applied Dependency (PAD; Q6–Q10) (T2) | **social_anxiety** · Digital stress test – Social Acceptance Anxiety subscale | pearson | **0.002** | **521** | 1 | Page 13, Table 3 | «PAD / 1 / 0.745 / 0.928 / 0.002 / 0.002 / 0.045» |
| E16 | ADHOC_R0691_1 · Cognitive/Affective Reliance (CAR; Q1, Q11, Q13–Q… (T4) | **social_anxiety** · Digital stress test – Social Acceptance Anxiety subscale | pearson | **-0.038** | **521** | 1 | Page 13, Table 3 | «CAR / 1 / 0.880 / 0.005 / -0.038 / -0.003» |

- E1: α ИИ omega = 0.95, α коррелята omega = 0.89; заметка: Scale measures anxiety in relation to AI use (includes concentration, tension, sleep items); coded ai_anxiety, reviewer may consider anxiety. Text confirms r = 0.228.
- E2: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.89; заметка: Column DIR.
- E3: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.89; заметка: Column PAD.
- E4: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.89; заметка: Column CAR.
- E5: **направление: as named (higher = higher perceived quality of life)**; α ИИ omega = 0.95, α коррелята NR; заметка: Self-developed QoL scale capturing psychological well-being; coded wellbeing. No reliability coefficient reported.
- E6: **направление: as named (higher = higher perceived quality of life)**; α ИИ NR (subscale omegas 0.75-0.92), α коррелята NR; заметка: Column DIR.
- E7: **направление: as named (higher = higher perceived quality of life)**; α ИИ NR (subscale omegas 0.75-0.92), α коррелята NR; заметка: Column PAD.
- E8: **направление: as named (higher = higher perceived quality of life)**; α ИИ NR (subscale omegas 0.75-0.92), α коррелята NR; заметка: Column CAR.
- E9: α ИИ omega = 0.95, α коррелята omega = 0.66; заметка: FoMO is a situational subscale of a study-adapted digital stress measure (based on Xie et al.), not the Przybylski FoMO Scale. Omega from Table 1.
- E10: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.66; заметка: Column FoMO.
- E11: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.66; заметка: Column FoMO.
- E12: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.66; заметка: Column FoMO.
- E13: α ИИ omega = 0.95, α коррелята omega = 0.66; заметка: Reviewer check: SAA measures fear of negative evaluation of one's online posts (digital stress component); mapping to social_anxiety is tentative.
- E14: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.66; заметка: Column SAA; tentative mapping to social_anxiety.
- E15: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.66; заметка: Column SAA (second 0.002 in row; first is AP); tentative mapping to social_anxiety.
- E16: α ИИ NR (subscale omegas 0.75-0.92), α коррелята omega = 0.66; заметка: Column SAA; tentative mapping to social_anxiety.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.01 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 521** — Page 6, Participants; Table 3 (n not stated in table) — «The study included 521 participants recruited through snowball sampling»
- **population: university_students** — Page 6, Participants — «The majority were undergraduate students (n = 466, 89.4%), with smaller proportions of postgraduate students (n = 10, 1.9%), faculty or lecturers (n = 18, 3.5%), and employees or technicians (n = 27, 5.2%).»
- **sampling: snowball** — Page 6, Participants — «The study included 521 participants recruited through snowball sampling»
- **ai_system: ai_unspecified** — Page 6-7, Instruments, AI-Dependency Scale — «To assess the extent to which individuals rely on digital tools and AI-driven resources in their daily tasks and decision-making processes.»

**Остальные поля:**
- country: SAU — Page 6, Participants — «The study included 521 participants recruited through snowball sampling, ensuring no participant was enrolled in classes taught by the researchers at King Abdu…»
- data_years: NR — Page 11, Ethical consideration — «approved by the Research Ethics Committee of the Faculty of Arts and Humanities, King Abdulaziz University (Serial Number: REC-FAH-KAU-2026-003, dated 31 Decem…»
- design: cross-sectional — Page 6, Design — «Data were collected via self-administered standardized measures during a single assessment period»
- clinical_group: NA — NA — «NA»
- age_mean: 21.92 — Page 6, Participants — «Participants’ ages ranged from 18 to 58 years (M = 21.92, SD = 3.75)»
- age_sd: 3.75 — Page 6, Participants — «Participants’ ages ranged from 18 to 58 years (M = 21.92, SD = 3.75)»
- age_min: 18 — Page 6, Participants — «Participants’ ages ranged from 18 to 58 years»
- age_max: 58 — Page 6, Participants — «Participants’ ages ranged from 18 to 58 years»
- pct_female: 80.2 — Page 6, Participants — «the sample was predominantly female (n = 418, 80.2%), with males comprising 19.8% (n = 103)»
- mode: online — Page 18, Declarations — «informed consent to participate was obtained online from all participants before their inclusion in the study.»
- attention_checks: NR — Page 6, Methodology — «Data were collected via self-administered standardized measures during a single assessment period»
- pub_status: preprint — Page 1 — «Posted Date: March 22nd, 2026 DOI: https://doi.org/10.21203/rs.3.rs-8870746/v1»
- language: English — whole text — «AI-Dependency and Its Relationships with Anxiety, Quality of Life, and Digital Stress»
- funding_coi: Funded by KAU Endowment (WAQF), King Abdulaziz University, and Deanship of Scientific Research; funders had no role; authors declare no competing interests. — Page 18, Declarations — «This project was funded by KAU Endowment (WAQF) at King Abdulaziz University, Jeddah, Saudi Arabia... The authors declare that they have no competing interests.»
- notes: 10.6% of the sample are faculty or employees, not students; the sample is coded as university students. Mode is coded online because consent was obtained online. Data-collection year is not reported (ethics approval dated 31 Dec 2025). Subscale omegas for the AI-Dependency Scale are reported only as a range (0.75–0.92).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Snowball sampling. — Page 6, Participants — «521 participants recruited through snowball sampling»
2. отклик: **unclear** — Response rate not reported. — Page 6, Participants — «The study included 521 participants recruited through snowball sampling»
3. валидная шкала зависимости от ИИ: **yes** — Study-specific 15-item scale, but this report gives psychometric validation (EFA, second-order CFA, omega). — Page 7, AI-Dependency Scale — «Exploratory factor analysis (EFA) of the 15-item AI dependency scale indicated excellent data adequacy... The second-order confirmatory factor analysis (CFA) s…»
4. надёжность шкалы ИИ в выборке: **yes** — Omega total 0.95 in this sample. — Page 7, AI-Dependency Scale — «Reliability analysis yielded high internal consistency, with Omega Total = 0.95, Omega Hierarchical = 0.80, and subscale Omegas ranging from 0.75 to 0.92»
5. валидные шкалы коррелятов: **no** — QoL scale is self-developed; AI-related anxiety scale has no cited source; digital stress scale is adapted/new situational items (psychometrics given in this report only). — Page 8, Quality of Life scale — «A self-developed measure of quality of life was constructed. At the same time, the instrument is original to the researcher»
6. качество данных: **unclear** — No attention checks or rules for invalid responses reported. — Page 6, Methodology — «Data were collected via self-administered standardized measures during a single assessment period»

Правки:
- 

Проверено: да

---

## ST018 · FAN 2026 · Frontiers in Psychology

Основной отчёт R0722: [текст](../../fulltext/text/R0722.txt) · [PDF](../../fulltext/pdf/R0722.pdf) — «The relationship between challenge-hindrance stressors and AI dependence among art students: the mediating roles of creative self-efficacy and positive experie…» — [DOI](https://doi.org/10.3389/fpsyg.2026.1924924)
Не выписано ИИ: The pilot sample of 50 art students was used only to check item clarity; it was not in the final sample and no data are reported for it. No other samples.
Расхождения в тексте: The correlations in the text (Section 4.3) match Table 4 exactly: CS-AID 0.515, HS-AID 0.530, CSE-AID −0.288. Table 3 (Fornell-Larcker discriminant validity) prints the same coefficients and labels them 'Pearson correlation coefficients', so they are not latent correlations and were not extracted as separate latent rows. Table 3 HTMT ratios were not extracted. One minor mismatch: the text gives the CI for the HS chain indirect effect as [−0.000, 0.004], while Table 6 gives [0.000, 0.004]. The AI dependence instrument is called 'AI Dependence Scale' in the text but cites the AI chatbot dependence scale (Zhang X. et al., 2025). Figure 2 shows only path coefficients; nothing was extracted from it.
Заметка ИИ: I extracted one cross-sectional sample: n=580 art and design undergraduates in China. There are three effects, all with AI dependence: challenge stressors and hindrance stressors, both coded academic_stress, and creative self-efficacy, coded self_efficacy. All three construct mappings need a reviewer's judgement. Positive experiences with AI tools was not extracted because it fits no dictionary key.

### ST018-1 · Art and design undergraduates, multiple Chinese universities, CHN, n=580
Отчёты: R0722 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **academic_stress** · Challenge Stressors (Challenge-Hindrance Stress Scale, Cava… | pearson | **0.515** | **580** | 1 | Page 8, Table 4 | «AID 4.303 1.175 0.515** 0.530** −0.288** 0.356** 1» |
| E2 | AICD · total (T4) | **academic_stress** · Hindrance Stressors (Challenge-Hindrance Stress Scale, Cava… | pearson | **0.530** | **580** | 1 | Page 8, Table 4 | «AID 4.303 1.175 0.515** 0.530** −0.288** 0.356** 1» |
| E3 | AICD · total (T4) | **self_efficacy** · Creative Self-Efficacy Scale (Tierney & Farmer, 2002) | pearson | **−0.288** | **580** | 1 | Page 8, Table 4 | «AID 4.303 1.175 0.515** 0.530** −0.288** 0.356** 1» |

- E1: α ИИ 0.906, α коррелята 0.896; заметка: Coded academic_stress because the items are coursework stressors (workload, time pressure). Table 3 repeats the same Pearson value.
- E2: α ИИ 0.906, α коррелята 0.828; заметка: Coded academic_stress because the items are coursework obstacles (unclear requirements, conflicting expectations). If both stressor rows are pooled, they are two subscales of the same instrument. Table 3 repeats the value.
- E3: α ИИ 0.906, α коррелята 0.866; заметка: Creative self-efficacy is domain-specific, not general or academic self-efficacy; reviewer to confirm it is eligible. Table 3 repeats the value.

**Ключевые поля выборки:**
- **n_analysed: 580** — Page 8, Table 4; Page 5, Section 3.1 — «The remaining 580 responses were retained for analysis, yielding a valid response rate of 93.5%.»
- **population: university_students** — Page 5, Section 3.1 — «All participants were currently enrolled art or design majors and had prior experience using at least one generative AI tool for creative tasks.»
- **sampling: convenience** — Page 5, Section 3.1 — «This study employed purposive sampling to recruit undergraduate students majoring in art and design from multiple universities»
- **ai_system: ai_unspecified** — Page 5, Section 3.1; Page 6, Section 3.2 — «had prior experience using at least one generative AI tool for creative tasks ... measures an individual's level of dependence on AI tools.»

**Остальные поля:**
- country: CHN — Page 5, Section 3.1 — «undergraduate students majoring in art and design from multiple universities across various regions of China»
- data_years: 2026 — Page 5, Section 3.1 — «Data were collected from May to June 2026 through the "Wenjuanxing" online survey platform.»
- design: cross-sectional — Page 12, Section 6.3 — «First, the cross-sectional study design limits causal inferences.»
- clinical_group: NA — NA — «NA»
- age_mean: 20.58 — Page 5, Section 3.1 — «The final sample (N = 580) ranged in age from 18 to 25 years (M = 20.58, SD = 1.309).»
- age_sd: 1.309 — Page 5, Section 3.1 — «(M = 20.58, SD = 1.309)»
- age_min: 18 — Page 5, Section 3.1 — «ranged in age from 18 to 25 years»
- age_max: 25 — Page 5, Section 3.1 — «ranged in age from 18 to 25 years»
- pct_female: 50.52 — Page 6, Table 1 — «Gender Male 287 49.48% Female 293 50.52%»
- mode: online — Page 5, Section 3.1 — «through the "Wenjuanxing" online survey platform»
- attention_checks: yes — Page 5, Section 3.1 — «40 responses were excluded based on the following criteria: (a) incomplete answers, (b) straight-lining responses, and (c) excessively short completion time (l…»
- pub_status: journal — Page 1 — «TYPE Original Research ... Front. Psychol. 17:1924924.»
- language: English — Page 1 — «The relationship between challenge-hindrance stressors and AI dependence among art students»
- funding_coi: Open Research Fund of the Xinjiang Key Laboratory of Education Cloud Technology and Resources (Grant No. 2026KLEOY004); authors declare no conflict of interest. — Page 13, Funding; Conflict of interest — «supported by the Open Research Fund of the Xinjiang Key Laboratory of Education Cloud Technology and Resources (Year 2026), Grant No. 2026KLEOY004 ... conducte…»
- notes: Scales were 7-point Likert, translated and adapted to the art-student context (the Brislin back-translation procedure plus a pilot with n=50). The AI dependence measure is called the 'AI Dependence Scale' (8 items, unidimensional) and is cited as Zhang X. et al. (2025), 'development and validation of an artificial intelligence chatbot dependence scale' (AICD). The items refer to 'AI tools', not chatbots specifically. Correlates not extracted: Positive Experiences with AI tools (r=.356 with AID). This is an AI-specific appraisal of usefulness and fits no dictionary key. Challenge and hindrance…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive (convenience) sample recruited via the Wenjuanxing online platform. — Page 5, Section 3.1 — «This study employed purposive sampling ... Data were collected from May to June 2026 through the "Wenjuanxing" online survey platform.»
2. отклик: **yes** — 620 questionnaires distributed, 580 valid (93.5%). It is unclear whether 'distributed' means invitations or returned questionnaires; please check. — Page 5, Section 3.1 — «A total of 620 questionnaires were distributed. ... The remaining 580 responses were retained for analysis, yielding a valid response rate of 93.5%.»
3. валидная шкала зависимости от ИИ: **yes** — The AI Dependence Scale is cited to a published development and validation study (Zhang X. et al., 2025, Cyberpsychol Behav Soc Netw); CFA is also reported in this sample. — Page 6, Section 3.2; Page 15, References — «The AI Dependence Scale was adopted from Zhang X. et al. (2025). It consists of 8 items ... The development and validation of an artificial intelligence chatbo…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha for AID = 0.906 in this sample. — Page 7, Table 2 — «AID 0.683 ~ 0.770 0.906 0.548 0.906»
5. валидные шкалы коррелятов: **yes** — Challenge-hindrance stressors (Cavanaugh et al., 2000; Rodell & Judge, 2009) and creative self-efficacy (Tierney & Farmer, 2002) are published instruments, adapted to the context. — Pages 5-6, Section 3.2 — «The Challenge-Hindrance stressors are based on those developed by Cavanaugh et al. (2000) and revised by Rodell and Judge (2009). ... The Creative Self-Efficac…»
6. качество данных: **yes** — Stated exclusion rules for incomplete, straight-lined and too-fast responses. — Page 5, Section 3.1; Page 7, Section 3.3 — «(b) straight-lining responses, and (c) excessively short completion time (less than 120 s)»

Правки:
- 

Проверено: да

---

## ST019 · Fang 2026 · Research Square

Основной отчёт R0724: [текст](../../fulltext/text/R0724.txt) · [PDF](../../fulltext/pdf/R0724.pdf) — «How AI and Human Behaviors Shape Psychosocial Effects of Extended Chatbot Use: A Longitudinal Randomized Controlled Study» — [DOI](https://doi.org/10.21203/rs.3.rs-8148142/v1)
Лонгитюд (для описания): Four-week RCT with weekly measurement. No cross-lagged paths between AI dependence (ADS-9 craving, PCUS) and psychosocial correlates are reported. The OLS models predict week-4 emotional dependence and problematic use from condition, baseline (week-1) values, age, gender and mean-centred daily duration (Tables S10, S11, S15, S16). Exploratory multivariable OLS models add prior characteristics (Table S18). For week-4 emotional dependence and problematic use, no personality, self-esteem or attachment trait was a significant predictor. Self-esteem, neuroticism and attachment anxiety predicted only week-4 loneliness and/or socialization. Emotional-vulnerability (worsening relationships) predicted problematic use (b=0.033). These are multivariable estimates and are not extracted as effects.
Расхождения в тексте: (1) Table S17 is a sparse heatmap of Spearman rhos between exploratory variables (measured at pre-study or as perceptions) and week-4 outcomes. Only BH-significant cells are printed, and the text layer loses cell positions. Rows for self-esteem (RSES), BFI-10 personality and Attachment Anxiety therefore could not be assigned to columns reliably, and they were NOT extracted. Tentative reading for the reviewer to check in the PDF: Self-Esteem L -0.708, S 0.344, ED -0.076, PU -0.129. Neuroticism possibly L 0.483, S -0.199, with ED/PU blank. Attachment-Anxiety possibly 0.396, -0.143, 0.073, 0.113. Extraversion possibly -0.349, 0.297, 0.109 (column of 0.109 unclear). If confirmed, these would be lagged correlations (pre-study trait vs week-4 ED/PU). Blank cells (non-significant) carry no extractable value. (2) Text p.6 gives problematic-use baseline β=0.10 alongside b=0.73. Table S11 shows β…
Заметка ИИ: One sample, two week-4 Spearman effects (loneliness with ADS-9 craving and with PCUS). Other correlations with eligible constructs exist only in the sparse heatmap (Table S17). They were not extracted because the cell positions are ambiguous; see consistency_notes. Neither AI-dependence measure has reliability reported.

### ST019-1 · CloudResearch US adults, 4-week ChatGPT RCT (n=981)
Отчёты: R0724 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | SIRVENT · total (T3) | **loneliness** · UCLA Loneliness Scale, 8-item (ULS-8) | spearman | **0.105** | **981** | 4 | Table S17, p. 70 (S39) | «Final Loneliness / 1.0 / -0.472 / 0.105 / 0.185 (column: Final Emotional Dependence)» |
| E2 | PCUS · total (T1) | **loneliness** · UCLA Loneliness Scale, 8-item (ULS-8) | spearman | **0.185** | **981** | 4 | Table S17, p. 70 (S39) | «Final Loneliness / 1.0 / -0.472 / 0.105 / 0.185 (column: Final Problematic Use)» |

- E1: заметка: Both measures from the week-4 (final) weekly survey. Same-occasion correlations are not reported for earlier waves. Spearman, BH-corrected matrix. n assumed to be the full analysed sample (not stated for the matrix). Values appear in heatmap cells; the 4x4 outcome block is complete, so the cell pos…
- E2: заметка: Both measures from the week-4 (final) weekly survey. Same-occasion correlations are not reported for earlier waves. Spearman, BH-corrected matrix. n assumed to be 981 (not stated for the matrix).

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2: поздняя волна: в основной анализ не идёт, только в описание

**Ключевые поля выборки:**
- **n_analysed: 981** — p. 37 (S6) — «The final set of participants consists of 981 people»
- **population: general_adults** — p. 36 (S5) — «All participants met the inclusion criteria of being over 18 years of age and fluent in English.»
- **sampling: quota or online panel** — p. 33 (S2) — «Participants were recruited on CloudResearch and were compensated $100 for completing the full study.»
- **ai_system: general_chatbot** — p. 34 (S3) — «Participants in the study were asked to interact with OpenAI's ChatGPT (GPT-4o) for at least five minutes each day for 28 days»

**Остальные поля:**
- country: USA — p. 36 (S5), Participants and Recruitment — «recruited from CloudResearch, an established online platform that provides access to a diverse participant pool from across the United States»
- data_years: 2024 — p. 15, footnote 1 — «the study began after the announcement of the 2024 U.S. presidential election result in November and concluded around the end of the year.»
- design: other — p. 34 (S3), Study Design — «We employed a 3 x 3 factorial design ... Participants were randomly assigned to one of nine experimental conditions»
- clinical_group: NA — NA — «NA»
- age_mean: 39.9 — p. 37 (S6) — «981 people with a mean age of 39.9 (SD=11.6)»
- age_sd: 11.6 — p. 37 (S6) — «981 people with a mean age of 39.9 (SD=11.6)»
- age_min: NR (inclusion criterion: over 18; youngest category 18-25) — p. 36 (S5); Table S19 — «being over 18 years of age ... 18-25 9.5 93»
- age_max: NR (oldest category 56+) — Table S19, p. 72 — «56+ 11.4 112»
- pct_female: 51.8 — p. 37 (S6); Table S19 — «an almost equal split of male and female (Female: 51.8%, Male: 48.2%)»
- mode: online — p. 35 (S4) — «All survey responses were captured via Qualtrics.»
- attention_checks: yes — p. 37 (S6), Outlier Definition and Exclusion Criteria — «those who completed the daily survey with minimal or no interaction with the chatbot ... were excluded. Additionally, observations were excluded if participant…»
- pub_status: preprint — p. 1 — «Posted Date: April 27th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-8148142/v1»
- language: English — whole text — «How AI and Human Behaviors Shape Psychosocial Effects of Extended Chatbot Use»
- funding_coi: Funded by OpenAI; four authors (Phang, Lampe, Ahmad, Agarwal) are OpenAI employees. — p. 30, Acknowledgments — «Funding: This research was funded by OpenAI. ... Competing interests: These authors are employees of OpenAI: J.P., M.L., L.A., S.A.»
- notes: Four-week RCT (3 modality x 3 task) with weekly surveys. Emotional dependence = ADS-9 craving subscale adapted to chatbot; problematic use = PCUS; both scored as item means (1-5) and first measured at the week-1 survey. The only zero-order correlations involving AI dependence and an eligible correlate are Spearman rhos at week 4 (Table S17, BH-corrected; only significant cells shown). Exclusion rules concern compliance (task completion, number of messages, survey timeliness, modality adherence); there were no attention-check items. Reliability is not reported for any scale.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online crowdsourcing panel (CloudResearch). — p. 33 (S2) — «Participants were recruited on CloudResearch»
2. отклик: **no** — 981 of 2,539 enrolled completed the study (about 39%). Completers were not compared with non-completers. — p. 37 (S6) — «A total of 2,539 participants were enrolled in the study, and 981 saw to the completion of the study.»
3. валидная шкала зависимости от ИИ: **yes** — The ADS-9 craving subscale (Sirvent-Ruiz et al., 2022) and the PCUS (Yu et al., 2024) both have published validation studies. The ADS craving subscale was adapted to refer to a chatbot, and the adapted version was not r… — p. 38 (S7) — «Evaluated using the "craving" subscale of the 9-item Affective Dependence Scale (ADS-9) (28), adapted to refer to a chatbot ... Measured using the Problematic …»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega is reported for either AI-dependence measure in this sample. — p. 37-38 (S6-S7), Main Outcome Measures — «Four key outcomes were measured weekly using validated scales.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (loneliness) was measured with the published ULS-8. — p. 37 (S6) — «Loneliness: Measured using the 8-item UCLA Loneliness Scale (ULS-8) (60)»
6. качество данных: **yes** — Stated exclusion rules for invalid or non-compliant observations. These concern compliance only; there were no attention-check items. — p. 37 (S6) — «Observations were excluded if any of the following criteria were met: participants who failed to complete the daily task consecutively for three days within an…»

Правки:
- 

Проверено: да

---

## ST020 · Flores 2026 · International Journal of Research and Innovation in Social Science

Основной отчёт R0770: [текст](../../fulltext/text/R0770.txt) · [PDF](../../fulltext/pdf/R0770.pdf) — «AI Dependence and Academic Motivation as Predictors of Academic Self-Efficacy Among Undergraduate Students» — [DOI](https://doi.org/10.47772/ijriss.2026.100801062)
Расхождения в тексте: The text, the abstract and Table 3 agree on AIDQ-GASE r = -.220. The AIDQ-academic motivation correlation (r = -.143, p = .031, Page 8 text) was not extracted because academic motivation (AMS-C 28 SDI) does not fit any key in the construct dictionary. Some reported values look implausible: the SDI mean is M = 3.5, SD = 0.401, even though the SDI ranges from -18 to +18 (an SD of 0.401 is very small for that range), and data were collected in July-August 2026 for the academic year 2026-2027. The regression betas were not extracted because they are multivariable.
Заметка ИИ: There is one eligible effect: AIDQ total with academic self-efficacy (GASE). No reliability coefficients are reported for any instrument.

### ST020-1 · Undergraduates, three private universities, Cebu, Philippines (n = 228)
Отчёты: R0770 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AIDQ · total (T2) | **self_efficacy** · General Academic Self-Efficacy Scale (GASE; van Zyl et al.,… | pearson | **-0.220** | **228** | 1 | Page 8, Table 3 | «AI Dependence / -0.220 / <.001 / Significant» |

- E1: заметка: The text and the abstract both report r = -.220, p < .001. The n is taken from Table 1 and the regression df F(2, 225).

**Ключевые поля выборки:**
- **n_analysed: 228** — Page 7, Table 1; Page 8, Table 4 — «N = 228»
- **population: university_students** — Page 5, Methods, Participants — «The sample consisted of 228 undergraduate students enrolled in three private universities»
- **sampling: quota or online panel** — Pages 5-6, Methods, Participants — «selected through non-probability quota sampling based on the proportional representation of students from each university»
- **ai_system: ai_unspecified** — Page 6, Methods, Instruments — «a 12-item self-report inventory that measures excessive use and overreliance on AI tools, specifically among undergraduate students»

**Остальные поля:**
- country: PHL — Page 5, Methods, Participants — «The sample consisted of 228 undergraduate students enrolled in three private universities in Cebu, Philippines»
- data_years: 2026 — Page 6, Methods, Instruments — «The data collection lasted four weeks, from July to August 2026.»
- design: cross-sectional — Page 5, Methods, Research Design — «This study employed a cross-sectional quantitative design»
- clinical_group: NA — NA — «NA»
- age_mean: 21.46 — Page 6, Methods, Participants — «Participants ranged in age from 19 to 24 years old (M = 21.46, SD = 1.60).»
- age_sd: 1.60 — Page 6, Methods, Participants — «Participants ranged in age from 19 to 24 years old (M = 21.46, SD = 1.60).»
- age_min: 19 — Page 6, Methods, Participants — «Participants ranged in age from 19 to 24 years old»
- age_max: 24 — Page 6, Methods, Participants — «Participants ranged in age from 19 to 24 years old»
- pct_female: 64.5 — Page 7, Table 1 — «Female | 147 | 64.5%»
- mode: online — Page 6, Methods, Instruments — «Data were collected electronically using three standardized self-report questionnaires ... Clear and comprehensive instructions were provided within the online…»
- attention_checks: NR — Page 6, Methods — «Data were collected electronically using three standardized self-report questionnaires»
- pub_status: journal — Page 1, header — «INTERNATIONAL JOURNAL OF RESEARCH AND INNOVATION IN SOCIAL SCIENCE (IJRISS)»
- language: English — Full text — «AI Dependence and Academic Motivation as Predictors of Academic Self-Efficacy Among Undergraduate Students»
- funding_coi: Funding NR; authors declare no conflict of interest — Page 6, Conflict of interest — «The author declares no conflict of interest.»
- notes: AIDQ: 12 items, 4-point Likert scale; M = 2.5, SD = 0.601. GASE: 5 items; M = 3.8, SD = 0.646. No reliability coefficients are reported for any scale.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability quota sampling at three private universities — Pages 5-6, Methods, Participants — «selected through non-probability quota sampling based on the proportional representation of students from each university»
2. отклик: **unclear** — Response rate not reported — Pages 5-6, Methods — «The sample consisted of 228 undergraduate students»
3. валидная шкала зависимости от ИИ: **yes** — AIDQ comes from a published development and validation study (Akinwale et al., 2025) — Page 6, Instruments; Page 11, Ref. 5 — «Akinwale, G.A., Ojakorotu, V., & Oloko, T.O. (2025). Developing and validating an artificial intelligence dependence questionnaire (AIDQ) for undergraduate stu…»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega reported for the AIDQ in this sample — Page 6, Instruments — «a 12-item self-report inventory that measures excessive use and overreliance on AI tools ... It is rated using a 4-point Likert scale.»
5. валидные шкалы коррелятов: **yes** — The extracted correlate (academic self-efficacy) was measured with the published GASE (van Zyl et al., 2022) — Page 6, Instruments — «The third instrument was the General Academic Self-Efficacy Scale (GASE) by van Zyl et al. (2022), a five-item self-report instrument»
6. качество данных: **unclear** — No data-quality screening reported — Page 6, Methods — «Data were collected electronically using three standardized self-report questionnaires»

Правки:
- 

Проверено: да

