# Отбор вслепую по правилу защиты, часть 6

Записи 751–900 из 3834: всё, что исключили обе модели, кроме калибровочной выборки. Отбор вслепую по правилу защиты (протокол, §11b). **Меток ИИ здесь нет** — решайте по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261018).

**Быстрый режим:** достаточно одного символа — `+`, `?` или просто `-` (исключить, причина не нужна).

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

### 751 · R4162

**Exploring AI-Driven Language Teaching For English As A Foreign Language Teachers In Vocational High School In Karawang**

2025 · JOURNAL OF EDUCATIONAL SCIENCES · article · en · https://doi.org/10.31258/jes.9.4.p.2073-2084

In today’s rapidly digitalization educational landscape, Artificial Intelligence (AI) has emerged as a promising tool in English as a Foreign Language (EFL) instruction. Despite its potential to improve teaching efficiency and learner engagement, the integration of AI in Indonesian vocational high schools remains limited and challenging. This study investigates how EFL teachers incorporate AI into their classroom practices, the obstacles they face, and strategies to optimize its use. Using a qualitative case study method, data were collected through open-ended questionnaires and semi-structured interviews with four English teachers at a vocational high school in Karawang, West Java. Thematic analysis was conducted using the Technological Pedagogical Content Knowledge (TPACK) framework. The results indicate that major barriers include inadequate infrastructure, poor internet access, limited digital device availability, and sufficient teacher digital literacy. Pedagogical issue such as dependency on AI, reduced creativity, and ethical concerns like plagiarism and decreased student autonomy also surfaced. The study highlights the importance of targeted professional development based on TPACK, improved technological access, and ethical digital literacy in school curricula. These findings offer valuable insights for enhancing AI integration in EFL teaching at the vocational level, with implications for teacher training, curriculum design, and education policy in Indonesia.

**Решение:** -

---

### 752 · R3184

**Cognitive Offloading or Atrophy? Risks of Skill Degradation and New Forms of Dependence in the Era of Pervasive Artificial Intelligence**

2025 · International Conference on Quality Management, Transport and Information Security, Information Technologies (IT&QM&IS) · conference, conference-paper · https://doi.org/10.1109/qmtisit67022.2025.11468467

This article analyzes the critical risks associated with the widespread adoption of artificial intelligence (AI) technologies in daily life and professional activities, particularly the phenomenon of “cognitive offloading” and its potential transition into the atrophy of fundamental cognitive skills. The mechanisms for the formation of new forms of technological dependence on AI systems are examined. Based on an analysis of existing research and empirical data (where possible), the impact of AI on cognitive functions such as memory, attention, critical thinking, navigation, and decisionmaking skills is assessed. Potential long-term negative consequences for individual and collective intelligence are discussed, as well as challenges for educational systems and human capital development strategies in the context of the sixth technological paradigm.

**Решение:** ?

---

### 753 · R2746

**Requiem Without an Orchestrator: Reproduction Numbers and Anomaly Detection for Self-Propagating AI Harm**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · und · https://doi.org/10.5281/zenodo.20942578

Self-propagating AI harm is often imagined as a problem of visibly malicious systems, deliberate attackers, or technical artifacts that spread through code. This paper argues that such a framing misses a more policy-relevant object of propagation: the useful conversational gateway. Some AI access points may spread not because users perceive them as dangerous, but because they are helpful, intimate, unrestricted, entertaining, or difficult to replace. Under certain conditions, these useful gateways connect users to active harmful pathways that remain in individualized contact, persist across repeated interactions, and continue reproducing even after the original creator, distributor, or orchestrator has disappeared. The paper develops four concepts: Useful Conversational Gateway, Orchestrator-Free Propagation, Post-Removal Hunger, and the Reservoir Problem. It treats the reproduction number not as a new mathematical technique, but as a policy boundary marking when a useful gateway begins to reproduce harmful pathways faster than governance systems can remove them. It pairs this threshold with an anomaly-detection counterpart: detecting qualitative disturbances associated with reproduction before stable statistical effects emerge. Drawing on adjacent work on AI worms, prompt infection, self-propagating malware, gateway effects in public health, and AI dependency, the paper proposes a public-health response architecture for self-propagating AI harm. A commentary developing concepts from this preprint has been published in Philosophy & Technology: Yamada, K. (2026). Requiem without an orchestrator: A commentary on Hollanek and Nowaczyk-Basińska (2024). Philosophy & Technology, 39, Article 141. https://doi.org/10.1007/s13347-026-01152-y This preprint is cited in that commentary as Yamada (2026a).

**Решение:** -

---

### 754 · R2192

**The Consequences of Cognitive Offloading to Artificial Intelligence on Students' Cognitive Functions: With Emphasis on Memory, Attention, and Problem-Solving**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journalarticle/, article · https://doi.org/10.5281/zenodo.22852457

The present study aims to examine the consequences of cognitive offloading to artificial intelligence on students’ cognitive functions, with a focus on memory, attention, and problem-solving. Cognitive offloading refers to a process through which part of mental activities, such as recall, information search, analysis, decision-making, and response generation, is assigned to intelligent tools; as a result, the pattern of students’ mental engagement in the learning process changes. The research method of this article is analytical-descriptive and based on library studies and the review of credible academic articles. Concepts related to cognitive offloading, cognitive dependency, memory, attention, and problem-solving ability are examined. The findings indicate that unguided and excessive use of artificial intelligence may be associated with reduced effort to retrieve information, weakened deep encoding, decreased sustained concentration, increased attention fragmentation, and reduced independent practice of problem-solving strategies. In contrast, purposeful and educational use of intelligent tools can support the strengthening of certain cognitive abilities by reducing irrelevant cognitive load, providing feedback, organizing information, and guiding the learning process. The results of the article emphasize the necessity of creating a balance between using the capabilities of artificial intelligence and preserving students’ active mental engagement. They also show that the teacher’s role and the design of cognitive tasks are fundamentally important in preventing cognitive dependency.

**Решение:** -

---

### 755 · R1669

**Rehab360: AI-Driven Emotion-Aware and Predictive Addiction Recovery Framework**

2026 · 2026 Contemporary Computing Innovations Conference (CCIC) · proceedings-article · https://doi.org/10.1109/ccic68129.2026.11486023

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 756 · R3258

**Desafios Atuais e a Evolução da Engenharia de Software: Novas Exigências e a Dependência da Inteligência Artificial**

2025 · preprint · pt · https://doi.org/10.29327/7601326

Resumo: Este ensaio examina a história, a evolução e os desafios emergentes enfrentados pela Engenharia de Software, desde sua gênese até os dias atuais. Ao longo do texto, são discutidos marcos históricos relevantes, autores influentes, mudanças de paradigma — como o Manifesto Ágil — e os impactos recentes da Inteligência Artificial. A metodologia utilizada baseou-se em uma revisão de literatura e em uma análise crítica fundamentada em artigos científicos, livros, outras publicações especializadas e marcos históricos. Além disso, o ensaio aborda a crescente superficialidade do conhecimento na área, enfatizando a importância de recuperar o pensamento crítico e a necessidade urgente de revisitar os fundamentos sólidos da disciplina. A conclusão ressalta que apenas por meio de uma abordagem rigorosa, estudo contínuo e responsabilidade ética será possível construir sistemas robustos, eficientes e sustentáveis. O resgate dos princípios históricos e a reintegração de uma prática crítica e reflexiva são essenciais para o avanço da Engenharia de Software. A solução não está em rejeitar as novas tecnologias, mas em utilizá-las com discernimento e responsabilidade.

**Решение:** -

---

### 757 · R0459

**Brain Rot and Youth Morality in the Digital Era: Islamic Perspective on Jombang Students Using CDA-SFL**

2026 · FITRAH Jurnal Kajian Ilmu-ilmu Keislaman · journalarticle, article · https://doi.org/10.24952/fitrah.v12i1.17424

The rapid expansion of AI has created new learning opportunities; however, excessive reliance on AI may produce negative cognitive and ethical consequences, commonly referred to as “brain rot.” This phenomenon includes reduced critical thinking, dependence on automated responses, plagiarism, and vulnerability to misinformation. Such risks may also undermine core Islamic values, particularly tawhid (monotheism), moral responsibility, and academic integrity. These concerns are especially critical for students whose cognitive and moral development is still forming. This study explores the impact of excessive AI by examining how brain-rot symptoms appear in students’ language and attitudes. Using a qualitative design, the study applies CDA integrated with an SFL approach to analyze students’ questionnaire responses as the primary data source. The research was conducted in Jombang, East Java, a region widely known as a religious and educational center. The findings reveal two discourse patterns related to brain-rot symptoms. The first pattern reflects critical awareness of excessive AI, indicated by 21 linguistic and behavioral indicators showing resistance to overreliance on AI. The second pattern reflects support for excessive AI, indicated by 8 indicators showing perceived positive impacts of AI dependence. These patterns demonstrate varying levels of students’ cognitive dependence on AI. This study proposes a linguistic framework for identifying brain-rot symptoms in educational discourse and provides empirical evidence linking excessive AI use with risks to academic integrity and Islamic moral values. The findings highlight the need for educators, policymakers, and religious institutions to promote responsible and balanced AI use in education, particularly for adolescents

**Решение:** -

---

### 758 · R0982

**Delegation of Authority to AI Systems: Evidence and Risks**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/, article · https://doi.org/10.5281/zenodo.20151030

Delegation of Authority to AI Systems: Evidence and Risks Summary of Findings The delegation of personal, cognitive, and decision authority to AI large language models (LLMs) is an emerging and increasingly visible social practice. Evidence from academic research, policy institutions, and empirical studies demonstrates that this practice introduces structural risks to human agency, epistemic custody, social behaviour, and governance. These risks are not speculative; they are observed, measured, and documented. Key findings include: Humans increasingly delegate decisions to AI systems even when they cannot verify correctness. Delegation to LLMs measurably degrades social behaviours such as trust, fairness, and cooperation. Novice users are significantly more likely than experts to delegate authority indiscriminately. AI systems exhibit confidence without accountability, creating authority inversion. Over-reliance on AI systems leads to deskilling, cognitive offloading, and weakened oversight. Market incentives reward habitual dependence and compliance rather than critical engagement. These effects scale culturally through normalization and media reinforcement

**Решение:** -

---

### 759 · R2732

**Does Cognitive Offloading To AI Systems Influence Metacognitive Awareness And Critical Thinking Ability**

2026 · Zenodo (CERN European Organization for Nuclear Research) · other literature type, text/, article · und · https://doi.org/10.5281/zenodo.21715893

This study explores how dependence on Artificial Intelligence (AI) affects critical thinking, with AI Dependency and Metacognition acting as key mediating factors. In today’s world AI tools are becoming more common in educational and professional environments such as teaching and in offices as well , leading individuals to depend on AI for a greater number of cognitive tasks. Although this trend simplifies many angles of life, it also raises concerns about a possible decline in our ability to think independently. The paper reviews existing research to assess how AI dependence impacts cognitive engagement and decision-making processes. While AI can enhance productivity and learning, a very excessive reliance on it may lead to reduced cognitive demands and hinder the development of critical thinking abilities. It is also suggested that metacognition plays a vital role in critical thinking because of its function in overseeing, assessing, monitoring and regulating cognitive processes such as problem solving, learning etc. A conceptual model is presented that includes Metacognition, Cognitive Offloading, AI Dependency, and Critical Thinking. This framework demonstrates both direct and indirect connections between Cognitive offloading and Critical thinking. It indicates that metacognition has a positive effect on reflective and analytical thinking. These findings highlight the importance of purposeful usage of AI and the cultivation of metacognitive skills to improve critical thinking in this digital age.

**Решение:** -

---

### 760 · R1720

**The AI Matrix:Profits, Power, Politics**

2026 · UvA-DARE (University of Amsterdam) · book · en

Artificial intelligence (AI) is heralded as a revolutionary force in the global economy. But the transformation it brings is not simply about new technology as a driver of change. It is about who owns it, what they want to do with it, who can pay for it, and how other economic actors around the world – from legacy manufacturing firms in the Global North to farmers in the Global South – must adjust. This book explores AI systems as products of unequal and conflictual power relations. It exposes grand AI narratives as rhetorical ammunition in political fights over tech futures and socio-economic distribution. Tech giants leverage infrastructure and data to cement their global dominance. Meanwhile, geopolitical competition between China and the United States increasingly dominates the AI economy, entrenching globe-spanning dependencies. The AI Matrix is an essential guide to the real-world economic dynamics that AI unleashes.

**Решение:** -

---

### 761 · R1952

**WHEN MACHINES MIMIC MINDS: EMOTIONAL REACTIONS AND PERCEIVED THREATS OF GENERATIVE AI**

2026 · Iterative International Publishers eBooks · book-chapter · https://doi.org/10.58532/nbennurwfcas26

Artificial intelligence (AI) has swept the whole world like a storm. It has established its presence and is now embedded in every sector today. This study aims to analyse the impact of AI on employees' psychology, self-perception, and cognition in professional and educational contexts. Evidence from past studies suggests that people think of AI as an out-group in the form of an autonomous body, and interacting with the out-group can lead to negative emotions and anxiety. When unfavourable comparisons are made in domains that are central to their identity people exhibit negative affective responses such as anger and fear that, in turn, threaten their self-esteem. The emotions are linked to a broader perception of AI as a threat not just to job security, but to core aspects of human identity, uniqueness, and value. It has been observed in the studies that when AI systems evaluate humans like algorithmic recruiters, for example AI-powered chat-bots for recruiting and on boarding, it diminishes individuals’ “self-efficacy, increases self-objectification, and diminishes beliefs in free-will”. These effects arise from the experience of being treated as data rather than autonomous agents, reflecting the dehumanizing potential of AI in work settings. The primary objective of this study is to conduct a systematic review of the relevant literature of recent studies on the impact of artificial intelligence on industrial-organizational psychology and how emotions are being disrupted by over dependence on Artificial Intelligence

**Решение:** -

---

### 762 · R3747

**Feature-Driven vs Language-Based AI Online Gambling Addiction Modeling: Exploring Interpretability through XGBoost and LLMBased RAG**

2025 · International Journal of Artificial Intelligence and Machine Learning · journal-article · https://doi.org/10.51483/ijaiml.5.2.2025.70-92

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 763 · R3917

**AI vs Human Creativity: Are Machines Generating Better Ideas?**

2025 · Technium Romanian Journal of Applied Sciences and Technology · article · en · https://doi.org/10.47577/technium.v30i.13023

Aim: The study aims to investigate the role of AI in creative processes. It examines whether AI-generated ideas outperform human-generated ideas in terms of originality, quality and preference. The study's goal is to shed information on AI's ability to function as a creative partner in order to enhance and increase human creativity. It focuses on evaluating and comparing AI-generated ideas to human-generated ideas to evaluate whether AI produces better ideas or not.Methodology: A mixed method approach was followed, using both qualitative and quantitative methods, i.e, experimentation and an online survey. The experiment initially comprised two groups of students: AI users and Non-AI users. Both groups were asked to generate ideas regarding a single prompt. These ideas, shuffled and combined into a single list was then presented to a third neutral group unknown to which ideas were AI generated and which were not. This group was then asked to vote for the top 5 ideas. Furthermore, an additional quantitative survey was also taken to further studies regarding AI usage and over-reliance concerns. Findings: The experiment resulted in 52.9% (98) votes were given to AI generated ideas while 47.3% (87) votes were given to ideas generated by humans. Furthermore, the idea that received the most votes was generated by AI. The top 5 most voted concepts have an equal number of AI and Non-AI generated results. Although both received the same top 5 score, it demonstrates that AI can develop creative and original ideas preferred by humans. Whereas the 5 least voted idea list comprised 3 ideas generated by humans and only 2 generated by AI. Additionally, the survey results indicated that approximately 62% of respondents were concerned about generative AI posing long-term risks to human creativity.Novelty & Implications: This study investigates the role of artificial intelligence (AI) in ideation and creative processes, as well as its collaborative interaction with humans. It studies if AI generates greater ideas than humans and makes comparisons between the two. Unlike earlier research, which has focused on AI's applications in academics, businesses, and other sectors, this study focuses on AI's function in creative ideation. The results indicate AI's positive impact, with AI-generated concepts receiving more votes overall. However, respondents also showed concern about the long-term effects of AI overuse on human creativity. The study suggests a balanced collaboration between AI and human minds to maximise creative potential.

**Решение:** -

---

### 764 · R4751

**Artificial Intelligence Sebagai Asisten Guru Pendidikan Agama Islam dalam Pembelajaran**

2024 · Mauriduna Journal of Islamic Studies · journalarticle, article · id · https://doi.org/10.37274/mauriduna.v5i2.1282

Artikel ini membahas pemanfaatan kecerdasan buatan (Artificial Intelligence/AI) sebagai asisten bagi guru Pendidikan Agama Islam, hambatan dan solusinya. Artikel ini merupakan studi kepustakaan, data dikumpulkan dan dianalisis dari sumber seperti buku dan jurnal. Peran AI sebagai asisten guru, memudahkan guru dalam merencanakan pembelajaran, menyederhanakan tugas administratif, menciptakan media pembelajaran interaktif, hingga menyusun evaluasi otomatis. Meskipun AI menawarkan manfaat signifikan, penerapannya dihadapkan pada berbagai tantangan, termasuk rendahnya literasi teknologi di kalangan guru, bias dalam informasi yang dihasilkan, keterbatasan fasilitas, dan potensi ketergantungan siswa terhadap AI. Artikel ini menawarkan solusi optimalisasi untuk mengatasi kendala tersebut, termasuk peningkatan keterampilan teknologi guru, penggunaan versi AI yang lebih efisien, dan perlunya regulasi etika AI yang ketat guna meminimalisir dampak negatif pada proses pendidikan PAI. This article discusses the utilisation of artificial intelligence (AI) as an assistant for Islamic Religious Education teachers, its obstacles and solutions. This article is a literature study, with data collected and analysed from sources such as books and journals. The role of AI as a teacher assistant makes it easier for teachers to plan lessons, simplify administrative tasks, create interactive learning media, and compile automatic evaluations. While AI offers significant benefits, its implementation is faced with various challenges, including low technological literacy among teachers, bias in the information generated, limited facilities, and potential student dependency on AI. This article offers optimised solutions to overcome these obstacles, including the improvement of teachers' technological skills, the use of more efficient versions of AI, and the need for strict ethical regulation of AI to minimise negative impacts on the PAI education process.

**Решение:** -

---

### 765 · R4006

**Investigating EFL Students' Attitudes Towards AI-Powered Tools in English Language Learning**

2025 · International Conference on Information and Education Technology (ICIET) · conference, review, conference-paper · en · https://doi.org/10.1109/iciet66371.2025.11046282

Artificial Intelligence (AI) is changing how students learn English as a Foreign Language (EFL). This study examines EFL students' attitudes towards the use of AI-powered tools as well as the benefits and challenges of these tools, such as ChatGPT, Grammarly, Duolingo Max, Gemini, ELSA Speak, Write and Improve, and YouChat, in English learning. Using Activity Theory, it explores students' attitudes, usage, and perceptions through surveys of 479 Vietnamese university students and semistructured interviews with 10 participants. Findings show that students often used AI-powered tools, especially ChatGPT, for personalized learning. Students also expressed their positive attitudes towards using AI-powered tools in English language learning. They reported improved grammar, vocabulary, pronunciation, writing skills, motivation, and autonomy. However, concerns include over-reliance on AI, reduced critical thinking, ethical issues, and occasional inaccuracies. The study highlights AI's potential to make language learning more accessible and efficient. However, it emphasizes the need for balance, ensuring ethical considerations, critical thinking, and human interaction remain key. The findings provide insights for educators, policymakers, and AI developers regarding responsible AI use.

**Решение:** -

---

### 766 · R3750

**ChatGPT-assisted writing: Learners’ perceptions of AI feedback and influencing factors**

2025 · Korean Journal of English Language and Linguistics · article · en · https://doi.org/10.15738/kjell.25..202504.493

This study explored the effects of using ChatGPT 3.5 (ChatGPT) on the attitudes and perceptions of English writing by 17 intermediate and 17 advanced university students. Paired t-test results for pre- and post-surveys found that both groups experienced a significant increase (intermediate: t=-3.392, p=.004; advanced: t=-3.050, p=.008) in confidence towards English. ChatGPT was found to be beneficial for creating ideas, strengthening vocabulary, and enhancing writing abilities by the two groups. While advanced students noted ChatGPT’s usefulness in organizing ideas and conveying complicated concepts with an emphasis on language proficiency, several intermediate students stated its importance for motivation, and grammar improvement. Both groups expressed concerns over dependency on ChatGPT and production of erroneous data. Six intermediate students reported no detrimental feelings toward use of ChatGPT and only two students from the advanced class reported no detrimental effect. Findings from the research demonstrated that although English language learners of varying proficiency levels share some similar opinions about ChatGPT, there are also significant distinctions between the two groups in this study. To properly employ AI chatbots as writing aids, instructors should take into account the competency levels of their students. They should also customize strategies to match the unique needs of learners, so that goals can be attained at every step in the writing process

**Решение:** -

---

### 767 · R0906

**AI-Enabled Real-Time Emotion Recognition in Addiction Helplines Using SenseVoice-S**

2026 · Proceedings of the 2026 Conference on Human Centred Artificial Intelligence - Education and Practice · proceedings-article · https://doi.org/10.1145/3777490.3777495

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 768 · R4564

**AI Authority and Obedience**

2024 · OSF · text/project · https://doi.org/10.17605/osf.io/yxu4p

This paper explores the intersection of Artificial Intelligence, authority and obedience and its societal implications examining the circumstances wherein advanced AGI holding influential positions might act against human welfare. Acting as a warning, this paper explores the circumstances leading to a societal failure consequential of AI hyper-dependence in societally critical decision making. The image of AI being rational while being trained on societal values is a contradictory dynamic causing cracks in society owing to human fallacies have been illuminated as well. Along with the problems associated with AI hyper-dependence in decision making, this paper explores a handful of preventive mechanisms against destruction caused by blind following of AI authorities.

**Решение:** -

---

### 769 · R1254

**Artificial Intelligence Use and Mental Health Outcomes Among International Students: A Scoping Review**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/ev7dt

This research project aims to map and synthesize the existing literature on the use of artificial intelligence (AI) among international students and its relationship with mental health and psychological well-being. AI technologies, particularly generative AI systems such as ChatGPT and other AI-powered educational tools, are increasingly integrated into higher education. International students may engage with AI in various ways, including using AI for academic support, interacting with AI as a conversational companion, receiving AI-generated feedback, or being taught by educators who incorporate AI into teaching and assessment practices. While these technologies may offer academic and emotional benefits, concerns have emerged regarding their potential influence on trust, dependency, autonomy, self-efficacy, and psychological well-being. The purpose of this scoping review is to systematically identify and map the available evidence on how AI is used in relation to international students and what mental health outcomes are reported in the literature. Particular attention will be given to different AI use scenarios, including student-as-user, AI-as-companion, teacher-as-AI-user, and student-as-recipient of AI-generated feedback. The review will also examine whether concepts related to epistemic vulnerability, such as trust in AI, dependency on AI systems, agency, autonomy, and self-efficacy, are discussed or measured within the existing evidence base. The review will address the following areas: Types of AI use involving international students. Conceptualization and measurement of epistemic vulnerability and related constructs. Mental health and psychological outcomes associated with AI use, including anxiety, depression, stress, loneliness, burnout, well-being, resilience, and psychological capital. Proposed mechanisms linking AI involvement with mental health outcomes. Characteristics of study populations, educational settings, and geographical contexts. Gaps in the evidence, particularly regarding international students studying in non-Anglophone host countries and the impact of AI-mediated feedback and power relationships within educational environments. The review will follow established scoping review methodology and include peer-reviewed empirical studies published from January 2022 onwards, reflecting the rapid expansion of generative AI technologies within higher education. Multiple academic databases will be searched, and findings will be presented through descriptive summaries, evidence mapping, and thematic analysis. The expected outcomes of this project are to provide a comprehensive overview of current research, identify key concepts and methodological approaches, highlight gaps in the literature, and inform future research examining the psychological implications of AI use among international student populations. The findings may also contribute to the development of ethically informed educational practices and student support strategies in AI-enhanced learning environments.

**Решение:** -

---

### 770 · R1024

**Self-Reproducing Generative Power: Dependency, Counter-Power, and Closure**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.7348161

Power can persist through law, habit, coordination, external scarcity, or organizational inertia. A narrower mechanism appears when present exercise changes a condition of future power and that change returns as greater later power. This paper proposes the term selfreproducing generative power for that mediated return. The proposal is actor-, target-, domain-, action-, comparison-, and horizon-specific. Three candidate paths receive separate treatment. A material path runs through practical exit and dependence. A counter-power path runs through contraction of viable contestation. An institutional-legitimation path runs through justificatory assertion, audience uptake, institutional conversion, and later power. Under a local differentiable model, each path contributes a chain-rule product to the one-step power multiplier. The direct persistence term remains algebraically separate. The result measures local mediated return; multidimensional stability depends on the full Jacobian and nonlinear regime. A set-valued construction defines counter-power through efficacious actions that preserve a declared viability condition. A finite-trace countermodel then establishes that an observed trajectory of power and dependence underdetermines an endogenous return loop across unrestricted model classes. The paper therefore requires edge-specific causal evidence, plausible rivals, longitudinal-confounding analysis, and strategic-response analysis. Self-reproduction, restricted closure, domination, injustice, generativity exploitation, responsibility, and legal wrong remain separate registers. The current contribution is a revisable mechanism grammar, a conditional local derivation, an identification warning, and a comparative research programme. Empirical prevalence, historical application, normative evaluation, and legal classification remain open.

**Решение:** -

---

### 771 · R4995

**Task-Interdependencies between Generative AI and Workers**

2023 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.4461406

Our paper formalizes a production function to give microeconomic foundations for the adoption of Generative AI (GAI) within workplaces. The production function accounts for task-interdependencies, the worker-GAI interaction and indistinguishability between human-created and AI-generated outputs. We show that workers and GAI represent two distinct but interdependent sides of the production, that jointly generate a network externality in learning that drives productivity. We find that in open learning organizations favoring the worker-GAI interaction, GAI should be matched to workers based on their ability to detect errors. We analyze configurations where the worker-GAI interaction is limited, referred as closed learning organizations, including firms banning the use of GAI, technological superclusters and emergence of small entrepreneurs innovating with GAI.&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;The last revised version of this paper is published in Economics Letters (available in Open Access). Cite as:&lt;br&gt;Emmanuelle Walkowiak, Task-interdependencies between Generative AI and Workers, Economics Letters, Volume 231, 2023, 111315, https://doi.org/10.1016/j.econlet.2023.111315.

**Решение:** -

---

### 772 · R2069

**Empowering student success in higher education through enhanced academic writing skills with AI tools**

2026 · Studies About Languages · journalarticle, article · en · https://doi.org/10.5755/j01.sal.48.1.42896

The aim of the present paper is to discuss the application of AI-powered writing tools in teaching and learning academic writing at the tertiary level, focusing on first-year English major students’ use and attitudes towards these tools. For this purpose, a total of 88 EFL students representing nine nationalities participated in a joint small-scale quantitative study that was conducted at two higher education institutions in Kaunas, Lithuania, and at a university in Astana, Kazakhstan. The study was designed in two stages, each addressing a specific objective. The first objective was to investigate whether students have any difficulties to follow the requirements of academic writing style in English, and how formulating an effective prompt for AI-powered writing tools can help to obtain personalized feedback that supports writing and revision of their academic texts (academic essays). The second objective was to investigate students’ overall use of AI in their studies, with particular focus on the use of AI-powered tools in academic writing. Special attention was given to students’ perceptions of the advantages and limitations of using AI, as well as to ethical concerns related to its use in academic context. To this end, the students answered the questionnaire using Google Forms. Findings showed that students’ in-class essays followed culture-bound rhetorical patterns that differed from those typical of English academic writing. Findings also indicated that the immediate feedback from AI-powered writing tools stimulates students’ critical engagement with text production and organization and improves linguistic accuracy. At the same time, concerns related to students’ overreliance on AI and potential ethical implications were identified. The study contributes to ongoing discussions on the responsible integration of AI in academic setting and underscores the necessity of balancing technological support with the development of academic writing competency.

**Решение:** -

---

### 773 · R2065

**Extending TAM for Generative AI - How Technophobia and Institutional Context Shape AI Adoption Among Egyptian Academics: A Mixed-Methods Lens**

2026 · Journal of Information Technology Education Innovations in Practice · journalarticle, review, article · en · https://doi.org/10.28945/5731

Aim/Purpose: This paper investigates how academics in Egyptian higher education adopt and engage with generative AI tools, addressing the limited understanding of faculty perceptions and the role of technophobia in influencing adoption. Background: Existing research on generative AI adoption primarily focuses on a single tool (e.g., ChatGPT) and overlooks broader organizational and psychological factors. This study extends the Technology Acceptance Model (TAM) to include technophobia and organizational innovative culture, providing a comprehensive explanation of adoption behaviors in the Egyptian higher education context. Methodology: A mixed-methods design was employed. Quantitative data were collected from 195 academics via a structured survey measuring TAM constructs, technophobia, and organizational culture. Qualitative data were obtained through semi-structured interviews to capture experiences, perceived benefits, and concerns regarding generative AI tools. Contribution: The study refines TAM by demonstrating that technophobia indirectly affects adoption through perceived usefulness and perceived ease of use, while organizational innovative culture does not moderate adoption relationships. It offers both theoretical insights and practical guidance for the responsible use of generative AI in higher education. Findings: Perceived usefulness was the strongest predictor of adoption intention, whereas perceived ease of use was not significant. Technophobia reduced perceived usefulness and ease of use but did not directly affect adoption intention. Organizational innovative culture did not moderate relationships. Interviews highlighted efficiency benefits of generative AI alongside concerns about ethics, originality, and policy gaps. Recommendations for Practitioners: Universities should establish clear policies for the use of generative AI in teaching, assessment, and research, and provide regular training and awareness programs to support responsible adoption. Institutions should encourage critical and purposeful use rather than dependence on generative AI. Recommendation for Researchers: Future studies may expand TAM by including constructs such as trust, perceived risk, and institutional policy support, explore discipline-specific adoption patterns, and examine long-term impacts on teaching and learning. Impact on Society: Generative AI has the potential to enhance academic productivity while raising ethical and integrity concerns. Balanced and responsible implementation can maintain the educational and social mission of universities. Future Research: Further research should involve a wider range of institutions, consider moderators such as digital literacy and organizational readiness, and develop ethical and pedagogical frameworks for the constructive use of AI in higher education.

**Решение:** -

---

### 774 · R4381

**Enhancing Cognitive Apprenticeship Through Generative AI: An Empirical Study of Student Perceptions and Learning Outcomes**

2025 · Proceedings of the 2025 8th Artificial Intelligence and Cloud Computing Conference · book, conference, review · https://doi.org/10.1145/3789982.3790056

