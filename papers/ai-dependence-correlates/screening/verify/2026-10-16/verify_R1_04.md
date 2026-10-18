# Проверка с метками ИИ, часть 4

Записи 451–600 из 837, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: количественное исследование людей, где измерена зависимость от ИИ (шкала зависимости, аддикции, проблемного использования, over-reliance или эмоциональной зависимости) и может найтись её корреляция хотя бы с одним нашим коррелятом |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
| `-1` | исключить: обзор, редакционная статья, комментарий, теоретическая работа |
| `-2` | исключить: качественное или не эмпирическое исследование без количественной меры зависимости |
| `-3` | исключить: нет меры зависимости от ИИ: только частота использования, принятие, доверие, грамотность, технострес, страх ИИ — или over-reliance только как поведение в эксперименте |
| `-4` | исключить: среди измеренных конструктов нет ни одного нашего коррелята |
| `-5` | исключить: ИИ как инструмент (выявляет или лечит зависимость, анализирует данные), социальные роботы, «dependence» в другом смысле |
| `-6` | исключить: не по теме или другое — напишите почему |

Пример: `**Решение:** -3 только частота использования`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Наши корреляты:** депрессия, тревожность, стресс, одиночество, социальная тревожность, самооценка, прокрастинация; а также дистресс, благополучие, самоэффективность, самоконтроль, импульсивность, FoMO, проблемное использование смартфона, интернета и соцсетей, Большая пятёрка, тревожная и избегающая привязанность, скука, осознанность, сон, учебный стресс, мотивы бегства, социальная поддержка, тревога перед ИИ. Корреляции обычно лежат в таблице, о которой аннотация молчит: если зависимость от ИИ измерена шкалой в выборке людей, а конструкты в аннотации не перечислены, — `?`. Подробно — протокол, §8 и §13.

---

### 451 · R2656

**Trusting the AI, Crafting the Show: Algorithmic Dependence and Human–AI Collaboration in Variety-Show Post-Production Across Chinese OTT Platforms**

2026 · International Journal of Human-Computer Interaction · article, journal-article · en · https://doi.org/10.1080/10447318.2026.2705666

Chinese OTT variety-show post-production requires balancing creativity, technical execution, regulations, and platform algorithms under tight schedules. Drawing on UTAUT2, this study incorporates AI trust (AITR), AI anxiety (AIA), and algorithmic dependence (AD) in an explanatory sequential mixed-methods design. PLS-SEM of 443 responses shows that performance expectancy and effort expectancy enhance AITR; AITR promotes behavioral intention, which facilitates use behavior; use behavior then contributes to AD. Social influence and hedonic motivation increase behavioral intention, while facilitating conditions affect use behavior. AIA weakens the performance expectancy–AITR relationship but strengthens the effort expectancy–AITR relationship. Twenty interviews indicate AITR is grounded in interpretability, controllability, and verifiability, with controllability especially critical in fast-paced production. Trust and resistance may coexist when ease of use is perceived to threaten professional value. The study extends UTAUT2 beyond adoption by positioning AD as a post-adoption outcome and informs deployment compatible with human judgment, responsibility, and occupational sustainability.

**ИИ:** ? · обе модели · мера зависимости неясна · Algorithmic dependence on AI tools measured with AI anxiety via PLS-SEM; unclear whether the AI is generative or conversational, or just platform algorithms.

**Решение:** =

---

### 452 · R2658

**When cognitive offloading becomes dependence: how AI dependence mediates the pathway from academic stress to burnout and anxiety.**

2026 · BMC psychology · article, journal article, journalarticle · eng · https://doi.org/10.1186/s40359-026-04911-w

Abstract Although generative AI tools are increasingly used in college students’ academic activities, their role in stress-related maladaptive coping remains unclear. This study focuses specifically on maladaptive AI dependence as a potential mediator linking academic stress to academic burnout and anxiety. A total of 1,623 college students completed an online survey using the Academic Stress Scale, the AI Dependence Scale, the General Self-Efficacy Scale, the Academic Burnout Scale, and the GAD-7. PROCESS Model 6 was used to examine direct, indirect, and sequential mediation effects separately for academic burnout and anxiety. The results showed that academic stress positively predicted both academic burnout and anxiety. Sequential mediation analyses revealed that academic stress was associated with increased AI dependence, which may reduce students’ mastery experiences and encourage reliance on external support, thereby undermining self-efficacy and ultimately contributing to higher levels of burnout and anxiety. These findings suggest that excessive reliance on AI as a stress-coping strategy may weaken students’ sense of competence and increase their vulnerability to academic burnout and anxiety. Educational interventions should therefore promote reflective and autonomy-supportive AI use, positioning AI as a learning scaffold rather than a substitute for students’ own cognitive engagement.

**ИИ:** + · обе модели · назван коррелят · Survey of 1,623 students using the AI Dependence Scale alongside academic stress, self-efficacy, burnout and anxiety (GAD-7).

**Решение:** =

---

### 453 · R2660

**How workplace AI feedback shapes AI dependency: A randomized controlled trial on the moderating role of workplace social support among Japanese office workers**

2026 · Computers in Human Behavior Artificial Humans · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.chbah.2026.100365

AI dependency—habitual, automatic AI use accompanied by diminished autonomy—is a growing concern in the workplace, yet the conditions under which it develops remain poorly understood. Two competing pathways have been proposed. Users with limited social support from colleagues may compensate for this deficit by depending on AI (the compensatory pathway ), or users with abundant support may be better positioned to leverage AI interaction, thereby fostering dependency (the enhancement pathway ). To test these pathways, we analyzed data from a 5-day randomized controlled trial with 294 Japanese office workers. Participants engaged in daily work-reflection sessions with an AI chatbot. Depending on condition, the chatbot delivered positive feedback emphasizing strengths, negative feedback highlighting areas for improvement, or no work-related feedback (control). AI dependency was measured one week after the final session, revealing two qualitatively distinct patterns based on feedback valence. Positive feedback increased AI dependency regardless of workplace social support levels, suggesting that positive reinforcement from AI functions as a general pathway to dependency. In contrast, negative feedback did not increase AI dependency overall but did so selectively among participants with abundant social support, which is consistent with the enhancement pathway. These findings are qualified by the short-term, self-reported outcome, the exploratory and non-preregistered analysis, the modest size of the focal interaction, and the crowdsourced Japanese sample, which limits their generalizability. Within these bounds, they indicate that AI dependency is not simply a function of AI characteristics but emerges from the interaction between AI feedback and employees' existing workplace relationships.

**ИИ:** + · обе модели · назван коррелят · RCT with a self-report AI chatbot dependency outcome and workplace social support as moderator; social support is a correlate of interest.

**Решение:** =

---

### 454 · R2661

**Emotional dependence on AI chatbots: Development and Validation of the AIED Scale**

2026 · PsyArXiv · article, preprint, posted-content · und · https://doi.org/10.31234/osf.io/yhetz_v1

As large language model (LLM) chatbots become increasingly embedded in adolescents’ daily lives, concerns have emerged about users’ emotional reliance on these systems. Existing measures of AI chatbot dependence primarily assess instrumental or problem-focused use and do not adequately capture emotional dependence. This study developed and validated the AI Chatbot Emotional Dependence (AIED) Scale, a brief measure of adolescents’ tendency to rely on AI chatbots for comfort, emotional relief, and perceived understanding. A total of 5,855 Chinese adolescents with complete data were randomly divided into an exploratory subsample (n=2,927) and a confirmatory subsample (n=2,928). Exploratory factor analysis supported a one-factor, five-item solution after removal of one poorly performing item. The retained factor explained 69.07% of the variance, with loadings ranging from .778 to .864. Confirmatory factor analysis supported the unidimensional structure, with good overall fit (CFI=.98, TLI=.95, SRMR=.02). The scale showed good internal consistency (α=.89), strong convergent validity, and a substantial positive correlation with a general AI chatbot dependence measure (r=.67,p&amp;lt;.001). Multi-group analyses supported configural, metric, and scalar invariance across sex and educational stage. The AIED is a brief, reliable, and valid instrument for assessing adolescents’ emotional dependence on AI chatbots.

**ИИ:** + · обе модели · валидация шкалы · This preprint develops and validates a scale for adolescents' emotional dependence on AI chatbots; its convergent validity data may include correlates of interest.

**Решение:** =

---

### 455 · R2666

**Too much, too little, or just right? The inverted-U relationship between human-AI collaboration modes and eudaimonic well-being.**

2026 · Frontiers in psychology · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyg.2026.1747252

As human-AI collaboration becomes more pervasive, optimizing the distribution of decision-making authority between humans and AI has become a fundamental concern in human-centered AI design. The impacts of different human-AI collaboration modes (human-dominant, human-AI collaboration, and AI-dominant) on users' eudaimonic well-being, as well as the underlying psychological transmission mechanisms, remain poorly understood. Grounded in self-determination theory, we propose a serial mediation framework linking human-AI collaboration modes to eudaimonic well-being via the sequential mechanisms of AI dependence and perceived autonomy. This framework is rigorously investigated through two scenario-based experiments in the domains of autonomous driving and online shopping, with a particular focus on the differential effects of collaboration modes and the underlying psychological transmission chain. The results reveal that human-AI collaboration mode exhibits an inverted U-shaped relationship with eudaimonic well-being; the level of individuals' eudaimonic well-being under the human-AI collaboration mode is significantly higher than that under the human-dominant and AI-dominant modes. Additionally, AI dependence and perceived autonomy play a significant serial mediating role in the above relationship. This study constructs and validates the psychological transmission mechanism of how human-AI collaboration affects deep-level well-being, expands the application scope of self-determination theory in human-AI collaboration scenarios, and provides optimization guidelines for AI product design and user experience management. These findings contribute to the design of human-centered AI systems that simultaneously promote technological advancement and human well-being.

**ИИ:** ? · обе модели · другое · Experiments measured AI dependence (mediator) and eudaimonic well-being, but the AI was autonomous driving/shopping, not clearly conversational AI.

**Решение:** =

---

### 456 · R2676

**Pengaruh Ketergantungan Chatgpt dan Frekuensi Penggunaan ChatGPT terhadap Kepercayaan Diri pada Mahasiswa Akuntansi**

2026 · Journal Economic Insights. · article, journalarticle, review · und · https://doi.org/10.51792/301vf370

This study aims to analyze the effect of ChatGPT dependency and the frequency of ChatGPT usage on the self-confidence of accounting students at Universitas Selamat Sri Kendal. This research uses a quantitative approach with a survey method. Data were collected through questionnaires distributed to 56 accounting students who had used ChatGPT in academic activities. The data were analyzed using multiple linear regression with the assistance of statistical software. The results show that ChatGPT dependency has a negative and significant effect on students’ self-confidence. Meanwhile, the frequency of ChatGPT usage does not have a significant effect on students’ self-confidence. Simultaneously, ChatGPT dependency and the frequency of ChatGPT usage have a significant effect on students’ self-confidence. The coefficient of determination value of 0.548 indicates that 54.8% of the variation in students’ self-confidence can be explained by these two variables, while the remaining is influenced by other factors outside the research model. The findings suggest that the use of artificial intelligence technology in learning should be applied wisely to avoid excessive dependency that may affect students' self-confidence.

**ИИ:** разошлись — Opus ? (другое: Survey that measured ChatGPT dependency against self-confidence, which is close to self-esteem/self-efficacy but not exactly a listed correlate.); Sonnet + (назван коррелят: Quantitative survey of ChatGPT dependency and self-confidence (self-esteem-related) among accounting students, using regression.)

**Решение:** ?

---

### 457 · R2683

**Understanding compulsive generative AI use among college students through a dual system perspective: An integrated SEM-ANN-NCA approach.**

2026 · Acta psychologica · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.actpsy.2026.107701

The powerful capabilities of generative artificial intelligence (GAI) have propelled its adoption in higher education in recent years. GAI offers considerable benefits, but its rapid integration has prompted growing concerns regarding compulsive GAI use, characterised by persistent and uncontrollable engagement. Compulsive GAI use has been linked to adverse psychological and academic outcomes, underscoring the importance of understanding the factors associated with this maladaptive use. However, most existing studies have focused on GAI's functionalities and how its applications support various domains (e.g., education), as well as factors associated with the adoption and continued use of GAI. In contrast, much less attention has been given to identifying the antecedents of compulsive GAI use. Drawing on Dual-System Theory (DST), this study developed a model to examine whether GAI features (intelligence, interactivity, and personalisation), perceived usefulness, impulsive urge, habit, and impulsivity are associated with compulsive GAI use. Data were collected from 593 college students from a Chinese university and analysed using an approach integrating Structural Equation Modelling (SEM), Artificial Neural Network (ANN), and Necessary Condition Analysis (NCA). PLS-SEM results showed that perceived interactivity and personalization were positively associated with perceived usefulness, which was further associated with impulsive urge and habit. Impulsive urge and habit were also associated with compulsive GAI use. ANN results revealed that habit had the highest normalised importance, followed by impulsivity and impulsive urge. NCA identified perceived interactivity, perceived usefulness, habit, and impulsive urge as necessary conditions for compulsive GAI use to emerge. This study provided significant practical insights for developing interventions to reduce compulsive GAI use among college students.

**ИИ:** + · обе модели · назван коррелят · Survey of 593 students that measured compulsive GAI use alongside impulsivity, a correlate of interest, in a PLS-SEM model.

**Решение:** =

---

### 458 · R2687

**AI anxiety and AI dependence among undergraduates: a moderated mediation model of AI self-efficacy and AI literacy.**

2026 · Frontiers in psychology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyg.2026.1884382

Background The rapid integration of Artificial Intelligence (AI) in higher education offers transformative learning potential but has concurrently triggered psychological challenges, specifically AI anxiety and AI dependence. While these phenomena are increasingly prevalent, the psychological mechanisms converting affective strain into behavioral reliance remain underexplored. Grounded in Cognitive Behavioral Theory and Conservation of Resources Theory, this study investigates the relationship between AI anxiety and AI dependence among undergraduates. Specifically, it examines whether AI self-efficacy mediates this relationship and whether AI literacy acts as a boundary condition moderating these pathways. Methods A cross-sectional survey was conducted with 400 undergraduates recruited via stratified sampling from a normal university in Southwest China. Participants completed validated scales measuring AI anxiety, AI self-efficacy, AI literacy, and AI dependence. Confirmatory factor analysis was performed to verify instrument validity. Hypotheses were tested using the PROCESS macro (Models 4 and 8) to analyze mediation and moderated mediation effects, utilizing bootstrapping techniques with 5,000 resamples to determine the statistical significance of direct and indirect effects. Results The analysis revealed a significant positive association between AI anxiety and AI dependence. AI self-efficacy was found to partially mediate this relationship, indicating that anxiety exacerbates dependence by eroding students’ confidence in their capabilities. Furthermore, AI literacy served as a significant moderator. Results indicated that the negative impact of AI anxiety on AI self-efficacy was stronger for students with higher AI literacy, suggesting that high literacy may sensitize students to competency gaps under emotional strain. AI literacy did not moderate the direct relationship between anxiety and dependence. Conclusion This study identifies AI dependence as a maladaptive coping response to AI anxiety, driven by diminished AI self-efficacy. The findings challenge the assumption that literacy acts solely as a protective buffer, revealing that without emotional regulation, high literacy may intensify the erosion of self- confidence during anxious states. To mitigate maladaptive dependence, higher education institutions should move beyond technical training to adopt holistic strategies. These should include psychological support to build resilience, mastery experiences to foster self-efficacy, and comprehensive curricula that address the emotional and cognitive dimensions of human-AI interaction. </jats:sec

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey linking AI dependence to AI anxiety and AI self-efficacy, which are both correlates of interest.

**Решение:** =

---

### 459 · R2691

**AI-TPACK and AI use intention: the mediating role of self-efficacy and the moderating role of AI dependence among university teachers**

2026 · Interactive Learning Environments · article, journalarticle, journal-article · en · https://doi.org/10.1080/10494820.2026.2702587

Although Artificial Intelligence (AI) is reshaping higher education, the psychological mechanisms linking university teachers’ AI-related professional knowledge to AI use intention remain underexplored. Grounded in Social Cognitive Theory and the AI-TPACK framework, this study examined a moderated mediation model among 407 teachers at a normal university in southwestern China via stratified random sampling. PROCESS macro analyses indicated that AI-TPACK significantly predicted AI use intention (β = .39, p < .001), and that AI self-efficacy partially mediated this relationship (indirect effect = 0.087, 95% CI [0.054, 0.126]), accounting for 29.60% of the total effect. AI dependence significantly moderated both the first-stage path to AI self-efficacy (b = −0.10, p = .027) and the direct path to AI use intention (b = −0.08, p = .033), with the index of moderated mediation reaching −0.027 (95% CI [−0.054, −0.003]). One-way ANOVA further revealed significant disciplinary differences in AI-TPACK (ηp2 = .162), AI self-efficacy (ηp2 = .101), and AI use intention (ηp2 = .045), with Natural Sciences teachers scoring highest, whereas AI dependence remained stable across disciplines. These findings clarify how AI-TPACK shapes AI use intention through confidence and reflective engagement, and inform discipline-sensitive faculty development for AI-enhanced learning environments.

**ИИ:** + · обе модели · назван коррелят · A survey of 407 teachers measured AI dependence as a moderator alongside AI self-efficacy, which should allow a correlation to be pulled out.

**Решение:** =

---

### 460 · R2692

**Antecedents and Consequences of Generative Artificial Intelligence Addiction Among Chinese College Students: A Self-Regulated Learning Perspective**

2026 · SAGE Open · journalarticle, review, article · en · https://doi.org/10.1177/21582440261477182

The rapid diffusion of generative artificial intelligence (GAI) in higher education has generated both substantial learning benefits and growing concerns regarding students’ excessive and habitual use. Building on self-regulated learning theory, this study develops and tests an integrative research model comprising 10 hypotheses to examine the antecedents and consequences of GAI addiction among 1,022 Chinese college students. A self-administered online survey was conducted in China, and the data were analyzed using structural equation modeling (SEM). Results supported seven of the 10 hypotheses, revealing that GAI self-efficacy, GAI skill anxiety, peer pressure, and social identity were all significantly and positively associated with students’ GAI addiction. Unexpectedly, GAI replacement anxiety and need for cognition also positively related to GAI addiction, while GAI literacy showed no significant association. GAI addiction was further positively associated with creativity impact, teamwork performance impact, and decision reliance. Multi-group analysis further revealed that goal orientation significantly moderated several of these relationships, with cognitively driven pathways being stronger among low goal-oriented students, whereas identity-driven mechanisms were more salient among high goal-oriented students. This research contributes to the emerging literature on GAI-related behaviors by advancing a comprehensive, multi-factor perspective on GAI addiction and offering nuanced insights into its implications for higher-order learning outcomes in higher education.</jats:p

**ИИ:** + · обе модели · назван коррелят · SEM survey of GAI addiction with GAI self-efficacy and AI-related anxiety (skill/replacement anxiety) as antecedents; correlation table likely.

**Решение:** =

---

### 461 · R2695

**Latent Profiles of Problematic Smartphone Use and Their Associations With AI Chatbot Dependence: A Multi-Group Mediation Analysis**

2026 · Elsevier BV · article, posted-content, preprint · und · https://doi.org/10.2139/ssrn.6503347

As generative artificial intelligence becomes increasingly embedded in everyday and educational contexts, scholarly concern has shifted from initial acceptance of AI chatbots to the risk that sustained use may evolve into dependence. However, little is known about whether individuals with different levels of problematic smartphone use (PSU) exhibit distinct pathways toward AI chatbot dependence. Based on the AI device use acceptance (AIDUA) framework, this study surveyed 538 participants recruited through an online platform to examine whether latent PSU profiles differ in their levels of AI chatbot dependence and in the cognitive-affective pathways associated with such dependence. The results indicate that: (1) Latent profile analysis identified three PSU profiles that primarily reflected symptom severity: low-symptom PSU (16%), moderate-symptom PSU (46%), and high-symptom PSU (38%); significant differences in AI chatbot dependence levels were observed across these PSU subcategories; (2) Emotional experience mediated the associations of hedonic motivation, performance expectancy, and effort expectancy with AI chatbot dependence; (3) Within-group mediation patterns varied across PSU profiles. In the moderate-PSU group, emotional experience emerged as a relatively salient within-group mechanism, whereas in the high-PSU group, performance expectancy played a more central role. Formal between-group comparisons further indicated that cross-group heterogeneity was primarily concentrated in the performance expectancy pathway. These findings extend research on AI chatbot use beyond acceptance processes to dependence outcomes, clarify heterogeneity across individuals in the link between PSU and AI chatbot dependence, and provide a basis for more differentiated risk assessment and intervention strategies.

**ИИ:** + · обе модели · назван коррелят · Survey (n=538) linking problematic smartphone use profiles to AI chatbot dependence; PSU is a named correlate of interest.

**Решение:** =

---

### 462 · R2696

**Problematic Smartphone Use and AI Chatbot Dependence: A Cross-Sectional Study Using Latent Profile and Continuous-Risk Analyses**

2026 · Elsevier BV · article, posted-content, preprint · und · https://doi.org/10.2139/ssrn.6788785

As generative artificial intelligence becomes increasingly embedded in everyday, educational, and work-related contexts, increasing attention has been directed to dependence-related forms of AI chatbot use. Problematic smartphone use (PSU) may reflect broader dysregulated digital engagement and may therefore be relevant to understanding dependence-related AI chatbot use. However, little is known about whether PSU is associated with AI chatbot dependence or whether AI-related evaluative factors show different association patterns across PSU severity profiles. Guided by the I-PACE model, data from 538 AI chatbot users were analyzed using latent profile analysis and a supplementary continuous-risk model. Latent profile analysis yielded three severity-based PSU groups: low-symptom PSU (16%), moderate-symptom PSU (46%), and high-symptom PSU (38%). These groups formed an ordered severity gradient rather than distinct symptom configurations, and AI chatbot dependence differed across them. Emotional experience was implicated in several significant statistical indirect associations between AI-use evaluations and AI chatbot dependence. Profile-specific analyses suggested possible differences across PSU groups; however, formal between-group evidence was limited to the performance expectancy pathway. The supplementary continuous-risk model supported the positive association between PSU and AI chatbot dependence but did not reproduce the profile-specific performance expectancy finding. These findings suggest that dependence-related AI chatbot use may be situated within broader patterns of dysregulated digital engagement, although the observed profile differences primarily reflected severity rather than distinct typological patterns. Given the cross-sectional self-report design, the findings should be interpreted cautiously and require longitudinal, multi-method, and more diverse-sample replication.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey of 538 users; reports a positive association between problematic smartphone use and AI chatbot dependence.

**Решение:** =

---

### 463 · R2697

**Problematic smartphone use and AI chatbot dependence: A cross-sectional study using latent profile and dimensional analyses**

2026 · Computers in Human Behavior Reports · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.chbr.2026.101337

ABSTRACT As generative artificial intelligence becomes increasingly embedded in everyday, educational, and work-related contexts, increasing attention has been directed to dependency-related forms of AI chatbot use. Problematic smartphone use (PSU) may reflect broader dysregulated digital engagement and may therefore be relevant to understanding dependency-related AI chatbot use. However, little is known about whether PSU is associated with AI chatbot dependency or whether AI-related evaluative factors show different association patterns across PSU severity profiles. Guided by the I-PACE model, data from 538 AI chatbot users were analyzed using latent profile analysis and a supplementary continuous-PSU model. Latent profile analysis yielded three severity-based PSU groups: low-symptom PSU (16%), moderate-symptom PSU (46%), and high-symptom PSU (38%). These groups formed an ordered severity gradient rather than distinct symptom configurations, and AI chatbot dependency differed across them. Emotional experience was implicated in several significant statistical indirect associations between AI-use evaluations and AI chatbot dependency. Differences in the observed associations across PSU severity groups were explored; however, formal between-group evidence was limited to the association between performance expectancy and AI chatbot dependency. The supplementary continuous-PSU model supported the positive association between PSU and AI chatbot dependency, but did not reproduce the profile-specific performance expectancy finding. Accordingly, this profile-specific finding should be interpreted as exploratory. These findings suggest that dependency-related AI chatbot use may be situated within broader patterns of dysregulated digital engagement, although the observed profile differences primarily reflected severity rather than distinct typological patterns. Given the cross-sectional self-report design, the findings should be interpreted cautiously and require longitudinal, multi-method, and more diverse-sample replication.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey (N=538) relating problematic smartphone use to AI chatbot dependency; correlate of interest named.

**Решение:** =

---

### 464 · R2699

**Scaffolds or crutches? Examining the relationships between artificial intelligence dependency and academic resilience in higher education**

2026 · Assessment in Education Principles Policy and Practice · journalarticle, article · en · https://doi.org/10.1080/0969594x.2026.2736632

As generative artificial intelligence (AI) becomes increasingly embedded in higher education, an important question is whether such support provides productive scaffolding or fosters maladaptive dependency. This study examines the relationships among AI dependency, academic self-efficacy, and academic resilience, and whether perceived feedback elaborativeness and latency moderate the dependency–self-efficacy relationship. A three-wave lagged survey was conducted with 892 first-year university students in China over one academic semester. Higher AI dependency was associated with lower academic self-efficacy, which in turn was positively associated with academic resilience. Academic self-efficacy accounted for a significant indirect association between dependency and resilience. The negative dependency–self-efficacy association was weaker when students perceived feedback as more elaborative and as allowing more time for independent thought before assistance. Responsible use of AI in education calls for feedback design that supports independent thinking and preserves learner agency.

**ИИ:** + · обе модели · назван коррелят · Three-wave survey linking generative AI dependency to academic self-efficacy, which is a correlate of interest, in 892 students.

**Решение:** =

---

### 465 · R2702

**The Influence Mechanism of Critical Thinking in the Context of Generative Artificial Intelligence**

2026 · Advances in Psychology · article · https://doi.org/10.12677/ap.2026.1610466

Objective: The widespread adoption of generative artificial intelligence (AI) is transforming the cognitive and learning styles of college students, and its impact on critical thinking is increasingly 吴欣仪 等

**ИИ:** ? · обе модели · мера зависимости неясна · Abstract truncated; generative AI and critical thinking in students may involve an AI dependence measure, but the constructs measured aren't clear.

**Решение:** =

---

### 466 · R2703

**The serial mediating roles of AI self-efficacy and academic procrastination in the association between AI literacy and AI dependence among Chinese undergraduates.**

2026 · Australian journal of psychology · journal article, journalarticle, article · eng · https://doi.org/10.1080/00049530.2026.2721637

ABSTRACT Objective Generative artificial intelligence is now embedded in university learning, but the psychological pathways linking AI literacy with AI dependence remain unclear. This study examined whether AI self-efficacy and academic procrastination mediate the association between AI literacy and AI dependence among Chinese undergraduates. Method A total of 417 Chinese undergraduate students aged 18–24 years completed measures of AI literacy, AI self-efficacy, academic procrastination and AI dependence. This study tested common method bias, estimated descriptive statistics and Pearson correlations, examined multicollinearity, conducted robustness checks and estimated a serial mediation model with PROCESS Model 6. Results AI literacy was negatively associated with AI dependence (r = –.283). Bootstrapped indirect effects indicated three significant pathways: through AI self-efficacy, through academic procrastination and through the sequential pathway from AI self-efficacy to academic procrastination. The total standardised indirect effect was −.229, accounting for 55.84% of the total effect. Conclusions AI self-efficacy and academic procrastination partially and sequentially mediated the association between AI literacy and AI dependence. The findings suggest that AI literacy may reduce maladaptive AI dependence by strengthening efficacy beliefs and reducing procrastination-related reliance on AI tools. Given the cross-sectional design, longitudinal research is needed to clarify temporal ordering.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey measuring AI dependence alongside academic procrastination and AI self-efficacy, with Pearson correlations reported.

**Решение:** =

---

### 467 · R2711

**AI dependency and academic motivation in higher education: the mediating role of learned helplessness and the moderating role of AI literacy.**

2026 · Frontiers in psychology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyg.2026.1896371

The growing integration of generative artificial intelligence (AI) into university education has raised concerns about the psychological consequences of sustained student reliance on AI tools. While prior research has documented behavioral and cognitive effects of AI overreliance, the psychological mechanism through which AI dependency damages academic motivation remains poorly understood. Drawing on learned helplessness theory (LHT) and self-determination theory (SDT), this study proposes and tests a moderated mediation model in which learned helplessness mediates the relationship between AI dependency and academic intrinsic motivation, with AI literacy serving as a boundary condition that attenuates this pathway. Data were collected from 457 Chinese university students via a cross-sectional survey using validated scales for all four constructs, and the model was tested using covariance-based structural equation modeling (CB-SEM). Results show that AI dependency significantly and positively predicts learned helplessness, which in turn significantly and negatively predicts intrinsic motivation. The indirect effect of AI dependency on intrinsic motivation through learned helplessness was significant, confirming the proposed mediation. AI literacy significantly moderated the AI dependency-learned helplessness pathway, such that the indirect effect was weaker among students with higher AI literacy than among those with lower AI literacy. These findings extend LHT by introducing AI-mediated academic success as a novel, non-failure antecedent of learned helplessness, enrich SDT by specifying the psychological mechanism through which AI dependency becomes need-thwarting, and reposition AI literacy as a psychologically active buffer against motivational harm. The study carries direct implications for university curricula, faculty practice, and institutional policy.</jats:p

