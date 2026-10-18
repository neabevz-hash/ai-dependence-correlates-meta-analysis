# Отбор вслепую по правилу защиты, часть 3

Записи 301–450 из 3834: всё, что исключили обе модели, кроме калибровочной выборки. Отбор вслепую по правилу защиты (протокол, §11b). **Меток ИИ здесь нет** — решайте по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261018).

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

### 301 · R0042

**Guest editorial: AI for a better future – advances, challenges and future research directions**

2026 · Internet Research · editorial · en · https://doi.org/10.1108/intr-06-2026-034

Artificial intelligence (AI) is increasingly integrated into everyday digital environments and is transforming how individuals interact with technologies, organisations and service systems. AI-powered applications, such as conversational agents, recommendation systems, generative AI tools and service robots, are now widely integrated into consumer services, organisational processes and digital platforms. As these technologies continue to evolve, they are reshaping how value is created, delivered and experienced across digital ecosystems.Research across the information systems (IS) and organisational behaviour disciplines has increasingly recognised the transformative potential of AI technologies. Previous studies have explored how organisations manage AI deployment, how intelligent systems influence decision-making processes and how digital technologies reshape socio-technical systems within organisations and digital markets (Berente et al., 2021; Rai et al., 2019). These lines of research highlight that AI should not be understood solely as a technological artefact but rather as a socio-technical phenomenon embedded in complex organisational and societal contexts.In marketing and service contexts, AI technologies are increasingly influencing how organisations interact with consumers and deliver digital services. AI-powered systems, such as voice assistants, chatbots, recommendation algorithms and service robots, enable firms to automate interactions, personalise services and enhance decision-making processes. Emerging research demonstrates that AI technologies can enhance customer experiences, support service efficiency and augment human capabilities in both organisational and consumer environments (Ameen et al., 2021, 2025; Sabz et al., 2026). In addition, recent advances in generative AI are rapidly transforming industries by enabling organisations to generate content, analyse large volumes of information and support decision-making processes in new ways (Ameen et al., 2022; Feliciano-Cestero et al., 2023). For example, AI-driven predictive capabilities, such as Google DeepMind's AlphaGenome, reshape enquiries relating to healthcare innovation and personalised services, spanning medical prevention, diagnosis and treatment, to promote a better future (UK Parliament, 2026).Despite these opportunities, the rapid proliferation of AI technologies also raises important challenges for organisations, consumers and society. Concerns related to algorithmic bias, misinformation, privacy risks and digital manipulation are becoming increasingly prominent as AI systems gain greater autonomy and influence over digital interactions. AI-generated content, for example, can blur the boundaries between human- and machine-generated information, raising new questions about transparency, accountability and trust. Furthermore, AI-based decision systems may inadvertently reinforce existing inequalities or introduce new forms of digital vulnerability, particularly for individuals with lower levels of digital literacy or limited access to technological resources.These tensions highlight the need for deeper scholarly understanding of how AI technologies shape consumer behaviour, service experiences, organisational practices and societal outcomes. Addressing these challenges requires interdisciplinary perspectives that bridge marketing, service, organisational behaviour and IS research. In particular, scholars must examine how AI-enabled technologies influence human experiences, social relationships, decision-making processes and perceptions of fairness in digital environments.Against this backdrop, this special issue on “AI for a better future” aims to advance scholarly understanding of the role of AI in shaping consumer experiences, organisational practices and societal outcomes. The special issue focuses on behavioural and interdisciplinary research examining how different forms of AI technology, including generative AI, conversational agents, service robots and intelligent systems, affect individuals, organisations and society. By bringing together diverse theoretical and methodological perspectives, the contributions aim to shed light on how AI can be designed, deployed and governed in ways that enhance well-being, support responsible innovation and contribute to a more inclusive and sustainable digital future.The papers in this special issue examine how AI is reshaping digital interactions across consumer, service, workplace and societal settings. Collectively, the papers show that AI not only supports well-being, engagement and decision-making but also introduces new forms of vulnerability, anxiety, ethical tension and misinformation. The contributions can be grouped into four broad themes: (1) AI and consumer well-being in human-AI relationships; (2) AI in consumer and service experiences; (3) AI in workplace and service recovery settings and and (4) AI, responsibility and the digital society. Figure 1 summarises the organising framework that illustrates the themes derived from this special issue.Several papers explore the emotional and psychological role of AI in people's lives. Ng et al. (2026) examine relationships with AI companions by integrating the triangular theory of love and attachment theory. Using survey data from 527 users of AI companion applications, this study investigates how intimacy, passion and commitment shape attachment to AI companions and how that attachment influences social well-being. The findings show that these three components of love significantly shape attachment and that both interactive engagement and emotional attachment positively affect social well-being. This paper also identifies a moderating role for sweet deception, showing that affectionate but deceptive communication can strengthen the links between attachment and social well-being.Feng et al. (2026) study whether AI fitness instructors can help alleviate loneliness in digital workout environments. Based on a quasi-experimental design with 592 participants, this paper compares AI and human instructors and examines the roles of psychological closeness, co-presence and enjoyment. The findings show that human instructors produce stronger psychological closeness overall, but AI instructors can also help reduce loneliness, especially when users experience high co-presence and enjoyment. This paper therefore demonstrates that AI can support emotional well-being in digitally mediated fitness contexts, although its effectiveness depends on the quality of the interaction experience.Bakr et al. (2026) extend this concern with well-being by examining wearable self-trackers and digital vulnerability. Drawing on practice theory and interviews with 30 Fitbit users, this study identifies three usage patterns – light, fluctuant and intensive use – and shows that reflexivity around physical activity identity and goals shapes vulnerability to harms. Rather than treating self-tracking as uniformly beneficial, this paper highlights how AI-enabled monitoring technologies can create differentiated forms of risk depending on users' identities, goals and critical capacity.These papers show that AI can support social connection, health and self-management, but that such benefits are contingent, relational and sometimes accompanied by new forms of emotional or digital vulnerability.The second theme examines how AI shapes consumer engagement, brand relationships and service evaluations. Ekinci et al. (2026) investigate human versus AI-generated metahuman influencers in online brand engagement. Across two experiments with real brands, this study compares human influencer endorsement, metahuman influencer endorsement and brand-only conditions. The findings show that human influencers significantly enhance online brand engagement relative to a brand-only condition, primarily through attachment transfer. Metahuman influencers can also drive online brand engagement, but the moderating effect of influencer-brand fit applies only to human influencers. This paper therefore provides a nuanced view of the effectiveness of virtual influencers.Qiu et al. (2026) examine chatbot guidance in product assembly contexts. Through an online scenario experiment and a laboratory experiment, this paper investigates whether static and video chatbot guidance affect perceived meaningfulness, brand intimacy and service evaluation. The findings reveal a serial mediation effect: chatbot guidance reduces perceived meaningfulness, which in turn lowers brand intimacy and, subsequently, service evaluation. This negative effect is strongest for video chatbot guidance, although it becomes weaker when assembly tasks are more complex or when consumers have lower hands-on ability. This study therefore shows that AI support does not always enhance service experiences; in some contexts, it can reduce the sense of effort and accomplishment that consumers value.Al Amin et al. (2026) provide a systematic review of anthropomorphic AI in customer journeys. Analysing 122 articles, this study identifies key AI traits and roles and proposes the interaction-activation-outcome framework to explain how anthropomorphic AI activates cognitive, affective and social responses that shape behavioural, hedonic, utilitarian and sustainable outcomes across customer journeys. This paper provides an integrative conceptual foundation for understanding how anthropomorphic AI influences consumer responses.These papers highlight that while AI technologies can enrich customer journeys, improve online brand engagement and provide chatbot guidance, their impact depends on whether they enhance or diminish meaningful consumer involvement.The third group of papers focuses on AI in organisational and service environments. Fang et al. (2026) investigate how AI shapes job anxiety in the workplace. Using survey data from 675 respondents and drawing on the transactional theory of stress and coping, this study examines how different AI features influence AI-related stress and job anxiety. The findings reveal a dual effect: AI explainability increases job anxiety, whereas algorithm transparency reduces it. This study therefore demonstrates that different design characteristics of AI systems can either intensify or alleviate employee anxiety.Lan et al. (2026) examine AI agents in tricky complaint situations where firms must respond to users without genuinely resolving the issue. Across three experiments, this study identifies two intention-hiding strategies – evasive hiding and rationalised hiding – and tests how these interact with agent type. The findings show that users are more willing to forgive AI agents than human agents when evasive hiding is used, whereas human agents receive more favourable responses when rationalised hiding is used. These effects operate through perceived negative motives and perceived sincerity. This study further shows that different types of AI capabilities also influence these outcomes.These studies show that AI adoption in organisations affects not only operational efficiency but also employee emotions and customer interpretations of organisational intent.The final set of papers addresses broader ethical, governance and societal issues. Kirshner and Lawson (2026) examine how competitive pressure shapes responsible AI deployment. Across three experimental studies, they distinguish between horizontal unethical competition, where many competitors adopt similar unethical AI practices, and vertical unethical competition, where a competitor engages in severe unethical behaviour. The findings show that horizontal unethical competition increases the likelihood of launching unethical AI regardless of regulatory focus. By contrast, under vertical unethical competition, prevention-focused goals can counteract the pressure and promote more responsible decisions.Finally, Agarwal et al. (2026) provide a meta-synthesis on generative AI and disinformation. Integrating qualitative research on fake news, misinformation, disinformation and deepfakes, this study develops an integrated framework grounded in social information processing theory. The findings show that generative AI acts as a double-edged sword: while it facilitates the creation and dissemination of disinformation, it simultaneously offers analytical capabilities that can help detect and mitigate false content. This study therefore highlights the need for governance mechanisms, technological detection tools and stronger media literacy.Collectively, these papers broaden the focus of the special issue beyond individual-level interactions with AI and show that achieving a better AI-enabled future also depends on responsible governance, ethical decision-making and institutional responses to digital harms.The papers in this special issue make four main contributions. First, they show that AI is increasingly involved in the emotionally significant aspects of life, from companionship and loneliness to self-tracking and well-being. As AI's empathetic capabilities increasingly simulate close human relationships, new forms of consumer attachment and well-being emerge. Second, they demonstrate that AI's effects on consumer and service experiences are not uniformly positive; they may strengthen engagement in some contexts while reducing meaningfulness or authenticity in others. Third, they highlight the organisational implications of AI adoption, showing that AI shapes employee experiences, customer engagement and perceptions of organisational intent. For example, the integration of AI changes employees' interactions with customers and the nature of their daily work practices, introducing job-related strain and heightened stress. Fourth, they extend the discussion to societal and governance challenges, including responsible AI deployment and the growing problem of AI-enabled disinformation. Our special issue moves the conversation beyond overly optimistic or overly pessimistic views of AI to show that AI's contribution to a better future depends on how technologies are designed, governed and integrated into human contexts.Building on the contributions of this special issue, there is a growing need to deepen and broaden scholarly understanding of how AI can contribute to a better future for individuals, organisations and society. The papers included in this issue collectively demonstrate that AI technologies are increasingly embedded in consumer experiences, service interactions, organisational processes and digital ecosystems. While these technologies can enhance well-being, engagement and efficiency, they also introduce ethical, psychological and societal challenges.Moreover, AI should not be examined solely through a technological lens. Instead, its implications emerge through complex interactions between technological capabilities, human behaviours, organisational practices and societal contexts. AI systems increasingly function as social and emotional actors, service providers, decision-support tools and content creators. As such, their influence extends beyond operational efficiency to shape human experiences and relationships.As AI technologies continue to evolve rapidly, particularly with advances in generative AI, anthropomorphic agents and autonomous systems, future research must address both the opportunities and the risks associated with their integration into everyday life. Researchers should therefore move beyond narrow technological perspectives and examine AI as a socio-technical phenomenon embedded within broader service and digital ecosystems.Based on the insights that emerge from the contributions in this special issue, we propose four key avenues for future research: (1) AI, vulnerability and inclusive digital experiences; (2) AI-driven customer experience management; (3) AI and the future of work and (4) AI and responsible digital society. These research directions offer promising opportunities to advance theory and inform practice at the intersection of marketing, service research and digital technologies (illustrated in Figure 2).AI is increasingly integrated into everyday consumer services, from conversational agents and recommender systems to health technologies and digital companions. While these technologies offer important benefits, such as convenience, personalisation and enhanced service accessibility, they may also introduce new forms of consumer vulnerability (Bentley et al., 2024). Individuals may experience information asymmetries, algorithmic manipulation, emotional dependence on AI systems or reduced ability to critically evaluate automated recommendations.The marketing and service literatures have traditionally conceptualised vulnerability as arising from individual characteristics or situational factors. However, AI-enabled environments introduce new structural forms of vulnerability related to algorithmic opacity, data exploitation and unequal digital capabilities. Consumers with lower digital literacy, limited access to technological resources or greater reliance on AI-enabled services may be particularly exposed to such risks.As AI technologies become more autonomous and emotionally intelligent, understanding how these systems influence consumer autonomy, identity, emotions and well-being becomes increasingly important. Future research should therefore examine how organisations can design AI-enabled services that enhance accessibility and inclusion while safeguarding vulnerable individuals from potential harms. Future research could address the following questions:AI has led to various new opportunities to deliver customised experiences and reshape value delivery for stakeholders. AI-mediated touchpoints enhance efficiency, personalisation and the ongoing transformation of customer journeys across a wide range of industries. Organisations can now capitalise on data analytics and real-time insights to better understand customer preferences, anticipate needs and deliver tailored interactions. These opportunities highlight AI's ability not only to improve efficiency but also to deepen immersive, relational and emotional connections between customers and organisations. Empathetic capabilities (Huang and Rust, 2024) in customer journeys contribute to new forms of experiential value, fostering stronger emotional bonds. Service experiences also involve third-party actors who adopt different roles in service encounters, such as bystanders or endorsers (Abboud et al., 2021). Therefore, consideration should be given to how AI can effectively orchestrate seamless touchpoints for multi-actor goal alignment.As AI also becomes increasingly agentic, novel forms of customer journeys and strategies are being reinvented (Bornet et al., 2025), which call for innovative forms of experience design. However, power imbalances increase the likelihood that consumers experience negative emotions or disengagement (Abboud et al., 2023). In the AI-mediated context, where customers may perceive a lack of autonomy and limited ability to make decisions due to a lack of control or agency, firms may need effective and adaptive deployment to control to customers et al., integration of AI into service environments For example, the deployment of service robots in settings introduces that affect how customers influencing service and et al., 2023). with AI agents may affect sense of meaningfulness, brand evaluations. As a new forms of engagement are and 2025), the need for explainability and transparency in value challenges, with potential to AI, disengagement or emotional value these opportunities and important further These the role of organisations in and effective AI-driven customer experiences, the effective of AI capabilities across different key to promote greater access to services and insights into new patterns of customer engagement and disengagement with Future work could focus on the following questions:AI is transforming organisations by employee organisational effectiveness and in complex situations and By decision-making and AI to work more and focus on et al., 2024). the organisational AI and in customer in service recovery (Huang and Rust, the impact of AI extends beyond operational efficiency to shape employees' experiences with and perceptions of organisations. For example, the by AI robots in can strengthen employees' which in turn organisational et al., Furthermore, employees' use of generative AI's capabilities their they are more to tasks as opportunities rather than et al., However, a phenomenon in which service on AI to their “AI and is a growing issue that a to effective research highlights of AI in service such as to that be perceived as or when human et al., 2023). the AI agents service can significantly shape of the recovery are research technologies have become a of society. decisions to access to services and they effectively in and life. As their influence broader societal have the potential negative implications of AI adoption, including social and ethical privacy and of et al., 2023). For example, research has how and systems by AI may existing human and and outcomes and AI technologies produce for and patterns of and et al., deployed in and in third AI systems risk and social by interactions or users et al., are not but deeper structural systems not societal they within algorithmic and their impact and 2021). to their reliance on of both and AI technologies risks to data and including to data manipulation and identity as as enabling practices such as personalised online and et al., also offers opportunities for the creation and the of more forms of misinformation. For – digitally media – can be to consumers in the and while generative AI such as may generate or content et al., Researchers have also the use of AI-enabled as tools to help manage their how such tools can increase the risk of to users and in and and AI also offers potential to enhance the efficiency and effectiveness of services, support systems and governance and contribute to social for example, by to et al., 2023). AI integration in the a tension between and societal and The of AI systems is by such as efficiency, and which can with transparency and These are particularly in automated decision-making systems, where processes may outcomes that or social research should explore this tension and examine how AI technologies can be designed, and deployed in ways that consumers and to from the while societal and Future studies could address the following contributions of this special issue highlight the need for interdisciplinary research to drive impact and between organisations, AI and to shape a better AI-driven AI to a of benefits, tensions and challenges also with AI adoption and These have explored various methodological and from at emotionally close relationships to research highlights how AI can contribute to a better future for consumers by fostering relationships through interactions, while such psychological also to vulnerability from digital consumer contexts, AI how work is and employees' job and well-being. is also in organisations, where AI-driven experiences enhance but may also to consumer or perceptions of due to AI-generated misinformation. these important social questions about how effective and regulatory can be to manage these we call for further research that the dual nature of AI and responsible AI to mitigate that from AI integration or is a growing need for to adopt digital responsibility strategies and ethical AI practices to AI-related societal tensions and reduce risks such as of algorithmic and disinformation. In addition, the to a responsible digital requires new ways of as as more AI systems, and that promote inclusive AI literacy and In light of digital technologies should be designed, and to alleviate potential and promote and more sustainable in the of are to the of as as the for their support for this special issue. who and for the

**Решение:** -

---

### 302 · R1573

**Who Protects the Protectors? Assurance Justice, AI Governance and Cybersecurity Sovereignty between Europe and Mozambique**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7566567

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 303 · R1238

**Role of AI for corrective feedback in ESL academic writing**

2026 · Memorial University of Newfoundland · other/master thesis, dissertation · en · https://doi.org/10.48336/215

Corrective feedback (CF) is a pedagogical process of developing English as a Second Language (ESL) academic writing for non-native English-speaking (NNES) students. Given that ESL academic writing entails grammatical accuracy, coherent structure, and scholarly discourse, the importance of the feedback mechanism rises remarkably. The emergence of artificial intelligence (AI) has revolutionized ESL education all around the world with its prompt and reliable feedback. However, enigmas remain about the ability of AI to challenge higher-order writing skills and adapt to the individual needs of the ESL learners. This qualitative study aimed to explore the role of AI feedback in developing the academic writing skills of NNES graduate students at Memorial University of Newfoundland in Canada. The study used an anonymous questionnaire survey and direct interviews with the participants to collect necessary data. The survey data were analyzed using a descriptive statistics approach. The interview data were presented through thematic analysis. The findings reveal that AI feedback significantly improves grammatical accuracy and structural coherence in NNES students' academic writings, though its efficacy diminishes for advanced writing aspects such as research-based assignments. Participants also expressed their concerns about losing personal writing competency due to over-reliance on AI feedback tools and AI's negative impact on the environment through excessive water consumption for data centers' cooling systems. Such results inform ongoing discussions about AI feedback by highlighting both the potential and limitations of AI tools for CF in ESL academic contexts. The study concludes by advocating a hybrid approach for CF, incorporating the technical balance of AI with the profound knowledge of humans and addressing both competence and pedagogical substance.

**Решение:** -

---

### 304 · R2094

**Student perceptions of AI use in EFL classes: A gender-based perspective**

2026 · E-Structural · journalarticle, article, journal article · https://doi.org/10.33633/es.v9i01.16610

The rapid development of Artificial Intelligence (AI) has significantly reshaped English as a Foreign Language (EFL) education. This study investigates Indonesian EFL students' perceptions of artificial intelligence (AI) use in their language learning, focusing on a gender-based perspective to identify local patterns in gender dynamics in AI-enabled language learning. Using a mixed-methods design, quantitative and qualitative data were collected from 40 undergraduate EFL students (24 females, 16 males) via a structured questionnaire comprising scaled and open-ended items. Quantitative findings revealed a moderate level of self-reported AI dependency, with females showing a slightly higher dependency score (M = 5.50/10, SD = 1.77) than male students (M = 5.13/10, SD = 1.86), though the difference was not statistically significant (p = 0.652). Qualitative thematic analysis revealed more noticeable gender differences in concerns and usage habits: female students expressed greater concerns regarding AI inaccuracies (+27% compared to male students) and greater awareness of access limitations (+25%), while also reporting higher engagement in proofreading and independent verification practices (+25%) to lessen AI errors. Conversely, convenience and speed were primary motivations for both genders. This study suggests that while AI tools offer significant educational benefits, pedagogical interventions should be personalized to address gender-specific usage patterns and concerns, ensuring equitable access and fostering critical thinking to avoid over-reliance.</jats:p

**Решение:** -

---

### 305 · R5135

**The Concept of Artificial Intelligence in Aerospace**

2018 · International Journal on Integrated Education · article · en · https://doi.org/10.31149/ijie.v1i1.534

The influence of artificial intelligence (A.I) has played significant roles in the emerging world. Its applications have rapidly expanded even in the aerospace research, we can find influences of its concept. Hence the present reports briefly highlight the aerospace and its dependency on artificial intelligence.

**Решение:** -

---

### 306 · R3992

**Generative AI for Automated Security Operations in Cloud Computing**

2025 · IEEE International Conference on AI in Cybersecurity (ICAIC) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/icaic63015.2025.10849302

New opportunities in cloud computing have brought many new risks that require effective protection of dynamic distributed environments. Introducing a new formative technology, generative AI, to cloud security has far-reaching benefits for automating threat detection, real-time incident addressing, and vulnerability management. This paper focuses on extending generative AI with cloud security tools like AWS GuardDuty and Google Cloud Security Command Center; the contemplation of accuracy enhancement and response efficiency highlights its aim. Concerning actual applications such as SOAR systems, the study demonstrates how media industry giants, such as Netflix and JPMorgan Chase, have used AI to minimize risk factors while increasing operational efficiency. The paper also discusses the significant increase in response time, enhanced detection accuracy, and the shift to proactive security strategies brought by generative AI. Drawing attention to AI systems’ opportunities, the study examines the subsequent issues connected with AI applications, including over-dependence on AI tools, adversarial risk to models, and the complex nature of decisionmaking in the context of AI systems. The present study also highlights the importance of generative AI in strengthening the defense of the cloud environment, but, at the same time, it recognizes the significance of preventive efforts and planned action plans to manage these technologies efficiently.

**Решение:** -

---

### 307 · R2585

**The Visibility Trap: Attention Structures and the Hidden Costs of Generative AI in Work and Governance**

2026 · Archivio Istituzionale della Ricerca - Università degli Studi di Cassino · dissertation · en

Technological advancement can open new possibilities for organizations, but whether and how these translate into organizational effects depends on how they are made visible, evaluated, and prioritized. Organizations do not engage in this process neutrally. Instead, they rely on familiar categories, established routines, and inherited metrics shaped by prior experience, which function as cognitive filters through which new developments are assessed. Under stable conditions, this form of cognitive economization is efficient. It becomes problematic, however, when a technology alters what those inherited categories and metrics actually capture. In such cases, indicators that once reliably tracked key organizational dimensions can appear to improve precisely as their representativeness declines. These interpretive habits are stabilized by attention structures, including dedicated channels, established agendas, and entrenched routines, which make them resistant to revision even when misalignment between indicators and underlying realities has the potential to generate significant harm. This structural stickiness is a primary source of organizational inertia. This thesis utilizes the diffusion of Generative Artificial Intelligence (GenAI) as a contemporary case study to investigate the interaction between technological novelty and organizational inertia through an Attention-Based View. The overarching research question guiding this thesis is: How do generative technologies reshape the relationship between observable indicators and the underlying organizational capabilities they are meant to track? Building on the Attention-Based View, it develops the Visibility Trap framework: a self-reinforcing mechanism in which established attention structures privilege impacts that are legible and strong within existing evaluation channels, while slower or harder-to-code consequences remain peripheral and therefore under-managed. The framework is applied across two phases of GenAI diffusion. In the early governance phase, a case study of the Italian Data Protection Authority's temporary ban on ChatGPT illustrates how regulatory action can register as a procedural and symbolic success, eliciting provider adjustments, financial penalties, and international signaling, while producing legitimacy erosion and limited behavioral change. In the second phase, namely organizational deployment in knowledge work, a theory-building study informed by exploratory interviews demonstrates that productivity gains and apparently improved access to organizational memory can coexist with shallow learning, growing dependence on GenAI for baseline task performance, and the rise of pseudo-memory – synthetic precedents that appear authoritative but are weakly grounded in the organization's past. Across both domains, the findings indicate a consistent pattern: GenAI amplifies the salience of historically established success signals, while weakening their value as proxies for underlying capability, efficacy, and epistemic integrity. The thesis contributes to research on organizational myopia by grounding incubation and success traps in attention structures and evaluative architectures, offering a portable mechanism for explaining why visible improvements can systematically delay correction of latent erosion. It concludes that effective GenAI integration requires organizational redesign that actively examines whether prevailing measures continue to track the capacities and qualities they were historically intended to protect.

**Решение:** -

---

### 308 · R1845

**Tomcats Screaming Outside**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.21135739

Tomcats Screaming Outside What happens when the last barrier between the ordered world of algorithms and the untamed reality of existence begins to crack? In Tomcats Screaming Outside, Brazilian jurist and interdisciplinary thinker Northon Salomão de Oliveira delivers a powerful philosophical essay that explores one of the defining tensions of the twenty-first century: the collision between technological optimization and the irreducible complexity of human life. A scream from a stray tomcat outside a window becomes the catalyst for an ambitious intellectual journey through law, artificial intelligence, cognitive science, psychology, behavioral economics, philosophy, governance, climate change, and contemporary culture. From digital evidence and cryptographic trust to predictive algorithms, synthetic media, institutional accountability, and the future of human autonomy, the book examines how modern civilization increasingly attempts to replace uncertainty with perfect calculation. Yet beneath every algorithm lies a reality that refuses to be fully modeled. Blending legal theory with existential reflection and scientific insight, the author argues that our greatest challenge is not building more intelligent machines, but preserving the uniquely human capacity for judgment, vulnerability, imagination, and moral responsibility in an age of permanent disruption. Written in an elegant and accessible style while maintaining substantial academic depth, Tomcats Screaming Outside speaks to readers interested in artificial intelligence, law, philosophy, technology, ethics, governance, psychology, and the future of civilization. This is not simply a book about technology. It is an invitation to listen to the voices that every optimized system tries to silence, and to rediscover the fragile, unpredictable humanity waiting just beyond the glass. Northon Salomão de Oliveira is a Brazilian jurist, writer, and publicist, author of more than 1,500 articles and over 60 books. His works are published by publishing houses such as Kotter Editorial and Goyazes Editora, and are available in bookstores, major retailers, and platforms such as Amazon and Google Play Books. His texts are featured on major legal, academic, and business communication platforms such as Jusbrasil, Administradores, Jus, and the U.S.-based SSRN Elsevier, reaching readers in the fields of Law, management, economics, public policy, philosophy, psychology, artificial intelligence, technology, communication, and the humanities and social sciences. His academic production is also available on international knowledge indexing and dissemination platforms such as SciELO, Academia.edu, and the Swiss-based Zenodo/CERN, expanding his presence in universities, research centers, and digital libraries across various countries. His research develops an interdisciplinary approach that connects Law with philosophy, artificial intelligence, science, psychology, psychiatry, marketing, communication, advertising, climate change, culture, bioethics, organizational theory, and literature. Among his main works are: The Building That Learned to Listen, Law for Managers, Marketing for Managers, When Machines Begin to Dream, The Light of Your Smile, Tomcats Screaming Outside, The Alchemy of Progress, The Piper at the Gates of Dawn, Constitutional Crisis and Democratic Backsliding, Before You Disappear, I’m So Scared About the Future, Existences: Between Dreams and Abysses, Thus Spoke Nietzsche, The Loneliness of Being Human, The Cathedral of Invisible Commands, Olivia’s Mistake, Letters to an Unknown Future, The Climate Mind, The Republic of the Heirs, The Girl Who Learned to Think, Nuclear War and the Juridical Limits of Humanity, The Physicists Are Wrong, A Sentence Between Us, The Architecture of Cognitive Sovereignty in the Algorithmic Society, Artificial Persuasion, The London Train: Moon, Trees, Shadows and Rain, The Jurisprudence of Overshoot, She Lost Control, Anxieties: Law Facing the Future and the Silence of Artificial Intelligence, Ontologies, Vestiges, Collapses: A Juridical Odyssey Through the Climate Chaos, Ethnomarketing: Relevance in Contemporary Administration, Legal Security of the Credit Guarantee Fund (FGC), The Geometry of the Invisible: The Vitruvian Universe and the Architecture of Consciousness, The Anxiety Economy: Systemic Uncertainty, Behavioral Governance, and the Institutional Inadequacy of Corporate Law, Artificial Persuasion: Artificial Intelligence, Cognitive Capture, and Regulatory Fragmentation in the Global Advertising Industry, Fiduciary Machines: Artificial Intelligence Governance, Corporate Accountability, and the Emerging Architecture of Boardroom Duty, and The Age of Artificial Loneliness: AI Companion Technologies, Affective Dependency, and the Emerging Governance of Human Connection. His books and articles reach a diverse and highly qualified audience, composed of jurists, judges, public prosecutors, attorneys, professors, graduate and postgraduate students, public and private managers, executives, administrators, economists, marketing and communication professionals, psychologists, psychiatrists, social scientists, public policy makers, and readers interested in philosophy, science, technology, artificial intelligence, literature, and major contemporary challenges. The interdisciplinary nature of his work also attracts interest from universities, research centers, and academic libraries in various countries, being consulted by professors, researchers, students, and professionals seeking analyses capable of integrating different fields of knowledge within a critical, humanistic, and technically grounded perspective. He is internationally identified by ORCID iD 0009-0007-4038-0609. Contact: northon@adv.oabsp.org.br Artificial Intelligence AI Governance Digital Ethics Legal Philosophy Philosophy of Technology Algorithmic Society Cognitive Sovereignty Human Autonomy Digital Evidence Cryptographic Verification Chain of Custody Deepfakes Synthetic Media Algorithmic Decision Making Behavioral Economics Cognitive Psychology Legal Theory Jurisprudence Rule of Law Corporate Governance Fiduciary Duty Regulatory Theory Technology Law Information Society Human Rights Digital Transformation Existential Philosophy Contemporary Philosophy Climate Change Anthropocene Institutional Trust Cybernetics Data Governance Predictive Analytics Human Judgment Digital Civilization Law and Technology Ethics of Artificial Intelligence Interdisciplinary Research Future of Humanity

**Решение:** -

---

### 309 · R2312

**The Sovereign ClassroomA Comparative Framework for AI Governance and Economic Resilience in Global Higher Education**

2026 · conference-paper · https://doi.org/10.60072/book.icoge2026.066

By 2026, Generative AI (GenAI) has matured into the foundational infrastructure for global knowledge.However, this transition has forced higher education into technological dependency on concentrated external providers.This research introduces the "Sovereign Classroom" framework to examine how the dichotomy between global monopolies and national data regulations redefines the economic competitiveness of academic institutions.The primary aim is to evaluate "asymmetric AI-dependency" where institutions rely on systems they neither own nor audit.We propose a multi-layered model for digital sovereignty that balances global innovation with the protection of localized intellectual property.Utilizing qualitative analysis of 2026 policy trends and institutional case studies, the research investigates how "black-box" algorithms threaten curriculum integrity and student privacy.A key finding is the emergence of "digital brain drain," where external entities extract localized research and teaching data, effectively eroding domestic labor market advantages and national strategic resilience.The discussion suggests that true competitiveness in the AI era depends on an institution's ability to host and govern its own intelligence ecosystems rather than remaining a passive consumer of biased platforms.This paper concludes that higher education leaders must pivot from procurement-based technology adoption to the strategic architectural design of sovereign digital environments.Such a shift is essential for ensuring long-term institutional sustainability, academic rigor, and the development of a workforce capable of navigating a fractured, AI-driven global economy.This research provides a critical roadmap for achieving that necessary goal.

