# Проверка выписывания — файл 14 из 14

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

## ST122 · Ignatowski 2026 · PsyArXiv

Основной отчёт R1053: [текст](../../fulltext/text/R1053.txt) · [PDF](../../fulltext/pdf/R1053.pdf) — «When AI Feels like Human: Anthropomorphism, Loneliness, and Problematic Use of Chatbots among School Teachers in Poland» — [DOI](https://doi.org/10.31234/osf.io/stndb_v1)
Расхождения в тексте: (1) Table 3: path c (total effect of loneliness on problematic use) has p = .040, but its 95% CI is [-0.008, 0.480], which includes zero. (2) Table 3, row c': the SE and Beta columns look swapped (0.190 is shown under SE and 0.134 under Beta). The text gives β = .190, SE = .134. (3) Page 8 says that 'anthropomorphization was positively associated with problematic AI use after controlling for loneliness', but the mediation b path is not significant (β = .205, p = .095). (4) Partial correlations controlling for PHQ-4 or loneliness (r = .27, r = .08) and the mediation betas are not extracted. (5) The title differs slightly between the record ('Anthropomorphism') and the PDF ('Anthropomorphisation').
Заметка ИИ: One sample, two zero-order effects (problematic AI use with UCLA-3 loneliness, and with PHQ-4 total coded as distress). Correlations with anthropomorphism and usage time are not dictionary constructs and were not extracted.

### ST122-1 · School teachers using AI chatbots, Bielany district of Warsaw, Poland (n=102)
Отчёты: R1053 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1053_1 · total (?) | **loneliness** · UCLA-3 (three-item UCLA Loneliness Scale, Polish translatio… | pearson | **.310** | **102** | 1 | Page 8, Table 2 | «3. Problematic use 1-5 1.389 0.578 .310** .295** —» |
| E2 | ADHOC_R1053_1 · total (?) | **distress** · PHQ-4 total (anxiety and depressive symptoms) | pearson | **.243** | **102** | 1 | Page 8, Table 2 | «4. Anxiety and depressive symptoms 0-3 0.917 0.726 .569*** .265** .243* —» |

- E1: α ИИ .685, α коррелята .741; заметка: Row 3 Problematic use x column 1 Loneliness.
- E2: α ИИ .685, α коррелята .846; заметка: PHQ-4 composite of anxiety and depression items, coded as distress. No separate anxiety or depression subscale correlations are reported.

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2: шкала ИИ не из списка семейств: напишите, какая это шкала

**Ключевые поля выборки:**
- **n_analysed: 102** — Page 5, Participants — «A total of 136 individuals provided informed consent and participated in the study. Of these, 102 participants who reported using AI chatbots were included in the present analyses.»
- **population: employees** — Page 5, Participants — «The participants were primary and secondary school teachers»
- **sampling: convenience** — Page 5, Participants/Procedure — «Participants enrolled in the project “Bielany promotes prevention, counters addiction, and supports diversity” first attended 90-minute educational sessions on addiction in the context of neurodiversity. Following the sessions, participants were invited to co…»
- **ai_system: general_chatbot** — Page 5, Participants; Appendix 2 — «102 participants who reported using AI chatbots were included in the present analyses.»

**Остальные поля:**
- country: POL — Page 5, Participants — «The participants were primary and secondary school teachers from the Bielany district of Warsaw»
- data_years: 2025 — Page 5, Procedure — «Data collection took place in November and December 2025.»
- design: cross-sectional — Page 12, Limitations — «First, the study had a cross-sectional and correlational design.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 5, Participants — «The largest age group was 35–44 years (36.3%), followed by 45–54 years (31.4%), 25–34 years (17.6%), and 55 years or older (13.7%); 1.0% were aged 18–24 years.»
- age_sd: NR — Page 5, Participants — «The largest age group was 35–44 years (36.3%)»
- age_min: NR (age reported in bands only; youngest band 18–24 years, 1.0%) — Page 5, Participants — «1.0% were aged 18–24 years.»
- age_max: NR (oldest band 55 years or older, 13.7%) — Page 5, Participants — «and 55 years or older (13.7%)»
- pct_female: 78.4 (80 of 102; computed) — Page 5, Participants — «The sample consisted of 80 women, 20 men, and 2 individuals who selected “prefer not to say” for gender.»
- mode: online — Page 5, Procedure — «participants were invited to complete an online survey.»
- attention_checks: NR — Page 5-6, Procedure/Data analysis — «All data were collected anonymously.»
- pub_status: preprint — Header (venue) — «venue: PsyArXiv; DOI: 10.31234/osf.io/stndb_v1»
- language: English — Full text — «WHEN AI FEELS LIKE A HUMAN: ANTHROPOMORPHISATION, LONELINESS, AND PROBLEMATIC USE OF CHATBOTS AMONG SCHOOL TEACHERS IN POLAND»
- funding_coi: Project co-funded by the Bielany District Office of the City of Warsaw and Research Development Center Ltd. (second author's affiliation); no COI statement reported. — Page 5, Participants — «The project was co-funded by the Bielany District Office of the City of Warsaw and Research Development Center Ltd. (Centrum Rozwoju Badań Sp. z o.o.)»
- notes: Participants were recruited after attending an addiction-prevention educational session, which may prime responses about addiction. Only AI chatbot users (102 of 136) were analysed. The problematic use index has 3 author-developed items based on ICD-11 criteria, rated 1–5 and averaged. PHQ-4 total (anxiety + depression combined) was coded as distress. Anthropomorphism and usage time are not dictionary constructs. The single-item escape motive has no correlation reported, so it was not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample of teachers who took part in a municipal prevention project and were invited after the sessions — Page 5, Procedure — «Following the sessions, participants were invited to complete an online survey.»
2. отклик: **unclear** — The number invited (session attendees) is not reported, so no response rate can be computed; 136 consented. — Page 5, Participants — «A total of 136 individuals provided informed consent and participated in the study.»
3. валидная шкала зависимости от ИИ: **no** — Ad hoc 3-item index written by the authors; no published validation. In this sample only alpha and item-total correlations are reported, with no factor analysis. The authors say it is not a homogeneous scale. — Page 5, Measures; Page 12, Limitations — «Problematic AI use was measured using a brief three-item symptom index based on criteria for behavioral addictions included in the ICD-11.»
4. надёжность шкалы ИИ в выборке: **no** — Alpha = .685 in this sample, below .70 — Page 6, Results — «The three-item problematic AI use index, based on ICD-11 criteria, demonstrated moderate internal consistency (α = .685).»
5. валидные шкалы коррелятов: **yes** — UCLA-3 (Hughes et al., 2004; Polish translation by the authors) and PHQ-4 (validated Polish adaptation) are published instruments — Page 6, Measures — «Loneliness was measured using the short three-item version of the UCLA Loneliness Scale (UCLA-3; Hughes et al., 2004), translated by the authors.»
6. качество данных: **unclear** — No attention checks, careless-responding screening or rule for invalid responses reported — Page 5-6, Procedure/Data analysis — «All data were collected anonymously. Data collection took place in November and December 2025.»

Правки:
- 

Проверено: да  # автор в чате 2026-10-18: «проверил, всё гуд»

---

## ST123 · Goh 2025 · PsyArXiv

Основной отчёт R3484: [текст](../../fulltext/text/R3484.txt) · [PDF](../../fulltext/pdf/R3484.pdf) — «Generative Artificial Intelligence Dependency: Scale Development, Validation, and its Motivational, Behavioral, and Psychological Correlates» — [DOI](https://doi.org/10.31234/osf.io/aphtb_v2)
Не выписано ИИ: Studies 1a (n = 19), 1b (n = 71) and 1c (n = 70) were Singapore item-development pilots: no correlates and no demographics. Study 2 (Singapore, n = 203) was an EFA with the GAIDS only. Study 3 (US CloudResearch, n = 410) was a CFA and sex-invariance study with the GAIDS only. Study 4 (Singapore, n = 168) measured test-retest reliability of the GAIDS only. None of these report a correlate from the construct dictionary.
Лонгитюд (для описания): NA. None of the extracted samples is longitudinal. Study 4 (excluded) gave the GAIDS twice, one week apart (ICC = .87; r = .87), but measured no correlates and reports no cross-lagged paths.
Расхождения в тексте: Study 6: the text says 261 participants, but Table 8, Figure 4 and AM12/AM13 give N = 266. Study 6 latent correlations for the total score (text/Figure 4) differ slightly from the Pearson rs in AM13: procrastination .16 vs .12, loneliness .15 vs .14, life satisfaction .25 vs .23, positive affect .06 vs .08. The Figure 4 note calls the CFA standardized covariances "bivariate zero-order correlations". Table 8 vs text: the text says FoMO correlated positively with "all three subscales", but Withdrawal = .12 is non-significant and its value is not given in the text. The text gives p = .001 for procrastination–negative consequences, while the table marks it ***. Study 5: the text reports latent |r| (absolute values) for the Fornell-Larcker comparison. Openness |r| = .31 in the text vs zero-order -.32 in AM11. The Analytic Plan says the Big Five were entered as observed scale means, but the A…
Заметка ИИ: Two samples extracted: Study 5 (Singapore students, Big Five; both the GAIDS and the Generative AI Addiction scale) and Study 6 (US CloudResearch adults). Correlates with no dictionary key were not extracted: BMPN needs, cognitive failure, task performance, indecisiveness, critical thinking, creative self, self-concept clarity and negative affect. Study 5 latent values are printed as absolute values only; the reviewer should decide whether to use them.

### ST123-1 · Study 5: Singapore university subject pool, n = 131
Отчёты: R3484 (main; PsyArXiv preprint v2 incl. ResearchBox #3834 Additional Materials); R3485 (version of record, not retrieved)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **extraversion** · BFI-2-S Extraversion | pearson | **-.19** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «3. Extraversion / -.19 / -.07 / —» |
| E2 | GAIDS · total (T1) | **agreeableness** · BFI-2-S Agreeableness | pearson | **-.22** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «4. Agreeableness / -.22 / -.16 / -.00 / —» |
| E3 | GAIDS · total (T1) | **conscientiousness** · BFI-2-S Conscientiousness | pearson | **-.21** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «5. Conscientiousness / -.21 / -.15 / .22 / .22 / —» |
| E4 | GAIDS · total (T1) | **neuroticism** · BFI-2-S Neuroticism | pearson | **.16** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «6. Neuroticism / .16 / .17 / -.32 / -.07 / -.46 / —» |
| E5 | GAIDS · total (T1) | **openness** · BFI-2-S Openness | pearson | **-.32** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «7. Openness / -.32 / -.16 / .38 / .10 / .10 / .00 / —» |
| E6 | GAIDS · total (T1) | **agreeableness** · BFI-2-S Agreeableness | latent | **/r/ = .22** | **131** | 1 | p. 23, Section 7.2.2 | «exceeded all /r/ values between Generative AI Dependency Scale and the Big Five domains (Agreeableness: .56 > .22» |
| E7 | GAIDS · total (T1) | **conscientiousness** · BFI-2-S Conscientiousness | latent | **/r/ = .21** | **131** | 1 | p. 23, Section 7.2.2 | «Conscientiousness: .66 > .21» |
| E8 | GAIDS · total (T1) | **extraversion** · BFI-2-S Extraversion | latent | **/r/ = .19** | **131** | 1 | p. 23, Section 7.2.2 | «Extraversion: .68 > .19» |
| E9 | GAIDS · total (T1) | **neuroticism** · BFI-2-S Neuroticism | latent | **/r/ = .16** | **131** | 1 | p. 23, Section 7.2.2 | «Neuroticism: .67 > .16» |
| E10 | GAIDS · total (T1) | **openness** · BFI-2-S Openness | latent | **/r/ = .31** | **131** | 1 | p. 23, Section 7.2.2 | «and Openness: .63 > .31» |
| E11 | ADHOC_R3484_2 · total (?) | **extraversion** · BFI-2-S Extraversion | pearson | **-.07** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «3. Extraversion / -.19 / -.07 / —» |
| E12 | ADHOC_R3484_2 · total (?) | **agreeableness** · BFI-2-S Agreeableness | pearson | **-.16** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «4. Agreeableness / -.22 / -.16 / -.00 / —» |
| E13 | ADHOC_R3484_2 · total (?) | **conscientiousness** · BFI-2-S Conscientiousness | pearson | **-.15** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «5. Conscientiousness / -.21 / -.15 / .22 / .22 / —» |
| E14 | ADHOC_R3484_2 · total (?) | **neuroticism** · BFI-2-S Neuroticism | pearson | **.17** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «6. Neuroticism / .16 / .17 / -.32 / -.07 / -.46 / —» |
| E15 | ADHOC_R3484_2 · total (?) | **openness** · BFI-2-S Openness | pearson | **-.16** | **131** | 1 | Supplement AM11 (suppl. p. 14) | «7. Openness / -.32 / -.16 / .38 / .10 / .10 / .00 / —» |

- E1: α ИИ NR, α коррелята .83; заметка: Value from the ResearchBox supplement; two decimals only
- E2: α ИИ NR, α коррелята .70; заметка: Value from the supplement
- E3: α ИИ NR, α коррелята .79; заметка: Value from the supplement
- E4: α ИИ NR, α коррелята .82; заметка: Value from the supplement
- E5: α ИИ NR, α коррелята .78; заметка: Value from the supplement; the CFA text reports |r| = .31 for openness
- E6: α ИИ NR, α коррелята .70; заметка: Standardized covariance between the higher-order latent GAIDS factor and the trait (Fornell-Larcker comparison). The text prints only the absolute value; the sign is not given (the zero-order r is -.22). Reviewer to decide on use.
- E7: α ИИ NR, α коррелята .79; заметка: Absolute value only; sign not reported (the zero-order r is -.21)
- E8: α ИИ NR, α коррелята .83; заметка: Absolute value only; sign not reported (the zero-order r is -.19)
- E9: α ИИ NR, α коррелята .82; заметка: Absolute value only; sign not reported (the zero-order r is .16)
- E10: α ИИ NR, α коррелята .78; заметка: Absolute value only; sign not reported (the zero-order r is -.32)
- E11: α ИИ .80, α коррелята .83; заметка: Generative AI Addiction scale (Zhou & Zhang, 2024), 3 items, 7-point scale
- E12: α ИИ .80, α коррелята .70; заметка: Generative AI Addiction scale
- E13: α ИИ .80, α коррелята .79; заметка: Generative AI Addiction scale
- E14: α ИИ .80, α коррелята .82; заметка: Generative AI Addiction scale
- E15: α ИИ .80, α коррелята .78; заметка: Generative AI Addiction scale

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2, E3, E5, E12, E14, E15: этого числа нет в независимом проходе ИИ по полному тексту — сверьте с таблицей
- E11, E12, E13, E14, E15: шкала ИИ не из списка семейств: напишите, какая это шкала
- в независимом проходе были ещё числа: -0.12, -0.09, -0.03, 0.02, 0.06, 0.07, 0.08, 0.12, 0.13, 0.15, 0.18, 0.23 … — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 131** — Supplement AM11 (suppl. p. 14) — «Note. N=131. Bolded text indicates statistical significance (p<.05).»
- **population: university_students** — p. 11, Section 4.1.1; p. 20, Section 7.1 — «recruited from the same university using identical procedures as Study 2»
- **sampling: convenience** — p. 11, Section 4.1.1 (procedures shared with Study 2); p. 20, Section 7.1 — «Participants were recruited through a local university in Singapore using its online subject pool system.»
- **ai_system: general_chatbot** — p. 14, Table 2 preamble — «Examples of generative AI include tools like Replika, ChatGPT, DALL-E, and other models that generate outputs in response to user inputs.»

**Остальные поля:**
- country: SGP — p. 20-21, Section 7.1; Supplement AM9 (suppl. p. 13) — «A separate sample of 131 participants ... was recruited from the same university using identical procedures as Study 2.»
- data_years: 2025 — p. 21, Section 7.1 — «Data for this study were collected between March to May 2025.»
- design: validation study — p. 20, Section 7 — «Study 5 aimed to evaluate the convergent validity of the Generative AI Dependency Scale with the Generative AI Addiction Scale, as well as its divergent validi…»
- clinical_group: NA — NA — «NA»
- age_mean: 21.60 — p. 20, Section 7.1 — «age in years: M = 21.60, SD = 2.08, range = 18−34»
- age_sd: 2.08 — p. 20, Section 7.1 — «age in years: M = 21.60, SD = 2.08, range = 18−34»
- age_min: 18 — p. 20, Section 7.1 — «range = 18−34»
- age_max: 34 — p. 20, Section 7.1 — «range = 18−34»
- pct_female: 83.21 — Supplement AM9 (suppl. p. 13) — «Sex (% of females) 83.21%»
- mode: online — p. 21, Section 7.1 — «All measures were administered via Qualtrics»
- attention_checks: NR — Section 7.1 — «Participants completed a survey that included demographic questions, the Generative AI Dependency Scale, the Generative AI Addiction Scale, and the Big Five pe…»
- pub_status: preprint — p. 1 — «This manuscript is a prepublication version and may not exactly match the final, authoritative article.»
- language: English — whole text — «Generative Artificial Intelligence Dependency: Scale Development, Validation, and its Motivational, Behavioral, and Psychological Correlates»
- funding_coi: Ministry of Education Academy Research Fund Tier 1 [22-SOSS-SMU-041] and Lee Kong Chian Fund for Research Excellence; COI statement not reported — p. 39, Acknowledgements — «This work was supported by the Ministry of Education Academy Research Fund Tier 1 [22-SOSS-SMU-041] and Lee Kong Chian Fund for Research Excellence.»
- notes: This is the PsyArXiv preprint (v2) of Goh, Hartanto & Majeed (2025), Computers in Human Behavior Reports 20, 100845 (record R3485, not retrieved: publisher page blocked). The preprint is treated as the report of the study. 20 items were given but only the final 11 GAIDS items were scored. Zero-order correlations come from the ResearchBox supplement (AM11). Sample-specific alpha for the GAIDS is not reported; the abstract gives only α = .92–.93 across studies. Generative AI Addiction (Zhou & Zhang, 2024; 3 items, α = .80) is a second AI-dependence measure (ADHOC_R3484_2).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample from a university online subject pool — p. 11, Section 4.1.1; p. 20, Section 7.1 — «Participants were recruited through a local university in Singapore using its online subject pool system.»
2. отклик: **unclear** — No response rate is reported — Section 7.1 — «A separate sample of 131 participants ... was recruited from the same university using identical procedures as Study 2.»
3. валидная шкала зависимости от ИИ: **yes** — The GAIDS is developed and validated in this report (EFA, CFA, invariance, test-retest) — p. 2, Abstract — «the Generative AI Dependency Scale demonstrated strong psychometric properties, including a stable three-factor structure»
4. надёжность шкалы ИИ в выборке: **unclear** — No GAIDS alpha is reported for this sample; the abstract gives a range across studies only. Alpha for the Generative AI Addiction scale = .80 — p. 2 Abstract; p. 20, Section 7.1.1 — «good internal consistency (α = .92–.93)»
5. валидные шкалы коррелятов: **yes** — Big Five measured with the published BFI-2-S — p. 21, Section 7.1.1 — «Participants' personality traits were assessed using the 30-item Big Five Inventory−2−Short (BFI-2-S; Soto & John, 2017).»
6. качество данных: **unclear** — No attention checks or screening are reported for Study 5 — Section 7.1 — «All measures were administered via Qualtrics, and participants were compensated with either course credit or cash.»

Правки:
- 

Проверено: да  # автор в чате 2026-10-18: «проверил, всё гуд»

### ST123-2 · Study 6: US adults via CloudResearch Connect, n = 266 (text: 261)
Отчёты: R3484 (main; PsyArXiv preprint v2 incl. ResearchBox #3834 Additional Materials); R3485 (version of record, not retrieved)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **fomo** · Single-item FoMO scale (Riordan et al., 2020) | pearson | **.21** | **266** | 1 | Supplement AM13 (suppl. p. 16), row 11, col 7 | «11. FoMO / -.25 -.02 -.06 .12 -.12 -.20 / .21 / -.43» |
| E2 | GAIDS · total (T1) | **procrastination** · General Procrastination Scale (GPS-9) | pearson | **.12** | **266** | 1 | Supplement AM13 (suppl. p. 16), row 12, col 7 | «12. Procrastination / -.30 .03 -.06 .13 -.27 -.27 / .12 / -.42» |
| E3 | GAIDS · total (T1) | **self_esteem** · Self-Views scale (Majeed et al., 2023) Self-esteem | pearson | **-.09** | **266** | 1 | Supplement AM13 (suppl. p. 17), row 18, col 7 | «18. Self-esteem / .13 -.01 .06 -.15 .42 .34 / -.09 / .52» |
| E4 | GAIDS · total (T1) | **self_efficacy** · Self-Views scale (Majeed et al., 2023) Generalized self-eff… | pearson | **-.03** | **266** | 1 | Supplement AM13 (suppl. p. 17), row 20, col 7 | «20. Self-efficacy / .11 .03 .06 -.09 .37 .26 / -.03 / .54» |
| E5 | GAIDS · total (T1) | **loneliness** · UCLA Loneliness Scale-8 | pearson | **.14** | **266** | 1 | Supplement AM13 (suppl. p. 17), row 21, col 7 | «21. Loneliness / -.16 -.04 -.06 .07 -.36 -.36 / .14 / -.62» |
| E6 | GAIDS · total (T1) | **wellbeing** · Satisfaction with Life Scale | pearson | **.23** | **266** | 1 | Supplement AM13 (suppl. p. 17), row 22, col 7 | «22. Life satisfaction / .15 -.04 .10 -.13 .56 .43 / .23 / .53» |
| E7 | GAIDS · total (T1) | **wellbeing** · I-PANAS-SF Positive affect | pearson | **.08** | **266** | 1 | Supplement AM13 (suppl. p. 17), row 23, col 7 | «23. Positive affect / .10 -.04 .05 .02 .35 .33 / .08 / .42» |
| E8 | GAIDS · total (T1) | **fomo** · Single-item FoMO scale (Riordan et al., 2020) | latent | **.21** | **266** | 1 | p. 29, Section 8.2.2 | «It was positively associated with FoMO to a medium extent (r = .21, p = .001).» |
| E9 | GAIDS · total (T1) | **procrastination** · General Procrastination Scale (GPS-9) | latent | **.16** | **266** | 1 | p. 29, Section 8.2.3 | «Generative AI dependency was positively correlated with procrastination to a small extent (r = .16, p = .015)» |
| E10 | GAIDS · total (T1) | **self_esteem** · Self-Views scale Self-esteem | latent | **−.09** | **266** | 1 | p. 29, Section 8.2.4 | «No significant associations were found with self-esteem (r = −.09, p = .174)» |
| E11 | GAIDS · total (T1) | **self_efficacy** · Self-Views scale Generalized self-efficacy | latent | **−.03** | **266** | 1 | p. 29, Section 8.2.4 | «self-efficacy (r = −.03, p = .603)» |
| E12 | GAIDS · total (T1) | **loneliness** · UCLA Loneliness Scale-8 | latent | **.15** | **266** | 1 | p. 29, Section 8.2.4 | «A small positive correlation was also observed with loneliness (r = .15, p = .025).» |
| E13 | GAIDS · total (T1) | **wellbeing** · Satisfaction with Life Scale | latent | **.25** | **266** | 1 | p. 29, Section 8.2.4 | «dependency was positively associated with life satisfaction to a medium extent (r = .25, p < .001)» |
| E14 | GAIDS · total (T1) | **wellbeing** · I-PANAS-SF Positive affect | latent | **.06** | **266** | 1 | p. 29, Section 8.2.4 | «positive affect (r = .06, p = .373)» |
| E15 | GAIDS · Cognitive preoccupation (T2) | **fomo** · Single-item FoMO scale | latent | **.23** | **266** | 1 | p. 32, Table 8 | «FoMO .23*** .24*** .12» |
| E16 | GAIDS · Negative consequences (T1) | **fomo** · Single-item FoMO scale | latent | **.24** | **266** | 1 | p. 32, Table 8 | «FoMO .23*** .24*** .12» |
| E17 | GAIDS · Withdrawal (T1) | **fomo** · Single-item FoMO scale | latent | **.12** | **266** | 1 | p. 32, Table 8 | «FoMO .23*** .24*** .12» |
| E18 | GAIDS · Cognitive preoccupation (T2) | **procrastination** · General Procrastination Scale (GPS-9) | latent | **.07** | **266** | 1 | p. 32, Table 8 | «Procrastination .07 .22*** .08» |
| E19 | GAIDS · Negative consequences (T1) | **procrastination** · General Procrastination Scale (GPS-9) | latent | **.22** | **266** | 1 | p. 32, Table 8 | «Procrastination .07 .22*** .08» |
| E20 | GAIDS · Withdrawal (T1) | **procrastination** · General Procrastination Scale (GPS-9) | latent | **.08** | **266** | 1 | p. 32, Table 8 | «Procrastination .07 .22*** .08» |
| E21 | GAIDS · Cognitive preoccupation (T2) | **self_esteem** · Self-Views scale Self-esteem | latent | **-.12** | **266** | 1 | p. 32, Table 8 | «Self-esteem -.12 -.15* .02» |
| E22 | GAIDS · Negative consequences (T1) | **self_esteem** · Self-Views scale Self-esteem | latent | **-.15** | **266** | 1 | p. 32, Table 8 | «Self-esteem -.12 -.15* .02» |
| E23 | GAIDS · Withdrawal (T1) | **self_esteem** · Self-Views scale Self-esteem | latent | **.02** | **266** | 1 | p. 32, Table 8 | «Self-esteem -.12 -.15* .02» |
| E24 | GAIDS · Cognitive preoccupation (T2) | **self_efficacy** · Self-Views scale Generalized self-efficacy | latent | **-.07** | **266** | 1 | p. 32, Table 8 | «Self-efficacy -.07 -.09 .06» |
| E25 | GAIDS · Negative consequences (T1) | **self_efficacy** · Self-Views scale Generalized self-efficacy | latent | **-.09** | **266** | 1 | p. 32, Table 8 | «Self-efficacy -.07 -.09 .06» |
| E26 | GAIDS · Withdrawal (T1) | **self_efficacy** · Self-Views scale Generalized self-efficacy | latent | **.06** | **266** | 1 | p. 32, Table 8 | «Self-efficacy -.07 -.09 .06» |
| E27 | GAIDS · Cognitive preoccupation (T2) | **loneliness** · UCLA Loneliness Scale-8 | latent | **.15** | **266** | 1 | p. 32, Table 8 | «Loneliness .15* .18** .06» |
| E28 | GAIDS · Negative consequences (T1) | **loneliness** · UCLA Loneliness Scale-8 | latent | **.18** | **266** | 1 | p. 32, Table 8 | «Loneliness .15* .18** .06» |
| E29 | GAIDS · Withdrawal (T1) | **loneliness** · UCLA Loneliness Scale-8 | latent | **.06** | **266** | 1 | p. 32, Table 8 | «Loneliness .15* .18** .06» |
| E30 | GAIDS · Cognitive preoccupation (T2) | **wellbeing** · Satisfaction with Life Scale | latent | **.13** | **266** | 1 | p. 32, Table 8 | «Life satisfaction .13 .16* .34***» |
| E31 | GAIDS · Negative consequences (T1) | **wellbeing** · Satisfaction with Life Scale | latent | **.16** | **266** | 1 | p. 32, Table 8 | «Life satisfaction .13 .16* .34***» |
| E32 | GAIDS · Withdrawal (T1) | **wellbeing** · Satisfaction with Life Scale | latent | **.34** | **266** | 1 | p. 32, Table 8 | «Life satisfaction .13 .16* .34***» |
| E33 | GAIDS · Cognitive preoccupation (T2) | **wellbeing** · I-PANAS-SF Positive affect | latent | **.07** | **266** | 1 | p. 32, Table 8 | «Positive affect .07 -.03 .14*» |
| E34 | GAIDS · Negative consequences (T1) | **wellbeing** · I-PANAS-SF Positive affect | latent | **-.03** | **266** | 1 | p. 32, Table 8 | «Positive affect .07 -.03 .14*» |
| E35 | GAIDS · Withdrawal (T1) | **wellbeing** · I-PANAS-SF Positive affect | latent | **.14** | **266** | 1 | p. 32, Table 8 | «Positive affect .07 -.03 .14*» |

- E1: α ИИ NR, α коррелята NA (single item); заметка: Value from the supplement; the text gives n = 261, the tables N = 266
- E2: α ИИ NR, α коррелята .80; заметка: Value from the supplement
- E3: α ИИ NR, α коррелята .87; заметка: Value from the supplement; 2-item subscale with momentary ('Right now') wording
- E4: α ИИ NR, α коррелята .80; заметка: Value from the supplement; 2-item subscale with momentary wording
- E5: α ИИ NR, α коррелята .89; заметка: Value from the supplement
- E6: α ИИ NR, α коррелята .94; заметка: Value from the supplement
- E7: α ИИ NR, α коррелята .82; заметка: Value from the supplement; a second wellbeing indicator (with SWLS) in the same sample
- E8: α ИИ NR, α коррелята NA (single item); заметка: Standardized covariance between the second-order latent GAIDS factor and the correlate (CFA)
- E9: α ИИ NR, α коррелята .80; заметка: CFA standardized covariance
- E10: α ИИ NR, α коррелята .87; заметка: CFA standardized covariance
- E11: α ИИ NR, α коррелята .80; заметка: CFA standardized covariance
- E12: α ИИ NR, α коррелята .89; заметка: CFA standardized covariance
- E13: α ИИ NR, α коррелята .94; заметка: CFA standardized covariance
- E14: α ИИ NR, α коррелята .82; заметка: CFA standardized covariance
- E15: α ИИ NR, α коррелята NA (single item); заметка: Table 8 values are CFA standardized covariances (separate subscale model)
- E16: α ИИ NR, α коррелята NA (single item); заметка: CFA subscale model
- E17: α ИИ NR, α коррелята NA (single item); заметка: The text says FoMO correlated with 'all three subscales', but the table value is non-significant
- E18: α ИИ NR, α коррелята .80; заметка: CFA subscale model
- E19: α ИИ NR, α коррелята .80; заметка: The text gives p = .001; the table marks it ***
- E20: α ИИ NR, α коррелята .80; заметка: CFA subscale model
- E21: α ИИ NR, α коррелята .87; заметка: CFA subscale model
- E22: α ИИ NR, α коррелята .87; заметка: CFA subscale model
- E23: α ИИ NR, α коррелята .87; заметка: CFA subscale model
- E24: α ИИ NR, α коррелята .80; заметка: CFA subscale model
- E25: α ИИ NR, α коррелята .80; заметка: CFA subscale model
- E26: α ИИ NR, α коррелята .80; заметка: CFA subscale model
- E27: α ИИ NR, α коррелята .89; заметка: CFA subscale model
- E28: α ИИ NR, α коррелята .89; заметка: CFA subscale model
- E29: α ИИ NR, α коррелята .89; заметка: CFA subscale model
- E30: α ИИ NR, α коррелята .94; заметка: CFA subscale model
- E31: α ИИ NR, α коррелята .94; заметка: CFA subscale model
- E32: α ИИ NR, α коррелята .94; заметка: CFA subscale model
- E33: α ИИ NR, α коррелята .82; заметка: CFA subscale model
- E34: α ИИ NR, α коррелята .82; заметка: CFA subscale model
- E35: α ИИ NR, α коррелята .82; заметка: CFA subscale model

**⚠ Проверка скриптом (обратите внимание):**
- E5, E35: этого числа нет в независимом проходе ИИ по полному тексту — сверьте с таблицей
- в независимом проходе были ещё числа: 0.19, 0.31 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 266** — p. 32, Table 8 note; Supplement AM13 note — «Note. N = 266. *p < .05; **p < .01; ***p < .001.»
- **population: general_adults** — p. 24, Section 8 — «correlates of generative AI dependency in a sample of adults from the United States»
- **sampling: quota or online panel** — p. 24, Section 8.1.1 — «Study 6 recruited a total of 261 participants ... via Connect by CloudResearch.»
- **ai_system: general_chatbot** — p. 24, Section 8.1.1; p. 14, Table 2 preamble — «prior experience using generative AI tools (e.g., started a conversation, used it to generate images) at least once»

**Остальные поля:**
- country: USA — p. 24, Section 8; Supplement AM12 (suppl. p. 15) — «Nationality (% of United States citizen) 100%»
- data_years: 2025 — p. 24, Section 8.1.1 — «Data for this study were collected between April to May 2025.»
- design: validation study — p. 7, Section 1.3; p. 24, Section 8 — «Study 6 investigated the associations between generative AI dependency and a range of motivational, behavioral, and psychological outcomes»
- clinical_group: NA — NA — «NA»
- age_mean: 37.01 — p. 24, Section 8.1.1 — «age in years: M = 37.01, SD = 12.22, range = 18−75»
- age_sd: 12.22 — p. 24, Section 8.1.1 — «age in years: M = 37.01, SD = 12.22, range = 18−75»
- age_min: 18 — p. 24, Section 8.1.1 — «range = 18−75»
- age_max: 75 — p. 24, Section 8.1.1 — «range = 18−75»
- pct_female: 42.48 — Supplement AM12 (suppl. p. 15) — «Sex (% of females) 42.48%»
- mode: online — p. 24, Section 8.1.1 — «Data were collected online using Qualtrics, and participants received cash compensation.»
- attention_checks: yes — p. 24, Section 8.1.1 — «a bot-detection screening at the start of the survey. Participants who did not meet eligibility criteria were excluded from the final dataset.»
- pub_status: preprint — p. 1 — «This manuscript is a prepublication version and may not exactly match the final, authoritative article.»
- language: English — whole text — «Study 6: Correlates of the Generative AI Dependency Scale»
- funding_coi: Ministry of Education Academy Research Fund Tier 1 [22-SOSS-SMU-041] and Lee Kong Chian Fund for Research Excellence; COI statement not reported — p. 39, Acknowledgements — «This work was supported by the Ministry of Education Academy Research Fund Tier 1 [22-SOSS-SMU-041] and Lee Kong Chian Fund for Research Excellence.»
- notes: This is the PsyArXiv preprint (v2) of Goh, Hartanto & Majeed (2025), Computers in Human Behavior Reports 20, 100845 (record R3485, not retrieved: publisher page blocked). The preprint is treated as the report of the study. Pre-registered. Pearson correlations come from the supplement (AM13). The latent correlations are standardized covariances from the CFA: the second-order GAIDS factor in the text and Figure 4, and the subscale factors in Table 8 (separate model). Sample-specific GAIDS alpha is not reported. Negative affect, BMPN needs, cognitive failure, task performance, indecisiveness, cr…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Crowdsourcing panel (CloudResearch Connect) — p. 24, Section 8.1.1 — «Study 6 recruited a total of 261 participants ... via Connect by CloudResearch.»
2. отклик: **unclear** — No response rate is reported — p. 24, Section 8.1.1 — «Participants who did not meet eligibility criteria were excluded from the final dataset.»
3. валидная шкала зависимости от ИИ: **yes** — The GAIDS is developed and validated in this report — p. 24, Section 8.1.2 — «The 11-item Generative AI Dependency Scale, which was developed and refined in previous studies, was used.»
4. надёжность шкалы ИИ в выборке: **unclear** — No GAIDS alpha is reported for this sample; the abstract gives a range across studies only — p. 2, Abstract — «good internal consistency (α = .92–.93)»
5. валидные шкалы коррелятов: **yes** — All extracted correlates use published instruments: single-item FoMO (Riordan 2020), GPS-9, Self-Views scale (Majeed 2023, preprint), ULS-8, SWLS, I-PANAS-SF. Note that FoMO is a single item and the Self-Views subscales… — pp. 25-26, Section 8.1.2 — «Fear of Missing Out was assessed using a single-item scale (Riordan et al., 2020).»
6. качество данных: **yes** — Bot-detection screening, with exclusion of ineligible respondents — p. 24, Section 8.1.1 — «a bot-detection screening at the start of the survey. Participants who did not meet eligibility criteria were excluded from the final dataset.»

Правки:
- 

Проверено: да  # автор в чате 2026-10-18: «проверил, всё гуд»