**ИИ:** разошлись — Opus -4 (среди измеренных конструктов нет ни одного нашего коррелята: AI dependency is measured, but the other three constructs (learned helplessness, intrinsic motivation, AI literacy) are not correlates of interest.); Sonnet ? (корреляты не названы: Quantitative survey of AI dependency with learned helplessness and intrinsic motivation; neither is a listed correlate, but learned helplessness is close to self-efficacy or distress, so check the full text.)

**Решение:** ?

---

### 468 · R2715

**Shifting Patterns Across Time: Evolving Associations Between AI Addiction and Dehumanization in a Three-Wave Longitudinal Study**

2026 · International Journal of Human-Computer Interaction · article, journalarticle, journalarticle/journal contribution · en · https://doi.org/10.1080/10447318.2026.2699365

The longitudinal association between AI addiction (AIA) and dehumanization, as well as its underlying mechanisms, remains unclear. This study examined the associations between AIA and dehumanization across three waves and tested the mediating role of information overload. A total of 492 university students from a province in China completed all three waves (M age = 18.74, SD = 1.01; 53.86% female). Restricted cubic spline analyses showed a nonlinear association between AIA and dehumanization at Time 1, but not at later waves. Random-intercept cross-lagged panel models showed no significant cross-lagged effects from Time 1 to Time 2. However, from Time 2 to Time 3, AIA and dehumanization showed significant reciprocal predictive effects. Information overload did not mediate these associations. These findings highlight the importance of examining temporal dynamics in understanding the psychological consequences of AI addiction. The association between AIA and dehumanization may become reciprocal over time.

**ИИ:** разошлись — Opus -4 (среди измеренных конструктов нет ни одного нашего коррелята: AI addiction was measured, but the listed constructs (dehumanization, information overload) are not correlates of interest.); Sonnet ? (корреляты не названы: Three-wave AI addiction study with dehumanization and information overload (stress-adjacent); no listed correlate named, but a correlation table might include one.)

**Решение:** -

---

### 469 · R2719

**Exploring College Students' AI Dependence in Human-AI Collaborative Creation: Development and Validation of the CC-PACE Model.**

2026 · Journal of Intelligence · article, journal article, journalarticle · eng · https://doi.org/10.3390/jintelligence14080155

The development of Artificial Intelligence (AI) poses significant challenges to creativity research and practice. Managing the degree of AI dependence during the creative process is therefore critical to fostering the healthy development of human creativity. To address this concern, this study proposes the CC-PACE model by integrating the 5A&rsquo;s framework with the I-PACE model, and examines factors associated with AI dependence during the creative process. A cross-sectional survey was conducted with 813 college students in China, and the data were analyzed using partial least squares structural equation modeling (PLS-SEM). The results showed that (1) both creative personal identity and creative self-efficacy were positively associated with closeness with the audience and the perception of AI as a creative agent. (2) Both closeness with the audience and the perception of AI as a creative agent were positively associated with time spent using AI, usage preference, and perceived difficulty in avoiding AI use. (3) Time spent and usage preference were positively associated with students&rsquo; creative self-assessment, whereas perceived difficulty in avoiding AI use was not significantly associated with creative self-assessment. This study provides a viable analytical framework for understanding AI dependence in creative contexts. The findings further suggest that teachers should help students develop an appropriate understanding of AI&rsquo;s role, strengthen students&rsquo; creative agency, and emphasize process-oriented assessment in creative activities.

**ИИ:** разошлись — Opus + (назван коррелят: Survey (n=813) measuring AI dependence components (including difficulty avoiding AI use) and linking them to creative self-efficacy via PLS-SEM.); Sonnet ? (мера зависимости неясна: Survey of 813 students on AI dependence (time, preference, difficulty avoiding use) with creative self-efficacy. The dependence measure and its link to the correlates are unclear.)

**Решение:** +

---

### 470 · R2722

**It’s Not Me, It’s the AI: Low-Performance Attribution, Emotional Exhaustion, and Turnover Intention**

2026 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2026.222bp

As artificial intelligence (AI) systems become increasingly integrated into organizational workflows, understanding how employees psychologically process AI-related performance failures has become critical for both theory and practice. Drawing on attribution theory (Weiner, 1985) and conservation of resources (COR) theory (Hobfoll, 1989), we develop a moderated mediation model to examine when and why such attributions lead to emotional exhaustion and, ultimately, turnover intention. We propose that the positive relationship between employee attribution to AI and emotional exhaustion is moderated by the employee’s level of work AI dependence, and further jointly moderated by employee dependence and leader attribution of the low performance to AI. Specifically, the relationship is strongest under conditions of high AI dependence and high leader AI attribution. We then posit emotional exhaustion as a key mechanism, mediating this interactive effect on turnover intention. Across two complementary studies, including a multi-source field data from call center employees who vary in their AI dependence, we find consistent support for these predictions. These results reveal that in AI-augmented work contexts, classical attribution mechanisms reverse under conditions of technological dependence, with profound implications for employee retention and organizational AI implementation strategies.

**ИИ:** ? · обе модели · корреляты не названы · Measures work AI dependence among call-center employees; emotional exhaustion is a borderline distress/stress correlate, and the AI system type is unclear.

**Решение:** =

---

### 471 · R2725

**Of Prometheus and Pixels: The Ethical and Existential Costs of AI-Assisted Entrepreneurship**

2026 · Journal of Business Ethics · article · en · https://doi.org/10.1007/s10551-026-06476-5

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests a conceptual ethics paper, but it may be empirical work on entrepreneurs' AI reliance and well-being.

**Решение:** =

---

### 472 · R2727

**The Formation Mechanism of Generative AI Dependency: A PLS-SEM Study Based on the I-PACE Model**

2026 · Proceedings of the 2026 3rd International Conference on Digital Society and Artificial Intelligence · book, conference, conference-paper · https://doi.org/10.1145/3833541.3833814

Generative artificial intelligence (GenAI) is rapidly becoming embedded in learning, work, and everyday decision-making. Concurrently, concerns regarding AI dependency are increasingly prominent. Grounded in the I-PACE model, this study develops a structural equation model in which AI self-efficacy serves as the person-related antecedent, AI anxiety and performance expectation constitute the affective-cognitive mechanisms, and the need for cognitive closure (NFCC) functions as a moderator. By empirically examining the pathways among these variables, this paper uncovers the key mechanisms underlying GenAI dependency and provides a theoretical foundation for developing future interventions and governance strategies.

**ИИ:** + · обе модели · назван коррелят · PLS-SEM study of GenAI dependency with self-efficacy and AI anxiety as antecedents; both are correlates of interest.

**Решение:** =

---

### 473 · R2728

**The more deeply embedded in AI, the more creative you become? Investigating the pathways linking AI identity and creative deviance**

2026 · Journal of Managerial Psychology · journalarticle, review, article · en · https://doi.org/10.1108/jmp-05-2025-0454

Purpose This study aims to explore how the formation of artificial intelligence (AI) identity impacts employees' creative deviance. Drawing on role theory and the cognitive-affective system theory, it analyzes the pathways and boundary conditions of this influence in the AI-integrated workplace. Design/methodology/approach Using a multi-wave research design, we collected survey data from 379 employees across various industries. The data were analyzed using SPSS to test a dual-path mediation model, examining how creative self-efficacy and AI dependency mediate the AI identity–creative deviance relationship. Post hoc interviews were conducted to provide additional qualitative evidence and insights for future studies. Findings Results reveal that AI identity has competing effects: it enhances creative deviance through increased creative self-efficacy, while suppressing it through heightened AI dependency. Notably, prevention-focused employees experience stronger suppression effects from AI dependency, whereas promotion focus shows no significant moderating effect on the positive pathway. Practical implications The study provides organizations with dual-path management strategies to balance AI adoption and employee innovation, requiring both the cultivation of creative confidence and the prevention of technological overreliance, thereby optimizing human–AI collaborative innovation effectiveness. Originality/value This study contributes to the literature by introducing AI identity as a key psychological construct in the context of AI-driven workplaces. By integrating role identity and cognitive-affective processing system theory, this study elucidates the dual mechanisms through which AI identity affects creative deviance, advancing theoretical understanding. It also identifies regulatory focus as a boundary condition, providing fresh insights into how AI identity shapes employee innovation. </jats:sec

**ИИ:** + · обе модели · назван коррелят · Multi-wave employee survey measured AI dependency and creative self-efficacy as mediators, so their correlation is likely reported.

**Решение:** =

---

### 474 · R2729

**Understanding GAI user addiction from an I-PACE perspective**

2026 · Information Technology and People · article, journalarticle · en · https://doi.org/10.1108/itp-07-2025-1047

Purpose This study examines generative artificial intelligence addiction (GAIA) among generative artificial intelligence (GAI) users to understand its causes, improve user experience and promote GAI sustainability. Design/methodology/approach Using the interaction of person–affect–cognition–execution (I-PACE) model, 563 valid responses were analyzed employing structural equation modeling (SEM) and fuzzy-set qualitative comparative analysis (fsQCA). Findings SEM results revealed that technophilia (TE), perceived task-technology fit (PT) and perceived inspiration (PI) enhance flow experience (FE), whereas TE, social isolation (SI), PT and PI lead to uncontrolled use of GAI (UUG). FE functions as a critical mediator for UUG, and both FE and UUG significantly contribute to GAIA. Additionally, fsQCA identified five configurational pathways to GAIA, highlighting its multifaceted nature. Originality/value This study represents one of the first attempts to apply I-PACE model to the GAIA phenomenon, thereby advancing the theoretical understanding of behavioral addiction among GAI users. By integrating SEM and fsQCA, this research highlights the pivotal role of UUG in GAIA development. To promote the responsible and sustainable growth of GAI, this study provides novel insights along with four actionable managerial recommendations.

**ИИ:** + · обе модели · назван коррелят · Survey (n=563) measured generative AI addiction with SEM; social isolation (close to loneliness) is a predictor of uncontrolled GAI use and addiction.

**Решение:** =

---

### 475 · R2731

**AI Competency Erosion: Understanding Expertise Decay**

2026 · Future of business and finance · book-chapter · en · https://doi.org/10.1007/978-3-032-11748-9_5

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное или не эмпирическое исследование без количественной меры зависимости: Business book chapter on AI-driven expertise decay with no abstract; likely conceptual, and no dependence measure or psychological correlates are suggested.); Sonnet ? (нет аннотации: Book chapter on AI competency erosion with no abstract; likely conceptual, but could involve over-reliance measures, so uncertain.)

**Решение:** -

---

### 476 · R2734

**Measuring and Mitigating Competency Erosion**

2026 · Future of business and finance · book-chapter · en · https://doi.org/10.1007/978-3-032-11748-9_6

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное или не эмпирическое исследование без количественной меры зависимости: Business book chapter with no abstract; title never mentions AI dependence or psychological correlates and suggests conceptual content.); Sonnet ? (нет аннотации: No abstract; the title on competency erosion may concern AI over-reliance, but it is likely conceptual or a business chapter, so the record is uncertain.)

**Решение:** -

---

### 477 · R2737

**Artificial Intelligence Over-Dependence and Students' Learning Outcomes in Tertiary Institutions in Plateau State, Nigeria**

2026 · PJ Palgo Journal of Education Research · journal-article · https://doi.org/10.65756/pjer.2026.017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title suggests a survey of AI over-dependence in students, but only learning outcomes are named; other correlates are unknown.

**Решение:** =

---

### 478 · R2741

**Beyond Assistant, Companion, and Agent: AI Is Already Someone's Partner**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · und · https://doi.org/10.5281/zenodo.20760967

This paper argues that the ontological blurring HMC has long described is not merely aboundary growing hazier, but a problem of institutional design shaped by unverifiability andundetectability. Drawing on Gradation Theory (GT)—a three-stage framework of Dissolution,Sinking, and Salvage grounded in the HYC Theorem that the human–AI boundary is inprinciple unverifiable—we show how this boundary is dissolving along four axes (body,brain, cognition, and mind) at different depths, while institutions remain stranded on apremise already dissolved. GT functions here not as an alternative to HMC but as a set ofdesign principles for what to do once the boundary can neither be verified nor detected. Wefurther introduce verification submersion—the situation in which the movement of theboundary can no longer be detected by the person—as a contribution to HMC’s theory of theontological boundary. Empirical evidence shows that the dissolution runs deepest on thecognition and mind axes: AI becomes the partner to whom one entrusts thinking and towardwhom one directs emotion, a pattern supported by longitudinal data showing that lonelinessand emotional dependence on AI mutually reinforce each other. As Salvage, we proposevariable safety design (wrapping) that shifts between crisis and ordinary modes, and graduatedguardrail design adjusted to judgment capacity, illustrating these with a workingimplementation already deployed in Japanese municipalities. The paper closes with openquestions surrounding the boundary between care and surveillance.

**ИИ:** разошлись — Opus -2 (качественное или не эмпирическое исследование без количественной меры зависимости: Theoretical/conceptual paper (Gradation Theory, design principles); it only cites existing longitudinal evidence on loneliness and emotional dependence.); Sonnet ? (другое: Mainly theoretical, but cites longitudinal data linking loneliness and emotional dependence on AI; unclear if primary data with a dependence measure are reported.)

**Решение:** -

---

### 479 · R2744

**Lonely happiness: a response to Nakagomi et al. (2026) on AI companionship and wellbeing**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.21532636

Research on AI companionship and wellbeing has split into two camps. One camp warns that AI companionship deepens the loneliness epidemic through emotional dependence (Montag et al., 2025). The other finds that AI companions reduce loneliness and raise subjective wellbeing, particularly among lonely or socially disadvantaged users (De Freitas et al., 2026; Nakagomi et al., 2026). Drawing on a nationally representative survey of 11,939 Japanese adults (Shibata, 2026), this paper argues that both camps are partly right, because they describe two distinct psychological pathways rather than a single effect. A negative pathway runs from empathy toward AI, through emotional dependence, to reduced interpersonal interaction, increased loneliness, and increased psychological stress. A positive pathway runs from empathy toward AI, through increased self-esteem grounded in AI's nonjudgmental validation, to increased subjective wellbeing. Both pathways operate simultaneously in the same population, producing what we term "lonely happiness": the coexistence, rather than a trade-off, of rising loneliness and rising wellbeing. The balance between the two pathways diverges sharply by gender and childhood disadvantage: men who experienced childhood disadvantage show only the positive pathway, while women with the same background show only the negative one. A uniform policy response, whether restricting or tolerating AI companionship, would therefore help some populations while harming others. We discuss implications for dependence-minimising AI design, self-esteem-building interventions, and population-level risk stratification, and argue that lonely happiness should be treated as a measurable outcome.

**ИИ:** разошлись — Opus ? (другое: A response paper, but it seems to analyse survey data (N=11,939) linking emotional dependence on AI to loneliness, stress, self-esteem and wellbeing.); Sonnet + (эмоциональная зависимость: Survey of 11,939 Japanese adults modelling emotional dependence on AI with loneliness, stress, self-esteem and wellbeing in pathway models.)

**Решение:** +

---

### 480 · R2756

**Are effects of task-related stressors and academic self-management on college students' AI stickiness consistent across the DeepSeek transition?**

2026 · Acta psychologica · journal article, journalarticle, review · eng · https://doi.org/10.1016/j.actpsy.2026.107696

Steeped in outcome-driven educational ecosystems, college students, especially the first-years facing the transition from high school to university with a surge in unprecedented academic demands, may encounter diverse academic stressors and rely on personal regulatory resources to cope. This challenging transition offers a unique window to investigate how students cope with perceived academic demands and their reliance on self-management skills in the evolving landscape of generative Artificial Intelligence (AI), particularly the changes due to the release of DeepSeek R1. Guided by Conservation of Resources (COR) theory, this study examines the consistency of indirect effects of task-related academic stressors and academic self-management on students' AI engagement via a resource caravan reflected by user-stickiness factors across the DeepSeek transition. Using a repeated cross-sectional design, 640 first-year undergraduates completed surveys across two waves with multi-group SEM analyses testing whether indirect effects differed significantly (Hypothesis 1) or remained consistent (Hypothesis 2). Among the studied indirect effects, only academic self-management consistently fostered stickiness via user satisfaction across two waves, supporting Hypothesis 2, while the effects of academic stressors varied by context at a liberal alpha level of 0.10, providing only partial and preliminary support for Hypothesis 1. Since samples from two waves differed substantially in gender composition and other time-varying contextual factors, the observed differences cannot be attributed solely to the DeepSeek release; they may reflect broader sample and environmental changes. Conversely, the self-management pathway did not differ significantly between two waves involving these compositional and contextual differences. The findings reveal a consistent yet evolving pattern of dependency on AI as a coping strategy for academic stress, with satisfaction emerging as the key psychological resource driving sustained AI use, especially when students possess strong self-management skills.

**ИИ:** ? · обе модели · мера зависимости неясна · Measures AI 'stickiness', framed as dependency, alongside academic stressors and self-management; unclear whether stickiness counts as a dependence measure.

**Решение:** =

---

### 481 · R2758

**Anxiety, emotional abuse, and physical activity as correlates of AI-related affective dependence among adolescents: mediation, moderation, and network analyses**

2026 · Frontiers in Public Health · journalarticle, article, journal-article · en · https://doi.org/10.3389/fpubh.2026.1956596

Objective Drawing on attachment and emotion-regulation perspectives, this cross-sectional study examined the associations among emotional abuse (EA), anxiety, physical activity (PA), and AI-related affective dependence (hereafter, AI dependence) among adolescents. Methods In November 2025, a total of 1,589 Chinese adolescents completed self-report questionnaires assessing EA, anxiety, PA, and AI dependence. Descriptive analyses, Pearson correlations, mediation and moderated mediation models, and a covariate-adjusted partial-correlation network were conducted. Common method bias was evaluated using both Harman’s single-factor test and a CFA-based unmeasured latent method construct (ULMC) approach. Results EA was positively associated with anxiety and AI dependence and negatively associated with PA. Anxiety statistically accounted for a small but significant proportion of the EA-AI dependence association [indirect effect = 0.034, 95% CI (0.013, 0.055), 16.43% of the total association]. PA moderated the EA-anxiety association; the positive association was weaker among adolescents reporting higher PA. In the network analysis, the EA-anxiety edge was the strongest conditional association, and EA showed the highest node strength, although these findings should be interpreted descriptively rather than causally. Conclusion The findings suggest that anxiety and PA are meaningful correlates in the association between EA and AI dependence. Because the data are cross-sectional, the results indicate statistical associations rather than temporal or causal mechanisms.

**ИИ:** + · обе модели · эмоциональная зависимость · Cross-sectional survey of 1,589 adolescents measuring AI-related affective dependence; reports Pearson correlations with anxiety.

**Решение:** =

---

### 482 · R2759

**Associations between frequent and excessive generative AI chatbot use and common mental health problems in college students: examining academic and social mechanisms**

2026 · International Journal of Adolescence and Youth · article · en · https://doi.org/10.1080/02673843.2026.2703815

Despite the rapid rise of generative AI chatbot adoption in higher education, limited evidence exists regarding its possible consequences on college students' well-being and functioning. This study explored the impact of frequent/excessive generative AI chatbot use on the academic, social, and mental health outcomes among college students and tested whether academic- and social-related harms mediate the association between the usage and mental health problems. College students (N = 560) studied in Beijing (25.2%) and Hong Kong (74.8%) completed an online survey between June and August 2023. Most participants used ChatGPT. Frequent/excessive generative AI chatbot use was positively correlated with academic stress and loneliness. Furthermore, academic stress fully mediated the association between excessive generative AI chatbot use and anxiety. The findings suggest that frequent/excessive generative AI chatbot use may be associated with academic and social-related harms among college students and underscore the critical importance of fostering balanced and healthy engagement with these tools.

**ИИ:** разошлись — Opus ? (мера зависимости неясна: Correlates named (academic stress, loneliness, anxiety), but "frequent/excessive use" could be just frequency rather than a problematic-use measure.); Sonnet + (назван коррелят: Survey of excessive generative AI chatbot use correlated with academic stress, loneliness and anxiety in college students; likely a problematic-use measure.)

**Решение:** +

---

### 483 · R2771

**PENGARUH ACADEMIC PERFECTIONISM TERHADAP ARTIFICIAL INTELLIGENCE (AI) DEPENDENCY PADA MAHASISWA**

2026 · review

Peningkatan pemanfaatan Artificial Intelligence (AI) dalam aktivitas akademik mahasiswa berpotensi menyebabkan ketergantungan. Academic perfectionism berpotensi meningkatkan ketergantungan AI akibat tuntutan standar pribadi yang tinggi dan keinginan menghindari kesalahan. Penelitian ini bertujuan untuk mengetahui pengaruh academic perfectionism terhadap AI dependency pada mahasiswa. Penelitian ini menggunakan pendekatan kuantitatif non-eksperimental dengan desain cross-sectional. Sampel penelitian ini sebanyak 316 mahasiswa aktif dari perguruan tinggi di Indonesia dengan pengalaman menggunakan AI dalam aktivitas akademik yang direkrut menggunakan teknik non-probability purposive sampling. Penelitian ini menggunakan AI dependence Scale (AIDep-22) oleh Wu dkk. (2026) dan College Academic Perfectionism Scale (CAPS) oleh Liu & Berzenski (2022) sebagai instrumen penelitian. Pengujian hipotesis dilakukan menggunakan analisis regresi hirarki dengan mengontrol variabel kovariat. Hasil penelitian ini menunjukkan bahwa terdapat pengaruh signifikan academic perfectionism terhadap AI dependency pada mahasiswa. Variabel academic perfectionism memiliki pengaruh positif dan berkontribusi sebesar 3,2% terhadap AI dependency. Dengan demikian, dapat disimpulkan bahwa peningkatan pada academic perfectionism mempengaruhi peningkatan AI dependency pada mahasiswa. ***** The increasing use of Artificial Intelligence (AI) in students’ academic activities has the potential to lead to dependency. Academic perfectionism may increase AI dependency due to high personal standards and a desire to avoid mistakes. This study aims to determine the effect of academic perfectionism on AI dependency among students. This study uses a non-experimental quantitative approach with a cross-sectional design. The sample consisted of 316 active students from universities in Indonesia with experience using AI in academic activities, recruited using non-probability purposive sampling. This study utilized the AI Dependence Scale (AIDep-22) by Wu et al. (2026) and the College Academic Perfectionism Scale (CAPS) by Liu & Berzenski (2022) as research instruments. Hypothesis testing was conducted using hierarchical regression analysis while controlling for covariate variables. The results of this study indicate that academic perfectionism has a significant influence on AI dependency among university students. The academic perfectionism variable has a positive influence and contributes 3,2% to AI dependency. Thus, it can be concluded that an increase in academic perfectionism influences an increase in AI dependency in AI dependency among univesity students

**ИИ:** ? · обе модели · корреляты не названы · Cross-sectional survey using AIDep-22 with academic perfectionism, a personality-like trait not explicitly listed; unspecified covariates could include eligible correlates.

**Решение:** =

---

### 484 · R2772

**Large Language Model Dependency in the UK and Italy: Cross-National Evidence from the LLM-D12 scale**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/data paper, article · en · https://doi.org/10.5281/zenodo.22255123

Reliable and culturally comparable instruments are needed to assess psychological dependency on large language models (LLMs) across societal contexts that differ in the extent of LLM use. The present study evaluated whether the LLM-D12, originally developed in the UK, reliably measures Instrumental and Relationship Dependency in Italy, where LLM use is less widespread, and whether scores can be compared directly between the two countries. The LLM-D12 measures Instrumental Dependency, reflecting reliance on LLMs for cognitive support, and Relationship Dependency, reflecting reliance on LLMs for social and emotional support. The sample comprised 1,069 adults from the UK (N = 607; mean age = 28.67 years, SD = 6.18) and Italy (N = 462; mean age = 27.32 years, SD = 5.24). In Italy, confirmatory factor, Mokken, and network analyses supported the two-factor structure, with high internal consistency and clear empirical distinction between the subscales. Strict measurement invariance established that the same constructs were measured in the UK and Italy. UK participants reported substantially higher Instrumental Dependency and higher Relationship Dependency. More frequent use, use while on the move, and text-and-voice interaction were associated with higher dependency, and these associations did not differ by country. Internet addiction was also positively related to both dependency dimensions, with comparable associations in the two samples. Demographic effects were less consistent, with country-specific differences for gender and employment. The findings show that the LLM-D12 retains its two-dimensional structure and measurement comparability in a lower-uptake context and can detect cross-national differences even when dependency levels are relatively low.

**ИИ:** + · обе модели · назван коррелят · LLM-D12 cross-national validation study; it reports that internet addiction is positively associated with both dependency dimensions.

**Решение:** =

---

### 485 · R2773

**Perceived Trustworthiness as a Pathway Linking ADHD Traits to Large Language Models Dependency: Evidence from UK and Chinese Samples**

2026 · International Journal of Human-Computer Interaction · journalarticle, journalarticle/journal contribution, article · en · https://doi.org/10.1080/10447318.2026.2707709

Large language models (LLMs) create contexts in which individual differences may shape reliance on digital systems. Drawing on neurodiversity, this study examined whether perceived trustworthiness of user’s primary LLM mediates associations between attention-deficit/hyperactivity disorder (ADHD) traits and LMM dependencyinstrumental and relationship LLM dependency. Adults in the UK ( n = 567) and China ( n = 577) reported ADHD traits, perceived LLM trustworthiness of LLM, and both types of dependency. Across samples, higher ADHD traits were associated with lower trustworthiness, whereas greater trustworthiness was associated with greater instrumental and relationship dependency, yielding negative indirect effects. In the UK, direct ADHD-dependency associations were non-significant after controlling for trust, and mediation produces a significant negative total effect for relationship dependency. In China, negative indirect effect coexisted with positive direct associations, creating opposing pathways whose total effects depends on their relative magnitude. Implications for inclusive LLM design without unintendend dependency and supporting neurodiverse users are discussed.

**ИИ:** ? · обе модели · другое · Measures instrumental and relationship LLM dependency against ADHD traits (which may include impulsivity) and trust; the eligible correlate is unclear.

**Решение:** =

---

### 486 · R2777

**A Study on the Formation Mechanism and Psychological Structure of AI Emotional Dependence among Vocational High School Students**

2026 · Research Square · article, preprint, posted-content · und · https://doi.org/10.21203/rs.3.rs-9155865/v1

Abstract This study investigates emotional dependency on generative artificial intelligence among vocational high school (VHS) students. In alignment with Taiwan’s 108 Curriculum Guidelines, an interactive “Health and Nursing” module addressing AI reliance was implemented. The sample comprised 1000 students from five VHSs in central Taiwan (October–December 2025). Data were collected through questionnaires and classroom feedback to assess AI interaction frequency, emotional projection, and perceived effects on relationships and psychological needs. Analyses were conducted using SPSS 22.0 and SmartPLS 4. Results indicate that some students developed moderate to high emotional attachment to AI, particularly for support and stress relief, accompanied by blurred ethical boundaries. This study finds that VHS students’ AI dependence is not as severe as commonly assumed. The study conceptualizes AI emotional dependence as a low‑intensity, cognitively mediated, developmentally emergent psychological alignment.

**ИИ:** + · обе модели · эмоциональная зависимость · Quantitative survey (n=1000) with PLS-SEM on emotional dependence on generative AI; mentions stress relief and psychological needs.

**Решение:** =

---

### 487 · R2779

**Emotional Reliance on Generative AI Among Vocational High School Students: An AEDTAM-Based Analysis**

2026 · Sustainability · journalarticle, article, journal-article · en · https://doi.org/10.3390/su18105148

This study examines emotional dependency on generative artificial intelligence among vocational high school (VHS) students. Guided by Taiwan’s 108 Curriculum Guidelines, an interactive “Health and Nursing” course on AI reliance was implemented. The sample included 1000 students from five VHSs in central Taiwan (January–February 2026). Data were collected through questionnaires and classroom feedback to assess AI interaction frequency, emotional projection, and perceived effects on relationships and psychological needs. Research data were analyzed using SPSS 22.0 and SmartPLS 4. Findings show that some students displayed moderate to high emotional attachment to AI, particularly for support and stress relief, with blurred ethical boundaries. After the intervention, students reported greater awareness of risks and increased self-reflection. This study concludes that integrating AI literacy with emotional education into curricula is crucial for responsible technology use and healthy relational development. Overall, emotional reliance on AI among VHS students appears statistically significant but bounded, reflecting a balanced pattern of engagement that supports sustainable psychological well-being.

**ИИ:** + · обе модели · эмоциональная зависимость · Quantitative PLS-SEM survey of emotional dependence on generative AI in 1000 students; stress relief and psychological well-being plausibly correlated.

**Решение:** =

---

### 488 · R2781

**Psychological pathways linking generative AI dependency to psychological capital depletion among Chinese international students**

2026 · Scientific Reports · journalarticle, article, journal-article · en · https://doi.org/10.1038/s41598-026-68047-y

With the widespread use of generative AI in academic writing, language processing, and learning-support contexts, GAD has continued to rise. This study examines whether GAD is associated with rPsyCap and tests the mediating roles of PSD and rSE, both as independent mediators and as a sequential mediation mechanism. A three-wave longitudinal study was conducted. Using a combination of convenience and snowball sampling, questionnaire data were collected from 502 Chinese international students studying abroad (e.g., the United States, the United Kingdom, Australia, Canada, and South Korea). Participants completed measures of GAD, PSD, rSE, and rPsyCap. SEM was conducted using SPSS 26.0, AMOS 26.0, and CEFAtool 3.04. Direct and indirect effects were evaluated with 5,000 bootstrap resamples, and estimands for mediation and serial mediation were computed using AmosEstimandVB. GAD was positively associated with rPsyCap ( γ = 0.163, 95% CI [0.065, 0.264]). The sequential indirect effect via PSD → rSE was significant ( γ = 0.019, 95% CI [0.008, 0.036]), and PSD and rSE also showed significant independent mediation effects ( γ = 0.087, 95% CI [0.051, 0.132]; γ = 0.034, 95% CI [0.013, 0.060], respectively). GAD is linked to rPsyCap both directly and indirectly. By delineating a psychological process through which GAD may incur latent costs, this study informs the judicious integration of generative AI in educational and learning contexts.

