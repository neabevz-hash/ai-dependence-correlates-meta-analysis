# Проверка выписывания — файл 8 из 13

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

## ST071 · Wang 2026 · BMC psychology

Основной отчёт R2658: [текст](../../fulltext/text/R2658.txt) — «When cognitive offloading becomes dependence: how AI dependence mediates the pathway from academic stress to burnout and anxiety.» — [DOI](https://doi.org/10.1186/s40359-026-04911-w)
Расхождения в тексте: The correlations in the text (r = 0.26 academic stress, -0.16 self-efficacy, 0.32 anxiety, 0.34 burnout with AI dependence) match Table 1. The text has typos in its p-values ('p < 0 0.001'). In Table 4, the F value for the first anxiety model (734.61) has no significance stars, unlike the matching F in Table 2; the text reports it as significant. The text lists the hypotheses twice. Table 1 does not state its n, and the gender counts (751 + 872 = 1623) match the valid sample.
Заметка ИИ: I extracted one sample with three correlations involving the DAI total score: academic stress, self-efficacy and anxiety. Academic burnout was left out because it is not in the construct dictionary. Funding, COI and data-collection years are not reported in the supplied text.

### ST071-1 · Undergraduate students, universities in China, online survey (n = 1,623)
Отчёты: R2658 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **academic_stress** · Stress Scale for College Students, academic stress subscale… | pearson | **0.26** | **1623** | 1 | Table 1 | «1. Academic stress / 2.16 / 0.56 / - / 0.26*** / -0.34*** / 0.59*** / 0.56***» |
| E2 | DAI · total (T4) | **self_efficacy** · General Self-Efficacy Scale (GSES) | pearson | **-0.16** | **1623** | 1 | Table 1 | «2. AI dependence / 2.98 / 0.74 / - / - / -0.16*** / 0.34*** / 0.32***» |
| E3 | DAI · total (T4) | **anxiety** · GAD-7 | pearson | **0.32** | **1623** | 1 | Table 1 | «2. AI dependence / 2.98 / 0.74 / - / - / -0.16*** / 0.34*** / 0.32***» |

- E1: α ИИ 0.76, α коррелята 0.91; заметка: Table n not stated; full valid sample assumed. Text gives the same value (r = 0.26, p < 0.001).
- E2: α ИИ 0.76, α коррелята 0.93; заметка: Table n not stated; full valid sample assumed.
- E3: α ИИ 0.76, α коррелята 0.92; заметка: Table n not stated; full valid sample assumed. GAD-7 scored 1-4 in this study rather than the usual 0-3.

**Ключевые поля выборки:**
- **n_analysed: 1623** — Method, Participants and procedure — «After the process, the total number of valid samples was 1623.»
- **population: university_students** — Method, Participants and procedure — «Participants were undergraduate students recruited from universities in China»
- **sampling: convenience** — Method, Participants and procedure — «A convenience voluntary online sampling approach was adopted, and the questionnaire was distributed through social media platforms and university networks.»
- **ai_system: ai_unspecified** — Abstract; Measures, AI dependence — «generative AI tools are increasingly used in college students' academic activities ... The DAI scale ... was employed to measure individuals' dependence on artificial intelligence.»

**Остальные поля:**
- country: CHN — Method, Participants and procedure — «Participants were undergraduate students recruited from universities in China through an online survey platform.»
- data_years: NR — NA — «NR»
- design: cross-sectional — Strengths and limitations — «First, the cross-sectional design limits the ability to draw causal inferences»
- clinical_group: NA — NA — «NA»
- age_mean: 19.47 — Method, Participants and procedure — «The average age of the sample was 19.47 years (SD = 1.08).»
- age_sd: 1.08 — Method, Participants and procedure — «The average age of the sample was 19.47 years (SD = 1.08).»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 53.73 — Method, Participants and procedure — «46.27% were male (751), and 53.73% were female (872).»
- mode: online — Abstract — «A total of 1,623 college students completed an online survey»
- attention_checks: yes — Method, Participants and procedure — «Responses were excluded if participants failed the fixed-answer items (questions with obvious answers to detect casual respondents) or spent less than 2 min or…»
- pub_status: journal — Report metadata — «venue: BMC psychology; DOI: 10.1186/s40359-026-04911-w»
- language: English — Full text — «When cognitive offloading becomes dependence: how AI dependence mediates the pathway from academic stress to burnout and anxiety»
- funding_coi: NR (no funding or competing-interest statement in the supplied text) — NA — «NR»
- notes: I coded the AI system as ai_unspecified: the paper frames the study around generative AI (it names ChatGPT, Gemini and DeepSeek in the Introduction), but the DAI items refer only to 'AI', and the paper never says which tools the participants used. A reviewer may prefer general_chatbot. The Academic Burnout Scale (Lian et al.) correlations (r = 0.34 with AI dependence) are not extracted because burnout has no key in the construct dictionary (it is explicitly excluded under depression). The n in Table 1 is not stated; I assumed the full valid sample of 1623.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience voluntary online sampling via social media and university networks. — Method, Participants and procedure — «A convenience voluntary online sampling approach was adopted»
2. отклик: **unclear** — No response rate or number invited/excluded reported; only the valid n is given. — Method, Participants and procedure — «After the process, the total number of valid samples was 1623.»
3. валидная шкала зависимости от ИИ: **yes** — DAI scale with a published development study (Morales-García et al., ref [24]). — Measures, AI dependence — «The DAI scale, developed by [24], was employed to measure individuals' dependence on artificial intelligence.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.76 in this sample. — Measures, AI dependence — «In this study, the Cronbach's α coefficient of this scale was 0.76.»
5. валидные шкалы коррелятов: **yes** — Extracted correlates measured with published instruments: academic stress subscale of the Stress Scale for College Students [17], GSES, GAD-7. — Measures — «This study used the subscale of academic stress from the Stress Scale for College Students [17]... The General Self-Efficacy Scale (GSES)... The scale of Gener…»
6. качество данных: **yes** — Fixed-answer attention items and completion-time rule used to exclude invalid responses. — Method, Participants and procedure — «Responses were excluded if participants failed the fixed-answer items (questions with obvious answers to detect casual respondents) or spent less than 2 min or…»

Правки:
- 

Проверено: да

---

## ST072 · Wu 2026 · Australian journal of psychology

Основной отчёт R2703: [текст](../../fulltext/text/R2703.txt) — «The serial mediating roles of AI self-efficacy and academic procrastination in the association between AI literacy and AI dependence among Chinese undergraduat…» — [DOI](https://doi.org/10.1080/00049530.2026.2721637)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R4336 (ST111): Both Chinese undergraduates at one normal or comprehensive university in Southwest China with the AIDep-22; R2703 has N = 417 (70.3% female, M = 21.21), R4336 Sample 1 has N = 400 (70.2% female)
Не выписано ИИ: A 30-student pilot sample (outside the analytic sample) was used to check the translations. It is not extracted because it has no reported data.
Расхождения в тексте: The AI dependence–academic procrastination correlation is .47 in Table 4 and .475 in the text; the table value was used. The text likewise gives three decimals for the other correlations (.542, −.309, −.283, −.420, −.361), while the table gives two (.54, −.31, −.28, −.42, −.36). Seniors are 28.8% in the text and 28.7% in Table 1. Correlations of AI dependence with AI literacy (−.28) and with AI self-efficacy (−.36) were not extracted: AI literacy has no key in the construct dictionary, and AI self-efficacy is excluded as an AI-specific cognition. No correlations were reported for the AIDep-22 subscales. Only the global score was analysed.
Заметка ИИ: There is one eligible sample with one effect: AIDep-22 total × APS-S academic procrastination. Funding and COI statements are not in the supplied text.

### ST072-1 · Normal university, Southwest China, undergraduates, N = 417
Отчёты: R2703 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AIDEP22 · total (T4) | **procrastination** · Academic Procrastination Scale-Short Form (APS-S) | pearson | **.47** | **417** | 1 | Table 4 | «4. AI dependence / 2.89 / 0.70 / .93 / −.28*** / −.36*** / .47*** / 1» |

- E1: α ИИ .93, α коррелята .84; заметка: The table gives two decimals; the text reports r = .475. Table value used.

**Ключевые поля выборки:**
- **n_analysed: 417** — Table 4 — «Table 4.Descriptive statistics and correlations (N = 417).»
- **population: university_students** — Methods, Recruitment — «Eligibility criteria required participants to be enrolled undergraduates aged 18–24 years»
- **sampling: probability** — Methods, Recruitment — «stratified random sampling was conducted by gender and major category... Within each stratum, students were selected using computer-generated random numbers and invited to participate.»
- **ai_system: ai_unspecified** — Measures, AI dependence; Abstract — «assess maladaptive reliance on AI in academic contexts... reducing procrastination-related reliance on AI tools»

**Остальные поля:**
- country: CHN — Methods, Recruitment — «Participants were recruited from a normal university in Southwest China.»
- data_years: NR — Methods, Recruitment — «Its 2025 to 2026 Office of Academic Affairs enrolment register formed the sampling frame.»
- design: cross-sectional — Methods, Recruitment — «A cross-sectional survey design was used.»
- clinical_group: NA — NA — «NA»
- age_mean: 21.21 — Results, Demographic characteristics — «a total of 417 students aged 18–24 years participated in the study (M = 21.21, SD = 1.48)»
- age_sd: 1.48 — Results, Demographic characteristics — «(M = 21.21, SD = 1.48)»
- age_min: 18 — Results, Demographic characteristics — «a total of 417 students aged 18–24 years participated»
- age_max: 24 — Results, Demographic characteristics — «a total of 417 students aged 18–24 years participated»
- pct_female: 70.3 — Results, Demographic characteristics; Table 1 — «124 were male (29.7%) and 293 were female (70.3%)»
- mode: online — Methods, Recruitment — «The survey was administered online in simplified Chinese.»
- attention_checks: yes — Methods, Recruitment — «eight showed repeated or patterned responses and five failed attention or consistency checks»
- pub_status: journal — Job header — «Year: 2026; venue: Australian journal of psychology; DOI: 10.1080/00049530.2026.2721637»
- language: English — Full text — «The serial mediating roles of AI self-efficacy and academic procrastination in the association between AI literacy and AI dependence among Chinese undergraduat…»
- funding_coi: NR — Full text — «No funding or conflict-of-interest statement appears in the supplied text.»
- notes: Possible overlap with R4336 (ST111). Both studies used Chinese undergraduates at one normal or comprehensive university in Southwest China with the AIDep-22. R2703 has N = 417 (70.3% female, M = 21.21); R4336 Sample 1 has N = 400 (70.2% female). Check for duplicate data. Data-collection year is not stated; the sampling frame was the 2025–2026 enrolment register. The AIDep-22 was given in its original Chinese form.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **yes** — Proportional stratified random sample drawn from the university enrolment register. — Methods, Recruitment — «stratified random sampling was conducted by gender and major category... students were selected using computer-generated random numbers»
2. отклик: **yes** — Effective response rate 92.67% (417 of 450 invited). — Methods, Recruitment — «417 valid responses were retained, yielding an effective response rate of 92.67%»
3. валидная шкала зависимости от ИИ: **yes** — AIDep-22 is a published instrument developed and validated with Chinese undergraduates (Wu et al., 2026). — Measures, AI dependence — «AI Dependence Scale for Chinese Undergraduates (AIDep-22) developed and validated with Chinese undergraduates by Wu et al. (2026)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .93 in this sample. — Measures, AI dependence; Table 4 — «In the present study, Cronbach's alpha was .93.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (academic procrastination) was measured with the published APS-S (Yockey, 2016). — Measures, Academic procrastination — «Academic Procrastination Scale-Short Form (APS-S) validated by Yockey (2016)»
6. качество данных: **yes** — Incomplete, patterned and attention-check-failing responses were excluded. — Methods, Recruitment — «Responses were excluded if they were incomplete, showed repeated or patterned answers or contained clear inconsistencies across attention-check items.»

Правки:
- 

Проверено: да

---

## ST073 · Yang 2026 · Frontiers in Public Health

Основной отчёт R2758: [текст](../../fulltext/text/R2758.txt) · [PDF](../../fulltext/pdf/R2758.pdf) — «Anxiety, emotional abuse, and physical activity as correlates of AI-related affective dependence among adolescents: mediation, moderation, and network analyses» — [DOI](https://doi.org/10.3389/fpubh.2026.1956596)
Не выписано ИИ: Supplementary discriminant-validity subsample (n = 1,676) from the same school survey: this is the same recruited sample, not a separate one. It reports only the correlation between AI dependence and short-form video addiction (r = 0.219), which is not in the construct dictionary, so it was not extracted.
Расхождения в тексте: Zero-order correlations appear only in the text (section 3.2). Figure 2 is a correlation heatmap whose cell values are not given in the text, so nothing was extracted from it. The composite reliability for the AI-dependence scale (0.890) is lower than its Cronbach's alpha (0.946). This is unusual but not a direct contradiction. The paper says 1,589 is 93.2% of the 1,705 respondents, and 1589/1705 = 93.2%, so the figures agree. Text r values for other pairs (not extracted): EA–AI dependence 0.214, EA–anxiety 0.387, EA–PA −0.136, anxiety–PA −0.149, PA–AI dependence −0.044.
Заметка ИИ: One sample, one eligible effect: AI-related affective dependence with anxiety (GAD-2). Emotional abuse (CTQ-SF) and physical activity (PARS-3) are not dictionary constructs. Network partial correlations and the PROCESS betas are adjusted for covariates and were not extracted.

### ST073-1 · Chinese school students (six primary, middle and high schools, five provinces), CHN, n=1589
Отчёты: R2758 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | SIRVENT · total (T3) | **anxiety** · GAD-2 (Generalized Anxiety Disorder Scale, 2 items) | pearson | **0.166** | **1589** | 1 | Page 4, 3.2 Correlation analysis | «Anxiety was also positively correlated with AI dependence (r = 0.166, p < 0.001)» |

- E1: α ИИ 0.946, α коррелята 0.862; заметка: Value reported in the text only; Figure 2 is a correlation heatmap. Network partial r (0.087) and mediation betas are covariate-adjusted and were not extracted.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.22 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 1589** — Page 3, 2.1 Participants — «Of the 1,705 respondents, 1,589 had eligible data for all focal variables and covariates required for the primary analyses and therefore constituted the main analytical sample (93.2%)»
- **population: adolescents** — Page 3, 2.1 Participants — «with a mean age of 14.62 ± 1.65 years. There were 225 elementary school students (14.2%), 933 junior high school students (58.7%), and 431 senior high school students (27.1%)»
- **sampling: convenience** — Page 9, Limitations — «although participants were recruited from multiple schools, the convenience sampling strategy limits generalizability»
- **ai_system: general_chatbot** — Page 2, Background; Page 3, 2.2.3 — «Generative artificial intelligence (AI), including ChatGPT, Kimi, Siri, Copilot, and Doubao ... adolescents' psychological concern, emotional needs, and reliance on generative AI»

**Остальные поля:**
- country: CHN — Page 2, 2.1 Participants — «six primary, middle, and high schools in Hunan, Sichuan, Shaanxi, Shanxi, and Anhui provinces, China»
- data_years: 2025 — Page 2, 2.1 Participants — «Data were collected in November 2025 from 1,705 students»
- design: cross-sectional — Page 1, Abstract — «this cross-sectional study examined the associations among emotional abuse (EA), anxiety, physical activity (PA), and AI-related affective dependence»
- clinical_group: NA — NA — «NA»
- age_mean: 14.62 — Page 3, 2.1 Participants — «with a mean age of 14.62 ± 1.65 years»
- age_sd: 1.65 — Page 3, 2.1 Participants — «with a mean age of 14.62 ± 1.65 years»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 51.9 — Page 3, 2.1 Participants — «The sample included 765 boys (48.1%) and 824 girls (51.9%)»
- mode: paper — Page 3, 2.1 Participants — «With assistance from homeroom teachers, students completed paper questionnaires in their classrooms.»
- attention_checks: NR — Page 3, 2.1 Participants — «1,589 had eligible data for all focal variables and covariates required for the primary analyses»
- pub_status: journal — Page 1 — «TYPE Original Research PUBLISHED 06 October 2026 DOI 10.3389/fpubh.2026.1956596»
- language: English — Full text — «Anxiety, emotional abuse, and physical activity as correlates of AI-related affective dependence among adolescents»
- funding_coi: No funding received; authors declare no conflict of interest. — Page 9, Funding; Conflict of interest — «The author(s) declared that financial support was not received for this work and/or its publication. ... conducted in the absence of any commercial or financia…»
- notes: Exclusion from 1,705 to 1,589 was based on missing/ineligible data for focal variables and covariates, not on stated careless-responding screening. The AI-dependence scale is a 5-item adaptation of the craving dimension of Sirvent-Ruiz et al. (2022) Emotional Dependence Scale. Zero-order correlations are reported only in the text (section 3.2); Figure 2 is a heatmap. Emotional abuse (CTQ-SF) and physical activity (PARS-3) correlates are not in the construct dictionary and were not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample of students from six schools. — Page 9, Limitations — «the convenience sampling strategy limits generalizability»
2. отклик: **unclear** — Number invited/response rate not reported; 93.2% is the share of the 1,705 respondents with complete data, not a response rate. — Page 3, 2.1 Participants — «Of the 1,705 respondents, 1,589 had eligible data for all focal variables and covariates ... (93.2%)»
3. валидная шкала зависимости от ИИ: **yes** — Adapted from a published validated scale (Sirvent-Ruiz et al., 2022); content validity, EFA/CFA and discriminant validity of the adaptation are reported in this report (described as preliminary). — Page 3, 2.2.3 — «The item-level content validity index (I-CVI) ranged from 0.80 to 1.00 ... Exploratory and confirmatory factor analyses supported a one-factor structure.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.946 in the analytical sample. — Page 3, 2.2.3 — «In the formal analytical sample, the five-item scale demonstrated excellent internal consistency (Cronbach's α = 0.946).»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (anxiety) was measured with the published GAD-2. — Page 3, 2.2.2 — «Anxiety was measured with the two-item Generalized Anxiety Disorder Scale (GAD-2) (33).»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported; exclusions were based only on missing/ineligible data. — Page 3, 2.1 Participants — «1,589 had eligible data for all focal variables and covariates required for the primary analyses»

Правки:
- 

Проверено: да

---

## ST074 · Yao 2026 · Scientific Reports

Основной отчёт R2781: [текст](../../fulltext/text/R2781.txt) · [PDF](../../fulltext/pdf/R2781.pdf) — «Psychological pathways linking generative AI dependency to psychological capital depletion among Chinese international students» — [DOI](https://doi.org/10.1038/s41598-026-68047-y)
Лонгитюд (для описания): This is a three-wave design. GAD was measured at T1 (June 2025), PSD and reduced self-efficacy (rSE) at T2 (September 2025), and reduced psychological capital at T3 (January 2026). Each construct was measured only once, so there are no autoregressive or cross-lagged paths. The study used a serial mediation SEM (standardised paths, Figure 3): GAD(T1)→rPsyCap(T3) a: γ = 0.19; GAD→PSD b: γ = 0.40; PSD→rSE c: γ = 0.32; rSE→rPsyCap d: γ = 0.16; GAD(T1)→rSE(T2) e: γ = 0.23; PSD→rPsyCap f: γ = 0.23 (all p < .01). The indirect effects in Table 5 were bcd = 0.019, bf = 0.087 and ed = 0.034; the direct effect was 0.163 and the total effect 0.302. The paper does not say which waves each zero-order correlation in Table 4 uses; the model figure suggests they are cross-wave.
Расхождения в тексте: (1) The measurement model fit in Table 2 (χ² = 927.795, df = 623) differs from the measurement model reported in the common-method-bias section (χ² = 1063.098, df = 659). (2) The single-factor CFA df = 665 and Bartlett df = 780 imply 38 and 40 items, but the paper states 37 items. (3) The abstract and Table 5 give the direct effect as 0.163, while Figure 3 / Section 3.5 give path a as γ = 0.19. These are probably different estimates (Table 5 bootstrap vs standardised), but this is not explained. (4) GAD is described as a 9-item adaptation, whereas the original Goh et al. scale has 11 items in 3 subscales; only a single-factor total is reported. (5) Table 4 does not state which wave each variable comes from; the timing is inferred from Figures 1 and 3.
Заметка ИИ: I extracted one effect: GAD total with reduced self-efficacy, r = .345, n = 502. Two points need the reviewer's decision. First, eligibility: this is a reverse-worded, AI-context adaptation of a self-efficacy scale. Second, the wave: GAD comes from T1 and rSE from T2. No figure-only coefficients were left out.

### ST074-1 · Chinese international students studying abroad (USA, GBR, AUS, CAN, KOR, other), 3-wave panel, n=502
Отчёты: R2781 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **self_efficacy** · Reduced self-efficacy (rSE), 10 items adapted from Pintrich… | pearson | **.345** | **502** | lagged: T1-T2 | Page 12, Table 4 | «3.rSE / .345** / .396** / 0.788669 / 4.53 / 1.409» |

- E1: **направление: reversed (higher = reduced self-efficacy when generative AI support is absent)**; α ИИ .957, α коррелята .942; заметка: GAD measured at T1, rSE at T2 (Fig. 1); no same-occasion correlation reported. Reviewer should confirm eligibility: rSE is an AI-context adaptation (confidence decrease without GenAI support), not a standard academic self-efficacy scale. Computed in SPSS (observed correlation).

**⚠ Проверка скриптом (обратите внимание):**
- E1: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление
- E1: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: 502** — Page 10, 2.4 Data Analysis — «The final analytic sample consisted of 502 participants with complete and successfully matched data.»
- **population: university_students** — Page 8, 2.2.2 — «all from Chinese international students enrolled in higher education (inclusion criterion: age ≥ 18 years).»
- **sampling: convenience** — Page 8, 2.2 Participants — «A combination of convenience sampling and snowball sampling was employed.»
- **ai_system: general_chatbot** — Page 8, 2.2; Page 9, Table 1 — «Chinese international students who use generative AI for academic writing ... Types of generative AI tools: China-based generative AI 162 32.3; International generative AI 340 67.7»

**Остальные поля:**
- country: MULTI: USA, GBR, AUS, CAN, KOR, other (25.5% 'Other' host countries not named) — Page 8, 2.2 Participants; Table 1 — «Chinese international students studying in the United States, the United Kingdom, Australia, Canada, South Korea, and other countries.»
- data_years: 2025-2026 — Page 7, 2.1 Research Procedure — «T1 on June 22, 2025; T2 on September 21, 2025; and T3 on January 23, 2026.»
- design: panel — Page 2, Abstract; Page 7 — «A three-wave longitudinal study was conducted.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 8, Table 1 — «18-22 years old 151 30.1 ... 23-25 years old 208 41.4 ... 26-29 years old 116 23.1 ... 30 and above 27 5.4»
- age_sd: NR — Page 8, Table 1 — «Age reported only in bands»
- age_min: 18 — Page 8, 2.2.2; Table 1 — «(inclusion criterion: age ≥ 18 years)»
- age_max: NR — Page 9, Table 1 — «30 and above 27 5.4»
- pct_female: 54.8 — Page 8, 2.2.2 — «The sample comprised 227 men (45.2%) and 275 women (54.8%).»
- mode: mixed — Page 8, 2.2 Participants — «The questionnaire was distributed both online (via Wenjuanxing and WeChat) and offline (on university campuses).»
- attention_checks: NR — Page 10, 2.4 Data Analysis — «Questionnaires with incomplete item responses or anonymous identification codes that could not be matched across all three survey waves were excluded.»
- pub_status: journal — Page 1 — «Article in Press ... Scientific Reports ... Accepted: 19 August 2026»
- language: English — Whole text — «Psychological pathways linking generative AI dependency to psychological capital depletion among Chinese international students»
- funding_coi: Funded by China Adult Education Association (Grant No. 2025-0742Y); funders had no role; authors declare no conflict of interest. — Page 2, Funding Information; Conflict of Interest — «This study was funded by China Adult Education Association, (Grant No.2025-0742Y). ... The authors declare that they have no conflict of interest.»
- notes: GAD scale is a 9-item contextual adaptation of Goh et al. (2025) GAIDS (original 11 items, 3 subscales); scored as a single first-order factor (only total). Measurement: GAD at T1, PSD and rSE at T2, rPsyCap at T3 (Fig. 1). Only exclusion rule is incomplete/unmatched responses; no attention checks. AI system: generic 'generative AI' (China-based or international) used for academic writing; coded general_chatbot, reviewer may prefer task_assistant. Correlates not in dictionary (not extracted): perceived skill degradation (ECog-adapted) and reduced psychological capital (PCQ-24-adapted).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience and snowball sampling, partly via Wenjuanxing/WeChat. — Page 8, 2.2 Participants — «A combination of convenience sampling and snowball sampling was employed.»
2. отклик: **unclear** — Number invited, T1 respondents and attrition across waves not reported; only the final 502 matched cases are given. — Page 10, 2.4 — «The final analytic sample consisted of 502 participants with complete and successfully matched data.»
3. валидная шкала зависимости от ИИ: **yes** — Based on the published GAIDS (Goh et al., 2025), adapted to 9 items; EFA/CFA in this report support it (CR .961, AVE .710). Note the adaptation. — Page 9, 2.3 Measurements; Page 11, Table 3 — «Based on the theoretical framework of Generative AI dependency proposed by Goh et al. (2025), ... the scale was contextually adapted to comprise 9 items. Cronb…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .957 in this sample. — Page 9, 2.3; Table 2 — «Cronbach’s α was .957.»
5. валидные шкалы коррелятов: **unclear** — The only extracted correlate (reduced self-efficacy) is a substantially reworded adaptation (reverse/attenuated, AI-absence context) of the Pintrich & De Groot self-efficacy scale; it has psychometric support only from … — Page 9, 2.3 Measurements — «Drawing on the Self-Efficacy scale used by Pintrich and De Groot (1990), items were semantically revised ... Reverse/attenuated wording was adopted to reflect …»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported; the only rule was excluding incomplete or unmatched questionnaires (missing-data rule). — Page 10, 2.4 Data Analysis — «Questionnaires with incomplete item responses or anonymous identification codes that could not be matched across all three survey waves were excluded.»

Правки:
- 

Проверено: да

---

## ST075 · Yao 2026 · AHFE international

Основной отчёт R2782: [текст](../../fulltext/text/R2782.txt) · [PDF](../../fulltext/pdf/R2782.pdf) — «When Creativity Encounters Algorithms: Personality Traits as Predictors of Design Students’ Adoption and Dependence on AI-Assisted Design» — [DOI](https://doi.org/10.54941/ahfe1007634)
Расхождения в тексте: (1) DAI has 5 items (Morales-García et al., 2024), but Table 1 lists only 4 DEP items, all labelled 'DEP1'. In fact every construct's items are labelled '...1'. (2) The Table 3 diagonals do not match sqrt(AVE). DEP is 0.812, but sqrt(0.700) = 0.837. NEU is 0.837, but sqrt(0.722) = 0.850. The diagonal entries may be misplaced. (3) Table 1 reports CR = 1.062 for Agreeableness, which is impossible. (4) The text says path results are in 'Table 5', but they are in Table 4. (5) In Table 4, EXT→ATT (p = .013) and OPE→ATT (p = .029) are significant but negative. They are labelled 'Unsupport', and the text says these relationships were 'not supported'. The abstract says extraversion and openness 'negatively predict' attitude. (6) In Table 5, the indirect effect is 0.188, but the 95% CI is 0.063–0.168, which does not contain the point estimate.
Заметка ИИ: Only latent (Fornell-Larcker) correlations are available; no observed Pearson correlations are reported. Age is reported only in categories (18–21, 22–25). The data-collection year is not reported.

### ST075-1 · Design students, China, snowball online survey (SoJump), n=345
Отчёты: R2782 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **extraversion** · Extraversion (EXT), 4 items adapted from Laouiti et al. (20… | latent | **−0.146** | **345** | 1 | Table 3 (Fornell-Larcker criterion), page 5 | «DEP 0.812 / EXT −0.146 0.788» |
| E2 | DAI · total (T4) | **agreeableness** · Agreeableness (AGR), 4 items adapted from Laouiti et al. (2… | latent | **0.051** | **345** | 1 | Table 3 (Fornell-Larcker criterion), page 5 | «AGR 0.051 −0.176 0.804» |
| E3 | DAI · total (T4) | **conscientiousness** · Conscientiousness (CON), 4 items adapted from Laouiti et al… | latent | **0.187** | **345** | 1 | Table 3 (Fornell-Larcker criterion), page 5 | «CON 0.187 −0.046 0.030 0.850» |
| E4 | DAI · total (T4) | **openness** · Openness (OPE), 4 items adapted from Laouiti et al. (2022) | latent | **−0.035** | **345** | 1 | Table 3 (Fornell-Larcker criterion), page 5 | «OPE −0.035 0.029 −0.159 −0.179 0.863» |
| E5 | DAI · total (T4) | **neuroticism** · Neuroticism (NEU), 4 items adapted from Laouiti et al. (202… | latent | **−0.213** | **345** | 1 | Table 3 (Fornell-Larcker criterion), page 5 | «NEU −0.213 0.064 −0.064 −0.146 −0.011 −0.241 −0.109 0.837» |

- E1: α ИИ 0.864, α коррелята 0.831; заметка: PLS-SEM latent variable correlation from the Fornell-Larcker table.
- E2: α ИИ 0.864, α коррелята 0.815; заметка: PLS-SEM latent variable correlation. Table 1 reports CR = 1.062 for AGR, which is impossible.
- E3: α ИИ 0.864, α коррелята 0.830; заметка: PLS-SEM latent variable correlation.
- E4: α ИИ 0.864, α коррелята 0.888; заметка: PLS-SEM latent variable correlation.
- E5: α ИИ 0.864, α коррелята 0.874; заметка: PLS-SEM latent variable correlation.

**Ключевые поля выборки:**
- **n_analysed: 345** — Page 4 — «A total of 345 valid responses were obtained.»
- **population: university_students** — Page 4; Table 2 — «targeting university students majoring in design-related disciplines»
- **sampling: snowball** — Page 4 — «This study employed a snowball sampling approach targeting university students majoring in design-related disciplines.»
- **ai_system: task_assistant** — Abstract; Page 1 — «AI-assisted design tools are increasingly integrated into design education»

**Остальные поля:**
- country: CHN — Page 8, Discussion (limitations) — «The sample of mainland Chinese design majors restricts cultural and disciplinary generalizability»
- data_years: NR — NR — «NR»
- design: cross-sectional — Page 8, Discussion (limitations) — «The cross-sectional design cannot capture changes in attitudes and dependence»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 2 — «Age 18–21 227 65.80 22–25 118 34.20»
- age_sd: NR — Table 2 — «Age 18–21 227 65.80 22–25 118 34.20»
- age_min: 18 (lower bound of age category) — Table 2 — «Age 18–21 227 65.80»
- age_max: 25 (upper bound of age category) — Table 2 — «22–25 118 34.20»
- pct_female: 60.87 — Table 2 — «Female 210 60.87»
- mode: online — Page 4 — «Data were collected via the online survey platform SoJump.»
- attention_checks: NR — Page 4 — «A total of 345 valid responses were obtained.»
- pub_status: conference — Page 1, header — «Human Factors in Communication of Design, Vol. 216, 2026, 160–170»
- language: English — Full text — «When Creativity Encounters Algorithms: Personality Traits as Predictors of Design Students’ Adoption and Dependence on AI-Assisted Design»
- funding_coi: NR (no funding or conflict-of-interest statement; acknowledgment thanks participants only) — Page 9, Acknowledgment — «We sincerely thank all participants for their valuable contributions to this study.»
- notes: AI system: generative AI (AIGC) design tools; the specific tools are not named. Analysis used PLS-SEM in SmartPLS 4.1. All correlations are latent-variable correlations from the Fornell-Larcker table. Undergraduates 81.16%, graduate students 18.84%.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Snowball sampling through an online survey platform (SoJump/Wenjuanxing). — Page 4 — «This study employed a snowball sampling approach targeting university students majoring in design-related disciplines. Data were collected via the online surve…»
2. отклик: **unclear** — No response rate reported; only the number of valid responses is given. — Page 4 — «A total of 345 valid responses were obtained.»
3. валидная шкала зависимости от ИИ: **yes** — AI dependence was measured with the Dependence on AI scale (Morales-García et al., 2024), which has a published validation study. Items were adapted, and Table 1 lists only 4 DEP items. — Table 1; References — «AI Dependence (DEP) (Morales-García et al., 2024) 0.864 0.921 0.700»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.864 in this sample. — Table 1 — «AI Dependence (DEP) (Morales-García et al., 2024) 0.864 0.921 0.700»
5. валидные шкалы коррелятов: **unclear** — The Big Five items were adapted from Laouiti et al. (2022), an applied entrepreneurship study rather than an instrument-validation study. The original Big Five instrument is not named. — Page 3; Table 1 — «All items were adapted from validated instruments in prior studies ... Extraversion (EXT) (Laouiti et al., 2022)»
6. качество данных: **unclear** — Responses are described as 'valid', but no attention checks or screening rule are described. — Page 4 — «A total of 345 valid responses were obtained.»

Правки:
- 

Проверено: да

---

## ST076 · Yauri 2026 · Proceedings of the LACCEI international multi-conference for engineering, educa…

Основной отчёт R2786: [текст](../../fulltext/text/R2786.txt) · [PDF](../../fulltext/pdf/R2786.pdf) — «Academic Self-Efficacy and Dependence on Artificial Intelligence in Peruvian Higher Education: The Mediating Effect of Performance Expectancy» — [DOI](https://doi.org/10.18687/laccei2026.1.1.1236)
Расхождения в тексте: The text and tables agree. The zero-order latent correlation between AS and AID is -0.318 (Table II), while the PLS path AS→AID is β = -0.707 (Table IV). This is suppression by PE: r(AS,PE) = 0.55 and r(PE,AID) = 0.318. Recomputing the paths from the correlations gives β ≈ ±0.707, R² ≈ 0.45 and an indirect effect of 0.55×0.707 = 0.389, all consistent with the report. The abstract calls the direct effect "strong", but the zero-order association is moderate. The PE–AID and AS–AID correlations are identical in size (0.318) with opposite signs, which is worth noting. Mode of administration, age and sex are not reported.
Заметка ИИ: There is one effect: academic self-efficacy × AI dependence (ACOSTA5 total), a latent correlation of -0.318 (n=430) from the Fornell-Larcker table. No observed correlation matrix is reported.

### ST076-1 · Public university students, northern Peru (Piura, Tumbes, Lambayeque, La Libertad, Cajamarca), n=430
Отчёты: R2786 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ACOSTA5 · total (T4) | **self_efficacy** · Academic self-efficacy (AS), 5 items adapted from Acosta-En… | latent | **-0.318** | **430** | 1 | Table II (Fornell–Larcker), p.7 | «AS 0.857 / PE 0.55 0.828 / AID -0.318 0.318 0.863» |

- E1: α ИИ 0.925, α коррелята 0.912; заметка: PLS-SEM latent construct correlation from the Fornell-Larcker table; no observed Pearson matrix is reported. Items AS1 and AS3 refer to working without AI, which overlaps in content with AI dependence.

**Ключевые поля выборки:**
- **n_analysed: 430** — Page 6, Metodología; Abstract p.1 — «A quantitative, non-experimental, cross-sectional explanatory design was implemented with 430 students from public universities in northern Peru»
- **population: university_students** — Page 6, Metodología — «Se incluyeron únicamente participantes con matrícula vigente [Only participants with current enrolment were included]»
- **sampling: quota or online panel** — Page 6, Metodología — «La muestra estuvo conformada por 430 estudiantes distribuidos por cuotas regionales en Piura (120), Tumbes (60), Lambayeque (100), La Libertad–Trujillo (110) y Cajamarca (40). [430 students distributed by regional quotas]»
- **ai_system: general_chatbot** — Page 6, Metodología — «hubieran utilizado herramientas de inteligencia artificial generativa (p. ej., ChatGPT, Gemini, Claude o Copilot) con fines académicos [had used generative AI tools (e.g., ChatGPT, Gemini, Claude or Copilot) for academic purposes]»

**Остальные поля:**
- country: PER — Page 6, Metodología — «estudiantes universitarios de universidades públicas del Perú [university students at public universities in Peru]»
- data_years: 2025 — Page 6, Metodología — «La recolección de datos se hizo en los meses de noviembre y diciembre del 2025. [Data were collected in November and December 2025.]»
- design: cross-sectional — Page 6, Metodología — «Se desarrolló un estudio cuantitativo, no experimental, de corte transversal y alcance explicativo [A quantitative, non-experimental, cross-sectional, explanat…»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: NR — NR — «NR»
- mode: NR — Page 6, Metodología — «La recolección de datos se efectuó mediante un cuestionario estructurado con escala Likert de 5 puntos [Data were collected using a structured 5-point Likert q…»
- attention_checks: yes — Page 6, Metodología — «se excluyeron respuestas incompletas o con patrones inválidos [incomplete responses or those with invalid patterns were excluded]»
- pub_status: conference — Page 1, header — «24th LACCEI International Multi-Conference for Engineering, Education, and Technology»
- language: Spanish (English abstract) — Page 2 — «Autoeficacia académica y dependencia de la inteligencia artificial en la educación superior peruana»
- funding_coi: NR (no funding or conflict-of-interest statement; no ethics committee approval) — Page 6, Metodología — «el estudio no requirió comité de ética [the study did not require an ethics committee]»
- notes: Inclusion required use of generative AI for academic purposes in the last academic period. The mode of administration (online or paper) is not stated. The number of excluded responses is not reported. The only eligible correlate is academic self-efficacy. Its items are adapted from Acosta-Enriquez et al. 2025, and two of them refer to working without AI.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Students were recruited with regional quotas; the report does not describe probability sampling. — Page 6, Metodología — «430 estudiantes distribuidos por cuotas regionales [430 students distributed by regional quotas]»
2. отклик: **unclear** — The report gives no response rate and no number of excluded responses. — Page 6, Metodología — «se excluyeron respuestas incompletas o con patrones inválidos [incomplete or invalid responses were excluded]»
3. валидная шкала зависимости от ИИ: **yes** — The 5-item AID scale is adapted from a published study (Acosta-Enriquez et al., 2025). This report also gives a measurement model with loadings, AVE and Fornell-Larcker results. — Page 6, Metodología; Table I, p.7 — «este cuestionario es adaptado de un estudio validado [31] [this questionnaire is adapted from a validated study]»
4. надёжность шкалы ИИ в выборке: **yes** — AID alpha = 0.925 in this sample. — Table I, p.7 — «AID (Dependencia de IA) AID1 0.843 0.925 0.927 0.944 0.744»
5. валидные шкалы коррелятов: **yes** — Academic self-efficacy uses 5 items adapted from the same published study [31], and a measurement model is reported here. However, these are not a standard self-efficacy instrument, and two items refer to AI, so the rev… — Page 6, Metodología — «AS1 (“Me siento capaz de comprender los temas académicos sin depender de la inteligencia artificial”) [I feel able to understand academic topics without depend…»
6. качество данных: **yes** — The report states a rule for excluding invalid responses. — Page 6, Metodología — «se excluyeron respuestas incompletas o con patrones inválidos [incomplete responses or those with invalid patterns were excluded]»

Правки:
- 

Проверено: да

---

## ST077 · Yuan 2026 · Australian journal of psychology

Основной отчёт R2823: [текст](../../fulltext/text/R2823.txt) — «From boredom to problematic AI chatbot use: a three-wave half-longitudinal mediation study of loneliness and dual-system self-control.» — [DOI](https://doi.org/10.1080/00049530.2026.2737094)
Лонгитюд (для описания): This is a three-wave half-longitudinal mediation design (about 30 days between waves, Oct–Dec 2024). Each construct was measured at one wave only: boredom proneness at T1; loneliness, control system and impulsive system at T2; PUAIC at T3. No autoregressive or cross-lagged paths could be estimated. Results come from PROCESS Model 81, pooled over 20 MI datasets and adjusted for sex and grade. Boredom T1 predicted loneliness T2 (β = .57), impulsive system T2 (β = .31) and control system T2 (β = −.38). Loneliness T2 predicted impulsive system T2 (β = .27) but not control system T2 (β = −.06). PUAIC T3 was predicted by boredom (β = .25), loneliness (β = .13) and impulsive system (β = .24); the control-system path was not significant (β = .08). Significant indirect effects ran through loneliness (.073), through the impulsive system (.077) and through the loneliness→impulsive serial path (.03…
Расхождения в тексте: Text and tables agree. The Discussion repeats the bivariate control-system–PUAIC r = −.15 from Table 1 and notes its sign reverses in the multivariate model (β = .08). Table 1 does not state its n or whether it was computed on imputed or complete-case data. No figure-only coefficients.
Заметка ИИ: One sample, four effects. All exposure–correlate correlations are cross-occasion (T1–T3 or T2–T3) because the half-longitudinal design gives no same-occasion pairs. The n per coefficient is NR.

### ST077-1 · Two Chinese universities, college students, three-wave half-longitudinal (CHN, n=551 baseline / 503 complete)
Отчёты: R2823 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PCUS · total (T1) | **boredom** · Chinese short form of the Boredom Proneness Scale (12 items) | pearson | **.39** | **NR** | lagged: T1-T3 | Table 1 | «5. PUAIC T3 / .39** / .36** / .39** / −.15** / 1» |
| E2 | PCUS · total (T1) | **loneliness** · Chinese short-form UCLA Loneliness Scale (ULS-8) | pearson | **.36** | **NR** | lagged: T2-T3 | Table 1 | «5. PUAIC T3 / .39** / .36** / .39** / −.15** / 1» |
| E3 | PCUS · total (T1) | **impulsivity** · Dual-System of Self-Control Scale, impulsive-system subscal… | pearson | **.39** | **NR** | lagged: T2-T3 | Table 1 | «5. PUAIC T3 / .39** / .36** / .39** / −.15** / 1» |
| E4 | PCUS · total (T1) | **self_control** · Dual-System of Self-Control Scale, control-system subscale … | pearson | **−.15** | **NR** | lagged: T2-T3 | Table 1 | «4. Control system T2 / −.42** / −.29** / −.33** / 1 / ... 5. PUAIC T3 / .39** / .36** / .39** / −.15** / 1» |

- E1: α ИИ .89, α коррелята .83; заметка: Boredom at T1, PUAIC at T3; no same-occasion correlation available. Table n not stated (551 baseline, 503 complete; MI used). Stat type assumed Pearson ('bivariate correlations').
- E2: α ИИ .89, α коррелята .86; заметка: Loneliness at T2, PUAIC at T3; no same-occasion correlation available. Table n not stated.
- E3: α ИИ .89, α коррелята .86; заметка: Impulsive system at T2, PUAIC at T3. Reviewer should confirm that mapping the impulsive system to impulsivity is acceptable. Table n not stated.
- E4: α ИИ .89, α коррелята .85; заметка: Control system at T2, PUAIC at T3; higher = greater self-regulatory capacity. Table n not stated.

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2, E3, E4: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: NR (n for Table 1 not stated; 551 at baseline, 533 at T2, 521 at T3, 503 complete cases; missing data multiply imputed)** — Methods, Participants and procedure; Data analyses — «Complete data across all three waves were available for 503 participants.»
- **population: university_students** — Abstract — «A three-wave half-longitudinal mediation design was used with 551 Chinese college students at baseline.»
- **sampling: convenience** — Methods, Participants and procedure — «participants were recruited from two universities in China using a convenience sampling method»
- **ai_system: general_chatbot** — Methods, Participants and procedure — «68.2% of participants primarily used Doubao, 21.9% reported using DeepSeek, and 9.9% used other AI tools, including Yuanbao, Qianwen, ChatGPT, and Gemini.»

**Остальные поля:**
- country: CHN — Methods, Participants and procedure — «participants were recruited from two universities in China using a convenience sampling method»
- data_years: 2024 — Methods, Participants and procedure — «At Wave 1, conducted in October 2024 ... At Wave 2, conducted in November 2024 ... At Wave 3, conducted in December 2024»
- design: panel — Methods, Participants and procedure — «A three-wave half-longitudinal design was implemented across the fall semester of 2024, with approximately 30 days between consecutive waves.»
- clinical_group: NA — NA — «NA»
- age_mean: 19.02 — Methods, Participants and procedure — «with a mean age of 19.02 years (SD = 1.17)»
- age_sd: 1.17 — Methods, Participants and procedure — «with a mean age of 19.02 years (SD = 1.17)»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 57.5 — Methods, Participants and procedure — «The baseline sample consisted of 57.5% female students»
- mode: NR — Methods, Participants and procedure — «Participants generated a self-created matching code based on the last four digits of their mobile phone number.»
- attention_checks: NR — Methods, Participants and procedure — «At Wave 3, conducted in December 2024, 521 participants provided valid responses on problematic AI chatbot use»
- pub_status: journal — Header — «venue: Australian journal of psychology; DOI: 10.1080/00049530.2026.2737094»
- language: English — Full text — «From boredom to problematic AI chatbot use: a three-wave half-longitudinal mediation study»
- funding_coi: Funding NR; no conflict of interest reported — Disclosure statement — «No potential conflict of interest was reported by the author(s).»
- notes: Half-longitudinal design: boredom proneness only at T1, loneliness and dual-system self-control only at T2, PUAIC only at T3; all Table 1 correlations with PUAIC are therefore cross-occasion. Two universities were recruited and analysed together as one sample. Missing data handled by 20 MI datasets; whether Table 1 is based on pooled imputed data or available cases is not stated. Mean weekly use 2.98 h (SD 1.05).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample from two universities. — Methods, Participants and procedure — «recruited from two universities in China using a convenience sampling method»
2. отклик: **unclear** — Initial response/participation rate not reported. Retention was high (503/551 complete, about 91%) and Little's MCAR test was non-significant, but this is attrition, not initial response. — Methods, Participants and procedure; Data analyses — «Complete data across all three waves were available for 503 participants.»
3. валидная шкала зависимости от ИИ: **yes** — Adapted from the published Problematic ChatGPT Use Scale (Yu et al., 2024); a CFA was also reported in this sample. — Measures, Problematic AI chatbot use — «Confirmatory factor analysis indicated acceptable fit (CFI = .95, TLI = .94, RMSEA = .062, SRMR = .047).»
4. надёжность шкалы ИИ в выборке: **yes** — alpha .89, omega .90 in this sample. — Measures, Problematic AI chatbot use — «The adapted scale demonstrated good internal consistency (Cronbach’s α = .89; McDonald’s ω = .90).»
5. валидные шкалы коррелятов: **yes** — Boredom Proneness Scale short form (Li et al., 2016), UCLA-8 (Hays & DiMatteo, 1987) and Dual-System of Self-Control Scale (Xie et al., 2014) are all published instruments. — Measures — «Dual-System of Self-Control Scale developed by Xie et al. (2014)»
6. качество данных: **unclear** — The report mentions 'valid responses' but states no attention checks or screening rule. — Methods, Participants and procedure — «521 participants provided valid responses on problematic AI chatbot use»

Правки:
- 

Проверено: да

---

## ST078 · Yıldırım 2026 · Current Perspectives in Social Sciences

Основной отчёт R2842: [текст](../../fulltext/text/R2842.txt) · [PDF](../../fulltext/pdf/R2842.pdf) — «Psychological Distress and Artificial Intelligence Dependency: The Moderating Role of Extraversion» — [DOI](https://doi.org/10.53487/atasobed.1920593)
Расхождения в тексте: (1) Table 1 note gives "*p < .01, ** p < .001". At N=438, r=.11 has p≈.02, so the star thresholds look mislabelled. (2) The Results text says AID is positively related to PD "whereas the relationships among the other variables are negative and significant". Table 1, however, shows gender–PD -.03 (not starred) and several positive correlations (age–gender .20, age–extraversion .16, gender–extraversion .13). (3) The interaction term differs between text and Table 2. Text: B = 0.01, 95% CI [0.005, 0.024]. Table 2: B = .02, CI .01 to .02. (4) The PD CI differs: text 95% CI [-0.20, -0.02], Table 2 LL -.21. The gender t also differs: text -2.56, Table 2 -2.57. (5) The Johnson–Neyman text says the PD–AID effect is significant below extraversion 2.87, while the -1 SD conditional effect is non-significant and negative. Its direction below 2.87 is not given. (6) Data-collection years are not stat…
Заметка ИИ: Single cross-sectional sample. Two zero-order Pearson correlations were extracted: DAI total with DASS-21 total (distress) and with TIPI extraversion. DASS subscale correlations were not reported, only the total score.

### ST078-1 · Turkish university students, convenience online sample (Pamukkale University ethics), n=438
Отчёты: R2842 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **distress** · DASS-21 total (psychological distress) | pearson | **.11** | **438** | 1 | Page 5, Table 1 | «4. PD / 18.71 / 12.09 / -.17** / -.03 / .11*» |
| E2 | DAI · total (T4) | **extraversion** · TIPI Extraversion | pearson | **-.13** | **438** | 1 | Page 5, Table 1 | «5. Extraversion / 9.47 / 3.20 / .16** / .13** / -.13** / -.18**» |

- E1: α ИИ .75, α коррелята .92; заметка: The matrix gives two decimals only. The star legend (*p < .01) looks inconsistent with r = .11 at N = 438.
- E2: α ИИ .75, α коррелята .65; заметка: The extraversion subscale has only 2 items and alpha .65.

**Ключевые поля выборки:**
- **n_analysed: 438** — Page 5, Table 1 note — «Note 1. N=438»
- **population: university_students** — Page 3, Participants — «The inclusion criterion for the study was being currently enrolled as a university student»
- **sampling: convenience** — Page 3, Participants — «a total of 438 university students (24.9% male) were recruited using a convenience sampling method.»
- **ai_system: ai_unspecified** — Page 4, Instruments — «to assess individuals' levels of dependence on AI ... "I feel unprotected when I do not have access to AI"»

**Остальные поля:**
- country: TUR — Page 4, Procedure; Page 1 affiliation — «ethical approval for the study was obtained from the Pamukkale University Social and Human Sciences Research and Publication Ethics Committee»
- data_years: NR — Page 4, Procedure — «Data were collected over a three-month period via an online survey platform. ... (Approval No: 68282350/2025/18, Date: December 30, 2025)»
- design: cross-sectional — Page 7, Discussion (limitations) — «The cross-sectional design limits causal interpretations.»
- clinical_group: NA — Page 3, Participants — «exclusion criteria included not being a university student or having a diagnosis of psychosis or a cognitive disorder.»
- age_mean: 21.65 — Page 3, Participants — «The mean age of the participants was 21.65 (SD = 3.65)»
- age_sd: 3.65 — Page 3, Participants — «The mean age of the participants was 21.65 (SD = 3.65)»
- age_min: 18 — Page 3, Participants — «with an age range between 18 and 50 years.»
- age_max: 50 — Page 3, Participants — «with an age range between 18 and 50 years.»
- pct_female: 75.1 (derived as 100 - 24.9% male; female share not stated directly) — Page 3, Participants — «a total of 438 university students (24.9% male)»
- mode: online — Page 4, Procedure — «Data were collected over a three-month period via an online survey platform.»
- attention_checks: NR — Page 4, Procedure / Statistical Analysis — «Participation in the study was restricted to individuals who provided informed consent.»
- pub_status: journal — Page 1, header — «Current Perspectives in Social Sciences ... Research Article Araştırma Makalesi DOI: 10.53487/atasobed.1920593»
- language: English (abstract also in Turkish) — Page 1-8 — «Psychological Distress and Artificial Intelligence Dependency: The Moderating Role of Extraversion»
- funding_coi: No funding; author declares no conflict of interest — Page 8, declarations — «Conflict of Interest: The author declare no conflict of interest. Financial Support: The author declared that they received no financial support for this study.»
- notes: Country is inferred from the Turkish university ethics committee and the Turkish versions of the scales; the sample's country is not stated directly. Percentage female is derived from the 24.9% male figure. No specific AI system is named; the study does not distinguish types of AI use. TIPI extraversion alpha is .65 (2 items).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited via an online survey — Page 3, Participants — «recruited using a convenience sampling method»
2. отклик: **unclear** — No response rate and no comparison of non-responders reported — Page 3-4, Methods — «participation was entirely voluntary»
3. валидная шкала зависимости от ИИ: **yes** — Published scale (Morales-García et al., 2024) with a published Turkish adaptation and validation (Savaş, 2024) — Page 4, Instruments — «The Turkish adaptation, as well as the validity and reliability study of the scale, was conducted by Savaş (2024), reporting a Cronbach's alpha coefficient of …»
4. надёжность шкалы ИИ в выборке: **yes** — Alpha .75 in this sample — Page 4, Instruments — «For the present study, the Cronbach's alpha coefficient of the scale was .75.»
5. валидные шкалы коррелятов: **yes** — DASS-21 (Turkish adaptation, Sarıçam 2018) and TIPI (Turkish adaptation, Atak 2013) are published instruments — Page 4, Instruments — «DASS-21, developed by Lovibond and Lovibond (1995) ... TIPI developed by Gosling et al. (2003) and adapted into Turkish by Atak (2013)»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported — Page 4, Procedure / Statistical Analysis — «The data obtained from the measurement instruments were analyzed using IBM SPSS Statistics version 31.0.»

Правки:
- 

Проверено: да

---

## ST079 · Zencirci 2026 · Eskişehir Türk Dünyası Uygulama ve Araştırma Merkezi Halk Sağlığı Dergisi

Основной отчёт R2858: [текст](../../fulltext/text/R2858.txt) · [PDF](../../fulltext/pdf/R2858.pdf) — «Assessment of dependence on artificial intelligence and associated factors among medical students» — [DOI](https://doi.org/10.35232/estudamhsd.1915530)
Расхождения в тексте: The correlations in the abstract (r=-0.235 with ASES; r=-0.376 with MSPSS) match the Results text on page 5. There is no correlation matrix. Table 3, Model 3 gives the 95% CI for daily AI use duration as (1.150; 2.301) for B=2.176. This looks like a typo but does not affect the extracted values. Figure 1 shows only frequencies of AI tool use and contains no coefficients.
Заметка ИИ: This is a draft for checking against the source. The paper has one sample (n=236 medical students in Türkiye) and two zero-order Pearson correlations with the DAI total score: academic self-efficacy (r=-0.235) and perceived social support (r=-0.376). The paper gives no reliability coefficients for this sample; all alphas it cites come from earlier validation studies. The ai_system code 'general_chatbot' is a judgement call (ChatGPT 95.8%, Gemini 55.5%, Canva AI/Notion AI 10.6%); 'mixed' is also defensible.

### ST079-1 · Medical students years 1-4, Bilecik Şeyh Edebali University, Türkiye, n=236
Отчёты: R2858 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale (ASES; Jerusalem & Schwarzer, … | pearson | **-0.235** | **236** | 1 | Page 5, Results text | «A weak negative correlation was found between DAI and ASES scores (r=-0.235, p<0.001)» |
| E2 | DAI · total (T4) | **social_support** · Multidimensional Scale of Perceived Social Support (MSPSS) … | pearson | **-0.376** | **236** | 1 | Page 5, Results text | «a moderate negative correlation was found between DAI and MSPSS scores (r=-0.376, p<0.001)» |

- E1: заметка: Reported in text (and abstract) only; no correlation table. Alpha 0.79 cited is from the Turkish validation study, not this sample.
- E2: заметка: Reported in text (and abstract) only; MSPSS subscale correlations not reported. Alpha 0.89 cited is from the Turkish validation study, not this sample.

**Ключевые поля выборки:**
- **n_analysed: 236** — Page 3, Research Design and Participants — «236 students (77.6%) who agreed to participate and completed the questionnaire were included.»
- **population: university_students** — Page 3, Research Design and Participants — «1st–4th grade students of the Faculty of Medicine at Bilecik Şeyh Edebali University»
- **sampling: census** — Page 3, Research Design and Participants — «The study aimed to reach all students and no sampling method was applied.»
- **ai_system: general_chatbot** — Page 3, Results; Figure 1 — «A total of 95.8% of the students reported using ChatGPT, 55.5% Gemini, and 10.6% Canva AI/Notion AI (Figure 1).»

**Остальные поля:**
- country: TUR — Page 3, Research Design and Participants — «1st–4th grade students of the Faculty of Medicine at Bilecik Şeyh Edebali University»
- data_years: 2025 — Page 3, Research Design and Participants — «This cross-sectional study was conducted in November 2025»
- design: cross-sectional — Page 3, Research Design and Participants — «This cross-sectional study was conducted in November 2025 among 1st–4th grade students»
- clinical_group: NA — NA — «NA»
- age_mean: 20.02 — Page 3, Results — «Their ages ranged from 18 to 28 years, with a mean age of 20.02±1.65 years.»
- age_sd: 1.65 — Page 3, Results — «with a mean age of 20.02±1.65 years»
- age_min: 18 — Page 3, Results — «Their ages ranged from 18 to 28 years»
- age_max: 28 — Page 3, Results — «Their ages ranged from 18 to 28 years»
- pct_female: 50.8 — Page 3, Results; Table 1 — «49.2% were male and 50.8% were female»
- mode: online — Page 3, Research Design and Participants — «a link to the questionnaire, which had been transferred to a digital platform, was shared via student WhatsApp groups»
- attention_checks: NR — Page 3, Material and Method — «236 students (77.6%) who agreed to participate and completed the questionnaire were included.»
- pub_status: journal — Page 1, header — «ESTÜDAM Halk Sağlığı Dergisi. 2026. Cilt 11 Sayı 2. Araştırma Makalesi / Original Research Article»
- language: English (with Turkish abstract) — Page 1-8 — «Assessment of dependence on artificial intelligence and associated factors among medical students»
- funding_coi: No funding; author declares no conflicts of interest — Page 8, Funding; Conflict of interest statement — «This research received no financial or other support. ... The author declares no conflicts of interest.»
- notes: Single-author single-faculty study. DAI asks about AI in general; tools used were mainly ChatGPT/Gemini (general chatbots) with some Canva AI/Notion AI (task tools) — reviewer may prefer 'mixed'. Reliability coefficients cited are from the original/Turkish validation studies, not this sample. Population denominator implied by 77.6% response (~304 students).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **yes** — All 1st–4th year medical students of one faculty were invited (census attempt of a defined population); no sampling applied, though recruitment via WhatsApp groups and voluntary participation. — Page 3, Research Design and Participants — «The study aimed to reach all students and no sampling method was applied.»
2. отклик: **yes** — Response rate 77.6% (≥60%). — Page 3, Research Design and Participants — «236 students (77.6%) who agreed to participate and completed the questionnaire were included.»
3. валидная шкала зависимости от ИИ: **yes** — DAI developed and validated by Morales-García et al. (2024); Turkish validation by Savaş (2024). — Page 3, Data Collection Instruments — «DAI was developed by Morales-García et al. and the Turkish validity and reliability study of the scale was conducted by Savaş in 2024 (8, 16).»
4. надёжность шкалы ИИ в выборке: **unclear** — Only the alpha from the validation study (0.82) is cited; no reliability for this sample reported. — Page 3, Data Collection Instruments — «The Cronbach's alpha value of the scale was reported as 0.82 (16).»
5. валидные шкалы коррелятов: **yes** — ASES (Jerusalem & Schwarzer; Turkish adaptation Yılmaz et al.) and MSPSS (Zimet et al.; Turkish adaptation Eker et al.) are published instruments. — Page 3, Data Collection Instruments — «Perceived social support was measured using the MSPSS, a scale developed by Zimet et al. and adapted into Turkish by Eker et al. (19, 20).»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported. — Page 3, Material and Method — «236 students (77.6%) who agreed to participate and completed the questionnaire were included.»

Правки:
- 

Проверено: да

---

## ST080 · Zhang 2026 · BMC psychology

Основной отчёт R2863: [текст](../../fulltext/text/R2863.txt) — «A SEM-ANN analysis to examine impact of AI overreliance through a social cognitive lens: the roles of dependency, FOMO, addiction, and anxiety.» — [DOI](https://doi.org/10.1186/s40359-026-04246-6)
Расхождения в тексте: 1) The text says all hypotheses H1–H7 were supported, but Table 6 lists only H1–H6. 2) The text says "The path from AI Dependency to AI Overreliance was positive and significant (β = 0.145, p < 0.001)", but the direct path in Tables 6/7 is 0.120 (p = 0.002). 0.145 is the total effect in Table 7. 3) The EFA text describes a "clean two-factor solution" with items AID1–AID4 on Factor 1 and the overreliance items on Factor 2. Table 2 shows a 7-component solution with five AI_Den items (AI_Den1–5) on component 7 and the AI_OL items on component 2. 4) The text says AVE values were "above 0.709", but the minimum AVE in Table 3 (TS) is exactly 0.709. 5) The text says Shanghai was chosen "rather than convenience sampling", yet sampling was non-probability purposive via Wenjuanxing. 6) The ANN is described as a multilayer network with sigmoid hidden layers, but the repetitions are called an "RBF …
Заметка ИИ: The only zero-order-type associations are the PLS latent construct correlations in Table 4 (Fornell-Larcker), so all rows use stat_type latent. HTMT ratios and path coefficients were not extracted. Correlations among the three AI-dependence scores (AI_OL–AI_Den 0.539, AI_OL–AI_ADD 0.578, AI_Den–AI_ADD 0.458) and with cognitive overload and technostress were not extracted because there is no dictionary construct for them. Anxiety coding depends on the item content in Appendix 1, which was not available.

### ST080-1 · Working adults, Shanghai, China (Wenjuanxing), n=504
Отчёты: R2863 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2863_1 · total (T4) | **anxiety** · Anxiety (Anx), 8 items adapted from Oei et al. [48] | latent | **0.594** | **504** | 1 | Table 4 (Fornell-Larcker criteria) | «Anx / 0.486 / 0.48 / 0.594 / 0.908» |
| E2 | ADHOC_R2863_1 · total (T4) | **fomo** · FOMO, 8 items derived from Budnick et al. [10] | latent | **0.57** | **504** | 1 | Table 4 (Fornell-Larcker criteria) | «FOMO / 0.453 / 0.474 / 0.57 / 0.542 / 0.507 / 0.899» |
| E3 | DAI · total (T4) | **anxiety** · Anxiety (Anx), 8 items adapted from Oei et al. [48] | latent | **0.48** | **504** | 1 | Table 4 (Fornell-Larcker criteria) | «Anx / 0.486 / 0.48 / 0.594 / 0.908» |
| E4 | DAI · total (T4) | **fomo** · FOMO, 8 items derived from Budnick et al. [10] | latent | **0.474** | **504** | 1 | Table 4 (Fornell-Larcker criteria) | «FOMO / 0.453 / 0.474 / 0.57 / 0.542 / 0.507 / 0.899» |
| E5 | ADHOC_R2863_3 · total (T4) | **anxiety** · Anxiety (Anx), 8 items adapted from Oei et al. [48] | latent | **0.486** | **504** | 1 | Table 4 (Fornell-Larcker criteria) | «Anx / 0.486 / 0.48 / 0.594 / 0.908» |
| E6 | ADHOC_R2863_3 · total (T4) | **fomo** · FOMO, 8 items derived from Budnick et al. [10] | latent | **0.453** | **504** | 1 | Table 4 (Fornell-Larcker criteria) | «FOMO / 0.453 / 0.474 / 0.57 / 0.542 / 0.507 / 0.899» |

- E1: α ИИ 0.969, α коррелята 0.970; заметка: PLS-SEM construct correlation from the Fornell-Larcker matrix (columns AI_ADD, AI_Den, AI_OL). Check whether the anxiety items are AI-specific.
- E2: α ИИ 0.969, α коррелята 0.966; заметка: PLS-SEM construct correlation; printed with two decimals.
- E3: α ИИ 0.953, α коррелята 0.970; заметка: PLS-SEM construct correlation; printed with two decimals. Check whether the anxiety items are AI-specific.
- E4: α ИИ 0.953, α коррелята 0.966; заметка: PLS-SEM construct correlation.
- E5: α ИИ 0.981, α коррелята 0.970; заметка: PLS-SEM construct correlation. Check whether the anxiety items are AI-specific.
- E6: α ИИ 0.981, α коррелята 0.966; заметка: PLS-SEM construct correlation.

**Ключевые поля выборки:**
- **n_analysed: 504** — Data collection procedure and ethical considerations — «a total of 504 valid responses were retained for subsequent analysis.»
- **population: employees** — Data collection procedure and ethical considerations — «targeting individuals who met two predefined criteria: (1) being employed full-time in Shanghai and (2) regularly using AI tools in their daily work tasks.»
- **sampling: convenience** — Research design; Data collection procedure — «This study adopted a non-probability sampling method, specifically purposive sampling, to collect data.»
- **ai_system: ai_unspecified** — Data collection procedure and ethical considerations — «(2) regularly using AI tools in their daily work tasks.»

**Остальные поля:**
- country: CHN — Data collection procedure and ethical considerations — «The study targeted working adults of Shanghai, China, as the research population.»
- data_years: 2025 — Data collection procedure and ethical considerations — «Data were collected online between February 12 and May 2025 through the Wenjuanxing online survey platform»
- design: cross-sectional — Limitation and future research — «First, the cross-sectional design limits causal inference.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age | Under 25 | 182 | 36.11»
- age_sd: NR — Table 1 — «Age | Under 25 | 182 | 36.11»
- age_min: NR (youngest band 'Under 25') — Table 1 — «Age | Under 25 | 182 | 36.11»
- age_max: NR (oldest band '55 +') — Table 1 — «55 + | 9 | 1.79»
- pct_female: 41.27 — Table 1 — «Female | 208 | 41.27»
- mode: online — Data collection procedure and ethical considerations — «Data were collected online between February 12 and May 2025 through the Wenjuanxing online survey platform»
- attention_checks: yes — Data collection procedure; Data analysis procedures — «all responses were carefully screened and cleaned to remove incomplete, inconsistent, or outlier entries.»
- pub_status: journal — Header — «BMC psychology; DOI: 10.1186/s40359-026-04246-6»
- language: English — Full text — «A SEM–ANN analysis to examine impact of AI overreliance through a social cognitive lens»
- funding_coi: NR (funding and COI statements not included in the supplied text) — NA — «NR»
- notes: Three AI-dependence scores: AI Overreliance (AI_OL, 11 items adapted from Maral et al.), AI Dependency (AI_Den, 5 items, Morales-García et al.), AI Addiction (AI_ADD, 12 items adapted from Pawlikowski et al.). Only correlations available are the latent (PLS construct) correlations in the Fornell-Larcker part of Table 4. Not extracted: cognitive overload (no dictionary key), technostress (excluded from stress), HTMT ratios, and correlations among the three exposure scores. The 'Anx' scale (8 items adapted from Oei et al. [48]) was coded as general anxiety. The theory section describes anxiety …

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive non-probability sample recruited through Wenjuanxing online platform. — Research design; Data collection procedure — «This study adopted a non-probability sampling method, specifically purposive sampling»
2. отклик: **unclear** — No response rate or number invited reported; no non-responder comparison. — Data collection procedure and ethical considerations — «Following these data screening and cleaning procedures, a total of 504 valid responses were retained»
3. валидная шкала зависимости от ИИ: **yes** — AI_Den adapted from published DAI (Morales-García et al., 2024). AI_OL and AI_ADD were adapted from published scales, and this report gives EFA/CFA evidence for them (loadings, CR, AVE, discriminant validity). AI_OL and… — Research design; Table 2; Table 3 — «AI Overreliance was adapted from Maral et al. [44], comprising 11 items. AI Dependency was measured using five items adapted from Morales-García et al. [46].»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha for all AI-dependence scores >= .95. — Table 3 — «AI_ADD | 0.981 | 0.983 | 0.826 AI_Den | 0.953 | 0.964 | 0.842 AI_OL | 0.969 | 0.973 | 0.765»
5. валидные шкалы коррелятов: **yes** — FOMO and anxiety were adapted from published instruments (Budnick et al.; Oei et al.). — Research design — «Fear of Missing Out (FOMO) was assessed with eight items derived from Budnick et al. [10]. ... Anx was measured with eight items adapted from Oei et al. [48].»
6. качество данных: **yes** — Stated rules for invalid responses: removal of missing, duplicate, inconsistent and outlier responses (criteria not specified; no attention-check items). Eligibility screening questions were also used. — Data collection procedure; Data analysis procedures — «responses with missing values were removed. In addition, responses with the same ID were treated as duplicate entries and retained only once.»

Правки:
- 

Проверено: да