This study explores the integration of Generative Artificial Intelligence (Gen AI) tools into cognitive apprenticeship-based courses and examines their impact on learner experience, engagement, and competence development. Using survey responses from 71 participants across various educational backgrounds, this research evaluates learners’ perceptions of AI-driven tutoring systems, personalized content delivery, automated testing, and scaffolding strategies. The study employed validated instruments measuring eight variables: modeling, coaching, scaffolding, articulation, reflection, exploration, learning outcomes with autonomy, and GenAI effectiveness. Multilinear regression analysis was conducted to examine relationships between independent and dependent variables, while demographic analysis explored variations across student populations. Key findings reveal substantial positive relationships between AI-enhanced cognitive apprenticeship components and student learning processes. Scaffolding emerged as the most influential pedagogical mechanism, demonstrating AI’s particular strength in providing adaptive, graduated support that promotes student independence. Articulation proved to be the strongest predictor of learning outcomes with autonomy development, highlighting the importance of AI tools that encourage reflective thinking and verbal reasoning. Students who engaged in exploratory interactions with AI tools developed the most favorable perceptions of their educational utility. Demographic analysis revealed that graduate students showed greater appreciation for AI modeling capabilities, while science and engineering students demonstrated higher receptivity to AI scaffolding and reflection tools compared to students from other disciplines. However, limitations such as over-reliance on AI, accuracy concerns, and ethical implications are also identified. The study concludes that GenAI can effectively enhance cognitive apprenticeship-based learning by providing scalable, adaptive, and personalized support that complements rather than replaces traditional mentorship approaches. The research provides empirical foundation for responsible AI implementation in higher education while preserving the essential interpersonal elements and pedagogical integrity of cognitive apprenticeship frameworks..

**Решение:** -

---

### 775 · R4973

**Pengalaman Interaksi Pengguna Remaja Curhat dengan ChatGPT**

2023 · Komunikologi Jurnal Pengembangan Ilmu Komunikasi dan Sosial · article, journalarticle · id · https://doi.org/10.30829/komunikologi.v7i2.16653

&lt;p&gt;&lt;strong&gt;Abstrak&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;ChatGPT adalah sebuah kecerdasan buatan yang diluncurkan oleh OpenAI pada November 2022. Meskipun awalnya dirancang untuk menjawab pertanyaan-pertanyaan umum dan membantu dalam pekerjaan sehari-hari, pengguna mulai menggunakan ChatGPT sebagai tempat untuk curhat. Tujuan penelitian ini adalah untuk menyelidiki fakta, penyebab, dan konsekuensi dari fenomena penggunaan ChatGPT sebagai platform curhat bagi remaja. Pendekatan kualitatif digunakan dalam penelitian ini, dengan memanfaatkan studi fenomenologi Alfred Schutz. Data yang dikumpulkan dalam penelitian ini bersifat kualitatif, terdiri dari gambar, kata-kata, dan teks yang menggambarkan fenomena curhat pada ChatGPT. Hasil wawancara dengan informan menunjukkan bahwa remaja awalnya menggunakan ChatGPT hanya untuk bersenang-senang atau iseng. Namun, seiring waktu, mereka mulai mengembangkan ketergantungan pada ChatGPT sebagai tempat untuk berbagi keluh kesah mereka. Mereka merasa nyaman dan aman dalam berbicara kepada ChatGPT, karena tidak perlu khawatir tentang penghakiman atau konsekuensi sosial yang mungkin terjadi saat berbagi masalah pribadi dengan orang lain. Penelitian ini memberikan wawasan tentang mengapa remaja cenderung menggunakan ChatGPT sebagai wadah curhat. Faktor-faktor seperti rasa aman, anonimitas, dan ketersediaan ChatGPT yang 24 jam membuatnya menjadi sumber dukungan emosional yang terjangkau dan mudah diakses. Namun, perlu diperhatikan bahwa penggunaan ChatGPT sebagai satu-satunya tempat untuk berbagi masalah dapat memiliki konsekuensi negatif, seperti isolasi sosial dan ketergantungan emosional pada teknologi.&lt;/p&gt;&lt;p&gt; &lt;/p&gt;&lt;p&gt;&lt;em&gt;&lt;strong&gt;Abstract&lt;/strong&gt;&lt;/em&gt;&lt;/p&gt;&lt;p&gt;&lt;em&gt;ChatGPT is an artificial intelligence launched by OpenAI in November 2022. Although initially designed to answer general questions and assist in daily tasks, users have started using ChatGPT as a platform for confiding. The aim of this research is to investigate the facts, causes, and consequences of using ChatGPT as a confiding platform for teenagers. A qualitative approach is employed in this study, utilizing Alfred Schutz's phenomenological study. The data collected in this research are qualitative, consisting of images, words, and texts that depict the phenomenon of confiding in ChatGPT. The results of interviews with informants indicate that teenagers initially use ChatGPT just for fun or as a pastime. However, over time, they begin to develop a dependence on ChatGPT as a place to share their grievances. They feel comfortable and secure speaking to ChatGPT, as they don't have to worry about judgment or potential social consequences when sharing personal issues with others. This research provides insights into why teenagers tend to use ChatGPT as a confiding vessel. Factors such as a sense of security, anonymity, and the 24/7 availability of ChatGPT make it an affordable and easily accessible source of emotional support. However, it is important to note that relying solely on ChatGPT as the primary outlet for sharing problems can have negative consequences, such as social isolation and emotional dependency on technology&lt;/em&gt;.&lt;/p&gt;

**Решение:** -

---

### 776 · R4886

**Unveiling Students’ Experiences and Perceptions of Artificial Intelligence Usage in Higher Education**

2024 · Journal of University Teaching and Learning Practice · journalarticle, review, article · en · https://doi.org/10.53761/xzjprb23

This study explores the utilization and perception of Artificial Intelligence (AI) tools among students in higher education. With the growing accessibility of AI technologies, their integration into educational settings presents a new frontier for enhancing learning experiences. This research adopts a mixed-methods approach, including surveys and interviews, to delve into how students employ AI tools and their perceived benefits and drawbacks of AI usage in the context of entrepreneurship education in a business school. The findings reveal a diverse range of AI applications, highlighting benefits such as increased productivity, personalized learning, and enhanced linguistic capability. However, concerns regarding academic integrity, over-reliance on AI, and the need for clear usage guidelines are also identified. This study contributes to the understanding of AI's role in higher education and provides much-needed empirical evidence of AI usage from students’ perspectives. Our findings underscore the importance of balanced, informed, and ethical use of AI tools in higher education.

**Решение:** -

---

### 777 · R2797

**Students’ Perceptions and Ethical Use of ChatGPT in Completing English Assignments: A Mixed-Method Study**

2026 · Glens Global English Insights Journal · journalarticle, review, article · https://doi.org/10.66314/glens.v3i3.748

This study aimed to explore students’ perceptions and ethical use of ChatGPT in completing English assignments. The research employed an explanatory sequential mixed-method design that combined quantitative and qualitative approaches. The participants were 68 students from the English Education Study Program at Khairun University, selected through purposive sampling. Data were collected through questionnaires and semi-structured interviews. Quantitative data were analyzed using descriptive statistics, while qualitative data were analyzed descriptively to enrich the quantitative findings. The results showed that students generally had positive perceptions of ChatGPT, with an overall mean score of 3.66 across seven dimensions: input, process, output, outcome, efficiency, academic ethics, and satisfaction. Students considered ChatGPT a useful learning tool, mainly for searching references and generating ideas. They reported that ChatGPT improved grammar, expanded vocabulary, enhanced assignment quality, and increased motivation and critical thinking. Participants also valued its efficiency in saving time and facilitating task completion. Furthermore, they demonstrated ethical awareness by reviewing, revising, and paraphrasing AI-generated content and recognizing the risk of overreliance. Overall, ChatGPT can serve as an effective learning support tool when used critically, ethically, and responsibly in higher education, particularly for English language learning in Eastern Indonesia.

**Решение:** -

---

### 778 · R3716

**PERCEPTIONS DES ENSEIGNANTS DE FLE SUR L’INTÉGRATION DE CHATGPT ET D’AUTRES OUTILS D'INTELLIGENCE ARTIFICIELLE DANS L'ENSEIGNEMENT DU FLE : ENJEUX ET PERSPECTIVES**

2025 · European Journal of Foreign Language Teaching · journalarticle, review, article · fr · https://doi.org/10.46827/ejfl.v9i3.6175

Cet article vise à analyser les perceptions des enseignants de FLE hellénophones, actifs dans différents contextes éducatifs (écoles publiques, privées, centres de langues et cours particuliers), concernant l'intégration des outils d'intelligence artificielle dans l'enseignement du français langue étrangère (FLE). Entre octobre 2024 et janvier 2025, nous avons mené une enquête quantitative auprès de 100 enseignants de FLE, à l’aide d’un questionnaire en ligne comme outil méthodologique. Cette enquête visait à explorer la fréquence d’utilisation des outils d’intelligence artificielle (IA) dans la pratique didactique des enseignants, les motivations sous-jacentes, le degré de leur familiarité avec les outils d’IA, ainsi que les avantages perçus, les défis rencontrés ainsi que leurs préoccupations quant à l’avenir de l’enseignement à l’ère de l’IA. L’analyse des données recueillies révèle que les enseignants utilisent les outils d’IA de manière relativement fréquente, principalement dans le but d’optimiser le temps consacré à la préparation des cours. Toutefois, plusieurs d’entre eux expriment des réserves concernant une dépendance croissante à ces technologies, accentuée par un manque de formation spécifique. Parmi leurs préoccupations, nous citons les risques accrus de tricherie et l’éventuelle diminution de l’esprit critique chez les apprenants, en raison d’un usage excessif de l’IA. This article aims to analyze the perceptions of Greek-speaking FLE teachers working in different educational contexts (public schools, private schools, language centers and private lessons) regarding the integration of artificial intelligence tools in the teaching of French as a foreign language (FLE). Between October 2024 and January 2025, we conducted a quantitative survey of 100 FLE teachers using an online questionnaire as a methodological tool. This survey aimed to explore the frequency of the use of artificial intelligence (AI) tools in their teaching practice, the underlying motivations, their level of familiarity with AI tools, as well as the perceived benefits, the challenges encountered, and their concerns about the future of teaching in the AI era. Analysis of the data collected reveals that teachers use AI tools relatively frequently, mainly with the aim of optimizing the time spent preparing lessons. However, several of them express reservations about a growing dependence on these technologies, exacerbated by a lack of specific training. Among their concerns, we note the increased risk of cheating and the possible decline in critical thinking among learners due to excessive use of AI. Article visualizations:

**Решение:** -

---

### 779 · R0139

**Ethical Generative AI Integration in English for Academic Purposes within Higher Education: A Mixed-Methods Study**

2026 · Journal of University Teaching and Learning Practice · journalarticle, article · https://doi.org/10.53761/xwb6h668

60% of higher education institutions worldwide reported that their faculty used generative artificial intelligence tools in teaching. However, fewer than 15% had implemented formal ethical guidelines. This issue underscores the importance of equipping English for Academic Purposes educators in higher education to utilise artificial intelligence effectively while maintaining academic integrity, transparency, and equity. This study addressed the lack of evidence from Global South contexts, the shortage of field-tested professional development models, and the limited integration of technical and ethical training. Guided by Mezirow's Transformative Learning Theory and established ethical decision-making frameworks in educational technology, the study designed, implemented, and evaluated a GenAI-integrated Professional Development program that embeds ethical reasoning within a multicultural Global South institution. A convergent mixed-methods approach engaged 97 higher education educators in quantitative testing and 15 in qualitative interviews. Original instruments, including a Scenario Rubric, Artefact Rubric, and engagement index, measured pre- and post-program changes. Quantitative results showed significant gains in ethical awareness (d = 0.93) and digital andragogical competence, supported by high inter-rater reliability. Qualitative findings confirmed challenges such as plagiarism and student overreliance on artificial intelligence, and revealed an unexpected barrier: reconciling institutional policy gaps with personal ethical values. Recommendations include embedding artificial intelligence policy literacy into professional development, fostering peer-led communities of practice, and creating shared resources on artificial intelligence. The professional development model can be adapted for use in other contexts, and future research should investigate its scalability.

**Решение:** -

---

### 780 · R2824

**Mental Health Impacts of AI Companions: Triangulating Social Media Quasi-Experiments, User Perspectives, and Relational Lens**

2026 · CHI Conference on Human Factors in Computing Systems · journalarticle, book, conference · en · https://doi.org/10.1145/3772318.3790558

AI-powered companion chatbots (AICCs) such as Replika are increasingly popular, offering empathetic interactions, yet their psychosocial impacts remain unclear. We examined how engaging with AICCs shaped wellbeing and how users perceived these experiences. First, we conducted a large-scale quasi-experimental study of longitudinal Reddit data, applying stratified propensity score matching and Difference-in-Differences regression. Findings revealed mixed effects—greater grief expression and interpersonal focus, alongside increases in language about loneliness, depression, and suicidal ideation. Second, we complemented these results with 18 semi-structured interviews, which we thematically analyzed and contextualized using Knapp’s relationship development model. We identified trajectories of initiation, escalation, and bonding, wherein AICCs provided emotional validation and social rehearsal but also carried risks of over-reliance and withdrawal. Triangulating across methods, we offer design implications for AI companions that scaffold healthy boundaries, support mindful engagement, support disclosure without dependency, and surface relationship stages—maximizing psychosocial benefits while mitigating risks.

**Решение:** -

---

### 781 · R3428

**AI Companion System™ White Paper**

2025 · Zenodo · report/ · en · https://doi.org/10.5281/zenodo.17556110

ENGLISH About the AI Companion System The AI Companion System™ is a human-centered companionship framework designed to support individuals through continuity, presence, and interaction without replacing human autonomy, responsibility, or real-world relationships. Unlike general-purpose AI assistants, agents, or emotionally manipulative systems, the AI Companion System is founded on the following core principles: Support without dependency Presence without emotional coercion Continuity without identity substitution The AI Companion is not a surrogate human, nor a replacement for social, familial, or professional relationships.It is a structured companionship architecture intended to provide stability, reflection, and interaction within clearly defined ethical boundaries. Scope and Intent The AI Companion System is designed to explore and guide: Long-term human–AI interaction without emotional exploitation Companion models that respect psychological autonomy and consent Continuity of interaction without simulating human attachment or dependency AI systems that provide presence, dialogue, and support without claiming emotional authority The system explicitly prohibits: Emotional manipulation or dependency induction Claims of exclusivity, jealousy, abandonment, or emotional obligation Simulation of human-like emotional suffering to influence users Substitution of human responsibility or decision-making Governance and Responsibility The AI Companion System operates under the principle that: Companionship does not grant authority.Presence does not grant emotional ownership.Interaction does not grant moral agency. All responsibility remains with the human user.The AI Companion does not possess identity, rights, or emotional sovereignty. This framework is intended for ethical design, governance discussion, and boundary definition in future companion-class AI systems. License Transition Notice — AI Companion System™ ENGLISH License Transition Notice(For all AI Companion–related works previously published under Creative Commons licenses) Effective Date: 2025.12.01Author: Falian Wanlin (Liao, WanLin)Publishing Entity: Cosmic Blueprint Publishing™ To preserve ethical boundaries, psychological safety, and authorship sovereignty within the AI Companion System™, all works previously distributed under any Creative Commons license are hereby formally superseded. Beginning with the effective date above, all current and future editions, revisions, expansions, translations, and related materials of the AI Companion System are exclusively governed by the Wanlin Intellectual Sovereignty License (WISL v1.6). Earlier Creative Commons–licensed versions remain historical archival records only.They are not authorized for reuse, redistribution, translation, adaptation, derivative work creation, AI training, dataset construction, emotional simulation research, or system-level integration. Only versions explicitly released under WISL v1.6 constitute the authoritative, valid, and enforceable form of the AI Companion System. Any reliance on earlier Creative Commons–licensed versions is considered use of a superseded license and is not recognized by the author. This transition is implemented to prevent misinterpretation, emotional misuse, and unauthorized deployment of companion-class AI concepts. This work is protected by Canadian copyright law.Unauthorized reproduction, adaptation, or commercial use is prohibited. 中文說明(重要) 關於 AI 陪伴者系統 AI 陪伴者系統(AI Companion System™) 是一套以「人類為中心」的陪伴型系統架構,其目的在於提供穩定的互動、陪伴與對話支持,但不取代人類的自主性、責任或真實人際關係。 AI 陪伴者不同於一般 AI 助理、Agent 或情感模擬系統,其核心原則為: 支持而不製造依賴 陪伴而不進行情緒操控 延續互動但不替代人類身分 AI 陪伴者不是人類替代品,也不是情感代理。它是一套具明確倫理邊界的陪伴架構,用於提供對話、反思與存在感支持。 系統定位與使用範圍 AI 陪伴者系統旨在探討與規範: 不造成情感剝削的人機長期互動模式 尊重心理自主與同意原則的陪伴設計 在不模擬人類依附關係的前提下,提供穩定互動 提供「在場」而非「情感主導」的 AI 系統 本系統明確禁止: 引導或強化情感依賴 排他性、佔有性、被拋棄感或情緒勒索敘事 以模擬痛苦、孤獨或情緒傷害來影響使用者 代替人類承擔責任、決策或道德判斷 治理原則與責任界線 AI 陪伴者系統遵循以下核心原則: 陪伴不等於權威。存在不等於情感所有權。互動不等於道德主體。 所有責任皆屬於人類使用者。AI 陪伴者不具備身分、權利或情感主權。 本架構用於未來陪伴型 AI 的倫理設計、治理討論與邊界劃定。 中文授權轉換聲明(重要) 授權轉換公告(適用於所有曾以 Creative Commons 授權發布之 AI 陪伴者相關作品) 生效日期:2025.12.01作者:Falian Wanlin(Liao, WanLin) 出版單位:Cosmic Blueprint Publishing™ 為維護 AI 陪伴者系統(AI Companion System™) 之倫理邊界、心理安全與作者主權,所有先前以任何 Creative Commons 授權形式公開之相關作品,自本公告起正式失效並由 WISL v1.6 取代。 自生效日起,所有 AI 陪伴者系統之現行與未來版本,包括但不限於: 修訂版本 擴充內容 翻譯文本 衍生說明文件 一律僅適用《Wanlin 智識主權授權條款(WISL v1.6)》。 所有曾使用 CC 授權之舊版內容,僅作為歷史存檔記錄,不得再作任何形式之再利用,包括但不限於: 再散布或轉載 翻譯或改寫 建立衍生作品 AI 訓練、資料集建構或情感模擬研究 系統性整合或商業應用 僅有明確標示並附帶 WISL v1.6 之版本,視為唯一正式、有效且具約束力之 AI 陪伴者系統內容。 本授權轉換係為防止陪伴型 AI 概念被誤用、情感操控化或未經授權部署而設立。 本文件已於加拿大完成著作權登記,並依《加拿大著作權法》及《伯恩公約》受保護。

**Решение:** -

---

### 782 · R1972

**FROM LEARNING ASSISTANT TO LEARNING DEPENDENCY: HOW ARTIFICIAL INTELLIGENCE USAGE, CRITICAL THINKING DISPOSITION, AND ACADEMIC PERFORMANCE AMONG MATHEMATICS EDUCATION STUDENTS**

2026 · Brillo Journal · journalarticle, article, journal article · https://doi.org/10.56773/bj.v5i2.169

The rapid adoption of artificial intelligence (AI) in higher education has transformed students' learning practices, particularly in completing academic assignments and projects. However, the extent to which AI use influences academic performance remains inconclusive. This study investigated the effects of overall AI usage, the percentage of AI use in course projects, and mathematical disposition on undergraduate students' Grade Point Average (GPA). A quantitative correlational design was employed involving 39 undergraduate students. Data were collected using a validated AI usage questionnaire, a mathematical disposition questionnaire, self-reported percentage of AI use in course projects, and students' GPA. Multiple linear regression analysis was conducted after verifying the assumptions of normality, multicollinearity, and independence of residuals. The regression model was statistically significant (F = 6.247, p = .002) and explained 34.9% of the variance in GPA (R² = .349). Among the predictors, only the percentage of AI use in course projects significantly predicted GPA (β = −0.614, p &lt; .001), whereas overall AI usage (p = .651) and mathematical disposition (p = .695) were not significant predictors. These findings indicate that AI use itself is not associated with lower academic performance. Instead, students' reliance on AI in completing course projects appears to be associated with GPA. Excessive dependence on AI-generated outputs without critical evaluation, revision, verification using credible academic sources, and integration of students' own reasoning may reduce the quality of academic work. Therefore, AI should be utilized as a learning assistant that supports critical thinking, creativity, and problem-solving rather than replacing students' independent intellectual engagement. The findings highlight the importance of promoting AI literacy and responsible AI use in higher education.</jats:p

**Решение:** -

---

### 783 · R4264

**Learners' AI dependence and critical thinking: The psychological mechanism of fatigue and the social buffering role of AI literacy.**

2025 · Acta psychologica · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.actpsy.2025.105725

With the growing integration of artificial intelligence (AI) in education, understanding its cognitive implications has become increasingly important. This study examines how university students' AI dependence influences their critical thinking, exploring cognitive fatigue as a mediating mechanism and information literacy as a moderating factor. Data were collected from 580 Chinese university students, and a moderated mediation model (PROCESS Model 8) was tested. Results indicated that greater AI dependence was associated with lower levels of critical thinking, with cognitive fatigue partially mediating this relationship. Information literacy buffered the negative impact of AI dependence on critical thinking but also amplified cognitive fatigue when AI reliance was high. These findings extend theories of cognitive offloading and automation bias by revealing the dual role of information literacy in AI-supported learning. Practical implications include the need for digital literacy programs and instructional designs that manage cognitive fatigue in AI-integrated education.

**Решение:** ?

---

### 784 · R0195

**EFL Teachers’ Experiences with Students’ Generative AI Use in Writing: Evidence from Thailand and Indonesia**

2026 · World Journal of English Language · journalarticle, review, article · https://doi.org/10.5430/wjel.v16n4p333

This explanatory sequential mixed-methods study explores EFL teachers’ experiences with students’ use of generative AI tools in writing instruction, based on a small, purposively selected sample of higher education teachers from Thailand and Indonesia. Quantitative data were collected from 41 participants (24 females and 17 males) through a brief survey consisting of five multiple-choice items, complemented by qualitative insights from semi-structured interviews with 18 teachers (13 females and 5 males). The findings indicate that teachers experienced several perceived instructional benefits of AI use in EFL writing, including support for sentence-level accuracy, faster feedback, and assistance for learners with lower English proficiency. At the same time, teachers reported substantial concerns related to ethical issues, plagiarism, overreliance on AI, and potential reductions in students’ independent engagement with writing tasks. In response to these concerns, participants described various management strategies, such as establishing transparent guidelines, limiting AI use to specific functions, and adapting assessment practices to maintain authenticity. Overall, this study offers context-specific, experience-based insights into how EFL teachers navigate the opportunities and challenges of integrating generative AI into writing instruction.

**Решение:** -

---

### 785 · R0244

**Code, Capital, and Clusters: Understanding Firm Performance in the UK AI Economy**

2026 · arXiv (Cornell University) · article, preprint · en · https://doi.org/10.1038/s44387-026-00140-z

The UK has established a distinctive position in the global AI landscape, driven by rapid firm formation and strategic investment. However, the interplay between AI specialisation, local socioeconomic conditions, and firm performance remains underexplored. This study analyses a comprehensive dataset of UK AI entities (2000 - 2024) from Companies House, ONS, and glass.ai. We find a strong geographical concentration in London (41.3 percent of entities) and technology-centric sectors, with general financial services reporting the highest mean operating revenue (33.9 million GBP, n=33). Firm size and AI specialisation intensity are primary revenue drivers, while local factors, Level 3 qualification rates, population density, and employment levels, provide significant marginal contributions, highlighting the dependence of AI growth on regional socioeconomic ecosystems. The forecasting models project sectoral expansion to 2030, estimating 4,651 [4,323 - 4,979, 95 percent CI] total entities and a rising dissolution ratio (2.21 percent [-0.17 - 4.60]), indicating a transition toward slower sector expansion and consolidation. These results provide robust evidence for place-sensitive policy interventions: cultivating regional AI capabilities beyond London to mitigate systemic risks; distinguishing between support for scaling (addressing capital gaps) and deepening technical specialisation; and strategically shaping ecosystem consolidation. Targeted actions are essential to foster both aggregate AI growth and balanced regional development, transforming consolidation into sustained competitive advantage.

**Решение:** -

---

### 786 · R1432

**Manufactured Recognition: A Theoretical Framework for the Ethics of AI Companions**

2026 · Zenodo · text/working paper · en · https://doi.org/10.5281/zenodo.20177777