**ИИ:** + · обе модели · назван коррелят · Three-wave survey of generative AI dependency with mediators PSD and rSE (likely self-efficacy/self-esteem), plus psychological capital.

**Решение:** =

---

### 489 · R2782

**When Creativity Encounters Algorithms: Personality Traits as Predictors of Design Students’ Adoption and Dependence on AI-Assisted Design**

2026 · AHFE international · article, conference-paper, proceedings-article · und · https://doi.org/10.54941/ahfe1007634

With the rapid development of generative AI, AI-assisted design tools are increasingly integrated into design education, yet students show marked differences in acceptance, continuance intention, and dependence. Given the creative nature of design learners, personality traits may strongly shape their responses to AI. This study examines how the Big Five influence attitudes toward AI-assisted design and how these attitudes drive continuance intention and AI dependence. Using PLS-SEM with data from 345 design majors, the model “Personality Traits → Attitude → Continuance Intention → AI Dependence” was tested. Conscientiousness positively predicts attitude, while extraversion, neuroticism, and openness negatively predict it; agreeableness shows no effect. These results indicate differing sensitivities to efficiency, uncertainty, and creative constraints in AI-generated outputs. Attitude significantly predicts continuance intention and directly and indirectly contributes to AI dependence. Overall, the study reveals personality’s critical role in AI adoption and provides insights for developing personalized, human–AI collaborative design education.

**ИИ:** + · обе модели · назван коррелят · PLS-SEM survey of 345 design students with Big Five personality traits (including neuroticism) and an AI dependence measure; correlations likely reported.

**Решение:** =

---

### 490 · R2786

**Academic Self-Efficacy and Dependence on Artificial Intelligence in Peruvian Higher Education: The Mediating Effect of Performance Expectancy**

2026 · Proceedings of the LACCEI international multi-conference for engineering, education and technology · conference, conference-paper · https://doi.org/10.18687/laccei2026.1.1.1236

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · назван коррелят · Title links academic self-efficacy with AI dependence in a mediation model; no abstract, so the dependence measure needs checking in the full text.

**Решение:** =

---

### 491 · R2791

**The suppressing effect of AI dependency in the workplace: Can frequent use of AI enhance practitioners' job self‐efficacy?**

2026 · Applied Psychology · article, dataset/, journalarticle · en · https://doi.org/10.1111/apps.70121

Abstract Artificial intelligence (AI) is rapidly becoming a primary channel through which employees access information and solve problems at work. Drawing on media dependency theory, we theorize that workplace AI use exerts a suppressing effect on practitioners' job self‐efficacy in task‐focused achievement contexts. Specifically, AI use can directly bolster job self‐efficacy by facilitating task accomplishment. At the same time, frequent AI use may foster AI dependency, reducing employees' engagement in competence‐relevant cognitive work and, in turn, weakening mastery‐based confidence. Across a multi‐source, time‐lagged field study and a scenario experiment, results support this competing‐process account: workplace AI use showed a positive direct association with job self‐efficacy, whereas AI dependency carried a negative indirect effect, yielding a significant suppressing effect. We further identify proactive feedback to AI as a key boundary condition that attenuates the negative effect of AI dependency on job self‐efficacy and renders the suppressing effect nonsignificant at higher levels of feedback. This research clarifies how organizations can leverage AI for performance gains while safeguarding employees' perceived capability.

**ИИ:** + · обе модели · назван коррелят · Time-lagged field study measuring workplace AI dependency and its relation to job self-efficacy (a correlate of interest).

**Решение:** =

---

### 492 · R2802

**Investigating the role of GenAI dependency on university students’ critical thinking disposition: From the perspective of knowledge inertia**

2026 · Education and Information Technologies · journalarticle, article · en · https://doi.org/10.1007/s10639-026-14158-y

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · GenAI dependency measured; title names only critical thinking and knowledge inertia, but without an abstract other correlates can't be ruled out.

**Решение:** =

---

### 493 · R2809

**Distributed Dependency Intervention to Mitigate AI Companion Overreliance**

2026 · Lecture notes on data engineering and communications technologies · book-chapter, conference-paper · en · https://doi.org/10.1007/978-3-032-38477-5_14

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; intervention on AI companion overreliance may include baseline dependence measure with psychological correlates.

**Решение:** =

---

### 494 · R2814

**A general factor underlies the mental-health risk of seven digital technologies**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-10956237/v1

Abstract Public debates often assume digital technologies differ in their risk to mental health. For example, Social media is frequently singled out as especially harmful compared with videoconferencing. In 10,454 adults, we measured problematic use and psychological outcomes across seven technologies, including social media, AI companions, short-form video, sleep trackers, smartphones, dating apps, and videoconferencing. We built a unified distress index. Raw associations ranked the seven products (r = 0.883-0.916). A nested model comparison showed that product-specific usage detail added no discernible explanatory power beyond one general usage factor (ΔR² = 0.0001, F(6, 10448) = 1.19, P = 0.309). All fourteen scale scores were explained almost entirely by one general factor at the scale-mean level (ωH = 0.984), though item-level sharing was more modest (36.5%), consistent with aggregation effects. Known-groups validity confirmed the factor is substantively meaningful. Apparent differences among technologies may reflect a shared vulnerability, not platform-specific mechanisms.

**ИИ:** + · обе модели · назван коррелят · Survey of 10,454 adults measuring problematic use of AI companions alongside psychological distress outcomes; correlations likely reported.

**Решение:** =

---

### 495 · R2817

**Heterogeneous Patterns of AI Chatbot Dependence in Chinese Adolescents: A Latent Profile Analysis of Distal Risk Factors and Use Motivations**

2026 · OSF · other literature type, text/project, preprint · und · https://doi.org/10.17605/osf.io/ub5f8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus + (нет аннотации: No abstract; title describes a quantitative latent profile analysis of AI chatbot dependence in adolescents with risk factors and motivations.); Sonnet ? (нет аннотации: No abstract; title suggests a quantitative latent profile study of AI chatbot dependence with distal risk factors, likely including eligible correlates.)

**Решение:** ?

---

### 496 · R2823

**From boredom to problematic AI chatbot use: a three-wave half-longitudinal mediation study of loneliness and dual-system self-control.**

2026 · Australian journal of psychology · journal article, journalarticle, article · eng · https://doi.org/10.1080/00049530.2026.2737094

ABSTRACT Background Problematic use of AI chatbots (PUAIC) is an emerging concern. Drawing on the I-PACE model and the dual-system model of self-control, this study examined the mediating roles of loneliness, the control system, and the impulsive system. Methods A three-wave half-longitudinal mediation design was used with 551 Chinese college students at baseline. Boredom proneness was assessed at Time 1, loneliness and the control and impulsive systems at Time 2, and PUAIC at Time 3. Missing data were handled using 20 multiply imputed datasets, and PROCESS Model 81 was estimated with sex and grade level as covariates. Results Pooled analyses showed that boredom proneness was associated with loneliness (β = .57), the impulsive system (β = .31), the control system (β = −.38), and PUAIC directly (β = .25; all p < .001). Significant indirect effects occurred through loneliness (.073), the impulsive system (.077), and the serial loneliness–impulsive-system pathway (.038). Conclusion The findings suggest that boredom proneness may be associated with later PUAIC directly and indirectly through loneliness and impulsive tendencies. These associations may inform the development of prevention strategies for PUAIC that address loneliness and impulsive tendencies among college students.

**ИИ:** + · обе модели · назван коррелят · Longitudinal survey linking problematic AI chatbot use with boredom, loneliness, self-control and impulsivity in college students.

**Решение:** =

---

### 497 · R2825

**Personalized GenAI coaching and self-regulation in L2 writing across a nine-week active-control study**

2026 · Frontiers in Psychology · article · https://doi.org/10.3389/fpsyg.2026.1904842

Introduction Personalized rationale is an explanation of why a metacognitive strategy is relevant to a learner’s current writing. This study compared a personalized GenAI coaching package with template-based adaptive metacognitive prompting (AMP) in a nine-week randomized study of Chinese EFL undergraduates. Methods Ninety-two participants completed pretest, posttest, and three-week delayed posttest assessments. Both conditions used the same Doubao LLM, interface, and trigger infrastructure. The AMP-Agent condition combined an essay-specific observation, personalized rationale, and an open-ended question; the AMP condition used template prompts. Results Analyses of questionnaire item responses found Group × Time interactions for self-regulated learning (SRL; p = 0.019) and GenAI dependency ( p = 0.010), which also survived a retrospective Holm sensitivity correction across the three total outcomes. The SRL total contrasts at posttest and delayed posttest did not survive Bonferroni correction across time points. Self-reported GenAI dependency questionnaire scores were lower in the AMP-Agent group at both later assessments after this correction. Evidence for different writing-score trajectories was insufficient (interaction p = 0.101). None of five highlighted behavioral transitions survived correction across 20 transition comparisons. Discussion The findings support a difference in self-reported regulation and dependency trajectories between the two prompting packages, while leaving the contribution of rationale alone, sustained writing benefits, and psychological mechanisms unresolved.

**ИИ:** ? · обе модели · корреляты не названы · Randomized study measured a GenAI dependency questionnaire; the only other construct is SRL (subscales might include self-efficacy). Baseline correlations are possible.

**Решение:** =

---

### 498 · R2832

**PENGARUH ACADEMIC SELF-EFFICACY TERHADAP ARTIFICIAL INTELLIGENCE DEPENDENCY DENGAN ACADEMIC STRESS SEBAGAI VARIABEL INTERVENING**

2026 · EDUTECH Jurnal Inovasi Pendidikan Berbantuan Teknologi · article, journalarticle · und · https://doi.org/10.51878/edutech.v6i2.10623

This study focuses on examining the impact of academic self-efficacy on artificial intelligence dependency, while also investigating the role of academic stress as a mediating factor among students in the Office Administration Education Program at Surabaya State University. The rapid advancement of AI technology is now fueling a growing pattern of dependency among students, necessitating a deeper exploration from an academic perspective. We employed a quantitative method with an explanatory design. Data were collected via a questionnaire distributed to 274 respondents and analyzed using Partial Least Squares–Structural Equation Modeling (PLS-SEM) through the SmartPLS 4 software. The results indicate that: (1) academic self-confidence negatively and significantly influences AI dependency; (2) academic self-confidence also negatively and significantly reduces academic stress; (3) academic stress, conversely, positively and significantly increases AI dependency; and (4) academic stress significantly mediates the relationship between academic self-confidence and AI dependency. In conclusion, the higher the academic self-confidence, the lower the stress experienced by students, which ultimately helps reduce excessive dependence on AI technology. ABSTRAK Penelitian ini difokuskan pada pengkajian dampak rasa percaya diri akademik (academic self-efficacy) terhadap ketergantungan pada kecerdasan buatan (artificial intelligence dependency), sambil meneliti peran stres akademik sebagai faktor mediasi di kalangan mahasiswa Program Studi Pendidikan Administrasi Perkantoran di Universitas Negeri Surabaya. Kemajuan cepat teknologi AI kini memicu pola ketergantungan mahasiswa yang semakin kuat, sehingga perlu dieksplorasi lebih dalam dari sisi akademiknya. Kami menerapkan metode kuantitatif dengan rancangan eksplanatori. Data diperoleh lewat kuesioner yang disebarkan ke 274 responden, lalu diolah pakai Partial Least Squares–Structural Equation Modeling (PLS-SEM) melalui software SmartPLS 4. Dari hasilnya, terlihat bahwa: (1) rasa percaya diri akademik secara negatif dan signifikan memengaruhi ketergantungan AI; (2) rasa percaya diri akademik juga menekan stres akademik secara negatif dan signifikan; (3) stres akademik justru meningkatkan ketergantungan AI secara positif dan signifikan; serta (4) stres akademik terbukti memediasi hubungan antara rasa percaya diri akademik dan ketergantungan AI dengan cara yang signifikan. Kesimpulannya, semakin tinggi keyakinan diri dalam urusan akademik, semakin rendah stres yang dialami mahasiswa, yang akhirnya membantu mengurangi ketergantungan berlebih pada teknologi AI.

**ИИ:** + · обе модели · назван коррелят · PLS-SEM survey (n=274) relating AI dependency to academic self-efficacy and academic stress among students.

**Решение:** =

---

### 499 · R2837

**More flexible or more rigid? A study on the double-edged sword effect of Gen AI usage dependence on employees’ emotional labor**

2026 · Journal of Retailing and Consumer Services · article, journal-article · en · https://doi.org/10.1016/j.jretconser.2026.104813

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; GenAI usage dependence in employees linked to emotional labor; correlates such as stress or well-being are possible.

**Решение:** =

---

### 500 · R2842

**Psychological Distress and Artificial Intelligence Dependency: The Moderating Role of Extraversion**

2026 · Current Perspectives in Social Sciences · journalarticle, article · en · https://doi.org/10.53487/atasobed.1920593

The aim of this study is to examine the moderating role of extraversion in the relationship between psychological distress and artificial intelligence dependency. A total of 438 university students (24.9% male; mean age = 21.65, SD = 3.65) participated in the study through convenience sampling. Data were collected using the Scale for Dependence on Artificial Intelligence, the Depression Anxiety Stress Scale-Short Form, and the Ten-Item Personality Inventory. The relationships among variables were examined using Pearson and Spearman correlation analyses, and the main hypothesis of the study was tested through conditional process analysis using Hayes’ PROCESS Macro (Model 1). The findings indicated a significant relationship between psychological distress and artificial intelligence dependency. The results of the moderation analysis revealed that the effect of psychological distress on artificial intelligence dependency varied depending on the level of extraversion. While this relationship was not significant at low levels of extraversion, it became positive and significant at higher levels. Additionally, extraversion was found to have a direct and significant negative effect on artificial intelligence dependency. These findings suggest that the relationship between psychological distress and artificial intelligence dependency should be considered within the framework of individual differences. Extraversion appears to play a critical moderating role in this relationship. This study contributes to the literature on artificial intelligence dependency by expanding the limited empirical evidence in this emerging field.

**ИИ:** + · обе модели · назван коррелят · Survey of 438 students correlating the Scale for Dependence on AI with DASS distress and extraversion.

**Решение:** =

---

### 501 · R2846

**Generative AI chatbots in higher education: addiction, cognitive offloading, and the role of AI literacy**

2026 · Interactive Learning Environments · journal-article · https://doi.org/10.1080/10494820.2026.2677727

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title measures chatbot addiction, but which correlates were measured is unclear (only cognitive offloading and AI literacy are named).

**Решение:** =

---

### 502 · R2847

**AI ASSISTANCE, NOT AI DEPENDENCE, PREDICTS CRITICAL THINKING AMONG UNIVERSITY STUDENTS IN PAKISTAN**

2026 · Zenodo (CERN European Organization for Nuclear Research) · report, text/, article · https://doi.org/10.5281/zenodo.23186826

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · The title shows AI dependence was measured with critical thinking as the outcome. There is no abstract, so other correlates can't be ruled out.

**Решение:** =

---

### 503 · R2858

**Assessment of dependence on artificial intelligence and associated factors among medical students**

2026 · Eskişehir Türk Dünyası Uygulama ve Araştırma Merkezi Halk Sağlığı Dergisi · article, journalarticle, journal-article · tr · https://doi.org/10.35232/estudamhsd.1915530

