# Unit 5: Clinical knowledge, decision making and standardised terminologies

This unit covers INC Unit VI, **Clinical Knowledge & Decision Making** (3 hours theory, 6 hours lab). It has two parts: how knowledge management improves decisions in clinical care and in health policy, and the standardised languages (terminologies and classifications) that make clinical data computable: SNOMED CT, the SNOMED CT to ICD-10-CM map, NANDA-I, NOC and the Omaha System.

## 5.1 Knowledge and knowledge management

**Knowledge** is information that has been understood, connected and tested in experience. It is of two kinds:

| Tacit knowledge | Explicit knowledge |
| --- | --- |
| Personal, gained by experience, hard to write down | Written, recorded, easy to share |
| The senior nurse who "knows" a child is becoming sick before the numbers change | Protocols, guidelines, textbooks, care plans, research papers |

**Knowledge management (KM)** is the deliberate process of **creating, capturing, organising, storing, sharing and applying** knowledge so that an organisation makes better decisions.

```text
  Create/acquire ─► Capture/codify ─► Store/organise ─► Share ─► Apply/use
        ▲                                                           │
        └──────────────────── evaluate and update ◄─────────────────┘
```

Nonaka and Takeuchi's **SECI model** shows how knowledge moves between the two kinds:

- **Socialisation** (tacit → tacit): learning by working alongside an experienced nurse.
- **Externalisation** (tacit → explicit): an expert writes a protocol or care pathway.
- **Combination** (explicit → explicit): guidelines from many sources merged into a hospital manual.
- **Internalisation** (explicit → tacit): a nurse practises the protocol until it becomes second nature.

**KM tools in health care**: clinical guidelines and protocols, care pathways, intranet policy libraries, e-learning, online databases (PubMed, Cochrane), communities of practice, case discussions, morbidity and mortality reviews, lessons-learned reports from incidents, clinical decision support systems.

## 5.2 Role of knowledge management in decision making

### Clinical context

- Puts the **best current evidence** at the bedside (point-of-care references, order sets based on guidelines).
- Reduces variation in care between nurses, wards and hospitals.
- Prevents errors through alerts and checklists.
- Shares the experience of experts with new staff.
- Supports nursing process steps: assessment prompts, suggested nursing diagnoses, linked interventions and outcomes.

### Policy context

- Managers and governments use summarised data (dashboards, programme reports, surveillance data) to decide where to place staff, beds, medicines and money.
- Evidence from research and evaluations shapes national programmes and guidelines.
- Knowledge from one district's success can be spread to others (best practices).

## 5.3 Clinical decision support systems (CDSS)

A **clinical decision support system** is software that gives clinicians **patient-specific assessments or recommendations** at the right time to help decisions.

**Types**

| Type | How it works | Example |
| --- | --- | --- |
| Knowledge-based | Uses a knowledge base of **IF–THEN rules** written by experts from guidelines | IF potassium > upper limit THEN alert the nurse |
| Non-knowledge-based | Uses **machine learning**: software that learns patterns from large past data sets | A sepsis-risk score that predicts deterioration from vital-sign trends |

**Forms of decision support**: alerts and warnings, reminders, order sets, care plan templates, clinical guidelines, dose calculators, early-warning scores (e.g. NEWS), diagnostic suggestions, links to reference information ("infobuttons").

**Components of a knowledge-based CDSS**: a **knowledge base** (rules), an **inference engine** (applies rules to patient data) and a **communication mechanism** (screen alert, message).

**Benefits**: safer prescribing and administration, earlier recognition of deterioration, better adherence to guidelines.

**Cautions**: alert fatigue; rules may be out of date; machine-learning tools may be biased by the data they learned from and may not explain their reasoning; the final decision and accountability stay with the clinician.

## 5.4 Why standardised languages are needed

Without standard terms, one nurse writes "bedsore", another "pressure sore", another "decubitus ulcer". A computer counts them as three different problems. **Standardised terminologies** give each concept one agreed name and code so that:

- data can be shared and understood across systems (semantic interoperability);
- nursing care can be counted, compared, audited and researched;
- decision support rules can work;
- nursing's contribution to outcomes becomes visible in national data.

| Kind | What it is | Examples |
| --- | --- | --- |
| **Terminology** (reference terminology) | A large, detailed set of concepts with codes and relationships, used for recording care | SNOMED CT |
| **Classification** | Groups concepts into categories, mainly for statistics and reporting | ICD-10, ICD-11, ICD-10-CM |
| **Interface/nursing terminology** | Terms nurses use in care plans | NANDA-I, NIC, NOC, Omaha System, ICNP |

## 5.5 SNOMED CT

**SNOMED CT** (Systematized Nomenclature of Medicine – Clinical Terms) is the most comprehensive, multilingual clinical health terminology in the world. It is maintained by **SNOMED International**. India uses it as the **primary clinical terminology** in its EHR standards and it has been made freely available in India.

**Structure**

| Component | Meaning | Example |
| --- | --- | --- |
| **Concept** | A clinical meaning, with a unique numeric **concept identifier** | Myocardial infarction |
| **Description** | Words that name the concept: a **fully specified name**, a **preferred term** and **synonyms** | "Heart attack" and "MI" are synonyms linked to the same concept |
| **Relationship** | Links between concepts. The **"is a"** relationship builds a hierarchy; **attribute** relationships give details | Myocardial infarction *is a* ischaemic heart disease; *finding site* = myocardium |

Concepts are arranged in **top-level hierarchies** such as clinical finding, procedure, body structure, organism, substance, pharmaceutical/biologic product, observable entity, situation with explicit context, and others.