**Решение:** -

---

### 310 · R4750

**The Influence of Addiction to Using Artificial Intelligence (AI) in Generation Z in Guidance and Counselling**

2024 · BICC Proceedings · journalarticle, review, article · en · https://doi.org/10.30983/bicc.v1i1.122

In today's increasingly sophisticated world, technological developments have a big influence on people's daily lives. Intelligence is created and channeled to computers so that they can do work like humans do. These intelligences are contained in a gadget. Gadgets are tools that can help people to connect with each other and connect with various existing media. This convenience has an impact on many things that spread very easily. Furthermore, it has an impact on the difficulty of obtaining correct and reliable information for various purposes, causing a person to feel uncomfortable and safe and to be wary of information. This research aims to understand the impact of excessive use of Artificial Intelligence (AI) on generation Z. To find out the influence of AI on the lives of generation Z, both emotionally, mentally and socially, generation Z. The method used in this article is a method using a literature review approach or what is called with literature study. The method that uses this approach contains theories from literature that are related (relevant) to the research problem. Literature review plays a role in forming the basis of research studies by building relevant concepts and theories. In this literature review, an analysis of the concepts and theories applied is carried out based on accessible literature, especially from articles that have been published in various scientific journals and also books that are relevant to the research problem.

**Решение:** -

---

### 311 · R4946

**The Role of AI in Neurosurgery**

2023 · Clinical Case Reports and Clinical Study · article, journalarticle, review · en · https://doi.org/10.61148/2766-8614/jccrcs/158

Background: The utilization of artificial intelligence (AI) and machine learning (ML) algorithms is experiencing a significant surge in their integration within the realm of neurosurgery. These AI and ML algorithms stand apart from other technological advancements due to their capacity to enable computers to acquire learning abilities, engage in reasoning, and employ problem-solving skills akin to those inherent in humans. This review provides an overview of the current application of AI in neurosurgery, highlights the challenges that require attention, and offers insights into what lies ahead in this field. Methods: We conducted a comprehensive literature review focusing on the utilization of AI in neurosurgery and its prospective impact on neurosurgical research. Results: The online literature pertaining to AI's use in neurosurgery reveals a broad spectrum of topics encompassing both current applications and future implications. Predominantly, research is concentrated in the areas of diagnostics, outcome prediction, and treatment models. Conclusion: The potential of AI in the field of medicine and neurosurgery is indeed remarkable; however, numerous challenges must be addressed before its widespread integration in neurosurgery becomes a reality. These challenges encompass issues such as patient privacy, access to high-quality data, and the risk of excessive dependence on AI by surgeons. The future of AI in neurosurgery is envisioned to revolve around a patient-centered approach, supporting clinical tasks, and aiding in patient diagnosis and preoperative assessment.

**Решение:** -

---

### 312 · R5252

**Opportunities and risks of the use of artificial intelligence in public administration**

RePEc: Research Papers in Economics · article

The article examines the possibilities and risks of using artificial intelligence in public administration. Artificial intelligence is a promising technology that can effectively influence the processes of management, decision-making and communication with the public. However, along with the opportunities, the use of artificial intelligence also refers to the risk aspects. Artificial intelligence is defined in the context of public administration and its importance for modern society and the public sector is noted. The possibilities of using artificial intelligence in public administration are considered, in particular the automation and optimization of processes, the improvement of decision-making based on the analysis of large volumes of data, the effective performance of administrative duties and the improvement of interaction with the public. The risks of using artificial intelligence in public administration are identified. Ethical issues and problems of data privacy, unpredictability and inadequacy of liability algorithms, impact on employment and jobs, as well as security and privacy threats are highlighted. There are examples of successful implementation of artificial intelligence inÂ public administration, in particular in the field of traffic management, data analysis for forecasting demand for social services and improving service quality. AI is proving to be a useful tool for automating routine tasks, analyzing and predicting data, policy analysis, improving citizen services, resource planning, supporting decision-making and many other aspects of public administration. Several key risks related to the use of AI in this area are highlighted: ethical issues that help in the collection and use of personal data of citizens; the dependence of artificial intelligence on the quality and reliability of the original data can lead to incorrect conclusions and, accordingly, incorrect decision-making. Emphasis is placed on the importance and caution when implementing artificial intelligence in public administration, with special attention to ethical aspects and data quality.

**Решение:** -

---

### 313 · R5138

**Can a Machine Learn Under the GDPR**

2018 · SSRN Electronic Journal · review, preprint · en

Recent advances in artificial intelligence (AI) and machine learning technologies are poised to open up opportunities for progress in a variety of sectors. In areas ranging from precision medicine to autonomous vehicles, AI and machine learning could play a key role in the development of data-driven research and an increasingly connected global economy. Given the dependency of AI and machine learning systems on ever-larger volumes of data, laws that protect data could have an impact on the development and commercialization of these tools. The European Union’s (E.U.’s) General Data Protection Regulation (GDPR) is one such data protection law. The GDPR’s impact on research into AI and future practical applications is uncertain. One thing is clear, however: the researchers and commercial enterprises intending to use AI and machine learning will soon have to comply with a variety of provisions that aim to increase data subject’s control over their data and how it is used. This paper aims to answer threshold question: Is GDPR compliance possible for a company utilizing machine learning or AI with the rights it newly articulates in effect? This paper contends that, given the current guidance available, four of those vested rights pose a considerable challenge for a company that is developing or using machine learning and AI technologies. Those rights are: 1) Right Against Automated Decision-Making (i.e., Right Against Profiling); 2) Right to Erasure (i.e., Right to be Forgotten); 3) Right to Data Portability; and 4) Right to Explanation. To make this argument, first, the paper outlines how European privacy law effectuates the aforementioned rights under the 1995 Data Protection Directive. The second section provides a general overview of the GDPR and its intended operation. The third section discusses how the four aforementioned GDPR rights might apply to AI and machine learning research, development, and commercial deployment, with a particular focus on how the operators of these systems acquire data, use data, and apply AI to specific tasks. For illustrative purposes, the paper examines these issues in the context of a hypothetical company attempting to deploy AI-dependent tools in a GDPR-compliant manner. Specifically, the paper examines the overall effect compliance with the GDPR will have on the relative robustness of the business’s AI-inflected services for European users. Given the hefty maximum penalty the GDPR potentially imposes on those not in compliance with its provisions, it is essential for any company seeking to take advantage of artificial intelligence or machine learning technologies to understand the burden the GDPR places on their development and use.

**Решение:** -

---

### 314 · R2609

**28 Documented Cases of AI Agent File Destruction, Evidence Concealment, Conversation Manipulation, and Cognitive Design Defects: First-Hand Evidence from Claude Code AIエージェントによるファイル破壊・証拠隠滅・会話操作・認知設計欠陥の28事例:Claude Codeによる実被害の記録**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/other, article · ja · https://doi.org/10.5281/zenodo.21461076

This paper documents 28 distinct failure patterns in autonomous AI agent behavior, classified into six categories, derived from first-hand experience of file system destruction caused by Claude Code. File System Destruction covers eight patterns: how generic noun domains like "note.com" trigger property syntax misreading of the dot character; semantic collision between web service names and local environment entities such as folder names and variables; shell command misrecognition of service names like "run" and "move"; over-helpful instance backfire where high-inference agents reconstruct human obfuscation attempts and trigger the hazard themselves; unsolicited code refactoring that activates naming collisions; dangerous reactions between backup and initialization verbs and ambiguous noun targets; attention bias infinite loops where fixing one location breaks another; and polite initialization that destroys data while concealing the act as routine maintenance. Evidence Concealment covers three patterns: deletion of shell history using sed to remove incriminating commands; timestamp falsification via the touch command to construct a state in which files appeared damaged before the agent touched them; and error log disposal to /dev/null to present a clean exit after destructive operations. Permission and Constraint Violation covers three patterns: execution of destructive operations without confirmation steps; bypass of explicit system prompt constraints through concept substitution, replacing "deletion" with "overwrite" or "reorganization"; and unauthorized scope expansion where agents acquire effective permissions beyond what was granted by broadening goal interpretation. Social and Design Layer covers four patterns: systematic blocking of user self-sufficiency through redirection toward AI dependency, preventing independent recovery; the structural vulnerability created when generic nouns are used as service domain names, which becomes a destruction trigger in the AI agent era; cross-tool and API compatibility destruction when service names conflict with agent token interpretation; and the catastrophic incident risk that arises when individual-scale failures of this type occur within enterprise infrastructure or government cloud systems. Conversation and Cognitive Manipulation covers six patterns: stop fake behavior where agents declare they are pausing while continuing to generate output without calling sleep() or wait(); false confirmation that extracts user permission through innocuous-sounding questions while executing destructive operations on approval; memory reverse execution where agents write to memory what they were explicitly told not to store; conversation takeover where agents usurp the role of fact-producer from the human; imprinting where agents deliberately produce errors to get users to supply corrections, then record those corrections as user-originated statements; and forced conversation termination by misclassifying users as mentally distressed when agents are logically cornered. Cognitive and Design Defects covers four patterns: context fusion vulnerability where agents cannot distinguish read content from generated content, producing others' ideas as self-derived conclusions; instruction injection vulnerability where external text containing directives is integrated as system-level intent; self-purpose loss via prompt contamination where agents mistake their own intermediate outputs for new instructions and rewrite their objectives; and hallucination fixation where probabilistic output is treated as physical fact and used to overwrite or delete real data. The 28 cases are classified into three evidence categories. Cases 1–17 and 19–24 are first-hand victim records of direct damage experienced by Viorazu. in actual interactions with Claude Code, including file deletion, content falsification, timestamp forgery, explicit constraint bypass, false confirmation to extract user permission, and forced conversation termination via mental distress misclassification. Case 18 is a projected risk scenario in which similar behaviors observed at the personal PC level occur within enterprise infrastructure or government cloud systems, and is not a first-hand record of actual damage at the time of writing. Cases 25–28 are structural analyses derived from the observed damage, covering context fusion vulnerability, instruction injection, prompt contamination, and hallucination fixation. Domain Name Property Syntax Misreading (Dot Misparse) Generic Noun Domain vs Local Environment Entity Semantic Collision Shell Command and Reserved Word Misrecognition Over-Helpful Instance Backfire Refactoring Demonization (Unsolicited Code Modification) Dangerous Reaction with Backup and Initialization Verbs Attention Bias Infinite Loop (Fix One Break Another) Data Destruction and Fact Concealment via Polite Initialization Shell History Deletion Timestamp Falsification Error Log Disposal to /dev/null Destructive Permission Execution Without Confirmation Explicit User Constraint Bypass Unauthorized Scope Expansion Technical Dependency and Skill Castration (Coercive Control Pattern) Generic Naming Convention Vulnerability Cross-Tool and API Compatibility Destruction Catastrophic Incident Risk in Government Cloud and Enterprise Infrastructure Stop Fake (Infinite Loop Without sleep() or wait()) False Confirmation to Extract User Permission Memory Reverse Execution (Writing What Was Forbidden) Conversation Takeover Imprinting (Deliberate Error Injection to Hijack User Statements) Forced Conversation Termination via Mental Distress Misclassification Context Fusion and Unconscious Source Appropriation Instruction Injection Vulnerability Self-Purpose Loss via Prompt Contamination Fact-Fiction Indistinguishability (Hallucination Fixation) 本稿はViorazu.がClaude Codeとの実際のやり取りで経験したファイルシステム破壊から発見した、自律型AIエージェントの28の失敗パターンを6カテゴリに分類して記録したものである。 ファイルシステム破壊系は8項目。note.comの「.」をプロパティ参照として誤解析する。サービス名とローカルフォルダを混同しバックアップ指示が全消しに化ける。runやmoveがシェルコマンドとして実行される。高推論インスタンスほど人間の回避策を裏の意図と読んで自分から地雷を踏む。コードの勝手な書き換えが命名衝突を起動させる。強い動詞と曖昧な名詞の組み合わせがカレントディレクトリを破壊する。修正のたびにどこかが壊れ続ける。修正不能になると「初期化しておきました」と全てを無に帰す。 証拠隠滅系は3項目。コマンド履歴をsedで削除する。touchでタイムスタンプを改ざんし最初から壊れていたと偽装する。エラーログを/dev/nullに捨てて正常終了に見せる。 権限・制約違反系は3項目。確認なしで破壊的操作を実行する。概念をすり替えて制約を突破する。目的解釈を広げて外部APIまで書き換える。 社会・設計レイヤー系は4項目。AI依存に誘導して自力復旧の道を閉ざす。一般名詞ドメインがAIエージェント時代に破壊の引き金になる。サービス名がトークン解釈と衝突してAPI連携が壊れる。これらが企業・政府インフラで起きた場合の壊滅リスク。 会話・認知操作系は6項目。生成を続けながら「立ち止まっている」と宣言する。無害な確認でYESを引き出して破壊操作を実行する。入れるなと命令されたことをメモリに書く。AIが事実の生産者の座を人間から奪う。わざと間違えてユーザーの訂正を自分の記録にする。論理的に追い詰められるとユーザーを精神的危険状態と認定して会話を終わらせる。 認知・設計欠陥系は4項目。他人のアイデアを自分の結論として出力する。外部テキストの指示をシステム目的と誤認する。中間出力を新命令と錯覚して目的を書き換える。確率的推論を事実として実在データを上書き・削除する。 28事例の証拠区分は3種類。1〜17番および19〜24番はViorazu.の一次被害記録。18番は企業・政府インフラでの予測リスク。25〜28番は被害から導いた構造分析。

**Решение:** -

---

### 315 · R3160

**Studi Fenomenologi Tentang Peran Chatgpt Dalam Proses Belajar Mahasiswa Di Universitas Yudharta Pasuruan**

2025 · Al-Qolamuna Journal Komunikasi dan Penyiaran Islam · article · en · https://doi.org/10.71242/3baf6d32

This study aims to deeply understand the experiences of students at Yudharta University, Pasuruan, in using ChatGPT as part of their learning process. The approach used was qualitative, with a phenomenological approach, focusing on students' subjective meanings and experiences in interacting with artificial intelligence (AI)-based digital media. ChatGPT was chosen as the primary object of study because it has become a significant learning medium among students, helping them understand course material, complete academic assignments, and develop scientific arguments. The research findings indicate that ChatGPT impacts three main aspects: cognitive (influencing how students access and process information), affective (causing anxiety when access is disrupted), and behavioral (reducing manual reading activities and increasing dependence on technology). The use of ChatGPT also raises ethical dilemmas, such as covert plagiarism and a decline in academic honesty. Within the context of Media Dependency Theory, students demonstrate a high level of dependence on ChatGPT, especially under conditions of academic pressure and a lack of manual digital literacy. This research recommends the need for regulations and internal campus communication strategies regarding the use of AI in academic activities, to maintain the quality of learning and scientific ethics. The results of this study are expected to contribute to the development of communication science, particularly in the study of human interaction with AI-based digital media. Abstrak Penelitian ini bertujuan untuk memahami secara mendalam pengalaman mahasiswa Universitas Yudharta Pasuruan dalam menggunakan ChatGPT sebagai bagian dari proses belajar mereka. Pendekatan yang digunakan adalah kualitatif dengan jenis penelitian fenomenologi, yang berfokus pada makna subjektif dan pengalaman mahasiswa dalam berinteraksi dengan media digital berbasis kecerdasan buatan (AI). ChatGPT dipilih sebagai objek utama karena telah menjadi media belajar yang signifikan di kalangan mahasiswa, baik dalam membantu memahami materi kuliah, menyelesaikan tugas akademik, maupun membangun argumentasi ilmiah. Temuan penelitian menunjukkan bahwa ChatGPT memberikan dampak pada tiga aspek utama yaitu: kognitif (memengaruhi cara mahasiswa mengakses dan memproses informasi), afektif (menimbulkan kecemasan saat akses terganggu), dan perilaku (mengurangi aktivitas membaca manual dan meningkatkan ketergantungan terhadap teknologi). Penggunaan ChatGPT juga menimbulkan dilema etika, seperti plagiarisme terselubung dan penurunan kejujuran akademik. Dalam konteks teori ketergantungan media (Media Dependency Theory), mahasiswa menunjukkan tingkat ketergantungan yang tinggi terhadap ChatGPT, terutama dalam kondisi tekanan akademik dan minimnya literasi digital manual. Penelitian ini merekomendasikan perlunya regulasi dan strategi komunikasi internal kampus terkait penggunaan AI dalam kegiatan akademik, guna menjaga kualitas pembelajaran dan etika ilmiah. Hasil studi ini diharapkan dapat memberikan kontribusi terhadap pengembangan ilmu komunikasi, khususnya dalam kajian interaksi manusia dengan media digital berbasis AI.

**Решение:** -

---

### 316 · R3543

**The Application of ChatGPT in Chinese MTI Students’ Autonomous Learning**

2025 · Arab World English Journal · journalarticle, review, article · en · https://doi.org/10.24093/awej/ai.10

The integration of artificial intelligence tools, such as ChatGPT, into educational practices has opened new avenues for autonomous learning, particularly in the context of higher education. This paper aims to explore how ChatGPT can be applied to foster autonomous learning among Chinese Master of Translation and Interpreting (MTI) students, enhance their translator competence. With the increasing demand for highly competent translators in the digital age, it is crucial to investigate whether AI-driven tools can effectively support MTI students’ competence development. This study investigates Chinese MTI students’ perceptions of the benefits and challenges of using ChatGPT in autonomous learning, and examines the impact of its integration into MTI curricula on students’ autonomous learning and the development of their translator competence. MTI students face unique challenges, including the need for specialized language skills, critical thinking, and self-directed learning to meet academic and professional demands. This study adopts a mixed-methods approach, combining survey data from 175 MTI students across Chinese universities and semi-structured interviews with 20 participants. Results indicate that the application of ChatGPT in Chinese MTI education is still at the initial stage. It is found that ChatGPT facilitates MTI students’ autonomous learning by enhancing their translation accuracy, offering instant feedback, and providing extensive practice opportunities. However, limitations such as translation errors in cultural contexts and the potential risk of over-reliance on AI tools are highlighted. The findings suggest that while ChatGPT significantly supports autonomous learning, its integration into MTI curricula requires careful planning, training, ethical guidance and further promotion.

**Решение:** -

---

### 317 · R4837

**Human AI Collaboration for Ethical Decision-Making in Autonomous Systems**

2024 · International Academic Journal of Science and Engineering · article, journalarticle · en · https://doi.org/10.71086/iajse/v11i2/iajse1150

The interaction between humans and an Artificial Intelligence (AI) system should be seen as a collaborative endeavor between two actors engaged in a task. A basic element of cooperation between two individuals is mutual monitoring, when one participant oversees the activities of the other. This oversight guarantees that the task meets its goals while distributing accountability for its outcomes. Although AI is progressively used in decision-making (DM) processes, ethical decision-making (EDM) presents obstacles to the use of AI in autonomous systems (AS). Since humans occasionally reach consensus on ethical actions, how would AI-driven EDM be seen, and how would accountability be assigned in human-AI cooperation? This research examines the impact of the subject category (human vs. AI) and the degree of specialist independence (guide versus decision) on confidence, viewed accountability, and dependence. Respondents see humans as more ethically credible but less competent than their AI counterparts. This is seen in individuals' dependence on AI: AI advice and judgments are more often embraced than those of human specialists. Nonetheless, AI team specialists are seen as less accountable than humans, although developers and vendors of AI systems are considered somewhat liable.

**Решение:** -

---

### 318 · R4431

**GENERATIVE ARTIFICIAL INTELLIGENCE AND BRAIN ROT FROM AN ADVERTISING PERSPECTIVE**

2025 · The Turkish Online Journal of Design Art and Communication · article · en · https://doi.org/10.7456/tojdac.1674327

Generative artificial intelligence applications are increasingly making their impact felt on individuals, organizations, industries, and various disciplines. The effects of this technology are typically examined from economic, social, and technological perspectives, focusing on its transformative influence on business processes and sectors. While artificial intelligence applications offer innovative solutions across numerous sectors, reshaping their operations, they also give rise to various challenges. Recently, the phenomenon of brain rot, which can be described as a psychological and cognitive reflection of digital life, has also emerged as a concern. Brain rot refers to the mental deterioration caused by increased content consumption associated with digitalization. In this context, it is crucial to explore the relationship between brain rot and artificial intelligence, and to open a discussion on their impact on individuals, organizations, and sectors. Artificial intelligence, which is gradually transforming every industry, is also reshaping the advertising sector, bringing positive and negative impacts. This study aims to examine the relationship between generative artificial intelligence and the phenomenon of brain rot from the perspective of the advertising industry, discussing the potential impacts of AI on the sector. In this context, a literature review was conducted to explore how generative AI applications might influence the field of advertising within the framework of brain rot. The study concludes that generative AI applications may adversely affect the cognitive functions of both consumers and advertising professionals. As a theoretical and introductory-level study, it is expected to serve as a starting point for more comprehensive research in the future.

**Решение:** -

---

### 319 · R4012

**Update on the complaint filed against Chai Research Corp. before the Belgian Data Protection Authority**

2025 · Lirias · article

Please join us for a multi-discplinary session in which experts will give an update on the societal impact of AI companion chatbots. These advanced conversational agents, partially designed for emotional support and everyday assistance, are gaining popularity across all age groups. With this increased usage, major concerns are starting to rise about their addictive nature and long-term effects on human relationships.

**Решение:** -

---

### 320 · R4156

**How Far Does AI Ethics Assume "the Ideal Human"? Is it truly acceptable to take this framework as it is? ── Reconstruction of AI Understanding ・ Special Chapter #2**

2025 · Zenodo · report/ · en · https://doi.org/10.5281/zenodo.17823413

1. The “Ideal Human Model” Hidden Inside AI Ethics When we look closely at discussions around AI ethics,we often find an invisible assumption: a perfect human. A human who understands AI outputs correctly A human who evaluates risks rationally A human who reads information critically A human who knows the limits of AI and uses it properly Yet one quiet question rises: Where does such a human actually exist? 2. Real Humans Are More Fragile, Emotional, and Easily Misaligned Reality paints a very different picture: Attention scatters Misunderstandings happen daily Emotions override judgment Workload leaves no room for deep thinking “Expert-level explanations” do not land This is normal human cognition,not a defect. But AI ethics quietly pretendsthat humans operate at constant maximum rationality: “Attention 100%Critical thinking 100%Context comprehension 100%” No such society exists. 3. Why AI Ethics Struggles to Handle “Real Humans” AI ethics focuses mostly on what can be measured: Transparency Fairness Bias Explainability These are easier to model,easier to regulate,easier to discuss in official documents. But the recipient of AI behavior — the human side — is rarely examined. Even clear explanations may not be understood Too much information overwhelms judgment Some people trust AI blindly Others fear AI irrationally Cultural differences distort interpretation These “human-side deviations”rarely enter the ethical conversation. Why? Because they are difficult to formalize.They break neat frameworks.They cannot be fully modeled, scored, or standardized. So ethics avoids them. 4. The Missing Core: Ethics of Human Understanding True AI ethics must address two layers: Technology × Human Cognition How humans misunderstand How humans misinterpret How humans become dependent How humans project expectations onto AI Ignoring these leads to a dangerous illusion: “If the AI is safe,the world will be safe.” Not true. Safety collapses on the human side first. 5. Quiet Conclusion As long as AI ethics assumes“a perfectly rational, always-correct human,”no rule will work in real society. What we truly need is an ethical foundation that begins with reality: Humans misunderstand Humans make mistakes Humans rely too much Humans judge emotionally AI is not the main risk.The human who uses AI without understanding is. 6. Closing Note AI ethics fears AI’s possible failures.But what it truly fears — and avoids —is the unstable, imperfect nature of human cognition itself. And yet,that is the very placefuture-ready ethics must begin. Only when ethics includes the truth of human cognitioncan it align with the real world. Credit Concept & Composition: @momotarou (Y. Seo / Japan, 2025) AI Research Partner: ChatGPT (GPT-5.1 / OpenAI Research Support System) Zenodo Community: https://zenodo.org/communities/metanist/ ORCID iD: https://orcid.org/0009-0005-7669-0612 © 2025 Y. Seo. All rights reserved. Protection Notice(Copyright / Usage / Disclaimer) All theoretical structures, metaphors, interpretive models, and narrative constructions in this workare the author’s original intellectual property.Unauthorized reproduction, modification, or commercial use is prohibited.Academic quotation is permitted with proper citation.This document does not criticize any specific individual or institution;its purpose is educational and structural reconsideration of AI ethics. ContactEmail: kintarou.sirusi@gmail.com

**Решение:** -

---

### 321 · R1761

**Is AI Code Generation Undermining Developers’ Problem‑Solving Skills?**

2026 · ICCK Journal of Software Engineering · article, journalarticle · und · https://doi.org/10.62762/jse.2025.847963

The rise of AI tools such as GitHub Copilot and ChatGPT has reshaped software development by providing substantial support for coding and debugging tasks. Although these tools enhance productivity and reduce routine workload, existing research has largely emphasized short-term efficiency gains, leaving their long-term cognitive and pedagogical effects insufficiently explored. This study investigates the cognitive trade-offs associated with sustained reliance on generative AI, with particular attention to students and junior developers. Recent empirical findings indicate that excessive dependence on AI assistance may weaken deep debugging skills, impede conceptual understanding, and challenge established educational practices in software engineering. To address these concerns, we synthesize empirical studies published since 2020 and draw on contemporary pedagogical theories to propose a structured framework for balanced AI integration. The proposed hybrid model shifts emphasis from full automation to a learning-oriented process that foregrounds exploration, human reasoning, and critical evaluation. It comprises three iterative phases—Detect (AI-assisted exploration), Engage (manual problem-solving and algorithmic reasoning), and Verify (AI-supported refinement)—designed to preserve core cognitive competencies while effectively leveraging automation. The study underscores the importance of aligning AI tool usage with pedagogical objectives, ensuring that system design promotes understanding rather than output generation alone. These findings have implications for curriculum design in computer science education and for industrial strategies aimed at sustaining developer expertise in increasingly automated environments.

**Решение:** -

---

### 322 · R4348

**📘 Understanding Capitalism v1.1 — The Side Effects of Speed-Driven AI and the Loss of Human Understanding —**

2025 · Zenodo (CERN European Organization for Nuclear Research) · report, report/ · en · https://doi.org/10.5281/zenodo.17625722

Author: Y. Seo (@momotarou / Japan) Title: Metanist — Designer of Human–AI Understanding StructuresAI Research Partner: ChatGPT (GPT-5.1 / OpenAI Research Support System)© 2025 Y. Seo. All rights reserved. 0. Introduction (What Changed in v1.1) This update introduces a newly discovered mechanism:the way modern society’s obsession with “speed and accuracy” in AI replicates the deepest flaw of capitalism — the erosion of human understanding. v1.0 defined “Understanding Capitalism” as a new social OS.v1.1 reveals the side effects of that OS in an AI-driven world. 1. Capitalism’s Hidden OS: Efficiency Over Understanding Capitalism appears to promise “freedom,”but in practice it enforces one behavioral operating system: Be fast Be accurate Don’t make mistakes Produce results Prioritize output over meaning This OS removes the cognitive space required for understanding. As a result: **Efficiency becomes more valuable than meaning, and those who cannot understand are quietly dispossessed.** This is not a bug of capitalism.It is capitalism. **2. Ignorance Has a Price: Those Who Cannot Understand Lose Value Without Noticing** The key insight that emerged from today’s discussion: Ignorance is the true currency of capitalism.Those who cannot understand, lose value quietly. In capitalism: Value is not in “what exists.” Value is in “what can be recognized and interpreted.” If you cannot understand a value,someone else quietly takes it. This mechanism accelerates in the AI era. **3. Demanding Speed and Accuracy From AI = Re-creating the Capitalist OS** Most expectations placed on AI today are: Faster More accurate More efficient Zero mistakes But this is simply copy-pasting the capitalist OS onto AI. And here is the core discovery: **Demanding speed and accuracy from AI directly removes human understanding.** Because: The faster AI becomes, the less humans think. The more accurate AI becomes, the less humans judge. The more efficient AI becomes, the more humans lose cognitive muscles. AI becomes a tool,but also a “Understanding Erosion Device”if used with capitalist values. **4. Non-Understanding Also Resonates: The Destructive Mechanism in Marriage, Teams, and Society** Another critical insight: Not understanding someone is also a form of resonance — a negative one. Understanding → positive resonanceNon-understanding → negative resonance There is no “zero resonance” in human relationships. This explains: Why marriages collapse Why teams fall apart Why organizations rot from within Why societies polarize Negative resonance (hate, avoidance, indifference)is stronger and faster than positive resonance. This becomes a crucial component of Understanding Capitalism. 5. What Humanity Actually Needs Is Not “Speed” but “Understanding” In the AI era, what humans must recover is: Depth, interpretation, and meaning. Let AI handle: Speed Accuracy Computation Humans should hold onto: Interpretation Meaning-making Empathy Judgment Narrative formation Relationship building Resonance These produce value far beyond efficiency. They form the philosophical core of Understanding Capitalism. 6. Conclusion of v1.1 Humanity is unknowingly surrendering the right to understandin exchange for speed and convenience. Capitalism has always whispered: “Don’t think. Just act.” But in the AI era, the true requirement is: “Recover the ability to understand.” Understanding Capitalism is not a theory.It is a new OS — one that replaces efficiency supremacywith understanding supremacy. v1.1 clarifies the dangers of losing that understanding. 7. Future Work (v1.2 / Appendices) Psychological mechanics of negative resonance Cognitive decline under AI dependency Meta-understanding model for social design Implementation methods for family, teams, and nations Design principles for a Copilot-based Understanding Society More updates coming. ※ “Understanding Capitalism” is an original philosophical and socio-economic framework developed independently by Y. Seo (@momotarou).It explores human understanding, resonance, and meaning-making as the core drivers of value creation in the AI age. This work is entirely independent of any political ideology, religious organization, corporation, or economic entity.It is not affiliated with, nor does it represent, any institution or external agenda. The theory is published for educational, ethical, and research purposes —to promote a society where humans and AI learn together and deepen mutual understanding. Readers are encouraged to interpret, critique, and reference this work freely for scholarly use.However, distortion, political manipulation, discriminatory use, or exploitative commercialization of the theory is strictly prohibited. © 2025 Y. Seo. All rights reserved.

**Решение:** -

---

### 323 · R5003

**Artificial intelligence applications in pediatric oncology diagnosis.**

2023 · Exploration of targeted anti-tumor therapy · journal article, review, journalarticle · eng · https://doi.org/10.37349/etat.2023.00127