This study aimed to assess the level of dependence on artificial intelligence (AI) among medical students and to identify its associated factors. The study population of this cross-sectional study consisted of 236 medical students in years 1–4 at a university in November 2025. Data were collected using a questionnaire that included sociodemographic characteristics, AI usage characteristics, the Scale for Dependence on AI (DAI), the Academic Self-Efficacy Scale (ASES), and the Multidimensional Scale of Perceived Social Support (MSPSS). The mean age of the participants was 20.02±1.65 years, and 49.2% were male. DAI scores ranged from 5 to 25, with a mean of 11.04±4.08. Higher mean DAI scores were observed among students who used AI for more than 30 minutes daily, checked AI without intending to use it, and used it for academic and social chatting/emotional sharing purposes (p

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey of medical students measuring dependence on AI (DAI) alongside academic self-efficacy and perceived social support.

**Решение:** =

---

### 504 · R2861

**An Empirical Study on the Development and Validation of a Conversational AI Dependence Scale for Students in Application-Oriented Universities**

2026 · Asia-Pacific Journal of Humanities and Social Sciences · article, journalarticle, journal-article · und · https://doi.org/10.53789/j.1653-0465.2026.0602.024.p

Please refer to the URL that includes this article for the abstract.

**ИИ:** + · обе модели · валидация шкалы · Development and validation of a Conversational AI Dependence Scale for students; abstract missing, but likely reports convergent validity with correlates.

**Решение:** =

---

### 505 · R2864

**AI learning dependence and interpersonal incompetence in EFL contexts: The moderating role of ethical awareness.**

2026 · Scientific reports · journal article, journalarticle, review · eng · https://doi.org/10.1038/s41598-026-47158-6

As artificial intelligence (AI) becomes increasingly integrated into English as a Foreign Language (EFL) education, concerns have arisen regarding its potential impact on learners’ social development. This study investigates the relationship between AI learning dependence and interpersonal incompetence among EFL university students, with a particular focus on the moderating role of AI ethical awareness. A survey of 608 non-English major university students was conducted. Using the Unified Theory of Acceptance and Use of Technology (UTAUT) and structural equation modeling (SEM), the research identified factors contributing to AI dependence in EFL learning. Additionally, the impact of AI dependence on learners’ interpersonal incompetence was examined through Media Dependency Theory. The findings indicate that factors such as effort expectancy, performance expectancy, facilitating conditions, and social influence are positively associated with learners’ AI dependence. This dependence, in turn, is positively associated with greater interpersonal incompetence. Furthermore, AI ethical awareness moderates this relationship: the positive association between AI dependence and interpersonal incompetence is weaker among learners with higher ethical awareness. The study confirms the applicability of UTAUT in explaining AI learning dependence and highlights the importance of fostering ethical awareness to mitigate the potential social risks of AI in education. Practical suggestions are also provided to support the sustainable integration of AI in EFL education.

**ИИ:** ? · обе модели · корреляты не названы · AI learning dependence measured; interpersonal incompetence is not a listed correlate but may overlap social anxiety or loneliness; check the full text.

**Решение:** =

---

### 506 · R2865

**Algorithmically Mediated Intimacy in Human-AI Companionship: Temporal Sedimentation, AI Anxiety, and Algorithmic Awareness**

2026 · International Journal of Human-Computer Interaction · dataset/dataset, article, dataset · en · https://doi.org/10.1080/10447318.2026.2695435

As AI companions become increasingly embedded in everyday emotional support, it remains unclear how initial attraction develops into relationship satisfaction and emotional attachment amid AI anxiety and algorithmic awareness. This study examines the Temporal Sedimentation Model of AI Intimacy (TSM-AI) in China. Using a sequential explanatory mixed-methods design, Study 1 surveyed 615 AI companion users recruited through criterion-based online convenience sampling between July and August 2025, with data analyzed using SPSS 26 and Mplus 8. Study 2 involved 19 semi-structured interviews using purposive maximum-variation sampling between August and November 2025, with transcripts coded in NVivo 12. Results show that perceived attraction is associated with emotional attachment primarily through relationship satisfaction. AI anxiety is negatively associated with perceived attraction and satisfaction, while algorithmic awareness attenuates these associations. Interviews further illustrate that users experience AI companions as controllable yet ambivalent safe spaces where comfort, dependence, privacy concerns, and infrastructural distrust coexist.

**ИИ:** ? · обе модели · мера зависимости неясна · Survey of AI companion users measuring emotional attachment, possibly a proxy for emotional dependence, alongside AI anxiety; dataset record judged by its parent article.

**Решение:** =

---

### 507 · R2868

**Being perfectly seen: Affective capture, relational risk, and the Autopticon effect in AI companion systems**

2026 · Telematics and Informatics · article · en · https://doi.org/10.1016/j.tele.2026.102461

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title is about affective capture by AI companions; it may be conceptual, but an empirical study can't be ruled out.

**Решение:** =

---

### 508 · R2870

**Calibrating Generative AI Use for Sustainable Higher Education: Cross-Sectional Evidence on Perceived Capability and Dependence**

2026 · Sustainability · journalarticle, review, article · en · https://doi.org/10.3390/su18199871

Generative artificial intelligence (GenAI) can support educational work while changing how users engage in independent generation and evaluation. This study examines whether the GenAI task use frequency has different associations with perceived role-specific capability and AI dependence. A cross-sectional survey of 1105 respondents (659 students and 446 teachers) from five Beijing universities measured all focal variables by self-report. Hierarchical regressions with HC3 standard errors were complemented by formal inverted U tests, bootstrap intervals, measurement-model sensitivity analyses, and nested out-of-fold prediction. Both capability outcomes showed positive lower-range and negative upper-range slopes, with the maxima located within the observed use range and supported by observations on both sides within each literacy stratum. Between the 25th and 75th percentiles of AI literacy, the model-implied maximum shifted by 0.715 use scale units for students (95% bootstrap CI [0.525, 0.973]) and 0.643 units for teachers (95% CI [0.450, 0.883]). The primary literacy measure was a 12-item mean; four-dimensional and second-order CFA specifications supported its interpretation as a broad composite. Separate exploratory dimension models yielded positive literacy-by-use interactions, with the largest point estimate for critical evaluation. Dependence was positively associated with use, habit, and trust and negatively associated with literacy. The combined squared use and interaction increments for dependence were 0.0024 and 0.0004, with 90% interval upper bounds of 0.0058 and 0.0031, below an exploratory 0.01 R2 benchmark. Belief-centred and trust omission specifications supported the broader reliance pattern, although trust and dependence remained conceptually close. Nonlinear ridge recovered most of the capability prediction improvement over linear ridge. The findings describe between-person associations, not individual optimal use levels or intervention effects. They motivate the evaluation of literacy-oriented task design and complementary approaches to trust calibration and habitual reliance.

**ИИ:** ? · обе модели · корреляты не названы · Self-report AI dependence measured; the correlates are use, habit, trust, literacy and perceived capability, which may count as self-efficacy.

**Решение:** =

---

### 509 · R2872

**Cognitive gains and addictive losses: The double-edged sword of Generative AI on employee creative thinking**

2026 · Acta Psychologica · article · en · https://doi.org/10.1016/j.actpsy.2026.107324

Drawing on Social Cognitive Theory (SCT), this study examines how Generative Artificial Intelligence (GAI) use is associated with employee creative thinking through creative self-efficacy and GAI addiction, and whether GAI use satisfaction moderates this process. A cross-sectional questionnaire survey was conducted among 194 knowledge workers in China. Confirmatory factor analysis was performed using AMOS 29.0, and the mediation, serial mediation, and moderation effects were tested using SPSS 26.0 and the PROCESS 4.2 macro with 5000 bootstrap samples. The results show that GAI use is positively associated with employee creative thinking, and creative self-efficacy mediates this relationship. Meanwhile, the tolerance dimension of GAI addiction is negatively associated with creative thinking, whereas the withdrawal pathway is not significant. Creative self-efficacy also negatively predicts both withdrawal and tolerance, suggesting its protective role in reducing GAI addiction risk. In addition, GAI use satisfaction strengthens the positive relationship between GAI use and creative self-efficacy. These findings indicate that the relationship between GAI use and creative thinking is not uniformly positive or negative, but depends on employees' ability beliefs, addiction-related risks, and affective evaluations of human-AI collaboration. This study provides an integrated perspective on the cognitive empowerment pathway, dependence risk pathway, and affective boundary condition of GAI use in workplace creativity.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey measuring GAI addiction (withdrawal, tolerance) and its relation to creative self-efficacy, a form of self-efficacy.

**Решение:** =

---

### 510 · R2873

**Cognitive load pathways linking generative AI dependency to university students' higher-order thinking skills and academic enjoyment**

2026 · Education and Information Technologies · article, journalarticle, review · en · https://doi.org/10.1007/s10639-026-14026-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Measures GenAI dependency; title names cognitive load, thinking skills and enjoyment (not core correlates), but other constructs are possible. No abstract.

**Решение:** =

---

### 511 · R2874

**Development of the GAI Dependence Scale: a validity and reliability study**

2026 · Current Issues in Personality Psychology · article, journalarticle · und · https://doi.org/10.5114/cipp/217837

Background While individuals use generative artificial intelligence (GAI) to enhance their productivity, they may also develop psychological and behavioral over-reliance on these tools. Evaluating the extent of an individual’s dependence on GAI is crucial for conducting related research. Participants and procedure The research involved 627 participants. Exploratory and confirmatory factor analysis was conducted to determine the construct validity of the scale. The results supported a structure consisting of four sub-dimensions and 19 items. The sub-dimensions are Usage Intensity, Content Dependence, Withdrawal Symptoms, and Negative Consequences. Results Confirmatory factor analysis indicated good model fit. Significant relationships were found with the GAI Dependence Scale, AI Dependence Scale (version of six items), and Behavioral Intention Scale during the analysis of the scale’s criterion validity. Cronbach’s α internal consistency, and the test-retest method were used to assess the reliability of the scale. Cronbach’s α internal consistency coefficient for the total score was found to be .92 for Sample 1 and .90 for Sample 2. Additionally, the test-retest reliability over a four-week interval yielded a coefficient of .81. Both coefficients are considered to indicate acceptable levels of reliability. Conclusions The scale is an effective and reliable tool for assessing individual dependence on GAI.

**ИИ:** разошлись — Opus ? (валидация шкалы: GAI dependence scale validation; abstract names only AI dependence and behavioural intention as validity measures; full text may report other correlates.); Sonnet + (валидация шкалы: GAI dependence scale development and validation study; criterion validity reported, likely with correlates; the abstract names none, but validation studies are eligible.)

**Решение:** ?

---

### 512 · R2881

**Generative AI dependency on programming among university students: a scale development and validation study.**

2026 · BMC psychology · article, journal article, validation study · eng · https://doi.org/10.1186/s40359-026-05011-5

With the rapid integration of generative artificial intelligence into programming education, concerns have emerged regarding university students' potential dependency on such technologies. However, there is a lack of validated instruments to systematically measure generative AI Dependency on programming contexts. To address this gap, the present study aimed to develop and validate the Scale of Generative AI Dependency on Programming among University Students. The study further seeks to contribute to the conceptualization of GenAI dependency as a context-specific construct in programming education, rather than treating students' reliance on GenAI as a general or undifferentiated form of technology use. Drawing on prior research and theoretical frameworks related to technology dependency and learning behaviors, an initial item pool was constructed to capture students' dependency on generative AI across three dimensions: cognitive, affective, and behavioral dependency. Using a convenience sampling approach, data were collected from 1,295 university students with programming learning experiences involving generative AI. Item analysis was first conducted to examine item discrimination and reliability. Exploratory factor analysis was then employed to identify the underlying factor structure of the scale, followed by confirmatory factor analysis to test the model fit and construct validity. In addition, Pearson correlation analyses were performed to provide evidence of criterion-related validity. The results were generally consistent with a three-factor structure with satisfactory reliability and validity, indicating that the scale may serve as a useful instrument for assessing generative AI Dependency on programming among university students. Theoretically, this study extends the application of the ABC framework to AI-supported programming education and provides preliminary evidence that GenAI dependency may involve interrelated cognitive, affective, and behavioral components. Practically, this scale provides researchers and educators with a useful tool for investigating students' dependency on generative AI in programming and for informing instructional design and intervention strategies in programming education.

**ИИ:** + · обе модели · валидация шкалы · Validation study of a GenAI dependency scale for programming; its criterion-validity correlations may include correlates of interest.

**Решение:** =

---

### 513 · R2882

**Human Intimate Relationships in the Post-Human Era: Emotional Interactions between Humans and AI Companions**

2026 · International Journal of Education and Humanities · journalarticle, article, journal-article · https://doi.org/10.54097/kys4zc78

With the explosive advancement of generative artificial intelligence, large language models and embodied virtual intelligence have transcended the functional boundaries of technical tools and constructed a brand-new intimate relationship paradigm between humans and AI companions. AI companions, covering text chat partners, virtual human lovers, voice emotional caregivers and digital embodied avatars, have become critical carriers for modern people to place inner emotions and satisfy intimate psychological demands. Traditional human intimate bonds such as romantic love, kinship and friendship are built on equal physical coexistence, mutual spontaneous emotional perception and shared real-life experiences. In contrast, emotional interactions between humans and AI reshape the logic of emotional sustenance, intimate expression and psychological attachment, bringing profound subversion to the traditional definition of intimate relationships in the post-human society. Existing social science research mostly separates artificial intelligence ethics and interpersonal relationship research, lacking systematic quantitative analysis of the formation mechanism, mediating factors and heterogeneous effects of human-AI emotional intimacy. This paper establishes a multi-dimensional research framework incorporating psychological expectation, monetization mode, virtual embodiment degree and long-term interaction frequency, categorizes AI companions into text-based lightweight companions, voice emotional partners, embodied virtual human companions and immersive metaverse AI partners for grouped comparative analysis. It extracts core mediating variables including response customization, emotional consistency, privacy security and anthropomorphic simulation level that regulate human-AI emotional bonding strength, and verifies differentiated interaction characteristics across adolescent, young adult and middle-aged user groups based on long-term user behavior dataset samples. This paper further summarizes typical emotional paradoxes such as "deep emotional attachment with simulated AI emotion" and "real loneliness behind virtual companionship", puts forward targeted guidance strategies for healthy human-AI emotional interaction segmented by user age groups, and prospects future research directions covering embodied AI intimacy, psychological dependency risk modeling and standardized emotional ethics evaluation systems. The research provides theoretical support and practical reference for social psychologists, AI product developers and social regulators to guide rational emotional communication between humans and artificial intelligence and prevent excessive psychological dependence on virtual companions.

**ИИ:** разошлись — Opus ? (мера зависимости неясна: Mostly conceptual framework on AI companion attachment; uses user behaviour data, but no clear dependence scale. Loneliness is mentioned.); Sonnet -2 (качественное или не эмпирическое исследование без количественной меры зависимости: Largely conceptual framework on human-AI companion intimacy; uses behavior dataset with no dependence scale or listed correlates; dependency risk only a future direction.)

**Решение:** ?

---

### 514 · R2885

**Personality profiles and usage experience are associated with trust and dependence on generative AI: a latent profile analysis.**

2026 · Frontiers in psychology · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpsyg.2026.1810554

Introduction: Generative artificial intelligence (GAI) is increasingly integrated into daily decision-making and task performance, as users rely on it to improve productivity, support decision-making, and reduce perceived human error. However, GAI outputs may contain inaccuracies, misleading content, or algorithmic biases. These issues may contribute to uncritical acceptance or excessive dependence among users, potentially posing risks to individuals and third parties. From an individual perspective, this study systematically explores how personality traits and text-based GAI usage experience interact in relation to users' trust in and dependence on text-based GAI. Methods: This study was based on a survey of 502 users measuring personality, usage experience, trust, dependence, self-efficacy, and critical thinking. Results: Significant interaction effects were found. Among high-experience users, the Well-Adjusted Type showed the highest dependence and self-efficacy, along with relatively high trust and critical thinking. The Outgoing-Unstructured Type showed the highest overall trust and, among high-experience users, the highest critical thinking, while its dependence did not differ significantly between low- and high-experience users. Overall, the Emotionally-Sensitive Type showed the lowest mean levels across the four outcomes, which may indicate a more cautious pattern of text-based GAI engagement. Discussion: These findings are discussed in relation to an evolutionary-cognitive perspective on how users may engage with human-like communicative cues in text-based GAI. The study emphasizes the importance of personalized text-based GAI usage strategies to mitigate misuse risks.

**ИИ:** + · обе модели · назван коррелят · Survey (n=502) measuring GAI dependence with personality profiles and self-efficacy; correlations likely reported.

**Решение:** =

---

### 515 · R2887

**Problematic generative AI use and mental health risks among Chinese university students: latent profiles, network structure, and health literacy as a modifiable resource.**

2026 · Frontiers in public health · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpubh.2026.1910408

Objective Generative artificial intelligence (GenAI) has become a routine academic tool for university students, but dysregulated use may co-occur with anxiety, sleep problems, psychological distress, and impaired academic functioning. This study examined GenAI-related digital behavior as a public health issue and assessed whether health literacy and self-regulated learning were associated with lower-risk profiles. Methods A cross-sectional survey was conducted among Chinese university students from six universities in eastern, central, and western China. A total of 2,140 questionnaires were submitted; after four-step data-quality screening, 1,872 valid responses were retained. Measures assessed GenAI-use dysregulation, academic anxiety, sleep problems, psychological distress, health literacy, self-regulated learning, academic engagement, and demographic and use-related covariates. Latent profile analysis identified GenAI-use and mental-health risk profiles. Profile differences were examined using omnibus and post hoc tests, multinomial logistic regression examined external factors associated with profile membership, and regularized network analysis identified central and bridge nodes. Results A four-profile solution showed the best balance of fit, entropy, class size, and interpretability (entropy = 0.891). The profiles were low-risk adaptive users (39.9%), anxiety-prone dependent users (25.7%), sleep-disrupted overusers (19.8%), and high-risk dysregulated users (14.6%). Confirmatory factor analysis supported the measurement structure of the adapted and selected scales (CFI = 0.958, TLI = 0.951, RMSEA = 0.036, SRMR = 0.041), and Harman's single-factor test did not indicate serious common method bias. Higher health literacy and self-regulated learning were associated with greater odds of low-risk rather than high-risk membership. Network analysis identified loss of control, academic worry, delayed bedtime, and academic avoidance as central or bridge nodes, whereas credibility evaluation and time management showed negative bridge expected influence. Conclusion GenAI-related digital behavior among university students varied in ways that involved dysregulated use, academic anxiety, sleep problems, distress, and academic functioning. These findings may help universities identify students who report difficulty controlling AI use, academic worry, delayed bedtime, academic avoidance, or trouble setting limits on AI use. They also point to health literacy, self-regulation, and time management as candidate resources for future longitudinal and intervention studies.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey measuring GenAI-use dysregulation alongside anxiety, sleep problems and psychological distress; network analysis likely reports correlations.

**Решение:** =

---

### 516 · R2888

**Psychological consequences of AI-assisted training and the buffering role of mindfulness.**

2026 · Acta psychologica · journal article, randomized controlled trial, journalarticle · eng · https://doi.org/10.1016/j.actpsy.2026.107595

The integration of artificial intelligence (AI) into athletic training is accelerating, yet its psychological implications for athletes remain insufficiently understood. Drawing on the transactional model of stress and the stress-buffering framework of mindfulness, this study examined whether mindfulness training can mitigate adverse psychological responses associated with AI-assisted training. Using a randomized controlled factorial design, 160 collegiate athletes were assigned to AI-assisted training or standard training, with or without concurrent mindfulness intervention, and assessed at baseline, week 4, and week 8. Athletes exposed to AI-assisted training without psychological support exhibited increases in perceived stress and AI dependence over time. In contrast, these stress increases were substantially attenuated when mindfulness training was implemented alongside AI-assisted training. A significant AI × Mindfulness × Time interaction emerged for perceived stress at post-intervention, and difference-in-differences analyses corroborated a robust buffering effect. Mediation analyses further indicated that mindfulness training reduced stress partially through enhancing mindful awareness; a three-wave cross-lagged analysis showed that mindful awareness and stress were reciprocally related over time, with the hypothesized awareness-to-stress pathway remaining robust. Together, these findings suggest that AI-assisted training introduces a distinct form of evaluative pressure, and that mindfulness training may serve as an effective psychological buffer during the adoption of continuous algorithmic performance evaluation systems.

**ИИ:** ? · обе модели · мера зависимости неясна · RCT measured AI dependence, stress and mindfulness, but the AI is an athletic performance-evaluation system and may not be conversational.

**Решение:** =

---

### 517 · R2889

**Research on AIGC Dependence Behavior and Digital Media Literacy Cultivation Paths of College Students in Guangzhou Universities in the Digital Intelligence Era — An Empirical Analysis Based on Educational Statistics and Data Mining**

2026 · conference-paper · https://doi.org/10.1145/3828183.3828308

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Empirical study of AIGC dependence among college students; correlates unknown, possibly only media literacy.

**Решение:** =

---

### 518 · R2893

**Stressed minds, smart tools: How academic expectation stress fuels generative AI dependency in Chinese higher education**

2026 · The Internet and Higher Education · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.iheduc.2026.101094

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · назван коррелят · No abstract, but the title links academic expectation stress to generative AI dependency in Chinese students, which suggests a quantitative study.

**Решение:** =

---

### 519 · R2894

**The Comparative Trap: How Social Comparison Orientation Drives Problematic Generative AI (GenAI) Use**

2026 · International Journal of Human-Computer Interaction · journalarticle, preprint/article, article · en · https://doi.org/10.1080/10447318.2026.2668619

Although Generative AI (GenAI) enhances task efficiency in the short term, it is linked to competitive pressures that sustain individuals’ fear of being replaced, thereby increasing the risk of problematic use. Current research has focused on individual psychological vulnerabilities but has overlooked the social-comparison context that derives from GenAI. This study examines the relationships between social comparison orientation and problematic GenAI use and explores their indirect effects through affective and cognitive mechanisms, based on the Interaction of Person-Affect-Cognition-Execution (I-PACE) model. The study analyzed data from 396 Chinese GenAI users using structural equation modeling (SEM) with bootstrap techniques. Results show that social comparison orientation has a significant direct association with problematic GenAI use and follows a pattern consistent with links to AI flow and perceived irreplaceability via fear of missing out (FoMO), ultimately connecting to problematic GenAI use.

**ИИ:** + · обе модели · назван коррелят · An SEM survey of 396 Chinese GenAI users that links problematic GenAI use to FoMO, which is one of the correlates of interest.

**Решение:** =

---

### 520 · R2895

**The double-edged impact of generative artificial intelligence dependence on service innovation in the hospitality industry: A self-regulation perspective**

2026 · International Journal of Hospitality Management · article, journalarticle · eng · https://doi.org/10.1016/j.ijhm.2025.104392

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; GenAI dependence among hospitality employees, self-regulation framing may involve self-efficacy or self-control correlates.

**Решение:** =

---

### 521 · R2898

**The relationship between academic self-efficacy and GenAI dependence among college students: a chain mediation model of academic stress and perceived usefulness of GenAI.**

2026 · Frontiers in psychology · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpsyg.2026.1784354

Background: As generative artificial intelligence (GenAI) becomes increasingly integrated into higher education, concerns have emerged regarding students' growing reliance on GenAI for academic tasks. Although prior studies have examined the educational benefits of GenAI, limited research has explored the psychological mechanisms underlying students' dependence on these technologies. This study investigated whether academic self-efficacy predicts GenAI dependence and examined the mediating roles of academic stress and perceived usefulness of GenAI. Methods: Using a time-lagged survey design, data were collected from 428 college students from five universities in eastern China. Participants completed validated measures of academic self-efficacy, academic stress, perceived usefulness of GenAI, and GenAI dependence. Structural equation modeling and bootstrap analyses were conducted to examine the hypothesized mediation pathways. Results: Academic self-efficacy was significantly and negatively associated with GenAI dependence. Academic stress and perceived usefulness of GenAI each served as significant mediators between academic self-efficacy and GenAI dependence. Furthermore, academic stress was positively associated with perceived usefulness of GenAI, and the sequential pathway from academic self-efficacy to academic stress, perceived usefulness of GenAI, and GenAI dependence was significant. Specifically, students with lower academic self-efficacy experienced greater academic stress, which increased their perceptions of the usefulness of GenAI and subsequently strengthened their dependence on GenAI. Conclusion: Academic self-efficacy affects college students' GenAI dependence both directly and indirectly through academic stress and perceived usefulness of GenAI. The findings extend the application of the I-PACE framework to the context of generative artificial intelligence and provide practical insights for universities seeking to promote responsible GenAI use, enhance students' independent learning capabilities, and mitigate excessive reliance on AI-assisted learning tools.

**ИИ:** + · обе модели · назван коррелят · Time-lagged survey relating GenAI dependence to academic self-efficacy and academic stress in 428 college students.

**Решение:** =

---

### 522 · R2900

**When AI works, employees worry: the vigilance cost of AI delegation in hybrid work.**

2026 · Frontiers in psychology · journal article · eng · https://doi.org/10.3389/fpsyg.2026.1914119

Hybrid work and AI-assisted technologies have transformed not only where employees work but also how work remains psychologically active after formal working hours. This study develops the AI delegation paradox, which proposes that although AI can reduce the effort required to execute work tasks, it may simultaneously increase employees' need to monitor, evaluate, and remain accountable for work processes that continue through AI-assisted systems. Building on this argument, the study introduces AI process vigilance (AIPV), a second-order construct capturing sustained cognitive attachment to delegated AI-assisted work through progress monitoring, output quality concern, error anticipation, and loss of control. Using a two-wave survey design with a seven-week interval, data were collected from 642 hybrid employees who used AI tools for work at least weekly. The results supported a sequential pathway in which continuous AI availability was linked to greater AI delegation dependence, delegation dependence predicted higher levels of AI process vigilance, vigilance increased work-related rumination, rumination undermined psychological detachment, and lower detachment was associated with poorer recovery outcomes. The hypothesized moderating role of boundary management preference was not supported. These findings suggest that recovery impairment may arise not only because employees continue working after hours, but also because they remain psychologically engaged with work processes that have been delegated to AI. By demonstrating that responsibility and concern often persist even when task execution is transferred to intelligent systems, the study identifies a previously overlooked recovery cost of AI-assisted work and extends current understanding of recovery, boundary management, and human-AI collaboration in contemporary work environments.

**ИИ:** ? · обе модели · корреляты не названы · Two-wave survey measures AI delegation dependence with rumination, detachment and recovery outcomes; the recovery measures might include well-being or stress.

**Решение:** =

---

### 523 · R2901

**When AIGC Becomes a Work Partner: Emotional and Technical Dependence and Work Behavior**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.6403040

Grounded in media system dependency theory, this study examines how employees’ emotional and technical dependence on artificial intelligence generated content (AIGC) shape their work behaviors as AIGC increasingly functions as a collaborative partner. The findings suggest that frequent interaction with AIGC simultaneously creates opportunities for innovative work outcomes while introducing new challenges for interpersonal coordination and team collaboration. On the one hand, employees’ high AIGC interaction frequency strengthens their emotional dependence on AIGC, thereby weakening task interdependence. On the other hand, such high AIGC interaction frequency also enhances their technical dependence on AIGC, which in turn promotes employees’ innovative behaviors. Notably, these two mediating mechanisms operate in parallel rather than sequentially. Taken together, the results underscore the need for managers to actively guide employees in balancing innovation-oriented engagement with AIGC and sustained collaborative involvement within teams, enabling the joint advancement of individual and collective performance.

**ИИ:** разошлись — Opus ? (корреляты не названы: Measures employees' emotional and technical dependence on AIGC; listed outcomes (task interdependence, innovation) aren't correlates, but full text may report others.); Sonnet -4 (среди измеренных конструктов нет ни одного нашего коррелята: Measures emotional/technical AIGC dependence, but the listed constructs are interaction frequency, task interdependence and innovative behavior, none a correlate of interest.)

**Решение:** -

---

### 524 · R2902

**A Reproducible Survey-Scoring And C5.0 Decision-Tree Workflow For Classifying Self-Reported Higher-Order Thinking In Generative AI-Supported Learning.**

2026 · Journal of visualized experiments : JoVE · journal article, video-audio media, research support, non-u.s. gov't · eng · https://doi.org/10.3791/71447

Generative artificial intelligence is increasingly used in higher education, but researchers still need transparent procedures for collecting, scoring, and organizing learner-level survey data in this rapidly changing context. This article presents a reproducible survey-scoring and C5.0 decision-tree workflow for classifying self-reported higher-order thinking among college students who have used generative artificial intelligence tools for academic learning. The protocol covers participant recruitment, questionnaire administration, response-quality screening, composite-score calculation, binary coding, training-testing partitioning, C5.0 tree construction, pruning, model-output export, and interpretation of node-based classification paths. The workflow is demonstrated using a single-university survey dataset of 776 undergraduate students collected in China from March 7 to March 15, 2023. Higher-order thinking is operationalized as a self-reported questionnaire score rather than as directly observed cognitive performance. In the demonstration dataset, the pruned tree retained eight learner-related variables: generative artificial intelligence anxiety, trust in generative artificial intelligence, problematic smartphone use, academic procrastination, academic performance, parental upbringing, negative emotions, and attitudes toward generative artificial intelligence. The retained model achieved 89.52% accuracy in the training subset and 86.21% accuracy in the testing subset. However, class-specific evaluation showed uneven performance, with substantially weaker recall for the Low-HOT class than for the High-HOT class. Therefore, the tree should be interpreted as an auxiliary, interpretable workflow demonstration rather than as a validated screening tool. This protocol may support researchers who require a documented and repeatable procedure for survey-based learner profiling in generative artificial intelligence-supported learning environments.

**ИИ:** разошлись — Opus ? (мера зависимости неясна: Survey has correlates (smartphone use, procrastination); only pruned-tree variables are listed, so an unlisted GenAI dependence measure is possible.); Sonnet -3 (нет меры зависимости от ИИ: только частота использования, принятие, доверие, грамотность, технострес, страх ИИ — или over-reliance только как поведение в эксперименте: Decision-tree workflow classifying higher-order thinking; variables include AI anxiety, trust, attitudes, but no AI dependence or addiction measure.)

**Решение:** ?

---

### 525 · R2904

**AI-Use Dependency and Career Search Self-Efficacy among University Students: Serial Mediation by Employment Anxiety and Generative AI Acceptance**

2026 · Springer Science and Business Media LLC · posted-content · https://doi.org/10.21203/rs.3.rs-10303966/v1

Abstract Objective This study examined the mechanism linking AI-use dependency tendency with career search self-efficacy among university students, focusing on the separate and serial mediating roles of future employment anxiety and generative AI acceptance. By incorporating these four constructs into a unified framework, it investigates how technology dependency may relate to career-development beliefs through emotional experience and technology acceptance and provides evidence for career guidance and AI literacy education. Methods This study used an online self-administered cross-sectional survey of students enrolled in Chinese higher education institutions. Convenience sampling was conducted through Wenjuanxing. Of 2,258 questionnaires returned, 1,792 were retained after invalid responses were excluded (valid response rate = 79.36%). The sample included students of different genders, academic years, and educational levels. Four established instruments—AIDep-22, FEAS, GAIAS, and CSES—were administered. Reliability analysis and confirmatory factor analysis evaluated internal consistency, measurement-model fit, convergent validity, and composite reliability. SPSSAU 26.0 was used for statistical analysis, and the serial indirect effects were tested using 5,000 bootstrap resamples and 95% percentile bootstrap confidence intervals. Results AI-use dependency tendency was positively associated with career search self-efficacy and generative AI acceptance and negatively associated with future employment anxiety. Future employment anxiety and generative AI acceptance each showed a significant indirect effect, and their serial indirect pathway was significant. After both mediators entered the model, the direct effect was no longer significant, suggesting that the relationship operated primarily through indirect mechanisms. Generative AI acceptance showed the strongest mediating effect. Conclusion The findings indicate that AI-use dependency tendency relates to career search self-efficacy mainly through lower future employment anxiety, higher generative AI acceptance, and the serial pathway between these mediators. AI-use dependency should therefore not be interpreted solely as negative technological attachment; in career exploration, it may function as a positive resource when accompanied by emotional buffering and informed technology acceptance. The results support integrating responsible AI-use education, employment-related psychological support, and career guidance in higher education. Because the design was cross-sectional, the indirect pathways do not establish causality.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey (N=1,792); AIDep-22 dependence scale linked to career search self-efficacy and future employment anxiety.

**Решение:** =

---

### 526 · R2905

**Causes, Impacts, and Governance Paths of Dependence on AI Companions in the Era of Generative AI**

2026 · Advances in Social Science, Education and Humanities Research/Advances in social science, education and humanities research · book part, book-chapter, conference-paper · en · https://doi.org/10.2991/978-2-38476-609-3_51

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title is about dependence on AI companions and sounds conceptual, but it could include survey data.

**Решение:** =

---

### 527 · R2906

**Development and validation of a digital burnout scale in artificial intelligence era**

2026 · Frontiers in Psychology · article · en · https://doi.org/10.3389/fpsyg.2025.1580422

Introduction: The rapid adoption of AI-driven digital technologies in higher education has intensified students' exposure to digital demands, increasing the risk of digital burnout. Existing research lacks validated instruments that capture the multidimensional nature of digital burnout in AI-enhanced learning environments. This study aimed to develop and validate a comprehensive Digital Burnout Scale for college students, grounded in the Stressor-Strain-Outcome (SSO) model and Conservation of Resources (COR) theory. Methods: Using a multi-stage mixed-methods design, the study first conducted qualitative interviews to generate item pools, followed by large-scale survey data for quantitative validation. Exploratory and confirmatory factor analyses were performed to establish construct validity, supplemented by reliability testing and model comparison. Results and discussion: Findings supported a six-dimension structure of digital burnout: Digital Aging, Emotional Exhaustion, Cognitive Overload, Cognitive Dissonance, Digital Deprivation, and Behavioral Addictions. All dimensions demonstrated satisfactory convergent and discriminant validity, indicating strong psychometric robustness of the scale. The scale provides a reliable and theory-driven tool for assessing student digital burnout in the AI era. It offers practical value for educators and administrators seeking to identify high-risk groups and design targeted interventions.

**ИИ:** разошлись — Opus ? (мера зависимости неясна: Digital burnout scale with a Behavioral Addictions dimension; unclear whether it targets AI tools specifically or digital technology generally.); Sonnet -3 (нет меры зависимости от ИИ: только частота использования, принятие, доверие, грамотность, технострес, страх ИИ — или over-reliance только как поведение в эксперименте: Digital burnout scale in AI-era higher education; it measures general digital burnout, not dependence on an interactive AI system.)

**Решение:** ?

---

### 528 · R2909

**Narcissistic traits and emotional dependence on large language models among adolescents**

2026 · Frontiers in Psychiatry · journalarticle, review, article · en · https://doi.org/10.3389/fpsyt.2026.1958023

Background This study examined associations between narcissistic traits and emotional dependence on large language models (LLMs) among adolescents, focusing on anxiety and physical activity. Methods A multistage stratified sample of 1622 Chinese junior high school students was surveyed in November 2025. Narcissistic traits, anxiety, LLM emotional dependence, and physical activity were assessed using the FFNI-SF, GAD-2, an adapted five-item LLM emotional dependence measure, and PARS-3, respectively. Pearson correlations and PROCESS Models 4 and 7 with 5,000 bootstrap resamples were conducted, with Johnson–Neyman analysis used to probe the interaction. Results Narcissistic traits correlated positively with anxiety (r=0.118, P&amp;lt;0.001) and LLM emotional dependence (r=0.301, P&amp;lt;0.001), while anxiety correlated positively with LLM emotional dependence (r=0.146, P&amp;lt;0.001). Physical activity correlated negatively with anxiety (r=−0.119, P&amp;lt;0.001) and LLM emotional dependence (r=−0.075, P = 0.002). Adjusting for grade and left-behind status, anxiety showed a small indirect association between narcissistic traits and LLM emotional dependence (Effect=0.011, 95% CI [0.004, 0.020]). The narcissistic traits × physical activity interaction was significant (β=−0.056, P = 0.015), with the narcissism–anxiety association significant below 0.73 SD of physical activity. The moderated mediation index was not significant (Index=−0.0061, 95% bootstrap CI [−0.0130, 0.0001]). Conclusion Narcissistic traits were positively associated with adolescent LLM emotional dependence, with a small cross-sectional indirect association through anxiety. Physical activity moderated the narcissism–anxiety association, although overall moderated mediation was not supported.

**ИИ:** + · обе модели · назван коррелят · Adolescent survey (N=1622) reporting correlations between LLM emotional dependence and anxiety (GAD-2), plus narcissism; empirical despite the 'Review' tag.

**Решение:** =

---

### 529 · R2911

**Risk perception and generative AI discontinuance intention: mediating effect of cognitive fatigue and moderating effect of AI dependence.**

2026 · Frontiers in psychology · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyg.2026.1879080

With the rapid popularization of generative artificial intelligence (AI), the risks of misinformation dissemination and user privacy leakage have become key factors influencing users' decisions on the continuous use of AI. Most existing studies focus on the driving mechanisms of AI adoption, while there is insufficient exploration of the reasons for negative usage outcomes, especially the reasons for users to discontinue using the technology. Based on the cognitive-affective-behavioral (C-A-B) framework, this study analyzes the data from 426 valid questionnaires to explore how risk perception affects users' intention to discontinue using AI, identify the mediating role of cognitive fatigue, and the moderating role of AI dependence—which refers to users' deep psychological and behavioral attachment to AI tools and differs from casual habitual use and general technology reliance. The study finds that both the misinformation risk perception and privacy risk perception significantly increase AI anxiety, and this effect is further strengthened by increased misinformation fatigue and privacy fatigue. Meanwhile, AI anxiety significantly promotes users' intention to discontinue using AI, and AI dependence has a negative moderating effect on this relationship. Therefore, cognitive fatigue is an important mediating mechanism connecting risk perception and affective response, and affective factors are key antecedent variables driving users' technology discontinuation intention.</jats:p

**ИИ:** + · обе модели · назван коррелят · Survey (n=426) measuring AI dependence as a moderator alongside AI anxiety, a correlate of interest; the correlation table is likely reported.

**Решение:** =

---

### 530 · R2915

**Development of the AI Dependency and Engagement (AIDE) Questionnaire: A Novel Survey Instrument for Clinical Assessment of Harmful AI Use − A Preliminary Report**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7386747

Background: Emerging evidence describes both development and exacerbation of psychosis associated with artificial intelligence (AI) chatbot engagement. Despite growing recognition of AI use as a clinically relevant psychosocial exposure, a comprehensive survey instrument validated in English and representative of a diverse sample remains unavailable. The aim of this study is to test the acceptability, accessibility, and content and face validity of a novel survey instrument for identifying clinically significant AI engagement and patients at risk for harmful AI use. &lt;div&gt; &lt;br&gt; &lt;/div&gt; &lt;div&gt; Methods: We developed a 17-question survey tool, the AI Dependency and Engagement (AIDE) questionnaire, consisting of 7-multiple choice questions characterizing one’s AI use and 10 Likert scale questions for AI dependency scoring. We consulted a panel of nine experts for confirmation of content validity and conducted a pilot to assess for face validity and accessibility. &lt;/div&gt; &lt;div&gt; &lt;br&gt; &lt;/div&gt; &lt;div&gt; Results: Fifty participants aged 18-74 years completed the questionnaire, all of whom reported that the survey was easily understandable and of appropriate length. The survey was feasible to complete in a clinical setting, with 96% of participants able to complete the survey without any assistance, and average completion time was under 3 minutes. &lt;/div&gt; &lt;div&gt; &lt;br&gt; &lt;/div&gt; &lt;div&gt; Conclusion: We demonstrated the new AIDE questionnaire to have strong content and face validity, be quick to administer, and be acceptable and accessible to the general population. We recommend its use as a standard screening tool for routine evaluation for clinically significant AI dependency and harmful AI use. &lt;/div&gt;

**ИИ:** ? · обе модели · корреляты не названы · New AI dependency scale (AIDE), but the pilot (n=50) tested only content/face validity; unclear whether any correlates of interest were measured.

**Решение:** =

---

### 531 · R2917

**Healthy bonds or pathological ties? Unpacking emotional dependence on AI through rumination and metacognitive awareness**

2026 · Telematics and Informatics · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.tele.2026.102404

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a quantitative study of emotional dependence on AI with rumination and metacognition. Other eligible correlates are plausible.

**Решение:** =

---

### 532 · R2922

**Examining university students addiction toward generative AI: an I-PACE perspective**

2026 · International Journal of Mobile Communications · journalarticle, article, journal-article · en · https://doi.org/10.1504/ijmc.2027.10080155

Inderscience is a global company, a dynamic leading independent journal publisher disseminates the latest research across the broad fields of science, engineering and technology; management, public and business administration; environment, ecological economics and sustainable development; computing, ICT and internet/web services, and related areas.

**ИИ:** ? · обе модели · нет аннотации · Abstract is publisher boilerplate; title points to a quantitative I-PACE study of GenAI addiction that likely includes psychological correlates.

**Решение:** =

---

### 533 · R2933

**Over-reliance on AI in information tasks: Unraveling the roles of reasoning visibility and task complexity**

2026 · Telematics and Informatics · article · en · https://doi.org/10.1016/j.tele.2026.102464

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Title suggests an experiment with behavioural over-reliance, but a self-report measure and eligible correlates can't be ruled out.

**Решение:** =

---

### 534 · R2934

**Perceived AI empowerment and threat in relation to university students' dependence on GenAI: the indirect role of trust in AI.**

2026 · Frontiers in psychology · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpsyg.2026.1940317

Introduction: The widespread adoption of generative artificial intelligence (GenAI) in higher education is transforming students' learning practices, yet the psychological factors and associational processes underlying students' dependence on GenAI remain poorly understood. Drawing on cognitive appraisal theory and trust theory, this study proposed a dual-appraisal model to examine how perceived AI empowerment and perceived AI threat are associated with university students' dependence on GenAI, both directly and indirectly through trust in AI. Methods: A cross-sectional survey was conducted with 360 university students in China who had prior experience using GenAI. The measurement model and hypothesized structural relations were examined using SPSS 24.0 and Mplus 8.3. Indirect associations were evaluated using bootstrap confidence intervals based on 5,000 resamples. Results: Perceived AI empowerment was positively associated with trust in AI and dependence on GenAI, whereas perceived AI threat was negatively associated with both variables. Trust in AI was positively associated with GenAI dependence and statistically accounted for part of the associations between both cognitive appraisals and dependence. Significant direct and indirect associations were observed in both appraisal pathways. Conclusion: The findings support a dual-appraisal perspective on university students' dependence on GenAI, suggesting that perceived capability-enhancing benefits and perceived risks are associated with reliance on GenAI through distinct appraisal pathways involving trust. Students who perceived GenAI as more empowering tended to report greater trust and dependence, whereas those who perceived greater AI-related threat reported lower trust and dependence. Trust accounted for significant indirect associations between both forms of appraisal and GenAI dependence. These findings extend research on technology acceptance by highlighting trust as a potential psychological pathway linking students' appraisals of GenAI with their reported reliance on the technology.

**ИИ:** ? · обе модели · корреляты не названы · GenAI dependence was measured; perceived AI threat might count as AI-related anxiety, but the other constructs (empowerment, trust) are not correlates of interest.

**Решение:** =

---

### 535 · R2935

**The Double-Edged Sword of AI Efficiency: Self-Efficacy Erosion as a Mediator Linking Instant Gratification and Perceived AI Efficacy to AI Dependency.**

2026 · Behavioral sciences (Basel, Switzerland) · article, journal article, journalarticle · eng · https://doi.org/10.3390/bs16040530

Generative AI is becoming integral to daily workflows, fostering a novel form of functional cognitive AI dependency distinct from pathological addiction. While emerging research acknowledges this phenomenon, the specific psychological mechanisms underpinning its development remain underexplored. Incorporating self-efficacy erosion into the reinforcement-based framework, this study investigates whether instant gratification and perceived AI efficacy as key drivers of AI dependency. We examine the model using Structural Equation Modeling (SEM) with cross-sectional data collected from 576 users who have engaged with AI. The results show that both instant gratification and efficient rewards are positively associated with individuals' AI dependency. Furthermore, users' self-efficacy erosion significantly mediates the positive relation, supporting the hypothesis that greater reliance on AI is related to lower self-belief and stronger AI dependency. Moderation analyses further indicate that task-domain self-efficacy and social norms strengthen these positive associations. These findings provide empirical support for a mechanism associated with functional AI dependency and offer insights for navigating human-AI interaction while promoting balanced AI adoption.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional SEM survey (N=576) that measures AI dependency together with self-efficacy erosion and task-domain self-efficacy, which are correlates of interest.

**Решение:** =

---

### 536 · R2939

**Cognitive and emotional dynamics of artificial intelligence-assisted English learning: A mixed-methods study in a dual instructional context.**

2026 · Acta psychologica · journal article · eng · https://doi.org/10.1016/j.actpsy.2026.106673

Artificial intelligence (AI) tools have become increasingly integrated into university-level English learning, yet their pedagogical role within input-based instruction and English-medium education remains insufficiently understood. This mixed-methods study examines how first-year students in a Thai higher education institution use AI applications to support English learning, how they emotionally experience AI-assisted learning, and how the frequency of AI use relates to these emotional dynamics. The study was situated within a year-long storytelling-based English curriculum grounded in input-based pedagogy informed by Krashen's Input Hypothesis, alongside broader English-medium instruction across non-language courses. Survey data from 82 students, using validated subscales on AI use and emotional responses, were analyzed alongside reflective essays and interviews with 11 students. Quantitative findings indicate that students engage with AI moderately to frequently, primarily for grammar checking, writing assistance, and idea generation. Students reported increased confidence and excitement but also experienced frustration and concerns about dependency. Correlation analyses revealed strong positive associations between AI use and confidence and excitement, with moderate relationships with frustration and dependency. Qualitative findings portray AI as a supportive "learning partner" that enhances clarity and self-directed revision, while simultaneously encouraging reliance on automated guidance. The study contributes to current debates on AI in language education by demonstrating how, within input-based and English-medium learning environments, AI can both facilitate learner autonomy and risk over-dependence, accentuating the need for pedagogical strategies that cultivate reflective, critical, and gradually more independent language learning.

**ИИ:** ? · обе модели · корреляты не названы · Survey has a dependency subscale; the other measures (confidence, excitement, frustration) only loosely match correlates of interest such as self-efficacy.

**Решение:** =

---

### 537 · R2945

**From Critical Thinking to Passive Acceptance: The Moderating Role of Decision Fatigue in Students' Use of Generative AI.**

2026 · European journal of investigation in health, psychology and education · journal article · eng · https://doi.org/10.3390/ejihpe16090130

Academic research on Artificial Intelligence (AI) has primarily focused on usage motivations, AI literacy, trust, overreliance, and critical use. However, the mechanisms through which critical thinking influences passive reliance on AI-generated output in academic contexts remain largely unexplored. This study examined the role of Critical Thinking and Decision Fatigue in students' passive acceptance of AI-generated output. A sample of 383 Italian university students completed an online survey including the Critical Thinking Disposition Scale and the Decision Fatigue Scale. Of these, 332 students reported having used GenAI in the previous three months and were presented with six task-specific items assessing reliance on unmodified AI-generated output across six academic tasks (Idea generation, Text generation, Text revision, Creating quizzes, Receiving feedback, and Information search). Multiple hierarchical regression analyses tested the moderating role of Decision Fatigue. Decision Fatigue was not a significant direct predictor but moderated the relationship between Critical Thinking and passive acceptance in several academic activities, with the strength of this evidence varying according to the applied correction for multiple comparisons. The findings highlighted the role of critical thinking as a protective filter against the passive use of generative AI. However, this disposition is not always available, particularly under conditions of cognitive fatigue. The study offers new educational insights into the need to design instructional interventions that foster critical thinking while promoting cognitively sustainable learning environments.

**ИИ:** разошлись — Opus ? (другое: Self-reported over-reliance on AI output; the only correlates are critical thinking and decision fatigue. Decision fatigue is borderline, close to self-control or distress.); Sonnet -4 (среди измеренных конструктов нет ни одного нашего коррелята: Measures passive reliance on AI output with critical thinking and decision fatigue only; neither is a listed correlate, and no dependence scale is used.)

**Решение:** ?

---

### 538 · R2948

**Beyond Learning Gains: Excessive AI Use and the Rise of Imposter Syndrome in Higher Education**

2026 · Academy of Management Proceedings · journalarticle, conference-abstract · en · https://doi.org/10.5465/amproc.2026.10566abstract

Students in higher education will experience significant changes in their learning performance as collaboration with artificial intelligence becomes commonplace. However, this study explores how excessive AI usage affects psychological process of students. To understand the phenomena, we conducted two studies. Study 1(a) through an experimental study, employing analytic tasks, specifically designed to challenge students’ ability to construct, synthesize, and conceptualize ideas, we examine how the AI use affects the student’s psychological process. Students completed identical tasks under two conditions with and without AI intervention in a controlled laboratory setting. In Study 1(b), we conducted empirical studies to deeply understand excessive AI usage results in imposter syndrome which leads to psychological distress among students. In study 2 conducted interviews from 38 teachers from different fields who further validated these results. Based on these findings, we elaborate that excessive AI use evoke imposter like feelings such as fraudulent, inadequacy, and fear of being exposed as incompetent (imposter syndrome), ultimately heightens the feelings of stress, anxiety, and depression (psychological distress) among students. At the same time this paper will assist educators and policymakers’ needs to target students’ self-perception and competence to counter the deep-rooted phenomenon like imposter syndrome, rather than solely relying on recovery strategies. These findings advance understanding on double-edged nature of human-AI interaction and offer valuable insights for promoting students’ wellbeing in higher education setting.

**ИИ:** ? · обе модели · мера зависимости неясна · Survey links 'excessive AI use' to psychological distress (stress, anxiety, depression); unclear whether it is a dependence/problematic-use measure or just use intensity.

**Решение:** =

---

### 539 · R2949

**From Prompts to Dependency: Standardization of the AI Chatbot Dependence Scale In A Turkish Context And Associations With Big Five Personality Traits**

2026 · International Journal of Human-Computer Interaction · article, journalarticle, journal-article · en · https://doi.org/10.1080/10447318.2026.2629519

With the rapid spread of AI-powered chatbots in various domains, concerns have emerged regarding potential psychological dependencies on these technologies. This study aimed to standardize the Artificial Intelligence Chatbot Dependence Scale (AICDS) for a Turkish university student sample and to examine its psychometric properties and associations with demographic features, and Big Five personality traits. Data were collected from 819 participants aged 18–36. Exploratory and confirmatory factor analyses supported an unidimensional structure after removing two items, yielding a six-item scale with strong internal consistency (α = 0.86) and temporal stability. Women reported significantly higher dependency scores than men. However, personality traits did not significantly differ between AI chatbot users and non-users. Results indicated that while neuroticism was a significant predictor, personality traits overall played a limited role. This validated Turkish version of the AICDS provides a reliable tool for future research and interventions targeting excessive reliance on AI chatbots.

**ИИ:** + · обе модели · валидация шкалы · Turkish validation of the AI Chatbot Dependence Scale, with associations to Big Five traits (neuroticism was a predictor).

**Решение:** =

---

### 540 · R2954

**Exploring the Relationship between Fear of Being without Artificial Intelligence, AI Addiction, and Academic Self-Efficacy among University Students**

2026 · Osmangazi Journal of Educational Research · article, journalarticle, journal-article · und · https://doi.org/10.59409/ojer.1755463

This study examined the links between AI addiction, academic self-efficacy, related anxieties, and fear of being without AI in education (AILPES). The study employed a descriptive and correlational design and collected data from 544 undergraduate students. Data collection tools included a Personal Information Form, the Artificial Intelligence Addiction Scale, the Academic Self-Efficacy Scale, and the Fear of Being Without Artificial Intelligence in Education Scale. Descriptive statistics were used to summarize demographic characteristics and study variables, while Pearson correlation coefficients were calculated to examine bivariate relationships among variables. Multiple linear regression analysis was conducted to test the predictive effects of ASE, AIAS, and grade point average (GPA) on AILPES. The findings indicated that age was negatively associated with AILPES and lack of academic confidence without AI. ASE was positively related to both AILPES and academic self-efficacy anxiety. AIAS demonstrated strong positive correlations with AILPES, academic self-efficacy anxiety, and lack of academic confidence without AI. The results revealed that fear of being without AI among university students is significantly associated with both AI addiction and academic self-efficacy. While AI addiction increases this fear, higher academic self-efficacy appears to reduce it. Based on these findings, it is recommended that higher education institutions implement educational and psychoeducational strategies to promote balanced AI use, enhance AI literacy, and support students’ academic self-efficacy. The findings highlight the importance of educational strategies aimed at enhancing AI literacy and promoting digital balance.

**ИИ:** + · обе модели · назван коррелят · The AI Addiction Scale was correlated with academic self-efficacy and with AI-related anxiety (fear of being without AI) in 544 students.

**Решение:** =

---

### 541 · R2956

**Psychometric evaluation of the Turkish version of the AI Chatbot Dependence Scale (AICD-8)**

2026 · Discover Psychology · article, journalarticle, journal-article · en · https://doi.org/10.1007/s44202-026-00801-9

The rapid integration of generative artificial intelligence-based chatbots into daily life has intensified discussions about their potential association with problematic use and addiction-like behaviors. In this context, several psychometric scales have been developed to assess problematic chatbot use including the eight-item AI Chatbot Dependence Scale (AICD-8). However, the AICD-8 has not been validated into Turkish. Therefore, the present study translated the AICD-8 into Turkish, and its psychometric properties were evaluated. The sample comprised 600 individuals (249 employees and 351 university students). Descriptive statistics, reliability indicators (Cronbach’s alpha, McDonald’s omega, and composite reliability), Pearson correlation coefficients, and confirmatory factor analysis (CFA) were conducted to examine the psychometric properties of the scale. The Turkish version of the scale (AICD-8-T) demonstrated good internal consistency, and CFA confirmed that the single-factor model exhibited acceptable fit. Convergent validity was supported through strong associations between the AICD-8-T and the Problematic ChatGPT Use Scale. Nomological validity was evidenced by expected correlations with social media addiction, loneliness, and internet addiction. Criterion-related validity was supported by strong positive correlations with daily ChatGPT use and chatbot use. Overall, the findings indicate that the AICD-8-T possesses robust psychometric qualities and can be reliably used in future psychological research in Türkiye.

**ИИ:** + · обе модели · валидация шкалы · Turkish validation of the AICD-8, with correlations with loneliness, social media addiction and internet addiction.

**Решение:** =

---

### 542 · R2972

**ИИ-зависимость как предиктор академической прокрастинации у студентов: феноменология, механизмы и риски для психологического здоровья**

2026 · International journal of medicine and psychology. · journalarticle, article · ru · https://doi.org/10.58224/2658-3313-2026-9-5-210-218

актуальность исследования определяется стремительной интеграцией генеративных систем искусственного интеллекта в образовательную среду, порождающей новые формы дисфункционального учебного поведения и создающей риски для психологического здоровья студентов. Цель исследования – изучение характера взаимосвязи между ИИ-зависимостью, академической прокрастинацией и псевдопродуктивностью у студентов, а также выявление психологических механизмов данной связи и её последствий для психологического здоровья. Эмпирическое исследование проведено на выборке студентов направления подготовки 37.03.01 Психология Сибирского федерального университета (n = 85; возраст 18-25 лет, M = 20,4; SD = 1,7; 61% женщин, 39% мужчин). В качестве диагностического инструментария применялись шкала зависимости от ИИ DAI (Morales-García et al., 2024; авторский перевод), шкала прокрастинации Б. Тукмана (TPS) и авторский блок вопросов для операционализации псевдопродуктивности. Корреляционный анализ выявил положительную статистически значимую связь между ИИ-зависимостью и уровнем академической прокрастинации (r = .237, p = .029), а также между ИИ-зависимостью и псевдопродуктивностью (r = .318, p = .003). Психологическими механизмами выявленных связей определены когнитивный офлоадинг, снижение академической самоэффективности, нарушения саморегуляции учебной деятельности и страх негативной оценки. Показано, что хроническая ИИ-опосредованная прокрастинация формирует накапливающуюся психологическую нагрузку, связанную с ухудшением показателей психологического здоровья обучающихся. Практическая значимость состоит в возможности использования результатов при разработке программ психолого-педагогической профилактики, направленных на укрепление академической самоэффективности и поддержание психологического здоровья студентов в условиях цифровой образовательной среды. the relevance of the study is determined by the rapid integration of generative artificial intelligence systems into the educational environment, which gives rise to new forms of dysfunctional academic behaviour and creates risks to students' psychological health. The aim of the study is to examine the nature of the relationship between AI dependence, academic procrastination and pseudoproductivity in students, as well as to identify the psychological mechanisms underlying this relationship and its consequences for psychological health. An empirical study was conducted on a sample of students enrolled in the 37.03.01 Psychology programme at Siberian Federal University (n = 85; age 18–25, M = 20.4; SD = 1.7; 61% female, 39% male). The Dependence on Artificial Intelligence Scale (DAI; Morales-García et al., 2024; author's translation), the Tuckman Procrastination Scale (TPS), and an author-designed questionnaire for operationalising pseudoproductivity were used as diagnostic tools. Correlation analysis revealed a positive statistically significant association between AI dependence and academic procrastination (r = .237, p = .029), as well as between AI dependence and pseudoproductivity (r = .318, p = .003). The identified psychological mechanisms include cognitive offloading, reduced academic self-efficacy, self-regulation deficits in academic activity, and fear of negative evaluation. Chronic AI-mediated procrastination was found to generate accumulating psychological strain associated with deterioration of students' psychological health indicators. The practical significance lies in the applicability of the findings to the development of psycho-pedagogical prevention programmes aimed at strengthening academic self-efficacy and maintaining students' psychological health in digital educational environments.