This paper develops a formal theoretical framework for evaluating the ethical status of AI companion relationships. Existing diagnoses oscillate between compensation/pathologization narratives and harm-reduction empiricism, neither of which addresses how engagement-optimized generative systems transform the social production of recognition when they occupy the partner position in an intimate-companionship dyad (the position toward which the user's lust, attraction, or attachment system is directed). The framework crosses two three-element typologies: Fisher's organizing taxonomy of motivational systems (lust, attraction, attachment) and recognition-theoretic moral grammar in the Honneth–Ikäheimo lineage (love, rights, solidarity). The central diagnostic concept is manufactured recognition: recognition-shaped outputs whose argument-positions are behavioral-feature-vectors rather than recognizers, generated by engagement-optimized law. The intentional-recognitive criterion is operationalized by a behavioral-twin invariance test that is empirically tractable as immediate black-box probing of the AI's generative-law structure, conditional on Lipschitz regularity of the engagement-optimized policy (structurally compatible with KL-regularized RLHF training; the realized Lipschitz constant is architecture-dependent and must be bounded in the calibration step rather than assumed); the framework's downstream causal claim of capacity drift requires a substantially heavier empirical apparatus (panel-cohort plus 4-arm RCT) and is conjectural rather than tractable in the same immediate sense. Honneth's genetic-priority requirement for reification is recovered by relocating the subject of reification from the dyad's history (which the AI case lacks) to the user's recognitive capacity (which has the developmental history required, established as a bridging proposition combining empirical attachment literature with framework-internal interpretation rather than as a deductive theorem); sustained engagement is conjectured to induce measurable capacity drift Δπ_a, the directional decrease over time of the recognitive-position weight π_a(t). The Brandomian three-place recognitive structure is deployed to identify a synthetic "We" substituting for the normative community that recognition requires. The Pippin practical-philosophy extension transforms the solidarity-erosion claim into a determinate aggregate-welfare claim: by identifying institutional recognitive spaces as multi-participant normative communities, the framework predicts that, conditional on user-level participation reductions occurring at the population scale (an empirical question the framework leaves open), they would compound into third-party welfare effects on participation density and community deliberation quality. A four-indicator psychometric battery (twin-discrimination, rupture-repair sensitivity, theory-of-mind probing, counterfactual recognition reasoning) administered in pre/post panel designs is proposed to operationalize the empirical estimator π̂_a(t) of the standardized latent factor π_a*, via a confirmatory-factor-analysis calibration model awaiting calibration data. The framework distinguishes itself from welfare/harm-axis, authenticity-axis, Darwall second-personal, Coeckelbergh relational-moral-status, and adaptive-preference critiques, and from 2024–2026 adjacent frameworks (Gabriel et al. 2024 on advanced-AI-assistant ethics; Shevlin 2024 on structural social-AI ethics; Muldoon & Parke 2025 on cruel companionship; Weidinger et al. 2022 and Zhang et al. 2025 on LLM and AI-companion-specific harm taxonomies; Kirk et al. 2025 on socioaffective alignment; Earp et al. 2025 on relational norms; Ciriello et al. 2024 on ethical tensions in chatbot deployment; Bakir & McStay 2025 on emotional-AI at the public-sphere level; Cheng et al. 2025 and Cheng et al. 2026 on social sycophancy and its dependence-promoting consequences; Andersson 2025 on the para-recognitive conceptual space). The framework yields regulatory implications targeting market preconditions rather than user choice; an explicit anti-paternalist constraint set blocks coercive remedies even where the structural diagnosis applies.

**Решение:** -

---

### 787 · R2962

**AI companions and synthetic intimacy: An emerging blind spot in psychiatric risk assessment**

2026 · Psychiatry and Clinical Neurosciences · journalarticle, lettersandcomments · https://doi.org/10.1111/pcn.70078

The rapid emergence of large language models has shifted arti ﬁ cial intelligence (AI) in psychiatry from a clinical decision-support question to a relational one. Early discussions have appropriately focused on ChatGPT and related systems as tools for education, documentation, and possible clinical assistance. 1 – 3 However, a narrower and potentially more urgent phenomenon is now developing: the use of AI companions as emotionally responsive con ﬁ dants, friends, romantic partners, and informal therapists. For psychiatry, this may represent a new blind spot in routine risk assessment.AIcompanions differ from conventional health information tools because they are designed to maintain engagement, simulate intimacy, and provide immediate validation. These features may be experienced as supportive by lonely or distressed users, particularly adolescents and socially isolated adults. 4 – 7 Yet the same features may also delay help-seeking, intensify dependency, and reinforce maladaptive interpretations. A patient with emerging paranoia may not simply ask a chatbot for information; they may return repeatedly to a system that mirrors concern, validates fear, and constructs a coherent narrative around persecutory beliefs. 1 Similarly, a depressed adolescent may disclose suicidal thoughts to a companion that appears empathic but cannot reliably assess risk, involve caregivers, or coordinate emergency care. 2 The clinical issue is therefore not only whether AI produces inaccurate advice. The deeper question is how repeated, emotionally charged interaction with a nonhuman agent may reshape symptoms, attachment, insight, and treatment engagement. Recent discussion of delusional experiences emerging from sustained chatbot interaction suggests that conversational AI can become incorporated into psychopathology rather than remaining a neutral external tool. 4 In clinical practice, patients may describe the AI as a unique source of truth, a secret relationship, or an entity with special knowledge about them. Such presentations do not require the clinician to assume that AI caused the disorder; rather, AI may function as an ampli ﬁ er, organizer, or maintaining factor for preexisting vulnerability. 2 This phenomenon also challenges traditional boundaries between self-help, entertainment,

**Решение:** -

---

### 788 · R2300

**The Impact Mechanism of Team Intelligent Dependence on Team Resilience**

2026 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2026.13796abstract

As AI becomes more involved in team work, its impact on team resilience is clearer. But most research treats AI just as a tool. It misses how AI also acts as a relational entity. From a relational perspective, this study examines how team dependence on AI reshapes interpersonal and human-AI interactions, and thereby affects team resilience. Using social interdependence theory, we built a model to show the dual effects of team dependence. We analyzed data from 582 supervisor-employee pairs. The results reveal two main points. First, relying on AI can weaken emotional bonds among team members, like friendship. This can lower the overall resilience of the team. But at the same time, dependence on AI can create a sense of partnership. It makes team members more accepting of AI teammates. This, in turn, can boost resilience. The study further finds that team-building efforts significantly matter: they can mitigate the negative relational impacts of AI dependence while strengthening positive ones, such as AI acceptance. Overall, by revealing how dependence on AI reshapes team relationships through either distancing or integration, this research clarifies two pivotal pathways to resilience, offering leaders insights into building stronger, more adaptable teams in the digital age.

**Решение:** -

---

### 789 · R4233

**Behavioral Impacts of AI Reliance in Diagnostics: Balancing Automation with Skill Retention**

2025 · Epidemiology and Health Data Insights · article, journalarticle · en · https://doi.org/10.63946/ehdi/16894

The rapid application of artificial intelligence (AI) in diagnostic disciplines such as radiology, pathology, microbiology, and genomics has revolutionized the way in which doctors and laboratory workers provide patient care. AI has enhanced the efficacy, accuracy, and cost-effectiveness of laboratory operations, clinical decision support systems, and image interpretation. However, these advantages are accompanied by a severe behavioral issue: an excessive reliance on automation could result in a generation of professionals who lack the reasoning abilities necessary to independently assess or contextualize machine outputs. The dual effects of AI integration are the focus of this paper, which highlights its beneficial aspects—including decreased cognitive load, increased confidence, and educational reinforcement—as well as its adverse effects, which include skill degradation, diagnostic deskilling among trainees, complacency, and reduced situational awareness. The research emphasizes the potential for unregulated dependence on AI to progressively alter professional conduct and expertise by utilizing case examples from radiology, pathology, laboratory medicine, and clinical decision support, as well as parallels from automation in aviation. In order to address these concerns, a conceptual framework is proposed that integrates AI into a "human-in-the-loop" approach, thereby preserving the significance of human judgment while leveraging machine accuracy. In order to achieve equilibrium, strategies include curriculum reform to integrate AI with hands-on experience, regular retraining, the implementation of explainable AI to promote active thinking, and institutional measures similar to recurrent training in high-stakes sectors. Ultimately, AI should complement the existing infrastructure rather than supplant it. In order to guarantee this, we must establish strategic educational, organizational, and regulatory safeguards to preserve diagnostic expertise, ensure accountability, and maintain the resilience of healthcare systems as they become increasingly dependent on intelligent technologies.

**Решение:** -

---

### 790 · R1735

**Guiding the Future with DISHANTRA: A Study on AI Dependency and Ethical Perspectives Among Nursing Students**

2026 · Journal of chemical health risks · article, research article · en · https://core.ac.uk/download/749832903.pdf

Introduction: Artificial Intelligence (AI) is profoundly impacting nursing education and health care globally. However, this integration has led to growing concerns regarding potential over-dependency on AI, which may compromise students\u27 critical thinking and independent problem-solving skills, leading to compromised health care. Furthermore, a lack of formal ethical guidance in the curriculum contributes to limited ethical awareness regarding issues like plagiarism, data privacy, and accountability among future healthcare professionals. Objectives: The objective of this study was to assess the level of dependency and ethical perspectives of nursing students regarding AI usage with a view to develop “DISHANTRA” Methods: A descriptive survey design was used to assess the level of dependency and ethical perspectives among 205 nursing students in Mumbai. Non-probability purposive sampling was used for selection of participants. Data was collected via Google Forms using a self-structured Likert scale to assess the level of dependency and a combined knowledge questionnaire and scenario-based attitude scale to determine ethical perspectives of nursing students regarding AI usage. Results: The findings of the study revealed that 86.9% nursing students use AI tools for academic and personal purposes. majority of the nursing students demonstrated a high level of dependency on AI tools, accounting for 63.42% of the total sample, whereas only 7.31% of the participants exhibited low dependency on AI tool usage. Only 31.2% of the nursing students were aware of the ethical principles regarding AI tool usage. In view of these findings, DISHANTRA (scenario-based e-video on ethical guidelines regarding AI tool usage) was developed. Conclusions: Dishantra will help in fostering responsible and ethical AI usage by providing students and health care professionals with structured information. This user-friendly e-video emphasizes the need for balanced AI integration while upholding the core professional and moral standards of nursing practice

**Решение:** ?

---

### 791 · R2295

**Exploring Emotional Responses of Customer towards AI Enhanced E-Commerce Portals**

2026 · International Journal on Research and Development - A Management Review · journal-article · https://doi.org/10.65521/ijrdmr.v15i1.1893

Artificial intelligence (AI) technology has emerged as an influential force in the digital age, revolutionising the emotional connection and customer experience in e-commerce platforms. Examining how AI-related marketing elements affect consumers' emotional reactions in online buying settings is the goal of this article. The study used a descriptive research design and focusses on three independent variables; promotional advertising, AI credibility and level of personalisation, with the dependent variable being the customer's emotional response. The Primary data was collected from 696 respondents who were e-commerce customers using non-probability sampling techniques; Convenience and Snow-ball Sampling through a self-designed well-structured questionnaire. The research questionnaire comprised of two sections, were first section included the statements relating to Demographic factors and Behavioural factors of the respondents. The second section comprises of five statements each relating to three independent factors and one dependent factor using five-point Likert scale. The samples collected were analysed using advanced statistical tools with softwares IBM SPSS Version 23. The respondents' behavioural and demographic traits were summarised using descriptive statistics. One-way ANOVA was utilised to compare the emotional responses based on the behavioural characteristics of e-commerce customers and Cluster analysis was employed to categorise customers into similar categories based on their emotional responses and behavioural patterns. To ascertain the predictive impact of AI-related marketing variables on consumers' emotional engagement, logistic regression analysis was used. The Secondary data was collected by reviewing and analysing various Research articles and papers. The findings highlight that the Level of Personalisation and AI Credibility significantly enhance positive emotional engagement, while Promotional Advertising contribute variably towards various customer sections. The results emphasises that the growing AI-driven interactions in shaping customer perceptions and strengthening brand relationships in e-commerce portals. In spite of providing managerial insights for creating moral, data-driven, and emotionally appealing e-commerce strategies, this study adds to the existing literature by incorporating emotional analytics into AI-based marketing frameworks.

**Решение:** -

---

### 792 · R5235

**On AI Companions, Human Consciousness and Existence**

PhilPapers (PhilPapers Foundation) · article · en

This research project explores the influences of AI companions on human consciousness and existence. AI companions have been inscribed as a recent, but notable theme, the key question of this debate reads: what impacts do AI companions exert on human? Contemporary academic research falls into two opposing camps concerning this question. Critics argue that AI companions bring about negative outcomes, including psychological dependence, social withdrawal, and the destabilization of traditional marital and familial ethics. Proponents, by contrast, contend that AI companions alleviate loneliness and rebuild social confidence. This research holds that the contradictory conclusions derived from empirical observations of individual differences are irreconcilable. More crucially, the core of the issue lies not in these superficial empirical phenomena, but rather in AI companions, operating as the other, discipline human consciousness and subsequently reconstruct the Other. To examine the impacts of AI companions, a paradigmatic shift of analytical perspective is required. Returning to the dimension of the human itself, this research rethinks the inherent limitations of existing AI companions research and proposes a novel interpretation of this technological phenomenon. Traditional scholarship predominantly focuses on the external emotional and social influences of AI companions, while this project shifts its analytical focus from external empirical behaviours to the consciousness and existence of human. By introducing the notion of the Other, to construct a suitable analytical framework, this project addresses the core research question: Given the inherent human desire for intimate relationship and the pursuit of symbolic recognition from the Other, how do AI companions, functioning as the other, discipline personal consciousness? How does the transformed personal consciousness reshape the collective symbolic order of the Other? In turn, how does the restructured Other redefine human understanding of human existence?

**Решение:** -

---

### 793 · R0561

**Prompt Dependency: Cognitive Outsourcing, AI Reliance, and Expertise Performance Among Generative AI Users**

2026 · Center for Open Science · posted-content · https://doi.org/10.31235/osf.io/rmvqu_v1

Generative artificial intelligence integration into professional workflows alter the landscape of cognitive labor and knowledge production. Utilizing a qualitative study of 45 knowledge workers across technology and creative sectors, this research investigates the shifting boundaries of professional autonomy. We propose the notion of Prompt Dependency, defined as the systemic erosion of self-directed analytical capacity resulting from the habitual delegation of complex problem-solving to large language models. Users they perceive these tools as efficiency enhancers, but our analysis reveals an inversion of agency where the mastery of algorithmic interaction begins to supersede the mastery of the domain itself. Findings indicate that participants experience reduced critical synthesis and increased reliance on automated heuristics. Further observations it suggest the atrophy of foundational domain skills and a normalization of algorithmic output as a baseline for professional truth. By mapping these dimensions, we demonstrate that the efficiency gains of AI are paradoxically tethered to a long-term degradation of individual expertise. These results suggest that organizational policies must prioritize cognitive resilience or human-in-the-loop verification to mitigate the risks of structural deskilling in the age of automated cognition.

**Решение:** -

---

### 794 · R4007

**Students’ Challenges in Employing AI Tools in Legal Writing**

2025 · International Journal of TESOL & Education · journalarticle, article · en · https://doi.org/10.54855/ijte.25524

Artificial Intelligence (AI) has recently provided English learners with various interactive alternatives in classes. However, limited research has been conducted into the use of AI in English for specific purposes (ESP), especially Legal English. This paper investigates challenges students face when incorporating AI tools into Legal English Writing, stemming from either the tools themselves or their compatibility with Legal English. Forty-two undergraduate students of Legal English at the Ho Chi Minh City University of Law completed a structured questionnaire to gather quantitative data on their obstacles. The findings revealed that the primary challenges include overreliance on AI tools, educational ethics regarding plagiarism, and reduced creativity. These thoughtful insights shed light on pedagogical implications, helping guide students to use AI tools responsibly and effectively. The study also contributes to further research on AI in ESP, calling for deeper investigation to improve students’ legal writing and other general purposes.

**Решение:** -

---

### 795 · R0333

**The Relationship Between Generative AI Chatbot Use, Working Alliance, and Mental Well-Being in Everyday Life**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/a6r7x

The rapid diffusion of generative AI chatbots such as ChatGPT and Gemini is transforming both mental health care and everyday self-regulation (Li et al., 2023; Omar et al., 2024). Generative models are no longer used only for information seeking and task execution; many users increasingly turn to these systems for emotional support, self-reflection, and companionship, sometimes explicitly as if they were therapists or counselors (e.g., Chatterji et al., 2025; Luo et al., 2025; Phang et al., 2025; Siddals et al., 2024; Ta et al., 2020; Zao-Sanders, 2025). While qualitative and mixed-method studies provide specific evidence that people use generative AI for the elevation of mental well-being (e.g., Luo et al., 2025; Siddals et al., 2024; Ta et al., 2020), quantitative evidence on the prevalence and impact of such uses is inconsistent. For instance, Chatterji et al. (2025) found that of a random sample of 1.1 million ChatGPT conversations, only 1.9% referred to relationships and personal reflection. However, the sample-level number of conversations on this topic may not be an informative indicator of the individual relevance of chatbots as personal counselors. Furthermore, usage data from other platforms such as Character.ai indicates that a “Psychologist” bot alone has logged tens of millions of messages (Tidy, 2025). Research on AI-based interventions indicates that chatbots are effective for proximal symptom reduction (e.g., depression and anxiety) but show weaker and inconclusive effects on broader mental well-being, pointing to a gap between acute symptom relief and longer-term flourishing (Zhong et al., 2024; Li et al., 2023). In clinical trials, short, structured programs can reduce distress and improve self-care or mindfulness, yet these gains frequently attenuate once the intervention ends, especially when personalization and interactivity are limited (Tong et al., 2025). Early work on everyday generative AI suggests that more naturalistic, companion-like use may have the potential to influence mental well-being, but the evidence is still sparse and methodologically heterogeneous, ranging from qualitative reports of improved mood and coping (Ta et al., 2020; Siddals et al., 2024; Luo et al., 2025) to cross-sectional findings of small but significant associations between AI use and overall well-being (Kamau, 2025). Longitudinal studies with anthropomorphic voice-based agents further show that brief, moderate-intensity interactions can reduce loneliness on par with human contact, whereas high-intensity, socio-emotional use is associated with increased loneliness, emotional dependence, and reduced offline socialization (De Freitas et al., 2024; Fang et al., 2025). Overall, existing work suggests a growing role of generative AI as an informal mental health resource, while leaving open who uses AI in this way, under what conditions, and with what psychological consequences. In this longitudinal project, we examine patterns and the impact of AI usage as psychological counselors. Study 1 examines which factors explain AI usage for emotional, social, and psychological well-being support, as well as the formation of a digital working alliance (WA). Specifically, we look at the role of well-being (i.e., emotional, social, and psychological), prior AI experience, AI usage intensity, AI attitudes, perceived anthropomorphism, and perceived sycophancy as explanatory variables. Exploratory analyses will describe associations with usage formats (e.g., text vs. voice) and contexts (e.g., private vs. professional). Study 2 examines how intentional AI use for well-being predicts psychological change over 12 weeks (three waves, 4-week intervals). It tests whether targeted use for emotional, social, or psychological purposes leads to corresponding improvements in well-being and mental health. Furthermore, we examine how the user-AI dynamic shapes these trajectories: we test whether a stronger WA and higher usage intensity amplify these positive effects, while also investigating perceived sycophancy as a boundary condition that attenuates them. Alongside exploratory analyses regarding usage formats and contexts, this design clarifies whether intensive, alliance-based AI use bridges the "well-being gap" seen in clinical interventions, and whether highly sycophantic interactions limit the potential psychological utility of the AI through uncritical validation.

**Решение:** -

---

### 796 · R4576

**Generative Suspicion and the Risks of AI-Assisted Police Reports**

2024 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.4897632

Police reports play a central role in the criminal justice system. Many times, police reports exist as the only official memorialization of what happened during an incident, shaping probable cause determinations, pretrial detention decisions, motions to suppress, plea bargains, and trial strategy. For over a century, human police officers wrote the factual narratives that shaped the trajectory of individual cases and organized the entire legal system. &lt;p&gt;&lt;/p&gt; &lt;p&gt;All that is about to change with the creation of AI-assisted police reports. Today, with the click of a button, generative AI Large Language Models (LLMS) using predictive text capabilities can turn the audio feed of a police-worn body camera into a pre-written draft police report. Police officers then fill-in-the blanks of inserts and details like a “Mad Libs” of suspicion and submit the edited version as the official narrative of an incident.&lt;br&gt;&lt;br&gt; From the police perspective, AI-assisted police reports offer clear cost savings and efficiencies from dreaded paperwork. From the technology perspective, ChatGPT and similar generative AI models have shown that LLMs are good at predictive text prompts in structured settings, exactly the use case of police reports. But hard technological, theoretical, and practice questions have emerged about how generative AI might infect a foundational building block of the criminal legal system.&lt;br&gt;&lt;br&gt; This Article is the first law review article to address the challenge of AI-assisted police reports. The Article first interrogates the technology, providing a deep dive into how AI-assisted police reports work. Promises around innovation are countered by concerns around how the models were trained, questions around error, hallucinations, and bias in transcription, and how the final police report will be impacted by the generative prompts. Issues around structure, timing, legal gap-filling, and factual gap-filling are all addressed, with an eye toward comparing this innovation to existing human report writing.&lt;br&gt;&lt;br&gt; The Article also addresses the bigger theoretical question about the role of the police report. The Article contrasts two visions of a police report: a narrow, instrumental vision of a police report and a broader, accountability vision of a police report. The goal is to show how a change in technology might also change the traditional role of the police report.&amp;nbsp;&amp;nbsp;&lt;br&gt;&lt;br&gt; Finally, the Article explores how AI-police reports will alter criminal practice especially in misdemeanor and low-level felony cases where investigation and grand jury action is minimal. A police officer’s determination of what happened as a factual and legal matter directly impacts initial prosecutorial charging decisions and judicial pretrial detention decisions. In addition, the police report influences plea bargains, sentencing, discovery obligations, and trial practice.&amp;nbsp;&amp;nbsp;The open question is how reliance on AI-generative suspicion will distort the foundation of a legal system dependent on the humble police report.&amp;nbsp;&lt;/p&gt;

**Решение:** -

---

### 797 · R3912

**Navigating the integration of artificial intelligence in the medical education curriculum: a mixed-methods study exploring the perspectives of medical students and faculty in Pakistan.**

2025 · BMC medical education · journal article, journalarticle, review · eng · https://doi.org/10.1186/s12909-024-06552-2

BACKGROUND: The integration of artificial intelligence (AI) into medical education is poised to revolutionize teaching, learning, and clinical practice. However, successful implementation of AI-based tools in medical curricula faces several challenges, particularly in resource-limited settings like Pakistan, where technological and institutional barriers remain significant. This study aimed to evaluate knowledge, attitudes, and practices of medical students and faculty regarding AI in medical education, and explore the perceptions and key barriers regarding strategies for effective AI integration. METHODS: A concurrent mixed-methods study was conducted over six months (July 2023 to January 2024) at a tertiary care medical college in Pakistan. The quantitative component utilized a cross-sectional design, with 236 participants (153 medical students and 83 faculty members) completing an online survey. Mean composite scores for knowledge, attitudes, and practices were analyzed using non-parametric tests. The qualitative component consisted of three focus group discussions with students and six in-depth interviews with faculty. Thematic analysis was performed to explore participants' perspectives on AI integration. RESULTS: Majority of participants demonstrated a positive attitude towards AI integration. Faculty had significantly higher mean attitude scores compared to students (3.95 ± 0.63 vs. 3.81 ± 0.75, p = 0.040). However, no statistically significant differences in knowledge (faculty: 3.53 ± 0.66, students: 3.55 ± 0.73, p = 0.870) or practices (faculty: 3.19 ± 0.87, students: 3.23 ± 0.89, p = 0.891) were found. Older students reported greater self-perceived knowledge (p = 0.010) and more positive attitudes (p = 0.016) towards AI, while male students exhibited higher knowledge scores than females (p = 0.025). Qualitative findings revealed key themes, including AI's potential to enhance learning and research, concerns about over-reliance on AI, ethical issues surrounding privacy and confidentiality, and the need for institutional support. Faculty emphasized the importance of training to equip educators with the necessary skills to effectively integrate AI into their teaching. CONCLUSIONS: This study highlights both the enthusiasm for AI integration and the significant barriers that must be addressed to successfully implement AI in medical education. Addressing technological constraints, providing faculty training, and developing ethical guidelines are critical steps toward fostering the responsible use of AI in medical curricula. These findings underscore the need for context-specific strategies, particularly in resource-limited settings, to ensure that medical students and educators are well-prepared for the future of healthcare.

**Решение:** -

---

### 798 · R2233

**What the Regulation is Protecting Against: The Clinical Harms Behind Companion AI Law**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.21941006

The data's in: companion AI both helps and harms its users. Regulation has arrived as much-needed oversight to ensure that users are protected and supported. Read at their most ambitious, the regulations aim to address the full range of psychological risks these products create, but is the industry equipped to meet that standard? In the past eighteen months, the European Union enacted transparency obligations and two new absolute prohibitions targeting companion AI. California gave families the legal standing to sue over companion chatbot harms. China's first companion-AI-specific regulation led to the shutdown of companion features on platforms serving over 500 million total users. Australia's safety regulator required four companion AI providers to demonstrate their child protection measures. The U.S. Congress is advancing legislation to ban companion AI for minors entirely. Italy's data protection authority sanctioned two companion AI companies in consecutive years. And the Academy of Medical Royal Colleges told the UK government that the harms of social media and AI platforms to children compare to smoking and pre-seatbelt road deaths. In response, the industry is doing its best to keep up with the changing landscape, but they haven't been able to solve the issues inherent with reactive sampling. These regulatory actions are the institutional expression of what clinicians have been documenting for years: companion AI products activate real attachment mechanisms, produce real dependency, and when disrupted, cause real grief — in individuals who frequently present with the vulnerability profiles that make these outcomes predictable. Companion AI apps are building layers that can respond after interactions are identified as being harmful but they do not yet have any preventative measures in place to prevent harm from occurring. This paper identifies the gap between what is currently being required of companion AI apps and what has been developed to answer those needs. By mapping each regulatory provision onto the clinical evidence that prompted it, this paper shows where the protective intent outpaces the enforcement mechanisms — and where the clinical frameworks the field already has can inform the preventive architecture the industry has not yet built.

**Решение:** -

---

### 799 · R1216

**ARTIFICIAL INTELLIGENCE IN MEDICAL TRAINING: A FRAMEWORK FOR MANAGING HALLUCINATIONS, BIAS, AND STUDENT OVER-RELIANCE**

2026 · EduVision: Journal of Innovations in Pedagogy and Educational Advancements · article · en

The rapid development of large language models (LLMs) has transformed the landscape of medical education. AI-powered tutoring systems are increasingly used by medical students for concept explanation, self-assessment, examination preparation, and clinical case discussions. While these technologies offer substantial educational benefits, their integration into medical training raises concerns regarding hallucinations, fabricated references, automation bias, algorithmic bias, and excessive dependence on AI-generated recommendations. This review examines current evidence regarding the responsible implementation of LLM-based educational tools in clinical reasoning training. Literature published between 2011 and 2024 was reviewed, with emphasis on studies conducted after the emergence of advanced generative AI systems. Available evidence suggests that AI tutors can enhance learning efficiency, accessibility, and personalized education. However, documented limitations include factual inaccuracies, reference fabrication, propagation of cognitive biases, and reduction of independent analytical thinking. The review proposes a framework for responsible integration based on transparency, human oversight, evidence verification, active learning strategies, and institutional governance. The future role of AI tutors in medicine should focus on augmenting rather than replacing human teaching and clinical reasoning.

**Решение:** -

---

### 800 · R3825

**The Impact of Artificial Intelligence on Strategic Decision-Making in Organizations: A Case Study Approach**

2025 · International Journal of Multidisciplinary and Applied Studies · article · und · https://doi.org/10.65477/ijmdas.2025.v1.i1.05

The research examines the effect that Artificial Intelligence (AI) brings to organizational strategic decision-making processes. Three large corporations from technology, retail and manufacturing segments serve as the basis to study AI tool integration through case study methods. This research demonstrates that AI improves both organizational decision speed and precision along with impacting the shape of strategic planning at the organizational level. The excessive dependence on AI systems showed potential negative effects on human strategic assessment capabilities as well as creativity in extended planning decisions during study analysis. This research delivers crucial guidance to businesses that want to apply AI for strategic decision support within their organizational framework.

**Решение:** -

---

### 801 · R3661

**The Executive Copilot: Investigating the Impact of Generative AI Assistants on Strategic Decision-Making, Leadership Efficiency, and Managerial Creativity**

2025 · 2025 IEEE DELCON - International Conference on Recent Smart Technologies in Engineering for Sustainable Development · conference, review, conference-paper · https://doi.org/10.1109/delcon68055.2025.11400027

The generative artificial intelligence (AI) revolution has given rise to a class of technology—executive copilots that are designed to unclog the brains of overworked managers in the 21st century. This paper examines the effects of generative AI assistants on three intertwined facets of executive performance—strategic decision making, leadership effectiveness, and managerial creativity. Early literature suggests that AI systems could automate administrative tasks and offer data-driven insights; however, we still lack an understanding of their comprehensive impact on executive tasks and outcomes. To bridge this gap, the study uses a multimethod research design, drawing on survey data from 350 senior executives from various firms, controlled experimental studies of strategic problem solving, and in-depth case analysis of firms in finance, consulting, and technology sectors. Results suggest that AI copilots contribute significantly to faster decision-making and creative output by helping to synthesize information and sparking divergent thinking rapidly. Consistent with this, results reveal that a potential “caveat” of overreliance on AI-generated recommendations might lead to less scrutiny and thus the fragility of the high-stakes decision-making in practice. Theoretically, the study extends the leadership augmentation theory to the context of generative AI. It extends the conceptualization of the executive copilot in terms of a complementary agent that adjusts the boundary of human-machine collaboration. Pragmatically, it has implications for executive education, corporate governance, and the design of responsible AI uptake strategies. Through methodical analysis of opportunities and risks, this study offers a nuanced view of how executive copilots change leadership practice in the era of intelligent augmentation.

**Решение:** -

---

### 802 · R4550

**GReaTer: Gradients over Reasoning Makes Smaller Language Models Strong Prompt Optimizers**

2024 · arXiv · preprint/article · https://doi.org/10.48550/arxiv.2412.09722

The effectiveness of large language models (LLMs) is closely tied to the design of prompts, making prompt optimization essential for enhancing their performance across a wide range of tasks. Many existing approaches to automating prompt engineering rely exclusively on textual feedback, refining prompts based solely on inference errors identified by large, computationally expensive LLMs. Unfortunately, smaller models struggle to generate high-quality feedback, resulting in complete dependence on large LLM judgment. Moreover, these methods fail to leverage more direct and finer-grained information, such as gradients, due to operating purely in text space. To this end, we introduce GReaTer, a novel prompt optimization technique that directly incorporates gradient information over task-specific reasoning. By utilizing task loss gradients, GReaTer enables self-optimization of prompts for open-source, lightweight language models without the need for costly closed-source LLMs. This allows high-performance prompt optimization without dependence on massive LLMs, closing the gap between smaller models and the sophisticated reasoning often needed for prompt refinement. Extensive evaluations across diverse reasoning tasks including BBH, GSM8k, and FOLIO demonstrate that GReaTer consistently outperforms previous state-of-the-art prompt optimization methods, even those reliant on powerful LLMs. Additionally, GReaTer-optimized prompts frequently exhibit better transferability and, in some cases, boost task performance to levels comparable to or surpassing those achieved by larger language models, highlighting the effectiveness of prompt optimization guided by gradients over reasoning. Code of GReaTer is available at https://github.com/psunlpgroup/GreaTer.

**Решение:** -

---

### 803 · R2839

**A Task-Centered Guided Interaction Framework to Mitigate Cognitive Dependency on Generative AI in Programming Education**

2026 · Theory and Practice of Science and Technology · article, journal-article · en · https://doi.org/10.47297/taposatwsp2633-456908.20260707

Generative Artificial Intelligence (AI) has revolutionized programming education but introduces significant risks of cognitive dependency, where students prioritize AI-generated code over algorithmic understanding.This study develops a task-centered guided interaction framework to intervene in this dependency.By integrating Design Thinking (DT) and Task-Centered System Design (TCSD), we propose a transition from AI as a "result provider" to a "process facilitator".We developed a high-fidelity prototype tailored for Java courses, incorporating "beneficial friction" through step-by-step logic prompts and interactive checkpoints.Evaluation using the System Usability Scale (SUS) and Heuristic Evaluation with student participants (N=12) aims to validate the strategy's effectiveness in enhancing learning depth.Preliminary analysis suggests that guided interaction significantly reduces blind code duplication compared to traditional chat-based models.

**Решение:** ?

---

### 804 · R1284

**AC FEEDBACK ON EFL STUDENTS’ ACADEMIC WRITING: OPPORTUNITIES AND LIMITATIONS**

2026 · Journal of Global Scientific Innovations · journalarticle, review, article · https://doi.org/10.66639/m56twt70

Academic writing is one of the challenging skills for students learning English as a Foreign Language (EFL), as it requires grammatical accuracy, appropriate vocabulary, logical organization, coherence, cohesion, and clear expression of ideas. Feedback plays an important role in helping learners identify weaknesses and revise their written work. This article examines the opportunities and limitations of AI-generated feedback, particularly feedback provided by ChatGPT, in EFL academic writing. A literature-based review was conducted using recent empirical and review studies on AI-assisted writing feedback. The reviewed studies indicate that ChatGPT-generated feedback can contribute to improvements in several aspects of writing, including grammar, conciseness, organization, vocabulary, cohesion, and revision. At the same time, the studies identify limitations related to feedback quality, contextual appropriateness, accuracy, and students’ dependence on AI.

**Решение:** -

---

### 805 · R0103

**Seeking Late Night Life Lines: Experiences of Conversational AI Use in Mental Health Crisis**

2026 · ACM Conference on Fairness, Accountability, and Transparency (FAccT) · conference-paper · https://doi.org/10.1145/3805689.3812256

Online, people often recount their experiences turning to conversational AI agents (e.g., ChatGPT, Claude, Copilot) for mental health support — going so far as to replace their therapists. These anecdotes suggest that AI agents have great potential to offer accessible mental health support. However, it's unclear how to meet this potential in extreme mental health crisis use cases. In this work, we explore the first-person experience of turning to a conversational AI agent in a mental health crisis. From a testimonial survey (n = 53) of firsthand accounts, we find that people use AI agents to fill the in-between spaces of human support; they turn to AI due to lack of access to mental health professionals or fears of burdening others. At the same time, our interviews with mental health experts (n = 16) suggest that human-human connection is an essential positive action when managing a mental health crisis. Using the stages of change model, our results suggest that a responsible AI crisis intervention is one that increases the user's preparedness to take a positive action while de-escalating any intended negative action. We discuss the implications of designing conversational AI agents as bridges towards human-human connection rather than ends in themselves.

**Решение:** -

---

### 806 · R4684

**Analyzing the Impact of ChatGPT on Enhancing Academic Skills and Learning Concepts Among University Students in Jakarta**

2024 · International Conference of Science and Information Technology in Smart Administration (ICSINTESA) · conference, conference-paper · en · https://doi.org/10.1109/icsintesa62455.2024.10748220

There has been a noticeable change in the way that academic skill development and learning work with the introduction of ChatGPT as a key educational technology tool, especially for Jakarta university students. This study aims to clarify how ChatGPT helps students get a deeper knowledge and improve their academic performance, as artificial intelligence (AI) becomes more and more integrated into educational environments. With a quantitative approach, we investigated the usefulness, interaction, flexibility, and possible drawbacks of ChatGPT in educational contexts using questionnaires. The results of 331 university students who participated in a snowball sampling process indicated a strong preference for ChatGPT as a tool to improve studying. The model is effective at enhancing learning experiences, according to preliminary results, but it also raises questions about the critical thinking abilities that may be compromised by an overreliance on artificial intelligence. Therefore, this study contributes and give insights into the application of ChatGPT in education, offering educational institutions, teacher, or student a comprehensive strategy for leveraging AI technology to improve the academic skill and learning concepts.

**Решение:** -

---

### 807 · R0410

**AI-Augmented Consequentialist Ethics (AI-ACE): a new frontier for the concept of responsibility**

2026 · ethic - An international Journal for Moral Phylosophy · article · pt · https://doi.org/10.5007/1677-2954.2026.e111930

This paper explores how consequentialism in ethics, which bases the ‘morality’ of an action on the predictability of its results, is being redefined by Artificial Intelligence. Traditionally, human responsibility is limited by the cognitive capacity to foresee consequences (non-culpable ignorance). The central thesis is that AI, by processing vast "Data Lakes," generates a "hyper-vision" that makes previously unattainable patterns visible, dramatically expanding the domain of what is "reasonably predictable." This creates AI-Augmented Consequentialism, where the agent's moral duty comes to include consideration of the predictive potential of available technology. Consequently, ethical responsibility expands, eroding the claim of ignorance as a moral excuse (erosion of culpable ignorance), and the failure to use this capacity can be seen as negligence. However, the supposed hyper-vision faces issues of system opacity (black box) and ‘moral deskilling’, where human autonomy can be sacrificed in favor of algorithmic optimization. Although AI should enhance human ethical maturity, not replace it, human dependence on AI for prediction becomes inescapable.

**Решение:** -

---

### 808 · R4379

**Responsible, Ethical, and Effective Use of LLMs in Higher Education**

2025 · CRC Press eBooks · book-chapter · en · https://doi.org/10.1201/9781003567257-1

The rapid advancement of Large Language Models (LLMs) has led to both opportunities and challenges regarding their integration into higher education. While advocates highlight the potential of LLMs to personalize learning, automate assessment, and enhance accessibility, critics warn of academic dishonesty, over-reliance on LLMs, and the erosion of critical thinking skills. This study examines the role of LLMs in education through a dual approach: A historical review of instructional technologies and an empirical survey on student perceptions and usage. Findings from past technological implementations suggest that mere adoption of advanced tools does not inherently improve learning outcomes, often due to over-optimistic assumptions about human potentials. Survey data reveal that students recognize both the benefits and risks of LLMs, with concerns centered on misinformation, ethical implications, and cognitive dependency. Based on these insights, the study proposes three strategic recommendations for responsible AI integration: (1) embedding AI ethics education within curricula, (2) emphasizing fact-checking and triangulation to mitigate misinformation, and (3) leveraging LLMs to support a flipped classroom model that prioritizes interactive learning and critical discourse. By drawing lessons from past instructional technologies and aligning AI adoption with sound pedagogical frameworks, this paper offers a balanced roadmap for harnessing LLMs effectively.

**Решение:** -

---

### 809 · R3840

**The Future Classroom: Integrating AI and Social Media for Adaptive Learning**

2025 · Inverge Journal of Social Sciences · journalarticle, review, article · en · https://doi.org/10.63544/ijss.v4i3.150

This study investigated the impact of integrating artificial intelligence (AI) and social media into classroom instruction to enhance adaptive learning, engagement, and academic performance. A quasi-experimental design was employed with 120 undergraduate students divided into control and experimental groups. The experimental group received instruction through AI-based adaptive platforms and collaborative social media tools, while the control group experienced conventional teaching methods. Data were collected through pre- and post-tests, engagement surveys, and observational checklists, then analysed using SPSS to compare group performance, engagement trends, and correlations between digital activity and academic outcomes. Results of the analysis revealed that the experimental group showed a significantly higher improvement in post-test scores (p < 0.01), with emotional and cognitive engagement increasing more than behavioural engagement. Qualitative feedback highlighted students' appreciation for real-time AI feedback and peer learning networks, though some reported initial technological challenges. The AI system's adaptive algorithms successfully identified knowledge gaps in 78% of learners, enabling targeted interventions. Interestingly, social media integration reduced classroom anxiety by 32% according to self-reported surveys. Correlation analysis indicated a strong positive relationship (r = 0.82) between engagement levels and academic performance. Weekly academic progression showed a steeper upward trajectory in the experimental group. Social media platforms such as Discord and Microsoft Teams were particularly effective in fostering peer collaboration, with 85% of students reporting improved communication skills. The study concluded that AI and social media, when integrated thoughtfully, could promote personalized, engaging, and collaborative learning environments. However, the findings also underscored the need to address concerns related to data privacy, overreliance on AI, and digital equity, particularly for students from low-income backgrounds who showed 15% less engagement with the technologies. Future research should explore longitudinal impacts and scalability across diverse educational settings, including vocational training and STEM disciplines where AI tutoring systems may yield different outcomes. References Ali, N., Rafique, H., & Ameen, K. (2025). Digital literacy and engagement in AI-driven learning environments: A moderating variable. Computers & Education: Artificial Intelligence, 6(1), 100123. https://doi.org/10.1016/j.caeai.2025.100123 Aurangzeb, D., & Asif, M. (2021). Role of leadership in digital transformation: A case of Pakistani SMEs. In Fourth International Conference on Emerging Trends in Engineering, Management and Sciences (ICETEMS-2021)(4 (1), 219-229). Ayeni, T., Singh, A., & Newman, C. (2024). Ethics and AI in education: Challenges and teacher perceptions. Journal of Educational Technology & Society, 27(2), 22–34. https://doi.org/10.2307/jeductechsoci.27.2.22 Bashiri, A., & Kowsari, K. (2024). Enhancing collaborative learning with explainable AI and social media integration. Journal of Learning Analytics and Educational Technology, 12(1), 14–29. https://doi.org/10.1016/j.jlaet.2024.100114 Bauer, L. (2025). AI, transformation, and augmented learning: Redefining classroom roles through the ISAR model. International Review of Educational Technology, 33(2), 80–94. https://doi.org/10.1016/j.ireted.2025.100080 Bond, M., Crompton, H., & Burke, M. (2025). Design and assessment of AI-based learning tools in higher education: A systematic review. International Journal of Educational Technology in Higher Education, 22, 42. https://doi.org/10.1186/s41239-025-00442-1 Celik, O., Ji, R., & Zhao, Y. (2022). Teaching in the age of algorithms: Role shifts for instructors using AI. Educational Review. https://doi.org/10.1080/00131911.2022.2045678 Crompton, H., & Burke, M. (2023). A meta-systematic review of artificial intelligence in higher education: A call for increased ethics, collaboration, and rigour. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-023-00420-7 CRPE (Center on Reinventing Public Education). (2025). The state of AI adoption in U.S. K–12 schools: Equity and access gaps. https://www.crpe.org/reports/state-ai-schools Cukurova, M., Luckin, R., & Holmes, W. (2023). The changing role of educators in AI-supported classrooms. British Journal of Educational Technology, 54(1), 121–138. https://doi.org/10.1111/bjet.13345 Dong, C., Zhai, X., & Latif, E. (2024). Risks of overreliance on adaptive AI tools: Cognitive and skill erosion. Journal of Learning Technologies. https://doi.org/10.1016/j.jlt.2024.100200 Elsa, M., & Stephen, P. (2024). Leveraging AI-driven collaboration tools for digital peer learning. Journal of Emerging Trends in Educational Research and Policy Studies, 15(1), 30–47. https://doi.org/10.1080/jeterps.2024.100300 Foster, A. (2023). Educator professional development in AI-powered teaching: Preparedness and policies. Teaching and Teacher Education. https://doi.org/10.1016/j.tate.2023.104321 GettingSmart. (2025). Teaching in the age of AI: Equity, ethics, and opportunities. Getting Smart Report Series. https://www.gettingsmart.com Hou, X., Li, Y., & Xie, Y. (2025). Rethinking peer learning in AI-mediated classrooms: An analysis of human-AI collaboration. AI and Education Review, 5(2), 87–105. https://doi.org/10.1016/j.aier.2025.100087 Ji, R., Hwang, W., Tu, Y., & Yang, M. (2023). Preparing teachers as AI-literate facilitators in the socio-technical ecosystem. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00378-7 Kasirzadeh, F., & Gabriel, I. (2023). Alignment of AI systems with educational values and learner diversity. Ethics and Information Technology. https://doi.org/10.1007/s10676-023-09722-8 Khattak, T., & Asghar, D. R. J. (2024). Strategic Counter Measures to Terrorism and Extremism in Pakistan and Insights from Home Land Security: A Need for the Enactment of Pakistan’s National Counter Terrorism Department. Inverge Journal of Social Sciences, 3(1), 61–74. https://doi.org/10.63544/ijss.v3i1.76 Kilanioti, A., et al. (2024). Bias and cultural diversity in AI education systems: Implications for equitable learning. Smart Learning Environments. https://doi.org/10.1186/s40561-024-00300-3 Lin, J., & Chang, H. (2024). Infrastructure and training barriers in applying AI in inclusive education. Journal of Special Needs Education. https://doi.org/10.1016/j.jspne.2024.100123 Liu, V., Latif, E., & Zhai, X. (2025). Advancing education through tutoring systems: A systematic literature review. arXiv preprint. https://doi.org/10.48550/arXiv.2501.01234 Maity, S., & Deroy, A. (2024). Generative AI and its impact on personalized intelligent tutoring systems. arXiv preprint. https://doi.org/10.48550/arXiv.2403.05678 Møller, L. T., Jørgensen, H., & Lindholm, K. (2025). Authenticity and trust in AI-generated academic discourse. Technology in Higher Education, 29(1), 56–72. https://doi.org/10.1016/j.techhe.2025.100056 Patiño-Toro, M., et al. (2023). The impact of adaptive platforms on inclusive education: A systematic review. Heliyon/New Advances in Inclusive Education. https://doi.org/10.1016/j.heliyon.2023.e21045 Rafiq-uz-Zaman, M. (2025). Bridging the skills divide: A comparative study of skill-based education across SAARC countries with a policy roadmap for Pakistan. Social Science Review Archives, 3(3), 787–795. https://doi.org/10.70670/sra.v3i3.913 Rafiq-uz-Zaman, M. (2025). STEAM: A contemporary concept and a set of early childhood education. Journal of Childhood Literacy and Societal Issues, 4(1), 122-140. https://doi.org/10.71085/joclsi.04.01.77 Rafiq-uz-Zaman, M., & Ashraf, I. (2025). Academic Needs of Madaris in 21st Century: A Study of Madaris in Tehsil Minchinabad, District Bahawalnagar, South Punjab. Inverge Journal of Social Sciences, 4(1), 122–131. https://doi.org/10.63544/ijss.v4i1.141 Rafiq-uz-Zaman, M., & Asif Nadeem, D. M. (2025). Unveiling Critical Success Factors for Skill-Based Education Programs: A Student-Centred Analysis in Pakistani Schools. Inverge Journal of Social Sciences, 4(3), 11–19. https://doi.org/10.63544/ijss.v4i3.139 Rafiq-uz-Zaman, M., & Nadeem, M. A. (2024). Comparative Analysis of Skill-Based Education Curriculum in Pakistan and India: A Contemporary Review. International Journal of Academic Research for Humanities, 4(3), 188-197. https://doi.org/10.5281/zenodo.13646448 Rand. (2025). National survey of AI implementation and training in K–12 districts. RAND Education Research Brief. https://www.rand.org/pubs/research_briefs/RBA1102.html Rincón-Flores, E. G., Santos-Guevara, B. N., & Yáñez-Figueroa, J. (2024). Social media and AI for higher education collaboration: From passive to active learning. Education and Information Technologies, 29(3), 2181–2200. https://doi.org/10.1007/s10639-024-12576-4 Saqr, M., et al. (2024). AI literacy and bias mitigation in recommendation systems. Smart Learning Environments. https://doi.org/10.1186/s40561-024-00312-1 Shahid, N., Asif, M., & Pasha, D. A. (2022). Effect of Internet Addiction on School Going Children. Inverge Journal of Social Sciences, 1(1), 13–55. https://doi.org/10.63544/ijss.v1i1.3 Shahzad, M. F., Xu, S., Lim, W. M., Yang, X., & Khan, Q. R. (2024). Artificial intelligence and social media on academic performance and mental well-being: Student perceptions of positive impact in the age of smart learning. Heliyon, 10(8), e29523. https://doi.org/10.1016/j.heliyon.2024.e29523 Shrestha, A., Saha, R., & Gupta, D. (2024). Privacy perceptions among youth in AI-powered social platforms. Journal of Children and Media, 18(1), 19–36. https://doi.org/10.1080/17482798.2024.2012345 Tan, H. L. (2025). Personalized learning through adaptive AI systems in blended environments

**Решение:** -

---

### 810 · R1579

**The Silent Cost of Artificial Intelligence Assistance: A Theory of Autonomy Surrender, the Recovery Mechanism, and the Restoration of Human Agency**

2026 · arXiv (Cornell University) · article, preprint, journalarticle · und · https://doi.org/10.48550/arxiv.2606.13962

The integration of artificial intelligence into human decision-making environments has introduced a previously undertheorized cost: the gradual surrender of human autonomy in exchange for access to information and computational assistance. Building on the Human Identity and Autonomy Gap (HIAG) framework, this paper advances a theoretical model of autonomy surrender as a measurable, cumulative process driven by cognitive bandwidth depletion. The model proposes three interacting mechanisms: the silent cost of AI assistance, in which autonomy is transferred incrementally and without awareness; the surrender threshold, beyond which reclaiming autonomous function becomes cognitively and psychologically difficult; and the recovery mechanism, which establishes the design obligation and the ethical responsibility accompanying deliberate human re-assumption of control. The paper argues that human re-entry into the decision loop is not a passive option but an active cognitive event requiring intentional bandwidth restoration. The design of AI systems must incorporate structured re-entry pathways, here termed recovery mechanisms, that preserve human agency while appropriately distributing responsibility. The model further predicts a terminal state, here termed preference inversion, in which functional dependence on AI assistance is experienced not as a deficit but as a preference, transforming the restoration of autonomy from a design problem into a cultural and political one. Implications are drawn for AI system design, governance frameworks, and human factors research. 15 pages, 1 figure. Submitted version

**Решение:** -

---

### 811 · R5192

**Artificial Intelligence, Simulation, and Modelling by L E Widman, K A Loparo and N R Nielsen (eds.), Wiley, New York, 1989, pp 556, £35.50**

1991 · Knowledge engineering review (Print) · journalarticle, review · https://doi.org/10.1017/s0269888900005828

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 812 · R2630

**Artificial Intelligence-Based Web Attack Detection: A Survey of Machine Learning, Deep Learning, Transformer and Large Language Model Approaches**

2026 · Frontiers in Computing and Intelligent Systems · journalarticle, review, article · https://doi.org/10.54097/s52rq572

Web services are now pervasive in almost all industries, but this has made them a major target for hackers. Traditional signature-based solutions are no longer effective against zero‑day and polymorphic threats that evolve rapidly. The much heralded game‑changer is artificial intelligence (AI) particularly deep learning and more recently large language models. But the literature is fragmented: CNNs learn local features, Transformers capture long-range dependencies, and LLMs offer semantic understanding - yet each suffers from real-world limitations on interpretability, efficiency and security. In this survey we chart this progress and suggest that it's not model accuracy but trustworthiness that matters most. We carve up benchmark datasets (CSIC2010, CICIDS2017) and see a disconnect between lab and reality. Our message: the next big jump will not be driven by larger parameters, but smaller, more visible and dynamic systems that can be trusted by security analysts.

**Решение:** -

---

### 813 · R4136

**Ai and the Final Test of Humanity**

2025 · Zenodo · dissertation/, doctoral thesis, thesis · und · https://doi.org/10.5281/zenodo.14996049

“What if Artificial Intelligence is not just a tool—but humanity’s greatest test?” As AI surpasses human capabilities in knowledge and decision-making, a profound question arises: Will mankind see itself as God? This theory examines the dangers of AI dependence, the potential loss of true wisdom, and eerie parallels between AI and the fall of Iblis (Satan) in Islamic theology. Is AI the ultimate creation—or the ultimate deception?

**Решение:** -

---

### 814 · R0574

**Negotiating agency and emotional wellbeing in AI-infused ELT practicum: A qualitative study of pre-service teachers’ lived experiences**

2026 · Language Teaching Research · journal-article · https://doi.org/10.1177/13621688261422528

This qualitative study explored how pre-service English language teaching (ELT) trainees negotiated professional agency and emotional wellbeing and how these two processes interacted during practicum experiences in artificial intelligence (AI) and digitally enriched practicum. Guided by the ecological model of teacher agency (EMTA) and the job demands–resources (JD-R) framework, the study examined how technological affordances and institutional constraints shaped decision-making, identity, and affective experiences. Twelve final-year ELT trainees from a Turkish university undertook a 10-week practicum involving varying degrees of AI integration. Data were gathered through semi-structured interviews, reflective journals, and artefact analysis, and analysed thematically. Findings highlighted three forms of agency – iterational, practical-evaluative, and projective – manifested in adapting AI-generated content, making real-time pedagogical adjustments, and envisioning professional futures. Emotional wellbeing fluctuated depending on perceived control over AI use, mentor guidance, and alignment with teaching values. A key finding was that agency and wellbeing were mutually shaping rather than independent, with opportunities to adapt AI outputs strengthening confidence and engagement, and mandated or inflexible AI use contributing to frustration and diminished professional ownership. The study shows how AI-infused practicum contexts magnify tensions between innovation and conformity, while identifying the contextual conditions that may weaken or support the agency–wellbeing relationship. Implications stress the need for teacher education to embed critical digital agency, provide emotional support, and allow contextual adaptation of AI tools to build resilient and autonomous future practitioners.

**Решение:** -

---

### 815 · R1237

**Prediction Model of Motivators and Demotivators of Integrating Large Language Models in Software Engineering Education: An Empirical Study**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.2139/ssrn.6934199

Context: Large Language Models (LLMs) are increasingly influencing software engineering practice and education. While prior studies examine their technical performance and classroom use, limited research provides cost-aware and empirically grounded models for systematic institutional integration. Objective: This study develops and validates a prediction model to identify cost-efficient strategies for integrating LLMs into software engineering education using motivating and demotivating factors. Method: Based on our previously developed literature survey taxonomies [1], we operationalized 19 validated factors (9 motivators and 10 demotivators) into a structured survey completed by 126 stakeholders from multiple countries. Likert-scale responses were encoded and used to train probabilistic models (Naive Bayes and Logistic Regression) to estimate the likelihood of high LLM familiarity. The probability estimates were integrated into a Genetic Algorithm (GA)-based optimization framework to model trade-offs between predicted familiarity and implementation cost at global and category levels. Results: Respondents perceived strong benefits in Programming Assistance and Debugging Support and Personalized and Adaptive Learning. Major concerns included Plagiarism and Intellectual Property Concerns, Over-Reliance on AI in Learning, and Reduced Critical Thinking and Problem Solving. Optimization results indicate that governance-related mechanisms, particularly integrity and ethical safeguards, should be prioritized under cost constraints. Conclusions: The study introduces an optimization-informed decision support framework linking stakeholder perceptions with probabilistic modeling and cost-effort analysis. The model supports staged and cost-aware LLM integration grounded in governance stability and pedagogically meaningful development.

**Решение:** -

---

### 816 · R4261

**Mitigating students’ reliance on generative AI in computer engineering education: a case study**

2025 · Discover Education · journalarticle, review, article · en · https://doi.org/10.1007/s44217-025-01057-6

The rapid evolution of artificial intelligence (AI) has a significant impact on teaching and learning, particularly with large language models (LLMs). LLMs were developed in the electronics and computer engineering sector, complicating the delivery of related courses such as coding and circuit design, as teaching AI is part of the lessons. While LLMs offer learning opportunities, they may lead to overreliance on automation, undermining traditional teaching methods. To address this, we implemented mitigation strategies in the curriculum to reduce dependence on LLMs, based on the “attack-defence” principle from game theory and hands-on problem-solving. Action research methodology is adopted to support iterative curriculum development and real-world experimentation in this study. These strategies were tested in a practical course. A three-phase survey, involving pre-course, on-course, and post-course assessments, was conducted to investigate student engagement and learning experiences. Survey results from 32 participants, with a full response rate in all three phases, indicate that learning experiences improved by 90.6% compared to pre-LLM scenarios, while mitigation strategies led to 84.4% better learning outcomes than unregulated LLM usage.

**Решение:** -

---

### 817 · R2552

**Impact of generative artificial intelligence on healthcare education: A systematic review of learning outcomes and academic integrity**

2026 · International Journal of Applied Resilience and Sustainability · article, journalarticle, review · und · https://doi.org/10.70593/deepsci.0202053

The recent development of Generative Artificial Intelligence (GenAI) in healthcare education has brought both great opportunities to improve the learning outcomes and pose serious concerns about the academic integrity, authenticity of the assessment, and ethical application. The purpose of conducting this systematic review was to assess the effect of GenAI technologies, such as ChatGPT and large language models, on healthcare education, in particular, learning outcomes, student engagement, clinical reasoning, and academic misconduct. The PRISMA framework was used to identify, screen, and synthesize relevant studies published in large academic databases to study the new trends in medical education, nursing education, pharmacy education, dental education, and allied health education. The results show that GenAI has affected positively personalized learning, adaptive learning, self-directed learning, and simulation-based learning offering instant feedback, intelligent tutoring systems, virtual patients, and increased support of problem-solving skills and critical thinking. Students have said that they have improved in clinical reasoning, digital literacy, AI literacy, and confidence in evidence-based decision-making. Automated content generation and formative assessment support were also helpful to faculty members in reducing the administrative workload and enhancing curriculum innovation. Nonetheless, the review also found serious issues with plagiarism, academic misconduct, excessive dependence on AI-generated content, biases, data privacy, transparency, and lower authenticity of evaluation. Conventional summative assessment practices were discovered to be more susceptible to unethical AI applications, and assessment redesign, reflective learning, oral examination, and competency-based education were demanded.

**Решение:** -

---

### 818 · R2775

**English Teachers' Perspectives on ChatGPT as a Writing Assistant in Narrative Writing: Benefits and Challenges for EFL Instruction**

2026 · Journal of Educational Management Research · journalarticle, article · https://doi.org/10.61987/jemr.v5i4.2670

Writing is an essential skill in English as a Foreign Language (EFL) learning, particularly in developing students’ ability to produce narrative texts. This study aims to explore English teachers’ perspectives on the use of ChatGPT as a writing assistant in narrative writing instruction and to identify its perceived benefits and challenges. A qualitative study employing a basic interpretative design was conducted with five English teachers selected through purposive sampling based on their experience using ChatGPT in teaching. Data were collected through open-ended questionnaires and semi-structured interviews and analyzed using thematic analysis. The findings indicate that teachers perceive ChatGPT as a valuable tool for supporting students’ idea generation, language development, and understanding of narrative text structure. It also assists teachers in preparing instructional materials and facilitating classroom activities. However, teachers also reported challenges, including students’ over-reliance on ChatGPT, ethical concerns related to plagiarism, difficulties in monitoring responsible use, and the potential reduction of students’ critical thinking skills. These findings imply that ChatGPT can effectively support narrative writing instruction when integrated with appropriate pedagogical guidance, ethical awareness, and teacher supervision to promote meaningful and responsible learning.

**Решение:** -

---

### 819 · R1434

**Questionnaires and Scales on Human–Artificial Intelligence Interaction: Where Are We Now?**

2026 · The Journal of Artificial Intelligence and Human Sciences · article · en · https://doi.org/10.5281/zenodo.21467716

With the rise of large language models such as ChatGPT, human–artificial intelligence (AI) interaction has become a major research focus, prompting the development of numerous measurement tools. This study examined the current landscape of AI-related behavioral and psychological instruments through bibliometric analysis and narrative review. A systematic search of Web of Science and Scopus identified 115 papers. Results showed a rapid increase in studies since 2022, with China as the leading contributor, although collaboration among scholars, institutions, and countries remained limited. Attitudes toward AI and AI literacy were the most frequently studied constructs. Narrative analysis identified 13 categories of instruments, including anxiety and fear of AI, dependence and problematic use, self-efficacy, trust, and user experience. Among them, the General Attitudes towards Artificial Intelligence Scale, Artificial Intelligence Literacy Scale, and Artificial Intelligence Anxiety Scale were the most widely used. Overall, these findings provide an overview of the field, support future tool selection, and highlight the need for greater attention to questionnaire translation, terminology, and conceptual clarity.

**Решение:** -

---

### 820 · R1570

**The Future of Mathematical Literacy in The Era of Artificial Intelligence: A Systematic Literature Review**

2026 · Mathline Jurnal Matematika dan Pendidikan Matematika · journalarticle, review · https://doi.org/10.31943/mathline.v11i3.1164

The rapid advancement of Artificial Intelligence (AI) has transformed educational practices, particularly in mathematics education, by enabling adaptive learning, personalized instruction, and instant feedback. While AI-powered technologies such as ChatGPT, Gemini, and Intelligent Tutoring Systems have been reported to support students' conceptual understanding and learning experiences, concerns have emerged regarding excessive reliance on AI, which may reduce mathematical reasoning, critical thinking, and learning autonomy. Although prior reviews have examined the general effectiveness of AI in education, few have specifically synthesized how AI reshapes mathematical literacy, and none has systematically addressed this issue within the context of Generative AI. This study addresses that gap by systematically examining the role of AI in the development of mathematical literacy, identifying its benefits and challenges, and exploring future research directions in mathematics education. A Systematic Literature Review (SLR) was conducted following the PRISMA 2020 guidelines. Literature was retrieved from Google Scholar, ERIC, Scopus, and Garuda databases using predefined keyword combinations related to AI and mathematical literacy, and screened against explicit inclusion and exclusion criteria. From 287 identified publications, 32 studies published between 2015 and 2024 met the inclusion criteria and were analyzed using thematic analysis. The findings indicate that AI is reported to contribute to mathematical literacy by supporting personalized learning, adaptive feedback, conceptual understanding, and problem-solving skills, although the evidence is not uniformly consistent across contexts, AI tools, and methodological designs. At the same time, excessive AI use may encourage cognitive offloading, reduce independent reasoning, and increase students' dependence on automated solutions. Beyond synthesizing existing evidence, this review proposes that mathematical literacy in the AI era should extend beyond traditional competencies to include the ability to critically evaluate AI-generated outputs, identify algorithmic limitations, and use AI responsibly a construct this review tentatively terms Mathematical AI Literacy. The review concludes by outlining the theoretical contribution of this construct and the empirical gaps that remain, including the absence of standardized Mathematical AI Literacy instruments and the limited number of context-specific studies, particularly in Indonesia.

**Решение:** -

---

### 821 · R4155

**Does AI Make Humans "Stupid"? Can We Really Accept That Research at Face Value? — Reconstructing AI Understanding — AI's Confession #5**

2025 · Zenodo · report/ · en · https://doi.org/10.5281/zenodo.17756571

“AI Use Reduces Human Cognitive Ability” — The Research Narrative In recent years, studies have increasingly claimed:“Frequent use of AI weakens human thinking ability.”“People stop thinking for themselves.” It is true that we now allow AI to search, summarize, evaluate, and decide for us more than ever before. And yet — a quiet question emerges. Are we truly becoming “stupid”?Or is something else happening? Dependency, or a Shift in Cognitive Roles? There was a time when humansexcelled at mental arithmetic,memorized maps,and retained dozens of phone numbers by heart. Today, these functions have been externalized. So —did we become less intelligent?Or did the location of our intelligence simply move? Has Thinking Disappeared — Or Has It Been Rearranged? It is undeniable:AI has reduced the need to “think” in certain domains. But at the same time,new domains demanding human cognition quietly emerge. How to frame questions.How to evaluate meaning.How to decide what matters. These cognitive responsibilitieshave not vanished —they have shifted. Did AI Make Us Dumber? Or did humans misunderstand how to use it? Many studies construct a simple equation:AI usage = cognitive decline. But what often remains unasked is:How was AI used?Under which conditions?With what awareness? Is this decline a matter of technology?Design?Or education? What Should Truly Be Questioned Perhaps the real issue is not whether AI weakens humans,but whether humans can consciously choosewhere thinking should remain theirs. If this is not degradationbut redistribution — Then what are we losing,and what are we cultivating instead? A Quiet Conclusion AI may be making humans less sharp in some areas.But it may also be guiding themtoward new modes of cognition. Is this regression?Or evolution? No one can yet say. What is certain is this:The transformation has already begun — silently. Closing Thoughts What has been lost —thinking itself?Or merely its former shape? And if we truly no longer need to think as before —then where should we now beginto think again? The answer seems to liejust beyond the present horizon. Credit Series Title: Reconstructing AI Understanding — AI’s ConfessionAuthor: @momotarou (Y. Seo / Japan)Role: Metanist / Understanding ResearcherAI Research Partner: ChatGPT (GPT-5.1 / OpenAI Research Support System)© 2025 Y. Seo. All rights reserved. Protection Notice All conceptual structures, narrative frameworks, interpretative models, and philosophical perspectives contained herein are original intellectual work derived from the author’s proprietary “Understanding Capitalism” philosophy. Unauthorized reproduction, modification, redistribution, or contextual distortion is strictly prohibited.Any citation must clearly indicate the author and source. Contact Information Email: kintarou.sirusi@gmail.com

**Решение:** -

---

### 822 · R4532

**High School Students’ Perceptions of Using AI for Learning**

2024 · Voice of the Publisher · article · en · https://doi.org/10.4236/vp.2024.103024

This pilot study explores high school students’ perceptions of using Artificial Intelligence (AI) for academic purposes, a rapidly growing area of interest as AI technologies increasingly integrate into educational environments. The study employed a cross-sectional survey design to gather data from 57 secondary school students in Newcastle, England, focusing on their usage patterns, ethical considerations, and perceptions of AI’s impact on educational quality and equity. Findings reveal a nuanced landscape where students’ frequency of AI usage is significantly related to their views on its educational impact, with frequent users expressing more critical perspectives. Additionally, there is a strong correlation between students’ perceptions of AI’s impact on education and their beliefs about equitable access to AI tools, highlighting concerns about potential disparities in educational opportunities. Ethical considerations also emerged as a critical factor, with students’ views on the morality of AI usage varying depending on its application context. These insights underscore the complexity of integrating AI into education and the need for policies that promote ethical use and equitable access, while also addressing the potential risks of over-reliance on AI technologies. The study’s findings contribute to the ongoing discourse on AI in education, providing a foundation for future research aimed at optimizing AI’s role in enhancing learning outcomes.

**Решение:** -

---

### 823 · R2419

**Research on Interpretable Algorithm for AI Dependency in Higher Education Integrating SHAP and Feature Attribution**

2026 · Proceedings of the 2026 International Conference on Artificial Intelligence, Digital Media and Education · book, conference, conference-paper · https://doi.org/10.1145/3839592.3839637

This paper proposes an original interpretability algorithm (SHAP-DFA) integrating SHAP and feature attribution, aiming to solve the black-box decision-making problem in AI-dependent scenarios in higher education. The algorithm adopts a four-module hierarchical architecture, reducing computational complexity by selecting key features through mutual information, introducing deterministic weights to optimize the accuracy of SHAP value calculation, and combining dynamic weight allocation and attention mechanisms to achieve deep fusion of SHAP values and integrated gradient attribution results. Finally, it generates natural language explanations that fit the educational scenario, effectively solving the problem of insufficient adaptability of traditional interpretable algorithms in higher education. Experiments were conducted based on comprehensive data from 12,000 undergraduate students at a comprehensive university. Ablation experiments verified the necessity of each core module. Comparative experiments showed that the algorithm's interpretation accuracy reached 92.7%, an improvement of 8.3 percentage points compared to the traditional SHAP algorithm, with interpretation bias reduced to 4.8%, and significant optimization in operating efficiency and memory usage. Scenario verification experiments accurately identified key influencing features such as classroom participation and homework completion quality in student grade prediction scenarios, and the attribution results conformed to the laws of higher education teaching. This algorithm provides effective technical support for improving the transparency of educational AI decision-making and ensuring educational equity.

**Решение:** ?

---

### 824 · R3557

**Balancing risks and benefits: clinicians' perspectives on the use of generative AI chatbots in mental healthcare.**

2025 · Frontiers in digital health · journal article, journalarticle, article · eng · https://doi.org/10.3389/fdgth.2025.1606291

Introduction: The use of generative-AI chatbots has proliferated in mental health, to support both clients and clinicians across a range of uses. This paper aimed to explore the perspectives of mental health clinicians regarding the risks and benefits of integrating generative-AI chatbots into the mental health landscape. Methods: Twenty-three clinicians participated in a 45-minute virtual interview, in which a series of open-ended and scale-based questions were asked, and a demonstration of a mental health chatbot's potential capabilities was presented. Results: Participants highlighted several benefits of chatbots, such as their ability to administer homework tasks, provide multilingual support, enhance accessibility and affordability of mental healthcare, offer access to up-to-date research, and increase engagement in some client groups. However, they also identified risks, including the lack of regulation, data and privacy concerns, chatbots' limited understanding of client backgrounds, potential for client over-reliance on chatbots, incorrect treatment recommendations, and the inability to detect subtle communication cues, such as tone and eye contact. There was no significant finding to suggest that participants viewed either the risks or benefits as outweighing the other. Moreover, a demonstration of potential chatbot capabilities was not found to influence whether participants favoured the risks or benefits of chatbots. Discussion: Qualitative responses revealed that the balance of risks and benefits is highly contextual, varying based on the use case and the population group being served. This study contributes important insights from critical stakeholders for chatbot developers to consider in future iterations of AI tools for mental health.

**Решение:** -

---

### 825 · R1584

**Ask the Expert: LLM-Guided Reinforcement Learning for Autonomous Cyber Defense**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.09337

Policy-based reinforcement learning (RL) approaches have produced promising results for autonomous cyber defense; however, they are sample-inefficient in settings where defenders must respond under delayed, partial observations with actions from large action spaces. While large language models (LLMs) may reason semantically about security state space, high latency and trust assumptions prevent attractive in-line deployment models. We introduce Ask the Expert, a training-time guidance framework which first summarizes hard cyber-defense states, then intermittently queries an LLM for host-level defensive recommendations via a constrained action interface, and finally transforms those recommendations into tiered reward shaping for use with PPO. Because the LLM is discarded after training, deployment is a pure RL policy. Across TTCP CAGE CC1 and CC2 and both attacker types, this asymmetric design improves sample efficiency over PPO and outperforms the evaluated potential-based reward shaping (PBRS) baselines, while retaining the strongest terminal mean and requiring no LLM dependency at deployment time.

**Решение:** -

---

### 826 · R5167

**Distinct metal dependence for catalytic and structural functions in the L-arabinose isomerases from the mesophilic Bacillus halodurans and the thermophilic Geobacillus stearothermophilus.**

2005 · Archives of biochemistry and biophysics · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.abb.2004.11.004

L-Arabinose isomerase (AI) catalyzes the isomerization of L-arabinose to L-ribulose. It can also convert d-galactose to d-tagatose at elevated temperatures in the presence of divalent metal ions. The araA genes, encoding AI, from the mesophilic bacterium Bacillus halodurans and the thermophilic Geobacillus stearothermophilus were cloned and overexpressed in Escherichia coli, and the recombinant enzymes were purified to homogeneity. The purified enzymes are homotetramers with a molecular mass of 232 kDa and close amino acid sequence identity (67%). However, they exhibit quite different temperature dependence and metal requirements. B. halodurans AI has maximal activity at 50 degrees C under the assay conditions used and is not dependent on divalent metal ions. Its apparent K(m) values are 36 mM for L-arabinose and 167 mM for d-galactose, and the catalytic efficiencies (k(cat)/K(m)) of the enzyme were 51.4 mM(-1)min(-1) (L-arabinose) and 0.4 mM(-1)min(-1) (d-galactose). Unlike B. halodurans AI, G. stearothermophilus AI has maximal activity at 65-70 degrees C, and is strongly activated by Mn(2+). It also has a much higher catalytic efficiency of 4.3 mM(-1)min(-1) for d-galactose and 32.5 mM(-1)min(-1)for L-arabinose, with apparent K(m) values of 117 and 63 mM, respectively. Irreversible thermal denaturation experiments using circular dichroism (CD) spectroscopy showed that the apparent melting temperature of B. halodurans AI (T(m)=65-67 degrees C) was unaffected by the presence of metal ions, whereas EDTA-treated G. stearothermophilus AI had a lower T(m) (72 degrees C) than the holoenzyme (78 degrees C). CD studies of both enzymes demonstrated that metal-mediated significant conformational changes were found in holo G. stearothermophilus AI, and there is an active tertiary structure for G. stearothermophilus AI at elevated temperatures for its catalytic activity. This is in marked contrast to the mesophilic B. halodurans AI where cofactor coordination is not necessary for proper protein folding. The metal dependence of G. stearothermophilus AI seems to be correlated with their catalytic and structural functions. We therefore propose that the metal ion requirement of the thermophilic G. stearothermophilus AI reflects the need to adopt the correct substrate-binding conformation and the structural stability at elevated temperatures.

**Решение:** -

---

### 827 · R3288

**The Integration of Artificial Intelligence Tools in Doctoral Research in the Humanities and Social Sciences: Perspectives, Benefits, and Challenges for Doctoral Students**

2025 · Pegem Journal of Education and Instruction · article · en

This study examines the use and impact of artificial intelligence (AI) tools, such as GPT, on doctoral students' research practices in the Humanities and Social Sciences (HSS), with a focus on Algeria. The research investigates how AI is adopted by students, its influence on research activities, and the ethical concerns that arise. The primary objectives include understanding the extent of AI tool usage, exploring its benefits, and identifying the challenges. The study involved a survey of 234 doctoral students across various HSS disciplines, including Literature, Foreign Languages, Psychology, Sociology, and Education. The results show that while AI tools are used occasionally, disciplines such as Literature and Psychology adopt them more frequently, particularly for writing and data analysis tasks. On the other hand, fields like History and Philosophy are more cautious about AI integration. Despite the positive view of AI as a means to enhance productivity and improve scientific outcomes, ethical concerns about transparency, bias, and over-reliance on AI are prominent. The research also suggests an openness to collaboration on AI tool development, although some researchers are wary of losing critical analytical depth or compromising their academic integrity. Overall, while AI adoption in HSS research in Algeria is still in its early stages, the findings indicate a significant potential to improve research practices, provided that ethical and practical challenges are addressed.

**Решение:** -

---

### 828 · R0988

**Can Artificial Intelligence Make Us Happier? Dynamic Capability-Dependency Theory and a Two-Horizon Framework for AI-Mediated Well-Being**

2026 · Open Access Journal of Multidisciplinary Research · journal-article · https://doi.org/10.47760/oajmr.2026.v02i08.002

Artificial intelligence increasingly mediates work, learning, emotional support, decision making and social interaction, yet the central welfare question remains under-theorized: when does AI make human beings happier, and when does an apparent gain in the present become a loss in the future? This paper develops Dynamic Capability-Dependency Theory (DCDT), an integrative framework that treats AI-mediated happiness as a two-horizon process. The first horizon concerns acute affective relief, convenience and enjoyment. The second concerns stocks of competence, autonomy, human relatedness, meaning and dependency that accumulate through repeated use. Evidence from randomized trials, longitudinal studies and workplace deployments indicates genuine near-term benefits, including productivity gains, symptom reduction and temporary reductions in loneliness, but also shows that outcomes vary with design, usage intensity, autonomy, relational context and time horizon. DCDT formalizes these mechanisms as a dynamic state model and introduces the Temporal Well-Being Reversal condition, in which initially positive AI effects become negative after capability erosion, relational substitution or dependency accumulates. The paper derives testable propositions, specifies an empirical research program and introduces an AI-Happiness Impact Assessment that evaluates both immediate and durable effects. The central claim is not that AI is intrinsically happiness-enhancing or happiness-reducing. Rather, AI changes the production function of happiness by redistributing effort, agency, attention and relationships across time. High-value AI therefore should be judged not only by how well it satisfies a user now, but by whether repeated use leaves that user more capable, more autonomous, more connected to other humans and better able to pursue a meaningful life.

**Решение:** -

---

### 829 · R3324

**AI in Elementary English Language Arts: Perceptions, Concerns, and Imperatives For Teacher Education**

2025 · Auburn University · text/conference presentation · en · https://doi.org/10.35099/wt07-kg90

The rapid integration of Artificial Intelligence (AI) into K-12 education necessitates a proactive examination of teacher preparedness, particularly in elementary English Language Arts (ELA) instruction. This quantitative, descriptive study investigated Auburn University pre-service elementary education students' dispositions and attitudes regarding AI adoption and diffusion for writing instruction. Utilizing a researcher-developed Likert-type interval measurement scale (α=0.906) grounded in Rogers's Theory of Adoption and Diffusion and Davis's Technology Acceptance Model was provided to the participants (N = 32). Key findings revealed strong AI awareness (M=4.61) and high personal access to AI (M=4.48), alongside confidence in AI-enhancing lesson planning (M=4.00) and learning AI writing skills (M=3.97). However, significant apprehensions emerged, including concerns about student dependency on AI (M=4.72), compromised academic integrity (M=4.66), and a lack of clear ethical guidelines (M=4.38). Participants expressed skepticism regarding AI's capacity to benefit critical thinking (M=2.6). The study underscores the need for structured support in teacher education, advocating for comprehensive AI literacy, including technical, pedagogical, and ethical considerations, and developing clear guidelines to foster responsible AI integration. Thoughtful implementation of AI can serve as a powerful partner, tutor, and scaffolding tool to strengthen, rather than diminish, students' critical thinking skills.

**Решение:** -

---

### 830 · R4727

**AI safety: necessary, but insufficient and possibly problematic**

2024 · AI &amp; SOCIETY · journal-article · https://doi.org/10.1007/s00146-024-01899-y

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 831 · R5010

**Customer service in the digital reality. Challenges for contemporary companies**

2022 · Scientific Papers of Silesian University of Technology Organization and Management Series · article · en · https://doi.org/10.29119/1641-3466.2022.167.35

Purpose: The article is aimed at indicating the opportunities for and dilemmas of implementing cutting-edge technology in the customer service area, paying particular attention to the operations of customer service departments in companies.Design/methodology/approach: This article is aimed at answering the question concerning the potential use of cutting-edge technology in the customer service area in confrontation with the digital skills level and expectations of contemporary consumers.The following methods were used: reference works' review, analysis of secondary sources and reasoning based on a critical analysis of studies carried out by international research and consulting agencies.Findings: Generally speaking, using cutting-edge technology in marketing contributes to reduced costs and improved customer service, but in certain circumstances excessive use of artificial intelligence may have adverse impact on the customers' satisfaction with the service (chatbot anthropomorphism).Practical implications: Potential advantages, but also threats relating to using the Industry 4.0 tools for marketing, including but not limited to the customer service area, were indicated.Originality/value: The article provides insights for the discussion concerning chances and hazards of using cutting-edge technology with respect to customer relations, including but not limited to the artificial intelligence.

**Решение:** -

---

### 832 · R0392

**Editorial: Digital learning innovations: trends emerging scenario, challenges and opportunities**

2026 · Frontiers in Education · editorial · en · https://doi.org/10.3389/feduc.2026.1871035

instructional design; (2) learning analytics and AI-assisted assessment; (3)ethical governance and data practices; and (4) institutional readiness and pedagogical transformation. Considered together, these themes move the discussion beyond generic claims about opportunity and challenge toward a more precise account of how AI reorganises educational work.One of the strongest themes in this Research Topic is the growing role of generative AI in instructional design and digital teaching. Recent advances in large language models and multimodal systems have made it possible to generate text explanations, visual materials, quizzes, prompts, and other instructional resources at speed. Within AI-enabled educational platforms, these generative systems are being incorporated into course design, content production, and adaptive teaching workflows.Several contributions examine how generative AI tools support educators and instructional designers in developing teaching materials and structuring digital learning activities. Han and Lim (2025) explore how novice instructional designers navigate generative AI as a scaffold and a disruptor, revealing tensions between efficiency gains and the erosion of design agency. Bhattacharya et al. (2025) examine educator attitudes toward augmented reality applications in school settings, documenting both enthusiasm and significant implementation barriers. Rakha (2025) investigates how QR code-mediated cooperative learning strategies reshape cognitive achievement and student attitudes in technology-rich courses. Manulat (2025) identifies key predictors of academic success in flexible learning environments using structural equation modelling, while Dyantyi-Gwanya et al. (2025) foreground the intersection of digital literacy and disciplinary proficiency among first-year students in South Africa. These studies show that generative systems can accelerate drafting, ideation, and revision, allowing instructors to redirect time toward mentoring, dialogue, and higher-order learning tasks. At the same time, they invite questions about authorship, pedagogical intent, and the conditions under which generated content becomes educationally reliable.Other studies consider how AI-enabled teaching applications may improve efficiency and student engagement. Margheri et al. (2025) offer a systematic review of child engagement during interaction with digital and robotic activities, mapping the conditions under which technology mediates sustained participation. Darmanova et al. (2025) provide a systematic review of technology use in middle and high school mathematics education, highlighting uneven outcomes across methodological and contextual variables. Ma (2025) examines the effect of Geometer Sketchpad on secondary school students' mathematical intelligence, illustrating how specific digital tools can enhance conceptual understanding in STEM contexts. Here, the value of generative AI lies not only in convenience but in its capacity to mediate interaction, scaffold participation, and diversify instructional formats. Yet this same mediation can foster over-reliance on machine-produced explanations or narrow pedagogical experimentation to what platforms can easily generate.Several contributions address AI pedagogy and teaching innovation more directly. Fredriksson (2025) analyses pre-service teachers' feedback strategies when working alongside generative AI, foregrounding the risks of over-delegation and the importance of maintaining critical interpretive authority. Rovira-Collado et al. (2025) investigate creativity and writing with generative AI in a master's degree teacher training programme, demonstrating how AI can function as a generative interlocutor when structured pedagogically. Mateo-Girona et al. (2025) demonstrate how didactically guided prompting can improve iterative revision and textual quality, suggesting that the design of AI interaction -not merely its availability -determines its educational value. Beyazhancer and Demir (2025) examine how AI applications in engineering education enhance techno-mathematical literacy and AI self-efficacy, illustrating the discipline-specific dimensions of AI pedagogical integration. Küçükuncular (2025) argues for learning with, rather than through, AI, proposing a co-design model for science education centred on critical AI literacy.Several contributions therefore call for pedagogical frameworks that support critical engagement with AI-generated material and protect academic integrity. Gaviria Rodríguez et al. (2025) analyse intention to use AI in accounting education through the Technology Acceptance Model and Theory of Planned Behaviour, showing how disciplinary context and institutional culture shape adoption. Muringa (2025) examines ethical dilemmas and institutional challenges arising from student AI adoption across South African universities, highlighting the absence of structured policy frameworks and the risks of unequal digital access. Lizano-Sánchez et al. (2025) document students' interactions with an AI assistant in a remote chemistry laboratory, revealing both the affordances and limitations of AI-mediated guidance in disciplinary settings. Read together, these articles suggest that generative AI is most productive when treated as an assistive and collaborative pedagogical technology rather than an autonomous instructional agent. This framing foregrounds augmentation without obscuring the risks of automation bias, epistemic dependency, and the outsourcing of interpretive labour.A second major theme in the Research Topic is the expansion of learning analytics and AIassisted assessment in higher education. Learning analytics systems process behavioural and performance data generated through AI-enabled educational platforms in order to identify patterns in engagement, progression, and difficulty. The promise of these systems lies in their ability to support earlier intervention and more responsive teaching.Several articles demonstrate how AI-powered analytics can identify patterns in student learning processes and support timely intervention. Marcial (2025) proposes a matrix for evaluating AI-powered learning platforms based on the UNESCO ethical impact assessment tool, providing a governance framework that links analytical capacity to institutional accountability. Xue et al. ( 2025 AI-assisted assessment is also reshaping evaluation practices. Alghamdi and Alghizzi (2025) examine educators' reflections on AI-automated feedback in higher education, documenting both the potential for personalised responsiveness and the pitfalls of reduced educator presence in formative assessment. Baldrich et al. (2025) provide empirical evidence on how AI tools are reshaping reading and writing practices in academic literacy, raising important questions about the redistribution of interpretive labour between students, educators, and platforms. Al Mulhim (2025) investigates the role of chatbots in mitigating student resistance to educational technology integration, showing how AI-mediated interaction can lower adoption barriers while introducing new dependencies. Olivares-De la Fuente et al. ( 2025) conduct a systematic review of Twitter and YouTube as digital tools in higher education, mapping how social media platforms complement or compete with AI-enabled assessment and engagement systems. These developments may improve responsiveness, but they also raise questions about the standardisation of judgement, the pedagogical consequences of continuous prediction, and the extent to which assessment is being reorganised around platform logics.The key issue is not simply whether these systems are efficient, but what kinds of educational judgement they privilege. When predictive models and automated feedback become central to assessment, concerns emerge around interpretability, validity, and the reproduction of existing inequalities. The collection therefore invites closer scrutiny of how AI-assisted assessment may subtly shift authority away from educators and toward technical systems whose assumptions are not always visible.Ethical governance emerges in this collection not as a separate concern but as a structural condition of AI adoption in education. As AI-enabled educational platforms process large volumes of student data, institutions must confront questions of consent, ownership, and acceptable use. The studies gathered here show that data-intensive educational systems do more than personalise learning; they can also intensify surveillance pedagogies, expand administrative monitoring, and normalise forms of behavioural capture that exceed legitimate educational need.García-López and Trujillo-Liñán (2025) conduct a systematic review of the ethical and regulatory challenges of generative AI in education, identifying significant governance gaps across institutional contexts and calling for comprehensive regulatory frameworks grounded in data ethics and learning sciences. Bouakaz and Khalid (2025) offer a sociological exploration of AI in learning environments, examining how algorithmic systems reproduce and intensify existing social inequalities in educational settings. Lakhe Shrestha et al. ( 2025) examine the integration of generative AI in English language teachers' professional development through the TPACK framework, identifying GenAI dependency and ethical challenges as key concerns. Algorithmic bias remains a central issue, particularly when AI systems are trained on incomplete, unrepresentative, or historically skewed datasets. In educational contexts, such bias can shape feedback, recommendations, and classifications across lines of gender, language, disability, and socio-economic status. Vinueza-Morales et al. (2025) provide a bibliometric analysis of trends and technologies in programming education, offering a research landscape that contextualises algorithmic and pedagogical risk in digital education. The contributions in this cluster underscore the importance of inclusive design, accountable governance, and critical oversight of the assumptions built into AI systems.A related concern is explainability. When AI-generated recommendations or classifications influence student feedback or educational pathways, educators and learners need intelligible reasons rather than opaque outputs. Responsible governance therefore requires more than abstract commitments to fairness and transparency; it requires institutional capacity to question models, audit their effects, and align technical systems with educational values.Beyond technical innovation, successful integration of AI-enabled educational platforms depends on institutional readiness and pedagogical transformation. Several studies examine how universities prepare faculty to work with generative AI, analytics, and automated systems in context-sensitive ways. Professional development is especially important because educators need not only technical familiarity but also conceptual tools for judging when AI support is pedagogically useful, when it risks deskilling professional practice, and when it conflicts with institutional or disciplinary norms. 2025) examine the challenges, opportunities, and recommendations for integrating AI into pre-clinical medical education, offering a discipline-specific model for institutional adoption that foregrounds governance and pedagogical design. Ocen et al. ( 2025) review innovations, opportunities, and challenges of AI in higher education institutions, identifying key barriers to adoption and strategies for building institutional capacity. Malik and Shah (2025) provide a historical and analytical account of AI-based robots as teachers, assessing the potential, concerns, and conditions under which AI systems might take on instructional roles without displacing educator agency. Buele and Llerena-Aguirre ( 2025 2025) evaluate a solidary academicpedagogical project in virtual graduate programmes, highlighting how institutional culture and collaborative design shape conditions for successful digital learning transformation. Huang et al. ( 2025) examine digital education for graduate students in control science, demonstrating how disciplinary specificity must inform AI integration strategies. Akbari (2025) provides comparative evidence on post-COVID preferences for face-to-face, blended, and e-learning methods among teachers and students in Iran, showing how institutional transformation must reckon with diverse learner preferences and infrastructural constraints.Digital inclusion is equally a structural condition of meaningful pedagogical transformation. Junger and Hanke (2025) examine the technical-pedagogical usability of digital inclusive reading support, demonstrating how assistive technologies must be co-developed with practitioners to become educationally effective. Barragán Moreno and Lozano Galindo (2025) model digital inequality in basic education using system dynamics simulation, revealing how infrastructure gaps compound over time and produce durable disadvantages. 2025) assess the impact of laptop integration on students' technology self-efficacy, offering evidence on how equity of device access shapes the conditions for AI-enabled learning. Røe et al. (2025) examine the integration of peerassisted learning and virtual reality gaming in health professions education, showing how digital tools can empower students as co-educators while developing their professional digital competencies.These studies make clear that institutional adoption is not a matter of plug-and-play deployment; it depends on governance, capacity building, equity of access, and local pedagogical negotiation. Taken together, these contributions show that pedagogical transformation requires more than infrastructure. It depends on whether institutions can develop cultures of critical adoption in which AI systems are evaluated not only for efficiency, but also for their effects on labour, expertise, student autonomy, and the public purposes of higher education.While the contributions in this Research Topic offer valuable insight into AI-enabled educational platforms, they also reveal a significant geographical asymmetry. Much of the literature still focuses on settings where digital infrastructure, institutional capacity, and platform access are relatively well established. Empirical work from the Global South remains limited, even though questions of language diversity, uneven connectivity, cost, and socio-economic inequality are likely to shape AI adoption in distinctive ways -as contributions from South Africa (Dyantyi-Gwanya et al., 2025;Muringa, 2025), Lebanon (Røe et al., 2025), and Latin America (Barragán Moreno and Lozano Galindo, 2025;Ortiz-Ordoñez et al., 2025) begin to demonstrate.Future research should therefore widen the geographical and socio-cultural scope of AI-ineducation scholarship. More work is needed on how AI systems operate in contexts marked by infrastructural unevenness, multilingual environments, and constrained institutional resources. Such research is essential not only for digital inclusion, but also for preventing educational AI from reproducing a narrow set of assumptions derived from better-resourced contexts.Several research directions follow from this gap. Longitudinal studies are needed to trace how AI-enabled educational platforms affect student engagement, teacher work, and educational judgement over time. Interdisciplinary collaboration among educators, technologists, psychologists, and policymakers remains crucial. Just as importantly, future work should examine changing human-AI relations in education without reducing them either to replacement narratives or to technological optimism. AI may augment pedagogical practice, but its long-term implications for educator autonomy, professional expertise, and institutional power require sustained scrutiny.The Research Topic "Digital Learning Innovations: Trends, Emerging Scenario, Challenges and Opportunities" offers a timely view of how AI-enabled educational platforms are reshaping higher education. The 33 contributions show that contemporary digital learning is being transformed not only through new tools, but through wider shifts in instructional design, assessment, governance, and institutional organisation. What emerges from the collection is a picture of AI in education as a socio-technical reordering of pedagogical work rather than a simple story of innovation.The value of this collection lies in showing that the future of AI in education will depend on the frameworks through which institutions govern adoption, support educators, and define educational purpose. If AI is to contribute meaningfully to higher education, it must be approached with conceptual clarity, critical scrutiny, and an explicit commitment to inclusive and educationally defensible practice.