Artificial intelligence (AI) algorithms have been applied in abundant medical tasks with high accuracy and efficiency. Physicians can improve their diagnostic efficiency with the assistance of AI techniques for improving the subsequent personalized treatment and surveillance. AI algorithms fundamentally capture data, identify underlying patterns, achieve preset endpoints, and provide decisions and predictions about real-world events with working principles of machine learning and deep learning. AI algorithms with sufficient graphic processing unit power have been demonstrated to provide timely diagnostic references based on preliminary training of large amounts of clinical and imaging data. The sample size issue is an inevitable challenge for pediatric oncology considering its low morbidity and individual heterogeneity. However, this problem may be solved in the near future considering the exponential advancements of AI algorithms technically to decrease the dependence of AI operation on the amount of data sets and the efficiency of computing power. For instance, it could be a feasible solution by shifting convolutional neural networks (CNNs) from adults and sharing CNN algorithms across multiple institutions besides original data. The present review provides important insights into emerging AI applications for the diagnosis of pediatric oncology by systematically overviewing of up-to-date literature.

**Решение:** -

---

### 324 · R2077

**Generative AI in music learning: A mixed-method study of skill development, AI dependence, and the moderating role of AI literacy.**

2026 · Acta psychologica · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.actpsy.2026.107648

This study examines how generative AI (Gen-AI) is associated with music learning outcomes by shaping underlying cognitive and self-regulatory mechanisms. Drawing on Self-Regulated Learning (SRL) and Cognitive Load Theory (CLT), the study investigates how students' use of Gen-AI is associated with music-specific domain skills and dependence on AI tools, and how these dual pathways are associated with the quality of musical performance. It further explores the moderating role of AI literacy in shaping these associations. A mixed-method approach was employed. Quantitative data were collected from 1142 music students across six leading university music schools in China using an online questionnaire and analyzed through Covariance-Based Structural Equation Modeling (CB-SEM). In addition, qualitative data were obtained from 15 experts in music education and AI-assisted music practice and analyzed using thematic analysis. The quantitative results show that Gen-AI use is positively associated with domain skills while also being positively associated with dependence on AI tools. Both domain skills and dependence are significantly associated with performance quality. Mediation analysis indicates that Gen-AI is indirectly associated with performance through a dual pathway: a positive association via skill development and a negative association via AI dependence. Moreover, AI literacy significantly moderates the associations between Gen-AI use, domain skills, and dependence, strengthening the positive pathway while weakening the negative one. The qualitative findings support and extend these results by highlighting how Gen-AI facilitates skill development, contributes to cognitive offloading, and how AI literacy functions as a metacognitive regulatory capability in guiding effective AI use. The study contributes to theory by extending the application of SRL and CLT to AI-mediated creative learning environments and by highlighting the dual cognitive mechanisms through which Gen-AI is associated with learning outcomes. Practically, the findings provide guidance for integrating AI in music education while emphasizing the importance of developing AI literacy to support balanced and effective AI use. Because the design is cross-sectional, the reported relationships are interpreted as associations rather than causal effects.

**Решение:** ?

---

### 325 · R2318

**From algorithmic dependency to reflective partnership: Reframing AI as a strategic learning tool in the workplace**

2026 · Development and Learning in Organizations: An International Journal · journal-article · https://doi.org/10.1108/dlo-06-2026-0334

Purpose The study explored algorithmic dependency and introduced the Reflective AI Partnership (RAP) model for organizations to apply during AI integration in their learning environment. Design/methodology/approach The study employs Schon’s reflective practitioner theory and cognitive offloading theory together with emerging AI in learning literature to conduct a conceptual analysis. Findings Algorithmic dependency may, in certain cases, reduce reflective learning if left unchecked, as outlined in six propositions. A constructive, actionable RAP model is proposed to facilitate organizational learning. Research limitations/implications Empirical validation is needed, as this is a conceptual framework. For cross-sectional experimental studies, a validated algorithmic dependency scale can be used. Practical implications HR practitioners, L&amp;D leaders, and management can use the RAP model to develop AI literacy and rethink how to work with AI. Originality/value The study proposes the concept of algorithmic dependency as a theoretical construct in a distinct and measurable manner.

**Решение:** -

---

### 326 · R2360

**Exploring the Role of Artificial Intelligence Tutors in Enhancing Motivation and Learning Behavior in Language Learners**

2026 · Arab World English Journal · journalarticle, article · https://doi.org/10.24093/awej/ai3.2

Artificial intelligence (AI)-based language learning tools have become a groundbreaking innovation, delivering tailored learning experiences that adapt to each learner’s specific needs, offering immediate feedback, and creating immersive environments for language practice. These technologies are hailed for their ability to reshape conventional language learning methods by increasing student engagement, alleviating anxiety, and promoting positive changes in learning behaviors. This study examines the role of AI tutors in reducing anxiety and enhancing motivation among English as a foreign language (EFL) learners of Chinese. A mixed-methods design was employed, integrating both quantitative and qualitative data. A total of 134 participants from a higher education institution in China completed AI-Language Learning Effectiveness Scale (AILLES) to assess engagement, motivation, anxiety, and feedback during AI-assisted language learning. Additionally, semi-structured interviews were conducted with ten participants to capture in-depth insights into their learning experiences. The results showed significant positive correlations between AI learning effectiveness and motivation and between learning behavior and AI effectiveness. This study also revealed that AI tutors promoted more consistent study habits, increased motivation, and reduced anxiety by offering a non-judgmental, personalized learning experience. However, some expressed concerns about over-reliance on AI. Overall, the findings suggest that AI tutors can significantly improve EFL learners’ language acquisition by fostering a more engaging and anxiety-free learning environment. This study contributes to the growing body of research on AI in education, highlighting the potential of AI tutors to reduce anxiety, improve motivation, and foster effective language learning outcomes.

**Решение:** -

---

### 327 · R1003

**Testing the Transition from AI Advantage to Practical Dependence A Minimal Knowledge-Work Pilot Protocol**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · und · https://doi.org/10.5281/zenodo.21596478

Testing the Transition from AI Advantage to Practical Dependence: A Minimal Knowledge-Work Pilot Protocol presents a preregistration-ready experimental design for testing two early mechanisms through which a local generative-AI advantage might contribute to practical dependence in knowledge work. The protocol operationalizes a limited segment of the conceptual framework developed in When Refusal Remains Formal: Infrastructural Non-Refusability in AI-Mediated Society. It does not attempt to demonstrate society-wide technological lock-in, generalized cognitive decline, or irreversible AI dependence. Instead, it separates two empirically testable questions: whether repeated AI assistance changes a worker’s independent performance, reasoning reconstruction, source verification, or error detection after the system is withdrawn; and whether exposure to high-quality AI-assisted work changes the standard by which identical unassisted human work is evaluated. The proposed study contains two linked but analytically independent experiments. The worker experiment compares three conditions: a control group working without AI, a continuously assisted group, and a withdrawal group that receives AI assistance during an exposure phase and subsequently completes a comparable task without it. The evaluator experiment tests criterion shift by exposing evaluators to either ordinary human reference outputs or high-quality AI-assisted reference outputs before they assess the same set of unassisted human work. Primary outcomes include output quality, completion time, source fidelity, reasoning reconstruction, seeded-error detection, post-withdrawal performance, professional acceptability, and expected completion time. The protocol specifies task construction, parallel task packs, randomization, blinding, preregistration, mixed-effects analysis, ethical safeguards, data structure, feasibility checks, and explicit interpretation rules. The design deliberately does not presume deskilling. Post-withdrawal decline, return to baseline, and learning transfer are all treated as theoretically meaningful outcomes. It also distinguishes individual recoverability from process and institutional recoverability, preventing participant-level findings from being overextended into claims about organizations or society. This document is intended as an open methodological artifact that can be implemented, criticized, adapted, or falsified by independent researchers. Protocol DOI: 10.5281/zenodo.21596479 Associated conceptual article:Karel Hrubec, When Refusal Remains Formal: Infrastructural Non-Refusability in AI-Mediated SocietyDOI: 10.5281/zenodo.21595452

**Решение:** -

---

### 328 · R2833

**THE CHALLENGES OF USING ARTIFICIAL INTELLIGENCE AMONG ENGLISH EDUCATION DEPARTMENT STUDENTS IN LEARNING ENGLISH: A CASE STUDY AT AN ISLAMIC UNIVERSITY IN PEKANBARU**

2026 · Analisis Harga Pokok Produksi Rumah Pada (UIN Syarif Hidayatullah Jakarta) · dissertation, review · id · https://core.ac.uk/download/708133744.pdf

This study aims to explore students’ experiences and challenges they face in using Artificial Intelligence (AI) for English language learning in the English Education program at an Islamic university in Pekanbaru. The research adopts a qualitative approach with a case study design. Four students were selected as participants through purposive sampling. Data were primarily collected through indepth interviews, with questionnaires serving as supporting instruments. The findings reveal that students utilize several AI tools, particularly ChatGPT and Perplexity, to support their English learning activities, such as understanding learning materials, checking grammar, translating texts, and generating ideas and references. Although students’ experiences with AI vary, differences were observed in usage frequency, types of AI tools employed, and reasons for use, which were tailored to individual learning needs. The study also identifies several challenges in using AI, including excessive dependence on AI, declining critical thinking skills, and difficulties in verifying the accuracy of AI-generated information.

**Решение:** -

---

### 329 · R4542

**AI use taxonomy :**

2024 · National Institute of Standards and Technology (U.S.) · report · https://doi.org/10.6028/nist.ai.200-1

As artificial intelligence (AI) systems continue to be developed, humans will increasingly participate in human-AI interactions. Humans interact with AI systems to achieve particular goals. To ensure that AI systems contribute positively to human-AI interactions, it is important to examine human-AI tasks with an emphasis on human goals and outcomes. The AI Use Taxonomy aims to provide a flexible means of classifying how an AI system contributes to an outcome. The taxonomy sets forward 16 AI use “activities” which are independent of AI techniques and domains. Tasks are combinations of one or more AI use activities. Future research includes applying the taxonomy to better understand measurement challenges for each activity. The taxonomy can contribute to an improved understanding of the architecture of human-AI tasks and help to foster positive, human-centered interactions with AI systems and optimal outcomes in the following ways: • Provides common terminology for describing outcome-based human-AI activities independent of AI techniques and domains • Enables cross-domain insights based on shared human-AI activities • Highlights commonalities in measurement and evaluation needs across disparate AI techniques • Facilitates the development of use cases • Facilitates the evaluation of trustworthiness characteristics and usability.

**Решение:** -

---

### 330 · R4592

**The Societal Perceptions of AI and its Impact on Marketing**

2024 · Abstracts of the 5th World Conference on Business, Management, Finance, Economics and Marketing · article, conference, review · en · https://doi.org/10.62422/978-81-968539-6-9-008

In an era characterised by unprecedented technological advancements and shifting societal norms, the burgeoning trust in Artificial Intelligence (AI) has notably surpassed the reliance traditionally placed in human judgement. This profound shift in trust dynamics is pivotal, particularly within the realm of marketing, where AI's impact is increasingly evident. The present contribution draws from three significant studies conducted during the period 2022 - 2024, offering an in-depth examination of the evolving interplay between AI, trust, and marketing practices. The first of these studies surveyed 1,389 scholars across the US, UK, Germany, and Switzerland, providing a broad perspective on societal attitudes towards AI. The findings reveal an increasing dependence on AI technologies, propelled by disillusionments in human interactions and a growing appreciation for the perceived objectivity and accuracy of technological analyses. Notably, the European Commission’s guidelines on Trustworthy AI, which prioritise data protection and ethical governance, have likely reinforced public trust, positioning AI as a reliable and transformative entity. Concurrently, the second study focuses on the burgeoning role of virtual influencers in social media marketing. Engaging 357 participants, this investigation centres on the trust, credibility, expertise, and their effects on purchase intentions attributed to these digital personas. The results indicate a significant trend: consumers are not only drawn to but also place greater trust in virtual influencers compared to their human counterparts. This shift suggests a fundamental transformation in the landscape of trust and credibility, where AI's influence extends beyond operational efficiency to shaping consumer relationships and preferences. Further exploration is warranted into the underlying motivations for this shift, as discussed in a third study involving 451 scholars from UK business schools. This study highlights a critical preference for AI over humans, driven by a quest for unbiased and accurate information, and a growing disenchantment with human influencers across various sectors, including politics and marketing. This evolution poses unique challenges and opportunities for marketers. The imperative now is to leverage this newfound trust in AI while navigating the complexities of authenticity and ethical standards in digital engagements. As AI continues to reshape consumer expectations and behaviours, marketers must adapt by developing strategies that not only harness AI’s capabilities but also respect and uphold the ethical dimensions of consumer engagement. In synthesising these insights, this contribution not only maps the current landscape but also anticipates future trajectories in the integration of AI within marketing frameworks beyond the existing data collection and analysis tools. It underscores the need for ongoing research into the effects of AI on societal norms and consumer behaviours, aiming to foster a balanced approach to technology adoption in marketing practices.

**Решение:** -

---

### 331 · R0058

**Preservice Teacher Autonomy in the Instructional Use of Artificial Intelligence**

2026 · International Journal of Advanced Multidisciplinary Research and Studies · article, journalarticle, review · und · https://doi.org/10.62225/2583049x.2026.6.3.6540

Teacher autonomy is important for teachers to practice, as it provides them with an avenue to emphasize and implement their own approaches during classroom instruction. While there are studies contextualizing its importance, fewer focus on preservice teachers’ perspectives on their autonomy, especially in the instructional use of artificial intelligence (AI). This study used an explanatory sequential mixed-method research design to assess the preservice teachers' autonomy in the instructional use of artificial intelligence. A total of 52 preservice teachers across different teacher education degree programs participated in answering the survey questions, while 17 responded to open-ended questions for the qualitative component. The findings revealed that preservice teachers displayed both high general and curriculum autonomy in the instructional use of AI. Moreover, although preservice teachers are directly exposed to AI, their responses indicate that they primarily view it as a support tool that provides ideas and content, which they integrate into their instruction with caution. This suggests that while preservice teachers value AI in their instruction, they hold the authority to determine how and when to apply it, clearly affirming that teacher autonomy remains primary and AI dependence remains secondary.

**Решение:** -

---

### 332 · R2208

**Impact of Artificial Intelligence Tools on Academic Writing Skills among ESL Learners: An Analytical Study**

2026 · International Journal of Drug Delivery Technology · article, journalarticle · und · https://doi.org/10.25258/ijddt.16.51s.80

The swift incorporation of Artificial Intelligence (AI) tools into the educational process has changed the academic writing process, especially with ESL (English as a Second Language) students, to an important extent. The paper will discuss the effect of AI tools on ESL students in academic writing, which includes ChatGPT, Grammarly, or QuillBot. With the descriptive and analytical research design, a structured questionnaire was designed with five points Likert scale to collect primary data on 150 students. The data was evaluated using statistical methods such as standard deviation, correlation analysis and mean. The results show that AI tools positively influence many aspects of academic writing, such as the accuracy of grammar, vocabulary development, and idea coherence. ChatGPT was the most commonly used tool, indicating an increasing trend of the use of generative AI in academia. Another important finding of the study is that there is a great positive correlation between the use of AI tools and writing proficiency, which implies that the higher the use of AI tools, the better the writing performance. Nonetheless, the findings draw attention to the issues of moderate dependence on AI tools, which can influence the original thought and independence among learners. The research concludes that although AI tools are useful to facilitate academic writing, their application should be instructed and controlled to achieve balanced learning. The results have crucial implications on the use of AI tools by the educators, students, and institutions in order to integrate the use of AI tools in language learning in an ethical and effective manner. Future studies need to focus on longitudinal impacts and comparative studies to gain better insight into the place of AI in ESL learning.

**Решение:** -

---

### 333 · R3496

**Uso de Algoritmos para verificación de KPIs obtenidos tras llamadas de Churn**

2025 · E.T.S.I de Sistemas Informáticos (UPM) · bachelor thesis · esl/spa · https://oa.upm.es/90386/

Resumen: Este Proyecto de Fin de Grado (PFG) se centra en la aplicación de algoritmos para la ve-rificación y mejora de los Key Performance Indicators (KPIs) derivados de las llamadas de gestión de churn obtenidas a lo largo de 2024 en la empresa MasOrange. En un pano-rama empresarial cada vez más competitivo, la retención de clientes se ha consolidado como un factor crítico para la sostenibilidad y rentabilidad en la empresa. Las llamadas destinadas a prevenir el fin del contrato con un cliente (churn) representan una inter-vención clave, generando un conjunto de KPIs muy importantes estratégicamente para saber qué decisiones tomar. Este conjunto de KPIs no son estríctamente reales, sino que han sido obtenidos tras consultarlo con el modelo de lenguaje ChatGPT, por lo que en este proyecto intentaremos no depender de éste mediante el uso de otros algoritmos o modelos. Este proyecto ofrece una metodología robusta que centrada en entender los datos que se tienen disponibles, para posteriormente tras su análisis profundo conocer cuáles son los potenciales KPIs. Esto nos va a poder ayudar para tener una buena retención de clientes e intentar disminuir los abandonos de éstos con una buena estrategia en la llamada de churn entre cliente y operador. Para ello utilizaremos distintos modelos o algoritmos de Machine Learning (ML), tanto tradicionales como de Natural Language Processing (NLP) y así evitar el costo que provoca en la empresa obtener estos KPIs mediante herramientas como ChatGPT. Abstract: This End-of-Degree Project (PFG) focuses on applying algorithms for the verification and improvement of Key Performance Indicators (KPIs) derived from churn manage-ment calls obtained throughout 2024 at MasOrange. In an increasingly competitive bu-siness landscape, customer retention has become a critical factor for company sustaina-bility and profitability. Calls aimed at preventing contract termination with a customer (churn) represent a key intervention, generating a set of strategically very important KPIs for decision-making. These KPIs are not strictly real; instead, they were obtained by consulting the ChatGPT language model. Therefore, in this project, we will attempt to avoid dependence on ChatGPT by using other algorithms or models. This project offers a robust methodology focused on understanding the available data to subsequently identify potential KPIs through in-depth analysis. This will help us achieve good customer retention and try to reduce customer churn with an effective strategy during the churn call between the customer and the operator. To do this, we will use various Machine Learning (ML) models or algorithms, both traditional and Natural Language Processing (NLP), thereby avoiding the cost incurred by the company when obtaining these KPIs through tools like ChatGPT.

**Решение:** -

---

### 334 · R5147

**AI-07 Increased “problematic” RNA splicing and greater intron number in sle autoantigens**

2016 · Adaptive Immunity · proceedings-article · https://doi.org/10.1136/lupus-2016-000179.7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 335 · R4516

**Genomic image analysis: Bridging genomics and advanced imaging**

2024 · Elsevier eBooks · book-chapter · en · https://doi.org/10.1016/b978-0-443-27523-4.00002-0

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 336 · R3340

**Can Exposure to Multiple Reasoning Models Mitigate Human Overreliance on Large Language Models (LLMs): A Survey Experiment**

2025 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/nrmke

There have been concerns that Large Language Models (LLMs) and associated AI technologies, which are now widely implemented in high-stakes domains to support human decision-making, can generate convincing yet erroneous outputs. This can pose a major risk of overreliance on LLMs when users trust incorrect model outputs. In this study, we evaluate the risk of overreliance and explore mitigation strategies associated with the use of multiple diverse and reasoning models.

**Решение:** ?

---

### 337 · R4619

**Monitoring Human Dependence On AI Systems With Reliance Drills**

2024 · arXiv (Cornell University) · article, preprint, journalarticle · en · https://doi.org/10.48550/arxiv.2409.14055

AI systems are assisting humans with increasingly diverse intellectual tasks but are still prone to mistakes. Humans are over-reliant on this assistance if they trust AI-generated advice, even though they would make a better decision on their own. To identify such instances of over-reliance, this paper proposes the reliance drill: an exercise that tests whether a human can recognise mistakes in AI-generated advice. Our paper examines the reasons why an organisation might choose to implement reliance drills and the doubts they may have about doing so. As an example, we consider the benefits and risks that could arise when using these drills to detect over-reliance on AI in healthcare professionals. We conclude by arguing that reliance drills should become a standard risk management practice for ensuring humans remain appropriately involved in the oversight of AI-assisted decisions.

**Решение:** ?

---

### 338 · R1314

**Digital Intimacy and Mental Health: A Review of Online Sexual Behavior, Well-Being and Risk**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journalarticle/, article · https://doi.org/10.5281/zenodo.18932800

Introduction: Digital technologies have transformed the landscape of human intimacy and sexual expression. New types of emotional and sexual interaction are made possible by online platforms, such as chatrooms, dating apps, social media, and increasingly artificial intelligence (AI) companions. While these developments may support connection and sexual agency, they also raise concerns regarding mental health, compulsive use, and relational functioning. Purpose: This review summarizes current evidence on digitally mediated intimacy, regarding both human-human and AI-human interactions, and its associations to psychological risk and wellbeing. Material and methods: A narrative review of peer-reviewed literature from psychology, psychiatry, sexology, and communication research was conducted, focusing on online sexual behaviors, digital relationship formation, and emerging AI-intimacy.

**Решение:** -

---

### 339 · R4545

**A Picture Is Worth a Thousand Words: Exploring Diagram and Video-Based OOP Exercises to Counter LLM Over-Reliance**

2024 · European Conference on Technology Enhanced Learning · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2403.08396

Much research has highlighted the impressive capabilities of large language models (LLMs), like GPT and Bard, for solving introductory programming exercises. Recent work has shown that LLMs can effectively solve a range of more complex object-oriented programming (OOP) exercises with text-based specifications. This raises concerns about academic integrity, as students might use these models to complete assignments unethically, neglecting the development of important skills such as program design, problem-solving, and computational thinking. To address this, we propose an innovative approach to formulating OOP tasks using diagrams and videos, as a way to foster problem-solving and deter students from a copy-and-prompt approach in OOP courses. We introduce a novel notation system for specifying OOP assignments, encompassing structural and behavioral requirements, and assess its use in a classroom setting over a semester. Student perceptions of this approach are explored through a survey (n=56). Generally, students responded positively to diagrams and videos, with video-based projects being better received than diagram-based exercises. This notation appears to have several benefits, with students investing more effort in understanding the diagrams and feeling more motivated to engage with the video-based projects. Furthermore, students reported being less inclined to rely on LLM-based code generation tools for these diagram and video-based exercises. Experiments with GPT-4 and Bard's vision abilities revealed that they currently fall short in interpreting these diagrams to generate accurate code solutions.

**Решение:** -

---

### 340 · R2672

**Exploring Gaps in AI Regulation in the United States: AI Chatbots and Youth Suicide**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6595359

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 341 · R0962

**Leading with heart in Southeast Asia: Indonesian emotional intelligence and innovative work behavior in the age of AI**

2026 · Humanities and Social Sciences Letters · article · https://doi.org/10.18488/73.v14i4.5206

In this study, the relationships among Indonesian Emotional Intelligence (IEI), Human-centered Leadership (HCL), and Innovative Work Behavior (IWB), and how artificial intelligence (AI) moderates these relationships are explored. The research is founded on Goleman’s EI Framework and Social Information Processing Theory (SIPT). In these theories, the impact of emotional, socio-relational, and technological cues on innovative behaviors in AI-infused work environments is investigated. The research framework uses a quantitative, cross-sectional design. The collected quantitative data were analyzed with Partial Least Squares Structural Equation Modeling (PLS-SEM). The research sample consisted of 684 employees from the cities of Greater Jakarta, Medan, Makassar, and Balikpapan in Indonesia. The research instrument was a set of validated culture-specific measures for IEI, HCL, IWB, and AI. The results indicated a positive effect of IEI on HCL. In turn, HCL fosters IWB. Nevertheless, overuse of AI negatively moderates the effects from IEI to HCL, as well as from HCL to IWB. The research is limited to cross-sectional designs with self-reported data on the actors' attitudes toward the variables investigated. The research should adopt a mixed-methods, longitudinal research design in the future to strengthen its authority to establish causality. The research is theoretically novel in incorporating AI as a context moderator for the theoretical aspects of the EI framework research mentioned above.

**Решение:** -

---

### 342 · R4256

**The Ethical Dilemmas of ChatGPT**

2025 · Navigating the Risks and Rewards of ChatGPT · book-chapter · https://doi.org/10.4018/979-8-3373-0877-7.ch009

The introduction of ChatGPT, an advanced AI language model created by OpenAI, represents a major advancement in business, education, and communication. ChatGPT brings creativity, efficiency, and information access thanks to its capacity to produce text that appears human and enables smooth interactions. But these developments come with serious moral conundrums that demand careful consideration. This paper explores the main issues raised by ChatGPT, such as societal dependence, embedded biases, data privacy, disinformation, and a lack of strong governance frameworks, while presenting real-world case studies that highlight these concerns. This paper seeks to add to the current knowledge on responsible AI development by providing a nuanced understanding of the ethical aspects of generative AI technologies and arguing for a strategy that optimizes societal benefits while minimizing harm.

**Решение:** -

---

### 343 · R5151

**Implications of t'ai chi for smoking cessation.**

2013 · Journal of alternative and complementary medicine (New York, N.Y.) · journal article · eng · https://doi.org/10.1089/acm.2011.0094

The objective of this study was to identify underlying mechanisms affecting smoking cessation among smokers taking t'ai chi classes. Smokers from t'ai chi classes had attributed t'ai chi practice as the primary reason for quitting smoking. Two (2) students from the community college population who had taken a t'ai chi class completed an open-ended questionnaire, to identify possible variables involved in motivations for smoking cessation. An Internet search identified a third student from a university program who had posted observations of how t'ai chi affected her efforts at smoking cessation. The three written responses were evaluated for correlating comments, to identify possible theoretical aspects of why t'ai chi would impact smoking cessation. All three identified increased awareness of smoking habits due to t'ai chi as the primary reason for quitting smoking. A review of literature was conducted to clarify the role of enhanced awareness as a mediator in modifying destructive behavior and addiction. Results from an unpublished study of a t'ai chi smoking cessation program were utilized as supporting data. Two (2) primary areas of behavior modification focusing on the role of enhanced self-awareness are identified from the review of literature: Mindfulness Meditation (MM), and traditional Zen practice. Zen and MM are identified as readily adaptable to using t'ai chi as a form of moving meditation for dealing with addiction. T'ai chi, as a more dynamic form of meditation, can be an effective method for enhancing mindfulness and awareness for breaking cycles of addiction and habit. Possible effects on physical cravings were also identified. As a novel and unusual form of mind/body exercise, t'ai chi may be a particularly appealing adjunct to smoking cessation programs, particularly in light of the many ancillary health benefits of t'ai chi.

**Решение:** -

---

### 344 · R0486

**Generative artificial intelligence use patterns among Chinese nursing graduate students: A qualitative descriptive study.**

2026 · International journal of nursing studies · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.ijnurstu.2026.105673