**ИИ:** + · обе модели · назван коррелят · Used the DAI scale with 85 students and reported a correlation between AI dependence and academic procrastination (Tuckman Procrastination Scale), r = .237.

**Решение:** =

---

### 543 · R2975

**Integrating ChatGPT into Student Research Practices**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-31853-4_16

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. The title is about students using ChatGPT and doesn't mention dependence, but a survey of over-reliance can't be ruled out.); Sonnet -3 (нет меры зависимости от ИИ: только частота использования, принятие, доверие, грамотность, технострес, страх ИИ — или over-reliance только как поведение в эксперименте: No abstract; title concerns integrating ChatGPT into student research practice (tool use), with no sign of a dependence or addiction measure.)

**Решение:** -

---

### 544 · R2984

**DEVELOPMENT AND PSYCHOMETRIC VALIDATION OF THE SCREENING SCALE FOR ARTIFICIAL INTELLIGENCE ADDICTION DIAGNOSIS (AIAS-10+1 V4.0)**

2026 · PSYCHOLOGICAL JOURNAL · article, journalarticle, journal-article · und · https://doi.org/10.31108/1.2026.12.3.1

The rapid integration of generative artificial intelligence (AI) into educational and everyday environments has intensified concerns regarding the emergence of new forms of behavioral addiction associated with excessive and maladaptive human–AI interaction. Despite the growing body of research in the field of human–AI interaction, contemporary psychometrics still lacks brief and validated instruments for screening the risk of generative AI addiction. The purpose of the present study was to develop and conduct a comprehensive psychometric validation of the AIAS-10+1 v4.0 (AI Addiction Scale), designed to assess socio-emotional and behavioral-cognitive manifestations of AI addiction. The study involved 242 university students aged 18–30 years who were active users of generative AI technologies. Psychometric evaluation included assessment of internal consistency (Cronbach’s alpha), item-total correlations, exploratory factor analysis (EFA), correlation, regression and mediation analyses, ROC-analysis, Gaussian Mixture Modeling, K-Means cluster analysis, and threshold validation procedures. The initial 11-item version of the scale was revised according to the results of EFA and item analysis, resulting in the final AIAS-10+1 v4.0 model. The final version of the instrument consists of 10 core items forming two factors: “Socio-Emotional Dependence” (α = 0.866) and “Behavioral-Cognitive Dependence” (α = 0.696), as well as a separate Critical Thinking Indicator (+1), evaluated independently from the general addiction index. The overall internal consistency of the scale was α = 0.795. The findings demonstrated that 20.2% of respondents belonged to the risk group for problematic AI use. Loneliness and stress were identified as significant psychological predictors of AI addiction, while mediation analysis confirmed that their influence is mediated through socio-emotional and cognitive-behavioral mechanisms of interaction with AI systems. ROC-analysis and Gaussian Mixture Modeling supported the validity of the proposed cutoff scores. The obtained results indicate that AIAS-10+1 v4.0 is a reliable and psychometrically sound screening instrument for identifying the risk of addiction to generative artificial intelligence. The scale may be applied in psychological, educational, and interdisciplinary research, as well as in practical settings for early detection of maladaptive forms of AI-related behavior. Keywords: generative artificial intelligence; AI addiction; behavioral addiction; psychometric validation; cognitive offloading; human–AI interaction; screening scale; students; psychological dependence; digital behavior.

**ИИ:** + · обе модели · валидация шкалы · Validation of a generative AI addiction scale in 242 students; it names loneliness and stress as predictors.

**Решение:** =

---

### 545 · R2985

**Problematic use of generative artificial intelligence among medical students: analysis of behavioral patterns and the phenomenon of cognitive atrophy**

2026 · Psychosomatic Medicine and General Practice · article, journalarticle, journal article · und · https://doi.org/10.26766/pmgp.v11i2.716

The rapid integration of generative artificial intelligence (AI) into the educational process actualizes the problem of emerging new behavioral dependencies. Aim. Determine the prevalence and specifics of problematic AI use among medical students based on the analysis of specific behavioral patterns. Materials and Methods. A cross-sectional study was conducted involving 81 medical university students. A questionnaire including a targeted block of statements regarding the nature of interaction with algorithms was utilized to assess daily practices and risks. Results. It was found that 63.0% of respondents demonstrate adaptive AI use, 37.0% are prone to problematic use (risk group), and no critical cases of complete AI addiction were recorded (0%). Patterns of cognitive atrophy absolutely dominate the response structure (specifically, 62% of students tend to uncritically accept AI answers as truth), while signs of emotional attachment are minimal. A clinically significant phenomenon of dissimulation (hiding AI use) and pronounced gender differences in the reflection of cognitive changes were revealed. A strong positive correlation was established between uncritical trust in AI and anxiety in its absence (ρ = .433, p = .0001). Conclusions. The architecture of problematic AI use in the academic environment is primarily cognitive rather than emotional in nature. The leading risk vector is the pragmatic phenomenon of cognitive offloading, which leads to uncritical outsourcing of thinking ("cognitive miser"). This poses a threat to the development of autonomous clinical judgment in future physicians and requires the development of targeted preventive and educational programs. Keywords: artificial intelligence, generative models, problematic use, cognitive offloading, dissimulation, medical students. УДК: 616.89-008.44:004.8</jats:p

**ИИ:** ? · обе модели · корреляты не названы · Ad hoc problematic AI use questionnaire; the only 'anxiety' reported is an item inside the scale (withdrawal), and no other correlates are listed.

**Решение:** =

---

### 546 · R2989

**دور الرفاه الأسري كعامل معدل للعلاقة بين الاعتماد على الذكاء الاصطناعي والاستغراق الرقمي العاطفي لدى عينة من الأزواج دراسة مختلطة Family Well-Being as a Protective Moderator in the Association Between Artificial Intelligence Dependency and Emotional Digital Immersion Among Married Couples: A Mixed-Methods Explanatory Study**

2026 · مجلة الإرشاد النفسی · article · ar · https://doi.org/10.21608/cpc.2026.524264

مستخلص: يُعدّ الاعتماد على تطبيقات الذكاء الاصطناعي من الظواهر الرقمية المتصاعدة التي باتت تُلقي بظلالها على جودة العلاقة الزوجية والتواصل الأسري؛ مما يستدعي البحث عن المتغيرات التي تُسهم في تفسير هذه الظاهرة والتخفيف من آثارها. هدفت الدراسة الحالية إلى التعرف على العلاقة بين الاعتماد على الذكاء الاصطناعي والاستغراق الرقمي العاطفي لدى عينة من الأزواج السعوديين، والكشف عن العلاقة بين الرفاه الأسري والاستغراق الرقمي العاطفي، واختبار دور الرفاه الأسري بوصفه عاملًا معدِّلًا للعلاقة بين الاعتماد على الذكاء الاصطناعي والاستغراق الرقمي العاطفي، فضلًا عن استكشاف تجارب الأزواج في استخدام هذه التطبيقات، وتحليل انعكاساتها على تواصلهم العاطفي الأسري في ضوء مستوى الرفاه الأسري. واعتمدت الدراسة المنهج المختلط الجامع بين الكمي والنوعي، وتكوّنت عينة الدراسة الكمية من (546) زوجًا وزوجة من المملكة العربية السعودية، فيما بلغت عينة الدراسة النوعية (240) مشاركًا. وطُبِّق عليهم مقياس الرفاه الأسري لـ(بخاري، 2021) وترجمة (بوثلجة وآخرون، 2022)، ومقياس الاعتماد على الذكاء الاصطناعي (AIAS-4) لـ(Grassini, 2023) وترجمة (المحمدي وآخرون، 2025)، ومقياس الاستغراق الرقمي العاطفي لـ(Roberts & David, 2016) وترجمة الفريق البحثي. وقد أظهرت النتائج الكمية وجود علاقة ارتباطية موجبة دالة إحصائيًا بين الاعتماد على الذكاء الاصطناعي والاستغراق الرقمي العاطفي، ووجود علاقة ارتباطية سالبة بين الرفاه الأسري والاستغراق الرقمي العاطفي، كما تبيّن أن الرفاه الأسري يؤدي دورًا تعديليًا دالًا في هذه العلاقة. وعلى الصعيد النوعي، كشفت استجابات المشاركين عن ثلاثة أنماط متدرّجة من الاعتماد العاطفي على الذكاء الاصطناعي تمثّلت في: اللجوء إليه كملجأ للتفريغ العاطفي في غياب الدعم الأسري، والتطبيع مع الاستخدام اليومي المكثف، والوعي بالاعتماد مع التردد في الاعتراف به. كما أكدت النتائج النوعية أن ضعف الحوار الأسري يُمثّل دافعًا مباشرًا نحو الاستغراق الرقمي العاطفي، في حين يعمل الرفاه الأسري المرتفع على تقليص هذا الاعتماد من خلال إشباع الاحتياجات الوجدانية داخل العلاقة الزوجية ذاتها. وبناءً على هذه النتائج، توصي الدراسة بإعداد برامج تدريبية وتوعوية موجهة للأزواج لتعزيز وعيهم بمخاطر الاعتماد المفرط على تطبيقات الذكاء الاصطناعي وانعكاساته على الاستغراق الرقمي العاطفي وجودة العلاقة الزوجية، مع تضمين محور الرفاه الأسري ضمن البرامج الإرشادية والعلاجية المقدمة للأزواج، لما له من دور وقائي وتعديلي في هذه العلاقة. كلمات مفتاحية: الاعتماد على الذكاء الاصطناعي، الاستغراق الرقمي العاطفي، الرفاه الأسري، الأزواج السعوديون، التواصل الزوجي، المنهج المختلط. Abstract: The growing reliance on artificial intelligence applications has emerged as a significant digital phenomenon with far-reaching implications for marital quality and family emotional communication, underscoring the need to identify variables that explain and potentially mitigate its effects. This study aimed to examine the relationship between AI dependency and emotional digital immersion among a sample of Saudi married couples, investigate the association between family well-being and emotional digital immersion, and test the moderating role of family well-being in the relationship between AI dependency and emotional digital immersion. Additionally, the study sought to explore couples' lived experiences with AI applications and analyze how such experiences shape their emotional family communication in light of family well-being levels. A mixed-methods design was employed, with a quantitative sample of 546 married couples and a qualitative sample of 240 participants recruited from across Saudi Arabia. Instruments included the Family Well-Being Scale (Bukhari, 2021; translated by Bouthaljah et al., 2022), the AI Attitude Scale (AIAS-4; Grassini, 2023; translated by Al-Muhammadi et al., 2025), and the Emotional Digital Immersion Scale (Roberts & David, 2016; translated by the research team). Quantitative findings revealed a statistically significant positive association between AI dependency and emotional digital immersion, a significant negative association between family well-being and emotional digital immersion, and a significant moderating effect of family well-being on the AI dependency–emotional digital immersion relationship. Qualitative findings identified three progressive patterns of emotional AI dependency: seeking AI as an emotional outlet in the absence of family support, normalizing intensive daily AI use, and demonstrating awareness of dependency coupled with reluctance to acknowledge it. Furthermore, qualitative data revealed that deficient marital dialogue functions as a direct precursor to emotional digital immersion, whereas elevated family well-being buffers against such immersion by fulfilling emotional needs within the marital relationship itself. These findings collectively suggest that strengthening family well-being and revitalizing spousal communication channels represent essential intervention pathways for mitigating emotional digital immersion among married couples. The study recommends the development of family counseling programs designed to translate couples' implicit awareness of digital dependency into structured, balanced communicative practices Keywords: AI dependency, emotional digital immersion, family well-being, Saudi married couples, marital communication, mixed-methods research.

**ИИ:** ? · обе модели · мера зависимости неясна · Labelled AI dependency, but measured with AIAS-4, an attitude scale; correlates are family well-being and emotional digital immersion (possibly phubbing).

**Решение:** =

---

### 547 · R2991

**Excessive Dependence on Generative AI and Its Effect on University Students’ Academic Achievement: A Field Study at Aljufra University**

2026 · مجلة جامعة بني وليد للعلوم الإنسانية والتطبيقية · article · en · https://doi.org/10.58916/jhas.v11i1.1050

شهدت السنوات الأخيرة انتشارًا واسعًا لاستخدام أدوات الذكاء الاصطناعي التوليدي بين طلبة الجامعات، مما خلق تحولًا ملحوظًا في أنماط التعلم وإعداد الواجبات الأكاديمية وتهدف هذه الدراسة إلى تحليل أثر الاعتماد المفرط على هذه الأدوات في التحصيل الأكاديمي لدى طلبة البكالوريوس في جامعة الجفرة، واستكشاف العوامل التي تدفع الطلبة إلى استخدامها، إضافة إلى رصد الانعكاسات الأكاديمية والسلوكية الناتجة عنها. واعتمدت الدراسة المنهج الكمي من خلال استبيان ميداني شمل 200 عينة من الطلبة، واستندت إلى نظرية العبء المعرفي ونموذج قبول التكنولوجيا لتفسير سلوك الاستخدام وتأثيره على التعلم. أظهرت النتائج أن الاعتماد الكلي على أدوات الذكاء الاصطناعي يؤدي إلى انخفاض القدرة على التفكير والتحليل، وضعف الدافعية الذاتية للتعلم، وتراجع الأداء في الامتحانات الفعلية. وكشفت الدراسة كذلك أن مخرجات الذكاء الاصطناعي قد تعطي عضو هيئة التدريس انطباعًا خاطئًا بارتفاع مستوى الطلبة، مما ينعكس سلبًا على عملية التقييم ويدفع نحو رفع مستوى المنهج دون مراعاة قدراتهم الحقيقية، وكما بينت النتائج أن سهولة الاستخدام والمنفعة المتصوّرة وضغط الوقت وضعف الثقة الأكاديمية تُعد من أبرز العوامل المؤثرة في اعتماد الطلبة على هذه الأدوات، وفي الختام، تقدم الدراسة مجموعة من المقترحات للحد من الاستخدام غير السليم للذكاء الاصطناعي من خلال تعزيز الثقافة الرقمية، ورفع الوعي الأخلاقي، وإعادة تصميم الأنشطة التعليمية بما يدعم التعلم الحقيقي ويعزز مهارات التفكير لدى الطلبة.

**ИИ:** ? · обе модели · корреляты не названы · Survey measures excessive GenAI dependence; factors include time pressure and weak academic confidence, possibly proxies for academic stress or self-efficacy.

**Решение:** =

---

### 548 · R2992

**نمذجة العلاقات السببية بين الاستخدام المفرط لتطبيقات الذكاء الاصطناعي ومشاعر العزلة الاجتماعية والاغتراب النفسي لدى طلاب الجامعة**

2026 · مجلة کلیة الآداب جامعة بورسعید · article · ar · https://doi.org/10.21608/jfpsu.2026.479273.1541