**Uses**: recording problems, findings and procedures in EHRs; decision support; data retrieval for audit and research; nursing documentation (it includes many nursing concepts).

## 5.6 ICD and the SNOMED CT to ICD-10-CM map

- **ICD** (International Classification of Diseases) is the **WHO** classification used for morbidity and mortality statistics, health planning and insurance claims. **ICD-10** codes start with a letter followed by digits (e.g. a chapter letter + numbers). **ICD-11** came into effect on **1 January 2022** and is designed for electronic use.
- **ICD-10-CM** (Clinical Modification) is the **United States** version of ICD-10 used for coding diagnoses, with more detailed codes (3–7 characters).
- **SNOMED CT** is detailed and used at the point of care; **ICD** is coarser and used for statistics and billing. A clinician should not have to code twice.

The **SNOMED CT to ICD-10-CM Map** (released by the US National Library of Medicine together with SNOMED International) links SNOMED CT concepts to ICD-10-CM codes so that a diagnosis recorded once in SNOMED CT can be turned into an ICD-10-CM code (semi-automatically) for reporting and claims.

```text
  Nurse/doctor records ──►  SNOMED CT concept  ──map rules──►  ICD-10-CM code
  at the bedside            (detailed, clinical)                (statistics, billing)
```

Mapping is not always one-to-one: one SNOMED CT concept may need **map rules** (for example, based on age or sex) to choose the right code, and some need human review.

| Feature | SNOMED CT | ICD-10 / ICD-10-CM |
| --- | --- | --- |
| Type | Clinical terminology | Statistical classification |
| Purpose | Record clinical care in detail | Count, report, bill |
| Size | Very large (hundreds of thousands of concepts) | Smaller |
| Owner | SNOMED International | WHO (ICD-10); US NCHS (ICD-10-CM) |

## 5.7 Standardised nursing terminologies

The American Nurses Association recognises several nursing terminologies. The syllabus names NANDA, NOC and the Omaha System; NIC is learned with them because the three are linked (NNN).

### NANDA-I (NANDA International) nursing diagnoses

- A **nursing diagnosis** is a clinical judgement about a human response to health conditions or life processes, for which the nurse is accountable.
- Each diagnosis has a **label**, **definition**, **defining characteristics** (signs and symptoms), **related factors** (causes) and, for risk diagnoses, **risk factors**.
- **Types**: problem-focused, risk, health-promotion and syndrome diagnoses.
- Organised in **Taxonomy II** with **13 domains** (e.g. Health promotion, Nutrition, Elimination and exchange, Activity/rest, Safety/protection) and classes within them.
- Written in **PES** format: Problem + Etiology + Signs/symptoms. Example: *Impaired skin integrity related to prolonged immobility as evidenced by a stage 2 pressure injury over the sacrum.*

### NIC (Nursing Interventions Classification)

Standard list of nursing interventions (treatments a nurse performs), each with a label, definition and list of activities, developed at the University of Iowa.

### NOC (Nursing Outcomes Classification)

- Developed at the **University of Iowa**; a standard list of **patient outcomes** that are sensitive to nursing care.
- Each outcome has a **label**, **definition**, a list of **indicators** and a **five-point Likert measurement scale** (1 = worst, 5 = best), so change can be measured before and after care.
- Example: Outcome "Tissue integrity: skin and mucous membranes", indicator "skin intactness", rated 2 on admission and 4 at discharge.

```text
  NANDA-I diagnosis  ──►  NIC interventions  ──►  NOC outcomes (rated 1–5)
  Impaired skin           Pressure management       Tissue integrity
  integrity               Skin surveillance         2 → 4
```

### Omaha System

Developed by the **Visiting Nurse Association of Omaha, Nebraska (USA)**, mainly for **community, home and public health** nursing. It has three linked parts:

| Part | Content |
| --- | --- |
| **Problem Classification Scheme** | Client problems grouped in **4 domains**: Environmental, Psychosocial, Physiological and Health-related behaviours |
| **Intervention Scheme** | **4 categories**: Teaching, guidance and counselling; Treatments and procedures; Case management; Surveillance; each applied to a target and a problem |
| **Problem Rating Scale for Outcomes** | Rates **Knowledge**, **Behaviour** and **Status** on a **1–5** scale at intervals |

It suits Indian community health nursing, for example rating a mother's knowledge of breastfeeding at the first and later home visits.

### Others

**ICNP** (International Classification for Nursing Practice) from the International Council of Nurses; **Clinical Care Classification**; **LOINC** also codes some nursing assessments.

## 5.8 Nurse's role

- Use the standard terms offered by the hospital system instead of free text where possible.
- Write nursing diagnoses in NANDA-I format and measure outcomes with NOC scales.
- Use decision support, but think for yourself before accepting or overriding advice.
- Share expert knowledge through teaching, protocols and case discussion.

## Remember

- Tacit knowledge is personal; explicit knowledge is written. SECI: socialisation, externalisation, combination, internalisation.
- CDSS: knowledge base + inference engine + communication; knowledge-based (rules) or machine-learning based.
- SNOMED CT = clinical terminology (concepts, descriptions, relationships; "is a" hierarchy); owned by SNOMED International; India's primary terminology.
- ICD = WHO classification; ICD-11 in effect from 1 January 2022; ICD-10-CM = US clinical modification.
- SNOMED CT to ICD-10-CM map: record once, code for statistics and billing.
- NANDA-I: 13 domains; PES format; problem-focused, risk, health-promotion, syndrome.
- NOC: outcomes with indicators on a 5-point Likert scale (University of Iowa).
- Omaha System: problem classification (4 domains), intervention scheme (4 categories), problem rating scale (knowledge, behaviour, status 1–5); community health.