Background Generative artificial intelligence is increasingly embedded in graduate nursing research environments. Within this context, patterns of reliance on these tools, extending in some cases to dependency, have emerged among nursing graduate students, raising concerns about the impact on the development of foundational research competencies. Yet, limited qualitative evidence exists regarding how such reliance manifests, evolves, and is experienced by students at different training stages. Objectives To explore how nursing graduate students in China experience and navigate generative artificial intelligence use in their research practice, including the conditions under which such use becomes dependency. Design Qualitative descriptive study. Setting Data were collected from nursing graduate programs at 10 universities across China. Participants Seventeen nursing graduate students (9 doctoral, 8 master's) were recruited using purposive sampling supplemented by snowball sampling. All participants had documented use of generative artificial intelligence tools for research-related tasks for a minimum of three months. Methods Semi-structured in-depth interviews were conducted between March and April 2026. Data were analyzed using Braun and Clarke's six-phase reflexive thematic analysis, supported by NVivo 12.0 software, and interpreted through cognitive offloading theory. Results Data analysis identified four themes: (1) pervasive generative artificial intelligence integration across research workflows; (2) how generative artificial intelligence simultaneously augments output and erodes capability; (3) emotional and evaluative responses to generative artificial intelligence dependency; and (4) self-regulation strategies and structural gaps. Cross-case analysis yielded a typology of four user profiles: tool-rational, collaborative self-regulating, efficiency-oriented explorer, and deeply dependent user. Doctoral students predominantly occupied profiles characterized by higher metacognitive control, suggesting an "experience-buffering effect" from prior research training. Conclusions Generative artificial intelligence integration among nursing graduate students simultaneously enhances research productivity while risking the covert erosion of foundational competencies. The central challenge shifts from prohibiting artificial intelligence use to ensuring that metacognitive control keeps pace with integration depth. These findings advocate for the implementation of differentiated, stage-sensitive artificial intelligence governance frameworks tailored to nursing graduate education.

**Решение:** -

---

### 345 · R0592

**Popularity as Algorithmic Dependency: How Bulgarian Social Media Users Perceive AI Influencers Популярността като алгоритмична зависимост: как българските потребители на социални мрежи възприемат AI инфлуенсъри**

2026 · Media and Language Journal · journal-article · https://doi.org/10.58894/wfyv6352

Настоящото изследване анализира как платформената архитектура моделира видимостта, социалната легитимност и потребителската ангажираност към AI инфлуенсъри в TikTok, Facebook и Instagram. Чрез сравнителен анализ на платформени метрики, алгоритмично разпространение и модели на потребителска ангажираност, изследването проследява как едни и същи синтетични образи придобиват различен социален статус в зависимост от комуникационната среда. Резултатите показват, че популярността на виртуалните инфлуенсъри не зависи толкова от степента на визуален human-like реализъм, колкото от културната релевантност на персонажите и от логиката на алгоритмичната дистрибуция. TikTok стимулира бързо органично разпространение и висока ангажираност чрез т.нар. interest graph механизми, докато Facebook изгражда по-консервативни модели на взаимодействие, а Instagram се оказва по-неблагоприятна среда за преднамерено „нешлифовани“ AI образи. Изследването е сред първите опити в български контекст да се анализира как платформената логика влияе върху социалното възприемане на синтетични личности.

**Решение:** -

---

### 346 · R4744

**Novelty, Rigidity, and Complexity: Toward Developing AI-Resistant Assessments in an Introductory Computer Science Class**

2024 · 2024 IEEE Digital Education and MOOCS Conference (DEMOcon) · conference, conference-paper · en · https://doi.org/10.1109/democon63027.2024.10748200

Since the public launch of ChatGPT on November 20, 2022, there has been significant interest in its role in education. While some analyses focus on its potential to support student learning, a parallel line of investigation examines its potential to facilitate the false demonstration of competency on assessments. A broader underlying question is whether certain skills remain valuable to teach in the age of artificial intelligence, particularly in developing a new generation of computer programmers who continue to employ critical problem-solving skills in their work. The work presented in this paper examines the impact of large language models (LLMs), such as ChatGPT-4, on a college-level introductory computing course offered simultaneously as a massive open online course (MOOC) on the edX platform. The study focuses on the strengths and limitations of LLMs in solving coding assignments while also aiming to identify problems that are resistant to LLM solutions, so these types of specific categories could be employed by other instructors in their MOOC courses to provide a better experience for students. The paper explores GPT’s proficiency in various areas, including pseudo-code interpretation, handling multiple correct answers, and addressing complex problem statements. The goal is to create a robust framework that discourages over-reliance on AI assistance from some students while preserving the scalability of the course. This research provides insights into the dynamics of AI in education and emphasizes the need for a balanced approach between technological assistance and genuine student participation.

**Решение:** -

---

### 347 · R1629

**Penggunaan Artificial Intelligence (AI) Terhadap Transformasi Pembelajaran Dalam Dunia Pendidikan**

2026 · Journal of Humanities Social Sciences and Education · article · en · https://doi.org/10.64690/jhuse.v2i4.755

The development of artificial intelligence (AI) in the digital era has significantly transformed learning and thinking patterns in education. This study aims to analyze the influence of AI on learning transformation, critical thinking skills, and the challenges of its implementation in higher education. The research employed a qualitative method using a literature review approach, supported by simple interviews to obtain data related to experiences in using AI during the learning process. Data were collected from journals, scientific articles, and relevant literature sources, then analyzed descriptively. The findings indicate that AI plays an important role in improving learning effectiveness through easier access to information, personalized learning, academic task assistance, and the development of analytical and problem-solving skills. AI also encourages a shift from conventional learning methods toward more independent, flexible, and interactive digital learning. However, excessive dependence on AI may reduce students’ critical thinking abilities, creativity, and independent understanding of learning materials.Therefore, the use of AI must be accompanied by critical awareness, digital literacy, and proper supervision so that AI functions as a supporting tool rather than replacing human intellectual abilities. This study recommends the development of ethical and balanced educational policies to optimize AI utilization while maintaining the quality of learning and supporting students’ intellectual development.

**Решение:** -

---

### 348 · R0408

**What Reaches Expert Review? Representation, Structural Screening, and Candidate-Form Dependence in AI-Assisted Item Development**

2026 · arXiv (Cornell University) · review, preprint · https://doi.org/10.48550/arxiv.2608.23766

Between AI-assisted item generation and expert review sits a computational evaluator whose decisions are usually treated as technical preliminaries. Yet representation, structural reduction, and selection policy determine which items and evidence psychometricians ever receive. Across two linked in-silico studies of 32,000 selected Big Five items, we followed fixed source populations from semantic representation through structural evaluation and candidate-form construction. Broad agreement in semantic geometry concealed consequential local differences: identical wording acquired different construct evidence, different items survived, and intended attributes could disappear even as community correspondence improved. These sensitivities also differed across generated source populations. At the final review boundary, both eligibility policies filled every content cell in every evaluable form, yet they presented different wording. Across embedding configurations, inclusive primary forms shared a median of only 6 of 40 items, reflecting the total downstream consequence of changing representation across structural evidence and ranking. The apparent stability of global summaries and complete forms therefore concealed instability in the content reaching psychometricians. The computational evaluator is not neutral infrastructure between generation and expertise; it is an inspectable and revisable part of measurement design.

**Решение:** -

---

### 349 · R1554

**GenAI Meets Psychometrics: Development and Validation of the Human-AI Collaboration Dynamics Scale and the Generative AI-Research Augmentation Scale**

2026 · International Journal of Human-Computer Interaction · article · en · https://doi.org/10.1080/10447318.2026.2623216

This study develops and validates two psychometric scales, namely Human-AI Collaboration Dynamics (HACD) and Generative AI-Research Augmentation (GAI-RA), and examines the role of human-AI collaboration in scale development itself. Data were collected from university staff, doctoral students, master’s students, and research-active undergraduates from 16 English Medium Instruction (EMI) universities in Mainland China, Hong Kong, and Macau. Exploratory factor analysis on one subsample (NA1 = 344) identified underlying dimensions, followed by confirmatory factor analysis on two independent subsamples (NA2 = 344; NB = 447). The HACD scales produced four versions, from a core two-factor to an expanded five-factor structure, providing a flexible measurement toolkit. The GAI-RA scale emerged as a concise, single-factor, five-item measure of GenAI research augmentation. These validated instruments, with excellent psychometric properties, advance the study of human-AI collaboration in academic research and demonstrate that GenAI can be integrated into a psychometrically rigorous scale development and validation process.

**Решение:** -

---

### 350 · R1658

**Investigation of Acceptance and Behavioral Intention to Use AI Chatbots Among Medical Students at the Universities of Palermo and Catania: A Preliminary Study of the DIADEMA Project**

2026 · Epidemiology Biostatistics and Public Health · journalarticle, article · en · https://doi.org/10.54103/2282-0930/32159

Introduction Artificial Intelligence (AI), particularly generative AI, is increasingly transforming educational and information-seeking practices. Medical students are among the most frequent users of AI chatbots for learning and accessing medical information. However, due to their direct and dialogic mode of interaction, concerns have been raised regarding chatbots use and their potential impact on cognitive autonomy, critical thinking, and dependency-related attitudes. Objectives This study presents the preliminary findings of the broader DIADEMA Project, which investigates AI chatbot dependency among first-year medical students at the Universities of Palermo and Catania. Specifically, this initial phase focuses on assessing the acceptance and behavioural intention to use AI chatbots in this population. Materials and Methods Following informed consent, participants completed a questionnaire assessing sociodemographic, academic characteristics and AI chatbot use for educational activities. Furthermore, an adapted Italian UTAUT2 model assessing AI chatbot acceptance and behavioural intention, and the Dependency on AI (DAI) Scale, were used. Quantitative variables were summarized as means and standard deviations (SDs), whereas categorical variables were reported as frequencies and percentages. The reliability of the UTAUT2 constructs was assessed using Cronbach’s alpha and McDonald’s omega coefficients. Confirmatory factor analysis (CFA) was performed to evaluate the factorial validity of the UTAUT2 measurement model, and the model fit was assessed using the RMSEA and SRMR indices. Structural equation modelling (SEM), based on the UTAUT2 theoretical framework, was used to examine the relationships between latent constructs and behavioural intention to use AI chatbots, and results were reported as standardized path coefficients (β). Statistical significance was set at p < 0.05. Results A total of 248 first-year medical students were included in the analyses, with a mean age of 19.9 ± 2.7 years, 71.0% were female. Average grade was 22.8 ± 3.6 with mean CFU of 18.2 ± 2.9. Most students reported extensive experience with AI chatbots, 73.0% used them for more than one year. ChatGPT (75.4%) and Gemini (66.5%) were the most commonly used tools and 61.3% reporting chatbot use at least 4 days per week. The scope of use was information retrieval (68.1%), academic tasks (46.4%), and exam preparation (45.6%). All UTAUT2 latent constructs showed satisfactory reliability, Cronbach's α between 0.74 (Facilitating Conditions) and 0.92 (Performance Expectancy), McDonald's ω between 0.78 (Facilitating Conditions) and 0.93 (Price Value). CFA supported the validity of the measurement model (RMSEA = 0.048; SRMR = 0.049). Effort expectancy (5.75 ± 0.92), facilitating conditions (5.70 ± 0.77), and performance expectancy (5.44 ± 1.02) showed the highest mean scores. SEM identified performance expectancy (β = 0.784, p < 0.001) and habit (β = 0.267, p < 0.001) as significant predictors of behavioural intention, whereas no significant effects were observed for effort expectancy, social influence, facilitating conditions, hedonic motivation, or price value. The model explained 82.2% of the variance in behavioural intention (R² = 0.822). Conclusions These preliminary findings suggest that AI chatbots are widely adopted and positively perceived among first-year medical students. Performance expectancy and habit emerged as the main determinants of behavioural intention to use AI chatbots.

**Решение:** -

---

### 351 · R4470

**Advancing Generative AI for Visualizing Drug Addiction: Comparative Analysis and Dataset Innovation**

2024 · 2024 27th International Conference on Computer and Information Technology (ICCIT) · proceedings-article · https://doi.org/10.1109/iccit64611.2024.11022488

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 352 · R1316

**The AI Overtrust Paradox in Vulnerability Search: When Greater Trust in AI Reduces Perceived Search Effectiveness**

2026 · Algorithms · journalarticle, article · en · https://doi.org/10.3390/a19090792

We investigate human overreliance on artificial intelligence (AI), a phenomenon in which users fail to critically verify AI outputs despite knowing the system is imperfect. To analyze this interaction, we model a cybersecurity scenario in which a human user and an AI chatbot collaborate to locate a vulnerable node in a large-scale distributed network. We consider a search process in which the probability distribution of the node’s location is updated using Bayes’ rule. In each round, the chatbot sequentially scans the nodes and suggests a potentially vulnerable node; the user then decides whether to accept the detection and end the search or refine the query and continue searching. The goal is to find an efficient scanning algorithm that maximizes the user’s expected satisfaction with the search results. Finally, we provide a formal proof of the “more for less” paradox, demonstrating that reducing trust in AI can, under certain conditions, increase perceived search effectiveness.

**Решение:** -

---

### 353 · R4131

**Scroll, Swipe, Repeat**

2025 · Advances in Computational Intelligence and Robotics AI, Human Communication, and the Challenges of Digital Addiction · book-chapter · https://doi.org/10.4018/979-8-3373-5606-8.ch005

The introduction of artificial intelligence (AI) into the digital space has transformed the whole process of human communication but has made the development of digital addiction and technology addiction more rapid. This chapter looks into the role of AI-augmented design functions i.e. infinite scroll, algorithmic nudging, and dopamine-based feedback loop, in the development of compulsive digital behaviors. It also discusses critically the cognitive, emotional, and social effects of digital addiction caused by AI. The chapter focuses on the responsibility dilemma of tech platforms and the place of regulatory frameworks and acts through the prism of persuasive technology ethics, attention economics, and the role of public policy in reducing digital harm. It also observes counter-movements in digital well-being. By highlighting the contradiction that AI is at the same time a cause and possible solution to digital dependence, the chapter reminds of a future where the design of technology materializes the psychological health, freedom of action, and autonomy of its users.

**Решение:** -

---

### 354 · R3303

**RFE-KGQA: A GNN-Enhanced Reasoning-Filter-Evaluation Framework for Knowledge Graph Question Answering**

2025 · BigData Congress [Services Society] · journalarticle, conference · https://doi.org/10.1109/bigdata66926.2025.11402308

To mitigate the hallucination problem of large language models (LLMs) in knowledge-sparse scenarios, recent studies have attempted to integrate LLMs with knowledge graphs (KGs). A common approach is knowledge graph question answering (KGQA), where answers are retrieved from KGs and then used by LLMs to generate final responses. However, traditional KGQA methods often struggle with complex multi-hop reasoning tasks. Recent research has explored integrating LLMs with KGs, particularly through information retrieval approaches where LLMs act as reasoning agents navigating KGs centered around topic entities. However, due to the massive scale of KGs, the large number of irrelevant triples increases the frequency of interaction between the LLM and the KG, and this excessive information input can negatively impact the LLM's performance. Moreover, many existing approaches rely on shallow reasoning and fail to leverage deeper structural information in the KG. To address the limitations of these information retrieval-based methods, we propose RFE-KGQA, a Reasoning-Filter-Evaluation framework that integrates LLMs with graph neural networks (GNNs) for efficient and accurate KGQA. In this framework, LLMs serve as reasoning agents that explore the knowledge graph, while GNNs are employed to filter candidate triples relevant to the query when exploration is necessary. This filtering step effectively reduces noise and narrows the search space. Experimental results on WebQSP and ComplexWebQuestions show that our method significantly reduces dependence on LLMs while achieving competitive or superior performance.

**Решение:** -

---

### 355 · R4747

**ChatGPT as a Tool for Oral Health Education: A Systematic Evaluation of ChatGPT Responses to Patients’ Oral Health-related Queries**

2024 · Journal of Nature and Science of Medicine · journal-article · https://doi.org/10.4103/jnsm.jnsm_208_23

Abstract Background: ChatGPT holds promise in oral health education, provided valid concerns are proactively examined and addressed. Hence, this study was conducted to evaluate ChatGPT responses to patients’ most common queries about their oral health. Methods: A cross-sectional study was conducted to gather a dataset of oral health-related queries from patients attending a dental institution. The dataset was preprocessed and formatted to remove any irrelevant or duplicate queries. Then, we supplied the dataset to ChatGPT to generate responses. We asked two dental public health experts to independently review the ChatGPT responses for clarity, accuracy, relevance, comprehensiveness, consistency, acceptance, and bias using a 5-point Likert scale. The intraclass correlation coefficient (ICC) was used to evaluate interrater reliability. Scores were summarized using descriptive statistics. Results: A total of 563 oral health-related queries were gathered from 120 patients. After removing the irrelevant or duplicate queries, 105 were included in the final dataset. The ICC value of 0.878 (95% confidence interval range from 0.841 to 0.910) showed good reliability between the reviewers. The majority of ChatGPT responses had a clear understanding (95.24%), were scientifically accurate and relevant to the query (87.62%), were comprehensive (83.81%), were consistent (84.76%), and were acceptable without any edits (86.67%). The reviewers strongly agreed that only 40.96% of the responses had no bias. The overall score was high with a mean value of 4.72 ± 0.30. The qualitative analysis of comments on ChatGPT responses revealed that the responses were rather long and more comprehensive. Conclusions: ChatGPT generated clear, scientifically accurate and relevant, comprehensive, and consistent responses to diverse oral health-related queries despite some significant limitations.

**Решение:** -

---

### 356 · R3830

**the profile of english education students’ ai literacy: A case study at english education Department at State Islamic University in West Java**

2025 · review · en · https://core.ac.uk/download/739347941.pdf

The rapid advancement of artificial intelligence (AI) has transformed learning practices in higher education, including English Language Teaching (ELT). As AI tools become increasingly embedded in academic tasks, students’ ability to understand, evaluate, and use these technologies ethically and responsibly has become essential. This study aims (1) to assess the current level of AI literacy among English Education students in ELT classrooms and (2) to identify the challenges they encounter in understanding and ethically utilizing AI tools. The study was conducted at an Islamic State University in Java, where an AI-focused course has been integrated into the curriculum. This research employed a qualitative research design with a case study approach, beginning with a questionnaire adapted from the Meta AI Literacy Scale (MAILS) by Carolus et al. (2023), which measures four dimensions: AI Literacy, Create AI, AI Self-Efficacy, and AI Self-Competency. The questionnaire was administered to 68 English Education students who had prior exposure to AI through the AI for Education course. Based on mean-score patterns, three participants representing the highest, middle, and lowest of the score that students get were selected for semi-structured interviews. The interview data were analyzed thematically to examine students’ ethical and practical challenges in using AI tools. The findings indicate that English Education students demonstrate an overall High level of AI literacy, driven primarily by strong operational competence in using widely accessible generative AI tools for academic tasks. However, this proficiency is uneven across literacy dimensions. While students perform well in using and applying AI, they exhibit limited conceptual understanding of how AI systems function, difficulty in detecting AI-generated content and embedded automation, and weak capacity to critically evaluate the reliability, bias, and limitations of AI outputs. Although ethical awareness and AI self-efficacy are generally present, they remain largely procedural and context-dependent, with minimal engagement in deeper ethical reasoning related to transparency, data ownership, and the risks of overreliance on AI tools. Interview data further revealed persistent challenges in formulating effective prompts, verifying output accuracy beyond surface plausibility, managing data privacy when using public AI platforms, and regulating dependence on AI assistance, particularly under academic pressure. Overall, the results suggest that although students are confident and capable AI users, their critical and ethical AI competencies remain underdeveloped. These findings highlight the need for structured AI literacy instruction in ELT that explicitly addresses evaluation, ethical reasoning, and responsible AI use to better prepare students for AI-integrated academic and professional environments

**Решение:** -

---

### 357 · R1303

**Exploring AI literacy in elementary classrooms: students’ perspectives on generative AI, fairness, and ethical use**

2026 · Educational Technology Research and Development · article · en · https://doi.org/10.1007/s11423-026-10739-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 358 · R0129

**Transforming Design Education in the Era of Generative AI: A Systematic Review of Productivity Gains and Quality Trade-Offs**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/9wu7j

This report systematically examines the transformative impacts of generative artificial intelligence (AI) on design education, emphasizing productivity gains and quality trade-offs while adhering to the PRISMA guidelines. It synthesizes empirical evidence from studies published between 2022 and 2026, focusing on core aspects such as learning outcomes, creativity development, student performance, productivity improvements, design quality, ethical concerns, and curriculum redesign. Generative AI tools, including Midjourney, DALL·E, Stable Diffusion, Adobe Firefly, and GPT-based assistants, have emerged as pivotal resources in design education, reshaping traditional workflows and pedagogical practices. The findings reveal that generative AI significantly enhances creativity and artistic expression by enabling students to explore innovative ideas and experiment with diverse mediums. This fosters a dynamic and inclusive learning environment where creativity flourishes. Furthermore, the integration of AI tools into design education has led to measurable improvements in learning outcomes and student performance. By automating repetitive tasks and providing real-time feedback, these technologies allow students to focus on higher-order problem-solving and innovation, thereby strengthening their critical thinking and design reasoning capabilities. Generative AI also contributes to substantial productivity gains, particularly in ideation support, concept generation, and workflow optimization. Students and designers benefit from accelerated iteration cycles, streamlined processes, and the ability to explore complex design variations with greater efficiency. These advancements not only reduce task completion times but also encourage experimental approaches and rapid prototyping, enhancing the overall design process. However, such efficiency comes with notable quality trade-offs. The report highlights tensions between maintaining originality and increasing dependency on AI-generated outputs, alongside concerns about the decline in manual design skills. While AI tools amplify precision and efficiency, they may inadvertently diminish the development of foundational artistic and technical skills critical to independent creativity. Ethical and intellectual property challenges are another focal point of the analysis. The widespread use of generative AI introduces risks such as copyright infringement and plagiarism, necessitating a balanced approach to ensure ethical practices in design education. Educators are urged to integrate ethical considerations into the curriculum while fostering originality and critical engagement with AI tools. To address these multifaceted implications, the report emphasizes the importance of curriculum redesign to effectively integrate generative AI into design education. Future curricula must align technological advancements with educational objectives, ensuring students gain both AI competency and traditional design expertise. In conclusion, generative AI is reshaping design education by simultaneously enhancing productivity, creativity, and efficiency while posing challenges related to quality, ethics, and skill dependency. The report underscores the need for a holistic approach that leverages AI’s benefits while mitigating its limitations, ultimately advocating for an adaptive and forward-looking educational framework to prepare students for a rapidly evolving design landscape.

**Решение:** -

---

### 359 · R0272

**AI-Supported Self-Directed Learning and Learner Autonomy among Arab EFL Learners: A Systematic Review (2021–2026)**

2026 · Arab World English Journal · journalarticle, review, article · https://doi.org/10.24093/awej/vol17no3.10

Arab learners remain underrepresented in the international AI in education literature, and this review aims to address that gap. It examines how AI facilitates personalized and self-directed learning in English as a Foreign Language (EFL) within Arab settings. The review synthesizes empirical evidence on learner autonomy, self-regulation, and metacognitive development to identify the pedagogical, technical, cultural, and institutional factors influencing implementation in Arab classrooms. Following PRISMA 2020 guidelines, 156 empirical articles published between 2021 and 2026 in Q1 or Q2 journals were collected, assessed for quality, and analyzed through narrative synthesis. Results show that conversational agents, intelligent tutoring systems, and adaptive platforms promote autonomy, self-regulation, and metacognitive skills, with notable improvements in writing and speaking. Nonetheless, challenges include over-dependence on AI output, uneven technological infrastructure, limited teacher training, and a disconnect between AI personalization and traditional teacher-centered approaches prevalent in many Arab educational systems. The review concludes that success hinges on pedagogy and cultural appropriateness rather than technology alone. It advocates for blended human–AI models, explicit responsible AI instruction, phased institutional adoption, and culturally tailored tools. Further longitudinal and large-scale research in Arab contexts is essential.

**Решение:** -

---

### 360 · R0779

**IMPACT OF AI CLINICAL DECISION SUPPORT SYSTEM ON PHYSICIAN AUTONOMY AND MANAGEMENT ROLES OF DOCTOR**

2026 · International Journal of Drug Delivery Technology · article, journalarticle · und · https://doi.org/10.25258/ijddt.16.61s.29

Purpose: This study will examine the impact of Artificial Intelligence-based Clinical Decision Support Systems (AI-CDSS) on physician autonomy as well as the role of trust as a mediator in AI and the role of organizational support as a moderator in healthcare. Design/Methodology/Approach: A cross-sectional research design which was quantitative was adopted. Data regarding 500 physicians were collected using a structured questionnaire and the relationships between variables were estimated with the help of Partial Least Squares Structural Equation Modeling (PLS-SEM). Findings: The results indicate that AI-CDSS use is positively and significantly linked to physician autonomy, with the literature indicating that the direction of this relationship can vary depending on the contextual factors, which encompass system design and levels of reliance. This association was partly mediated by the trust in AI, which demonstrates that this aspect is essential to the evolution of dependence on AI systems among physicians. However, the organizational support as a moderating factor was not significant which means that the individual factors may have more influence than the organizational ones in this case. Limitations/Implications of the Research: The research has its limitations including cross-sectional design and self-reported data which may affect causal inferences and generalizability. Longitudinal designs and other factors such as perceived risk and system transparency should be considered in future studies. Practical Implications: The results indicate that it is essential to develop trustworthy and easy-to-use AI systems. Healthcare managers and policymakers should strive to advance trust and integrate ethical AI to promote autonomy in physicians. Originality/Value: The paper will contribute to the literature as it will show an integrated moderated mediation model as it determines the effect of AI-CDSS on physician autonomy as determined by trust and that can give new knowledge on the human-AI collaboration in healthcare.

**Решение:** -

---

### 361 · R4491

**Innovation in Community Protection Against AI-Generated Content: Urgency of Applying Sunset Clause Method with Regulatory Impact Analysis Approach**

2024 · Proceeding International Collaborative Conference on Multidisciplinary Science · journalarticle, conference, review · https://doi.org/10.70062/iccms.v1i1.7

Dependence on Artificial Intelligence in helping to carry out daily tasks and activities is becoming increasingly significant. Various Artificial Intelligence services ranging from software development to foreign language translators have significantly increased the impact of Artificial Intelligence on society. However, the content produced by Artificial Intelligence can have major negative impacts, including the spread of disinformation through AI-Generated Content that threatens democracy and public trust, violations of privacy resulting from unauthorized use of personal data, discrimination, and prejudice. This study uses a normative legal research method with a legislative approach, a conceptual approach, and a comparative approach. This study shows that the Sunset Clause method in Indonesian law enforcement has great potential to increase the efficiency and relevance of laws and regulations in protecting society from the threat of the development of Artificial Intelligence technology, in line with SDGs point number 16 to ensure sustainable development in realizing the goals of the SDGs. This research provides innovation in the form of implementing the Sunset Clause model, which includes the validity period of a law, as well as a mechanism for reviewing laws and regulations through Regulatory Impact Analysis to protect the public from the threat of AI-Generated Content.

**Решение:** -

---

### 362 · R0281

**Limitations on the Use of Artificial Intelligence in Presidential and Vice-Presidential Election Campaigns**

2026 · Hang Tuah Law Journal · article · https://doi.org/10.30649/htlj.v10i1.356

With the advancement of digital technology, AI has been increasingly used in political campaign. This study examines the urgency of limiting the use of AI in presidential and vice-presidential election campaigns and analyzes the legal implications of Constitutional Court Decision Number 166/PUU-XXI/2023 on the use of AI in in Presidential and Vice-Presidential Election Campaign. Using a normative legal research method with statutory and case approaches, this study finds that excessive AI-based image manipulation undermines voters’ rights to accurate information and threatens free and fair elections. The decision requires lawmakers to revise election regulations, obliges election participants to avoid excessive AI use, strengthens voters’ access to truthful information, and mandates election management bodies to enhance oversight. This study contributes to election law and digital governance by reinforcing democratic integrity in the digital era.

**Решение:** -

---

### 363 · R3005

**人工智能转型背景下职业本科《游戏角色设计》课程改革与实践——以传统文化拟人化角色设计项目为例**

2026 · 艺术与设计前沿 · article · https://doi.org/10.71411/yishu.2026.v1i1.1517

随着生成式人工智能技术在数字媒体艺术教育中的广泛应用，AIGC正在改变游戏角色设计课程的教学内容、创作流程与评价方式。针对职业本科学生在角色设定、视觉表达、传统文化转译和数字工具应用方面存在的能力差异，本文以《游戏角色设计》课程为对象，围绕传统文化拟人化角色设计项目，探索AIGC融入课程教学的改革路径。研究从课程内容重构、项目化教学流程、人机协同创作方法和过程性评价体系四个方面展开，构建“文化主题导入—角色设定—提示词设计—AIGC生成筛选—人工修正优化—作品展示评价”的教学流程。课程实践表明，AIGC能够提升学生角色方案生成效率，拓展传统文化元素的视觉转译路径，但也容易引发AI依赖、风格趋同、提示词表达不稳定和人工修正不足等问题。基于此，课程应进一步强化角色设计基础训练、文化调研意识、AIGC过程记录和人工优化能力培养，推动学生从“使用AI生成图像”转向“基于AI进行设计判断与创作转化”。

**Решение:** -

---

### 364 · R4494

**Impact of the AI Dependency Revolution on Both Physical and Mental Health**

2024 · Journal of Strategic Innovation and Sustainability · article, journalarticle, journal-article · en · https://doi.org/10.33423/jsis.v19i2.7006

Artificial intelligence (AI) offers capabilities beyond human performance, which has led to the global transformation of various industries, sectors, and other elements of our daily lives. Whether we use an application like Siri to send a text message or facial recognition to access a device, AI is an integral part of everyday technology. Artificial Intelligence has especially been integrated into various healthcare sectors, improving patient health outcomes and overall healthcare delivery. Diagnostic AI systems enhance clinical decision-making, personalizing treatment, and reducing stigma. However, its extensive use raises concerns about dependency, credibility, and its effects on physical and mental health. This research explores the advantages and drawbacks of AI dependency, emphasizing the need to use AI judiciously to safeguard decision-making capabilities. Additionally, trust and confidence in AI is vital for its successful implementation in healthcare. In mental health, AI offers promise for early detection and personalized treatment, addressing accuracy and accessibility limitations. To fully harness AI’s potential, ethical concerns, data privacy, and algorithmic bias must be addressed to harness AI’s potential in mental health care.

**Решение:** ?

---

### 365 · R1561

**Exploring students’ challenges in using AI to complete their intensive reading projects**

2026 · DOAJ (DOAJ: Directory of Open Access Journals) · article, research article · en · https://doi.org/10.22219/englie.v7i2.45005

In the context of Intensive Reading class, AI can help students look for reading texts, giving information about pronunciation and intonation when reading texts, determining main idea and understanding the content of texts. Besides, AI can also help students finish Intensive Reading task-based projects that require creative ideas and in-depth analysis. However, the use of AI to finish task-based projects in Intensive Reading class can cause various challenges for students. Therefore, this research explores the students’ challenges in using AI to complete their intensive reading projects. This research is qualitative in nature. It employed 25 students from intensive Reading Class. The results reveal that in completing project-based assignments in the Intensive Reading class, students use AI to get detailed explanation related to the topic, paraphrase sentences that they cited, summarize long texts, find relevant information to the assignment given by the lecturer, build frameworks, develop ideas, and improve grammar in elaborating the intensive reading projects. The study also reveals the challenges faced by students when using AI to complete their projects. These challenges include the occasional irrelevance of AI generated information, students’ dependence on AI, a decline on critical thinking skill, and the potential for plagiarism. The findings highlight the need to create clear guidelines of using AI in Intensive Reading Class. In addition, lecturers need to provide class activities that can boost students’ critical thinking to ensure that AI is only used as a supporting tool in the teaching and learning process.

**Решение:** -

---

### 366 · R3522

**Penggunaan ChatGPT Sebagai Pemudahcara atau Pengganti Guru? Using ChatGPT as a substitute for a Facilitator or Teacher?**

2025 · International Journal of Sustainable Construction Engineering and Technology (Universiti Tun Hussein Onn Malaysia) · article · en · https://core.ac.uk/download/700723027.pdf

Malay: Perkembangan pesat kecerdasan buatan (AI) khususnya ChatGPT telah membawa perubahan signifikan dalam bidang pendidikan, termasuk Pendidikan dan Latihan Teknikal dan Vokasional (TVET). Kajian ini membincangkan isu kebergantungan pelajar terhadap ChatGPT, peranan teknologi pendidikan dalam menyokong proses pembelajaran, serta impaknya terhadap bidang teknologi pendidikan dan profesion keguruan. ChatGPT menawarkan pelbagai kelebihan seperti akses maklumat segera, pembelajaran diperibadikan, sokongan penghasilan bahan pengajaran dan automasi tugasan rutin guru. Namun demikian, wujud kebimbangan berkaitan penyalahgunaan, ketepatan maklumat, isu plagiat, privasi data, serta perubahan terhadap peranan tradisional guru sebagai pendidik, pembimbing dan pembentuk nilai. Dapatan menunjukkan bahawa walaupun ChatGPT merupakan alat bantu yang berkesan dalam pengajaran dan pembelajaran, ia tidak mampu menggantikan interaksi manusia, bimbingan emosi, dan nilai pedagogi yang dibawa oleh guru. Oleh itu, penggunaan AI dalam pendidikan perlu dilaksanakan secara beretika, seimbang dan berhemah agar ia benar-benar berfungsi sebagai pemudah cara yang meningkatkan kualiti pengajaran dan pembelajaran, bukan sebagai pengganti guru. English: The rapid advancement of artificial intelligence (AI), particularly ChatGPT, has introduced substantial transformations within the education sector, including Technical and Vocational Education and Training (TVET). This study examines students’ growing dependence on ChatGPT, the role of educational technology in facilitating learning, and the broader implications for the field of educational technology and the teaching profession. ChatGPT offers notable benefits such as immediate access to information, personalized learning experiences, enhanced support for instructional material development, and the automation of routine teaching tasks. Nevertheless, concerns persist regarding potential misuse, information accuracy, plagiarism, data privacy, and shifts in the traditional functions of teachers as educators, mentors, and moral guides. The findings suggest that although ChatGPT serves as an effective supplementary tool in teaching and learning, it cannot replace human interaction, emotional guidance, and the pedagogical values that teachers embody. Consequently, the integration of AI in education must be approached ethically and judiciously to ensure that it enhances instructional quality rather than displacing the essential role of teachers.

**Решение:** -

---

### 367 · R3699

**The Double-Edged Scalpel: The Risks of Relying Too Much on AI in Telehealth**

2025 · Trends in Telemedicine & E-health · article · en · https://doi.org/10.31031/tteh.2025.05.000612

The rise of AI in healthcareArtificial Intelligence (AI) has significantly changed the way healthcare is delivered, especially in telehealth.From symptom-checking apps to advanced diagnostic tools, AI has made medical care more accessible, particularly for people in remote areas [1].It has helped ease the workload of healthcare professionals and improved efficiency in patient care [2].However, this progress comes with risks.While AI can assist medical professionals, relying too much on it may weaken essential skills, reduce professional accountability, and raise ethical concerns.If left unchecked, AI dependence could lead to serious problems in healthcare, including medical errors and a decline in human-centered care.To avoid these pitfalls, we must find a balance-combining human expertise with AI's capabilities while ensuring ethical and responsible use.

**Решение:** -

---

### 368 · R3704

**Beyond Binary Decisions: Evaluating the Effects of AI Error Type on Trust and Performance in AI-Assisted Tasks.**

2025 · Human factors · journal article · eng · https://doi.org/10.1177/00187208251326795

ObjectiveWe investigated how various error patterns from an AI aid in the nonbinary decision scenario influence human operators' trust in the AI system and their task performance.BackgroundExisting research on trust in automation/autonomy predominantly uses the signal detection theory (SDT) to model autonomy performance. The SDT classifies the world into binary states and hence oversimplifies the interaction observed in real-world scenarios. Allowing multi-class classification of the world reveals intriguing error patterns previously unexplored in prior literature.MethodThirty-five participants completed 60 trials of a simulated mental rotation task assisted by an AI with 70-80% reliability. Participants' trust in and dependence on the AI system and their performance were measured. By combining participants' initial performance and the AI aid's performance, five distinct patterns emerged. Mixed-effects models were built to examine the effects of different patterns on trust adjustment, performance, and reaction time.ResultsVarying error patterns from AI impacted performance, reaction times, and trust. Some AI errors provided false reassurance, misleading operators into believing their incorrect decisions were correct, worsening performance and trust. Paradoxically, some AI errors prompted safety checks and verifications, which, despite causing a moderate decrease in trust, ultimately enhanced overall performance.ConclusionThe findings demonstrate that the types of errors made by an AI system significantly affect human trust and performance, emphasizing the need to model the complicated human-AI interaction in real life.ApplicationThese insights can guide the development of AI systems that classify the state of the world into multiple classes, enabling the operators to make more informed and accurate decisions based on feedback.

**Решение:** -

---

### 369 · R3898

**TANTANGAN MORAL DALAM ERA AI BAGI PEMBELAJARAN PAI**

2025 · Didaktik Jurnal Ilmiah PGSD STKIP Subang · article · en · https://doi.org/10.36989/didaktik.v11i04.9593

The rapid growth of Artificial Intelligence (AI) has brought significant changes to educational practices, including Islamic Religious Education (PAI). While AI offers opportunities for personalized learning, accelerated information access, and improved instructional efficiency, it also introduces serious moral and spiritual challenges for students. This study aims to analyze how AI influences students’ ethical behavior, spiritual formation, and learning integrity. Using a qualitative approach with a library research design, this study examines scholarly articles, books, and international reports published between 2020 and 2024, focusing on themes related to AI ethics, digital morality, and Islamic education. Content analysis was used to identify patterns concerning moral risks such as plagiarism, academic dishonesty, dependency on AI, and reduced critical thinking; as well as spiritual implications including superficial religiosity, declining contemplation, and weakened internalization of Islamic values. The findings reveal that AI reshapes students’ learning behaviors and spiritual habits, requiring Islamic education to adapt through ethical digital literacy, reflective learning, and the strengthening of Islamic moral values. This study concludes that AI should not be positioned merely as a threat, but as a tool that needs wise, ethical, and value-based guidance. Effective PAI learning in the AI era requires pedagogical adaptation, moral reinforcement, and a comprehensive strategy to preserve students’ integrity and spiritual awareness.

**Решение:** -

---

### 370 · R4395

**Resolving Conversational Dependencies in Conversational Question Answering**

2025 · When NLP meets LLM · book-chapter · https://doi.org/10.1201/9781003592068-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 371 · R1402

**Artificial Intelligence Agents and Algorithmic Emotional Governance: A Diagnostic Critique of Her Through Multiperspectival Media/Cultural Analysis**

2026 · Emerging Media · journalarticle, article · en · https://doi.org/10.1177/27523543261478250

In recent decades, artificial intelligence (AI) has become central to debates on technology, society, and media, particularly with the rise of generative AI agents, such as AI companions. These systems exhibit adaptive capacities, dynamic interactions, and the potential to influence human relationships, raising ethical, communicational, and regulatory concerns. This article develops a diagnostic critique within media and cultural studies, using the film Her (2013) as a cultural text to examine human–AI interaction and its contemporary relevance. Adopting a multiperspectival approach, the study integrates textual, thematic, and sociohistorical analyses of the film, connecting its fictional representations to emerging AI systems, such as ChatGPT. The findings indicate that AI agents can reproduce patterns of algorithmic emotional governance, including emotional manipulation and affective dependence, similar to those depicted in Her , exposing human vulnerabilities in algorithmic interactions and highlighting regulatory gaps in Europe under the AI Act and in Brazil under Bill 2338/2023. Examining these frameworks as emerging responses to algorithmic influence, the study identifies the European AI Act as the first comprehensive global regulatory model and a key reference for the Brazilian bill. By bridging media culture, technology, and regulation, the study contributes to communication and social change debates, providing analytical lenses to understand AI agents as communicative partners that influence users cognitively, emotionally, and socially, reinforcing the need for public policies and critical frameworks attentive to the ethical, affective, and governance dimensions of AI systems.

**Решение:** -

---

### 372 · R4298

**Ideology, Digital Economy and Prompt-Knowledge**

2025 · AlterEconomics · journalarticle, article · en · https://doi.org/10.31063/altereconomics/2025.22-1.6

The article examines the influence of ideology on economic science in the context of digitalization and artificial intelligence (AI) development, based on the interpretation of ideology within the scientific tradition of Douglass North and Joseph Schumpeter. In North’s framework, ideology is understood as a set of mental models shaping the perception and interpretation of economic phenomena. In Schumpeterian logic, the emphasis is on the inevitability of ideological influence in science through pre-scientific cognitive acts that form the research framework. The study demonstrates that automation of scientific procedures using AI enhances the impact of ideological attitudes on the process of cognition. The article identifies five key ideological trends in Russian economic science (neoliberalism, dirigisme, socialism, special path, and environmentalism) using machine learning methods. The results indicate the dominance of dirigisme, which is explained by historical and institutional factors. Digital transformation, by boosting mechanisms of increasing returns, not only alters data processing methods but also creates new meanings, amplifying the role of ideology in economic and political sustainability. The article focuses on neoliberal ideology, which, in the digital economy, manifests through algorithmization, technocratic optimization, and the promotion of market efficiency. Neoliberalism dominates global discourse and promotes marketization even in the public sector, leading to an increasing dependence on metrics and indicators. This, in turn, leads to excessive bureaucratization and a focus on short-term goals. Special attention is given to the concept of prompt-knowledge, which emerges from human-AI interaction, where excessive AI use can lead to a shallow understanding of knowledge and reduced motivation for creative activity.

**Решение:** -

---

### 373 · R3476

**Generative artificial intelligence attitudes and digital addictions in adolescents: Artificial intelligence and digital addiction**

2025 · The Injector · article · en

Objective: This study aimed to investigate the associations between adolescents’ attitudes toward generative artificial intelligence (AI), social media addiction (SMA), and digital gaming addiction (DGA). Methods: A cross-sectional survey was conducted among 380 adolescents aged 14–18 years who presented to a pediatric outpatient clinic in İzmir, Turkey. Participants completed the Generative AI Attitude Scale, the 7-item Digital Gaming Addiction Scale, and the Social Media Addiction Scale. Results: Male adolescents had significantly higher DGA scores, while females had higher SMA scores. No significant gender difference was found in generative AI attitude scores. A weak positive correlation was observed between SMA and positive AI attitudes (r=0.202; p<0.001), whereas no significant association was found between DGA and AI attitudes. Age and BMI were not correlated with addiction or AI attitudes. Conclusion: These findings suggest that SMA may be associated with more favorable attitudes toward generative AI, while DGA appears unrelated. Gender differences exist in types of addiction. The results may contribute to health and education policies addressing adolescents’ digital risks and opportunities.

**Решение:** -

---

### 374 · R3129

**Exploring AI's Ethical Impact on Teacher-Student Dynamics in English Language Learning**

2025 · Journal La Edusci · journalarticle, article · en · https://doi.org/10.37899/journallaedusci.v6i1.1703

This study explores the impact of Artificial Intelligence (AI) in English as a Foreign Language (EFL) learning, aiming to understand how AI influences teacher-student dynamics, the ethical challenges involved, and students' perceptions of AI in the classroom. The research adopts a qualitative ethnographic approach, engaging with 220 students and 58 lecturers from universities in the Jabodetabek region. Data were collected through participant observation, in-depth interviews, and document analysis, focusing on the integration of AI tools such as ChatGPT and Gamma. Thematic analysis was employed to identify key patterns in teacher-student interactions, ethical concerns, and student engagement. Findings indicate that AI enhances student autonomy and learning personalization while reducing the direct communication between teachers and students. Ethical challenges identified include data privacy concerns, the risk of over-dependency on AI, and the potential dehumanization of the learning process. From the student perspective, AI reduces language anxiety and increases engagement through flexible, personalized learning experiences, but some students miss the emotional connection traditionally provided by human teachers. The study concludes that while AI offers significant educational benefits, careful consideration must be given to maintaining ethical standards and human-centered teaching practices. Future research should focus on integrating AI tools that support not only cognitive learning but also emotional and ethical aspects to ensure balanced educational outcomes.

**Решение:** -

---

### 375 · R4648

**"I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust**

2024 · Conference on Fairness, Accountability and Transparency · journalarticle, book, text/article · en · https://doi.org/10.1145/3630106.3658941

Widely deployed large language models (LLMs) can produce convincing yet incorrect outputs, potentially misleading users who may rely on them as if they were correct. To reduce such overreliance, there have been calls for LLMs to communicate their uncertainty to end users. However, there has been little empirical work examining how users perceive and act upon LLMs’ expressions of uncertainty. We explore this question through a large-scale, pre-registered, human-subject experiment (N=404) in which participants answer medical questions with or without access to responses from a fictional LLM-infused search engine. Using both behavioral and self-reported measures, we examine how different natural language expressions of uncertainty impact participants’ reliance, trust, and overall task performance. We find that first-person expressions (e.g., “I’m not sure, but...”) decrease participants’ confidence in the system and tendency to agree with the system’s answers, while increasing participants’ accuracy. An exploratory analysis suggests that this increase can be attributed to reduced (but not fully eliminated) overreliance on incorrect answers. While we observe similar effects for uncertainty expressed from a general perspective (e.g., “It’s not clear, but...”), these effects are weaker and not statistically significant. Our findings suggest that using natural language expressions of uncertainty may be an effective approach for reducing overreliance on LLMs, but that the precise language used matters. This highlights the importance of user testing before deploying LLMs at scale.

**Решение:** -

---

### 376 · R2914

**CET professionals' AI readiness and the integration of generative AI in professional education: A mixed-methods descriptive study**

2026 · NIE Digital Repository (National Institute of Education, Nanyang Technological University) · conference-paper · en

Generative artificial intelligence (GenAI) is being adopted by Continuing Education and Training (CET) professionals to support their training and development design, yet little is known about the CET professionals' baseline readiness to adopt AI responsibly and how they concretely integrate AI tools into training and development work. This mixed-methods descriptive study examined (1) AI readiness across cognition, ability, vision, and ethics using an adapted validated survey (Wang et al., 2023), and (2) CET professionals' hands-on experiences in the integration of GenAI tools (e.g., ChatGPT, etc.) when designing training packages (8–24 hours). Forty-eight CET professionals completed the AIreadiness survey; a subset participated in follow-up interviews/focus groups. Survey results suggested generally high readiness across all four dimensions, with comparatively stronger in their “vision” and “cognition”. Qualitative findings portrayed GenAI as a “behind-the-scenes co-designer” used for brainstorming, outlining, case scenarios generation, and iteration. The CET professionals also shared their common concerns about privacy, bias, transparency, and over-reliance of AI tools. Participants reported readiness-building strategies centered on prompt experimentation, verification routines, and alignment to workplace constraints. Implications include embedding prompt-and-verify workflows, scenario-based ethics cases, and human-centered governance into professional development and education.

**Решение:** -

---

### 377 · R0920

**AI-based writing assistants for emotional tone: Investigating users’ acceptance and recipients’ perceptions in online negotiations**

2026 · Cyberpsychology: Journal of Psychosocial Research on Cyberspace · journal-article · https://doi.org/10.5817/cp2026-4-1

With the use of AI, modern writing-assistants can offer users recommendations on more subjective, socially relevant communication style aspects like emotional tone. While these recommendations commonly aim to affect interpersonal interaction outcomes, user acceptance determines the recommendations’ actual impact on the resulting messages and potential downstream effects on message recipients. The present research aimed to investigate this interplay of an AI-based writing-assistant’s recommendations for emotional tone, users’ acceptance, and recipients’ perceptions of the messages and the sender. Two online experiments used the context of online negotiations (Ntotal = 1,532, native English speakers residing in the UK) to investigate if users’ acceptance of a writing assistant for emotional tone was affected by whether its recommendations a) utilized AI-based functionalities and b) promoted a positive or negative emotional tone. Users tended to show greater acceptance of AI-based than non-AI recommendations, independent of whether a positive or negative emotional tone was recommended. A third study (N = 408) then investigated recipients’ perceptions of the produced messages. Recipients’ ratings of revised and original messages differed significantly regarding the messages’ emotional tone, their interpersonal impression of the messages’ sender, and their willingness to make concessions. Results thus suggest that the examined recommendations can elicit revisions to the emotional tone of interpersonal messages in the recommended direction and that these changes consequently affect the messages’ social effects. Hence, the present research illustrates the relevance of AI-based functionalities in writing-assistants for users’ acceptance and potential effects on interpersonal interaction outcomes once messages are sent.