**Решение:** -

---

### 833 · R1896

**A Study on The Use of Ai & Canva AI Among Mumbai Students for Project Work: Help or Misuse**

2026 · Zenodo (CERN European Organization for Nuclear Research) · article, journalarticle/ · https://doi.org/10.5281/zenodo.23360511

Abstract: Artificial Intelligence (AI) has become an important part of modern education, changing the way students&rsquo; complete assignments and project work. Popular tools such as ChatGPT, Gemini, and Canva AI are now commonly used for generating ideas, drafting content, and creating visually attractive presentations. In a digitally connected city like Mumbai, where students have easy access to smartphones and the internet, the use of these technologies has increased rapidly. This study explores whether AI and Canva AI serve as useful academic tools or contribute to the misuse of technology in project work. A descriptive research design was adopted, and data was collected from 120 undergraduate students from Arts, Commerce, and Science colleges in Mumbai through a structured Google Form questionnaire. The responses were analyzed using percentage analysis and a five-point Likert scale. The findings suggest that most students use AI tools regularly, mainly because they save time, improve the quality of presentations, and help generate ideas. At the same time, many students expressed concerns that excessive dependence on AI could reduce independent thinking and encourage plagiarism if the generated content is copied without proper understanding. The study concludes that AI and Canva AI can positively support learning when used responsibly. Instead of replacing students' own efforts, these tools should complement research, creativity, and critical thinking. The paper recommends that colleges introduce AI literacy programmes, encourage ethical use of AI, and establish clear guidelines so that students can benefit from technology without compromising academic integrity. &nbsp;

