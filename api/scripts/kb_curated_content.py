"""
Curated Class 10 syllabus and concept notes (paraphrased from public board syllabi).
Used as reliable RAG source when web scraping returns thin content.
"""

# (board, subject, slug, markdown_body)
CURATED_DOCUMENTS = [
    (
        "CBSE",
        "Science",
        "curated_syllabus_units",
        """# CBSE Class 10 Science — Syllabus & Key Concepts (2025-26)

## Exam structure
- Theory: 80 marks | Internal assessment: 20 marks
- Five units with competency mix: knowledge (46%), application (22%), analysis/evaluation (32%)

## Unit I: Chemical Substances — Nature and Behaviour (25 marks)

### Chemical Reactions and Equations
- Balanced chemical equations; types: combination, decomposition, displacement, double displacement, precipitation
- Oxidation and reduction; exothermic and endothermic reactions

### Acids, Bases and Salts
- Definitions using H+ and OH- ions; pH scale (0-14)
- Neutralisation; common salts: NaCl, NaHCO3, washing soda, bleaching powder, Plaster of Paris

### Metals and Non-metals
- Physical and chemical properties; reactivity series
- Ionic compounds; extraction (metallurgy basics); corrosion and prevention

### Carbon and Its Compounds
- Covalent bonding; homologous series; nomenclature
- Versatile nature of carbon; saturated vs unsaturated hydrocarbons
- Ethanol and ethanoic acid; soaps and detergents

## Unit II: World of Living (25 marks)

### Life Processes
- Nutrition (autotrophic, heterotrophic); respiration; transportation in plants and animals; excretion

### Control and Coordination
- Nervous system in animals; reflex arc; coordination in plants (tropisms, hormones)

### How do Organisms Reproduce?
- Asexual and sexual reproduction; reproductive health

### Heredity
- Mendel's laws; sex determination; variation (evolution topics may be reduced per latest CBSE notice)

## Unit III: Natural Phenomena (12 marks)

### Light
- Reflection and refraction; mirror and lens formulae; power of lens
- Human eye; defects of vision and corrections; dispersion; scattering of light

## Unit IV: Effects of Current (13 marks)

### Electricity
- Ohm's law; resistance; series and parallel circuits; electrical power and energy

### Magnetic Effects of Electric Current
- Magnetic field due to current; electromagnet; electric motor; electromagnetic induction; domestic circuits

## Unit V: Natural Resources (5 marks)

### Our Environment
- Ecosystems; food chains and webs; ozone layer; waste management; biodegradable vs non-biodegradable

## Question style hints for examiners
- Section A: 1-mark MCQs / assertion-reason on definitions and facts
- Section B: 2-mark very short answers on laws, diagrams, one-step numericals
- Section C: 3-mark short answers with reasoning or small derivations
- Section D: 5-mark long answers with labelled diagrams
- Section E: 4-mark case-based / source-based units linking environment or daily-life context
""",
    ),
    (
        "CBSE",
        "Mathematics",
        "curated_syllabus_units",
        """# CBSE Class 10 Mathematics — Syllabus & Key Concepts

## Units and themes
1. **Number Systems** — Euclid's division lemma; fundamental theorem of arithmetic; irrational numbers; decimal expansions
2. **Algebra** — Polynomials (zeros, relationship between zeros and coefficients); pair of linear equations (graphical and algebraic methods); quadratic equations (factorisation, formula, nature of roots); arithmetic progressions
3. **Coordinate Geometry** — Distance formula; section formula; area of triangle
4. **Geometry** — Similar triangles (criteria, areas); circles (tangent theorems); constructions
5. **Trigonometry** — Ratios; identities; heights and distances
6. **Mensuration** — Surface areas and volumes of combinations of solids; conversion of solids
7. **Statistics and Probability** — Mean, median, mode of grouped data; probability of events

## Typical question types
- Prove similarity or apply Pythagoras in coordinate geometry
- Word problems on AP and quadratic equations
- Prove trigonometric identities
- Surface area/volume of frustum or combined solids
- Cumulative frequency ogive and median
""",
    ),
    (
        "CBSE",
        "Social Science",
        "curated_syllabus_units",
        """# CBSE Class 10 Social Science — Syllabus Overview

## History (India and the Contemporary World)
- The Rise of Nationalism in Europe; Nationalism in India
- The Making of a Global World; The Age of Industrialisation
- Print Culture and the Modern World

## Geography (Contemporary India)
- Resources and Development; Forest and Wildlife; Water Resources
- Agriculture; Minerals and Energy; Manufacturing Industries; Lifelines of National Economy

## Political Science (Democratic Politics)
- Power Sharing; Federalism; Gender, Religion and Caste
- Political Parties; Outcomes of Democracy

## Economics (Understanding Economic Development)
- Development; Sectors of the Indian Economy
- Money and Credit; Globalisation and the Indian Economy; Consumer Rights

## Exam skills
- Map-based questions in Geography
- Source-based questions in History
- Case studies on democracy and development
""",
    ),
    (
        "CBSE",
        "English",
        "curated_syllabus_units",
        """# CBSE Class 10 English — Syllabus Overview

## Reading
- Unseen passages (discursive / case-based); inference and vocabulary in context

## Writing
- Formal letter (complaint, enquiry, order); analytical paragraph; article/story (as per latest pattern)

## Grammar
- Determiners; tenses; modals; subject-verb agreement; reported speech; clauses; connectors

## Literature (First Flight + Footprints)
- Prose and poetry: theme, character, literary devices, extract-based questions
- Long answer: value-based and analytical responses with textual evidence
""",
    ),
    (
        "ICSE",
        "Science",
        "curated_syllabus_units",
        """# ICSE Class 10 Science — Syllabus (Physics, Chemistry, Biology)

Three separate theory papers (80 marks each) + 20 marks internal assessment each.

## Physics
1. Force, Work, Power and Energy — machines, levers, power
2. Light — reflection, refraction, lenses, dispersion, scattering
3. Sound — echoes, SONAR, loudness, pitch, quality, noise pollution
4. Electricity and Magnetism — Ohm's law, household circuits, electromagnetic induction, transformers
5. Heat — specific heat, change of state, latent heat
6. Modern Physics — radioactivity, nuclear fission/fusion (introductory)

## Chemistry
1. Periodic Properties and Chemical Bonding
2. Acids, Bases and Salts; Analytical Chemistry (ions)
3. Mole Concept and Stoichiometry
4. Electrolysis; Metallurgy
5. Study of Compounds (HCl, ammonia, nitric acid, sulphuric acid, NaOH, etc.)
6. Organic Chemistry — hydrocarbons, functional groups, polymers

## Biology
1. Basic Biology — cell structure, tissues
2. Plant Physiology — photosynthesis, transpiration, absorption
3. Human Anatomy and Physiology — circulatory, excretory, nervous, endocrine
4. Population and Human Evolution
5. Pollution and conservation

## ICSE paper pattern
- Section I (40 marks): compulsory short answers
- Section II (40 marks): answer 4 out of 6 long questions
""",
    ),
    (
        "ICSE",
        "Mathematics",
        "curated_syllabus_units",
        """# ICSE Class 10 Mathematics — Key Topics

- Commercial Mathematics: GST, banking, shares
- Algebra: quadratic equations, ratio and proportion, remainder theorem, matrices (intro)
- Geometry: similarity, circles, tangents, constructions
- Mensuration: cylinder, cone, sphere, combination of solids
- Trigonometry: identities, heights and distances
- Statistics: mean, median, mode; ogives
- Coordinate geometry: section formula, equation of line
- Probability: classical definition, simple events
""",
    ),
    (
        "ICSE",
        "English",
        "curated_syllabus_units",
        """# ICSE Class 10 English — Key Areas

## Language (Paper 1)
- Composition: narrative, descriptive, argumentative
- Letter writing: formal and informal
- Unseen comprehension and summary
- Grammar: transformation of sentences, prepositions, conjunctions

## Literature (Paper 2)
- Drama, poetry, prose from prescribed texts
- Context questions and critical appreciation
- Character sketch and theme-based long answers
""",
    ),
    (
        "ICSE",
        "History & Civics",
        "curated_syllabus_units",
        """# ICSE Class 10 History & Civics

## History
- The Indian National Movement (1857-1947)
- First War of Independence; growth of nationalism; Gandhian era; partition and independence
- Contemporary world events (WWI, WWII, UN) as per CISCE syllabus

## Civics
- The Union Legislature, Executive, Judiciary
- Local self-government; fundamental rights and duties
- Directive Principles; challenges to democracy
""",
    ),
    (
        "WB",
        "Physical Science",
        "curated_syllabus_units",
        """# West Bengal Madhyamik — Physical Science and Environment (90 marks written)

## Environment
- Concerns about Our Environment (5 marks)

## Common / Chemistry foundations
- Behaviour of Gases (8); Chemical Calculations (4)
- Periodic Table and Periodicity (6); Ionic and Covalent Bonding (6)
- Electricity and Chemical Reactions (6)
- Inorganic Chemistry in Laboratory and Industry (8)
- Metallurgy (5); Organic Chemistry (8)

## Physics
- Thermal Phenomena (5)
- Light (12) — reflection, refraction, lenses
- Current Electricity (12) — Ohm's law, circuits, power
- Atomic Nucleus (5) — radioactivity basics

## Question distribution
- Mix of MCQs (Group A), very short (Group B), short (Group C), long (Group D)
- Emphasis on numerical problems in electricity and chemical calculations
""",
    ),
    (
        "WB",
        "Life Science",
        "curated_syllabus_units",
        """# West Bengal Madhyamik — Life Science and Environment (90 marks written)

## Themes and weightage
1. Control and Coordination in living organisms (19 marks)
2. Continuity of life — reproduction, growth (17 marks)
3. Heredity and common genetic diseases (15 marks)
4. Evolution and adaptation (15 marks)
5. Environment, resources and conservation (24 marks)

## Key concepts
- Nervous and hormonal coordination in humans and plants
- Asexual and sexual reproduction; reproductive health
- Mendelian inheritance; sex-linked disorders overview
- Natural selection and adaptation; evidence of evolution
- Biodiversity, pollution, conservation practices

## Exam style
- Many short-answer questions; diagrams of human organs and plant parts
- Application questions on health, environment, and genetics
""",
    ),
    (
        "WB",
        "Mathematics",
        "curated_syllabus_units",
        """# West Bengal Madhyamik — Mathematics

## Algebra
- Quadratic equations; arithmetic and geometric progressions
- Ratio, variation, partnership

## Geometry and Trigonometry
- Theorems on circles and tangents; similarity
- Trigonometric ratios and identities; heights and distances

## Mensuration and Statistics
- Area and volume of solids
- Mean, median, ogive

## Madhyamik pattern
- Objective (1 mark), very short (1 mark), short (2 marks), long (3-4 marks)
""",
    ),
    (
        "WB",
        "English",
        "curated_syllabus_units",
        """# West Bengal Madhyamik — English

## Grammar and composition
- Article, preposition, voice, narration, transformation
- Letter and paragraph writing

## Comprehension
- Unseen passage with vocabulary and inference

## Literature
- Textbook-based short and long questions on prose and poetry
""",
    ),
    (
        "WB",
        "Bengali",
        "curated_syllabus_units",
        """# West Bengal Madhyamik — Bengali (First Language)

## Grammar (Byakaran)
- Samas, sandhi, pratyay, alankar
- Sabdartha, bakyartha

## Composition
- Prabandha (essay), patra (letter), anuchchhed

## Literature
- Gadya and padya from prescribed WBBSE texts
- MCQ and short questions on authors and literary context
""",
    ),
    (
        "common",
        "Science",
        "exam_question_framing",
        """# Class 10 Science — Question Framing Guide (All Boards)

Use these patterns when generating original questions (do not copy textbook wording).

## Objective / 1-mark
- Define, state law, identify diagram part, match column, assertion-reason

## Very short (2 marks)
- State difference between two concepts; one numerical with given formula; label diagram

## Short (3 marks)
- Explain process with diagram; derive formula; numerical with two steps

## Long (5 marks)
- Describe experiment with observation table; compare two systems; application to daily life

## Case-based (4 marks)
- Short passage on environment/health/technology followed by 2-3 sub-questions

## Cognitive levels
- Easy: direct recall and single-step numerical
- Medium: application and two-step reasoning
- Hard: multi-concept integration and novel scenarios
""",
    ),
]