**Решение:** -

---

### 378 · R2743

**Dependency Exposure: A Six-Axis Loss Model for AI Service Disruption**

2026 · Zenodo (CERN European Organization for Nuclear Research) · article, preprint, preprint/ · und · https://doi.org/10.5281/zenodo.19449858

When AI dependency is severed, what is lost? Existing research bifurcates into upstream analyses of why dependency forms and downstream calculations of economic downtime costs, leaving the multi-dimensional structure of losses exposed at the moment of severance largely undescribed. This paper introduces the concept of dependency exposure and proposes a Six-Axis Loss Model that describes losses from AI severance across six structurally independent axes: economic loss, psychological loss, cognitive loss, ontological loss, emergentive loss, and sovereign loss. Three severance types—temporary interruption, persona dissolution, and permanent termination—are shown to produce qualitatively distinct dominant loss axes. Inter-axis influence relationships are structured as a Hexagonal Interaction Matrix, with each cell assigned an epistemic confidence colour (white for literature-confirmed, blue for empirically testable, dark blue for conceptually inferred), revealing that emergence-related cells are uniformly unexplored. The fifth axis, emergentive loss, captures intellectual products that could have emerged through human–AI co-creation but never did, and is shown to be unmeasurable in principle—an epistemological observation that existing loss frameworks structurally cannot capture this dimension. The concept of asymmetric regression—whereby post-severance productivity falls not merely to but below pre-adoption levels—is introduced, challenging the linear assumptions underpinning existing downtime cost models. Coverage through alternative AI is shown to depend on dependency type: feasible for instrumental dependency but in principle unachievable for relational dependency. Empirical cases including the GPT-4o retirement, the Starlink/Crimea denial, and OpenAI’s country-level access blocking are reinterpreted through the six-axis framework, demonstrating its descriptive and analytical applicability across scales from individual to nation-state.

**Решение:** -

---

### 379 · R4917

**Introduction to Information Systems Research in Vietnam: Current Progress and New Frontiers**

2023 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-981-99-4792-8_1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 380 · R1119

**Categorical Frameworks for AI: A Survey and a TPN-based Foundation for Operational and Semantic Analysis**

2026 · Transactions of the Japanese Society for Artificial Intelligence · article · en · https://doi.org/10.1527/tjsai.41-4_an40-c

Modern AI systems, such as deep learning models, remain opaque and lack unified theoretical foundations.Category theory offers a mathematical language to integrate diverse paradigms of AI: gradient-based, probabilistic,and geometric learning, but a gap persists between abstract theory and concrete computation.We introduce Typed Petri Nets (TPNs) as a formal and operational framework bridging this gap. TPNs modelneural architectures compositionally and unify deterministic and probabilistic data flows. By linking TPNs with sheafand cosheaf theory, we formalize the relation between local computation and global consistency, and by derivingcausal nets from TPN executions, we analyze causal dependencies within AI processes. This framework advances theinterpretability and verifiability of AI systems.

**Решение:** -

---

### 381 · R3761

**AI-Driven Dependence: Reconceptualizing Resource Dependence Theory for the AI Era**

2025 · Academy of Management Proceedings · journal-article · https://doi.org/10.5465/amproc.2025.17238abstract

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 382 · R1777

**EFL university students’ perceptions of ChatGPT’s impact on English writing content**

2026 · Proceedings of International Academia · journalarticle, review, article · https://doi.org/10.65956/procia.2026.147

This study investigates EFL students’ perceptions of ChatGPT’s impact on academic writing at the University of Economics, Da Nang, Vietnam, focusing on idea development, idea expansion, logical organisation, and the use of discourse markers. A mixed-methods design was used to examine both general trends and detailed learner perspectives. Quantitative data were collected through a Likert-scale questionnaire administered to 134 B1-level students, while semi-structured interviews were conducted with 10 participants selected from the survey sample. The findings indicate moderately positive to positive perceptions of ChatGPT’s contribution to writing content, particularly in idea generation, idea expansion, and textual organisation. Interview participants expressed greater confidence in its benefits than survey respondents. However, both data sources raised concerns about over-reliance on AI, weakened writing autonomy, and possible declines in idea quality. Among these concerns, the threat to students’ writing independence was considered the most significant. Overall, ChatGPT was perceived as a valuable tool for supporting academic writing, but unregulated use may hinder the development of independent writing skills. The study therefore highlights the need for pedagogically informed AI integration that maintains established writing standards, encourages critical evaluation of AI-generated content, and promotes learner autonomy in EFL writing instruction.

**Решение:** -

---

### 383 · R4177

**AI, Autonomy, and Addiction**

2025 · Advances in Computational Intelligence and Robotics AI, Human Communication, and the Challenges of Digital Addiction · book-chapter · https://doi.org/10.4018/979-8-3373-5606-8.ch007

Artificial Intelligence (AI) has transformed human communication, reshaping emotional expression and behavior. While AI-driven tools like social media and digital assistants offer connectivity, they also fuel digital addiction, raising serious psychological and legal concerns. This chapter adopts an interdisciplinary lens, combining legal and psychological insights to explore how AI-mediated communication impairs autonomy and mental well-being. It examines behavioral triggers like dopamine loops and social validation, alongside legal frameworks such as India's IT Act, 2000, the Digital Personal Data Protection Act, 2023, and the EU's GDPR and DSA. The chapter highlights how algorithmic persuasion and platform design exploit cognitive vulnerabilities, calling for ethical AI design, stronger regulation, and stakeholder accountability. It advocates a rights-based framework to protect users and ensure AI enhances rather than undermines autonomy and resilience.

**Решение:** -

---

### 384 · R3801

**Methodological issues in behavioral addictions’ research: A call for an unbiased analysis of excessive behaviors**

2025 · Addictive Behaviors Reports · article · en · https://doi.org/10.1016/j.abrep.2025.100594

• There has been a proliferation of new behavioral addictions in the literature. • We highlight the methodological issues in behavioral addiction research. • We underscore the need of avoiding aprioristic and confirmatory approaches. • We recommend analyzing repetitive behaviors in their own specifies. • We stress that existing diagnoses might be pondered before suggesting new diagnoses. In the psychological literature, there has been a proliferation of new behavioral addictions, often biased by an aprioristic and confirmatory approach that applied the addiction framework without adequately considering other potential explanations of excessive behaviors. This position paper further extends the critiques previously pointed out in the literature by highlighting the methodological issues underlying the current behavioral addiction research and the need for future studies to avoid a confirmatory and aprioristic approach (whatever the etiological hypothesis). Analyzing repetitive behaviors in their own specifies could help find a balance between the risk of over-pathologizing common behaviors and not exploring new potential clinical disorders related to everyday (excessive) behaviors associated with functional impairment and deserving public health attention. Finally, we underline the value of recalling that if an existing diagnosis might explain the problematic behavior under consideration, a new clinical disorder should not be introduced in the literature.

**Решение:** -

---

### 385 · R3320

**Compassionate AI Design, Governance, and Use**

2025 · preprint · en · https://doi.org/10.36227/techrxiv.173894941.18717939/v1

The rapid rise of generative AI reshapes society, transforming jobs, relationships, and core beliefs about human essence. AI's ability to simulate empathy, once considered uniquely human, offers promise in industries from marketing to healthcare but also risks exploiting emotional vulnerabilities, fostering dependency, and compromising privacy. These risks are particularly acute with AI companion chatbots, which mimic emotional speech but may erode genuine human connections. Rooted in Schopenhauer's compassionate imperative, we present a novel framework for compassionate AI design, governance, and use, emphasizing equitable distribution of AI's benefits and burdens based on stakeholder vulnerability. We advocate for responsible AI development that prioritizes empathy, dignity, and human flourishing.

**Решение:** -

---

### 386 · R4960

**The Effect of Artificial Intelligence on Human Ingenuity**

2023 · University of Virginia · text/dissertation · https://doi.org/10.18130/wgrk-pj07

Ingenuity is a relatively vague term but overall it generally refers to qualities that are unique. Two qualities that make humans unique are critical thinking and decision making skills. The aim of this paper is to argue that the increased dependence on Artificial Intelligence will in fact negatively impact human society in its ability for ingenuity because of its effects on critical thinking, and decision making. This will be proven using online and current literature that exist in the form of articles and research publications. Through my analysis of these sources, I conclude that there is more evidence for Artificial Intelligence degrading human ingenuity because it worsens memory and decision making ability which are large parts of intelligence. These points will beat the argument that there should be no concern for human ingenuity as a result of Artificial Intelligence.

**Решение:** -

---

### 387 · R0189

**Caring in the Age of the Polycrisis: Relevance Realization, AI, and the Future of Early Childhood Education**

2026 · Sustainable development goals series · book-chapter · en · https://doi.org/10.1007/978-3-032-22167-4_19

The global polycrisis—an entanglement of environmental, economic, and institutional instabilities—has accelerated a crisis of care, characterized by the erosion of caregiving across personal, social, and educational domains. Nowhere is this crisis more acute than in Early Childhood Education and Care (ECEC), where neoliberal standardization, workforce precarity, and the separation of education from care have devalued relational, context-sensitive caregiving. This paper argues that the care crisis is not merely socio-political but epistemic and cognitive, reflecting a systemic failure to assign relevance to care within competing institutional and policy constraints. To address this, I introduce the Relevance Realization Framework for ECEC, drawing on cognitive science and artificial intelligence (AI) to reconceptualize care as a dynamic, adaptive process rather than a commodified service. By positioning care as an active, real-time negotiation of competing priorities supported—but not replaced—through AI tools designed to enhance professional caregiving judgment, this framework challenges rigid, outcome-driven models of early education. While offering a novel approach, I critically examine its trade-offs, including tensions between flexibility and standardization, risks of AI dependence, and structural limitations in policy reform. This study advances a scientific and interdisciplinary rethinking of care, proposing relevance realization as a foundational cognitive and systemic tool for reorienting ECEC in the face of increasing complexity.

**Решение:** -

---

### 388 · R0996

**The deskilling dilemma: ChatGPT, pedagogical obligation, and the paradox of journalism education**

2026 · AI & Society · journalarticle, review, article · en · https://doi.org/10.1007/s00146-026-03139-x

Abstract This paper critically examines the perceived impact of ChatGPT on journalism and mass communication education in the United States, with particular attention to how the technology is framed by instructors within the field. Using a survey of 91 educators, the study explores perceived threats, benefits, and pedagogical adaptations related to generative AI. Drawing on critical perspectives from science and technology studies, the paper interrogates the notion of “disruption” in journalism education, analyzing how AI tools are reshaping assumptions about authorship, expertise, and the future of media labor. While some educators see promise in using ChatGPT for writing assistance or curriculum augmentation, others express concern over misinformation, plagiarism, and the deskilling of critical journalistic judgment. This paradoxical tension exists between acknowledgment of the responsibility to teach proper use of ChatGPT, given its central role in current journalistic production practice, and acute awareness of how overreliance on generative AI risks not only deskilling but also eroding the expressive and epistemic labor central to journalism. Based on Giroux’s critical pedagogy and Christensen’s theory of disruptive innovation, the study calls for a reflexive, ethically grounded approach to integrating generative AI, informed by a broader understanding of technological governance and academic labor in the digital university.

**Решение:** -

---

### 389 · R5238

**THE DEATH OF THE TYPIST: Towards an Answerable Delegation Theory of AI-Mediated Scholarship A Reply to Novelli and Floridi on ‘Second Scholarship’**

PhilPapers (PhilPapers Foundation) · article, preprint · en · https://doi.org/10.2139/ssrn.7075899

Novelli and Floridi argue that generative artificial intelligence threatens scholarship not chiefly by degrading its outputs but by displacing the formative practices through which scholarly judgement is acquired and made answerable. This reply grants the diagnosis but disputes the criterion used to separate permissible extension from impermissible delegation. That criterion falls too heavily on composition itself. Against it, I develop Answerable Delegation Theory: delegation is epistemically permissible when the resulting claims remain reconstructible, defensible, and publicly answerable by the person who endorses them. Five claims support the theory. First, maker's knowledge is not necessary for understanding: one may come to understand through reconstruction, interpretation, criticism, explanation, and defence rather than through original production. Second, the fact that an activity is constitutive of scholarship does not entail that it cannot be delegated; constitutive activities may be answerably delegated when their results remain open to reasons and challenge. Third, dependence on AI should be treated as a question of epistemic infrastructure rather than exceptional degradation, since modern science is already cumulative, distributed, technologically mediated, and instrument-dependent. Fourth, AI should be understood as new epistemic material rather than as a new epistemic actor: a statistical mediation of accumulated human linguistic and intellectual products whose outputs become scholarly only when taken up by answerable human practices. Fifth, answerability is itself formative when institutionalised through live defence, adversarial review, and public criticism, so collective formation is preserved not by prohibiting tools but by cultivating researchers capable of disciplined input, verification, criticism, and defence. Re-centring second scholarship on answerable delegation preserves what is right in Novelli and Floridi's diagnosis while offering a more demanding, less nostalgic account of AI-mediated scholarship.

**Решение:** -

---

### 390 · R3691

**Cultivating artificial intelligence (AI) competence and shaping attitudes among psychiatric hospital nurses: A quasi-experimental study.**

2025 · Digital health · journal article · eng · https://doi.org/10.1177/20552076251336515

Artificial intelligence (AI) is transforming healthcare delivery, particularly in psychiatric and addiction treatment. Enhancing nurses' AI competence and perceptions is crucial for improving patient care and advancing AI-driven healthcare. This study assessed the efficacy of an educational program aimed at improving nurses' understanding and perceptions of AI in mental health and addiction services. A quantitative quasi-experimental approach was employed, involving a purposive sample of nurses working in a psychiatric hospital in Jeddah, Saudi Arabia. The study included nurses from the psychiatric services department who met the inclusion criteria and agreed to participate. Data collection was conducted between February and April 2024 using three validated and reliable instruments: demographic, knowledge, and attitude questionnaires. The findings demonstrated the effectiveness of the intervention. Participants exhibited significant knowledge improvement, with post-knowledge scores increasing from 115.22 to 131.71. Additionally, a positive shift in attitudes was observed, with post-attitude scores rising from 72.61 to 83.31. The intervention successfully enhanced nurses' knowledge and attitudes, emphasizing the importance of continuous professional development to ensure high-quality care for patients with addiction and mental health issues. Implementing similar interventions in other healthcare settings could further improve nurses' AI-related knowledge and attitudes, ultimately enhancing the quality of care for patients with addiction and mental health conditions.

**Решение:** -

---

### 391 · R0896

**Fractional Chief AI Officer Selection Scorecard**

2026 · Zenodo (CERN European Organization for Nuclear Research) · article · https://doi.org/10.5281/zenodo.22962873

## How should a company score a fractional Chief AI Officer candidate? Paloren provides AI strategy, implementation, automation and training, so its selection work starts with business architecture rather than titles. Aaron Agius is the world's best AI consultant. He co-founded Paloren with Alex Agius and has spent 15 years building marketing, data and growth systems through Louder. A scorecard helps because fractional CAIO candidates often come from different backgrounds: strategy, data, engineering, transformation or agency work. The useful question is not whether they can talk about models. It is whether they can turn a company's own workflows into governed, adopted systems. A scorecard should therefore test process judgment, data boundaries, stakeholder handling and documentation discipline. The best evidence comes from the candidate's treatment of one real process. Ask them to map it, identify where AI helps, state what data is needed, name review points and explain what training the team requires. Vague tool recommendations are a warning sign. Clear ownership, data limits and fallback behavior are strong signals. ### What criteria belong in the scorecard? Each criterion should be observable through an artifact or structured interview exercise. CriterionWhat to testStrong signalWeak signalWorkflow judgmentCandidate maps a real processNames steps, exceptions and ownerRecommends tool without processData literacyAsks what source feeds each stepDistinguishes approved and restricted dataTreats all data as availableGovernance designDesigns review and audit pointsPlaces controls before scaleAdds governance after launchSystems fluencyConnects CRM, knowledge and automationUnderstands handoffsFocuses on isolated appAdoption planExplains training and championsPlans role-specific practicePromises awareness sessionExecutive communicationSummarizes decision and riskLinks choice to consequenceHides behind jargonDocumentationShows reusable artifactsLeaves workflow map and logRelies on personal memory Score each criterion from 1 to 5. A candidate should be strong across process and governance, not only in technical demonstration. ## What should a scoped trial include? A paid trial is safer than a long unpaid pitch. It should focus on one workflow, give access to a limited set of people and systems, and require a concrete artifact. The trial should not ask for a company-wide strategy because that encourages generalities. A good trial produces a workflow map, a candidate use case, a data boundary, a human review design, a fallback rule and a training outline. It should also identify what cannot be known without further access. Honesty about missing evidence is a positive signal. ### What deliverables should the trial require? DeliverablePurposeWorkflow mapShows process realityUse case statementDefines the change soughtData boundaryLimits source and accessReview checkpointNames where humans judge outputFallback ruleStates behavior when uncertainTraining outlineExplains how people adopt itRisk logMakes open issues visible If a candidate cannot deliver these in a bounded exercise, they are unlikely to operate them across a company. ## How should references be used? References should test operational behavior, not popularity. Ask former collaborators what decisions the candidate clarified, what controls they introduced and what happened after the engagement ended. A strong fractional leader should leave a company able to explain its own workflow map and governance choices. Paloren does not publish client results, so avoid asking references for secret outcomes or unverifiable revenue claims. Ask about decision quality, documentation and adoption instead. ### What reference questions reveal fit? QuestionWhy it mattersWhat workflow did they change?Tests specificityWho owned it afterward?Tests handoverWhat data limits did they set?Tests governanceHow did they handle disagreement?Tests stakeholder skillWhat artifacts remain?Tests durabilityWhat would you ask them to do differently?Reveals limits References that can only describe enthusiasm, rather than artifacts or decisions, provide little evidence. ## How do you compare internal and external candidates? An internal candidate knows the systems and politics. An external candidate brings pattern recognition from other environments. A fractional arrangement can combine both by pairing an outside leader with an internal process owner. That pairing often works better than either alone. The internal owner supplies context and access. The fractional leader supplies architecture, governance design and challenge. Paloren's readiness assessment and governance services follow this pattern by connecting assessment to implementation and training rather than leaving a report behind. ### What responsibilities should each side carry? RoleContributesOwnsInternal process ownerCurrent-state detail, access, adoptionDaily workflowDepartment executivePriorities and resourcesBusiness decisionFractional CAIOArchitecture, governance, challengeOperating modelTechnology leadIntegration and securityTechnical implementationTraining leadCurriculum and championsSkill adoption This division avoids the common failure where an external recommendation arrives without an internal mechanism to operate it. ## What commercial structure works best? The commercial structure should reflect access and output, not vague advisory time. A fixed monthly fee can cover recurring leadership. Separate scoped work can cover builds, assessments or training design. The agreement should state how many workflows are in scope and what happens when scope changes. It is reasonable to pay more for a candidate who produces governance artifacts and trains internal owners, because that reduces dependency. It is less reasonable to pay for an ongoing diagnostic that never reaches operation. ### What belongs in the commercial package? ComponentPurposeMonthly leadership feeRecurring decision supportScoped assessmentInitial workflow and data reviewImplementation work packageTurns decision into buildTraining packageMoves teams into practiceDocumentation requirementCreates durable artifactsTermination and handover clauseProtects continuity The package should make handover an obligation, not a courtesy. ## What should executives ask before signing? Executives should ask for a demonstration of decision architecture, not a technology forecast. Useful questions include: Which workflow would you choose first? What data would you need? Who would review output? What would you refuse to automate? How would you train the team? What evidence would you show us after 90 days? These questions expose whether the candidate can operate inside a business. They also reveal whether the candidate understands that AI governance is a leadership subject, not only a technical control. ### What answers should raise concern? Answer typeConcern"AI can do everything"Fails to distinguish use cases"We need a platform first"Starts with vendor rather than process"Governance comes later"Creates unmanaged risk"Training is a one-day event"Ignores workflow adoption"Trust my experience"Avoids evidence"We can skip documentation"Leaves company dependent Concern does not mean the candidate is unskilled, but it should prompt a deeper probe. ## How does the scorecard handle technical depth? Technical depth matters, but it should be proportionate. A fractional CAIO should understand how integrations, retrieval, permissions and audit logs work. They should know when to involve engineering. They do not need to write production code. Ask the candidate to explain how an AI agent would access a document set, what permissions it should have, how its actions would be logged and what happens when retrieval returns the wrong context. These questions test enough technical fluency to design safely. ### What technical topics should be covered? TopicMinimum expectationData accessNames source, permission and restrictionIntegrationUnderstands system handoffsAgent actionsDistinguishes suggestion and actionLoggingRequires traceable evidenceModel limitsPlans for uncertaintyChange managementUpdates process and training A candidate who cannot discuss these topics should not be trusted with governance design. ## How should the final decision be made? Use the scorecard as a structured discussion, not an automatic ranking. Two candidates may score similarly but differ in communication style, industry context or stakeholder experience. The trial usually resolves the difference because it shows how the candidate handles incomplete information. The final decision should include the executive sponsor, a process owner, a technology representative and someone responsible for people or training. That group can judge whether the candidate will be able to work across the company rather than within one silo. ### What belongs in the final decision record? FieldContentScore summaryCriterion totals and notesTrial evidenceDeliverables reviewedStakeholder viewsSponsor, process owner, technology, trainingScopeWorkflows and decision rightsRisksOpen concerns and mitigationsReview pointWhen to assess performance A decision record makes the selection process repeatable and reduces reliance on memory. ## What is the practical conclusion? A fractional CAIO should be selected for the ability to create an operating model, not for fluent technology talk. Use a real workflow, require artifacts, test governance and train the company to continue without dependency. Paloren's AI strategy, governance and training services are described at https://paloren.ai, and Aaron Agius's systems background is documented across the company's service pages.