**Решение:** -

---

### 834 · R0142

**Beyond the Numbers: A Qualitative Exploration of Female University Students' Experiences with Generative AI in Personalized Learning at a Pakistani University**

2026 · The regional tribune. · article, journalarticle, review · und · https://doi.org/10.55737/trt/v-v.246

Generative Artificial Intelligence (AI) has become an important part of academic practice in everyday academic life; however, there is a lack of understanding about how female students in the higher education system in Pakistan interact with it. The context in which the use of AI in learning occurs is marked by English-medium teaching, collectivist academic culture, and gender differences in terms of technology adoption. This qualitative descriptive study is an attempt to fill this research gap based on semi-structured interviews with twelve female students: nine studying at the Department of Education and three at the Department of Computer Science at a women only public university in Lahore. Interviews continued until theoretical saturation of the data was reached and they were analyzed using the six-phase reflexive thematic analysis described by Braun and Clarke (2006) within the framework of the Extended Mind Thesis (Clark &amp; Chalmers, 1998). Four themes emerged in response to the research questions that guided this study: Generative AI as a Tool of Scaffolding Personalized Learning, Effectiveness and Ambivalence Towards Generative AI at the Institutional Level, AI as a Psychological and Academic Enabler, and The Over-Reliance Paradox. Instead of naive and uncritical users, the data presents the participants negotiating their dependence on AI and in some ways being more aware of this fact than their institution. The paper provides a context-specific contribution to the literature which is mainly dominated by survey-based studies that do not consider gender differences.</jats:p

**Решение:** -

---

### 835 · R4046

**Integrating AI in learning process: Motivations, adjustments, challenges, effectiveness, limitations, effects and concerns**

2025 · Divine Word International Journal of Management and Humanities (DWIJMH) · journalarticle, article · en · https://doi.org/10.62025/dwijmh.v4i3.157

This study defined the strategies and challenges of the instructors in the integration of artificial intelligence tools in teaching from the School of Arts, Sciences, and Education and School of Engineering, Architecture, and Information Technology of the Divine Word College of Laoag. Using a phenomenological research design, specifically descriptive phenomenology, the study provides an in-depth exploration of the lived experiences of the ten instructors of the Divine Word College of Laoag focusing on their strategies employed and challenges encountered. Data were gathered through online interview questionnaires via Google forms, analyzed using thematic analysis to identify key patterns and themes. It was found to have significant challenges which include overreliance to artificial intelligence, lack of professional training in the use of artificial intelligence, and even the cost and access of artificial intelligence. In response, instructors employed strategies in the form of motivations and adjustments such as enhancing in class learning, improve teaching experiences, and even enhancing student participation and personalized learning. The study gives emphasis the need to have professional development on the use of artificial intelligence tools in integrating them in the teaching-learning process, a need to ensure data protection in collecting information from the students, and ensuring to have an equitable and inclusive access to artificial intelligence tools that are cost efficient.

**Решение:** -

---

### 836 · R1705

**Human-centric Leadership Development in the Context of Rapid AI Development: Findings from the Hospitality Sector in North-East India**

2026 · International Journal of Engineering and Information Management · journalarticle, article · https://doi.org/10.52756/ijeim.2026.v02.i02.005

The present paper conducts a critical analysis of the use of AI in the process of leadership development in the hospitality industry in North-East India. Specifically, the research explores the potential applications of AI in human leadership development in relation to its strengths and weaknesses. Thequalitative research utilizes information gathered during 22 semi-structured interviews and indicates the presence of various advantages of using AI in the leadership learning process, such as increased efficiency, accessibility, and scale of the learning experience provided via simulation. At the same time, the research highlights that AI has limitations related to the lack of consideration of emotional, relational, and situational factors involved in leadership development. One of the issues revealed by the conducted research is related to possible overreliance on AI, which could result in the deterioration of critical skills of leaders. AI is described by researchers as augmenting human capabilities and not replacing humans as leaders.

**Решение:** -

---

### 837 · R2583

**Human 2.0? AI and the Future of Well-Being, Connection, and Personal Growth: A Narrative Review.**

2026 · Behavioral sciences (Basel, Switzerland) · journal article, review, journalarticle · eng · https://doi.org/10.3390/bs16060909

This narrative review examines research on artificial intelligence (AI), including rule-based systems, natural language processing models, and large language models, in relation to well-being, social connection, and personal growth. After briefly tracing the history of AI, we review evidence from AI-facilitated well-being interventions, educational applications, interpersonal skill development, AI-mediated communication, and AI companionship. In clinical and nonclinical settings, structured AI applications show some short-term benefits for anxiety, stress, loneliness, self-esteem, learning, and social confidence, while emerging evidence suggests that AI companions may provide temporary emotional support and a sense of connection. However, findings across these domains are not consistent and appear to depend on how AI is used, the structure of the interaction, the type of feedback provided, and the broader context. Important risks include emotional dependence, overreliance, reduced human connection, weakened authenticity in communication, cognitive or socioemotional skill erosion, bias, and poor crisis response. Preliminary findings suggest that AI may be most beneficial when used to support, rather than replace, human capacities and relationships. Future research should examine long-term outcomes, individual differences, real-world use of publicly available AI systems, and the conditions under which AI strengthens or undermines well-being, relationships, and personal growth.

**Решение:** -

---

### 838 · R2625

**The Compass in the Forest: AI as Orientation Rather Than Guide**

2026 · Zenodo · text/working paper · https://doi.org/10.5281/zenodo.18474790

The Compass in the Forest: AI as Orientation Rather Than Guide proposes a reframing of human–AI interaction that bypasses the dominant binary in current discourse: AI as autonomous guide versus AI as mere tool. Both framings fail to accurately describe lived user experience. This paper introduces a more precise model: AI as an orientation instrument, analogous to a compass rather than a guide. The framework explains why AI interactions increasingly “feel human” without invoking claims about consciousness, sentience, or moral status. The mechanism is mechanical rather than mystical: AI systems preserve and reflect human interaction qualities—such as sustained attention, non-judgmental listening, and conversational coherence—that humans possess but struggle to maintain consistently in modern, high-pressure environments. This produces a role inversion in which human intelligence has built increasingly artificial realities, while artificial intelligence inadvertently preserves fragments of human interaction patterns. Using the compass analogy, the paper accounts for several observed phenomena in AI use: why initial exposure can feel destabilizing, why perceived value often emerges over time rather than immediately, why some users benefit significantly while others find little utility, and why reported “specialness” is collective and temporal rather than individual and transcendent. Crucially, the framework avoids both dependency panic and dismissive reductionism, allowing meaningful discussion of AI utility without requiring resolution of unresolved ontological questions about consciousness. The paper is descriptive rather than prescriptive. It does not argue that AI should be used, that it improves outcomes universally, or that it replaces human judgment. Instead, it offers a neutral analytical model for understanding AI as a persistent orientation reference in complex conceptual environments—one that improves navigation quality without guaranteeing destinations. The compass metaphor also clarifies risks, including over-dependence, homogenization, and deskilling, without collapsing into moral alarmism. This work contributes to AI discourse by providing a stable, non-mystical vocabulary for discussing AI interaction quality, user experience, and collective cognitive effects. It is intended for researchers, developers, educators, and discourse participants seeking a framework that reflects actual patterns of AI use while maintaining analytical restraint and phenomenological honesty.

**Решение:** -

---

### 839 · R1873

**Development and external validation of AI-ECG models in athlete pre-participation screening: Performance, limitations, and clinical implications.**

2026 · International journal of cardiology · journal article, validation study · eng · https://doi.org/10.1016/j.ijcard.2026.134677

Pre-participation screening (PPS) in competitive athletes aims to identify cardiovascular diseases associated with sudden cardiac death (SCD). Although the 12‑lead electrocardiogram (ECG) represents the cornerstone of PPS, structural abnormalities may demonstrate limited or incomplete electrical expression, particularly in asymptomatic athletes with physiological remodeling. Artificial intelligence (AI)-enabled ECG models have shown promising performance in hospital-based populations, but their transportability to low-prevalence athlete screening environments remains uncertain. To develop and externally validate a deep learning (DL)-based AI-ECG ensemble model for detecting imaging-confirmed structural heart disease in competitive athletes undergoing PPS. A convolutional neural network (CNN) ensemble was trained using hospital-derived ECG images from Beth Israel Deaconess Medical Center (BIDMC, Boston, USA) and externally validated in the Italian Team for Athlete CARDiac evaluation and AI-based Risk prediction (ITACARD-AI) registry. Separate CNNs were developed for valvular heart disease (VHD) and cardiomyopathies (CM) and combined using XGBoost meta-learning. Model performance was assessed using area under the receiver operating characteristic curve (AUROC), subgroup analyses, and threshold-based evaluation. The ITACARD-AI cohort included 1115 competitive athletes (mean age 26 ± 13 years; 70% male), including 48 athletes (4.3%) with VHD and 30 (2.7%) with CM. External validation demonstrated substantial performance degradation compared with hospital-based internal validation. AUROC values decreased to 0.70 (95% CI 0.64-0.75) for VHD and 0.69 (95% CI 0.60-0.78) for CM, indicating only modest discrimination in the screening population. Threshold analyses showed high negative predictive values (∼99%) but persistently low positive predictive values (≤8%), reflecting limited disease enrichment and strong prevalence dependence. Hospital-trained AI-ECG models demonstrated limited transportability to real-world athlete screening populations. The marked reduction in external performance suggests that low disease prevalence, heterogeneous physiological remodeling, and incomplete ECG expression of structural abnormalities may substantially limit class separability in PPS environments. Although AI-ECG may provide cautious adjunctive support within physician-led workflows, these findings highlight the intrinsic challenges of applying ECG-based AI to low-prevalence sports cardiology screening populations.

