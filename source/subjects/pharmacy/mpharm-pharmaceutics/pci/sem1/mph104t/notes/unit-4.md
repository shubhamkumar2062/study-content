# Unit 4: Non-clinical drug development and global submissions

This unit is PCI Unit 3. It explains the **non-clinical (pre-clinical) studies** that must be done before and alongside human trials, how the first human dose is chosen, and how the resulting data are filed **globally**: the IND and its equivalents in other regions, then the NDA and ANDA (and their foreign counterparts). It ends with two documents named in the syllabus: the EU **Investigational Medicinal Product Dossier (IMPD)** and the **Investigator's Brochure (IB)**.

US items (IND contents, Investigator's Brochure contents) were checked against 21 CFR 312.23; EU clinical trial dates against the EMA website. Check the current texts before using them at work.

## 4.1 Drug development: where non-clinical work fits

```text
Target identification and validation
 → Hit → lead → lead optimisation → candidate selection
 → NON-CLINICAL DEVELOPMENT (pharmacology, ADME, toxicology, CMC)
 → IND / CTA → Phase I → Phase II → Phase III (non-clinical studies
   continue in parallel: chronic toxicity, reproductive, carcinogenicity)
 → NDA / MAA → approval → Phase IV
```

Only a small fraction of candidates that enter non-clinical development reach the market; development usually takes many years. Non-clinical studies aim to:

1. Identify the pharmacological effects and mechanism of action.
2. Characterise toxicity: target organs, dose dependence, reversibility.
3. Describe absorption, distribution, metabolism and excretion (ADME).
4. Choose a safe starting dose and a dose-escalation plan for humans.
5. Identify parameters to monitor clinically.
6. Support each later phase and the final marketing application.

## 4.2 Components of a non-clinical programme

### a. Pharmacology

| Study | Purpose |
| --- | --- |
| Primary pharmacodynamics | Effect on the intended target and disease models |
| Secondary pharmacodynamics | Effects on other targets (off-target) |
| **Safety pharmacology (ICH S7A)** | Effects on vital functions. **Core battery:** central nervous system, cardiovascular system and respiratory system |
| QT liability (ICH S7B with E14) | hERG channel assay and in vivo QT study to predict delayed ventricular repolarisation |
| Drug interactions (pharmacodynamic) | Where relevant |

### b. Pharmacokinetics and ADME

Absorption and bioavailability in test species; plasma protein binding; tissue distribution (including placental and milk transfer when needed); metabolism (in vitro with liver microsomes and hepatocytes from animals and humans; metabolite identification; CYP inhibition and induction, ICH M12); excretion and mass balance; **toxicokinetics (ICH S3A)** — exposure measured in toxicity studies so that animal exposure can be compared with human exposure.

### c. Toxicology

| Study | Key points |
| --- | --- |
| Single-dose (acute) toxicity | Often as dose-range finding; information on overdose |
| Repeat-dose toxicity | In two species (one rodent, one non-rodent) for small molecules; duration matched to the clinical trial duration (ICH M3(R2)); chronic studies defined by ICH S4 |
| Genotoxicity (ICH S2) | Standard battery: bacterial reverse mutation (Ames) test + an in vitro mammalian cell test and/or in vivo test (for example micronucleus) |
| Carcinogenicity (ICH S1) | For drugs used long term or with cause for concern; usually completed before marketing |
| Reproductive and developmental toxicity (ICH S5) | Fertility, embryo-foetal development, pre- and post-natal development; timing tied to inclusion of women of child-bearing potential |
| Local tolerance | At the site of administration |
| Immunotoxicity (S8), phototoxicity (S10), juvenile animal studies (S11) | When indicated |
| Biotechnology products (ICH S6) | Only **pharmacologically relevant species**; immunogenicity; often one species; standard genotoxicity and carcinogenicity usually not applicable |
| Anticancer drugs (ICH S9) | Reduced package for patients with advanced cancer |

### d. Good Laboratory Practice (GLP)

Pivotal safety studies must follow **GLP**: the quality system for planning, performing, monitoring, recording, archiving and reporting non-clinical safety studies. USA: **21 CFR Part 58**; internationally: **OECD Principles of GLP**, with mutual acceptance of data among adhering countries. In India, the **National GLP Compliance Monitoring Authority (NGCMA)** certifies test facilities. Key GLP elements: study director (single point of control), quality assurance unit, approved protocol, SOPs, characterised test item, qualified facilities and equipment, raw data, final report and archives.

### e. Animal welfare

Studies are approved by an institutional animal ethics committee and follow the **3Rs**: replacement, reduction and refinement. In India animal experiments are controlled under the Prevention of Cruelty to Animals Act, 1960 through the national committee for control and supervision of experiments on animals (check the current name and rules on its website).

## 4.3 Timing of non-clinical studies (ICH M3(R2))

ICH M3(R2) links each clinical stage to the non-clinical data needed:

| Before … | Typical non-clinical data needed |
| --- | --- |
| First-in-human (Phase I) | Safety pharmacology core battery, repeat-dose toxicity in two species of at least the planned clinical duration, in vitro genotoxicity, ADME basics, local tolerance |
| Phase II / longer trials | Longer repeat-dose studies, complete genotoxicity battery, embryo-foetal studies before women of child-bearing potential are included (with regional differences) |
| Phase III and marketing | Chronic toxicity, full reproductive package, carcinogenicity (when needed) |

Exploratory clinical trials (microdosing, "Phase 0") can start with a reduced package, as described in ICH M3(R2).

## 4.4 Choosing the first human dose (principles only)

Two approaches are used:

1. **NOAEL-based approach (FDA guidance on estimating the maximum safe starting dose):** find the no-observed-adverse-effect level in each species → convert to a **human equivalent dose (HED)** using body-surface-area scaling → pick the most appropriate species → divide by a **safety factor** (default 10, increased when there is reason for concern) → maximum recommended starting dose.
2. **MABEL (minimal anticipated biological effect level):** used for high-risk products such as immune agonists, where pharmacology rather than toxicity drives risk; based on receptor binding and in vitro activity.

Sentinel dosing (one subject first, with observation before the rest of the cohort) is used for higher-risk first-in-human trials.

## 4.5 Global submission of the IND (and its equivalents)

### a. USA — Investigational New Drug application (21 CFR 312)

Contents under **21 CFR 312.23(a)**:

1. Cover sheet (**Form FDA 1571**).
2. Table of contents.
3. Introductory statement and general investigational plan.
4. (Reserved.)
5. Investigator's Brochure.
6. Protocols.
7. Chemistry, manufacturing and control information.
8. Pharmacology and toxicology information.
9. Previous human experience with the investigational drug.
10. Additional information (for example drug dependence and abuse potential, radioactive drugs, paediatric studies).
11. Other relevant information requested by FDA.

Each investigator signs **Form FDA 1572**. The IND goes into effect **30 days after FDA receives it** unless FDA imposes a **clinical hold**. Types: investigator IND, emergency use IND, treatment IND, commercial IND. Later filings: protocol amendments, information amendments, IND safety reports, annual reports.

### b. Other regions

| Region | Clinical trial application | Notes |
| --- | --- | --- |
| European Union | **Clinical trial application** under **Regulation (EU) No 536/2014**, submitted once through **CTIS** for all chosen member states | Regulation applied from 31 January 2022; CTIS mandatory for new applications from 31 January 2023; transition of older trials ended 31 January 2025. Part I (scientific, coordinated by a reporting member state) and Part II (national and ethical aspects) assessment |
| UK | Combined review by MHRA and research ethics committee | Clinical trials regulations updated recently; check MHRA |
| Japan | Clinical trial notification to PMDA | Consultations with PMDA before filing |
| Canada | Clinical Trial Application (CTA) to Health Canada | Default review period set in the regulations |
| Australia | CTN (notification) or CTA (approval) scheme with the TGA | Most trials use CTN with ethics committee approval |
| India | Application in **Form CT-04** to the Central Licensing Authority; permission in **Form CT-06** | Decision within 90 working days; 30 working days for drugs discovered and developed in India; ethics committee approval and CTRI registration also needed |

### c. Strategy for global development

- Run **multi-regional clinical trials (ICH E17)** so one programme supports approval in many regions; consider ethnic factors (ICH E5).
- Seek scientific advice early (FDA meetings, EMA scientific advice, PMDA consultations, CDSCO pre-submission meetings).
- Keep one core data package; adapt Module 1 and local requirements.
- Plan paediatric development early (US Pediatric Study Plan; EU Paediatric Investigation Plan).

## 4.6 Global submission of the NDA and ANDA

### a. Marketing applications compared

| Region | New drug | Generic | Granted document |
| --- | --- | --- | --- |
| USA | NDA (505(b)(1)/(b)(2)); BLA | ANDA (505(j)); biosimilar 351(k) | Approval letter / licence |
| EU | Marketing authorisation application (MAA): centralised, decentralised, mutual recognition, national | Generic MAA (Article 10(1) of Directive 2001/83/EC); hybrid; biosimilar | Marketing authorisation |
| UK | MAA to MHRA (national or reliance route) | Generic MAA | Marketing authorisation |
| Japan | New drug application to MHLW/PMDA | Generic application | MHLW approval |
| Canada | New Drug Submission (NDS) | Abbreviated NDS | Notice of Compliance + DIN |
| Australia | Registration of new chemical entity | Generic registration | ARTG entry (AUST R) |
| India | CT-18 (import) / CT-21 (manufacture) to CLA | Application to CLA while still a "new drug"; afterwards State licence | Permission from CLA; licence |

### b. Typical sequence for a global NDA

```text
Core CTD (Modules 2–5) prepared once
 → USA: NDA via electronic gateway (eCTD) + PDUFA fee
 → EU: MAA via EMA (centralised) with EU Module 1, RMP, PIP compliance
 → Japan, Canada, Australia, Switzerland, others: regional Module 1
 → ROW: after a first approval, using COPP and reliance routes
 → Answer questions (FDA information requests, CHMP list of questions
   at day 120 and outstanding issues at day 180 in the EU)
 → Inspections → approvals → launch sequence
```

### c. Global ANDA / generic submissions

- Reference product differs by region (US RLD, EU reference medicinal product, national reference elsewhere); a BE study against one region's reference may not be accepted elsewhere unless allowed.
- Stability must cover the climatic zones of target markets.
- Patents and data/market protection differ: in the EU, generics follow the "8 + 2 (+1)" data and market protection rule; check current EU legislation, which was under revision.
- Labelling must follow each region's reference label.

## 4.7 Investigational Medicinal Product Dossier (IMPD)

**Definition:** the IMPD is the EU document that gives the **quality, manufacture and control** information on the investigational medicinal product (IMP), together with non-clinical and clinical data summaries where these are not in the Investigator's Brochure. It is submitted with a clinical trial application in the EU (the US IND gives similar information in its CMC and pharm/tox sections).

### a. Parts of an IMPD

| Part | Content |
| --- | --- |
| IMPD-Q (quality) | Drug substance: general information, manufacture, characterisation, control, reference standards, container closure, stability. Drug product: description and composition, pharmaceutical development, manufacture, control of excipients, control of product, container closure, stability. Placebo and comparator information |
| IMPD-S and E (safety and efficacy) | Summaries of non-clinical pharmacology, PK and toxicology, and of previous clinical data, with an overall benefit-risk assessment — may be replaced by cross-reference to the IB |

The quality part follows the CTD Module 3 structure, but the depth is **phase-appropriate**: early-phase IMPDs give provisional specifications and limited stability; later phases add more validation and data.

### b. Simplified IMPD

A shorter IMPD is allowed when the IMP is already authorised (in the EU or an ICH country) and used within or near its authorised conditions, or when data were submitted earlier by the same sponsor. Typically only the parts that have changed (for example re-packaging, blinding of a comparator) need full data.

### c. Related requirements

- IMPs are made under GMP for investigational products and released by a Qualified Person.
- Labelling of IMPs follows the clinical trials rules (trial reference, "for clinical trial use only", storage, sponsor).
- The IMPD is updated as the product and process change; substantial changes are submitted as modifications.

## 4.8 Investigator's Brochure (IB)

**Definition (ICH E6):** a compilation of the clinical and non-clinical data on the investigational product(s) that are relevant to its study in human subjects. Its purpose is to give investigators the information they need to understand the rationale for the protocol and to manage subjects safely: dose, frequency, administration and safety monitoring.

### a. Who writes and maintains it

The **sponsor** prepares the IB, keeps it up to date (reviewed at least once a year, and revised whenever important new information appears), and gives it to investigators and ethics committees. For a marketed product used in its approved way, the approved product information may replace the IB.

### b. Contents (ICH E6 outline)

1. Title page and confidentiality statement.
2. Table of contents.
3. **Summary** (physical, chemical, pharmaceutical, pharmacological, toxicological, PK, metabolic and clinical information).
4. **Introduction**: name, active ingredients, class, rationale, anticipated indications.
5. **Physical, chemical and pharmaceutical properties and formulation**, including storage and handling.
6. **Non-clinical studies**: pharmacology, PK and metabolism in animals, toxicology — with tables of findings and their relevance to humans.
7. **Effects in humans**: PK and metabolism, safety and efficacy, marketing experience.
8. **Summary of data and guidance for the investigator**: overall interpretation, possible risks and adverse reactions, precautions, special monitoring, and the **reference safety information (RSI)** used to decide whether a serious reaction is "expected".

The US rules list the same core: description of the drug substance and formulation; pharmacological and toxicological effects in animals and, if known, humans; pharmacokinetics and biological disposition; safety and effectiveness information from prior human studies; and anticipated risks and side effects with precautions or special monitoring (21 CFR 312.23(a)(5)).

### c. IB vs IMPD vs protocol

| Point | Investigator's Brochure | IMPD | Protocol |
| --- | --- | --- | --- |
| Audience | Investigators, ethics committees | Regulator (EU) | Everyone running the trial |
| Focus | Clinical and non-clinical data, risks, guidance | Quality of the IMP (+ summaries) | How this trial is run |
| Scope | The product (across trials) | The product as made for trials | One trial |
| Updated | At least yearly | When product/process changes | By amendment |

## 4.9 India: non-clinical and investigational requirements in brief

- The **NDCT Rules, 2019** set out the non-clinical data required for clinical trials and new drug applications in their schedules (pharmacology, toxicology, toxicokinetics, genotoxicity, reproductive and carcinogenicity data as appropriate).
- A clinical trial application includes the IB, protocol, informed consent documents, chemistry and manufacturing data, non-clinical data and, for global trials, data from other countries.
- Test licences permit manufacture or import of small quantities of a new drug for examination, testing or clinical trials.
- Applications go through the SUGAM portal; the Subject Expert Committee advises CDSCO.

## Remember

- Non-clinical aims: mechanism, toxicity profile, ADME, safe starting dose, clinical monitoring.
- Safety pharmacology core battery (S7A): CNS, cardiovascular, respiratory; QT: S7B + E14.
- Toxicology: single and repeat dose (two species), genotoxicity battery (S2), carcinogenicity (S1), reproductive (S5), biotech (S6, relevant species), anticancer (S9). Timing: ICH M3(R2).
- GLP: 21 CFR 58; OECD; India NGCMA; study director + QAU.
- First human dose: NOAEL → HED → safety factor; MABEL for high-risk biologics.
- IND contents 312.23(a)(1)–(11); Forms 1571 and 1572; 30-day rule; clinical hold.
- EU CTR 536/2014: applied 31 Jan 2022; CTIS mandatory for new trials from 31 Jan 2023; transition ended 31 Jan 2025; Part I / Part II.
- India: CT-04 → CT-06; 90/30 working days; CTRI.
- Global NDA: core CTD + regional Module 1; NDA, MAA, NDS, J-NDA; generics: ANDA, generic MAA, ANDS.
- IMPD: EU; quality (S + P) + summaries; phase-appropriate; simplified IMPD for authorised products.
- IB: sponsor's compilation for investigators; reviewed at least yearly; contains reference safety information.