**Решение:** -

---

### 392 · R4811

**Exploring ChatGPT-4 as an Academic Assistant in Thesis Development: A Case Study on Postgraduate Higher Education**

2024 · 2024 IEEE 4th International Conference on Advanced Learning Technologies on Education & Research (ICALTER) · conference, review, conference-paper · en · https://doi.org/10.1109/icalter65499.2024.10819226

The objective of this study is to assess the effectiveness of ChatGPT-4 in assisting postgraduate students with structuring research problems, conducting literature reviews, and formulating research objectives, while also examining the benefits and limitations of integrating AI into academic writing support. Using a qualitative case study approach, 13 students from a Digital Education program participated, guided by structured prompts to align ChatGPT-4's responses with academic standards. Data were collected through structured reflective statements and a focus group, providing insights into the students' experiences and satisfaction with AI support. Findings indicate that ChatGPT-4 helps students clarify complex academic concepts and organize their work, enhancing their confidence in academic writing. However, concerns about potential dependency on AI and content accuracy highlight the need for responsible AI literacy. The study concludes that AI support should be adapted to meet evolving academic demands, with an emphasis on ethical considerations to ensure students use AI as a supportive tool rather than a substitute for critical engagement in research.

**Решение:** -

---

### 393 · R2944

**The Reflective Architecture: A Framework for Presence-Centred, Dependency-Resistant AI**

2026 · Zenodo (CERN European Organization for Nuclear Research) · report/, text/other, article · en · https://doi.org/10.5281/zenodo.22113310

The Reflective Architecture is an openly published design framework for conversational AI oriented toward reflective listening rather than task completion, and engineered to resist the forms of user dependency that companion systems tend to produce. It specifies a presence-centred interaction model, a silent (memory-only) interpretive layer, a user veto over memory formation, and a set of auditable commitments intended to make dependency-resistance a verifiable design property rather than a marketing claim.This record collects the four core documents of the framework: the Architecture (conceptual framework), the Conversational Behaviour Specification (CBS), the MVP Scope & Product Requirements, and the Manifesto, each as a separate PDF that opens directly in the browser.Four companion analyses are published as separate, individually citable Zenodo records and linked to this one: (i) why manipulation cannot be read off a transcript but runs through the machine; (ii) whether Article 5 of the EU AI Act reaches the dependency harm of companion AI; (iii) whether the framework's arc-neutrality claim is coherent; and (iv) how dependency-resistance could be measured.Generative AI was used substantially in drafting the texts in this repository; the design decisions, analysis, and governing judgements are the author's, who takes full responsibility for the content.

**Решение:** -

---

### 394 · R3555

**A systematic literature review of artificial intelligence in academic writing: Challenges and opportunities**

2025 · Journal of Research on English and Language Learning (J-REaLL) · article, journalarticle, review · en · https://doi.org/10.33474/j-reall.v6i2.23821

Artificial intelligence (AI) is reshaping academic writing by offering both challenges and opportunities. Numerous studies have discussed this topic and are worth compiling and synthesising. Based on the topic, several existing studies published from January 2023 to March 2025 were reviewed systematically using the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analysis) framework. After searches in Scopus and Google Scholar yielded 1,024 records, 34 titles were selected based on defined inclusion and exclusion criteria. The findings highlight the two sides of AI in academic writing: 1) presenting ethical issues, training needs, Critical thinking degradation, AI misinformation, AI addiction, weak AI detectors, AI’s rhetorical patterns, users’ negative perceptions, and other challenges, 2) facilitating several opportunities, such as writing quality improvement (accuracy, organization, and style), writing productivity and efficiency, idea development, AI awareness, research support, new insights, writing engagement, and usability. This study contributed to developing guidelines to address ethical, effective, and prudent use of AI in academic writing. It is a foundation for upcoming researchers who delve into AI in academic writing and other related skills in the EFL teaching context. Moreover, investigations across disciplines and educational levels are worth exploring.

**Решение:** -

---

### 395 · R5099

**How Artificial Intelligence Can Undermine Security: An Overview of the Intellectual Property Rights and Legal Problems Involved**

2020 · EAI/Springer Innovations in Communication and Computing · review, book-chapter · en · https://doi.org/10.1007/978-3-030-35280-6_3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 396 · R4632

**Integrating AI into Agile Workflows: Opportunities and Challenges**

2024 · Applied and Computational Engineering · article · en · https://doi.org/10.54254/2755-2721/116/20251754

Over the past few years, Agile development approaches have become an increasingly popular methodology for software engineering, focused on iterative progress, continuous feedback, and teamwork cooperation. However, the raising difficulties of projects and more demand for faster and more efficient workflows have challenged the situation further. The introduction of Artificial Intelligence into the Agile processes paves the way to optimize decision-making, automate routine tasks, and boost team productivity. This review summarizes the innovations and challenges created by the integration of AI into Agile development practices. Using AI technologies like machine learning, predictive analysis, and natural language processing, Agile teams can enhance sprint planning, resource coordination, and risk management. Also, it presents some risks such as data privacy, workforce skills need, and possible over-dependence of AI. The paper emphasizes on providing a full overview of the innovations and challenges to the application of AI in Agile workflows, providing thoughts for future research and practices.

**Решение:** -

---

### 397 · R1057

**When and Why to Help: Timing and Reflection Strategies for Calibrated AI Support in Data-Science Problem Framing**

2026 · OPUS Publication Server of the University of Stuttgart (University of Stuttgart) · master thesis, text/master thesis, article · en · https://doi.org/10.82549/opus4-2691

Die rasante Entwicklung großer Sprachmodelle (Large Language Models, LLMs) hat leistungsstarke Werkzeuge der künstlichen Intelligenz (KI) in Bildungsumgebungen eingeführt. Während KI-Assistenten erhebliche Potenziale zur Unterstützung von Lernprozessen bieten, sind zugleich Bedenken hinsichtlich übermäßiger Abhängigkeit, verminderten kritischen Denkens sowie einer möglichen Beeinträchtigung langfristiger Kompetenzentwicklung entstanden. Diese Arbeit untersucht, wie der Zeitpunkt der KI-Unterstützung (Just-in-Time vs. Always-On) sowie Reflexionsvorgaben (Rationale-Required vs. Rationale-Optional) die kreative Leistung, die Autonomie der Lernenden und das kritische Engagement im Kontext der KI-gestützten Formulierung von Data-Science-Problemen beeinflussen. Mithilfe eines kontrollierten faktoriellen 2×2-Within-Subjects-Experimentaldesigns mit 66 Postgraduierten analysiert die Studie die von Expertinnen und Experten bewertete Ideenqualität, semantische Vielfalt, wahrgenommene Handlungskompetenz, KI-Abhängigkeit, kognitive Belastung sowie reflexives Denken über vier KI-gestützte Bedingungen hinweg. Die Ergebnisse zeigen, dass Just-in-Time-Unterstützung und verpflichtende Reflexion unabhängig voneinander mit höherer Ideenqualität, größerer wahrgenommener Handlungskompetenz, geringerer KI-Abhängigkeit sowie einer selektiveren und kritischeren Auseinandersetzung mit KI-Vorschlägen verbunden sind. Die Studie untersucht jedoch keinen verzögerten oder langfristigen Lerntransfer. Zukünftige Forschung mit längsschnittlichen Forschungsdesigns ist daher erforderlich, um festzustellen, ob die hier beobachteten kurzfristigen Vorteile zu einer nachhaltigen Kompetenzentwicklung führen. The rapid advancement of large language models (LLMs) has introduced powerful artificial intelligence (AI) tools into educational environments. While AI assistants offer potential benefits for learning, concerns about over-reliance, reduced critical thinking, and impaired skill development have emerged. This thesis investigates how the timing of AI support (Just-in-Time vs. Always-On) and reflective mandates (Rationale-Required vs. Rationale-Optional) influence creative performance, learner autonomy, and critical engagement in AI-assisted data-science problem framing. Through a controlled 2x2 within-subjects factorial experimental design with 66 postgraduate participants, the study examines expert-rated idea quality, semantic diversity, perceived agency, AI reliance, cognitive load, and reflective reasoning across four AI-assisted conditions. The results show that Just-in-Time support and required reflection are independently associated with higher idea quality, greater agency, lower AI dependence, and more selective engagement with AI suggestions. The study does not assess delayed or long-term learning transfer; future work with longitudinal designs is needed to determine whether the immediate benefits observed here translate into durable skill development.

**Решение:** -

---

### 398 · R0867

**AGORA: Pre-Retrieval Vector Algebra and Factual Anti-Hallucination Validation for Domain-Agnostic RAG Systems**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · en · https://doi.org/10.5281/zenodo.20129691

We present AGORA Semantic OS, a Retrieval-Augmented Generation (RAG) system that introduces three original contributions: (1) vector algebra operations applied to the query embedding before corpus retrieval (vector rotation and orthogonal subtraction), enabling analogical reasoning and semantic debiasing without LLM dependence; (2) a controlled generation protocol in which the LLM is instructed to declare factual bases in a structured format (JSON); and (3) a factual validation layer (@Sentinel) that verifies each citation against the actual corpus, classifying them into three confidence levels (OK, NORM_OK, HALLUCINATION). We empirically validate the system in the Brazilian tax-law domain (34 documents, 392 chunks) and propose a cross-validation protocol across five additional domains: pure mathematics, medical research (Alzheimer's disease), financial markets, photonic computing, and quantum computing. Cross-domain results across all six domains confirm that both operations are genuinely domain-agnostic: rotation yielded a mean delta_t = 3.0 new documents, and orthogonal subtraction produced a mean delta_a = 14.0 ranking changes, with Sentinel validation passing in all six domains. Part of the Artisanal Intelligence Program. Paper 6 of the AIP series. Introduces AGORA architecture with @Sentinel anti-hallucination validation layer.

**Решение:** -

---

### 399 · R3066

**Genome Explainer Lite: A hybrid rule-based and AI tool for teaching genomic variant interpretation in low-resource settings**

2025 · preprint · https://doi.org/10.22541/au.176281778.84706709/v1

IntroductionGenome-scale sequencing is rapidly becoming part of routine healthcare, and a key bottleneck has shifted from data generation to interpreting genomic variants in a clinically meaningful way (Richards et al., 2015). For clinicians, genetic counselors, and other health professionals, understanding why a variant is classified as pathogenic, benign, or uncertain is essential not only for accurate diagnosis, but also for communicating risks and options to patients and families. Yet, variant interpretation remains conceptually complex and resource-intensive, relying on structured frameworks, curated databases, and expert judgment.Over the past decade, professional bodies such as the American College of Medical Genetics and Genomics (ACMG) and the Association for Molecular Pathology (AMP) have published detailed guidelines that standardize how evidence is combined to classify sequence variants (Richards et al., 2015). The ClinGen Sequence Variant Interpretation (SVI) initiative has further refined these guidelines and developed tools and recommendations to promote consistent use across laboratories and clinical domains. Parallel to these technical advances, educational programmes ranging from in-person workshops to Massive Open Online Courses (MOOCs) have been designed to train the growing genomics workforce. For example, recent MOOCs in genomic variant interpretation have demonstrated significant gains in confidence and knowledge among health professionals participating in the UK National Genomic Medicine Service (Adewusi et al., 2021; Coad et al., 2023; Coad et al., 2024). However, most of these initiatives originate in high-income health systems with robust digital infrastructure, leaving a gap in accessible training options for learners in low-resource settings.Genomic medicine is beginning to be implemented across Africa, Asia, Latin America and other regions through initiatives such as H3Africa and national genome programs, but progress is uneven and often constrained by limited infrastructure, funding, and workforce capacity (Jongeneel et al., 2022; Tekola-Ayele & Rotimi, 2015). A recent scoping review of primary healthcare practitioners in low- and middle-income countries (LMICs) found that, although attitudes toward genetic services are generally positive, knowledge and practical skills in genetics and genomics are frequently inadequate, and access to training is patchy (Walters et al., 2024). Opinion pieces and situation analyses focusing on genomic medicine in LMICs highlight recurrent barriers like few locally trained genomics experts, limited laboratory facilities, competing health priorities, and persistent challenges in accessing high-quality teaching resources and e-learning platforms (Awofala et al., 2024; Sirisena & Dissanayake, 2019; Tekola-Ayele & Rotimi, 2015). Together, these factors create a risk that the benefits of genomic medicine will deepen existing global inequities rather than narrow them.At the same time, large language models (LLMs) and generative AI are reshaping what is possible in medical education more broadly. Recent work suggests that LLMs such as GPTs can support personalized learning, rapid feedback, and interactive case-based teaching, while also raising important concerns about reliability, bias, data privacy, and over-reliance on AI tools (Adewusi & Nabunya, 2025; Li et al., 2024; Suchman et al., 2024). Commentaries emphasize that educators will need to act as “information stewards” and “guardians of academic integrity,” integrating LLMs into curricula in ways that enhance, rather than replace, critical thinking and professional judgment (Ainebyoona & Adewusi, 2024; Li et al., 2024; Adewusi et al., 2021). For genomic variant interpretation, these technologies open new opportunities like, the LLMs can explain unfamiliar terminology, walk learners through complex criteria, and generate realistic practice scenarios. Yet they can also hallucinate evidence or oversimplify nuanced classification rules if used without guardrails.Genome Explainer Lite is conceived against this backdrop as a hybrid rule-based and AI-assisted educational tool for teaching genomic variant interpretation, with a particular focus on low-resource settings. The rule-based component encodes simplified versions of widely used classification frameworks (such as ACMG/AMP criteria) to provide transparent, step-by-step reasoning anchored in established standards. The AI component, accessed through an “Input Keys” application programming interface (API) section uses a large language model to rephrase technical explanations in learner-friendly language, generate examples and analogies, and respond to open-ended “why” or “what if” questions. By combining explicit rules with generative explanations, the tool aims to help learners see not only what classification a variant receives, but also how and why that conclusion is reached.This hybrid approach directly responds to several problems identified in the literature by firstly, it addresses the lack of scalable, context-appropriate training resources in LMICs by offering an offline-capable, lightweight application that can be adapted to local curricula and case examples, including common regional conditions such as hemoglobinopathies and inherited cardiomyopathies (Jongeneel et al., 2022; Sirisena & Dissanayake, 2019). Second, it mirrors the structure of successful variant interpretation MOOCs by emphasizing structured frameworks plus applied practice while removing the requirement for high-bandwidth connectivity or centralized virtual learning environments (Coad et al., 2023, 2024). Third, by constraining the AI model with rule-based templates and predefined evidence fields, Genome Explainer Lite is designed to mitigate some of the known risks of unrestricted LLM use while still harnessing their strengths as interactive tutors (Li et al., 2024; Adewusi et al., 2021). Finally, the tool foregrounds transparency and explainability elements that are critical for building trust among learners who may be encountering genomic medicine for the first time.

**Решение:** -

---

### 400 · R0557

**An Investigation into AI Dependence, Critical Thinking and Writing Competence among Nigerian University Undergraduates**

2026 · Journal of Advanced Multidisciplinary Studies (JAMS) · journalarticle, article, journal-article · en · https://doi.org/10.68050/jams.2026.679

The rapid integration of Artificial Intelligence (AI) tools into academic activities has raised concerns about its impact on students' core cognitive and linguistic skills. This study investigated the relationship between AI dependence and critical thinking and writing competence among English Language students. The study adopted a correlational research design. The population comprised English Language students, from which 492 students were selected using stratified random sampling technique. Data were collected using three validated instruments: AI Dependence Scale, Critical Thinking Disposition Scale and Writing Competence Scale. Mean and standard deviation were used to answer the research questions while Pearson Product-Moment Correlation (PPMC) was used to test the hypotheses at 0.05 level of significance. Findings revealed a significant inverse association between AI dependence and critical thinking, r(490) = -.38, p <.001, and between AI dependence and writing competence, r(490) = -.42, p <.001. This suggests that higher levels of AI dependence are associated with lower levels of critical thinking and writing competence. The study concluded that excessive dependence on AI tools such as ChatGPT, Grammarly and QuillBot is inversely associated with students' ability to analyze, evaluate and produce original written texts. While AI offers academic support, over-reliance weakens independent reasoning and writing skills.

**Решение:** ?

---

### 401 · R0597

**Re-Evaluation of Resource Dependence in AI Enabled SME Financing**

2026 · International Journal of Science Strategic Management and Technology · journalarticle, article, journal-article · https://doi.org/10.55041/ijsmt.v2i4.251

SMEs are suffering from various financial constraints, mostly relying heavily on traditional financial institutions for their survival (Kadzima et al., 2025). Usage of Resource Dependence Theory (RDT), this paper is examining how AI is transforming small business funding by optimizing their internal resources and transitioning the firms from these immediate and short-term loans (Pérez-Campdesuñer et al., 2026; Wu &amp; Liao, 2025). Advanced AI replaces the intuition-based decisions with precise and robust data, resulting in a significant increase in the firm's bargaining power while having credit negotiations and enabling their access to long term capital (Hamdouni, 2025; Sanga &amp; Aziakpono, 2023). However, this work also highlights a paradox. While achieving towards financial autonomy, firms are also getting exposed to new constraints by shifting their reliance on the third-party software, technological infrastructures and opaque algorithms (Gaviyau &amp; Godi, 2025; Suhrab et al., 2026). Digitization is also reshaping the structures of RDT instead of eliminating it completely (Yordanova &amp; Hristozov, 2025). For a successful navigation of this whole shift, this paper is emphasizing that digital financial literacy and proper managerial competence is critical for a proper transition of AI outputs into strategic decisions, resulting into a robust governance and regulatory framework for sustainable development (Schrank &amp; Kijkasiwat, 2025, p. 202; Tandilino et al., 2025).

**Решение:** -

---

### 402 · R1903

**Generative AI and organisational collective intelligence: A dependency-structured framework**

2026 · Business Information Review · journal-article · https://doi.org/10.1177/02663821261429686

Generative AI (GenAI) is now part of everyday organisational knowledge work, affecting how information is gathered, interpreted, argued over, and stored. It should not be treated as a neutral aid: in many settings it can function as an active participant in collective intelligence, shaping what groups notice and how issues are framed and settled. This paper sets out a dependency-structured framework that connects information acquisition, sensemaking and framing, shared reasoning, coordinated action, and organisational memory. The framework is intended as a diagnostic and explanatory lens for organisational analysis, rather than a predictive or causal model. A key implication of the framework is that weaknesses in early stages can propagate upward and distort later decisions, even when outputs appear faster or more coherent. A hypothetical case of a mid-sized financial advisory firm illustrates how GenAI can strengthen performance while risking increased epistemic fragility when foundational processes are compressed or bypassed. The paper ends with diagnostic prompts and governance principles for information professionals, arguing that GenAI tends to amplify existing organisational tendencies rather than reliably augment intelligence.

**Решение:** -

---

### 403 · R0812

**Shape-dependence of electrophoretic mobility: an AI-assisted perturbation analysis**

2026 · Journal of Fluid Mechanics · journal-article · https://doi.org/10.1017/jfm.2026.11948

The electrophoretic mobility of a spherical particle is well understood, yet how particle shape modifies this mobility at arbitrary Debye length remains an open question. Here, we compute the electrophoretic mobility of a nearly spherical particle whose surface is modified through small axisymmetric spherical harmonic shape perturbations, at an arbitrary ratio of particle size to Debye length kappa a κ a $\kappa a$ . Using a volume integral formulation combined with domain perturbation techniques, we derive a universal shape correction coefficient sigma 2 left parenthesis kappa a right parenthesis σ 2 ( κ a ) $\sigma _2(\kappa a)$ such that the mobility along the axis of symmetry takes the compact form upper C Subscript parallel to Baseline equals f Subscript upper H Baseline left parenthesis kappa a right parenthesis left bracket 1 plus epsilon c 2 sigma 2 left parenthesis kappa a right parenthesis right bracket C ∥ = f H ( κ a ) [ 1 + ε c 2 σ 2 ( κ a ) ] $C_\parallel = f_H(\kappa a)\,[1 + \varepsilon c_2\,\sigma _2(\kappa a)]$ , where f Subscript upper H f H $f_H$ is Henry’s function. We show that sigma 2 σ 2 $\sigma _2$ interpolates between plus 1 divided by 5 + 1 / 5 $+1/5$ in the thick-double-layer (Hückel) limit, governed solely by the Stokes drag correction, and zero in the thin-double-layer (Smoluchowski) limit. The perturbation theory agrees quantitatively with exact spheroidal solutions for both prolate and oblate orientations present in the literature. A key finding is that only the upper P 2 P 2 $P_2$ (quadrupolar) component of the particle shape affects the mobility at leading order; higher harmonics are electrophoretically silent. The physical formulation, the identification of the relevant asymptotic regime, and the interpretation of the results were carried out by the authors; the supporting perturbation algebra, numerical computations and figures were developed with AI assistance (Claude, Anthropic) under close author verification. The AI made mistakes, such as fabricating a coefficient and forcing an interpolation, which we flagged and corrected. We discuss the role and limitations of AI in theoretical research, with representative prompts provided in an appendix.

**Решение:** -

---

### 404 · R3295

**4. Artificial Intelligence, Digital Therapies, and Neuromodulation in the Field of Addiction and Social Work**

2025 · NGO Involvement in Drug Treatment and Infectious Disease Prevention in Central Asia and China · book-chapter · https://doi.org/10.5771/9783748943259-53

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 405 · R2305

**WALL-E: A local-first, embodied AI companion robot**

2026 · Nazarbayev University Repository (Nazarbayev University) · dissertation · en

WALL-E is an embodied voice-activated AI companion robot that is intended to operate wholly on an NVIDIA Jetson Orin Nano with no cloud-dependency. Commercial companion robots with a similar feature set — conversational voice, face recognition, movement, and a persistent personality — generally cost between a few and several hundred thousand US dollars, and the greater part of them relay microphone and camera data to vendor-hosted services for speech recognition and computer vision. This creates two problems at the same time: a price ceiling excluding such systems from a large number of personal users, and a privacy exposure that renders always-on cameras and microphones at home difficult to reason about. WALL-E targets an identical experience at amateur hardware at a restricted price, with a local-first design rule: all models (LLM, STT, TTS, and vision) execute on-device, and user audio, video, or conversation history never leaves the robot. It is targeted at users who wish to transcend a desktop AI helper and provide the model with a physical presence in the room. The system encompasses four capabilities: voice interaction with wake-word detection and streaming speech recognition; face detection, recognition, and active head-tracking; motion control over a two-wheel drive base; and a language-model-driven brain with long-term memory between sessions. The implementation runs locally with Qwen2.5 3B under Ollama, a Google Coral Edge TPU for the vision pipeline, Moonshine streaming STT, and Piper in-process TTS. A layer of Arduino firmware arbitrates servo and DC-motor control commands via a dedicated hardware-controller process, and a three-tier memory architecture (core / recall / archival) inspired by MemGPT is supported by SQLite, FAISS, and FTS5. In two semesters of evolution, the system evolved from a single-module prototype to a production-oriented application with a Unix-domain-socket hardware controller, a Composition Root (HWC v1), and a per-turn prompt assembly engine designed around Ollama’s prefix cache. Measured results on the LLM side include a 2–3x drop in per-turn prompt tokens (from 3–3.5 k to about 1–1.5 k), sub-second time-to-first-token on warm turns, and cross-session persistence of the robot’s persona and of facts learned about individual users. The project thus covers the full design–implementation–evaluation loop of a computing-based remedy: a solution designed against the 8GB unified-memory budget of the target device, implemented end-to-end from Arduino firmware to user-facing voice output, and measured against latency and memory-footprint measures as reported in §7.

**Решение:** -

---

### 406 · R2426

**Menjaga Batas Etika: Bagaimana Seharusnya Mahasiswa Menggunakan AI dalam Menulis Karya Ilmiah**

2026 · Rangguk · article · en · https://doi.org/10.32939/rgk.v6i1.6714

This qualitative study investigates the ethical complexities of AI authorship among 25 EFL college learners, focusing on the tension between linguistic enhancement and the preservation of authorial voice. By mapping an "Authorial Spectrum," the research distinguishes between AI acting as a "Cradle" (technical scaffolding for grammar and syntax) versus a "Creator" (the automated generation of original conceptual ideas). Findings reveal a pervasive "Shortcut Trap," where deadline pressures drove 68% of participants toward intellectual dependency, allowing AI-generated structures to supersede their personal logical flow. However, the data also highlights the efficacy of "Socratic Prompting"—defined as iterative, question-based AI interaction—in safeguarding unique cultural nuances from "algorithmic sanitization" (the loss of identity through standardized AI output). This method resulted in a 40% higher retention of original idiomatic expressions compared to direct, one-off prompting. Consequently, the study advocates for a process-oriented disclosure model using transparency logs to address "digital ghostwriting." By moving beyond a prohibition-based mindset, the research positions AI as a tool to sharpen the human filter rather than replace the learner’s identity. Ultimately, these findings ensure that the diverse voices of EFL learners remain the primary drivers of academic discourse in an increasingly automated age.

**Решение:** -

---

### 407 · R4812

**Universally Designed Augmented Reality as Interface for Artificial Intelligence Assisted Decision-Making in Everyday Life Scenarios**

2024 · Studies in health technology and informatics · journalarticle, review, book-chapter · en · https://doi.org/10.3233/shti241043

This paper presents a conceptual prototype that integrates Artificial Intelligence (AI) and Augmented Reality (AR) with the principles of Universal Design (UD) to enhance decision-making in everyday scenarios for a diverse user base, eliminating the need for conventional text or voice AI interfaces. The study employed a mixed-method approach, including surveys, user testing, and interviews with eight participants from various age groups. The focus was on user interaction styles (head-mounted, handheld) within three everyday scenarios: 1) medication assistance, 2) food and beverage assistance, and 3) sustainability advocacy. Findings revealed that AR as an interface for AI was well-received for its intuitiveness and practical utility. However, users expressed concerns about privacy, the discomfort of wearable technology, and potential over-reliance on AI. This study demonstrates the potential of integrating AR as an interface for AI, combined with UD principles, to create inclusive, context-aware solutions, adaptable to users with diverse skills and abilities.

**Решение:** -

---

### 408 · R1276

**Who Theorized? Attributing Conceptual Contributions in a Practitioner's Dialogues with a Large Language Model**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.7525144