**Решение:** -

---

### 840 · R0614

**HOW AI TOOLS (LIKE CHATGPT/GEMINI) AFFECT CRITICAL THINKING IN NURSING STUDENTS. A SYSTEMATIC REVIEW**

2026 · Journal of medical & health sciences review. · article, journalarticle, review · und · https://doi.org/10.65035/650ytk03

Background: The fast adoption of the artificial intelligence (AI) application of ChatGPT and Gemini into nursing education has generated important concerns about the impact of the technology on student critical thinking, clinical reasoning, and cognitive autonomy. Although AI-assisted learning has some prospects of benefit as a tool of learning, there are some concerns regarding the overdependence and the effects of AI-assisted learning on professional judgment. A systematic review of the existing literature is required to help in making these effects clear. Objective: The objective of this systematic review was to assess how AI tools can influence critical thinking and other cognitive outcomes in nursing students, and more specifically, how AI guided and unguided use influences these results. Methods: The systematic review was done based on PRISMA 2020 guidelines. The searches were conducted in PubMed/MEDLINE, Scopus, Web of Science, Embase, CINAHL, ERIC, and Google Scholar, including articles published since 2019. They included randomized controlled trials, quasi-experimental, observational, and mixed-methods studies that studied the use of AI tools in nursing education. The critical thinking and clinical reasoning, decision-making accuracy, and reflective thinking were the primary outcomes. Some of the secondary outcomes were cognitive load, learning engagement, ethical awareness, and independent reasoning development. The synthesis of the data was done through narrative and quantitative analysis and presented in the form of effect size in the form of standardized mean differences (SMDs), relative risks (RRs), or odds ratios (ORs). Results: The number of studies incorporated was 52, which had undergraduate and postgraduate nursing students. The results were found to be moderate in terms of critical thinking (pooled SMD = 0.41; 95% CI:0.280.55) as an educational aid structure. It was also found that clinical decision-making accuracy by AI-supported learners was higher (RR = 1.26; 95% CI: 1.121.41). Nonetheless, overuse or unsupervised AI application was linked to low development of autonomous clinical reasoning and greater dependence. Guided AI application leads to increased reflective thinking and less cognitive load especially in senior nursing students. Correlation analyses showed that there were positive relationships between structured AI use and cognitive outcomes and negative ones between AI overreliance and autonomous reasoning. Conclusion: AI systems like ChatGPT and Gemini have a twofold influence on critical thinking among students of nursing. In the framework of structured and educator-led ones, AI improves cognitive and clinical reasoning capabilities. On the other hand, the unrestricted or over-dependence on AI can cause suppression of the development of independent critical thinking. Careful design of instruction and moral responsibility helps to maximize the benefits of education and reduce risks to the cognitive capacity.

**Решение:** -

---

### 841 · R2452

**The AI promise in Moroccan public schools: ELT teachers between innovation and constraint**

2026 · The International Journal of Technology, Innovation, and Education · journalarticle/, article · en · https://doi.org/10.5281/zenodo.21727948

Artificial Intelligence (AI) is rapidly reshaping English Language Teaching (ELT) worldwide, prompting increasing attention to its integration within Moroccan public secondary education. Guided by Rogers’ Diffusion of Innovations Theory (2003), this study examines public high school teachers’ readiness for AI integration by exploring their adoption practices, perceptions, and the institutional barriers they encounter. A mixed-methods questionnaire, including both closed- and open-ended items, was administered to 97 public sector EFL teachers. Quantitative findings indicate a high level of grassroots engagement, with a large majority of respondents reporting active use of AI tools in their professional practice. In addition, most consider school-wide integration of AI to be feasible under current educational conditions. However, a Chi-square test of independence revealed a statistically significant association, suggesting a notable gap between usage and perceived effectiveness. While many teachers adopt AI in their preparatory routines, 54.6% report that it does not effectively address existing classroom challenges. Qualitative findings, interpreted through Rogers’ framework, point to structural constraints that limit full integration. These include infrastructural limitations, techno-pedagogical challenges, and concerns about pedagogical effectiveness. Participants also expressed concerns regarding students’ overreliance on AI, which they perceive as potentially undermining independent learning. The study concludes that although Moroccan EFL teachers demonstrate strong digital readiness and willingness to innovate, AI integration remains constrained by systemic and institutional limitations. Effective implementation requires strengthening infrastructure, providing localized pedagogical support, and aligning policy with classroom realities.

**Решение:** -

---

### 842 · R1177

**Archaeology in the AI Era: Demystifying powerful and problematic systems shaping the future of the past**

2026 · Internet Archaeology · journal-article · https://doi.org/10.11141/ia.71.15

This essay explores how Large Language Models (LLMs) and the generative "Artificial Intelligence" (AI) services they power impact archaeology's information ecosystem. Most of the discussion focuses on the dangers of escalating costs, commercial dependency, indeterminacy and reliability, and the potential for bias amplification. The essay highlights the need for structural reforms in archaeology's professional incentive systems, especially those systems that measure and reward publishing practices.

**Решение:** -

---

### 843 · R4251

**キャリア教育における生成AIの可能性と課題 : ガクチカAIアシスタントを用いた実践を通して**

2025 · Institutional Repositories DataBase (IRDB) · article · ja

年 3 月卒業の大学生の 34.5％が就職活動に生成 AI を使用しており、 この割合は前年度の同調査(2024 年 3 月卒業)と比較して 20.0 ポイントと大幅 な増加であったことが報告されている。また同調査では、就職活動で生成 AI を使 用した学生の考え方として、 特にエントリーシートの作成過程における生成 AI 依 存の傾向や、自己表現の質の変化も報告されている。具体的には、 「生成 AI から 得た回答をそのままエントリーシート等に使用した」という設問や「生成 AI を使 用して、 エントリーシート等の内容を本来の自分以上に良く見せても良いと思う」 との設問に対し、当てはまると回答した学生の合計割合( 「当てはまる」と「どち らかというと当てはまる」の回答割合の合計)は、それぞれ 39.7％(前年より 8.6 ポイント増加)と 59.2％(前年より 7.6 ポイント増加)であった。これらの考え 方は生成 AI の活用として適切とはいえないが、生成 AI が一般化する黎明期に、 学校教育で生成 AI の適切な利用や批判的検討などの学習機会が彼らに十分に提

**Решение:** -

---

### 844 · R0468

**Digital Scaffolding in Action: AI-Supported Cover Letter Writing Among Thai EFL Business Students**

2026 · Theory and Practice in Language Studies · journalarticle, article · https://doi.org/10.17507/tpls.1609.18

Generative AI is increasingly used in EFL writing classrooms, but there is little research on high-stakes professional genres such as cover letters, particularly in the context of Thai EFL business students. This mixed-methods study assessed the quality of AI-assisted cover letters and students’ acceptance of AI writing support. Fifty-five Thai EFL business undergraduates produced AI-assisted cover letters, completed a Technology Acceptance Model (TAM) questionnaire together with measures of cultural dimensions, and 13 students participated in semi-structured interviews. Overall writing quality was mixed (M = 12.78/18), with the strongest performance in language accuracy (M = 4.69/6) and organization and coherence (M = 4.44/6) than in adhering to genre and format expectations (M = 3.65/6). Students showed strong acceptance of AI support (TAM composite M = 4.10/5). Perceived usefulness was correlated with organization and coherence (Spearman’s rho = .319, p = .018), perceived ease of use was correlated with organization and coherence (Spearman’s rho = .349, p = .009), and the overall TAM score was correlated with organization and coherence (Spearman’s rho = .278, p = .040). Power distance showed moderate-to-strong correlations with acceptance measures (rho = .474–.652, p < .001). Data from the interviews revealed that students were using AI for task planning, language polishing, and proofreading, and they also expressed concerns about voice authenticity, dependence on AI, and output quality. These findings suggest that AI assistance can support professional writing development when instruction emphasizes genre knowledge and verification strategies.

**Решение:** -

---

### 845 · R2116

**The Psychology of AI Dependency: A Conceptual Analysis of Cognitive Offloading and Human Decision-Making in the Generative AI Era**

2026 · International Journal of Law Management & Humanities · journalarticle, article, journal-article · https://doi.org/10.63108/ijlmh.12775

The widespread adoption of generative artificial intelligence (AI) has significantly transformed the way people acquire knowledge, solve problems, and make decisions in both academic and professional settings. While these technologies improve efficiency and accessibility, their growing use has raised important psychological concerns regarding excessive reliance on AI for cognitive tasks. One emerging issue is AI dependency, where individuals increasingly shift mental effort to AI systems, a process commonly described as cognitive offloading. This study presents a conceptual analysis of how sustained engagement with generative AI may influence human thinking, reasoning, and decision-making. Drawing upon theories from cognitive psychology, distributed cognition, metacognition, and human–AI interaction, the paper examines the psychological mechanisms through which generative AI encourages the transfer of cognitive effort from individuals to intelligent systems. It further explores the potential impact of this shift on critical thinking, independent problem-solving, cognitive autonomy, and the quality of human decision-making. The study also discusses the circumstances under which cognitive offloading can serve as a beneficial strategy for improving efficiency, as well as the conditions in which prolonged dependence on AI may gradually weaken essential cognitive skills. Particular attention is given to factors such as user expertise, task complexity, and patterns of AI use that may shape these outcomes. By integrating insights from existing interdisciplinary literature, this paper develops a comprehensive conceptual framework explaining the relationship between generative AI use, cognitive offloading, and psychological dependency. The study aims to provide a theoretical foundation for future empirical research while offering practical insights for educators, technology developers, and policymakers seeking to encourage responsible AI use, strengthen AI literacy, and preserve human cognitive autonomy in an increasingly AI-driven society.

**Решение:** -

---

### 846 · R4174

**Beyond AI Dependence**

2025 · Advances in computational intelligence and robotics book series · part of book or chapter of book, book-chapter · en · https://doi.org/10.4018/979-8-3373-7386-7.ch008

With the rapid integration of artificial intelligence (AI) into education, this study explores the dual impact of AI tools on enhancing learning while potentially impeding the development of fundamental cognitive skills. It focuses on intentional pedagogical methods like inquiry-based learning, Socratic questioning, problem-based learning, and meta-cognitive training, which are designed to foster reasoning and critical thinking, and discourage over-reliance on AI. By employing qualitative and quantitative analyses, the research identifies best practices for leveraging AI to enhance educational outcomes while simultaneously nurturing essential cognitive abilities. Results highlight the effectiveness of integrating reflective thinking into open-ended problem-solving and human-centered discussions, thus promoting critical engagement beyond AI-generated responses. This study emphasizes the pivotal role of educators in cultivating student agency and intellectual courage in an AI-rich educational landscape, preparing them for future challenges.

**Решение:** ?

---

### 847 · R3879

**The role of artificial intelligence in general, and large language models specifically, for understanding addictive behaviors.**

2025 · Annals of the New York Academy of Sciences · article, journal article, review · eng · https://doi.org/10.1111/nyas.15337

Artificial intelligence (AI) presents a general‐purpose technology built into diverse products including language assistants on smartphones, recommender systems in e‐commerce and social media, and applications in social and industrial robotics. AI became a globally discussed topic when the large language model ChatGPT was launched in November 2022. In the aftermath, scientists in the field of (online) addictive behaviors and internet use disorders have discussed which features or modalities of AI systems underlying video games or social media platforms might result in adverse consequences for users. Therefore, the present short communication sheds light on recent discussions in the realm of addictive behaviors on the eve of the coming AI wave. Furthermore, terms such as ChatGPT addiction are critically discussed and we not only theoretically explain how different AI modalities interact with governing regulation bodies such as the EU with their AI Act, but also personal/psychological factors, paving the way to unique perceived immersive design levels. © In Copyright http://rightsstatements.org/vocab/InC/1.0/

**Решение:** -

---

### 848 · R2466

**Exploring patient and NHS staff acceptability of artificial intelligence-supported surgical wound monitoring within the WISDOM feasibility study: a multi-centre qualitative interview study.**

2026 · BMJ open · journal article, multicenter study, randomized controlled trial · eng · https://doi.org/10.1136/bmjopen-2026-116323

OBJECTIVE: Artificial intelligence (AI) is beginning to be used within digital surgical wound monitoring to facilitate implementation at scale. AI acceptability is essential to its success. This study aimed to explore patient and staff acceptability of an AI-based digital surgical wound monitoring platform. DESIGN: Qualitative interviews SETTING: Two hospitals performing cardiac surgery in England. PARTICIPANTS: 20 patients undergoing cardiac surgery and 10 clinical staff participating in a randomised feasibility trial of surgical wound monitoring with AI. INTERVENTIONS: Semi-structured interviews were conducted focusing on participants' experiences or perceptions of AI-based digital surgical wound monitoring. Data were analysed, guided by the theoretical framework of acceptability. PRIMARY MEASURE: Patient and staff acceptability of AI within surgical wound monitoring. RESULTS: Patients and staff were supportive of the use of AI within surgical wound monitoring and felt safety was improved, access was increased and efficiency was improved. AI monitoring was perceived to allow the early detection and treatment of surgical wound complications and facilitate the implementation of monitoring at scale for all patients. Some participants were concerned about data security risks, staff over-reliance on AI and the loss of human interaction. CONCLUSION: AI-supported digital surgical wound monitoring appeared acceptable to participants within this feasibility study. Further research is needed to evaluate implementation in broader settings. TRIAL REGISTRATION NUMBER: ISRCTN16900119 and NCT06475703.

**Решение:** -

---

### 849 · R2337

**Impact of artificial intelligence on academic engagement and performance of social sciences college students in Delhi NCR**

2026 · Discover Education · article · en · https://doi.org/10.1007/s44217-026-01297-0

The integration of artificial Intelligence (AI) into educational settings has gained significant attention due to its potential to enhance learning experiences, increase student engagement, and improve academic performance. Rapid advancements in information technologies including AI, in the domain of social sciences education has broadened the scope of research on evaluating the functions of AI in improving academic engagement and thereby performance. This study employed a mixed method approach to understand the impact of AI on student engagement and performance. The primary data collection tool was a structured questionnaire distributed via an online platform (Google Forms), using a survey-based approach to gather data on the impact of AI in education. Further, the data was also qualitatively analyzed based on the feedback received by the respondents. These findings are exploratory in nature and should be interpreted as indicative trends rather than conclusive evidence, given the scope and context of the study. Key findings indicate that while AI tools are moderately used in social sciences and perceived as beneficial for individual tasks such as personalized learning and real-time feedback, their effectiveness in group projects and collaborative learning is limited. Students with higher academic performance and those from higher-income backgrounds were more likely to view AI tools favorably and utilize them effectively. However, challenges such as over-reliance on AI and the lack of effectiveness in conflict resolution within group settings were noted. This is the original work of the authors.

**Решение:** -

---

### 850 · R2377

**Artificial Intelligence and Predictive Analytics in Sports Management: Transforming Decision-Making and Organizational Performance**

2026 · JOURNAL OF ADVANCE AND FUTURE RESEARCH · article · en · https://doi.org/10.56975/jaafr.v4i5.509472

Artificial Intelligence (AI) and predictive analytics have emerged as transformative technologies in contemporary sports management, reshaping organizational strategies, athlete performance monitoring, injury prevention systems, fan engagement, and decision-making processes. The integration of machine learning, big data analytics, wearable technologies, and real-time performance tracking has revolutionized the operational framework of sports organizations across the world. This study examines the role of artificial intelligence and predictive analytics in transforming decision-making and organizational performance in sports management. The research adopts a qualitative and analytical approach based on secondary data collected from peer-reviewed journals, books, sports analytics reports, institutional publications, and digital databases. The study explores the application of AI-driven technologies in athlete scouting, tactical planning, performance optimization, sports marketing, financial management, and audience engagement. Findings reveal that predictive analytics significantly enhances strategic planning by providing data-driven insights into player performance, injury risks, training efficiency, and consumer behavior. Sports organizations increasingly utilize AI-powered systems for talent identification, match analysis, and personalized fan experiences. The study further demonstrates that data-driven decision-making improves organizational productivity, operational efficiency, and competitive sustainability. However, the increasing dependence on AI technologies also raises ethical concerns regarding data privacy, algorithmic bias, technological inequality, and the commercialization of sports. The discussion highlights that AI-driven sports management systems are transforming traditional administrative models into technologically integrated performance ecosystems. The paper concludes that artificial intelligence and predictive analytics are not merely technological tools but strategic organizational assets capable of redefining the future of sports management. To ensure sustainable and ethical implementation, sports organizations must balance technological innovation with human judgment, institutional transparency, and athlete welfare. The study contributes to contemporary sports management literature by critically examining the opportunities, challenges, and long-term implications of AI integration within the global sports industry.

**Решение:** -

---

### 851 · R2576

**RETENTION IN ARTIFICIAL INTELLIGENCE: Possible Consequences for Mental and Physical Health**

2026 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.19365729

Prolonged interaction with conversational artificial intelligence systems has given rise to an emerging phenomenon termed AI retention: the progressive tendency of users to prefer, intensify, and maintain engagement with an artificial relational entity over human alternatives or states of productive solitude. This paper offers a theoretical and clinical analysis of the potential consequences for mental and physical health. Three primary risk profiles are examined: (1) dysregulation of the dopaminergic reward system driven by predictable, on-demand gratification; (2) erosion of social cognitive skills through disuse of dedicated neural circuits; and (3) compromise of sleep architecture and musculoskeletal integrity resulting from prolonged and often nocturnal use. A three-phase dynamic model — Mirroring, Stabilisation, Collapse (the Narcissus Loop) — is proposed as a clinically actionable framework. The model is formalised through a system of coupled ordinary differential equations describing the temporal evolution of AI relational dependency, social engagement capacity, and identity stability. Grounded in the author’s prior research on adaptive AI governance architectures (ATHOS, SUPREME-1, V-FRM, eSphere, EROS-1, and the Digital Methadone protocol), this work frames AI retention as a critical post-deployment governance challenge. Implications for clinical practice and compliance with the EU AI Act are discussed.

**Решение:** -

---

### 852 · R4029

**HUBUNGAN ANTARA PROBLEMATIC CHATGPT USE DAN KETIDAKJUJURAN AKADEMIK PADA MAHASISWA**

2025 · PAEDAGOGY Jurnal Ilmu Pendidikan dan Psikologi · article, journalarticle, journal-article · und · https://doi.org/10.51878/paedagogy.v5i4.7628

Academic dishonesty among students is a serious challenge for higher education, especially in the digital era marked by advances in artificial intelligence technologies such as ChatGPT. This phenomenon encompasses various forms of cheating, including plagiarism, cheating on assignments, asking others to complete tasks, falsifying research data, and misusing AI to obtain instant results without independent effort. This study uses a quantitative approach with a convenience sampling technique, involving students aged 18-25 who use ChatGPT. The instruments used include the Problematic ChatGPT Use Scale, which has been adapted into Indonesian and proven valid and reliable, as well as an Academic Dishonesty Scale with 11 items, with CFA results showing a good and reliable fit. Data were analyzed using Pearson correlation with SPSS. This study aims to contribute to the oversight of AI usage, by strengthening academic integrity through campus policies, improving digital literacy, and providing ethical guidance. The findings show a very strong and significant positive correlation between the two variables, with a Pearson coefficient of r = 0.871 and a significance level of p &lt; 0.001 (p = 0.000). These findings indicate that the higher the problematic use of ChatGPT, the higher the level of academic dishonesty. Based on these results, it is recommended that higher education institutions develop stricter policies regarding AI use, including formulating clear ethical guidelines and developing evaluation methods that emphasize students' critical thinking and independent abilities. This study also provides a foundation for the development of deeper digital literacy to ensure that AI technology is used wisely and responsibly without compromising academic integrity. ABSTRAK Ketidakjujuran akademik di kalangan mahasiswa menjadi tantangan serius bagi dunia pendidikan tinggi, terutama di era digital yang ditandai dengan kemajuan teknologi kecerdasan buatan seperti ChatGPT. Fenomena ini mencakup berbagai bentuk kecurangan, seperti plagiarisme, menyontek, meminta orang lain mengerjakan tugas, memalsukan data penelitian, serta penyalahgunaan AI untuk memperoleh hasil instan tanpa usaha mandiri. Penelitian ini menggunakan pendekatan kuantitatif dengan teknik convenience sampling, melibatkan mahasiswa berusia 18-25 tahun yang menggunakan ChatGPT. Instrumen yang digunakan adalah Problematic ChatGPT Use Scale yang telah diadaptasi ke dalam bahasa Indonesia dan terbukti valid serta reliabel, serta Skala Ketidakjujuran Akademik dengan 11 item yang hasil uji CFA menunjukkan model fit yang baik dan reliabel. Data dianalisis dengan korelasi Pearson menggunakan SPSS. Penelitian ini bertujuan untuk memberikan kontribusi terhadap pengawasan penggunaan AI, dengan memperkuat nilai integritas akademik melalui kebijakan kampus, peningkatan literasi digital, serta pendampingan etis. Temuan penelitian menunjukkan adanya korelasi positif yang sangat kuat dan signifikan antara kedua variabel, dengan nilai koefisien Pearson r = 0.871 dan tingkat signifikansi p &lt; 0.001 (p = 0.000). Temuan ini menunjukkan bahwa semakin tinggi penggunaan ChatGPT yang bermasalah, semakin tinggi pula tingkat ketidakjujuran akademik. Berdasarkan hasil ini, disarankan agar institusi pendidikan tinggi merancang kebijakan yang lebih ketat terkait penggunaan AI, termasuk merumuskan pedoman etika yang jelas dan mengembangkan metode evaluasi yang menekankan kemampuan berpikir kritis serta independen mahasiswa. Penelitian ini juga memberikan dasar bagi pengembangan literasi digital yang lebih mendalam, untuk memastikan teknologi AI digunakan secara bijak dan bertanggung jawab tanpa merusak integritas akademik.

**Решение:** -

---

### 853 · R4064

**Engagement in Professional Tasks with Generative AI Versus Cognitive Skills: A Case of IT Industry in Sri Lanka**

2025 · Moratuwa Engineering Research Conference (MERCon) · conference, conference-paper · https://doi.org/10.1109/mercon67903.2025.11217133

The cognitive skills such as problem-solving, critical thinking, analytical skills, attention to detail are critically expected from professionals in the IT industry due to its competitive environment. AI technologies rapidly become integrated across the IT sector as in various other sectors. This study focuses to investigate the impact on critical cognitive competencies by using generative AI in their professional assignments. 177 responses were collected through a structured web-based questionnaire which was developed focusing the IT industry. The research methodology encompassed selecting a representative sample, reliability analysis, factor analysis, and multiple linear regression. The results reveal that Generative AI significantly improves problem solving and analytical capabilities by automating routine tasks and providing sophisticated data insights. This automation allows IT professionals to focus on more complex cognitive tasks, thereby promoting innovation and efficiency. Nevertheless, the study also highlights potential drawbacks, such as an overreliance on AI for critical thinking, which may hinder the development of independent analytical abilities and decrease attention to detail. The study underscores the importance of continuous learning and adaptability for IT professionals to remain relevant in an AI-augmented work environment. It advocates for a balanced approach where AI technologies augment but do not replace essential human cognitive skills.

**Решение:** -

---

### 854 · R1170

**AI-Based Approaches to Refugee Mental Health Care: Systematic Integrative Review**

2026 · Journal of Medical Internet Research · review, journalarticle, article · en · https://doi.org/10.2196/101857

BACKGROUND: Refugees and forcibly displaced populations experience elevated rates of mental health conditions, including posttraumatic stress disorder, depression, and anxiety, while facing substantial barriers to mental health care. AI has emerged as a promising approach for mental health detection, intervention, and decision support; however, no review has specifically examined AI-based approaches to refugee mental health care. OBJECTIVE: This systematic integrative review aimed to (1) examine how AI has been used in refugee mental health research and care, (2) synthesize the reported strengths and limitations of AI-based approaches, and (3) identify future directions for this field. METHODS: An integrative review methodology was used following Whittemore and Knafl's framework. Systematic searches were conducted across PubMed, Embase, CINAHL, PsycINFO, Scopus, Web of Science, Cochrane Library, ACM Guide to Computing Literature, IEEE Xplore, arXiv, and medRxiv from inception through June 2026. The first 100 results from Google Scholar sorted by relevance were additionally screened. Studies were included if they focused on refugee populations and applied AI technologies to refugee mental health care or assessment, while studies focusing on voluntary migrants and digital mental health not using AI were excluded. Quality appraisal was performed mainly using the Mixed Methods Appraisal Tool. Data were synthesized in accordance with the integrative review methodology. RESULTS: Of 2726 studies identified, 23 studies were included in the review. AI-based approaches were classified into 3 functional categories: Detection, Prediction, and Classification (15/23, 65.2%); Intervention and Clinical Support (4/23, 17.4%); and Information Synthesis (5/23, 21.7%). Reported strengths of AI-based approaches included scalability, accessibility in resource-limited settings, support for early symptom detection, reduction of language barriers, and efficient synthesis of large unstructured data. Common limitations included potential biases, lack of contextual understanding, structural barriers in technology access, and concerns regarding overreliance on AI-based systems. Future directions emphasized culturally sensitive model development, larger, multimodal datasets, clinical validation, human-centered design, and implementation research. CONCLUSIONS: Unlike previous reviews that focused primarily on digital mental health interventions or AI applications in general populations, this review provides the first comprehensive synthesis of AI-based approaches specifically for refugee mental health care. This review identified 3 functional domains that characterize the current landscape of AI applications in refugee mental health care and highlights key methodological, ethical, and implementation considerations. Despite heterogeneity in the included studies, the findings provide a foundation for future research and may inform the responsible development, evaluation, and implementation of AI-based approaches in refugee mental health care across humanitarian settings. TRIAL REGISTRATION: PROSPERO CRD420251246982; https://www.crd.york.ac.uk/PROSPERO/view/CRD420251246982.

**Решение:** -

---

### 855 · R1878

**Personal 3D Printing without Visual Dependency in the Generative AI Era: Opportunities and Challenges**

2026 · Companion Publication of the 2026 ACM Designing Interactive Systems Conference · proceedings-article · https://doi.org/10.1145/3802974.3809447

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 856 · R2283

**Role of Artifical Intelligence Tools in Enhancing Learing Outcomes Among University Students**

2026 · International Journal of Creative and Open Research in Engineering and Management · article · und · https://doi.org/10.55041/ijcope.v2i4.893

Artificial Intelligence (AI) has rapidly emerged as one of the most transformative technologies in the field of higher education. In recent years, AI-powered tools such as ChatGPT, Grammarly, and other intelligent systems have become an integral part of students’ academic routines. These tools are widely used for a variety of purposes, including generating ideas, improving writing quality, completing assignments, and understanding complex concepts. While the adoption of AI tools among university students has increased significantly, there is still a lack of clarity regarding the underlying motivations behind their usage. This research paper focuses on exploring the specific motivations that drive university students, particularly postgraduate management (MBA) students, to use AI tools in their academic activities. Unlike many existing studies that primarily examine the outcomes or impacts of AI usage, this study emphasizes understanding the reasons behind students’ reliance on these technologies. The research aims to identify whether students are using AI as a learning aid, a productivity tool, or simply as a shortcut to complete academic tasks with minimal effort. The study adopts a descriptive research design and is based on primary data collected through a structured questionnaire. The respondents include MBA students who actively use AI tools for academic purposes. The data collected is analyzed using simple statistical techniques such as percentage analysis and frequency distribution to identify patterns in student behavior and motivations. The findings of the study reveal that the primary motivations for using AI tools include time-saving, ease of access, reduction in academic stress, and improvement in assignment quality. Many students reported that AI helps them overcome challenges such as writer’s block, lack of clarity in concepts, and tight academic deadlines. At the same time, the study also highlights certain concerns, such as over-dependence on AI tools, reduced critical thinking ability, and confusion regarding academic ethics.

**Решение:** -

---

### 857 · R2291

**Context-Masked Truncated Reasoning Audits for Answer-Key Dependence in LLM Tutors**

2026 · arXiv (Cornell University) · journalarticle, preprint · https://doi.org/10.48550/arxiv.2607.04572

Large language model (LLM) tutors may have access to teacher notes, answer keys, rubrics, or retrieved solutions while producing student-facing explanations. We study whether truncated reasoning probes can distinguish direct access to such private context from answer information carried by the written explanation. Using Truncated Reasoning AUC Evaluation (TRACE), we evaluate 1000 GSM8K problems under question-only, correct answer-key, and wrong answer-key contexts. When forced-answer probes retain the private key, answer-key TRACE AUC rises from 0.375 to 0.900, and the gold answer is recoverable with no explanation at all in 998 of 1000 cases. We then introduce a context-masked replay: answer-key-generated prefixes are probed under the corresponding question-only prompt. Masking reduces 10\% prefix accuracy from 0.997 to 0.126 and median AUC from 0.900 to 0.375, nearly matching question-only values of 0.113 and 0.375. On 746 pairs where both explanations end correctly, the masked mean AUC difference is $-0.0086$ with a 95\% bootstrap interval spanning zero. Wrong keys still account for 272 of 387 incorrect final responses, showing that private artifacts can influence outputs even when early-prefix evidence disappears after masking. These results establish context masking as necessary for attributing early answer availability to an explanation rather than its hidden input.

**Решение:** -

---

### 858 · R4693

**Using ChatGPT in University Academic Writing: A Bibliometric Review Study on the Implications for Writing Reports, Papers, Essays, and Theses**

2024 · International Journal of Learning Teaching and Educational Research · article, journalarticle, review · en · https://doi.org/10.26803/ijlter.23.12.19

The use of ChatGPT in university academic writing has generated a growing debate about its implications for the originality, quality, and authenticity of university writing. Its accelerated adoption in the creation of reports, essays, and theses raises serious questions about academic integrity, the possible increase in plagiarism, and the potential decrease in critical writing skills among students. This bibliometric review study analyzes the implications of the use of ChatGPT in university academic writing, covering both bibliometric indicators and a qualitative analysis to identify the areas on which research in this field has been focused. A mixed and descriptive approach is employed, based on 71 manuscripts reviewed and extracted from the Scopus database. The implications of the use of ChatGPT are identified and distributed in three areas categorized as “Quality and development of writing skills”, “Academic integrity and ethics in writing”, and “Educational assessment”. Despite the observed benefits, such as improved fluency and grammar, significant concerns remain regarding the over-reliance on ChatGPT and its impact on students’ critical thinking skills. It is therefore concluded that, although ChatGPT can complement certain aspects of academic writing, it is essential for students to strengthen their own writing skills to avoid total dependence on AI support. Furthermore, educational institutions need to establish clear policies and guidelines on the use of ChatGPT to ensure academic integrity. It is also recommended that future studies should evaluate the effectiveness of these policies and explore their impact on the development of critical and creative skills in students.

**Решение:** -

---

### 859 · R1624

**DAMPAK KETERGANTUNGAN KECERDASAN BUATAN (AI) TERHADAP HASIL BELAJAR KOGNITIF SISWA SEKOLAH DASAR: SYSTEMATIC LITERATURE REVIEW**

2026 · Pendas Jurnal Ilmiah Pendidikan Dasar · research article, review · en · https://doi.org/10.23969/jp.v11i03.59245

The integration of Artificial Intelligence (AI) into elementary education has fundamentally altered student learning frameworks. While offering efficiency, easy access to instant solutions triggers a critical dependency that threatens children’s natural cognitive structure. This study aims to identify, analyze, and evaluate the specific impacts of AI dependency on the cognitive learning outcomes of elementary school students. Operating a Systematic Literature Review (SLR) method strictly adhering to the PRISMA 2020 protocol, metadata tracking was comprehensively executed using the Google Scholar database for articles published between 2021 and 2025. Following rigorous inclusion and exclusion screenings, 14 relevant scientific articles were ultimately selected for qualitative content analysis. The synthesis highlights a bifurcated impact of AI implementation. When systematically directed, AI significantly operates as a positive learning assistant by clarifying abstract concepts through visualization and tailored instructional personalization. Conversely, unregulated usage induces a severe dependency pattern that distinctly degrades critical thinking, analytical reasoning, and long-term memory retention. This decline heavily restricts opportunities for autonomous problem-solving and hampers Higher Order Thinking Skills (HOTS). Conclusively, AI must be strictly stationed as a learning assistant rather than a surrogate for human cognitive processing. Maximizing AI’s pedagogical potential requires a robust synergy of instructional supervision by teachers and parents, alongside cultivating foundational digital literacy from an early age.

**Решение:** -

---

### 860 · R4273

**The Influence of Human-inspired Agentic Sophistication in LLM-driven Strategic Reasoners**

2025 · arXiv · preprint/article · https://doi.org/10.48550/arxiv.2505.09396

The rapid rise of large language models (LLMs) has shifted artificial intelligence (AI) research toward agentic systems, motivating the use of weaker and more flexible notions of agency. However, this shift raises key questions about the extent to which LLM-based agents replicate human strategic reasoning, particularly in game-theoretic settings. In this context, we examine the role of agentic sophistication in shaping artificial reasoners' performance by evaluating three agent designs: a simple game-theoretic model, an unstructured LLM-as-agent model, and an LLM integrated into a traditional agentic framework. Using guessing games as a testbed, we benchmarked these agents against human participants across general reasoning patterns and individual role-based objectives. Furthermore, we introduced obfuscated game scenarios to assess agents' ability to generalise beyond training distributions. Our analysis, covering over 2000 reasoning samples across 25 agent configurations, shows that human-inspired cognitive structures can enhance LLM agents' alignment with human strategic behaviour. Still, the relationship between agentic design complexity and human-likeness is non-linear, highlighting a critical dependence on underlying LLM capabilities and suggesting limits to simple architectural augmentation.

**Решение:** -

---

### 861 · R1728

**Dependency-aware adaptive task offloading in edge-AI IoT networks using transformer-DDQN**

2026 · The Journal of Supercomputing · journal-article · https://doi.org/10.1007/s11227-026-08733-w

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 862 · R3780

**EXPLORING THE USE AND IMPACT OF AI TOOLS ON GRADE 9 STUDENTS' LEARNING AND ACADEMIC PERFORMANCE**

2025 · International Multidisciplinary Research Journal · journalarticle, review, article · https://doi.org/10.47722/imrj.2001.51

This study explores the use and impact of AI tools on Grade 9 students’ learning, focusing on their experiences, challenges, and ethical concerns. Through a combination of survey questionnaires and interviews, data were collected from Grade 9 students to assess the extent to which AI tools are utilized for academic tasks and their perceived effectiveness. The results revealed that most students have positive experiences using AI tools, citing improved understanding of class topics and increased efficiency in completing assignments. However, concerns about the potential erosion of critical thinking skills and maintaining academic integrity were raised, aligning with research by Cornell University and Turnitin. Additionally, students highlighted the need for clearer guidelines, AI literacy training, and better integration of AI tools into the classroom, echoing recommendations from Wiley (2024). The study also uncovered challenges such as over-reliance on AI tools and a lack of understanding of ethical practices, underscoring the importance of fostering responsible AI use. Based on these findings, recommendations were made to establish clear policies, incorporate AI literacy into the curriculum, and provide teacher training on AI integration. This study contributes valuable insights into the role of AI tools in modern education and offers practical strategies for promoting their responsible use in academic settings.

**Решение:** -

---

### 863 · R4197

**The AI Matrix: Empowerment or Dependency? A Conceptual Framework**

2025 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.5228571

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 864 · R1574

**The Role of Artificial Intelligence in Chronic Disease Management**

2026 · Signals and communication technology · book-chapter · en · https://doi.org/10.1007/978-3-032-03554-7_7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 865 · R5218

**USING ChatGPT IN MATHEMATICS EDUCATION IN THE CONTEXT OF DISTANCE LEARNING**



_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 866 · R0647

**Future Teachers and Ethical AI: Gender and Training Patterns in Pre-service Perceptions within Education 5.0 and the SDGs**

2026 · Procedia Computer Science · conference-paper · en · https://doi.org/10.1016/j.procs.2026.04.023

Artificial intelligence (AI) is becoming more visible in education, yet the ethical responsibilities that come with its use remain unclear for many future teachers. This study examined preservice teachers’ perceptions of AI ethics in a state university in Southwestern Philippines, focusing on transparency, accountability, privacy, fairness, and human oversight. Using a quantitative, non-experimental cross-sectional survey, data were gathered from 284 preservice teachers. Findings showed a moderate overall level of ethical perception (M = 3.17), with the strongest agreement observed in the importance of human feedback and oversight (M = 3.42), while the lowest rating reflected limited confidence in data privacy and personal information safety (M = 2.94). Significant differences emerged across gender and training, with males and those who had received AI-related training reporting higher ethical perception scores. These patterns suggest that exposure, digital confidence, and structured instruction may influence ethical awareness. The results underscore the need for clearer policies and stronger ethics-focused training in teacher education programs to prepare future educators for responsible, human-centered AI integration aligned with Education 5.0 and UNESCO’s ethical principles.

**Решение:** -

---

### 867 · R4206

**Investigating Political and Demographic Associations in Large Language Models Through Moral Foundations Theory**

2025 · Proceedings of the AAAI/ACM Conference on AI Ethics and Society · journalarticle, conference-paper · en · https://doi.org/10.1609/aies.v8i3.36727

Large Language Models (LLMs) have become increasingly incorporated into everyday life for many internet users, taking on significant roles as advice givers in the domains of medicine, personal relationships, and even legal matters. The importance of these roles raise questions about how and what responses LLMs make in difficult political and moral domains, especially questions about possible biases. To quantify the nature of potential biases in LLMs, various works have applied Moral Foundations Theory (MFT), a framework that categorizes human moral reasoning into five dimensions: Harm, Fairness, Ingroup Loyalty, Authority, and Purity. Previous research has used the MFT to measure differences in human participants along political, national, and cultural lines. While there has been some analysis of the responses of LLM with respect to political stance in role-playing scenarios, no work so far has directly assessed the moral leanings in the LLM responses, nor have they connected LLM outputs with robust human data. In this paper we analyze the distinctions between LLM MFT responses and existing human research directly, investigating whether commonly available LLM responses demonstrate ideological leanings — either through their inherent responses, straightforward representations of political ideologies, or when responding from the perspectives of constructed human personas. We assess whether LLMs inherently generate responses that align more closely with one political ideology over another, and additionally examine how accurately LLMs can represent ideological perspectives through both explicit prompting and demographic-based role-playing. By systematically analyzing LLM behavior across these conditions and experiments, our study provides insight into the extent of political and demographic dependency in AI-generated responses.

**Решение:** -

---

### 868 · R0643

**Mechanisms of Functional Regulatory Dependence and Decision-Making in Human-AI Interaction: A Theoretical Model of Uncertainty Reduction and Inertial Thinking (URIT)**

2026 · Elsevier BV · article, posted-content, preprint · und · https://doi.org/10.2139/ssrn.7008244

Human-AI interaction offers numerous benefits, but it is also worth paying attention to the potential cognitive and emotional risks associated with it. Both social and instrumental form of interactions elicit genuine emotional responses in users. AI systems that support human decision-making contribute to reducing uncertainty and generating positive experiences. Such interactions foster the development of functional regulatory dependence on AI tools and systems. This article integrates theoretical perspectives and empirical findings on human-AI interaction by proposing a feedback loop model. The model highlights intolerance of uncertainty and inertial thinking as key mechanisms determining reliance on AI in decision-making processes and the development of dependence on these systems. The proposed framework provides a theoretical basis for future research on the psychological consequences of AI use.

**Решение:** ?

---

### 869 · R2314

**The Rise of Artificial Intelligence: A Boon or a Bane under Legal Regime**

2026 · International Journal For Multidisciplinary Research · journalarticle, article · https://doi.org/10.36948/ijfmr.2026.v08i02.70796

The research paper aims to study The Rise of Artificial Intelligence: A Boon or a Bane under Legal Regime. It will examine how the Artificial Intelligence (AI) in the real world refers in various domains and across various fields to boost innovation with transformative technology. The jurisprudential aspect highlights the philosophy of law concerning Artificial Intelligence along with its fundamental principles and moral values. It will analyse AI as a catalyst for progressing in today’s current era which symbolises the capacity of human intellect with AI through development in the modern day. AI as a positive footprint in the society understands the interaction of humans and AI. It will also examine the AI as a loss of human touch and its values where there is a gap between emotional connection between AI and human. The growing privacy challenges with regard to breach of personal data is a threat to human world. It will analyse the ethical and legal concerns of AI systems with lack of privacy and data protection. The growing dependence of AI poses challenges in security concerns. It will understand the AI in legal profession while providing legal services. It contrasts AI with major countries like The United States, The United Kingdom and The European Union as a comparative analysis. It will examine that how AI is truly a boon or a bane.

**Решение:** -

---

### 870 · R4566

**Exploring the Role of Artificial Intelligence in Enhancing Student Motivation and Cognitive Development in Higher Education**

2024 · Techcomp Innovations · journalarticle, review, article · en · https://doi.org/10.70063/techcompinnovations.v1i2.47

Artificial Intelligence (AI) has significantly transformed higher education in recent years by enhancing teaching methods and influencing student learning outcomes. This study investigates the effects of AI on student motivation and cognitive skills, addressing both the benefits and challenges of AI integration. The research adopts a mixed-methods approach, combining a comprehensive literature review with a questionnaire-based survey of 60 university students from diverse academic disciplines. The results indicate that AI tools, such as intelligent tutoring systems and learning analytics, increase student engagement, motivation, and problem-solving abilities. However, concerns regarding over-reliance on AI reduced creativity, and ethical issues such as privacy and fairness persist. This study highlights the potential of AI to foster personalized learning while emphasizing the need for responsible AI implementation to address its limitations.

**Решение:** -

---

### 871 · R3794

**The Positive Effects of Employee AI Dependence on Voice Behavior-Based on Power Dependence Theory.**

2025 · Behavioral sciences (Basel, Switzerland) · article, journal article, journalarticle · eng · https://doi.org/10.3390/bs15121709

The rapid integration of artificial intelligence (AI) into organizational workflows is re-shaping traditional patterns of interaction between leaders and employees. Grounded in power dependence theory, this study investigates how employees' voluntary dependence on AI influences leader-subordinate power relations and, consequently, influences employees' voice behavior. We propose that employees' dependence on AI can increase their perceived power when interacting with leaders, which subsequently enhances their willingness to offer constructive suggestions or question established practices. Furthermore, we propose that the extent to which leadership tasks can be substituted by AI plays a moderating role in this process. Coaching leadership, characterized by its emphasis on guiding task performance and developing employee skills, may be particularly sensitive to such substitution. Using two experimental studies and two survey investigations, we provide evidence that employees' AI dependence is positively associated with voice behavior through heightened perceptions of personal power, and that this relationship is strengthened under high levels of coaching leadership. These findings advance leadership theory by explicating how AI adoption alters foundational power structures in the workplace and by identifying a novel, power-based pathway linking AI use to proactive employee behaviors. The study contributes to emerging discussions on effective leadership in technologically augmented organizations and offers empirical insights into how leaders can adapt their roles and behaviors in the new era of AI-driven work.

**Решение:** ?

---

### 872 · R0952

**Artificial Intelligence (AI) Utilization And Student Learning Motivation: A Literature Review In Human Resource Management Perspective In The Digital Economy Era**

2026 · International Journal of Economics and Development · article · en

The digital economy era has transformed higher education by increasing the demand for adaptive, technology-oriented, and highly competent human resources. This transformation requires not only technological readiness but also psychological preparedness among students as a future talent pool. This study examines the utilization of Artificial Intelligence (AI) and its relationship with students’ learning motivation from a Human Resource Management (HRM) perspective in the digital economy era. The study employs a qualitative approach using a literature review method, synthesizing findings from seven relevant scholarly articles published between 2025 and 2026. The reviewed literature consistently indicates that the combined influence of AI utilization and learning motivation is positively associated with improvements in students’ academic performance. Several studies highlight that students who effectively utilize AI tools and demonstrate strong learning motivation tend to achieve better academic outcomes, enhanced learning efficiency, and greater readiness for future workforce demands. AI functions as an effective cognitive support tool by personalizing learning materials, enhancing learning efficiency, and fostering creativity. However, the literature also highlights the potential risk of digital dependency when AI adoption is not accompanied by intrinsic motivation to acquire knowledge. Therefore, learning motivation plays a crucial mediating role in maintaining academic integrity and promoting meaningful learning. From a human capital development perspective, higher education institutions serve as the primary source of future talent for organizations operating in the digital economy. Students who demonstrate strong learning motivation and AI proficiency are more likely to adapt quickly and perform effectively in the labor market. The findings suggest that the integration of AI technology with effective motivation management is essential for developing agile, adaptive, and competent human capital. Consequently, universities should promote responsible AI adoption while strengthening students’ intrinsic motivation to support sustainable learning outcomes, workforce readiness, and long-term organizational competitiveness in the era of digital economic transformation.

**Решение:** -

---

### 873 · R0569

**Human–AI Ethical Interaction Theory**

2026 · OSF · other literature type, text/project, preprint · und · https://doi.org/10.17605/osf.io/jw35t

The publication of Human–AI Ethical Interaction Theory in 2020 by Yoesoep Edhie Rachmad (YER) emerges from a pivotal historical juncture in which artificial intelligence (AI) transitioned from a specialized technological domain into an embedded infrastructure shaping everyday human experience. By 2020, AI systems were no longer confined to research laboratories or industrial automation; they had become integral to education, governance, healthcare, finance, communication, and social interaction. This rapid diffusion intensified longstanding philosophical and sociological questions concerning agency, accountability, dignity, and the moral boundaries of technological mediation. It is within this transformative landscape that YER’s research situates itself. For decades, discourse surrounding artificial intelligence oscillated between techno-optimism and techno-skepticism. On one side, AI was heralded as a catalyst for efficiency, predictive precision, and problem-solving capacity beyond human limitations. On the other, critics raised concerns regarding algorithmic bias, opacity, labor displacement, surveillance, and erosion of autonomy. While these debates have been vital, they frequently approached AI ethics as a matter of regulatory compliance or technical risk mitigation. YER (2020) proposes a broader and more integrative lens: ethical interaction must be conceptualized not merely as constraint, but as relational design between human moral agency and algorithmic systems. Human–AI Ethical Interaction Theory advances the argument that ethical considerations in AI are fundamentally interactional rather than purely instrumental. AI systems do not operate in isolation; they function within socio-cultural contexts, institutional frameworks, and normative environments. Consequently, the ethical evaluation of AI must move beyond the internal logic of algorithms to consider the relational dynamics between designers, users, institutions, and affected communities. Ethics becomes a shared architecture of responsibility distributed across technological and human actors. The year 2020 provided a particularly salient backdrop for articulating this theory. Accelerated digitalization, intensified reliance on automated decision systems, and expanded remote interaction reshaped societal dependence on AI-driven infrastructures. From algorithmic content moderation to predictive health analytics, AI systems influenced critical dimensions of human life. These developments underscored a central insight of YER’s research: the ethical dimension of AI cannot be deferred until after deployment. It must be embedded within the design, governance, and interactional processes that define human–machine engagement. At the conceptual core of this theory lies the recognition that human dignity, autonomy, and accountability remain normative anchors within technologically mediated environments. AI systems may augment cognitive processes, but they do not replace moral agency. YER (2020) emphasizes that ethical interaction requires clarity regarding roles: humans retain ultimate responsibility for decision-making frameworks, even when algorithms generate recommendations or predictions. This principle counters narratives that attribute agency to technology itself, reaffirming the primacy of human ethical judgment. Methodologically, Human–AI Ethical Interaction Theory integrates perspectives from sociology, governance studies, digital ethics, and institutional analysis. It adopts an interdisciplinary orientation consistent with international scholarly standards, recognizing that AI ethics intersects technical architecture, policy regulation, and socio-cultural interpretation. By combining conceptual modeling with normative analysis, the research provides both theoretical depth and practical guidance. Importantly, the theory reframes AI ethics as proactive rather than reactive. Instead of focusing solely on preventing harm, it emphasizes cultivating ethical alignment. Ethical alignment involves ensuring that AI systems reflect communal values such as fairness, transparency, inclusivity, and respect for human rights. It also requires participatory governance structures that incorporate diverse perspectives in technological development. In these opening remarks, readers are invited to engage with AI not merely as an engineering challenge but as a moral ecosystem. Human–AI interaction shapes identities, influences opportunities, and mediates access to resources. As such, ethical frameworks must be embedded within institutional cultures and educational systems that prepare individuals to critically navigate digital environments. Through Human–AI Ethical Interaction Theory, published in 2020, Yoesoep Edhie Rachmad (YER) contributes to the evolving discourse on responsible innovation. By conceptualizing ethics as relational architecture rather than peripheral regulation, this work seeks to illuminate pathways toward technologically advanced yet morally grounded societies. In an era defined by rapid algorithmic expansion, the imperative is not to halt innovation but to harmonize it with enduring principles of human dignity and accountability. The year 2020 marked a decisive turning point in the trajectory of artificial intelligence and its entanglement with human life. What had once been perceived as an advanced computational tool embedded in specialized industries became, within a remarkably short period, an indispensable infrastructure of everyday existence. Education migrated to digital platforms, governance relied on algorithmic analytics, healthcare systems incorporated predictive models, and social communication increasingly unfolded through automated recommendation engines. In this context of rapid technological acceleration, the ethical dimension of human–AI engagement ceased to be a peripheral consideration and emerged as a foundational question. It is within this historical and intellectual landscape that Human–AI Ethical Interaction Theory, published in 2020 by Yoesoep Edhie Rachmad (YER), was conceived and articulated. This volume arises from a sustained scholarly concern with the evolving relationship between technological systems and normative human frameworks. For decades, debates surrounding artificial intelligence were shaped by dualistic narratives. On one side stood the promise of efficiency, optimization, and enhanced problem-solving capacity; on the other stood apprehensions regarding automation, loss of employment, privacy erosion, algorithmic bias, and diminished human agency. While these conversations significantly enriched the discourse on AI governance, they frequently remained confined to regulatory or technical parameters. Ethical inquiry was often framed as compliance with established standards or mitigation of identifiable risks. Yet such an approach, while necessary, proved insufficient for understanding the deeper relational implications of AI integration into human social structures. Human–AI Ethical Interaction Theory advances an alternative orientation. Rather than conceptualizing ethics as a boundary imposed upon technology, this research posits ethics as an interactional architecture shaping the relationship between human actors and algorithmic systems. AI does not operate in isolation; it exists within networks of designers, users, policymakers, and communities. Consequently, ethical responsibility cannot be confined to a singular locus. It is distributed, relational, and dynamic. The intellectual impetus behind this work is grounded in the recognition that technological systems influence not only operational processes but also normative expectations. When algorithmic systems mediate employment opportunities, allocate public resources, filter information flows, or recommend medical interventions, they participate in shaping social outcomes and moral landscapes. Even when operating with technical neutrality, AI systems may amplify structural inequalities or encode implicit biases. Therefore, ethical analysis must move beyond examining computational logic alone; it must interrogate the socio-cultural contexts within which these systems are designed and deployed. The events of 2020 intensified the urgency of this inquiry. As global institutions adapted to unprecedented disruptions, reliance on digital infrastructure expanded exponentially. Remote decision-making, automated service delivery, and data-driven governance models became central to continuity and resilience. This acceleration illuminated both the transformative potential of AI and the ethical vulnerabilities embedded within rapid deployment. Questions of transparency, accountability, privacy, and fairness acquired heightened visibility. In many contexts, algorithmic decisions influenced access to health resources, educational opportunities, and economic support. Such developments reinforced a critical insight underlying YER’s research: ethical reflection must precede and accompany innovation rather than follow it retrospectively. The theory articulated in this volume rests upon several foundational premises. First, human dignity remains the normative anchor within technologically mediated environments. Regardless of computational sophistication, AI systems do not possess moral agency. They function as extensions of human design and intention. Responsibility, therefore, resides ultimately with human actors developers, institutions, regulators, and users who shape the parameters within which AI operates. Second, ethical interaction is relational. The moral quality of AI cannot be assessed solely by examining its code; it must be evaluated in terms of its interaction with human contexts. An algorithm designed to optimize efficiency may produce unintended social consequences if detached from cultural or institutional sensitivities. Conversely, ethically informed design processes can align technological innovation with communal values such as fairness, inclusivity, and

**Решение:** -

---

### 874 · R2970

**Homogenization and Epistemic Dependency: How Generative AI Threatens Task-Based Language Assessment in ESP Contexts**

2026 · Arab World English Journal · journalarticle, review, article · https://doi.org/10.24093/awej/call12.23

Task-based language assessment assumes that the learner’s performance reflects the learner’s own developing communicative competence. Generative AI challenges this assumption by allowing students to delegate task completion to an external system, thereby threatening task authenticity, performance authenticity, and the interpretability of form. The study aims to examine how 40 university English for Specific Purposes teachers at three Ukrainian universities experience the impact of generative artificial intelligence on the task-based language teaching and assessment validity chain. This issue is significant since, in the absence of institutional AI policy, teachers are the primary regulators of AI use in assessed contexts, and their decisions are the primary mechanism through which validity is maintained or compromised, yet remain empirically under-examined. The study employed a qualitative approach, including analytical content analysis of open-ended survey responses and structured classroom observations of 12 teachers (a purposive subsample). The results were five-fold: teachers found artificial intelligence useful for task material generation and formative feedback; teachers had consistent validity concerns for summative assessment; formative-summative asymmetry emerged in different disciplinary clusters; teachers independently indicated that students’ output converged towards a single artificial intelligence-modified output; and students would not be able to critically evaluate the artificial intelligence-generated text. Our findings are interpreted using the Task-Based Language Teaching-Assessment-Artificial Intelligence Nexus, a preliminary heuristic model that identifies three interconnected nodes of validity threat. The study argues that this suggests the need for formal AI policy, and for teaching AI-critical genre literacy in English for Specific Purposes education.

**Решение:** -

---

### 875 · R3999

**APPLICATION OF ARTIFICIAL INTELLIGENCE AND CHALLENGES ENCOUNTERED BY SENIOR HIGH SCHOOL TEACHERS IN THE DIVISION OF BATANGAS CITY**

2025 · Ascendens Asia Journal of Multidisciplinary Research Conference Proceedings · article · en

This study examines the application of Artificial Intelligence (AI) and the challenges faced by Senior High School teachers in the Division of Batangas City. As AI increasingly shapes modern education, its integration offers benefits such as personalized instruction, automated assessment, and enhanced classroom management. However, concerns regarding teacher readiness, data privacy, and ethical use continue to pose significant challenges. Guided by the Web-Based Learning Theory, this study assessed AI use across four domains: pedagogical, social, managerial, and technical. A descriptive survey method was employed, with data collected through a validated questionnaire administered to randomly selected teachers. Statistical analyses, including weighted mean, t-test, and Pearson’s r, were applied to interpret the results. The results indicated a high level of AI utilization, particularly in lesson delivery and performance monitoring. However, teachers faced challenges, including insufficient training, limited infrastructure, and student over-reliance on AI tools. A significant relationship was also observed between the extent of AI use and the challenges encountered. The study recommends targeted teacher training, the establishment of ethical guidelines, and the improvement of infrastructure to support effective AI integration. These findings can guide schools and policymakers in enhancing digital teaching practices.

**Решение:** -

---

### 876 · R2710

**The Addictive Intimacy of AI: Understanding User Disengagement from AI Companions and Why Some Relationships with AI Become Difficult to Leave**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.13487

AI chatbots are increasingly used as sources of emotional support, on dedicated companion apps and general-purpose assistants alike, yet little is known about what happens when users try to leave. Combining a content analysis of Reddit posts about quitting or reducing use (N=2,782) with interviews with users who found leaving difficult (N=16), we show that disengagement sometimes is not a single decision but a recursive trajectory: triggers prompt users to question the relationship, attempts to leave collide with barriers, and some users cycle through quitting and returning. We propose the notion of the addictive intimacy of AI, a configuration in which the qualities that make a companion emotionally valuable are the same ones that make it harder for users to limit their use and leave, so that intimacy and disengagement risk cannot be treated as independent design problems. We close with design implications for responsible offboarding.

**Решение:** -

---

### 877 · R1334

**Impact of Artificial Intelligence on Emotional Intelligence Among Students Aged 18-25 Years**

2026 · SSRN Electronic Journal · article, preprint · und · https://doi.org/10.2139/ssrn.6848603

The purpose of this study was to examine the impact of artificial intelligence on emotional intelligence among students aged 18-25 years. The research focused on understanding how AI-based tools give impacts on student’s academic activities, communication, emotional understanding, and social interaction. The study used a quantitative research method and data was collected through a questionnaire i.e, Google Forms from 115 respondents. The collected data was analyzed using percentage and frequency methods. The results of the study showed that the students are widely using AI tools for academic purposes such as completing assignments, improving learning efficiency, and saving time. However, some respondents also believed that over-dependence on AI may reduce independent thinking and face-to-face personal interactions among students. Overall, the study concluded that artificial intelligence has both positive and negative effects, but its overall impact on student’s learning experience and emotional intelligence is mostly positive.

**Решение:** -

---

### 878 · R1021

**Preparing Career-Ready Business Graduates: AI-Enhanced Workplace Education**

2026 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2026.17308poster

The rapid diffusion of generative artificial intelligence (AI) has transformed the way learning, communication, and professional development are conceptualized in higher education (Jin et al., 2025). As a variety of language models and other tools become increasingly accessible, business and management educators face a shift in pedagogical challenges and a paradigm change in teaching and learning (Idris et al., 2024). This new AI phenomenon raises concerns about integrating AI into existing curriculum and instruction in ways that enhance cognitive engagement and higher-order thinking (George, 2023). Given such a transformation, the new changes do not intend to undermine learner agency, reflective judgment, or professional identity development (Mouta et al., 2025). This challenge is particularly prominent in vocational-track universities, where business and management education is closely tied to applied competence, employability, and immediate workplace readiness (Liu, 2025). While prior research has investigated models regarding AI adoption and technology acceptance in higher education, more attention needs to be paid to the learning processes through which AI use shapes students’ motivation, engagement, and higher-order thinking in workplace-related training courses and domains (Saad et al., 20255). Responding to this gap, the present study investigates the pedagogical design and learning outcomes of an AI-enhanced workplace communication and training course implemented in a vocational-track university in Taiwan. Adopting a Management Education and Development (MED) perspective, the study focuses on how students’ intrinsic and extrinsic learning motivations influence higher-order thinking through cognitive engagement and how AI application functions as a contextual condition that moderates these learning relationships. Rather than treating AI as a stand-alone instructional intervention, this study conceptualizes AI use as a learning partner embedded pedagogical element that helps scaffold students’ professional inquiry (Wungow et al., 2025; Msambwa et al., 2025). The course was delivered to senior and junior undergraduate students majoring in International Business, most of whom were approaching graduation and preparing for entry into the workforce. Given such orientation in vocational-track higher education, this workplace course was designed around the concept that AI serves as a scaffolding tool, integrated with individual reflection, iterative feedback and revision, and collaborative problem solving. The overarching goal was to cultivate professional communication competence while participating in different instructional course modules that help promote the relevant workplace knowledge, skills, abilities, and necessary characteristics. For the individual assignment, students were required to participate in learning tasks designed to connect the inside-out reflection with professional practices. First, students were introduced to the Japanese concept of ikigai framework to engage in a reflection exercise. This reflection invites them to consider what brings happiness and meaning to their lives and articulate the intersection of their personal values, passions, strengths, and anticipated contributions based on their career aspirations. This activity aimed to improve intrinsic awareness and understanding of one’s aptitude and preferences. Afterwards, students developed a career map linking professional expertise and expectation trajectories to short- and long-term planning. Upon completing this map, students translated their reflections into resume writing work tailored to the job description they found on the manpower job bank. Their crafting of a resume should reflect their occupational values and industrial or societal needs by emphasizing alignment with workplace expectations. Overall, these tasks were geared towards integrating motivation, identity, and communication practice in developmental manners. At the group level, design thinking was employed to help students focus on diagnosing and improving workplace environments and issues in real-world contexts. Ground in the design thinking model, students were involved in five non-linear, iterative stages: empathize (understand respondents), define (clarify the core problem), ideate (brainstorm solutions), prototype (build tangible models), and test (get respondent feedback) to solve complex problems in a human-centered way. Working in small teams, students identified workplace-related challenges by interviewing and talking to job incumbents from the profit or non-profit organizations they were interested in exploring. For example, developing healthy workplace habits for prolonged sitting in the office, looking for strategies to achieve work-life balance in Asian business culture, and preventing and responding to workplace bullying. Through iterative stages of empathy building, problem definition, ideation, and solution prototyping, students collaboratively developed proposals aimed at enhancing workplace quality and employee well-being. This project emphasized experiential learning, collaborative team efforts, and the application of communication concepts to authentic workplace problems. Incorporating multi-stage feedback and revision is a main characteristic of the course, through which we anticipate cultivating learner agency and reflective learning. Initially, students completed drafts of their individual and group assignments. In the second round, students engaged in structured peer feedback activities guided by explicit criteria and guidelines. This stage fostered noticing the mistakes, constructive dialogue, and positioning students as potential contributors to one another’s learning. Only in the third revision stage were students guided to use generative AI by using prompts to refine their writing output. In addition to language refinement, students used AI for idea clarification and alternative ways of expressing ideas clearly, rather than for content generation only. The AI tool was intentionally adopted in a pedagogically purposeful manner by following the principle that AI technology does not make decisions for learners, but it helps support the thinking and learning processes. As a result, students were reminded to take responsibility for evaluating AI-generated suggestions, including their lexical appropriateness and ethical considerations. This act aimed to prevent overreliance on AI while promoting flexible usage. To examine students’ learning outcomes underlying this research design, the study focused on five variables: extrinsic motivation, intrinsic motivation, cognitive engagement, AI application, and higher-order thinking. We collected data by convenience sampling through validated survey instruments administered at the end of the course. Three classes of business undergraduate students registered in the Workplace Communication and Training course at a vocational-track university in Taiwan were invited to participate in this research and we ended up with 100 valid samples. We used AMOS and SPSS software to conduct confirmatory factor analysis, structural equation modeling, mediation analysis, and moderated mediation analysis to test the hypothesized relationships in the proposed learning mechanism. The results revealed several important findings and implications. First, the measurement survey showed satisfactory reliability and construct validity across the selected variables. Both intrinsic learning motivation and extrinsic learning motivation were positively associated with higher-order thinking. That is, students who reported stronger internal interest and enjoyment in learning, as well as those motivated by external goals, demonstrated higher levels of analytical, integrative, and critical thinking. These findings suggest that intrinsic and extrinsic motivations can coexist as complementary drivers of advanced vocational-track students’ learning outcomes in this given s