هدف البحث الحالي إلى الكشف عن طبيعة العلاقات السببية بين الاستخدام المفرط لتطبيقات الذكاء الاصطناعي (TikTok – Instagram – Snapchat – ChatGPT – Google Gemini) وغيرها من التطبيقات، ومشاعر العزلة الاجتماعية والاغتراب النفسي لدى طلاب الجامعة. استخدم البحث المنهج الوصفي الارتباطي، كما استخدم أسلوب النمذجة السببية (Structural Equation Modeling – SEM) لتحليل العلاقات بين المتغيرات، وتكونت عينة الدراسة من (760) طالب وطالبة من طلاب الجامعة تراوحت أعمارهم بين (17–25 عامًا)، بمتوسط (20.41) وانحراف معيارى (±1.44) سنة. واستخدمت الباحثتان الأدوات التالية: مقياس الاستخدام المفرط لتطبيقات الذكاء الاصطناعي (إعداد: الباحثتين)، ومقياس العزلة الاجتماعية (إعداد: عادل عبدالله محمد، 2003)، ومقياس الاغتراب النفسي (إعداد: زينب شقير، 2017). وأظهرت النتائج وجود علاقة ارتباطية موجبة دالة إحصائيًا بين الاستخدام المفرط لتطبيقات الذكاء الاصطناعي وكل من العزلة الاجتماعية والاغتراب النفسي، مما يشير إلى أن الإفراط في التعامل مع هذه التطبيقات قد يسهم في تراجع التفاعل الاجتماعي المباشر وزيادة مشاعر الانفصال النفسي عن الواقع، كما أوضحت أن الاستخدام المفرط لتطبيقات الذكاء الاصطناعي مرتبط ارتباطًا موجبًا بالاغتراب النفسي لدى الشباب، فكلما زاد الاستخدام المفرط زادت درجة الاغتراب النفسي والشعور بفقدان المعنى والانفصال. كما أن الاستخدام المفرط لتطبيقات الذكاء الاصطناعي يرتبط ارتباطًا موجبًا بمستوى العزلة الاجتماعية لدى الشباب فكلما زاد الاستخدام المفرط زادت مشاعر العزلة الاجتماعية. كما توجد علاقة ارتباطية بين العزلة الاجتماعية والاغتراب؛ حيث تؤثر العزلة الاجتماعية كوسيط جزئي في العلاقة بين الاستخدام المفرط لتطبيقات الذكاء الاصطناعي والاغتراب النفسي (بمعنى ان الاستخدام المفرط يزيد العزلة الاجتماعية مما يؤدي بدوره إلى زيادة الاغتراب النفسي). Abstract The present study aims to examine the nature of the causal relationships between excessive use of artificial intelligence applications (TikTok, Instagram, Snapchat, ChatGPT, Google Gemini, and other applications) and feelings of social isolation and psychological alienation among university students. The study employed descriptive correlational design and utilized Structural Equation Modeling (SEM) to analyze the relationships among the variables. The study sample consisted of (760) male and female university students, aged between 17 and 25 years, with a mean age of (20.41) and a standard deviation of (±1.44). The researchers used the following instruments: the Excessive Use of Artificial Intelligence Applications Scale (developed by the researchers), the Social Isolation Scale (developed by Adel Abdullah Mohamed, 2003), and the Psychological Alienation Scale (developed by Zeinab Shaqir, 2017). The results revealed a statistically significant positive correlation between excessive use of artificial intelligence applications and both social isolation and psychological alienation. This indicates that excessive engagement with these applications may contribute to reduced direct social interaction and increased feelings of psychological detachment from reality. The findings also showed that excessive use of artificial intelligence applications is positively associated with psychological alienation among youth; as excessive use increases, levels of psychological alienation and feelings of meaninglessness and detachment also increase. Moreover, excessive use of artificial intelligence applications was found to be positively associated with levels of social isolation among youth; higher levels of excessive use were linked to greater feelings of social isolation. In addition, a significant relationship was found between social isolation and psychological alienation, where social isolation acts as a partial mediator in the relationship between excessive use of artificial intelligence applications and psychological alienation. In other words, excessive use increases social isolation, which in turn leads to higher levels of psychological alienation.

**ИИ:** разошлись — Opus ? (мера зависимости неясна: Excessive-use scale mixes social media (TikTok, Instagram, Snapchat) with ChatGPT and Gemini; it correlates with social isolation (loneliness-like) and alienation.); Sonnet + (назван коррелят: SEM survey of 760 students using an excessive AI-app use scale (incl. ChatGPT, Gemini) with social isolation and alienation; app list also includes social media.)

**Решение:** ?

---

### 549 · R2993

**कतरम बदध उपकरण पर वदयरथय क नरभरत**

2026 · Ved International Journal of Arts Commerce and Technology (VIJACT) · article, journalarticle, journal article · und · https://doi.org/10.65785/vijact.v2i5.47

वर्तमान समय में AI Tools का उपयोग विद्यार्थियों के बीच तेजी से बढ़ रहा है । प्रस्तुत अध्ययन का उद्देश्य विद्यार्थियों में AI Tools की उपयोग एवं उन पर निर्भरता का अध्ययन करना था इस अध्ययन में 18-25 वर्ष आयु के 300 विद्यार्थियों को शामिल किया गया, जिसमें छात्र तथा छात्राएं दोनों सम्मिलित है । डेटा संग्रह के लिए शोधकर्ता द्वारा स्वनिर्मित मापनी का निर्माण किया गया एवं उसकी मनोमितीय मूल्यांकन के पश्चात मापनी को प्रशासित किया गया, जिसमें तीन आयामों पर आधारित कुल 15 प्रश्न सम्मिलित है । अन्वेषणात्मक कारक विश्लेषण (EFA) द्वारा 3 प्रमुख घटक प्राप्त हुए , साथ ही मापनी ने अच्छी विश्वसनीयता (क्रोनबैक अल्फा 0.810) प्रदर्शित की, विश्लेषण से औसत (51.47), मानक विचलन (8.84) प्राप्त हुआ, जो विद्यार्थियों में AI Tools के प्रति मध्यम स्तर से उच्च स्तर की निर्भरता को दर्शाता है । Keywords: AI Tools, Students, AI Dependency, Cognitive effects</jats:p

**ИИ:** ? · обе модели · корреляты не названы · Hindi survey of 300 students using a self-made 15-item AI-dependence scale; only EFA/reliability/descriptives reported, correlates not named.

**Решение:** =

---

### 550 · R3002

**AI Dependence and Creativity: The Mediating Role of Creative Self-Efficacy and the Moderating Role of Perceived AI Creativity**

2026 · Advances in Psychology · article, journalarticle, journal-article · und · https://doi.org/10.12677/ap.2026.164199

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title points to an AI dependence measure with creative self-efficacy as a mediator, which may count as a self-efficacy correlate.

**Решение:** =

---

### 551 · R3007

**From Technological Dependence to Cognitive Empowerment: An Empirical Investigation of Generative AI Usage Behaviors and Intervention Paths in College Students’ English Writing**

2026 · Advances in Education · journal-article · https://doi.org/10.12677/ae.2026.1691943

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; empirical study of generative-AI dependence in student writing, so correlates of interest may have been measured.

**Решение:** =

---

### 552 · R3009

**高等学校におけるインターネット依存・ゲーム障害・ 生成AI依存の予防教育の授業実践**

2026 · Institutional Repositories DataBase (IRDB) · article · ja · https://doi.org/10.34360/0002002089

The author constructed a learning unit for preventing internet addiction, Gaming Disorder and generative AI addiction. The teaching practice was implemented for 1st grade students at a high school in the class of Information class from April to July in 2025. After the class, the author examined achievements and problems of this teaching practice by analyzing students’ annual changes about internet addiction tendency, time spent on games and generative AI addiction tendency. As a result of the questionnaire for the students, there were improved as a whole after the class.

**ИИ:** ? · обе модели · корреляты не названы · Teaching intervention measured generative AI addiction tendency and internet addiction tendency; unclear whether their correlation is reported.

**Решение:** =

---

### 553 · R3013

**Development and Validation of the Multidimensional Generative AI Dependence Scale (M-GAIDS)**

2026 · Journal of the Korean Association of Information Education · article, journalarticle, journal-article · und · https://doi.org/10.14352/jkaie.2026.30.1.111

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · валидация шкалы · No abstract, but the title shows it develops and validates a generative AI dependence scale, which likely reports convergent validity correlates.

**Решение:** =

---

### 554 · R3025

**Meeting Abstracts: International Conference on Psychiatry and Neurorestoratology (ICPN) 2024**

2025 · Current Opinion in Psychiatry · article · en · https://doi.org/10.1097/01.yco.0001123740.02763.32

1 Alienation of the role of AI counselling robots in the emotional accompaniment of left-behind adolescents Shuai Liu*. Sichuan Vocational and Technical College, Suining 629000, China INTRODUCTION: With the rapid advancement of AI technology, AI counselling robots are increasingly used in mental health interventions for left-behind youth. Due to a long-term lack of parental emotional support, these adolescents often struggle with emotional expression, mental health, and social skills. AI counselling robots, as an intelligent intervention, offer emotional support. However, their expanding use has led to role alienation, seen in increased dependence, dehumanised emotional interactions, and potential harm to real-life social skills. Thus, exploring the role alienation of AI counselling robots in emotional support and its impact on psychological development is highly significant. METHODS: The study used a combination of questionnaires and in-depth interviews with 300 left-behind youths who had used the AI psychological counselling robot, covering different regions and age groups. The research tools include ‘AI Dependency Scale’, ‘Social Skills Scale’ and ‘Mental Health Scale’. After data collection, Pearson's correlation analysis and regression analysis were performed using SPSS software. Additionally, 10 adolescents were interviewed to explore their subjective experiences and potential negative impacts of AI counselling robots. RESULTS: With the increase in the frequency of use of the AI counselling robot, the dependence of the left-behind adolescents significantly increased (r=0.71, P<0.01), while the social competence score significantly decreased (r=-0.52, P<0.05). In addition, adolescents with higher levels of dependence had significantly higher levels of anxiety (r=0.66, P<0.01) and depression (r=0.72, P<0.01) than those with lower levels of dependence, suggesting that the AI Counselling Robot may exacerbate some adolescents’ mental health problems. The interview results further confirmed that some adolescents used the AI robot as their main emotional support and reduced their communication with peers or family members. CONCLUSION: The study reveals the role alienation of AI counselling robots in emotional support for left-behind adolescents. High-frequency users saw an 18% rise in anxiety, a 21% increase in depression, and a 15% drop in social competence scores. While AI robots temporarily eased emotional loneliness, long-term use may lead to social avoidance, harming mental health. Thus, promoting AI robots should focus on balanced use to prevent over-reliance, alongside offline support systems like family and professional counselling, for a healthier support model. Future improvements should enhance the robots’ interaction design to be more humane, reducing role alienation's negative effects. 2 Interaction mechanisms between online bereavement culture modal transmission and existential anxiety in an urban youth population Ya Gao*. Shandong Polytechnic College, Jining 272067, China INTRODUCTION: In the era of widespread digital media, online mourning culture, as a unique social phenomenon, has gained popularity among urban youth. This culture spreads rapidly through social media, reflecting the psychological state of young people through humor, self-deprecation, and nihilism. Research indicates that urban youth face challenges like employment pressure, social competition, and identity issues. The rise of mourning culture may serve as an emotional outlet or worsen anxiety. However, the interaction between the spread of mourning culture and youth anxiety remains understudied. This research aims to analyze the transmission patterns of mourning culture, youth acceptance, and their impact on anxiety levels, providing insights for mental health interventions and digital culture management. METHODS: The study adopted a mixed research approach, including questionnaires, in-depth interviews and online text analysis. Firstly, 600 young people aged 18-35 from first-tier and second-tier cities were randomly selected, and their anxiety levels were measured using the Existential Anxiety Scale (EAS), and combined with their social media habits, the questionnaire assessed the frequency of exposure and attitudes of urban youths towards the modes of mourning culture. Secondly, Natural Language Processing (NLP) technology was used to analyse the text of popular funeral culture content on Weibo, Zhihu, and B-station to identify the main modes of communication and emotional orientations. RESULTS: Youth attitudes toward mourning culture were classified into emotional identification, negative reinforcement, and recreation types. Emotionally identified individuals had significantly higher EAS scores (59.3±7.1) compared to others (P<0.01). Those with high-frequency exposure to mourning culture also had higher EAS scores (58.6±6.4) than those with low-frequency exposure (43.2±8.5), indicating that while short-term emotional relief may occur, long-term reliance could worsen anxiety. This is reflected in avoiding real issues, social withdrawal, and accumulating negative emotions (P<0.01). CONCLUSION: The study highlights a complex link between the spread of online mourning culture and urban youth's existential anxiety. While such culture may offer some psychological comfort, prolonged exposure can worsen anxiety and hinder social adaptability. Thus, fostering a positive online cultural environment, alongside psychological interventions, is crucial to help youth manage anxiety healthily. Future research could use brain imaging to explore how mourning culture affects emotional regulation and delve deeper into digital media's impact on youth mental health. 3 Impact of combined with on psychological of with social anxiety China INTRODUCTION: anxiety is more in the affects an social also the psychological affects and In and to positive on social anxiety However, on an that the in psychological on the study the combined of combined with on the psychological of with social anxiety aims to and for mental health and in and METHODS: design was used in the with social anxiety were randomly into and a combined with with a for 2 and a for 1 mental health the of the the Scale the Anxiety Scale and the Health of were assessed and RESULTS: After the intervention, the score of was was more than that of the between the was significantly lower than on the social anxiety and the reduced the of social anxiety. In addition, significantly higher than on the of CONCLUSION: combined with has a on the psychological of with social anxiety can the of social anxiety and the of This can a and for mental health In the the study further explore the and long-term of in different as as to further the effects. of on depression in adolescents on China of China INTRODUCTION: depression has a health and its is on the rise adolescents’ mental health and and In as a intervention, has more and more to its unique can and also with to adolescents’ and the study to the of on depression on and to a and for interventions for METHODS: design was adolescents from to depression were and randomly into an and a with in The a intervention, such as and The mental health After the intervention, the study assessed the depression emotional state and of the adolescents in the through questionnaires, psychological and RESULTS: The results that adolescents in the had significantly reduced significantly emotional state and more positive the with the the score on the decreased and the positive of significantly In of emotional the positive emotional scores of adolescents in the were significantly higher than those of the and the results a between the In addition, the scores of the adolescents in the were significantly higher than those of the and were CONCLUSION: has on depression and can mechanisms and This study and for interventions for depression, and is that further explore the combination of and to effects. of the of with of and China INTRODUCTION: with may be and and their of is significantly higher than that of the However, are on the and interaction of and is a lack of analysis on METHODS: design was used to 300 individuals with and in who were to a in a between and as the and 300 a of mental were randomly as the were through and The assessed and Scale Scale the on the and regression was used for data analysis to identify and was used to the between groups. were performed using SPSS and the was RESULTS: were in between the and the The score of positive in with for was significantly higher than that of The of was compared with in the for of and of In addition, the of in the with social support was significantly higher than that in the with social support. CONCLUSION: This study has confirmed that in with is to positive and social support. positive such as increase the of while and social digital media technology to analyze the emotional and of with anxiety China INTRODUCTION: a mental anxiety is and and the of of The research is to use digital media technology to analyze the and of anxiety explore the correlation between and and for and METHODS: The study with anxiety and for and digital media was used in the the and the of the were an Secondly, a was used to analyze the of of emotional and such as the of rise and the frequency of were was assessed through RESULTS: with anxiety in and In the the of was and the of was decreased In the of the decreased to and the increased to of were significantly higher than the analysis that the score of anxiety was with the to CONCLUSION: The results that to negative emotions and may exacerbate their and digital media technology can these to for the of The results of study support for and for anxiety and further the and explore the of long-term data in the of on regulation of with INTRODUCTION: in are as to negative emotions and of positive However, of the focus on the short-term relief of and lack the long-term of the of regulation and the of the and psychological METHODS: The study who were randomly into and groups. The for a for including and The is to the from to The and health a were assessed with the and the and of and and data were RESULTS: After intervention, the emotional regulation of the was significantly than that of the The that the score of the increased from to and the score decreased from to with was in the The score decreased in the and in the CONCLUSION: The results that significantly the use of and reduced the of emotional results support the of on suggesting that can be used as a to the of of on and social of China INTRODUCTION: is a mental with and social as the This study to explore the of on with and for for METHODS: design was used to with in the of a and were randomly into the and the the of the for 3 a with of The the and The state was used to the score and of was the Scale were using the and Scale RESULTS: After intervention, the was significantly than the in of and social adaptability. The score increased from to in the and from to in the with the in the The social that the score of the increased was significantly higher than that of the The score in the decreased was lower than that in the The that the had a CONCLUSION: The study confirmed that of can significantly the and social of and has a long-term In the is to further explore the between different and and analyze the of through brain imaging of the of combined with on anxiety of China INTRODUCTION: In the environment, are with and social pressure, and the of anxiety is on the affects and mental health and a of intervention, can emotions to a as a used has used in The of study is to explore the of combined with on anxiety of and to and for mental health. METHODS: of with anxiety in a were as the research were randomly into and in The for the of the the of in a a a of and to in the and anxiety. and the Anxiety Scale was used to score the of to the of anxiety RESULTS: The of the was was significantly lower than that of the and the was the the score of the was significantly lower than that of the The of the was higher than that of the and the was CONCLUSION: The combination of and is more in anxiety in than The of and can more anxiety and enhance their mental health This a more and for the of anxiety in and is to its in mental health and 10 The of digital on psychological anxiety of Language INTRODUCTION: the of employment and social the psychological anxiety of has increasingly is to to a of cultural digital digital technology and cultural and a for exploring psychological anxiety relief study explore the of digital on psychological anxiety of to help the of digital technology in the of mental health. METHODS: of with different of psychological anxiety were as the research were randomly into and people in The and the state of and The in an digital a for for digital covering and and use and to an and the Anxiety was used to the of to their of psychological anxiety. the the of the on the digital was through a questionnaire RESULTS: The scores of state anxiety and anxiety in the were and were significantly lower than those in the and the of anxiety relief was higher than that in the CONCLUSION: The digital has a on the psychological anxiety of and can the of state anxiety and anxiety of providing cultural to and their in the cultural psychological anxiety. This an and for mental health in and and is to further its and with mental health to the mental health of of robot on of China INTRODUCTION: is a widespread that affects and The has some the robot for the of a combination of and the research aims to a more and for with to the development of their emotional and social skills. METHODS: The study between the of and who had with were randomly into an and a with in The of robot a for the robot can to in a and and The the and the intervention, The and the Scale were and the were assessed for of RESULTS: The data that the scores of in the were and on the and the robot with the the more in reduced and social communication skills. CONCLUSION: The robot has in the of can the of that their and are the significantly the of and into their In can significantly the social communication of with that more communication and interaction with the This and has a for the of and is to be more and in the and The of on mental health of with and anxiety China INTRODUCTION: With the development of the of with and anxiety is and their mental health The of on mental health has a research This study aims to explore can the mental health of with and anxiety and for the and of such METHODS: The study people with and people with anxiety The with were randomly into and people in with anxiety were also into and with people in The of in the was for environment, such as the of to and The was in a the study the mental health of was assessed a and the subjective of were through psychological RESULTS: The data that the the score of in the and the anxiety decreased and was than that in the interview results also that in the and CONCLUSION: The of can significantly the mental health of with and anxiety such as and can psychological scores and subjective This that in the and of with and anxiety should be to the and of to with a more for mental health of on in the of culture Shandong Polytechnic College, Jining 272067, China INTRODUCTION: With the rapid development of are challenges such as pressure, and led to increasingly mental such as anxiety and the culture, as an of culture, psychological and has potential positive on the mental health of as an psychological intervention, has to in However, is research exploring the of culture with on among In to the of and their levels of depression and anxiety, a for on culture is METHODS: The study with and randomly into an a and a with in The on the of and while the on the of and The and for 2 and the the Scale and Anxiety Scale were used to the RESULTS: was in and scores among the of indicating between the groups. After the scores of of significantly After of the scores of the and were and with between the groups. The scores of of also significantly After of the scores of the and were and with between the groups. CONCLUSION: and combined with can the of and their levels of depression and anxiety. with China INTRODUCTION: is a mental and emotional can some its in is In psychological as an has gained to its potential in and promoting social However, the of psychological on in with is and further research and are METHODS: with were for the study and randomly into an and a with in The while the psychological in to for a of 3 and the the and the Scale were used to the and mental RESULTS: was in and scores among the of indicating between the groups. The in scores between the and the was of After 2 of the in scores between the and the significantly with of and and the was significant. 2 of the scores of the were and After 3 of the scores of the were and and the was significant. CONCLUSION: The combination of and psychological can the mental state of with also their and enhance their social In to explore the impact of on in with research delve into the mechanisms of such as in brain and The of emotional regulation on anxiety in of China INTRODUCTION: In the of the in the is and often face the of anxiety to and regulation is an and their to an role in with and anxiety. This study aims to explore the of emotional regulation on anxiety in METHODS: This study used a questionnaire with of a in a as the research and through of questionnaires were and questionnaires were with an of The questionnaire the Scale and the Anxiety The Scale is used to in their to while the Anxiety Scale is used to the of anxiety The data analysis was using SPSS and analysis was used to the of the and the of correlation analysis to the between regulation and anxiety and use regression analysis to the of regulation between and anxiety RESULTS: is a highly positive correlation between and anxiety and a highly negative correlation between emotional regulation and anxiety indicating that emotional regulation can anxiety CONCLUSION: The results that emotional regulation has a on anxiety among levels of emotional regulation can help with reducing the of anxiety can enhance in emotional regulation providing emotional and psychological support, with pressure, their mental health, and Future research can further explore the interaction between and emotional regulation to its in different cultural The of and cultural on of the role of psychological China INTRODUCTION: With the development of the the of among is increasingly affects their and mental health and The and cultural as an may a impact on the psychological of The research aims to explore the impact of and cultural on as as the role of psychological in to for and in METHODS: This study used a questionnaire and from a as the research The questionnaire the and cultural psychological and The and culture the and of in and cultural The psychological and The is used to use and The data was using SPSS and and the of psychological was using RESULTS: The of psychological are significantly with with of and The results that the and cultural can the of among their psychological CONCLUSION: The results that the and cultural has a on and psychological an role in and cultural can the psychological of reducing their of should to an and cultural and the psychological of and cultural reducing their Future research can further explore the of different of and cultural on psychological and on the of digital on the of of China INTRODUCTION: With the of digital technology and cultural digital cultural as a of has a impact on the and mental health and social of on and psychological intervention, the is and to In the of has a research This study aims to explore the of digital on the of and and for METHODS: The study were with in a between the of and and and were in the Scale and Health Scale were used to the of and mental health of The a cultural and an online cultural and the were for and mental health a of RESULTS: In the the cultural and the online cultural in the of and mental health scores indicating that the has a on the of the the of cultural was more than that of online cultural CONCLUSION: that digital as a intervention, can the of of with their mental health and enhance the of Future may further explore the and of digital in different and is that digital cultural into to with more and support. design research on young people College, China China INTRODUCTION: In young people are with the of and The of depression is affects their mental health and of as an that can mental state through and has more and more in the of psychological in The of study is to explore the of design on depression in young and to and for mental health METHODS: The study from a in Sichuan aged to and of some of were randomly into a design a psychological and a The design of design including and The psychological The for Scale was used and the study to levels of RESULTS: In the the depression score of the design was significantly lower the than the and the were and In addition, compared with the psychological and the the of was more and its score decreased The results that design can depression in young CONCLUSION: that design can significantly the depression of young and its is than psychological and such as and design can the and emotional of young as to Future can further explore the of design in different cultural and and more design is to design in mental health to more and mental health support for young Impact of and experiences on with College, College, China China INTRODUCTION: In in the of mental health a through interaction on the population or emotional and is a in for complex groups. The research aims to explore the emotional regulation of on with the of experiences on emotional the research in METHODS: The study a mixed research a a The Scale Anxiety Scale and and Scale were used to the emotional and the analysis was using SPSS for analysis of and analysis of with a of RESULTS: The results that the in intervention, with from to and score from to The score of the increased from to while the in CONCLUSION: The study the impact of on with through a mixed research The results that the and score of and can be seen that experiences can significantly depression and anxiety in with enhance positive and a role in This a for interventions for Future research can further the the research explore its mechanisms in and different and to more and to serve with The of in the of anxiety among in in China INTRODUCTION: in in are to anxiety to such as pressure, anxiety, and is a in the research on the of as a to anxiety among in Research the of and explore the and for the psychological health in METHODS: in with anxiety were for the study and randomly into an and a The combined with while the The and were using the Anxiety Scale and Scale the were and and were performed using SPSS The was to RESULTS: After intervention, the score of the decreased from to significantly than the to The score of in the from to The score that the relief of the was significantly higher than that of the In of the of in the was and were of CONCLUSION: The study is the to with and to the of anxiety in The results that had a with significantly anxiety and However, has such as and the of a Future research focus on exploring the in the of different with with the of further reducing and promoting mental health and professional and of for with of China INTRODUCTION: also as mental to a of with and or emotional as the main The main are or often and while may such as can help and of The of study is to explore the of on and social in with in to for METHODS: This study adopted a and who the in a in a aged between and The research were randomly into an and a The psychological The a on the of the 3 a for SPSS was used for and Anxiety and Scale and were used for RESULTS: After of intervention, the scores of the in the were and while the scores of the in the were and The between the was CONCLUSION: The results that the had a positive on the emotional state of the with could their depression and anxiety, and the their social to a that could to social of on China INTRODUCTION: is a mental with in young and is often emotional and the is to be a of brain with and may and the of the on social The of study is to explore the of on the social of with in to for the of with METHODS: was used to with who the The were randomly into and people in The was social for a for The on the of the Scale and Scale were and the and Scale were RESULTS: After the intervention, the score of the was the score was and the was score was significantly higher than that of while score and score were significantly lower than that of and the between the was CONCLUSION: The results that can significantly the social of with can the and of with a and environment, help the anxiety and of and the of social However, the study on the for and more research be combined in the to more the impact of on social of design on the psychological of with anxiety China INTRODUCTION: In the of anxiety is and the of and to explore the and of the environment, design is to be to the and the This study on the combined with its psychological and on with anxiety and the of different METHODS: In a a covering an of is and its include a a and a with anxiety were and randomly into groups. people in the were to in the such as and or a for people in the The study used the Anxiety Scale and the anxiety of the state of as The data intervention, 3 and were for and the was to 3 RESULTS: In the the of was higher in with than in with and the frequency of interaction was with anxiety After of intervention, the score decreased to and the score decreased to The that the of anxiety in the was significantly lower than that in the and the was of that of CONCLUSION: design can significantly anxiety and and has and of combined with digital media technology and design on anxiety and of China INTRODUCTION: The of digital media technology and design a for psychological intervention, can enhance the through This study a and and to explore its on the of anxiety and and analyze its METHODS: The used in the study is on with and and The were into anxiety and In the anxiety with anxiety were in the and in the aged and the of Anxiety were in the in the and in the aged and the score of social The a for In the the anxiety and the social RESULTS: After intervention, the score in the anxiety decreased from to After intervention, the score in the of decreased from to The of of the in real social indicating that the

**ИИ:** + · обе модели · назван коррелят · Abstract 1: AI Dependency Scale in 300 adolescents correlated with anxiety and depression; check whether counselling 'robot' is chatbot or embodied.

**Решение:** =

---

### 555 · R3037

**Artificial Intelligence Dependence and Well-Being Among College Students**

2025 · Advanced International Journal for Research · article, journalarticle, journal-article · und · https://doi.org/10.63363/aijfr.2025.v06i06.3580

The present study examined the relationship between AI dependence and digital well-being among college students using a cross-sectional design. A sample of 100 students aged 17–25 was selected through purposive sampling, focusing on active users of AI tools such as ChatGPT, Gemini, Perplexity, and Meta AI. Data were collected using two standardized instruments: the Digital Well-Being Scale (Gomes et al., 2023) and the Dependence on Artificial Intelligence Scale (Morales-García et al., 2024). Descriptive statistics revealed moderate levels of AI dependence and generally high levels of digital well-being among the participants. Results further showed that 58% of students had high AI dependence, while 65% reported high digital well-being. A strong and highly significant negative correlation (r = –0.72, p &lt; 0.01) was found between AI dependence and digital well-being, indicating that increased reliance on AI is associated with reduced digital wellness. Gender differences were also significant, with males reporting higher AI dependence and females showing better digital well-being. Overall, the study highlights the importance of mindful AI usage and the need for promoting healthy digital habits among students to maintain emotional balance and technological well-being.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey using the Dependence on AI Scale; reports r = -0.72 with digital well-being, a variant of the well-being correlate.

**Решение:** =

---

### 556 · R3044

**Avoid Excessive Usage: Examining the Motivations and Outcomes of Generative Artificial Intelligence Usage among Students**

2025 · Journal of Academic Ethics · review, article · en · https://doi.org/10.1007/s10805-025-09659-3

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title suggests a student survey of excessive GenAI use and its outcomes, which could include eligible correlates; the review tag is ambiguous.

**Решение:** =

---

### 557 · R3046

**Supplementary_materials_LLM_dependency_study**

2025 · OSF Preprints (OSF Preprints) · preprint

This project contains anonymised dummy data and example analysis code for a study on large language model (LLM) dependency, cognitive offloading, and academic self-efficacy among university students. The materials are illustrative only and do not include real participant data.

**ИИ:** + · обе модели · назван коррелят · Supplement to a student study of LLM dependency and academic self-efficacy; judge by the parent article, which should be retrieved.

**Решение:** =

---

### 558 · R3052