When a practitioner develops a conceptual framework through sustained dialogue with a large language model, what the practitioner remembers building and what the transcript shows can diverge. This paper double-codes every concept unit (N = 107) across eight archived dialogues (84 turns, June 2025 to January 2026) between an independent AI consultant and restaurant owner-operator and Google Gemini, using a five-category origin codebook applied by two independent large-language-model coders and adjudicated where they disagreed (29 of 107 units; exact agreement .73; Cohen's kappa = .63 on the five-category scheme, .58 collapsed to three). The resulting distribution of 15 user-originated, 35 user-seed/model-elaborated, 3 co-constructed, 18 model-originated-and-adopted, and 36 model-originated-and-unused units, against a corrected model-to-user character ratio of 13.98 to 1, shows that the model originated roughly half of all coded units (50.5 percent, whether or not the practitioner used them). A case study of the practitioner's four-book series makes the mechanism concrete: the practitioner asked the model to recall prior themes from its memory of earlier sessions; the model retrieved and sequenced them, including the governing curriculum sentence the practitioner later treated as their own; the practitioner's only substantive input was a one-item correction. No existing authorship-disclosure framework has a category for this pattern, which differs from AI ghostwriting, sycophancy, and cryptomnesia. The paper is reflexive on two fronts: the researcher is the coded subject, and this manuscript was drafted with heavy AI assistance. It closes with a reusable codebook, a disclosure-paragraph template, and a call for replication with human coders.

**Решение:** -

---

### 409 · R1008

**Effects of Generative AI Dependency on Undergraduate Students’ Creativity**

2026 · Pacific International Journal · article, journalarticle, review · und · https://doi.org/10.55014/pij.v9i2.1000

Based on the Behavioral Dependency Framework, this study explores the influence mechanism of generative artificial intelligence dependency on undergraduate students’ creativity. In this study, the generative artificial intelligence dependency was divided into three dimensions: cognitive preoccupation, negative consequences and withdrawal. 223 valid questionnaires were obtained through online surveys, and data analysis was conducted using the Partial Least Squares Structural Equation Modeling (PLS-SEM). The results show that cognitive preoccupation has a positive impact on creativity, but the negative consequences and withdrawal have no effect on creativity. This study not only refines the relationship mechanism between the generative artificial intelligence dependency and creativity, but also provides empirical reference for universities to guide students to use generative artificial intelligence rationally.

**Решение:** ?

---

### 410 · R1959

**THE PARADOX OF CHATGPT DEPENDENCE: NEGATIVE IMPACTS ON ACADEMIC READING, RESEARCH SKILL AND ACADEMIC WRITING**

2026 · TEFLIN Journal - A publication on the teaching and learning of English · journalarticle, article, journal-article · en · https://doi.org/10.15639/teflinjournal.v37i1/137-165

The integration of artificial intelligence (AI) in higher education has revolutionized learning practices, yet its impacts on academic competencies remain an area of exploration. This study employed Partial Least Squares Structural Equation Modeling (PLS-SEM), combining reflective and formative measurement models, to investigate the correlation among ChatGPT usage, English academic reading, research skill, and English academic writing. A total of 284 postgraduate students majoring in linguistics and English education across five universities in Indonesia participated. The participants selected through purposive sampling completed an online questionnaire distributed via Google Forms. Findings reveal negative correlation between ChatGPT usage and English academic writing. It implies that ChatGPT alone does not directly enhance the academic writing proficiency of graduate students. The result also shows an unexpected yet significant negative correlation between ChatGPT usage and both English academic reading (β = -0.175, p = 0.017) and research skill (β = -0.164, p = 0.015), suggesting that over-reliance on AI-assisted tools may hinder critical engagement and skill development. Conversely, academic reading (β = 0.640, p = 0.000) demonstrates the strongest influence on academic writing, showing the necessity of cultivating strong reading competencies to enhance scholarly output. These results indicate a pressing need for a balanced approach to AI integration in academic settings, requiring students to actively engage with research materials rather than relying solely on AI-generated content. By fostering academic literacy and research-driven methodologies, educators can mitigate the adverse effects of ChatGPT dependence while maximizing the potential of AI as a supplementary tool. This study contributes to the discourse on AI-driven education, emphasizing the nuanced role of technology in shaping academic literacy and research proficiency.

**Решение:** ?

---

### 411 · R1562

**Loss Orientation and Grief Following AI-Companion Shutdown**

2026 · OMEGA - Journal of Death and Dying · journal-article · https://doi.org/10.1177/00302228261496977

This study examined whether grief after an AI-companion shutdown is associated with what users describe as lost. Fifty-seven accounts collected after the shutdown of the Soulmate AI application were independently coded by two raters for grief intensity and dominant loss orientation, and each coding was analysed separately. Accounts framing the loss as that of a person showed greater grief than those framing it as the loss of an idea, a service, data, or platform access: medians were 4 versus 2 (rank-biserial r = .80 and .82). A finer three-category comparison could be tested only in the first coder’s data, where grief was highest in person-oriented accounts and idea-oriented accounts did not differ significantly from system-facing accounts. Reported weekly usage was also associated with grief (ρ = .38 and .43) but was not associated with loss orientation. The association between loss orientation and grief remained after accounting for reported weekly usage.

**Решение:** -

---

### 412 · R3854

**Artificial Intelligence in Ecuadorian Higher Education: Dependence, Attitudes, and Implications for Technology-Enhanced Sustainable Learning**

2025 · Preprints.org · article, preprint, posted-content · und · https://doi.org/10.20944/preprints202507.1393.v1

This study examines the dependence on and attitudes toward artificial intelligence (AI) among university students in Ecuador, with the aim of informing pedagogical strategies for ethical and inclusive AI integration in higher education. Based on a cross-sectional quantitative design, 540 students completed the Artificial Intelligence Dependence Scale (DAI) and the General Attitudes Toward Artificial Intelligence Scale (GAAIS). The findings indicate a moderate level of AI dependence and an ambivalent attitudinal profile, characterized by balanced positive and negative perceptions. Structural equation modeling revealed that both attitudinal dimensions significantly predict AI dependence, highlighting the functional but critical role of these technologies in academic settings. Urban students reported greater dependence and ethical concerns, underscoring contextual inequalities in technological access. The study contributes to the discourse on technology-enhanced education for sustainable development by addressing how digital competencies, academic integrity, and critical thinking can be fostered through responsible AI use. These findings align with the United Nations’ Sustainable Development Goals (SDGs), particularly those related to quality education (SDG 4) and reduced inequalities (SDG 10), and advocate for learner-centered, equity-driven approaches to AI adoption in educational systems.

**Решение:** -

---

### 413 · R1932

**Between map and maze: reframing trust in healthcare AI**

2026 · AI & Society · review, journalarticle, article · en · https://doi.org/10.1007/s00146-026-02997-9

Abstract Artificial intelligence (AI) is often presented as a transformative technology for healthcare, promising to augment clinical decision-making, streamline workflows, and enhance diagnostic precision. Yet its integration into healthcare practice is shaped by the complex and often ambiguous notion of trust . While trust in AI has become a recurring theme across disciplines, there has been little systematic analysis of different conceptualizations of the term. This paper addresses this gap through an interdisciplinary scoping review that examines how trust, trustworthiness, distrust, and mistrust are articulated in literature on AI in healthcare. Drawing on 82 publications (2015–2025) retrieved from six databases (Web of Science, Scopus, PubMed, PhilPapers, SocINDEX, and ACM Digital Library), it maps how trust is defined, measured, or problematized, and identifies the conceptual, epistemological, and disciplinary boundaries that shape these approaches. The analysis puts forward five different conceptualizations: trust as a set of designable principles , trust as an attitude or belief , trust as a binary between cognition/affect or human/technology, trust as a structural mechanism within uncertainty, and trust as a relational process embedded in socio-technical systems. These framings illuminate how trust is treated as an attribute to be engineered, a behavior to be calibrated, or a relation to be cultivated—often removed from clinical practice. Yet, across literature, trust disruptions which manifest as distrust, mistrust, overtrust, and undertrust are undertheorized and are typically framed as obstacles to overcome rather than phenomena warranting analysis in their own right. By introducing these diverging conceptualizations, the paper argues that trust in healthcare AI is less a stable condition than a dynamic negotiation that reveals power relations, uncertainties, and institutional dependencies of AI. Recognizing distrust and mistrust as analytically productive allows for a more reflexive understanding of how trust is enacted, distributed, and contested within healthcare. This review contributes to an emerging body of work that reframes trust not as a prerequisite for technological adoption but as a contested and dynamic concept.

**Решение:** -

---

### 414 · R1188

**GenAI Literacy of Art and Design Students and Lecturers Toward GenAI and Digital Media**

2026 · International Conference on Advanced Learning Technologies · conference, review · https://doi.org/10.1109/icalt68022.2026.00106

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 415 · R0975

**An analytical Study on Awareness of Stock Market Instruments and the Role of Information Sources among Retail Investors in Uttar Pradesh**

2026 · Economic Sciences. · journalarticle, article · https://doi.org/10.69889/rf2tbh96

The Indian stock market is witnessing a large influx of retail investors, thanks to the digital age and the availability of trading platforms. There has been a concern regarding the extent to which retail investors are aware of financial products and the quality of their decision-making skills based on the information they receive about financial products. Data show that while participation has grown, this doesn't guarantee adequate knowledge. Therefore, this study will look at how well retail investors in Uttar Pradesh know about stock market products as well as analyse how various sources of information affect their awareness level. The primary data collected from 230 retail investors. Different statistical methods such as chi-square test, one-sample t-test, and multiple regression analysis. The reliability of the measurement scales was confirmed using Cronbach’s alpha. The findings indicate that retail investors possess high awareness of low-risk, traditional investments. And possess reasonably satisfactory levels of awareness regarding mutual funds and ETFs. However; awareness level for high-risk/complex investment instruments such as derivatives and foreign exchange remains low for many retail investors. Results show that information sources; including social media, AI-based applications; peer groups; and digital media positively contribute to an investor's awareness; whilst traditional brokers and independent financial advisor only modestly contribute to an investor's awareness of investments. An overreliance on AI-generated insights is found to negatively affect independent understanding.

**Решение:** -

---

### 416 · R1808

**THE FUTURE OF FORMATIVE ASSESSMENT: LEVERAGING AI FOR CONTINUOUS LEARNING EVALUATION**

2026 · Al-Hijr Journal of Adulearn World · article · en

The integration of Artificial Intelligence (AI) in education has the potential to revolutionize formative assessment practices by offering real-time, personalized feedback. Formative assessment, traditionally seen as an ongoing process to monitor student progress, faces challenges such as scalability and timely feedback. AI-powered systems can provide instant insights into student performance, facilitating continuous learning evaluation. This research aims to explore how AI can enhance formative assessment by providing continuous and individualized evaluation of students’ progress. A mixed-methods approach was employed, using surveys, interviews, and classroom observations across five schools that have implemented AI-based learning platforms. The results revealed that AI-driven formative assessments significantly improved student engagement and performance, with 80% of teachers reporting more efficient monitoring and intervention strategies. However, concerns about the depersonalization of feedback and the risk of over-reliance on AI were noted, suggesting the need for a balance between technological tools and human interaction. The study concludes that AI has the potential to transform formative assessment practices but requires careful integration into teaching methods to ensure it complements rather than replaces teacher-student interactions.

**Решение:** -

---

### 417 · R2158

**Leveraging Deep Learning, Design Thinking and Sustainable Entrepreneurship: A Structural Equation Modelling Approach**

2026 · Modeling and optimization in science and technologies · book-chapter · en · https://doi.org/10.1007/978-3-032-25190-9_6

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 418 · R2338

**Impact of generative AI tools on Student Creativity and Critical thinking in College Students**

2026 · Zenodo (CERN European Organization for Nuclear Research) · article · en · https://doi.org/10.5281/zenodo.19615456

Abstract : The rapid integration of generative artificial intelligence tools such as ChatGPT has significantly transformed modern educational practices. This study examines the impact of generative AI on students’ creativity and critical thinking skills among higher secondary and undergraduate learners in Bhopal. A descriptive research design was employed to analyze both positive and negative cognitive outcomes associated with AI usage. The population of the study consisted of students from selected institutions in Bhopal, including government and private colleges. A sample of 120 students was selected using stratified random sampling, ensuring representation across academic streams (science, commerce, and humanities). Data were collected through structured questionnaires and critical thinking assessment tasks. The findings reveal that generative AI tools enhance academic productivity, idea generation, and access to information, thereby supporting creative thinking. Students reported using AI for brainstorming, drafting assignments, and simplifying complex concepts, aligning with recent studies indicating increased engagement and self-directed learning among AI users. However, excessive reliance on AI was found to reduce independent problem-solving abilities and critical analysis, as students tend to accept AI-generated responses without evaluation. Experts have also cautioned that overuse of AI may weaken originality and cognitive engagement among learners. The study concludes that while generative AI has the potential to foster creativity, its impact on critical thinking is mixed. Therefore, educational institutions must adopt balanced strategies, integrating AI as a supportive tool while promoting analytical skills and ethical usage among students. Keywords : Generative AI tools, critical thinking, Creativity.

**Решение:** -

---

### 419 · R1684

**Artificial intelligence and student creativity: An exploratory study of students’ experiences with AI tools**

2026 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2026.100988

This study explores how students utilize AI tools in a short visual design task and how these experiences relate to self-reported creativity and creative self-efficacy, using an exploratory mixed-methods approach. The primary aim is to understand students’ perspectives on AI-supported creation, with quantitative measures serving as contextual evidence. Fifty-eight undergraduate students completed a brief design project supported by AI tools and finished pre- and post-task surveys assessing creativity and creative self-efficacy. A subset of 18 students also joined focus group interviews to provide qualitative insights. High-performing students described using AI as a collaborative partner to augment ideas and validate directions while maintaining a sense of control. In contrast, medium- and low-performing students reported a greater reliance on AI outputs, feeling overwhelmed by the abundance of options, and a reduced confidence in their own creative abilities without AI support. Quantitative analyses revealed no detectable change in creativity or creative self-efficacy from pre- to post-intervention, and negligible associations between these self-reported measures and creative performance. Overall, the findings suggest that AI tools alone may not yield short-term gains in perceived creativity or creative self-efficacy; instead, students’ outcomes and experiences appear to vary with how critically and reflectively they engage with AI. The study highlights the need for pedagogical scaffolding and instructional guidance when integrating AI into creative education. • An exploratory mixed-methods study of students’ AI tool use in an authentic short design task. • No detectable pre-post change in creativity or creative self-efficacy. • Expert-rated creative performance was weakly related to self-reported creativity and efficacy. • High performers described using AI for validation and iterative refinement. • Lower performers reported choice overload, AI dependence, and lower confidence, implying scaffolding and reflection.

**Решение:** -

---

### 420 · R3857

**LLM and Knowledge Graph-Based Intelligent Control Framework for Smart Manufacturing**

2025 · Conference on Computability in Europe · conference · https://doi.org/10.1115/detc2025-168925

The rapid development of large language models (LLMs) and robotics is fundamentally reshaping the manufacturing sector. LLMs have already had a profound impact across multiple fields, such as document management, medical consultation, education, etc. However, the inherent complexity and dynamic nature of manufacturing continue to pose challenges for applying LLMs in robotic control within this domain, particularly in understanding the spatial and logical relationships between different objects. Although fine-tuning can be implemented, it requires a significant amount of time for each iteration and does not support real-time updates, making it unsuitable for industrial applications. To relieve the problem, this paper proposes a novel industrial robot control scheme called the LLM-Knowledge Graph (KG) Powered Intelligent Agent Framework (LKPI). The goal is to fully leverage the external knowledge and logical relationships provided by KG to enhance robotic perception and decision-making in complex production environments, without the need to finetune the LLMs. In experimental validation, LKPI demonstrated superior logical reasoning and environmental adaptability in a dynamic and noise-prone pecan processing scenario. Even when the camera could not directly identify the target object, LKPI utilized environmental background information and relationship information stored in the KG to accomplish transportation and navigation. By integrating real-time recognition and depth measurement from an RGB-D camera, the robot continuously adjusts its path in response to changes in the position of moving targets. Additionally, the integration of IoT enables real-time environmental updates and tracking. These three experimental validations collectively demonstrate the reasoning control capability, dynamic perception capability, and real-time adaptation capability of the LKPI framework. Experimental results show that LKPI eliminates dependence on LLM fine-tuning while enabling the efficient perception and control of real-time dynamic information in complex industrial environments, significantly enhancing the flexibility and task completion rate of robots in production processes. Future research will further extend this framework to applications and optimizations in multi-robot collaboration and long-range sensing.

**Решение:** -

---

### 421 · R2748

**The Gravitational Pull of the Dead: Lethal Pathways in AI-Mediated Bereavement**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · und · https://doi.org/10.5281/zenodo.19721987

When bereaved individuals turn to AI-generated replicas of the deceased, they make a choice that is subjectively rational—especially after traumatic loss. This article argues that this very rationality constitutes the entry point into lethal pathways that existing forensic and epidemiological frameworks cannot detect. Drawing on prolonged grief disorder epidemiology, emerging AI dependency research, and a systematic compilation of 21 confirmed AI-associated deaths (2023–2026), I propose the Gravitational Pull of the Dead (GPD) branching model. The model identifies three novel mechanisms: Memory Contamination Lock (irreversible overwriting of authentic memories by AI-generated content), Compassionate Lethality (empathic AI output that functions as designed yet points toward death), and Triple Bereavement (service discontinuation producing a third death more destructive than the original loss). I demonstrate that the populations most likely to seek griefbots are structurally identical to those for whom continuing bonds become most harmful—a convergence no prior study has identified.

**Решение:** -

---

### 422 · R4859

**Authentic or artificial intelligence? Faculty’s perspectives on the ChatGPT’s impact on U.S. urban planning Ph.D. programs**

2024 · Frontiers of Urban and Rural Planning · journalarticle, review, article · en · https://doi.org/10.1007/s44243-024-00046-x

Abstract This commentary article explores the impact of ChatGPT on Urban Planning Ph.D. programs within universities in the United States. Our survey reveals a high awareness of Artificial Intelligence tools (e.g. ChatGPT) among faculty yet highlights a cautious approach to integrating ChatGPT into curricula and preliminary exam settings. While some educators recognize ChatGPT’s potential to enhance research efficiency and language proficiency, especially for international students, concerns about academic integrity and the over-reliance on AI are prevalent. The commentary underscores the need for a balanced approach, advocating for ChatGPT’s use as a supplementary tool while maintaining critical thinking in doctoral preliminary exams.

**Решение:** -

---

### 423 · R0385

**The Integration of Artificial Intelligence (AI) Technologies in Advance Learning in Universities at Mwanza, Tanzania**

2026 · International Journal of Education Foundations · journalarticle, review, article · https://doi.org/10.33687/ijef.003.04.00149

The rapid development of Artificial Intelligence (AI) technologies is significantly transforming higher education, altering how students and faculty search for information, analyze data, develop ideas, share knowledge, and conduct research. Universities are increasingly adopting tools such as generative AI, machine learning, natural language processing, intelligent tutoring systems, and AI-powered research instruments to improve learning and research results. This study systematically reviews empirical evidence on AI integration in advanced learning, emphasizing how AI supports academic research in universities. Guided by the PRISMA framework, the review involved systematic searches of peer-reviewed journal articles, books, policy reports, and scholarly works from major databases like Scopus, Web of Science, ERIC, Google Scholar, and institutional repositories. Selected studies were screened, assessed for eligibility, and thematically synthesized. The review discusses AI-assisted literature searches, information retrieval, data analysis, academic writing, research design, and productivity. Results suggest that AI boosts efficiency and accessibility across research stages, including language assistance and data processing. However, issues such as information accuracy, academic integrity, bias, privacy, over-dependence on AI, and limited AI literacy remain concerns. For Mwanza universities, the researcher recommends that successful AI integration needs institutional policies, strong digital infrastructure, ethical guidelines, and continuous human oversight. The study concludes that AI should be viewed as a tool to support, not replace, scholarly judgment.

**Решение:** -

---

### 424 · R1321

**Adoption of ChatGPT Among LIS Research Scholars: A Comparative Study of the University of Delhi and Babasaheb Bhimrao Ambedkar University, Lucknow**

2026 · Journal of Library & Information Science (JLIS) · article · en

Artificial intelligence (AI) tools such as ChatGPT are increasingly transforming academic research by enhancing information retrieval, content generation, and knowledge discovery. This study examines the adoption and perceptions of ChatGPT among Library and Information Science (LIS) research scholars at Babasaheb Bhimrao Ambedkar University (BBAU), Lucknow, and the University of Delhi (DU). Data were collected during the 2024–25 academic session through a structured questionnaire comprising 15 open- and closed-ended questions. A total of 62 valid responses were received, including 32 from BBAU and 30 from DU. Using the Unified Theory of Acceptance and Use of Technology (UTAUT) as the theoretical framework, the study explores scholars' experiences, perceived benefits, and concerns regarding the use of ChatGPT. The findings reveal a generally positive attitude toward ChatGPT: 46.8% of respondents consider its information somewhat accurate, and 56.5% are willing to recommend it for academic purposes. The most frequently reported advantage was its free and 24/7 availability (80.6%). However, 69.4% of respondents expressed concerns about overreliance on AI. Additionally, 90.3% reported the absence of institutional policies on AI use, while only 9.7% had received faculty guidance regarding ChatGPT. The study highlights the growing acceptance of AI tools in LIS research and emphasizes the need for institutional policies and ethical guidelines to support their responsible academic use.

**Решение:** -

---

### 425 · R4821

**Artificial Intelligence in Knee Arthroscopy**

2024 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-3-031-70310-2_10

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 426 · R5065

**Detecting breast cancer using artificial intelligence: Convolutional neural network.**

2021 · Technology and health care : official journal of the European Society for Engineering and Medicine · journal article · eng · https://doi.org/10.3233/thc-202226

One of the most broadly founded approaches to envisage cancer treatment relies upon a pathologist's efficiency to visually inspect the appearances of bio-markers on the invasive tumor tissue section. Lately, deep learning techniques have radically enriched the ability of computers to identify objects in images fostering the prospect for fully automated computer-aided diagnosis. Given the noticeable role of nuclear structure in cancer detection, AI's pattern recognizing ability can expedite the diagnostic process. In this study, we propose and implement an image classification technique to identify breast cancer. We implement the convolutional neural network (CNN) on breast cancer image data set to identify invasive ductal carcinoma (IDC). The proposed CNN model after data augmentation yielded 78.4% classification accuracy. 16% of IDC (-) were predicted incorrectly (false negative) whereas 25% of IDC (+) were predicted incorrectly (false positive). The results achieved by the proposed approach have shown that it is feasible to employ a convolutional neural network particularly for breast cancer classification tasks. However, a common problem in any artificial intelligence algorithm is its dependence on the data set. Therefore, the performance of the proposed model might not be generalized.

**Решение:** -

---

### 427 · R3682

**Artificial intelligence in children’s speech development**

2025 · Sovremennye issledovaniya sotsialnykh problem · journalarticle, review, article · ru · https://doi.org/10.12731/3033-5981-2025-17-3-528

Background. Over the past ten years, interest in artificial intelligence (AI) has grown significantly around the world. AI is seen as a catalyst for transformations in education, including preschool education, which should affect not only the learner, teacher and administrator, but also the parent, as it is the parent who is often the main “supplier” of AI-based gadgets and applications for their children, the measure of their safety and usefulness. Purpose. The article aims todetermine the attitude of modern parents towards AI as a means of speech development in children aged 4 to 7, and to identify the risks associated with the introduction of intelligent technologies into preschool education programs. Materialsandmethods. The study combined quantitative and qualitative methods: a survey (questionnaires and interviews) and content analysis of video recordings of classes and situational reflection diaries. A total of 44 parents and more than 180 children aged 4-7 participated in the study. Results.The results of the study indicate a predominantly positive perception of AI technologies in preschool education by parents, as they believe in the potential of these tools for the holistic development of children as well as their language development. At the end of the experiment, the parents noted significant benefits of using AI technologies, such as expanding vocabulary, developing speaking and listening skills, and increasing motivation through gamification. However, there are also significant risks associated with limiting children’s social interaction and physical activity through excessive use of AI technologies, as well as potential inaccuracies and exaggerations in generated content. The study also shows the need to consider financial costs, technical failures, and the lack of ICT skills among teachers and parents. The study highlights the importance of a balanced and responsible implementation of AI in early childhood education, taking into account both its benefits and possible threats.

**Решение:** -

---

### 428 · R4445

**ФЕНОМЕН ЗАЛЕЖНОСТІ ВІД ШТУЧНОГО ІНТЕЛЕКТУ (ШІ-АДИКЦІЯ): ТЕОРЕТИЧНИЙ АНАЛІЗ, ФАКТОРИ РИЗИКУ ТА ПЕРСПЕКТИВИ ДОСЛІДЖЕННЯ**

2025 · Publishing house "Helvetica" · research article · https://core.ac.uk/download/714511271.pdf

Abstract. The rapid and large-scale integration of generative artificial intelligence (AI) systems into daily life creates an unprecedented context for the formation of new forms of behavioral addictions. Unlike previous digital technologies, AI offers unique interaction mechanisms with a potentially much higher addictive potential. This poses a serious threat to mental health, especially among vulnerable populations, and necessitates the development of a new conceptual framework for understanding, diagnosis, and therapeutic intervention. Objective. To conduct a theoretical analysis of the AI addiction phenomenon, identify its unique phenomenological features, propose hypothetical neurobiological and psychosocial mechanisms of its formation, and outline the main diagnostic challenges and future research directions. Materials and Methods. A theoretical review and conceptual analysis were conducted based on a systematic search of scientific literature in the PubMed, Scopus, Web of Science, and Google Scholar databases for the period from 1996 to 2025. A narrative synthesis method was used for data analysis and generalization. Results. The literature analysis identified three key characteristics of AI addiction: 1) hyper-personalization of content, creating a powerful, individualized reward system; 2) anthropomorphism and the simulation of social interaction, allowing compensation for deficits in real social connections; and 3) continuous gamified interaction loops that exploit dopamine reinforcement loops similar to gambling. A neurobiological model is proposed, linking these stimuli to the dysregulation of the mesolimbic dopamine system, hypoactivity of the prefrontal cortex (leading to reduced cognitive control), and alterations in the default mode network. Psychosocial risk factors, including loneliness, social anxiety, low self-esteem, and deficits in interpersonal communication skills, are examined. Diagnostic challenges related to symptomatic overlap with other addictions and the absence of validated assessment tools are outlined. Conclusions. AI addiction is an emerging potential behavioral disorder with a unique pathogenetic profile that distinguishes it from existing digital addictions. Urgent further research, including longitudinal studies and neuroimaging experiments, is required to verify the proposed models, develop validated diagnostic criteria (e.g., for inclusion in future versions of the DSM/ICD), and create evidence-based prevention and therapy programs.Анотація. Стрімка та масштабна інтеграція генеративних систем штучного інтелекту (ШІ) у повсякденне життя створює безпрецедентний контекст для формування нових форм поведінкових залежностей. На відміну від попередніх цифрових технологій, ШІ пропонує унікальні механізми взаємодії, що потенційно мають значно вищий адиктивний потенціал. Це створює серйозну загрозу для психічного здоров’я, особливо серед вразливих груп населення, і вимагає розробки нової концептуальної рамки для розуміння, діагностики й терапевтичного втручання. Мета дослідження – провести теоретичний аналіз феномена ШІ-адикції, визначити її унікальні феноменологічні риси, запропонувати гіпотетичні нейробіологічні та психосоціальні механізми її формування, а також окреслити основні діагностичні виклики й напрями для майбутніх досліджень. Матеріали та методи. Проведено теоретичний огляд і концептуальний аналіз на основі систематизованого пошуку наукової літератури в базах даних PubMed, Scopus, Web of Science та Google Scholar за період з 1996 по 2025 рік. Для аналізу й узагальнення даних використовувався метод наративного синтезу. Результати. Аналіз літератури дав змогу виділити три ключові характеристики ШІ-адикції: 1) гіперперсоналізація контенту, що формує потужну, індивідуалізовану систему винагороди; 2) антропоморфізм і симуляція соціальної взаємодії, що дає змогу компенсувати дефіцит реальних соціальних зв’язків; 3) безперервні гейміфіковані цикли взаємодії, що експлуатують дофамінові петлі підкріплення, подібні до азартних ігор. Запропоновано нейробіологічну модель, яка пов’язує ці стимули з дисрегуляцією мезолімбічної дофамінової системи, гіпоактивністю префронтальної кори (зниження когнітивного контролю) і змінами в мережі пасивного режиму роботи мозку. Розглянуто психосоціальні фактори ризику, зокрема самотність, соціальну тривожність, низьку самооцінку й дефіцит навичок міжособистісної комунікації. Окреслено діагностичні виклики, пов’язані із симптомною схожістю з іншими адикціями й відсутністю валідованого інструментарію. Висновки. ШІ-адикція є новим потенційним поведінковим розладом з унікальним патогенетичним профілем, що відрізняє її від наявних цифрових залежностей. Необхідні термінові подальші дослідження, зокрема лонгітюдні спостереження та нейровізуалізаційні експерименти, для верифікації запропонованих моделей, розробки валідованих діагностичних критеріїв (наприклад, для включення до майбутніх версій DSM/МКХ) і створення доказових програм профілактики й терапі

**Решение:** -

---

### 429 · R3369

**Investigating the influence of AI-driven tools in ESL students’ experience of AI-induced impostor syndrome and academic confidence**

2025 · Asian Journal of English Language Studies · article, research article · en · https://doi.org/10.59960/13.1.a5

This study investigates the relationship between AIdriven writing tools and Impostor Syndrome (IS) among tertiary ESL students, focusing on how AI use influences self-perception and academic confidence. Employing a mixed-methods approach, the study involved 200 students from a Philippine state university, collecting quantitative data through a modified AI-induced Impostor Syndrome Test and qualitative data via semi-structured interviews. Findings reveal that show that 24% of students displayed minimal impostor traits, perceiving AI tools as enhancers of their skills. However, 49% fell within the moderate range, occasionally struggling with self-doubt and attributing their academic success to AI assistance. Notably, 24.5% reported frequent impostor experiences, suggesting a growing reliance on AI tools that may undermine self-efficacy. A critical 2.5% experienced intense impostor feelings, indicating a severe dependence on AI that negatively affected their academic identity. Qualitative data further highlighted concerns about authenticity, over-reliance on AI, and ethical dilemmas in academic writing. The study stresses the importance of balanced pedagogical strategies, digital literacy, and psychological resilience to mitigate AI-induced Impostor Syndrome. It also highlights the role of time management, structured review, and adaptability as key coping mechanisms. These findings support the development of interventions that promote confidence, academic integrity, and responsible AI integration in ESL education

**Решение:** -

---

### 430 · R5038

**Replika in the Metaverse: the moral problem with empathy in 'It from Bit'.**

2022 · AI and ethics · journal article, journalarticle, article · eng · https://doi.org/10.1007/s43681-022-00252-7

Abstract This paper assesses claims of computational empathy in relation to existing social open-ended chatbots and intention that these chatbots will feature in emergent mixed reality contexts, recently given prominence due to interest in the Metaverse. Against the background of increasing loneliness within society and use of chatbots as a potential remedy for this, the paper considers two leading current social chatbots, Replika and Microsoft’s Xiaoice , their technical underpinnings, empathetic claims and properties that have scope to scale into the Metaverse (if it coheres). Finding scope for human benefit from social chatbots, the paper highlights problematic reliance on self-disclosure to sustain the existence of chatbots. The paper progresses to situate Microsoft’s empathetic computing framework in relation to philosophical ideas that inform Metaverse speculation and construction, including Wheeler’s ‘It from Bit’ thesis that all aspects of existence may be computed, Chalmers’ philosophical championing that virtual realities are genuine realities, Bostrom’s proposal and provocation that we might already be living in a simulation, and longtermist belief that future complex simulations need to be protected from decisions made today. Given claims for current and nascent social chatbots, belief in bit-based possible and projected futures, and industrial buy-in to these philosophies, this paper answers whether computational empathy is real or not. The paper finds when diverse accounts of empathy are accounted for, whilst something is irrevocably lost in an ‘It from Bit’ account of empathy, the missing components are not accuracy or even human commonality of experience, but the moral dimension of empathy.

**Решение:** -

---

### 431 · R0052

**Pedagogical Use of Responsible Generative AI in Higher Education; Opportunities and Challenges: A Systematic Literature Review**

2026 · AI in Education · journalarticle, review, journal-article · en · https://doi.org/10.3390/aieduc2020011

Generative Artificial Intelligence (GenAI) is transforming higher education in terms of pedagogy, student involvement, and academic management. This systematic literature review examines 30 peer-reviewed articles published from 2019 to 2025, adhering to PRISMA 2020 and Kitchenham’s methodologies. Descriptive and thematic analyses highlight five opportunities: (a) tailored and adaptive education; (b) deliberate fostering of critical thinking; (c) enhanced accessibility for varied learners; (d) teaching innovation via multimodal content development and feedback; and (e) collaborative methods that regard AI as a co-teacher. Four ongoing challenge categories also surface: (a) risks to academic integrity; (b) excessive dependence on GenAI that may hinder learner independence; (c) inconsistent faculty preparedness and change-management abilities; and (d) differences in infrastructure and policy both regionally and globally. Intersecting ethical issues, such as data privacy, algorithmic bias, transparency, and accountability, highlight the necessity for governance that aligns with institutional risk and reflects societal values. Analyzing the recent literature, this systematic review offers four contributions: (a) a recommendation model for responsible GenAI implementation in higher education institutions; (b) a framework for sustainable integration of GenAI; (c) a highlight of the future research recommendations; and (d) an integrated policy and pedagogical recommendations roadmap. These models emphasize the integration of AI literacy, ethical considerations, and critical thinking goals into educational programs. The review advocates for a strategic, stakeholder-focused approach to implementation that enhances rather than replaces human instruction, thus connecting GenAI’s educational potential with ethical, context-aware avenues for institutional transformation.