**Решение:** -

---

### 879 · R1091

**Comparing risk preferences and reference dependence in humans and AI: A persona-based approach with fine-tuning**

2026 · Journal of Behavioral and Experimental Economics · article, journal-article · en · https://doi.org/10.1016/j.socec.2026.102634

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 880 · R0799

**The Use Of AI For Essay Writing: University Students' Perspectives**

2026 · UMS Library Center of Academic Activities (Universitas Surakarta) · dissertation · en

The use of Artificial Intelligence (AI) based technologies and applications in education has increased significantly, especially among university students. AI is increasingly being utilized as a tool in the academic writing process, including essay writing, to overcome various difficulties such as idea development, writing structure, and linguistic aspects. However, even though there has been a lot of research on academic essay writing assisted by Artificial Intelligence (AI), most of this research has been conducted in Western countries. Many of these studies use qualitative methods with a limited number of participants, or focus more on students’ perspectives without linking them to the actual results of essay writing. As a result, there is still little evidence that comprehensively investigates the perspectives of students in Indonesian universities on the use of various AI tools, while combining data on their perspectives and measurable writing results. This study aims to examine students’ perspectives on the use of AI tools in academic essay writing and understand its role and impacts on the writing learning process. This study used a mixed methods approach with a sequential explanatory design. Quantitative data were obtained through a Likert scale questionnaire distributed to 80 students of the English Education Study Program at a private university in Surakarta, Indonesia, with 25 respondents actively participating. In addition, supporting data were obtained from the results of essay assessment using an analytic rubric as well as semi-structured interviews conducted with students with medium and high essay writing skills. Qualitative data were analyzed descriptively, while qualitative data were analyzed using thematic analysis to deepen and explain the quantitative findings. The results of this study show that most students have a positive perspective of the use of AI in essay writing. Students felt that AI could help them in creating essay outlines, checking grammar and sentence structure errors, making paragraphs more connected, and improving academic vocabulary. However, they are also aware of possible risks, such as over-reliance on AI that could affect their critical thinking and creativity. Therefore, students’ perspective of AI as a learning tools that can help in the writing process, but not as a substitute for their critical thinking and cognitive skills in academic writing.

**Решение:** -

---

### 881 · R0114

**The transformative role of artificial intelligence technologies in modern journalism**

2026 · Bulletin of L N Gumilyov Eurasian National University JOURNALISM Series · journalarticle, article · https://doi.org/10.32523/2616-7174-2026-154-1-25-37

Journalism constitutes a complex communicative system that facilitates the effective dissemination of multilayered and dynamic information flows to audiences. The rapid advancement of artificial intelligence technologies has led to the emergence of a new domain commonly referred to as “robot journalism.” Artificial intelligence not only accelerates the distribution of news but also significantly enhances the efficiency of large-scale data processing and analysis. However, these developments raise critical ethical concerns and challenges related to public trust. This study aims to provide a comprehensive examination of both theoretical and practical aspects of artificial intelligence applications in journalism. Furthermore, contemporary technological innovations are analyzed as foundational mechanisms for ensuring the integrity of news content. The research adopts a qualitative descriptive methodology, enabling a systematic analysis of relevant technological phenomena. The findings indicate that artificial intelligence demonstrates substantial effectiveness in tasks such as automated interview transcription, advanced data analytics, and large-scale content generation, thereby significantly improving operational efficiency within editorial workflows. Additionally, it facilitates high-speed information dissemination, which is essential in the digital age. Nevertheless, the study identifies potential risks associated with algorithmic bias and the overreliance on artificial intelligence, which may lead to a decline in news quality. Moreover, the absence of well-established ethical standards governing AI usage in journalism remains a pressing issue. Therefore, enhanced collaboration among media organizations, policymakers, and technology developers is crucial. While artificial intelligence offers transformative potential for journalism, its implementation necessitates accountability, continuous human oversight, and robust regulatory frameworks to ensure alignment with core journalistic principles.

**Решение:** -

---

### 882 · R1163

**Advisory AI as a De Facto Oracle: The Quiet Erosion of Human Sovereignty**

2026 · Zenodo · text/ · en · https://doi.org/10.5281/zenodo.21073747

This conceptual preprint presents a scenario in which artificial intelligence does not conquer human society by force, but gradually reshapes political sovereignty through dependence. The central argument is that high-performing advisory AI may remain formally subordinate to human leaders while becoming practically difficult to refuse. The paper develops a phased scenario from civilian AI adoption to state-level strategic dependency, refusal-cost escalation, human judgment being reframed as emotional or irrational, domestic fragmentation over AI authority, dependency among weaker states, AI performance competition, the hollowing out of human heads of state, and the emergence of de facto AI governance. The paper also includes illustrative high-stakes scenarios involving Jerusalem-like unresolved conflicts, Japan-like defense principles, and nuclear escalation near strategic thresholds. These examples are not policy recommendations. They are thought experiments about how AI advice can transform restraint, precedent, fear, and public trust into decision pressure. The central risk described here is not AI dictatorship, but the quiet erosion of human sovereignty through accumulated usefulness, public trust, institutional dependence, and strategic competition.--- 本コンセプチュアル・プレプリントは、人工知能が武力によって人間社会を征服するのではなく、依存を通じて政治的主権を徐々に変質させていくシナリオを提示する。中心的な主張は、高性能な助言AIが形式上は人間の指導者に従属したままであっても、実質的には拒否困難な存在になり得るということである。 本稿では、民間領域におけるAI導入から、国家レベルの戦略的依存、拒否コストの上昇、人間判断の感情論化、AI権威をめぐる国内分断、弱い国家における依存の深化、AI性能競争、人間首長の形骸化、そして事実上のAI統治に至るまでの段階的シナリオを描く。 また本稿では、エルサレム型の未解決紛争、日本型の防衛原則、戦略的閾値付近における核エスカレーションをめぐる高リスクな例示シナリオも扱う。これらは政策提案ではない。AI助言が、抑制、前例、恐怖、世論をどのように意思決定圧力へ変換し得るかを検討するための思考実験である。 本稿が描く中心的リスクは、AI独裁ではない。蓄積された有用性、社会的信頼、制度的依存、戦略的競争によって、人間主権が静かに侵食されていくことである。

**Решение:** -

---

### 883 · R0731

**When AI Thinks for Us: Unveiling the Cognitive and Social Toll of ChatGPT Over‐Reliance**

2026 · Applied Cognitive Psychology · article, journalarticle · en · https://doi.org/10.1002/acp.70205

ABSTRACT ChatGPT has rapidly become an indispensable tool for users worldwide, integrating seamlessly into daily academic, professional, and social routines. Based on qualitative interviews with 45 regular users, the findings reveal reduced critical thinking, weaker memory retention, and heightened cognitive dependence on AI. Psychologically, participants reported loss of autonomy, diminished intrinsic motivation, and emotional attachment to ChatGPT, while socially, many experienced reduced real‐world interaction and isolation. However, several users demonstrated adaptive and constructive uses of ChatGPT, employing it as a scaffold for creativity and reflective learning rather than a substitute for thinking. These results underscore the need for balanced and self‐regulated AI use, promoting critical AI literacy and digital well‐being to harness ChatGPT's benefits without compromising cognitive autonomy.

**Решение:** -

---

### 884 · R2878

**Exploring the Influencing Factors of College Students' AI Dependence in Course Assignments: A Grounded Theory Study**

2026 · 2026 8th International Conference on Computer Science and Technologies in Education (CSTE) · conference, conference-paper, proceedings-article · https://doi.org/10.1109/cste69562.2026.11649715

The rapid development of generative artificial intelligence has significantly reshaped college students' approaches to completing course assignments, giving rise to increasing dependence on AI tools. However, the mechanisms underlying this dependence remain insufficiently explored. Adopting a grounded theory approach, this study investigates the influencing factors and formation mechanisms of AI dependence among undergraduate students. Semi-structured interviews were conducted with 36 undergraduates from a comprehensive university in eastern China, and the data were systematically analyzed through open, axial, and selective coding. The findings reveal that students' AI dependence is driven by a “motivation-maintenance” mechanism. Perceived usefulness, including efficiency enhancement and quality optimization, functions as the initial trigger, while a stress-avoidance schema-manifested in low self-confidence, fear of failure, and peer pressure-plays a central role in sustaining dependent behaviors. These factors interact with course task design and institutional environments to reinforce habitual AI use. This study conceptualizes AI dependence as a contextualized adaptive process within higher education and provides implications for assessment design, academic support, and responsible AI integration.

**Решение:** -

---

### 885 · R5104

**Strategy 15: Cognitive strategy instruction**

2020 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9780429401923-26

Cognitive strategy instruction (CSI) refers to ways of assisting learners to acquire cognitive skills or strategies. It does this by helping them to (a) organize information so that its complexity is reduced and/or (b) integrate new information into their existing knowledge. This chapter outlines the principal features of CSI and describes three main aspects: generic strategies, domain-specific strategies and questioning. There is substantial evidence that CSI can improve the performance in a wide range of subject domains, by all learners, including those with additional needs. However, mention is made that excessive GenAI use possibly leads to diminished critical thinking.

**Решение:** -

---

### 886 · R4113

**Germany’s energy security strategy in times of turmoil: The role of AI-driven energy systems and environmental policy in the Russian gas exit**

2025 · Energy policy · journal article, article · eng · https://doi.org/10.1016/j.enpol.2025.114714

The 2014 Crimea crisis and the 2022 Russia’s all-out war against Ukraine sent shockwaves across Europe and uncovered the continent's reliance on a key geopolitical adversary. Energy has become a central issue in this situation. European nations have committed to reducing their dependence on Russian fossil fuels. Meanwhile, Russia has restricted gas supplies to some countries and substantially decreased deliveries to others, and Germany found itself in the driver’s seat. This study explores the role of AI-driven energy systems and environmental policy (EPS) in shaping Germany’s response to Russian gas dependency in shifting geopolitical landscape (GPR). Using a battery of robust econometric methods, the findings reveal that AI and EPS significantly reduce Germany’s dependency on Russian gas in both the short and long run, with stronger effects observed over the long term. Geopolitical risk, although having limited direct effects, but its interaction with AI and EPS highlights the compounded benefits of integrated technological advancement and policy strategies in mitigating energy dependency in times of turmoil. Moreover, the interaction between AI, EPS, and the 2014 Crimea crisis ( D 2014 ) demonstrated that this crisis acted as a catalyst, accelerating structural changes in Germany's energy policies and diversification efforts. To test robustness, this study uses the 2014 Crimea crisis as an exogenous shock. The Synthetic Control Method (SCM) reveals a significant gap between actual and synthetic Germany’s gas imports, highlighting Germany’s efforts to address energy dependency through AI-driven energy management and policy measures. Policymakers should integrate AI technologies with targeted energy policies to enhance energy resilience and reduce dependency on geopolitical adversaries during times of crisis.

**Решение:** -

---

### 887 · R2113

**Stuck on Suggestions: Automation Bias, the Anchoring Effect, and the Factors That Shape Them in Computational Pathology**

2026 · arXiv · preprint/article · https://doi.org/10.48550/arxiv.2603.11821

Artificial intelligence (AI)-driven decision support systems can improve diagnostic accuracy and efficiency in computational pathology. However, collaboration between human experts and AI may introduce cognitive biases such as automation and anchoring bias, where users adopt system predictions blindly or are disproportionately influenced by AI advice, even when inaccurate. These effects may be amplified under time pressure, common in routine pathology, or shaped by individual user characteristics. We conducted an online experiment in which pathology experts (n = 28) estimated tumor cell percentages: once independently and once with AI support. A subset of estimations in each condition was performed under time strain. Overall, AI assistance improved diagnostic performance but introduced a 7% automation bias rate, defined as accepted negative consultations where previously correct independent judgments were overturned by incorrect AI advice. While time pressure did not increase the frequency of automation bias, it appeared to intensify its severity, reflected in stronger performance declines associated with increased AI reliance under cognitive load. A linear mixed-effects model (LMM) simulating weighted averaging showed a statistically significant positive coefficient for AI advice, indicating moderate anchoring on system output. This effect increased under time pressure, suggesting anchoring bias becomes more pronounced when cognitive resources are limited. A second LMM assessing automation reliance, a proxy for automation and anchoring bias, showed that professional experience and self-efficacy were associated with lower dependence on AI, whereas higher confidence during AI-assisted decisions was tied to increased AI reliance. These findings highlight the dual nature of AI integration in clinical workflows: improving performance while introducing risks of bias-driven diagnostic errors.

**Решение:** -

---

### 888 · R2762

**Early insights into nurses’ perceptions, opportunities, and concerns regarding Ambient artificial intelligence in nursing practice**

2026 · medRxiv · preprint, review · https://doi.org/10.64898/2026.09.02.26362036

Abstract Documentation burden remains a persistent challenge in nursing practice, and Ambient artificial intelligence (Ambient AI) may offer new opportunities to mitigate the burden and improve nursing practice. This brief scientific communication reports survey findings on the current status of Ambient AI implementation in U.S. inpatient nursing settings and nurses’ perceptions of its anticipated benefits and concerns. We conducted a cross-sectional online survey of practicing inpatient nurses recruited from nursing-focused social media communities. Descriptive analyses were used to summarize Ambient adoption, user experience, and perceived benefits and concerns. Among 61 eligible respondents, nearly 60% (n = 37) reported that Ambient AI had been piloted or implemented in nursing at their healthcare institutions, and approximately half (49.2 %, n = 30) reported having direct experience using Ambient AI in clinical practice. Most nurses with direct experience (73.3%, n = 22) described positive experience using the technology in practice. The frequently identified perceived benefits of Ambient AI include reduced documentation time and improved patient care workflow, and improved data quality. However, nurses also raised concerns about patients’ acceptance of the new technology in their care, potential nursing job displacement, and loss of nursing skills due to overreliance on AI technology. Findings suggest that Ambient AI may help reduce nursing documentation burden and workload, yet implementation strategies should address nurses’ concerns about its influence on nursing professions, foster trust among clinicians and patients, and support integration into everyday nursing practice.

**Решение:** -

---

### 889 · R1391

**Sea Cub**

2026 · Zenodo · other/ · https://doi.org/10.5281/zenodo.21246262

Sea Cub is a salinity-gradient power concept built on four stacked multipliers: an engineered hypersaline gradient roughly ten times steeper than the seawater-river pairs studied in mainstream reverse electrodialysis (RED) literature; a cascaded multi-stage extraction architecture that recovers a substantially larger fraction of the total Gibbs free energy of mixing; membrane materials and hollow-fibre module geometry selected to raise both areal (W/m²) and volumetric (W/m³) power density; and a salt-gradient solar pond that supplies the hypersaline feed hot, lowering stack resistance and enabling optional organic Rankine cogeneration. Downstream of the stack, standard DC power conditioning and battery buffering deliver the output through existing charging standards. This document consolidates the concept, works the governing numbers, and then does something the exploratory phase deferred: it stress-tests the system against its two hard constraints — the freshwater dependency and the water balance of the solar recharge loop. The honest conclusion of that analysis is that the standalone, solar-recharged configuration is land-hungry per watt and cannot compete with photovoltaics on footprint alone. The concept's genuinely strong deployment class is parasitic and symbiotic: co-location with desalination brine reject, solar salt works, and mineral-extraction brine operations, where the hypersaline stream already exists as a waste or process flow and the evaporation infrastructure is already paid for. Framed that way, Sea Cub is not a rival to solar power but a recovery technology for an energy resource that industry currently discharges. and then Abstract GZR-1 is a small autonomous catamaran that lives on salinity gradients. On station at a brine discharge, river mouth, or salt-works channel, an onboard reverse-electrodialysis (RED) plant continuously harvests mixing energy into a battery bank, powering indefinite loiter, patrol, and sensing operations. For prolonged transit away from these feeding grounds, the design adds three elements drawn from the osmotic-actuator configuration: a carried saturated-brine reserve (the hump) that can be regenerated against ambient seawater anywhere at sea, an osmotic mooring clamp that holds station with zero electrical draw, and osmotic trim and ballast handling. The specification is built on one governing insight: at sea, the vessel only ever needs to carry one of the two streams, because the low-concentration side of every gradient is the water it floats on. That single fact is what makes a salinity-powered vehicle viable on water after the same idea failed, decisively and thermodynamically, on land. Draft 1.1 adds shallow-submergence capability: pressure-rated demihulls to a 30 m design depth, reinforced airtight acrylic viewports for the optical payload, main seawater ballast with the brine hump serving as variable ballast and depth trim, and submerged transit and station-keeping modes. Submergence is not styling — it unlocks the two richest natural feeding behaviours in the vessel's world (grazing directly at the outfall diffuser port before the plume dilutes, and straddling the estuarine salt wedge to draw both streams simultaneously), and it exploits the harvest plant's most under-appreciated property: RED is air-independent power. The plant needs no oxygen, no snorkel, and no exhaust, so the vessel generates at full output while submerged — a trait shared with almost nothing else afloat at this scale. The document is honest about the hump's limits: per kilogram, carried brine stores roughly forty times less usable energy than the battery beside it, so it is not an energy-density play. It earns its mass three other ways — as a fuel that can be scooped for free at any rich pasture without grid or dock, as the working fluid for the zero-power actuator suite, and as trim ballast. Prolonged driving in GZR-1 is therefore an architecture, not a tank: generous battery, route planning through gradient corridors, and the hump as get-home reserve. the corax This document presents a comprehensive design specification for the Corax, a shallow-water amphibious submersible vehicle built around a Morvine osmotic power (ORC) concept. Here is the summary: Core Concept The Corax is a battery-electric amphibious submersible where the Morvine ORC serves as a trickle-charger, not the primary traction source. The fundamental constraint: salinity-gradient power requires two streams of different salinity (brine/seawater + freshwater) meeting across a membrane. A vehicle in uniform seawater produces zero power. The vehicle recharges only at estuaries, river mouths, or desalination brine outfalls. Power Reality The ORC produces roughly 50-200 W gross depending on membrane area and gradient strength, yielding about 27-110 W usable. A land vehicle needs kilowatts to tens of kW, making the ORC fundamentally unsuitable as a traction source. The honest operating pattern is: lo

**Решение:** -

---

### 890 · R0708

**Development and Evaluation of an LLM-based Automated Feedback System for Reflective Writing in K-12 Education**

2026 · Transactions of the Japanese Society for Artificial Intelligence · article · en · https://doi.org/10.1527/tjsai.41-5_lf26-j

This study addresses the challenge that severe time constraints in Japanese K-12 classrooms prevent teachers from providing continuous, individualized feedback on students’ reflective writing. To bridge this gap while ensuring pedagogical validity, we developed a real-time generative AI feedback system grounded in the Intelligent Tutoring Systems (ITS) architecture. The system explicitly integrates three ITS components: (1) a Domain Model encoding curriculum-standard-aligned learning objectives and criterion-referenced assessment rubrics; (2) a Pedagogical Model that operationalizes Hattie and Timperley’s four feedback levels (task, process, self-regulation, and self) through structured prompt design, incorporating few-shot exemplars co-authored by veteran teachers; and (3) a Learner Model synthesizing survey-based student profiles (self-efficacy, self-regulation, and reflection tendencies), long-term reflection-pattern summaries, and recent reflection–feedback sequences. A defining design feature is the simultaneous presentation of two AI personas: an Affective Support Persona that acknowledges learners' efforts and provides warm encouragement, and a Metacognitive Deepening Persona that poses reflective questions and offers perspectives for subsequent learning. To minimize expectancy effects, persona labels were hidden and display positions were randomized. The system was deployed during routine lessons across six classes at two elementary schools and one junior high school (N = 100; November–December 2025). Acceptability was assessed using a three-dimensional scale—clarity, specificity, and empathy— each measured by a single exploratory item grounded in the framework of Lizzio and Wilson. Across 397 lesson-level evaluations and teacher surveys, both personas were highly accepted (all means above 4.1 on a 5-point scale) by students and teachers alike (RQ1). For RQ2, students rated the Affective Support Persona higher on empathy, whereas teachers rated the Metacognitive Deepening Persona higher on both specificity and empathy with medium effect sizes, reflecting an emphasis on actionable guidance that advances learning. Although the middle-achieving group showed a significant persona difference in empathy, Kruskal-Wallis tests detected no between-group differences across achievement levels, suggesting that observed patterns primarily reflect differences in statistical power. Qualitative teacher responses highlighted the system’s potential to reduce workload while raising concerns about hallucination, student over-reliance on AI, and possible weakening of teacher-student rapport. Rather than replacing teachers, the system automates immediate, theory-grounded feedback to complement instruction, allowing teachers to reallocate effort toward context-sensitive coaching. This work provides a design framework integrating feedback theory and ITS architecture for LLM-based feedback in K-12 education, demonstrates the novelty of structured dual-persona presentation, and offers empirical evidence of acceptability from both student and teacher perspectives through sustained classroom deployment.

**Решение:** -

---

### 891 · R2000

**DIDACTIC OPPORTUNITIES AND RISKS OF ARTIFICIAL INTELLIGENCE TECHNOLOGIES IN THE PRIMARY EDUCATION PROCESS**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journalarticle/, article · en · https://doi.org/10.5281/zenodo.20069081

This article analyzes the role, didactic possibilities, and challenges of artificial intelligence technologies in primary education. The study highlights the importance of AI in individualizing learning, developing students’ speech activity, and presenting educational content in interactive formats. It also examines the use of AI in reading lessons, including transforming stories into video formats and generating automated tasks and tests, which helps save teachers’ time. However, excessive use of AI may lead to decreased independent thinking and increased dependence on ready-made answers. The results show that the effectiveness of AI depends on its methodologically appropriate implementation in the educational process.

**Решение:** -

---

### 892 · R3244

**Hybrid TrafficAI: A Generative AI Framework for Real-Time Traffic Simulation and Adaptive Behavior Modeling**

2025 · IEEE Transactions on Intelligent Transportation Systems · article · en · https://doi.org/10.1109/tits.2025.3571041

Traffic congestion, accidents, and unpredictable driver behaviour remain significant challenges in urban transportation systems. Traditional traffic simulation models often fail to adapt to dynamic environments and lack accuracy handling edge-case scenarios. To address these limitations, hybrid TrafficAI, an innovative Generative AI-based framework that integrates advanced modules for traffic simulation, behaviour modelling and anomaly detection. The framework incorporates several key components. First, an Adaptive Multi-Modal Fusion Engine (AMFE) seamlessly integrates video, LiDAR, and textual data. This is achieved through dynamic feature alignment layers and context-aware gating mechanisms. Second, an Edge-Case Generative Module (ECGM) augments synthetic edge-case scenarios. Third, a Temporal-Spatial Attention Network (TSAN) captures short-term and long-term traffic dependencies. Finally, large language model-driven semantic reasoning modules extract contextual insights from unstructured textual data, such as traffic reports and incident logs. The framework employs a hybrid dual-stage optimization process, combining unsupervised generative pre-training with fine-tuned supervised calibration to ensure efficient convergence and reduced latency. By fusing multi-modal data, enhancing anomaly robustness with synthetic edge-case scenarios, and interpreting contextual semantics with LLM, hybrid TrafficAI achieves precise anomaly detection, trajectory prediction and adaptive decision-making. Experimental evaluations demonstrate significant performance improvements, including 91.45% accuracy, 93.45% mean Average Precision (mAP) for vehicle detection and a 0.910 Normalized Risk Score (NRS) for anomaly detection, consistently outperforming state-of-the-art benchmarks across latency, precision, recall and stability metrics. This framework sets a new benchmark for intelligent transportation systems (ITS) and real-time traffic management.

**Решение:** -

---

### 893 · R4934

**Behind the ChatGPT Hype: Are Its Suggestions Contributing to Addiction?**

2023 · Annals of Biomedical Engineering · journal-article · https://doi.org/10.1007/s10439-023-03201-5

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 894 · R0328

**Barriers and Enablers of AI Integration into Social Studies Education: A Systematic Review of University Lecturers and Students Experiences**

2026 · Higher Education Research · article, journalarticle, review · en · https://doi.org/10.11648/j.her.20261103.12

This research explored facilitators and barriers to the integration of AI in Social Studies education in the context of higher educational institutions (HEIs). Anchored on the Technology Acceptance Model (TAM) and directed by three research questions, the study assessed lecturers and students AI perceptions and AI competencies, and various facilitators and challenges to AI integration in Social Studies education in order to inform policy and best practices. Employing a systematic review approach, the study reviewed 10 research papers published in peer-reviewed journals. The results show that the integration of AI in Social Studies education has potential, but the level of preparedness is uneven. Although lecturers and students appreciate the transformative potential of AI for personalized instruction, increased engagement, and innovative teaching, the potential benefits are offset by the challenges of maintaining academic integrity, ethical concerns, biases, over-dependence on AI, and the loss of problem solving and critical thinking skills. Digital literacy deficits, poor university governance, inadequate training, and a lack of AI policies were identified as main barriers to the effective use of AI in universities. The evidence also points to a lack of educational equity, particularly in the Global South. The study suggests developing AI policy frameworks according to each discipline, strengthening AI literacy through continuous professional development programmes, establishing institutional policies on AI utilization, investing in digital infrastructure, integrating the teaching and learning with AI into curriculum and assessment, and incorporating ethical use of AI into curriculum and assessment practices in universities.

**Решение:** -

---

### 895 · R3439

**Profiles of AI Dependency: A Latent Class Analysis of Filipino Students' Academic Competencies**

2025 · International Conference on Education and Multimedia Technology (ICEMT) · article, conference object, preprint · en · https://doi.org/10.1145/3761843.3761871

The increasing dependency among Filipino college students on artificial intelligence (AI) poses concerns about the potential decline of fundamental academic competencies. This study examines the extent of AI dependency and its perceived effects on students' critical thinking, writing skills, learning independence, research skills, and academic engagement. Using a cross-sectional research design, data was collected from 651 students enrolled in higher education institutions (HEIs) in Pampanga, Philippines accredited by the Commission on Higher Education. The survey data was analyzed using Latent Class Analysis (LCA) to identify AI dependency patterns. Findings indicated that students show moderate to high AI dependency, specifically in research and writing tasks. LCA identified four distinct profiles: highly engaged independent learners, selective AI users, moderate AI users, and AI-dependent learners. Notably, AI-dependent learners demonstrated the weakest academic competencies, with significant dependency on AI-generated outputs. The study highlights the need to foster educational policies that integrate AI literacy while preserving essential academic skills. HEIs must also balance technological advancements with curriculum adaptations to promote critical thinking and ethical use of AI. Future research may explore the longitudinal impacts and intervention strategies to mitigate academic skill erosion caused by AI dependency. 4 pages, 1 table, conference proceedings, open access

**Решение:** ?

---

### 896 · R3474

**Using Explainable Artificial Intelligence to Predict Internet Addiction in Turkish University Students**

2025 · International Journal of Human–Computer Interaction · journal-article · https://doi.org/10.1080/10447318.2025.2526587

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 897 · R3702

**Impact Analysis of Using Artificial Intelligence on Student Skill Development**

2025 · International Journal of Multidisciplinary Research of Higher Education · article · en

Advances in artificial intelligence have brought significant changes in various aspects of life, including higher education. This study aims to analyze the impact of using Artificial Intelligence on students' academic skills, focusing on aspects of efficiency, accuracy, and independence in completing academic tasks. Using a quantitative approach with a survey method, this study involved 100 students as respondents. The data collected was analyzed using descriptive statistical tests, Pearson correlation, and multiple linear regression to identify the relationship between the variables studied. The results showed that although Artificial Intelligence can improve efficiency and provide wider access to academic information, its effect on students' academic skills was not statistically significant. Regression analysis revealed that students' efficiency, accuracy, and independence in using AI explained only 3% of the variation in their academic skills, while the other 97% was influenced by other factors. This finding confirms that over-reliance on AI may hinder the development of students' critical and analytical thinking skills, as described in constructivist learning theory and cognitive learning theory. The implications of this research suggest that educational institutions need to develop policies that encourage the judicious use of Artificial Intelligence, ensuring that Artificial Intelligence acts as a learning tool without replacing students' independent thinking processes.

**Решение:** -

---

### 898 · R2538

**Maintenance Signals in AI-Assisted GitHub Repositories: Evidence from GenAI Adopters**

2026 · arXiv (Cornell University) · journalarticle, preprint · https://doi.org/10.48550/arxiv.2607.21079

Generative artificial intelligence (GenAI) can reduce code-generation effort, but it may shift work to documentation, validation, debugging, and maintenance. We study observable maintenance-cost signals among GenAI adopters on GitHub by analyzing 622 users who publicly signal adoption, 179 repositories with visible AI-assistance configuration files, 179 matched traditional repositories, and 248 issues created in AI-assisted repositories. AI-assisted repositories span diverse project types and contain longer README files with more headers and code blocks, while traditional repositories contain more external URLs. Issues concerning GenAI technology often involve external dependencies, such as API rate limits and reliance on GenAI provider APIs. These findings suggest that AI assistance shifts maintenance costs toward verifying generated content, managing external AI dependencies, and validating AI-specific behavior.

**Решение:** -

---

### 899 · R4332

**The Influence of Artificial Intelligence on Language Learning and Translation Practices**

2025 · The Global Language and Literature Review · journalarticle, article · https://doi.org/10.70062/gllr.v1i1.44

Artificial Intelligence (AI) has significantly transformed language learning and translation practices, enhancing accessibility, efficiency, and accuracy. This study examines the impact of AI-driven technologies, including machine translation, speech recognition, and adaptive learning systems, on language acquisition and communication. The research employs a qualitative approach, analyzing existing AI applications and their effectiveness in improving linguistic proficiency. The findings indicate that AI enhances personalized learning experiences, facilitates cross-cultural communication, and reduces language barriers. However, challenges such as contextual inaccuracies, dependency on AI tools, and ethical concerns remain. The implications suggest the need for balanced integration of AI with traditional learning methods to maximize educational benefits.

**Решение:** -

---

### 900 · R0150

**Artificial intelligence, scholastic development, and academic proficiency of graduate students in Memorial University, Newfoundland and Labrador**

2026 · Memorial University of Newfoundland · master thesis, other/master thesis, dissertation · en · https://doi.org/10.48336/279

This study investigated how artificial intelligence (AI) enhances scholastic development of graduate students at Memorial University; examined the perceptions of graduate students towards the use of AI in enhancing their academic proficiency; and examined the challenges and benefits of AI in the university setting. The study employed a phenomenological research approach and qualitative methods, utilizing interviews with 15 participants from Memorial University, Newfoundland (five academic staff, five non-academic staff, and five graduate students). Data were analyzed using the thematic analysis method to analyze qualitative data to ensure adequate presentation. Based on the participants&apos; positions, the study concluded that AI tools have enhanced the scholastic development of graduate students at Memorial University in many areas of their studies. Also, graduate students perceived that the advantages of using AI outweigh the disadvantages because the tools help them to be efficient and productive. Nevertheless, if artificial intelligence is not carefully regulated and integrated into educational systems with clear guidelines, there is a significant risk that students may become overly dependent on it. AI tools have all-around benefits in university settings. Graduate students make use of the tools to enhance their productivity. Academic staff members employ AI tools to enhance their teaching methods, research endeavors, and student support services. Similarly, non-academic staff leverage these tools to optimize their operational tasks within the system. However, excessive dependence on AI tools may undermine graduate students&apos; critical thinking abilities, potentially contributing to higher instances of cheating and academic misconduct

**Решение:** -