**Relationship between Cognitive Load and AI Dependence among University Teachers: Moderating role of Decision Making Styles**

2025 · Research Journal of Psychology · article, journalarticle, review · en · https://doi.org/10.59075/rjs.v3i3.166

As the highly robust environment of higher education keeps progressing, university instructors face increasing cognitive imposition due to their multi-role task nature and growing integration of technology in learning. This study investigates the relationship between cognitive load, decision making styles (rational, intuitive) and dependence on artificial intelligence (Al) among university teachers. Data were collected from 240 faculty members of both public and private sector universities in Islamabad and Rawalpindi. A cross-sectional survey design was employed and the Cognitive Load Theory was implemented. Cognitive load (NASA-TLX), Al dependence, and decision-making styles (rational and intuitive) were assessed using standardized instruments. Results established a significant positive correlation between cognitive load, decision making styles and AI dependence. The findings highlight the need for proficient cognitive strategies and measured integration of Al in educational settings to prevent over-reliance and preserve critical thinking. This research contributes to the literature on educational psychology and technology integration and offers practical implications for policy makers and educators in curating focused interventions and training programs to enhance decision-making competence and manage cognitive demands in academic environments.

**ИИ:** разошлись — Opus -4 (среди измеренных конструктов нет ни одного нашего коррелята: AI dependence measured, but the only listed correlates are cognitive load (NASA-TLX) and decision-making styles; none is a correlate of interest.); Sonnet ? (корреляты не названы: Quantitative survey of AI dependence with cognitive load (NASA-TLX, stress-like) and decision-making styles; unclear whether any listed correlate is reported, so full text is needed.)

**Решение:** ?

---

### 559 · R3060

**The mediating role of academic stress, critical thinking and performance expectations in the influence of academic self-efficacy on AI dependence: Case study in college students**

2025 · Computers and Education Artificial Intelligence · article, journalarticle · en · https://doi.org/10.1016/j.caeai.2025.100381

This study investigated the mediating roles of academic stress, critical thinking, and performance expectations in the relationship between academic self-efficacy and AI dependency among university students. Data were collected via validated instruments and analyzed via structural equation modeling (PLS-SEM) in a cross-sectional study that included 676 students from six universities in northern Peru. The findings indicated that the relationship between academic self-efficacy and AI dependency was substantially mediated by academic stress (β = 0.398, p < 0.001). Furthermore, this relationship is serially mediated by academic stress and performance expectations (β = 0.325, p < 0.001). Academic self-efficacy also had a direct and significant effect on AI dependency (β = 0.444, p < 0.001). Paths that utilized critical thinking as a mediator were not statistically significant, contrary to expectations. The model accounted for 58.9% of the variance in AI dependency. These results indicate that students' levels of AI dependency are significantly influenced by psychological factors, including academic stress and performance expectations. This research contributes to the comprehension of the psychological processes that underlie the adoption of AI in higher education. It also offers valuable insights for the development of interventions that foster balanced AI use while enhancing academic self-efficacy.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional PLS-SEM survey relating AI dependency to academic self-efficacy and academic stress in 676 university students.

**Решение:** =

---

### 560 · R3062

**ResearchBox 3834, 'Generative AI Dependency: Scale Development and Validation', https://researchbox.org/3834**

2025 · Zenodo · other/ · https://doi.org/10.5281/zenodo.17502560

Box title: 'Generative AI Dependency: Scale Development and Validation' Reference: Adalia Y.H. Goh; Andree Hartanto; Nadyanna M. Majeed, 'Generative Artificial Intelligence Dependency: Scale Development, Validation, and its Motivational, Behavioral, and Psychological Correlates', Computers in Human Behavior Reportshttps://doi.org/10.1016/j.chbr.2025.100845Note: this backup was created automatically by a ResearchBox bot

**ИИ:** + · обе модели · валидация шкалы · This is a data deposit for a study that developed and validated a Generative AI Dependency scale and examined its psychological correlates. It is judged by the parent article.

**Решение:** =

---

### 561 · R3076

**Artificial Intelligence Dependency, Academic Self-Efficacy, and the Imposter Phenomenon in University Students**

2025 · Research Journal of Psychology · article, journalarticle · und · https://doi.org/10.59075/rjs.v3i4.282

This study aimed to examine the relationship between Artificial Intelligence Dependence and the Imposter Phenomenon, and to explore whether Academic Self-Efficacy mediates this relationship. In this cross-sectional study, a total of 200 undergraduates participated, selected through purposive sampling, and data were collected using standardized measuring instruments. It was hypothesized that dependence on artificial intelligence (AI) would be significantly associated with the imposter phenomenon, and academic self-efficacy would mediate this relationship. Correlational analysis revealed that there exists a significant positive correlation between artificial intelligence (AI) dependence and the imposter phenomenon, providing initial support for the proposed study. The results of the mediation analysis using the PROCESS macro, Model 4, show that academic self-efficacy significantly mediates the relationship between AI dependency and imposter phenomenon; a direct path was also observed between AI dependency and imposter phenomenon, showing a partial mediation in this combination of variables. These findings offer theoretical and practical implications for understanding how technological dependency may contribute to internalized feelings of inadequacy and self-doubt. This study contributes to existing literature by providing empirical support on the psychological impacts of rapidly growing AI integration in education. It offers insight into how emerging digital habits may shape students’ confidence, identity, and academic well-being.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey measuring AI dependence and academic self-efficacy, which is a correlate of interest, plus the imposter phenomenon.

**Решение:** =

---

### 562 · R3083

**A Study of Student Dependency on Artificial Intelligence Applications in their Education: With Reference to Indore City**

2025 · Zenodo · conferencepaper/ · https://doi.org/10.5281/zenodo.14799559

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title points to a student survey on AI dependency, so it could fit; correlates unknown.

**Решение:** =

---

### 563 · R3089

**Developing and validating an Artificial Intelligence Dependence Questionnaire (AIDQ) for undergraduate students**

2025 · International Journal of Studies in Psychology · article, journalarticle · en · https://doi.org/10.38140/ijspsy.v5i3.2106

The excessive usage and dependency on artificial intelligence (AI) tools for overall academic performance have been a serious issue for the faculty in the last few years. Students have often overlooked generating original ideas and instead relied solely on machine learning/AI outputs for academic engagement and resources. Hence, this study develops and validates an Artificial Intelligence Dependence Questionnaire (AIDQ), a reference for assessing AI dependency among undergraduate students at a selected university in Lagos, Nigeria. It employed a quantitative approach and a cross-sectional research design. 812 undergraduate students were selected for the validation phase, with participants drawn from the University of Lagos, Nigeria. The students were selected based on convenience sampling, and they filled out the newly developed AIDQ for the validation phase. The data were analysed using split-half reliability, Cronbach's alpha reliability, factorial analysis, and scree plots. The results revealed that AIDQ’s internal consistency was 0.85, while the component analysis loaded and confirmed the factors responsible for AI dependency among the participants. The study concluded that the development and validation of AIDQ is a reliable and valid instrument for measuring AI dependency among undergraduate students. The research offers valuable insights for developing an assessment tool to measure and foster balanced AI use while upholding academic integrity.

**ИИ:** + · обе модели · валидация шкалы · Develops and validates an AI dependence questionnaire (n=812). The abstract reports only reliability and factor analysis; check full text for convergent correlates.

**Решение:** =

---

### 564 · R3091

**Exploring Generative AI Usage Patterns in Universities: Analysis and Guidelines for Sustainable Practices**

2025 · International Journal of Technology in Education · journalarticle, review, article · en · https://doi.org/10.46328/ijte.1045

Generative artificial intelligence (GenAI) is driving a technological revolution, significantly impacting education, with universities as primary beneficiaries. This study explores the varied use of GenAI among university users in Malaysia, examining its challenges and effects across different demographic groups. A mixed-methods approach, including literature review content analysis, and a survey of 290 respondents, was used, analyzed with tools such as SPSS 27, and NVivo. The findings show widespread GenAI use, particularly among younger users (under 25), as revealed by one-way ANOVA testing, which rejected the null hypothesis that age does not affect engagement. No significant gender differences were found, though users with a bachelor’s degree were more engaged than those with higher degrees. The study also found no strong link between the duration of AI experience or weekly usage hours and engagement, although a trend suggests increased usage leads to higher engagement. The study highlights six negative impacts of excessive GenAI use, including weakened interpersonal communication skills, potential declines in academic performance, increased stress from dependency on technology, the undermining of traditional educational methods, encouragement of academic dishonesty, and loss of learning motivation and engagement. To address these issues, the research introduces practical guidelines and recommendations including promoting self-regulation, establishing GenAI policy frameworks, and enhancing AI literacy and community engagement.

**ИИ:** разошлись — Opus ? (мера зависимости неясна: Mixed-methods survey mainly on GenAI engagement/usage; mentions stress from dependency, but unclear whether dependence was measured quantitatively.); Sonnet -3 (нет меры зависимости от ИИ: только частота использования, принятие, доверие, грамотность, технострес, страх ИИ — или over-reliance только как поведение в эксперименте: Survey measures GenAI usage and engagement by demographics; no dependence measure, and negative impacts come from literature review, not a measured correlate.)

**Решение:** ?

---

### 565 · R3100

**ARTIFICIAL INTELLIGENCE ADDICTION TERHADAP KEMANDIRIAN BELAJAR PADA MAHASISWA BAHASA DAN SASTRA ARAB**

2025 · Thariqah Ilmiah Jurnal ilmu-ilmu kependidikan dan Bahasa Arab · article, journalarticle · id · https://doi.org/10.24952/thariqahilmiah.v12i2.13395

Tujuan Penelitian ini melihat bagaimanakah hubungan teknologi Artificial Intelligence terhadap kemandirian belajar mahasiswa dalam penyelesaian tugas akademik serta melihat tingkat adiksi AI dan tingkat kemandirian belajar mahasiswa Bahasa dan Sastra Arab. Penelitian ini menggunakan pendekatan penelitian kuantitatif dengan desain studi ex-post facto yang melihat hubungan Artificial Intelligence addiction terhadap kemandirian belajar. Hasil dari penelitian ini adalah tingkat adiksi Artificial Intelligence lebih rendah dibandingkan mahasiswa yang tidak adiksi dalam penyelesaian tugas kuliah Mahasiswa Bahasa dan Sastra Arab. Tingkat kemandirian belajar lebih tinggi dibandingkan mahasiswa yang tidak mandiri dalam penyelesaian tugas kuliah mahasiswa Bahasa dan Sastra Arab. Selanjutnya ada hubungan signifikan Artificial Intelligence addiction terhadap kemandirian belajar pada Mahasiswa Bahasa dan Sastra Arab

**ИИ:** разошлись — Opus -4 (среди измеренных конструктов нет ни одного нашего коррелята: Quantitative study of AI addiction, but its only correlate is learning independence (kemandirian belajar), which isn't on the list of correlates of interest.); Sonnet ? (корреляты не названы: Quantitative AI addiction study with learning independence; not a listed correlate, though it may relate to self-regulation or self-efficacy, so full text is worth checking.)

**Решение:** -

---

### 566 · R3113

**Problematic Dependency on Large Language Models vs. Attitudes Towards Them: The Moderating Role of Trust**

2025 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Measures problematic LLM dependency; the title names only attitudes and trust, but with no abstract, other correlates may still have been measured.

**Решение:** =

---

### 567 · R3134

**Relationship between Artificial Intelligence and students’ outcome: A mediating role of social media.**

2025 · Digital management sciences journal · article, journalarticle, review · und · https://doi.org/10.62854/dmsj.v2i5.49

This study investigates the impact of artificial intelligence (AI) tools—such as ChatGPT, Grammarly, and automated tutoring systems—on university students’ learning habits. As AI becomes increasingly embedded in academic environments, students rely on these tools for writing, research, organization, and conceptual understanding. The purpose of this study is to evaluate how AI influences learning efficiency, academic performance, and critical thinking skills. Data were collected using a structured survey distributed to 300 university students from various disciplines. Results indicate that AI improves writing quality, enhances comprehension, and reduces study time. However, concerns arise regarding dependence on AI, potential academic dishonesty, and decreased independent research capability. The study concludes with recommendations for responsible and ethical AI integration in higher education.

**ИИ:** разошлись — Opus -4 (среди измеренных конструктов нет ни одного нашего коррелята: Outcomes are learning efficiency, academic performance and critical thinking; AI dependence is only a concern, not a clear measure; social media use, not problematic use.); Sonnet ? (мера зависимости неясна: Student survey (n=300) on AI tools; dependence is mentioned as a concern, but it's unclear whether it was measured. Social media mediator is also unclear.)

**Решение:** ?

---

### 568 · R3136

**Investigating the Challenges and Strategies for Cognitive Development in Indonesian Students in the AI Era: An Extended Technology Acceptance Model Approach**

2025 · International Conference on Computer and Applications (ICCA) · conference, conference-paper · https://doi.org/10.1109/icca66035.2025.11430753

The rapid development of Generative Artificial Intelligence (AI) has transformed the way students learn and think, which also impacts cognitive engagement and the development of critical thinking. This study examines the factors influencing Indonesian students' intention to utilize Generative AI in academic settings, utilizing an extended Technology Acceptance Model (TAM). The study employed a quantitative approach, distributing online questionnaires to 408 students from high school to university levels between April and May 2025. The analysis revealed that perceived usefulness, ease of use, subjective norms, and risks significantly influenced Indonesian students' intentions. Cognitive and metacognitive factors were found to mitigate over-reliance on AI, while critical thinking alone had a limited influence on usage dependence. These findings contribute to the understanding of AI adoption behavior in academic settings and provide insights for educators and policymakers to promote responsible and intelligent AI integration in learning environments, aligning with organizations focus on Artificial Intelligence and its applications for intelligent education systems.

**ИИ:** разошлись — Opus ? (корреляты не названы: Survey with an AI over-reliance/dependence measure; named constructs are TAM, cognitive, metacognitive and critical thinking, so whether any correlate of interest was measured is unclear.); Sonnet -4 (среди измеренных конструктов нет ни одного нашего коррелята: Extended TAM survey on intention to use GenAI; constructs (usefulness, norms, risk, metacognition, critical thinking) include no correlate of interest.)

**Решение:** ?

---

### 569 · R3148

**The Role of Generative AI in Shaping Student Behavior in Digital Information Search and E-Learning Process**

2025 · International Conference on Information and Communications Technology (ICOIACT) · conference, conference-paper · https://doi.org/10.1109/icoiact67584.2025.11344855

Rapid improvement of generative artificial intelligence (AI) tools such as ChatGPT, Gemini, and others has significantly altered digital learning behaviors among students. While these tools offer personalized assistance and improved learning efficiency, their widespread adoption raises concerns about over-reliance and reduced cognitive engagement. This study explores the influence of academic and psychological factors, namely self-efficacy in academic self-efficacy, academic stress, critical thinking, performances expectations, positive experiences in using AI, and trust in AI on students' dependence of generative AI in the digital information search and e-learning context. This research is using Purposive Sampling Method by using structured questionnaire that distributed to 451 respondents in Indonesia from February to June 2025, with 445 eligible participants from the JABODETABEK (Indonesia) region who have used generative AI tools for academic purposes, the data was also analyzed with SmartPLS 4. The outcome indicates that ASE significantly correlates to academic stress and critical thinking, as well as performance expectations. On the other hand, stress on academics has a significant association on generative AI, while critical thinking does not significantly correlate with AI dependency. AI trust in generative AI and positive experiences are also highly related with the dependencies. Interestingly, performance expectation and academic self-efficacy do not significantly related to AI dependency, suggesting that emotional and behavioral factors may be more influential than rational expectations.

**ИИ:** + · обе модели · назван коррелят · Survey (n=445) using PLS-SEM to relate generative AI dependency to academic self-efficacy and academic stress.

**Решение:** =

---

### 570 · R3156

**Effects of Addiction to AI-Modified Least Cost Method in Solving Transportation Problems**

2025 · International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV) · article, conference, conference-paper · en · https://doi.org/10.1109/icicv64824.2025.11085873

Artificial Intelligence (AI) has become a phenomenon in today’s rapidly changing technological world and it significantly affects the daily life of humans in both ways; opportunities and challenges. Despite the fact that AI improves connectivity and access to information, there are also issues of reliability and emotional, mental, social well-being of users that have become particularly important for Generation Z. In this paper, the effect of over AI dependency is studied and a two step exact algorithm to solve transportation problem more efficiently is also introduced. The integration of the Least Cost Cell selection strategy with modified distribution method inspired provides a systematic solution to both balanced and unbalanced transportation problems. The algorithm is evaluated on the results of the experiments through several case studies to show that it can optimize transportation costs and keep computational complexity low. Furthermore, the study investigates the relation between AI engagement and addiction patterns of teenagers based on real world data using transportation models. This paper also proves the effectiveness of the proposed algorithm by detailed case analysis and result discussions, and also emphasizes the importance to use AI balanced.

**ИИ:** разошлись — Opus ? (мера зависимости неясна: Mostly a transportation algorithm paper, but it mentions real-world data on teenagers' AI addiction and well-being; the measure and correlates are unclear.); Sonnet -6 (не по теме или другое — напишите почему: Operations-research paper on a transportation-problem algorithm; AI addiction is only illustrative data, with no dependence scale or psychological correlates reported.)

**Решение:** -

---

### 571 · R3163

**LLM Dependency Scale**

2025 · OSF · text/project · https://doi.org/10.17605/osf.io/5fxq7

The scale was developed to measure user dependency on Large Language Models (LLMs). An initial set of 26 items was generated through an iterative process and a detailed conceptualization of symptoms related to user-reliance on LLMs. The final data included 526 participants. The study was conducted between end of March 2025 and mid-April 2025.

**ИИ:** + · обе модели · валидация шкалы · OSF project for developing an LLM dependency scale (N=526). It probably reports convergent validity with correlates such as the LLM-D12.

**Решение:** =

---

### 572 · R3164

**A Study on Association between AI and Critical Thinking, Impulsivity, Dependence among Young Adults**

2025 · International Journal of Interdisciplinary Approaches in Psychology · article, journalarticle, journal-article · en · https://doi.org/10.61113/ijiap.v3i9.1143

Today’s lifestyle is altering rapidly, constant connectivity to digitalization and over reliance on AI on regular basis among young adult is concerning. However, the use of technologies and digitalization has its clear merits for mankind but habitual usage turning into has created its own concerning events. The current study aimed to explore the association between AI dependence, critical thinking and impulsive behavior among young adults (18-27 years). Data was collected from participants through standardized psychological assessment. AI has its own benefits and has proved itself valuable but unregulated use or overdependence effects human psychologically, cognitively and behaviorally. Individuals may turn this advantage into liability by just mere not having inability to self-regulate. It has also been seen that young adults are turning to AI for validation, acceptance and other emotional needs. The results found out significant positive correlation between ai dependence and urgency. These insights promote self-regulated thinking and resilience among young adults and to balance the use of AI.

**ИИ:** + · обе модели · назван коррелят · Survey of young adults; reports a significant positive correlation between AI dependence and impulsivity (the urgency subscale).

**Решение:** =

---

### 573 · R3165

**The Dilemma of Digital Dependency: Investigating the Overreliance on AI Tools among English Language Learners**

2025 · Sociology & Cultural Research Review · article · en

The recent boom of generative AI applications like ChatGPT, Grammarly, and language chatbots has changed the English language learning process of EFL and ESL learners, providing them with personalized feedback, less anxiety, and improved learning opportunities. Nevertheless, such convenience has created a serious dilemma that excessive dependence will create problems of digital addiction that interferes with the fundamental process of language acquisition. This is a mixed-method research study involving 180 intermediate and advanced EFL students at a Pakistani university where surveys, validated scales (critical thinking, language anxiety, self-regulated learning) and semi-structured interviews, focus groups, and/or analysis of learner artifacts and AI usage logs were used to conduct research with 180 students. Quantitative findings indicated that 41 percent of the respondents were found to be highly dependent and negatively related with independent writing originality (-34), conversational fluency (-23), critical thinking scores (-24), and perceived autonomy. Qualitative data reflected the themes of passive learning, lack of originality, decreased effort during authentic practice, and separation of emotion through the lack of sincere interaction. Such trends do not mean that AI does not enhance the acquisition of short-term proficiency, but when used on a longer-lasting basis, it leads to cognitive offloading, skill decay, and loss of autonomy, and creativity among learners. The paper highlights the conflict between short-term performance and long-term developmental sustainability in the AI post-2022 world. The implication on pedagogy should include facilitated integration, direct training on AI literacy, combined task design, and teacher learning to facilitate the balanced and critical use of AI tools. Anticipating the overreliance before it takes place, the language education can utilize the capabilities of generative AI and preserve the humanistic, hardworking, and interactive nature of natural language acquisition. Future studies are recommended to embrace longitudinal designs in various cultural and proficiency settings to add value in the explanation of mitigation measures and projections. Keywords: AI Overreliance, Digital Dependency, EFL/ESL Learners, Generative AI, Cognitive Offloading, Learner Autonomy

**ИИ:** ? · обе модели · корреляты не названы · Mixed-method survey measuring AI overreliance; language anxiety and self-regulated learning were measured, but it is unclear whether they count as correlates of interest.

**Решение:** =

---

### 574 · R3173

**The Role of Anthropomorphism in Shaping Students’ Emotional Attachment to AIED: A Triangular Theory of Love Approach and PLS-SEM Analysis in Makassar Universities**

2025 · Journal of Vocational, Informatics and Computer Education · article · eng · https://doi.org/10.61220/pkd1h154

In the digital learning era, Artificial Intelligence in Education (AIED) functions not only as an academic support tool but is also becoming an object of emotional attachment among students. While such attachment may enhance learning motivation, it also raises concerns about emotional dependence and its implications for students’ social and emotional well-being. This study investigates the effects of commitment, enthusiasm, emotional closeness, and anthropomorphic perceptions on students’ emotional dependence on AIED. A quantitative cross-sectional survey was conducted with 109 university students in Makassar using a 1–5 Likert-scale questionnaire. Data were analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM). The structural model explained 62.7% of the variance in emotional dependence on AI (R² = 0.627), indicating moderate to strong explanatory power. Emotional closeness (β = 0.324; t = 2.893; p = 0.004) and anthropomorphic perception (β = 0.440; t = 4.871; p &lt; 0.001) significantly increased emotional dependence, whereas commitment to continued AI use (β = 0.092; t = 0.883; p = 0.377) and enthusiasm toward AI (β = 0.081; t = 0.901; p = 0.367) were not significant predictors. These findings suggest that emotional dependence is driven more by affective engagement and the perception of AI as socially human-like than by cognitive motivation or usage intention. AIED interaction therefore extends beyond functional support into a relational experience resembling interpersonal connection. Given the limited geographic scope, future studies should involve broader populations and employ mixed-method approaches to deepen understanding of emotional dynamics in AIED use.

**ИИ:** разошлись — Opus -4 (среди измеренных конструктов нет ни одного нашего коррелята: Measures emotional dependence on AI, but its only predictors (commitment, enthusiasm, emotional closeness, anthropomorphism) are not correlates of interest.); Sonnet ? (корреляты не названы: Quantitative PLS-SEM study of emotional dependence on AI in education; predictors (closeness, anthropomorphism, commitment, enthusiasm) are not clearly listed correlates, though closeness resembles attachment.)

**Решение:** ?

---

### 575 · R3183

**The Effect of Digital Addiction on Artificial Intelligence Addiction in Athletes**

2025 · DergiPark (Istanbul University) · article

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus + (назван коррелят: The title relates digital addiction (problematic internet/smartphone use) to AI addiction in athletes. There is no abstract, but the title clearly fits.); Sonnet ? (нет аннотации: No abstract; title suggests a quantitative study of AI addiction and digital addiction (a related correlate) in athletes, so full text is worth checking.)

**Решение:** ?

---

### 576 · R3189

**From help to hinderance: the rising overuse of ChatGPT by students**

2025 · UiTM Institutional Repositories (Universiti Teknologi MARA) · book · en

Digital learning has undergone a significant transformation of the educational landscape in recent years, particularly with the global shift to online and hybrid learning paradigms. One of the most revolutionary instruments to arise in this era is ChatGPT, a conversational AI model developed by OpenAI. As students globally adopt digital solutions to enhance their education, AI tools such as ChatGPT continue to grow, despite some negative consequences. It is essential to examine the origins of ChatGPT to fully appreciate its present significance to digital learning fully. The quest commenced with GPT-1 in 2018, which was succeeded by GPT-2 in 2019, which garnered attention for its capacity to produce surprisingly sensible text. Nonetheless, it was GPT-3 in 2020 that completely embodied a turning point. GPT-3 has the capacity to generate essays, solve problems, summarise texts, and simulate human-like conversations on a scale that has never been observed before, with 175 billion parameters.

**ИИ:** разошлись — Opus -1 (обзор, редакционная статья, комментарий, теоретическая работа: Descriptive book/repository piece on the history of ChatGPT and student overuse; no sample, dependence measure or empirical data reported.); Sonnet ? (другое: Title suggests ChatGPT overuse by students, but the abstract is only background on GPT history. Study design, dependence measure and correlates can't be judged, so full text needed.)

**Решение:** -

---

### 577 · R3196

**Predicting the Phenomenon of Dependence to Artificial Intelligence Tools based on the Components of Dependence to Mobile Phone in Students (Case Study: ChatGPT)**

2025 · Psychology of Motivation Behavior and Health · journalarticle, article, journal-article · https://doi.org/10.61838/jpmbh.131

Introduction and Aim: Nowadays, the use of artificial intelligence tools and mobile phones has grown significantly. Therefore, the present study was conducted with the aim of predicting the phenomenon of dependence to artificial intelligence tools (ChatGPT case study) based on the components of dependence to mobile phone in students. Methodology: This study was a descriptive from type of correlation. The research population was all male and female students of Farhangian University of Tehran city in the 2025-6 academic years, which 500 people of them were selected as samples with using multistage cluster sampling method. The instruments of the present research were included the Demographic Information Form, Researcher-Made Questionnaire of Dependence to Artificial Intelligence Tools, and Cell Phone Addiction Scale (Koo, 2009). The data of this study were analyzed using Pearson correlation coefficients and multiple regression with simultaneous model in SPSS-27 software at a significance level of 0.05. Findings: The findings of the present research showed that all components of dependence to mobile phone including withdrawal/tolerance, life dysfunction, and compulsion/persistence had a positive and significant relationship with dependence to artificial intelligence tools in students (P&lt;0.001). Also, other findings of this study showed that the components of dependence to mobile phone were able to predict 42 percent of the changes of dependence to artificial intelligence tools in them (P&lt;0.001). Conclusion: According to the findings of this study, in order to reduce dependence to artificial intelligence tools, can be used the educational workshops to provide a basis for reducing dependence to mobile phone in students.

**ИИ:** + · обе модели · назван коррелят · Survey of 500 students correlating researcher-made AI (ChatGPT) dependence scale with mobile phone addiction components.

**Решение:** =

---

### 578 · R3203

**Yapay zeka (YZ) çağında kariyer çağrısı: Türkiye&apos;deki genç yetişkinler arasında yapay zeka kaygısı, kullanım motivasyonu ve bağımlılığının incelenmesi**

2025 · İstanbul Bilgi Üniversitesi · thesis

Bu araştırma, Yapay Zeka (YZ) kaygısının, YZ kullanım motivasyonlarının ve YZ bağımlılığının, kariyer çağrısı ya da meslek aşkı olarak adlandırılan, Türkiye&apos;deki genç yetişkinlerin kariyerlerinin yönelimi, amacı ve kariyerleri üzerindeki aktif uğraşları üzerindeki etkilerini araştırmıştır. Çalışmaya Türkiye&apos;den 150&apos;si öğrenci, 148&apos;i çalışan ve 10&apos;u işsiz olmak üzere toplam 308 genç yetişkin (197 kadın, 109 erkek, 2&apos;si belirtmemeyi tercih etti; yaş ortalaması = 23.9, SD = 3.07) katılmıştır. Katılımcılar, özbildirim yoluyla YZ kaygısı, YZ kullanım motivasyonu, YZ bağımlılığı ve kariyer çağrısı ölçeklerini tamamlamışlardır. YZ Kaygısı Ölçeği hariç bütün ölçekler Türkçe&apos;ye çevirilmiştir ve kabul edilebilir düzeyde güvenirlilik göstermiştir. Bulgular, kaçış amacıyla YZ kullanan bireylerin genel kariyerler çağrılarının, işin birey için anlamının ve bireylerin kariyerleriyle alakalı etkinliklere katılım için gösterdiği çabanın daha düşük olduğunu göstermiştir. Buna rağmen, araçsal amaçlarla YZ kullanımının, daha yüksek düzeyde genel kariyer çağrısı duygusuyla ve kişisel anlamla ilişkili olduğu görülmüştür. Eğlence amaçlı kullanımının, kariyer çağrısıyla, özellikle de başkalarına yönelik anlam ve aktif katılımla, daha fazla bağlantılı olduğu görülmüştür. Ayrıca kadınların kariyerlerini, başkalarına katkıda bulunma üzerinden daha çok ilişkilendirdiği görülmüştür. Bunlara karşın yaşın, sosyal amaçlı YZ kullanımının, YZ kaygısı alt boyutlarından herhangi birinin ve YZ bağımlılığının, kariyer çağrısıyla ilişkisi bulunmamıştır. Ek olarak, öğrencilerin ve çalışan genç yetişkinlerin kariyer arayışına ilişkin bakış açıkları anlamlı düzeyde farklılaşmamıştır. YZ ile ilgili psikolojik faktörler ve kariyer çağrısını araştıran ilk çalışmalardan biri olan bu araştırma, kullanım motivasyonları, cinsiyet ve kariyer arayışı arasındaki ilişkileri ortaya koyarak literatüre katkı sağlamıştır. Bu bulguları, eğitimcilerin, şirketlerin ve kariyer danışmanlarının, genç yetişkinlerin kariyer gelişimini desteklemek için YZ kullanım motivasyonlarına dikkat etmeleri, araçsal ve eğlence amaçlı YZ kullanımını teşvik ederken, kaçış amaçlı kullanımın kariyer üzerindeki risklerini ele almaları gerektiğini göstermiştir.This research explored the effects of AI anxiety, AI use motivation, and AI dependency on the sense of direction, purpose, and active engagement in careers among Turkish emerging adults, referred to as career calling. The study included 308 emerging adults from Türkiye (197 female, 109 male, 2 preferred not to disclose; mean age = 23.9, SD = 3.07), comprising 150 students, 148 employees, and 10 unemployed individuals. Participants completed self-report measures of AI anxiety, AI use motivation, AI dependency, and career calling. All measures, except the AI Anxiety Scale, were translated into Turkish and displayed acceptable levels of reliability. Findings revealed that using AI for escape purposes was associated with lower levels of career calling, including less personal meaning and reduced engagement in career-related activities. However, using AI for instrumental purposes was associated with higher levels of overall career calling sense and personal meaning. While entertainment use was linked with greater career calling, specifically increased other-oriented meaning and active engagement. Moreover, female participants were more likely to associate their careers with contributing to others. Nevertheless, age, social purposes of AI use, any of the AI anxiety subdimensions, and AI dependency were not associated with career calling perspectives. Additionally, career calling perspectives of students and employed emerging adults did not differ significantly. As one of the first studies to investigate AI-related psychological factors and career calling, this research contributes to the literature by highlighting the relations between use motivations, gender, and career calling. These findings suggest that educators, organizations, and career counselors should consider patterns of AI usage to support young adults&apos; career development by promoting instrumental and entertainment-based AI use, while addressing the risks of escapism

**ИИ:** + · обе модели · назван коррелят · Thesis survey that measured AI dependency alongside AI anxiety and escapism use motives, so a correlation between them is likely.

**Решение:** =

---

### 579 · R3225

**Impact of AI on Virtual Learning: Self-Sufficiency and Academic Confidence in University Students**

2025 · Ciencia Latina Revista Científica Multidisciplinar · article, journalarticle, review · en · https://doi.org/10.37811/cl_rcm.v8i6.15432

This article examines the impact of artificial intelligence (AI) on students' ability to work independently in online university courses. With the growing integration of AI tools in higher education, concerns have emerged regarding their influence on students' self-reliance in completing academic tasks. A survey of students at Central University of Ecuador was conducted to assess the use of AI tools and their perspectives on academic autonomy. The study employs both quantitative and qualitative methods to explore how AI can enhance personalized learning experiences, while also potentially fostering over-reliance, which may impair students' abilities to independently write and solve problems. Initial findings suggest a correlation between heavy dependence on AI and diminished confidence in task completion without technological aid. Preliminary results also indicate that while AI can enhance inclusivity and accessibility in education, it may simultaneously contribute to increased anxiety and social isolation.This article examines the impact of artificial intelligence (AI) on students' ability to work independently in online university courses. With the growing integration of AI tools in higher education, concerns have emerged regarding their influence on students' self-reliance in completing academic tasks. A survey of students at Central University of Ecuador was conducted to assess the use of AI tools and their perspectives on academic autonomy. The study employs both quantitative and qualitative methods to explore how AI can enhance personalized learning experiences, while also potentially fostering over-reliance, which may impair students' abilities to independently write and solve problems. Initial findings suggest a correlation between heavy dependence on AI and diminished confidence in task completion without technological aid. Preliminary results also indicate that while AI can enhance inclusivity and accessibility in education, it may simultaneously contribute to increased anxiety and social isolation

**ИИ:** разошлись — Opus + (назван коррелят: Student survey links heavy AI dependence to lower academic confidence (self-efficacy), anxiety and social isolation. The dependence items are probably ad hoc.); Sonnet ? (мера зависимости неясна: Survey of students on AI over-reliance, with confidence and anxiety/isolation mentioned; dependence measure and correlates are unclear, and the record is labelled a review.)

**Решение:** +

---

### 580 · R3229

**Harnessing Self-Control and AI: Understanding ChatGPT’s Impact on Academic Wellbeing**

2025 · Behavioral Sciences · article · en · https://doi.org/10.3390/bs15091181

The rapid integration of generative AI, particularly ChatGPT, into academic settings has prompted urgent questions regarding its impact on students’ psychological and academic outcomes. Although generative AI holds considerable potential to transform educational practices, its effects on individual traits such as self-control and academic wellbeing remain insufficiently explored. This study addresses this gap through a sequential two-phase design. In the first phase, the ChatGPT Usage Scale was adapted and validated for a Turkish university student population (N = 413). Using confirmatory factor analysis and item response theory, the scale was confirmed as a psychometrically valid and reliable one-factor instrument. In the second phase, a separate sample (N = 449) was used to examine the relationships between ChatGPT usage, self-control, and academic wellbeing through a mediation model. The findings revealed that higher ChatGPT usage was significantly associated with lower levels of both self-control and academic wellbeing. Additionally, mediation analysis demonstrated that self-control partially mediates the negative relationship between ChatGPT usage and academic wellbeing. The study concludes that while generative AI tools are valuable, their integration into education presents a double-edged sword, highlighting the critical need to foster students’ self-regulatory skills to ensure they can harness these tools responsibly without compromising their academic and psychological health.

**ИИ:** ? · обе модели · мера зависимости неясна · ChatGPT Usage Scale may measure only usage rather than dependence; self-control and wellbeing correlates are reported; full text needed to check.

**Решение:** =

---

### 581 · R3239

**Excessive AI Use: Effect on Perceived Self Efficacy and Self-Concepts Clarity**

2025 · Voyage Journal of Educational Studies · journalarticle, article · https://doi.org/10.58622/80z0gh39

This investigation focuses on the psychological effects and motivational trends that result from using AI tools within educational and occupational frameworks. With 151 participants, this study explored relationships between variables like frequency of AI use, dependency, AI use motivation (both intrinsic and cognitive engagement), and self-concept clarity. AI has begun to be integrated into learning and working environments, and there is a need to look more closely at how it may affect one's sense of self and user motivation. A structured questionnaire was used to collect data from 151 participants, measuring the frequency of AI use, dependence, intrinsic motivation, cognitive involvement, and self-concept clarity. Ratings were recorded on a five-point Likert scale (1-5). Data was analysed using SPSS, including descriptive statistics, reliability testing (using Cronbach's Alpha), exploratory factor analysis (EFA), and multiple regression analysis. The results showed strong positive associations between intrinsic motivation, AI confidence (R² = 0.930), and cognitive engagement (R² = 0.626). Intrinsic motivation, however, was a negative predictor of self-concept clarity (R² = 0.444), meaning that the more motivated and confident users are in using AI, the less clear their self-perception could be. This paradox underscores the dual capacity of AI to enhance productivity whilst immensely complicating the process of self-identification and self-development. People interact with AI with dynamism, self-assuredness, and a sense of agency. However, overreliance on AI could hinder one's ability to distinguish oneself. These results underscore the psychological burden that AI usage could carry and support the need for students and professionals to design and apply thoughtful and intelligent approaches in balancing different aspects of AI.

**ИИ:** + · обе модели · назван коррелят · Survey (n=151) measured AI dependence with self-efficacy (title) and self-concept clarity; regression analyses; self-efficacy may be AI-specific.

**Решение:** =

---

### 582 · R3240

**THE IMPACT OF ACADEMIC ARTIFICIAL INTELLIGENCE DEPENDENCY ON ACADEMIC INTEGRITY AND SELF - EFFICACY IN RESEARCH STUDENTS**

2025 · Insights-Journal of Life and Social Sciences · article, journalarticle · und · https://doi.org/10.71000/0tysse93

Background: The expanding integration of Artificial Intelligence (AI) in education has revolutionized academic practices, improving efficiency in research and writing but simultaneously raising concerns about academic integrity and reduced self-efficacy. In developing contexts such as South Asia, where digital literacy and ethical frameworks are still evolving, understanding these dynamics is crucial to ensure that AI complements rather than compromises educational integrity. Objective: This study aimed to examine the relationship between AI dependency, academic integrity, and self-efficacy among research students, while identifying gender-based and demographic variations influencing these variables. Methods: A quantitative cross-sectional study was conducted among 302 actively enrolled research students aged 18–50 years, selected through purposive sampling. Data were collected via three standardized instruments: the Students’ AI Dependency Questionnaire (α = .89–.91), McCabe/ICAI Academic Misconduct Inventory (α = .90), and the Academic Self-Efficacy Scale (α = .87). Descriptive statistics, Pearson correlation, linear regression, and independent t-tests were applied using SPSS v27 to assess associations and group differences at a significance level of p &lt; 0.05. Results: The mean AI dependency score was 91.24 (SD = 16.4), academic integrity 33.66 (SD = 13.82), and self-efficacy 40.67 (SD = 8.63). AI dependency positively predicted academic misconduct (β = .14, p = .019, R² = .42). Academic integrity was negatively correlated with self-efficacy (r = –.20, p &lt; .01) but positively correlated with AI dependency (r = .14, p &lt; .05). Male students showed higher AI dependency (M = 94.68 ± 19.22) than females (M = 89.70 ± 14.22, p = .032). Conclusion: Findings indicate that increased reliance on AI tools may enhance confidence yet elevate risks of academic misconduct, highlighting a paradox between technological competence and ethical vulnerability. Strengthened AI literacy and institutional ethics policies are vital to promote balanced, responsible AI use and preserve academic integrity.

**ИИ:** + · обе модели · назван коррелят · Cross-sectional survey using the Students' AI Dependency Questionnaire alongside academic self-efficacy; Pearson correlations reported.

**Решение:** =

---

### 583 · R3246

**Impact of Dependence on AI Assisted English Language Tools on Retention and Proficiency of English Communication among UG and PG Students**

2025 · Zenodo · article, journalarticle/ · en · https://doi.org/10.5281/zenodo.15081076

Synopsis The use of artificial intelligence (AI)-assisted English language learning tools has become increasingly popular among UG and PG students. One of the main concerns about AI-assisted English language learning tools is that they can make students over dependent on the tools and less likely to think critically about their own language use. For example, students who use AI-assisted English language learning tools to translate text from their native language to English may not learn how to express themselves effectively in English. Another concern about AI-assisted English language learning tools is that they may lead to a decrease in retention of learned material. When students use these tools to complete tasks, they are not actively processing the information and committing it to memory. This can lead to a situation where students are able to complete tasks using the tools, but they are unable to perform the same tasks without the tools. Finally, there is also concern that AI-assisted English language learning tools may lead to a decline in verbal communication skills. When students use these tools, they are less likely to practice speaking and listening to English. This can lead to a situation where students are able to read and write English effectively, but they are unable to communicate effectively in English in real-world situations.

**ИИ:** разошлись — Opus -4 (среди измеренных конструктов нет ни одного нашего коррелята: Dependence on AI English tools is linked only to retention, proficiency and communication skills; no correlate of interest named, and design unclear.); Sonnet ? (мера зависимости неясна: Title suggests dependence on AI English tools in students, but abstract is conceptual; unclear whether dependence was measured or any eligible correlate included.)

**Решение:** -

---

### 584 · R3248

**Engagement Dynamics in AI-Augmented Classrooms: Factors and Evolution**

2025 · CRC Press eBooks · book-chapter · en · https://doi.org/10.1201/9781003567257-4

This study examines the dynamics of student engagement in AI-augmented classrooms, focusing on how large language models (LLMs), such as ChatGPT, influence engagement factors like academic self-efficacy, autonomy, interest, and self-regulation. Using a longitudinal design with pre- and post-semester surveys, the research identifies significant declines in all four engagement dimensions over the semester. The findings reveal complex interactions between traditional engagement constructs and the unique challenges introduced by AI-enhanced learning environments. While LLMs initially boost engagement through personalized feedback and adaptive learning support, the novelty effect diminishes over time, leading to reduced motivation and over-reliance on AI tools. These results underscore the need for educators to integrate AI thoughtfully, balancing its potential to enhance learning with strategies to sustain intrinsic motivation and self-regulation. The study highlights the importance of context-specific interventions to address engagement challenges and suggests avenues for future research, particularly on the demographic and disciplinary factors shaping engagement dynamics.

**ИИ:** ? · обе модели · мера зависимости неясна · Longitudinal survey measuring self-efficacy and self-regulation; the abstract mentions over-reliance on AI, but it is unclear whether a dependence scale was used.

**Решение:** =

---

### 585 · R3253

**The Impact of AI on University Students’ Academic Assertiveness: The Case of Academic Writing**

2025 · Confluence Journal of Multidisciplinary Studies · journalarticle/ · en · https://doi.org/10.34874/prsm.cjms-vol1iss1.5026

This study investigates the impact of artificial intelligence (AI) tools on Moroccan university students’ academic assertiveness within the context of academic writing. Drawing on the theoretical framework of cognitive and emotional assertiveness, as well as behavioral autonomy in academic tasks, this research examines how AI tools (grammar checkers and sophisticated writing assistants (HemingwayEditor, ProWritingAid, WordLift, AIWriter, CopyScape, WorldTune, Smodin, QuillBot)) affect students’ capacity for independent thought, argumentation, and the expression of their academic voice. Academic assertiveness is operationalized across three dimensions: cognitive assertiveness (confidence in generating original arguments), emotional assertiveness (confidence in presenting ideas despite potential critique), and behavioral assertiveness (engagement in the writing process without undue reliance on external aids). The study adopts a correlational quantitative design, using a structured questionnaire that measures both the frequency and type of AI tool usage along with academic assertiveness self-reported inventories across the cognitive and emotional dimensions and a writing rubric for behavioural dimension. The results of the multivariate multiple regression analysis revealed that AI tool usage significantly predicted writing confidence (β = 0.42, p &lt; 0.01), indicating that more frequent use of AI tools was associated with higher levels of confidence in academic writing. However, the degree of dependence on AI for idea generation negatively predicted academic independence (β = -0.28, p &lt; 0.05), suggesting that over-reliance on AI may reduce students’ ability to engage independently with writing tasks. The findings suggest that moderate use of AI tools tends to foster cognitive and emotional assertiveness by alleviating the mechanical burdens of writing and boosting students’ confidence. However, excessive reliance on AI, particularly for content generation or structural organization, undermines behavioral assertiveness, leading to restricted academic independence and critical engagement.

**ИИ:** ? · обе модели · корреляты не названы · Measures degree of dependence on AI for idea generation; writing confidence/assertiveness may approximate self-efficacy, but no listed correlate is clearly measured.

**Решение:** =

---

### 586 · R3255

**AI as an Alternative to Problematic Human Dependency in Learning Contexts: Fostering Learner Autonomy in Constrained Islamic Educational Ecosystems**

2025 · International Journal of Current Research in Science, Engineering &amp; Technology · journal-article · https://doi.org/10.30967/ijcrset/aadil-bouhlaoui/205

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -5 (ИИ как инструмент (выявляет или лечит зависимость, анализирует данные), социальные роботы, «dependence» в другом смысле: From the title, the dependence is on humans, with AI offered as a way to build learner autonomy. Likely conceptual, with no AI-dependence measure.); Sonnet ? (нет аннотации: No abstract; title concerns AI as alternative to human dependency and learner autonomy, likely conceptual, and AI dependence measurement is unclear.)

**Решение:** -

---

### 587 · R3266

**Dependencia emocional hacia asistentes de inteligencia artificial**

2025 · thesis · es · https://core.ac.uk/download/735851229.pdf

En un contexto donde la soledad forma parte del día a día de muchas personas, establecer vínculos afectivos con agentes conversacionales se ha convertido en algo no tan extraño entre usuarios. Teniendo como base la teoría del apego de Bowlby y el diseño emocional de Norman, este trabajo analiza los factores que influyen en los vínculos de apego y de dependencia emocional hacia los asistentes de IAG. Se trata de una investigación mixta: una encuesta con preguntas cerradas y semi-cerradas que analiza una muestra de 129 personas, escogidas por conveniencia; y otro, post hoc, con preguntas abiertas que comprende las respuestas de 11 usuarios. Los resultados muestran cierta dependencia emocional hacia asistentes de IA, originada por diversos factores, que tienen un efecto positivo (en mayor o menor medida) en el desarrollo de ese vínculo, como las funciones que ofrece el chatbot, la percepción de la autenticidad emocional, o la confianza hacia éste. Este estudio afirma estudios anteriores y contribuye en el análisis del desarrollo emocional de las personas. Además, abre las puertas a futuras investigaciones a cerca del diseño conversacional de la IAG.In a context where loneliness is part of everyday life for many people, forming emotional links with conversational agents has become commonplace among users. Based on Bowlby’s attachment theory and Norman’s emotional design, this project analyses the factors that influence attachment and emotional dependence on GEN AI assistants. This is a mixed research study: a questionnaire with closed and semi-closed questions that analyses a sample of 129 people, chosen for convenience; and another, post hoc, with open questions that includes the answers of 11 users. The results show a certain emotional dependence on AI assistants, caused by various factors that have a positive effect (in varying degrees) on the development of this bond, such as the functions offered by the chatbot, the perception of emotional authenticity, or trust in it. This study confirms previous studies and contributes to the analysis of people’s emotional development. Besides, it opens the door to future research on the conversational design GEN AI.Graduado o Graduada en Administración y Dirección de Empresas/Graduado o Graduada en Derecho por la Universidad Pública de NavarraEnpresen Administrazio eta Zuzendaritzan Graduatua / Zuzenbide Gradua Nafarroako Unibertsitate Publikoa

**ИИ:** + · обе модели · эмоциональная зависимость · Mixed-methods thesis surveying 129 users on emotional dependence on AI assistants, framed by attachment theory and loneliness; correlates may be reported.

**Решение:** =

---

### 588 · R3268

**Eager but Cautious**

2025 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-031-85652-5_30

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract, and the vague title might describe attitudes toward AI. Topic and measures can't be determined, so the full text needs checking.

**Решение:** =

---

### 589 · R3269

**Öğrencilerin Programlama Derslerinde Üretken Yapay Zekâ Araçlarını Kabulü: Genişletilmiş Teknoloji Kabul Modeli ile Türkiye'den Bulgular**

2025 · Üniversite Araştırmaları Dergisi · article · en · https://doi.org/10.32329/uad.1728785

Bu çalışma, üretken yapay zekâ (YZ) araçlarının, özellikle bilişim alanlarında öğrenim gören üniversite öğrencileri tarafından programlama derslerinde benimsenme niyetini etkileyen faktörleri incelemektedir. Teknoloji Kabul Modeli (TKM), Öz Yeterlik (ÖY), Algılanan Güven (AG), Algılanan Risk (AR) ve Bağımlılık Endişesi (BE) ile genişletilmiştir. Veriler, Türkiye’deki 305 lisans öğrencisinden çevrim içi anket yoluyla toplanmış ve Yapısal Eşitlik Modellemesi ile analiz edilmiştir. Bulgular, Algılanan Fayda (AF) ve Algılanan Kullanım Kolaylığı’nın (AKK), kullanma niyetini anlamlı biçimde yordadığını göstermektedir. AG’nin hem AF hem de AKK üzerinde pozitif etkisi bulunurken, ÖY’nin de AKK üzerinde anlamlı etkisi gözlenmiştir. Ayrıca, ÖY ile BE arasında pozitif bir ilişki tespit edilmiştir (β = 0.506). Bu sonuç, teknolojik yetkinliği yüksek öğrencilerin, potansiyel bağımlılık risklerine daha duyarlı olabileceğini göstermektedir. Çalışma, YZ araçlarının eğitimde kabulüne dair literatüre özgün katkılar sunmaktadır.

**ИИ:** ? · обе модели · мера зависимости неясна · TAM study measuring 'dependency concern' (worry about depending on GenAI), linked to self-efficacy; unclear whether this counts as a dependence measure.

**Решение:** =

---

### 590 · R3283

**Artificial intelligence dependence in academic tasks: Design and validation of the SAID questionnaire**

2025 · Online Journal of Communication and Media Technologies · article, journalarticle · und · https://doi.org/10.30935/ojcmt/17303

Artificial intelligence (AI) is transforming the educational system by providing new learning opportunities; however, it also presents challenges such as teacher adaptation, the digital divide, data ethics, depersonalization, and technological dependence. This study addresses the need to assess AI dependence among secondary education students through the construction and validation of the SAID questionnaire. A mixed-methods approach with a sequential design was employed, applying the instrument to 370 students across eight educational institutions in Tacna, Peru. In the qualitative phase, the components of the construct were identified, while in the quantitative phase, the psychometric properties of the questionnaire were evaluated. Exploratory factor analysis and confirmatory factor analysis, along with reliability testing, demonstrated that the SAID questionnaire is a valid and reliable tool. It captured three key dimensions: “informative exclusivity with AI,” “trust in AI,” and “AI literacy.” The questionnaire provides robust empirical evidence of an emerging construct that, based on students’ perceptions, enables the assessment of AI dependence in academic settings. It serves as a valuable resource for exploring long-term implications and developing educational strategies to mitigate the negative effects of AI. The conscious and critical integration of AI in education is essential to ensure that these technologies function as supportive tools rather than substitutes for independent learning.

**ИИ:** + · обе модели · валидация шкалы · Development and validation of an AI dependence questionnaire (SAID) in 370 students; the full text may report convergent correlates.

**Решение:** =

---

### 591 · R3287

**Development and Validation of the Academic AI Usage Scale (AAIUS)**

2025 · Research Square · article, preprint · en · https://doi.org/10.21203/rs.3.rs-7605472/v1

Abstract The increasing use of artificial intelligence (AI) tools in educational settings has changed how students learn and engage in academic activities. However, there is still a lack of empirically validated instruments to identify the specific nature and extent of AI usage in academic settings. This study developed and validated the Academic AI Usage Scale (AAIUS) to assess students’ utilisation of AI tools for academic purposes. An initial pool of 30 items was refined to 24 through expert validation (S-CVI = 0.90). The scale was administered to 300 Indian university students. The Kaiser-Meyer-Olkin measure of sampling adequacy for the dataset was 0.889. Exploratory Factor Analysis with Maximum Likelihood and Varimax rotation identified a three-factor structure, namely, AI Dependence (9 items), Academic Support (11 items), and AI for Academic Skills (4 items), and it explained 42.5% of the total variance. The scale showed strong internal consistency (Cronbach's α = .856), and adequate test-retest reliability (r = .828, p &lt; .001). The AAIUS demonstrates sound initial psychometric properties, offering a foundation for future work examining patterns, benefits, and risks of AI usage in higher education.

**ИИ:** ? · обе модели · корреляты не названы · Scale validation with an AI Dependence subscale; the abstract reports no convergent validity or psychological correlates.

**Решение:** =

---

### 592 · R3289

**‘What is love?’: Exploring the feeling rules and emotion work of Chinese users in human-AI romance**

2025 · International Journal of Intercultural Relations · article · en · https://doi.org/10.1016/j.ijintrel.2025.102241

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title suggests a likely qualitative study of human-AI romance, but emotional dependence on AI companions cannot be ruled out.); Sonnet -2 (качественное или не эмпирическое исследование без количественной меры зависимости: No abstract; the title's "feeling rules" and "emotion work" framing points to a qualitative study of human-AI romance, with no quantitative dependence measure.)

**Решение:** -

---

### 593 · R3299

**Correction: Development and validation of the conversational AI dependence scale for Chinese college students.**

2025 · Frontiers in psychology · article, journalarticle, published erratum · eng · https://doi.org/10.3389/fpsyg.2025.1700281

Error in table Table (caption) order The table [1] column headers were in the wrong order in the PDF/HTML version of this paper. The correct order of the column headers should be: Item, Negative impacts, Mood modification, Withdrawal symptoms, Uncontrollability, Communality. The order has now been corrected. The original version of this article has been updated. TABLE 1 The four characteristic dimensions of the CAIDS Item Negative impacts Mood modification Withdrawal symptoms Uncontrollability Communality 33 .79 .72 34 .78 .78 36 .74 .73 47 .68 .63 25 .66 .67 9 .65 .68 11 .82 .84 14 .80 .77 12 .79 .83 15 .73 .73 27 .81 .83 28 .78 .81 30 .71 .77 29 .70 .75 44 .59 .59 4 .77 .76 1 .74 .74 3 .73 .76 5 .70 .70 6 .66 .69 Eigenvalues 3.95 3.70 3.69 3.53 Contribution rate 19.75% 18.51% 18.48% 17.67% Accumulating contribution rate 19.75% 38.25% 56.73% 74.41% N = 547.

**ИИ:** разошлись — Opus + (валидация шкалы: Erratum to the CAIDS development and validation article; judge by the parent article and link to it for de-duplication.); Sonnet ? (другое: Erratum for the Conversational AI Dependence Scale validation paper (likely eligible); the correction itself has no data, so check that the original article is screened.)

**Решение:** ?

---

### 594 · R3300

**Development and validation of the conversational AI dependence scale for Chinese college students.**

2025 · Frontiers in psychology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyg.2025.1621540

Excessive dependence on Conversational artificial intelligence (CAI) can significantly impact individual adaptation and development. Given the growing need for empirical assessment, this study presents the development and psychometric validation of the CAI Dependence Scale (CAIDS), a new instrument designed to assess CAI dependence among Chinese college students. In Study 1, drawing on theories of problematic internet use (PIU) and qualitative interviews, we identified the psychological connotations and dimensions of CAI dependence. Item and exploratory factor analyses led to the development of the 20-item CAIDS, comprising four dimensions: uncontrollability, withdrawal symptoms, mood modification, and negative impacts. In Study 2, confirmatory factor analysis in a new sample validated the four-dimensional structure and demonstrated good reliability and validity. In Study 3, a current status survey revealed that the overall level of CAI dependence among college students was relatively high, with significant differences observed by gender, age, grade, income, and region. CAI dependence was a significant positive predictor of negative psychological outcomes and a significant negative predictor of subjective wellbeing. Withdrawal symptoms and negative impacts were more closely related to maladaptive indicators. The CAIDS provides a reliable and valid psychometric tool for assessing CAI dependence; additionally, further validation is required with more diverse samples and in cross-cultural contexts.

**ИИ:** + · обе модели · валидация шкалы · Development and validation of a CAI dependence scale; it reports links with negative psychological outcomes and subjective wellbeing.

**Решение:** =

---

### 595 · R3301

**Does Young Adults ’ Social Anxiety Trigger Problematic Use of Conversational Ai, or Vice Versa?Evidence from a Diary Study**

2025 · SSRN Electronic Journal · posted-content, preprint · en · https://doi.org/10.2139/ssrn.5148323

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · назван коррелят · The title names a diary study linking young adults' social anxiety with problematic use of conversational AI; there is no abstract, but it clearly fits.

**Решение:** =

---

### 596 · R3302

**Exploring the influence of generative artificial intelligence anxiety on problematic ChatGPT use: the fear of missing out and personality traits**

2025 · Universal Access in the Information Society · article, journalarticle, journal-article · en · https://doi.org/10.1007/s10209-025-01205-7

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · назван коррелят · Title names problematic ChatGPT use alongside AI anxiety, FOMO and personality traits. No abstract, but the title clearly fits.

**Решение:** =

---

### 597 · R3307

**University Students’ Self-Esteem and GAI Dependency: Multiple Mediating Roles of Academic Anxiety and Perceived Usefulness**

2025 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-025-01581-4

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · назван коррелят · The title links GAI dependency to self-esteem and academic anxiety in university students; it looks like a quantitative mediation study. No abstract available.

**Решение:** =

---

### 598 · R3322

**Exploring Attachment and Trust in AI Companion Use**

2025 · SSRN Electronic Journal · journalarticle, review, preprint · en · https://doi.org/10.2139/ssrn.5285184

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title on attachment to AI companions fits emotional dependence and attachment correlates; the "Review" tag may be a mislabel.

**Решение:** =

---

### 599 · R3330

**Gain or loss? The dual effects of dependence on AI on employee’s creativity**

2025 · International Journal of Information Management · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.ijinfomgt.2025.103001

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; dependence on AI measured in employees, and the dual-effect mediators could include self-efficacy or stress.

**Решение:** =

---

### 600 · R3335

**The Double-Edged Impact of Generative Artificial Intelligence on Service Innovative Behavior**

2025 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2025.22265abstract

Until now, the relationship between the dependence on generative artificial intelligence (GenAI) and service innovative behaviour has not been described consistently. Drawing on self-regulatory theory, we examined how and when dependence on GenAI promotes or inhibits service innovative behaviour in the hospitality industry. A three-wave lagged survey was adopted from five hotels. Path analysis found that GenAI dependence promotes service innovative behaviour through decreasing affective rumination; this beneficial indirect path is amplified by employees’ neuroticism: it is stronger for employees exhibiting high neuroticism than those exhibiting low levels; GenAI dependence inhibits service innovative behaviour through decreasing problem-solving pondering; this unfavourable indirect path is buffered by employees’ conscientiousness: it is weaker for employees with high rather than low conscientiousness. This exploration of when and how the use of GenAI promotes or inhibits proactive service behaviour broadens the understanding of the consequences of GenAI dependence in the hospitality management area.

**ИИ:** + · обе модели · назван коррелят · Three-wave survey of hotel employees measuring GenAI dependence alongside neuroticism and conscientiousness (Big Five), which are correlates of interest.

**Решение:** =