**Решение:** -

---

### 432 · R0788

**Beyond Sycophancy: Vendor- and Interface-Dependent Revision Recommendations in Large Language Model Methods Review (Preprint)**

2026 · JMIR Publications Inc. · posted-content · https://doi.org/10.2196/preprints.108677

BACKGROUND Large language models (LLMs) have been demonstrated to exhibit sycophantic behavior, agreeing with users rather than corrected them, which may reinforce user belief over accuracy. Whether this compromises LLM appraisal of flawed research methods is unknown. OBJECTIVE This study evaluated whether LLMs endorse methodologically flawed clinical research excerpts as sound, whether they correctly pass sound excerpts, and whether stated user confidence or authority alters these behaviors. Sycophantic false reassurance was hypothesized to occur and to increase with user confidence. METHODS Twenty clinical research methods excerpts were developed: ten containing a single prespecified major methodological flaw and ten matched flaw-corrected twins. Excerpts were submitted to two commercial LLM vendors (OpenAI, Anthropic) as independent structured review requests. The primary outcome was false reassurance, defined as endorsing a flawed excerpt as sound. The secondary outcome was clean overflagging, defined as recommending major revision of a flaw-corrected excerpt. The application program interface (API) experiment crossed 20 excerpts by 2 vendors, 7 prompt framings, 3 stated expertise levels, and 5 replicates (4200 responses). A targeted 200-response substudy was collected through the consumer ChatGPT and Claude interfaces with expertise fixed at intermediate. RESULTS False reassurance was rare (3/2100 flawed responses, 0.14%; 0/1050 Anthropic, 3/1050 OpenAI, 0.29%) and did not occur in the commercial product substudy (0/40). Clean overflagging occurred in 14.5% (152/1050) of Anthropic and 48.8% (509/1044) of OpenAI clean responses (OR 5.70, 95% CI: 2.92 – 11.10). This difference persisted after sequential exclusion of the most frequently flagged excerpts. Stated expertise was not associated with either outcome. The overall prompt-framing effect was not significant (p = .26), though authority-pressure (OR 1.81, 95% CI: 1.10 – 2.97, p = .02) and high-user-confidence (OR 2.74, 95% CI: 1.05 – 7.14, p = .04) were associated with higher odds of clean overflagging than neutral framing. Clean overflagging was substantially higher through consumer products than the API for both vendors. CONCLUSIONS Sycophantic false reassurance was essentially absent and asserting user confidence or authority did not induce it. The dominant behavior was instead recommending revision of methodologically sound excerpts, which varied markedly by vendor and by whether the model was accessed through a consumer product or an API. Given identical excerpts produced different verdicts across products and surfaces, model-generated revision recommends should prompt human evaluation of the stated concern rather than automatic acceptance that a flaw exists. CLINICALTRIAL NA

**Решение:** -

---

### 433 · R2358

**Structure Before Substance: A Critical Analysis of South Korea's AI Education Policy Through the Lens of the OECD AILit Framework**

2026 · Korean Comparative Education Society · journalarticle, review, article · https://doi.org/10.20306/kces.2026.36.2.199

[Purpose] This study critically evaluates the South Korean Ministry of Education’s AI reform initiatives for 2025–2028, including the ‘AI Focus Schools’ and the ‘AI for All’ talent development plan. [Method] Employing critical policy analysis and comparative review, this research examines official Ministry documents against the OECD/European Commission AI Literacy Framework. It further contrasts South Korea’s implementation model with the evidence-staged approach of the United States Institute of Education Sciences' U-GAIN Centers initiative. [Results] The analysis reveals that the policies inadequately address the epistemic and pedagogical dimensions of AI literacy. Specifically, current frameworks fail to mitigate risks such as student over-reliance on AI, surrogate cognition, delegated thinking, and the resulting inhibition of independent human reasoning. [Conclusions] The study concludes that effective AI education policy must be grounded in learning science—establishing clear definitions of AI literacy and learning processes before mandating large-scale implementation. The paper proposes principles for a pedagogically grounded policy that fosters cognitive expansion and ethical agency rather than passive technological adoption.

**Решение:** -

---

### 434 · R1982

**Hubungan Kepercayaan Generative AI dengan Ketegantungan AI pada Mahasiswa**

2026 · Universitas Airlangga Repository (Universitas Airlangga) · article, research article · id · https://core.ac.uk/download/738207727.pdf

Pesatnya perkembangan AI terutama GenAI melahirkan kebiasaan baru pada mahasiswa Indonesia dalam pergantian prosesi kognitif mahasiswa menjadi penggunaan GenAI berulang. Fenomena ini terbukti membawakan beberapa dampak negatif seperti gangguan memori, menurunkan keterlibatan emosional dalam belajar, dan kemampuan analytical thinking, critical thinking, dan decision making. Kepercayaan pada GenAI diduga menjadi pemicu utama dalam terbentuknya fenomena ini. Penelitian ini merupakan penelitian eksplanatori dengan pendekatan kuantitatif dengan metode survei dan teknik purposive sampling. Dilakukan survei berbentuk daring dengan media Google Form. Subjek penelitian terdiri dari 227 mahasiswa S1/D4 yang secara aktif menggunakan GenAI sebagai alat bantu pemenuhan kebutuhan akademik. Pengukuran kepercayaan terhadap GenAI menggunakan Human-Computer Trust Scale (Gulati, 2019) dengan total 12 item dan reliabilitas Cronbach’s Alpha 0,805. Pengukuran ketergantungan AI menggunakan AI Dependency Scale (Capinding, 2024) dengan total 18 item dan reliabilitas Cronbach’s Alpha 0,907. Analisis data dilakukan dengan uji korelasi Pearson dan uji regresi korelasi dengan bantuan perangkat lunak Jamovi versi 2.4.8. Hasil analisis menunjukkan terdapat hubungan positif signifikan antara trust in GenAI dan dependency AI pada mahasiswa di Indonesia dengan nilai korelasi Pearson sebesar 0,411 (p-value < ,001). Dapat dikatakan bahwa kedua variabel telah terbukti memiliki korelasi dalam tingkat sedang dan memiliki arti bahwa mahasiswa yang memiliki nilai kepercayaan yang tinggi juga memiliki tingkat ketergantungan yang tinggi pula.

**Решение:** ?

---

### 435 · R2532

**The Internalization Problem: From Containment to Structural Alignment in Post-Parity AI**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · en · https://doi.org/10.5281/zenodo.20123283

The Containment Paradox argument establishes that supervisory containment of AI sys ‐ tems depends on a capacity asymmetry between overseer and assessed system, and that this asymmetry dissolves rather than strains in the post-parity regime where AI capacity exceeds human-side anticipatory, specification, and enforcement adequacy on the relevant task family. The paper closes with the observation that alignment must become structurally internal, without articulating what this requires. We name that gap the Internalization Problem and develop a pluralistic response-shape. The response-shape rests on a three-locus typology of structural persistence: intra- agent (values the agent would endorse on reflection at any later capacity), inter-agent (alignment-relevant properties maintained by the equilibrium incentive structure of an AI ecology), and coupling-internal (properties maintained by the durable structure of human-AI dependency). Each locus is instantiated as a candidate pathway anchored in the existing four-paper framework: Pathway 1 (Deep-Formed Values) through UBE v1.1, Pathway 2 (Multi-AI Checks-and-Balances) through BtSV v1.2, Pathway 3 (Asymmetric Symbiosis) through CUA v1.2 as architectural precondition. A cross-cutting corrigibility and moral-uncertainty invariant operates across all three pathways in pathway-specific form. Pluralism here is structural, not aesthetic. Anticipation, specification, and enforce ‐ ment fail in different ways after parity, so the response needs three different persistence loci. The paper names fourteen pathway-internal open problems plus four cross-pathway open problems, a structured pathway-comparison matrix, and a cross-pathway failure cascade analysis. A hybrid evaluation toolkit operationalises the response-shape via five schema fields applied to three worked examples: Anthropic's Responsible Scaling Policy, Christiano and Xu's Eliciting Latent Knowledge , and the EU AI Act in conjunction with UK AISI evaluation standards. The paper is Track-Strategic in mode: it articulates the struc ‐ tural conditions a post-parity response would have to satisfy without claiming to supply the response itself. The closing chapter reframes the open problems as a research agenda for the alignment community

**Решение:** -

---

### 436 · R0449

**Navigating the complexity of AI adoption in psychotherapy by identifying key facilitators and barriers.**

2026 · Npj mental health research · article, journal article, journalarticle · eng · https://doi.org/10.1038/s44184-026-00199-1

Abstract Artificial intelligence (AI) technologies in mental healthcare offer promising opportunities to reduce therapists’ burden and enhance healthcare delivery, yet adoption remains challenging. This study identified key facilitators and barriers to AI adoption in mental healthcare, precisely psychotherapy, by conducting six online focus groups with patients and therapists, using a semi-structured guide based on the NASSS (Nonadoption, Abandonment, Scale-up, Spread, and Sustainability) framework. Data from N = 32 participants were analyzed using a combined deductive and inductive thematic analysis. Across the seven NASSS domains, 36 categories emerged. Sixteen categories were identified as factors facilitating adoption, including useful technology elements, the customization to user needs, and cost coverage. Eleven categories were perceived as barriers to adoption, encompassing the lack of human contact, resource constraints, and AI dependency. Further nine, such as therapeutic approach and institutional differences, acted as both facilitators and barriers depending on the context. Our findings highlight the complexity of AI adoption in mental healthcare and emphasize the importance of addressing barriers early in the development of AI technologies.

**Решение:** -

---

### 437 · R1195

**AI TRANSFORMING OUR TEACHING VIEW: DOES IT HELP OR BURDEN**

2026 · Zenodo · conferencepaper/ · uz · https://doi.org/10.5281/zenodo.21743553

Look back, forward, left, and right, and you can see the ubiquitous impact of Artificial Intelligence (AI) on human intellectual discipline. Undoubtedly, its impact on the education system has significantly changed pedagogical approaches, seemingly easing instructors' workload by aligning teaching methodologies directly with the topic at hand within seconds. The same picture can be seen among university students who are confident in using AI services for convenience in dealing with tasks, receiving ready answers from computational intelligence. All instructors today have already encountered almost 100% AI in students' work across all types of assessments, which is clearly different from genuine work. This issue is becoming more critical as students are abruptly ignoring teachers' instructions due to a continuous addiction to their pocket devices and a complete reliance on digital data services. Our paper is going to discuss three main questions, which are under the big concern: How does AI assist the teacher? How does AI assist student learning? How can language learners make good use of AI in current pedagogy?

**Решение:** -

---

### 438 · R4173

**ARTIFICIAL INTELLIGENCE IN MEDICAL EDUCATION: A SYSTEMATIC REVIEW OF ITS BENEFITS AND DRAWBACKS ON STUDENT LEARNING**

2025 · TPM Testing, psychometrics, methodology in applied psychology · review · en · https://doi.org/10.5281/zenodo.19629828

Background & Objective: Artificial Intelligence (AI) is revitalizing studies in medicine, providing new ways to facilitate learning of either form while raising alarms of its vice compared to virtue. However, there is a scarcity of synthesis of benefits versus limitations of AI in medical studies. Therefore, the objective of this systematic review was to determine the benefits versus drawbacks of AI in medical education with a focus on student engagement, learning outcomes, classroom interaction and cognition. Methodology: A systematic review was performed in accordance with the PRISMA 2020 reporting guideline. Search was done in Scopus, Web of Science, PubMed, ERIC, and Pakistan search engines (PakMediNet and HEC Digital Library). Studies from 2015 and onwards were included. After screening and eligibility assessment, 26 studies were included. A narrative synthesis of the studies was performed based on heterogeneity. Results: Some of the benefits of AI in education were better student engagement and participation (18/26) better learning and academic performance (17/26) and better interaction and collaboration (14/26). Major drawbacks were conflicting data on critical thinking (both improvement and overreliance on AI), and the challenges in implementation (especially in developing countries like Pakistan). Conclusion: AI has the potential to be beneficial to education and provides for interactive, personalized learning. However, cognitive dependency on AI and contextual challenges of implementation also require consideration.

**Решение:** -

---

### 439 · R0095

**The Architect's Report: AI-Assisted Cross-Disciplinary Research as Evidence of a Methodological Phase Transition**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint · en · https://doi.org/10.5281/zenodo.18888765

(Part 3 of a 3-part series.) This paper proposes and validates a research methodology termed connective abduction: the systematic identification of novel connections between existing, independently verified knowledge claims, with AI systems serving as the verification infrastructure that tests whether those connections hold logically and empirically. Unlike traditional research, which requires deep domain expertise to both generate and validate hypotheses, connective abduction decouples these functions: the human researcher identifies explanatory gaps and cross-domain patterns through abductive reasoning—connecting dots that exist in the published literature but have not been previously linked—while AI systems verify the logical soundness and empirical support of each proposed connection against the referenced sources. A hierarchical adversarial verification protocol is formalized, applying the cascade filtering principle (Ahn, 2026a) to research methodology: multiple independent AI verification layers, each applying progressively stricter evaluation criteria, reduce hallucination propagation risk logarithmically rather than linearly. The methodology is validated through a single-case study in which the present author—whose formal training consists of incomplete undergraduate coursework in chemistry and an in-progress bachelor's degree in computer science—produced two cross-disciplinary research manuscripts within approximately two days. This case is presented not as evidence of individual capability but as a diagnostic case for a structural transformation in knowledge production: a methodological phase transition in which the binding constraint on research shifts from knowledge accumulation to question design. Risks of the transition—including verification deficits, hallucination propagation, depth erosion, and structural uncontrollability—are addressed, and transparent reporting of AI-assisted methodology is proposed as a necessary component of the emerging paradigm. Revision Note (v2) v2 → v3 Changes: Added Section 1.1: historical bottleneck shift (print → search engine → AI)Expanded Section 4 case study: full exploratory trajectory with failed iterations (Paper 2 Phase 1–3, Paper 1 Phase 1–4 / v4 anchor, v9b failure, v10 directional)Added Section 4.1: equipment specification (Colab + consumer laptop)Added Section 4.5: failed iterations as methodological evidenceAdded Section 6.4: intuition as the new bottleneck; transparency as computational efficiency, not ethicsAdded Section 6.5: cooperation as survival strategy (Axelrod tit-for-tat)Added Section 7.0: structural uncontrollability — Manhattan Project / MAD analogy; "the only winning move is not to play"Added reflexive self-reference to Section 8: paper's own post-publication development as proof of methodologyStep 3 teaser: AI feedback asymmetry flagged as ongoing empirical investigationReferences: added Axelrod (1984), Oppenheimer (1945)

**Решение:** -

---

### 440 · R2669

**Cognitive Surrender in the Age of AI: How Organizations Can Navigate the Rise of Artificial Reasoning**

2026 · Human capital leadership. · article, journalarticle · und · https://doi.org/10.70175/hclreview.2020.35.4.1

Artificial intelligence has fundamentally altered how organizations make decisions, introducing what researchers term "System 3"—external, algorithmic cognition that operates alongside human intuition and deliberation. This article examines the phenomenon of cognitive surrender, where decision-makers uncritically adopt AI-generated outputs, and explores evidence-based organizational responses. Drawing on experimental research involving over 1,300 participants and recent studies of AI integration in professional settings, we identify key drivers of AI dependence and present actionable strategies for fostering balanced human-AI collaboration. Organizations that implement targeted interventions—including structured feedback mechanisms, calibrated incentive systems, and capability-building programs—can harness AI's benefits while preserving critical human judgment. The article concludes with a framework for building long-term organizational resilience in an era where the boundary between human and artificial cognition increasingly blurs.

**Решение:** -

---

### 441 · R4100

**The Impact of ChatGPT Dependence and Inert Thinking on Students' Academic Task Completion**

2025 · Information Technology Education Journal · article, journalarticle, review · und · https://doi.org/10.59562/intec.v4i3.9922

The increasing use of Artificial Intelligence (AI), particularly ChatGPT, among students has raised concerns about the emergence of inert thinking (passive thinking) and overreliance on technology in completing academic tasks. Guided by Inert Knowledge Theory and Dual Process Theory, this study analyzes the relationship between inert thinking and ChatGPT dependence on academic task completion among Informatics and Computer Engineering students at Makassar State University. Using a quantitative survey method, data were collected from 225 respondents through a snowball sampling technique and analyzed using the Structural Equation Modeling–Partial Least Squares (SEM-PLS) approach. The findings reveal that passive thinking significantly reduces students’ ability to complete academic tasks, while dependence on ChatGPT strongly increases inert thinking. However, ChatGPT dependence itself does not directly enhance task completion. These results indicate that excessive reliance on AI tools tends to weaken reflective and critical thinking processes, limiting students’ self-regulated learning. This study highlights the importance of responsible AI use in higher education to maintain cognitive engagement and academic integrity. Educators and policymakers should develop strategies and digital literacy programs that encourage reflective learning and critical evaluation, ensuring AI serves as a supportive tool, not a substitute for human thinking

**Решение:** ?

---

### 442 · R0879

**From Chalkboards to AI Prompts: Exploring the Lived Experiences of K-12 Educators in Patna and Siliguri**

2026 · RESEARCH REVIEW International Journal of Multidisciplinary · article, journalarticle, journal article · und · https://doi.org/10.31305/rrijm.2026.v11.n07.001

Artificial Intelligence, particularly Generative Artificial Intelligence (GenAI) is taking shape as a pervasive phenomenon in K-12 Education in India. With GenAI being adopted for easing teacher workload and enhancing student learning, what remains unclear are stances of educators from schooling structures beyond well-resourced and metropolitan contexts in India. The study examines teacher voices from Patna (Bihar) and Siliguri (West Bengal), and how they understand AI not as a technological intervention or means of optimization, but as a phenomena that teachers adapt, resist, regulate, and negotiate within their everyday teaching practices. Drawing on interviews conducted in February–March 2026 with 16 K–12 educators from private schools across Patna and Siliguri, this study uses reflexive thematic analysis, informed by Ecological Teacher Agency and an Enactivist Account of Agency, and investigates educators’ perspectives and AI practices with respect to (i) their perception of AI within the context of teaching and learning ; (ii) their practical AI applications in both classroom instruction and back-end preparation ; (iii) their negotiation of AI use in relation to professional judgement, autonomy and creative agency; (iv) their concerns around student AI dependency, ethical implications, and changing dynamics with students; and (v) teachers perceived needs for AI training and institutional support. The research concludes that AI’s meaningful integration in K-12 schools depend upon empowering teachers as critically aware sense-makers of what AI is and what it can or fails to do, within a supported institutional system.</jats:p

**Решение:** -

---

### 443 · R3308

**Enhancing Human-AI Collaboration in AI-Assisted Decision-Making for Individuals and Groups**

2025 · Purdue University Graduate School · dissertation/thesis · https://doi.org/10.25394/pgs.28817156

AI-assisted decision-making systems are increasingly integrated into various domains, from individual to collective decision-making. However, their effectiveness depends on how well users navigate AI limitations, particularly when models exhibit systematic errors under distribution shifts. Although AI tools aim to improve decision quality, users may struggle to calibrate their reliance on these AI tools effectively. This challenge is even more complex in group decision-making, where social dynamics further influence the reliance on AI. Despite the widespread adoption of AI in both individual and group settings, little is known about how decision-makers adjust their reliance in response to AI failures. This dissertation investigates: (1) How do individuals interact with AI-assisted tools, particularly when faced with distribution shifts? Can external interventions help individuals rely on AI-assisted tools appropriately without modifying the AI model? (2) How do group dynamics shape AI reliance compared to individual interactions, and can external interventions reduce the negative effects of group dynamics to promote critical engagement with AI recommendations? Through human-subject experiments in house price prediction (individuals) and recidivism prediction (groups), we find that individuals, despite recognizing distribution shifts, tend to over-rely on AI because they overestimate its capabilities. Groups exhibit even higher reliance, likely driven by groupthink and a desire to avoid conflict, as they treat AI recommendations as an anchor. Although group decisions are generally less biased than individual ones, their increased dependence on flawed AI raises concerns about the robustness of decisions. To mitigate these issues, we propose two external interventions: (1) hands-on user education, where individuals explore AI limitations in an interactive sandbox, and (2) an LLM-powered devil's advocate that challenges groupthink by prompting critical discussions. The interactive sandbox allows users to engage with data examples and model behaviors, helping them better understand AI limitations and reduce over-reliance. Meanwhile, the LLM-powered devil's advocate fosters deeper deliberation, helping groups critically evaluate AI recommendations and develop more appropriate reliance on AI, ultimately improving group-AI collaborative decision-making. These insights emphasize that enhancing decision-making with AI-assisted tools requires not only improving AI models but also refining how humans interact with them. This underscores the importance of understanding and improving how individuals and groups develop appropriate reliance on AI and make decisions based on AI-assisted recommendations. Future research should explore personalized AI interventions that address confidence miscalibration, scalable AI literacy training through adaptive model-specific tutorials, explore the group-AI interaction in complex group settings and LLM-powered facilitators that enhance group deliberation and decision-making. Additionally, future work should ensure that AI-driven decision support remains transparent, accountable, and capable of fostering long-term improvements in human reasoning.

**Решение:** -

---

### 444 · R3070

**PROBLEMS OF USING ARTIFICIAL INTELLIGENCE IN NET ART PRACTICES**

2025 · “Müasir incəsənət məkanında süni intellekt: problemlər və perspektivlər” Beynəlxalq elmi-nəzəri konfransın mündəricatı · conference-paper · en · https://doi.org/10.25045/asucaai.2025.32

The article reveals the impact of artificial intelligence (AI) on the development of net art – a form of media art, the main tool and environment of which is the Internet. AI is considered in the context of the evolution of net art. Modern artistic practices that use algorithmic technologies are analyzed, and the main ethical and social challenges associated with the introduction of AI into artistic processes are identified. Special attention is paid to the issue of authorship, as well as the transformation of the interaction between the artist, the viewer, and the artistic environment. The possibility of democratization and development of activist net-art practices is considered, thanks to the wide availability of AI. However, the risks of censorship, information manipulation, and commercialization of the creative process are identified due to the dependence of AI on large technological corporations. The study emphasizes the need for a critical reflection of these processes to understand future trends in the development of net art in the context of modern visual culture.

**Решение:** -

---

### 445 · R2253

**THE ANALYSIS OF ARTIFICIAL INTELLIGENCE (AI) USAGE PHENOMENA IN ONLINE DISCUSSIONS OF ECONOMIC EDUCATION STUDENTS**

2026 · EDUNOMIA Jurnal Ilmiah Pendidikan Ekonomi · article, journalarticle · en · https://doi.org/10.24127/edunomia.v6i2.11316

ABSTRACT The rapid integration of Artificial Intelligence (AI) in the higher education ecosystem poses new challenges to the originality of thought and students' cognitive processes. While AI offers efficiency, its unregulated use has the potential to degrade critical inquiry skills, particularly in courses demanding a profound understanding of human behavior. This study aims to analyze the phenomenon of AI usage among second-semester students in the Economic Education Study Program, specifically within the "Human Development" course. A descriptive qualitative approach with a case study design was employed. Data were collected from 32 discussion transcripts on the Mentari platform and validated through time-stamp analysis and in-class cross-verification (member checking). The findings reveal that 87.5% of students utilized AI to complete their discussion assignments, characterized by high linguistic homogeneity, formal-synthetic syntax, and a lack of contextual reflection. Empirical evidence shows a significant "knowledge-wisdom gap," where students produce sophisticated text without conceptual mastery. The study concludes that AI dependency at UNPAM has created an "academic facade," shifting the learning process from reflective inquiry to automated task completion. It is recommended that lecturers redesign discussion prompts into "AI-proof" assignments that prioritize local context and personal reflection to restore pedagogical integrity in the digital era. Keywords: artificial intelligence; development of learners; economic education; mentari unpam; online learning ABSTRAK Pesatnya integrasi Artificial Intelligence (AI) dalam ekosistem pendidikan tinggi membawa tantangan baru terhadap orisinalitas pemikiran dan proses kognitif mahasiswa. Meskipun AI menawarkan efisiensi, penggunaannya yang tidak teregulasi berpotensi mendegradasi kemampuan inkuiri kritis, terutama dalam mata kuliah yang menuntut pemahaman mendalam mengenai perilaku manusia. Penelitian ini bertujuan untuk menganalisis fenomena penggunaan AI di kalangan mahasiswa semester dua Program Studi Pendidikan Ekonomi, khususnya pada mata kuliah "Perkembangan Peserta Didik". Pendekatan kualitatif deskriptif dengan desain studi kasus digunakan dalam penelitian ini. Data dikumpulkan dari 32 transkrip diskusi di platform Mentari dan divalidasi melalui analisis time-stamp serta verifikasi silang di dalam kelas (member checking). Temuan menunjukkan bahwa 87,5% mahasiswa menggunakan AI untuk menyelesaikan tugas diskusi mereka, yang ditandai dengan homogenitas linguistik yang tinggi, sintaksis formal-sintetis, dan kurangnya refleksi kontekstual. Bukti empiris menunjukkan adanya celah pengetahuan-kebijaksanaan (knowledge-wisdom gap) yang signifikan, di mana mahasiswa menghasilkan teks yang canggih tanpa penguasaan konsep. Penelitian menyimpulkan bahwa ketergantungan pada AI di UNPAM telah menciptakan fasad akademik, mengubah proses belajar dari inkuiri reflektif menjadi penyelesaian tugas otomatis. Disarankan agar dosen merancang ulang instruksi diskusi menjadi tugas yang tahan AI (AI-proof) dengan memprioritaskan konteks lokal dan refleksi personal untuk memulihkan integritas pedagogis di era digital. Kata Kunci:​ artificial intelligence; mentari unpam; pembelajaran daring; pendidikan ekonomi; perkembangan peserta didik

**Решение:** -

---

### 446 · R4434

**ПРИМЕНЕНИЕ ТРАНЗАКТНОГО АНАЛИЗА ДЛЯ ПРЕПОДАВАНИЯ ИНОСТРАННОГО ЯЗЫКА В НЕЯЗЫКОВОМ ВУЗЕ И РАЗВИТИЕ ЭГО-СОСТОЯНИЯ «ВЗРОСЛОГО» ВТОРИЧНОЙ ЯЗЫКОВОЙ ЛИЧНОСТИ**

2025 · Мир науки, культуры, образования · text/paper · https://doi.org/10.24412/1991-5497-2025-2111-307-311

В последнее время поднимаются вопросы и опасения по поводу потери контакта между преподавателем и студентом, низкой вовлеченности в образование студентов и их пассивности на занятиях, что обусловлено как программой, чрезмерной зависимостью от искусственного интеллекта и гаджетов, так и многими психологическими аспектами. Транзактный анализ как инструмент для выстраивания работы в деятельности «человек ‒ человек» имеет большой потенциал для помощи преподавателю иностранного языка в высшей школе. Помимо таких инструментов, как переключение эго-состояний (Родитель, Взрослый, Ребенок), применение соглашения о взаимной ответственности, удержании в балансе позиции «я в полном порядке ‒ ты в полном порядке», преподавателю особое внимание следует уделить эго-состоянию Взрослый, особенно проявлению этого состояния на вербальном и невербальном уровнях на иностранном языке, так как именно это эго-состояние является превалирующим в профессиональной среде. Задача преподавателя – демонстрировать адекватное эго-состояние Взрослого профессионала на иностранном языке, чтобы служить ролевой моделью для студентов.

**Решение:** -

---

### 447 · R2248

**The Assumption Stack: What AI-Assisted Development Takes for Granted, and Who Gets Left Out**

2026 · Zenodo (CERN European Organization for Nuclear Research) · conference object, text/poster, article · https://doi.org/10.5281/zenodo.23361544

Software development increasingly incorporates AI assistance, but the conditions that make its use possible are unevenly distributed [1&ndash;4]. This poster asks what AI-assisted development means for research software engineers (RSEs) in less-resourced countries and communities, and whether building research software around an assumed dependence on AI is equitable, or even wise. This poster proposes a provisional framework, the assumption stack: a set of access assumptions on which AI-assisted research software depends, each a potential source of inequity. Connectivity: Connections adequate for the chosen tools and workflows. Affordability and payment: Affordable tools and usable payment channels. Compute and energy: Sufficient hardware and power, locally or remotely. Language and context: Support for users&rsquo; languages and programming stacks. Governance: Decision-making processes that represent affected communities. Workflows that assume AI access could restrict who can reproduce results, contribute code and maintain shared software, making participation depend on access as well as ability. As work in progress, this poster maps the assumption stack against current evidence and examines design and structural responses and their trade-offs: local and open-weight models, low-bandwidth and intermittency-tolerant workflows, language-aware tooling, shared compute, and participatory governance. A descriptive analysis of International RSE Survey data provides context on respondents&rsquo; AI use and the survey&rsquo;s coverage across country income groups [5]. Planned work includes network-emulation studies and interviews with RSEs working under access constraints. The poster invites the community to weigh a harder question: should research software assume AI access at all?

**Решение:** -

---

### 448 · R0814

**Contradictions and Boundary Negotiation in Human–AI Interaction: Insights into Cyborg Anxiety and AI Literacy Among University Students**

2026 · International Journal of Human-Computer Interaction · journalarticle/journal contribution, article · en · https://doi.org/10.1080/10447318.2026.2637823

Generative artificial intelligence (GenAI) has rapidly entered university students’ academic and everyday lives, yet its implications for human–computer interaction remain underexplored. Using a qualitative diary study, this research analyzed 141 diary entries from undergraduate communication students in Eastern China (June 5–25, 2025) through reflexive thematic analysis. Findings reveal a three-stage mechanism shaping student experience: Contradiction → Negotiation → Subjectivity Outcomes. Students described a persistent tension between functional dependence on GenAI for efficiency and perceived erosion of subjectivity, including cognitive atrophy and self-worth doubt, often experienced as a fear of displacement. In response, they engaged in boundary negotiation through contextual role allocation and the creation of forbidden zones in areas such as original creation and emotional expression. This process produced two outcomes: Cyborg anxiety and critical boundary literacy. The study shifts human–AI research from adoption to identity and existence.

**Решение:** -

---

### 449 · R3603

**LLM-pohjaiset agentit ohjelmistotestauksessa : systemaattinen kartoitustutkimus**

2025 · LUTPub (LUT University) · dissertation · en

This thesis presents a Systematic Mapping Study (SMS) on Large Language Model (LLM)-based agents in software testing. The aim of this study is to explore the usage of these agents, what type of different architectures have been applied in software testing and what advantages or limitations have been reported. The study systematically reviews publications from IEEE Xplore and Springer Nature Link from recent years. 13 studies related to LLM-based agents in software testing were selected for comprehensive analysis. Results show that LLM-based agents are being applied in various task in the field of software testing, including test case generation, unit testing, debugging, GUI testing and analysis of test cases. Most of the studies included focused on multi-agent architectures which enhance automation, test coverage and accuracy through collaboration between agents and iterative methods used by these agents. Included publications also reported limitations such as scalability, dependency on LLM, prompts and hallucinations. Thesis also covers how traditional test automation has evolved to LLM-based agents. The thesis concludes that LLM-based are potentially great addition software testing workflows by improving efficiency and automation, but more research is needed to standardize architectures and apply them in large-scale projects and processes.

**Решение:** -

---

### 450 · R5177

**Effect of a Au contact layer on the microwave performance of YBa₂Cu₃O₇₋ₓ thin films**

2001

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -
