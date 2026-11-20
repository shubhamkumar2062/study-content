# Unit 5: Clinical trials, ethics committees, informed consent, HIPAA and pharmacovigilance

This unit is PCI Unit 4. It covers how a **clinical trial protocol** is developed, how an **institutional review board (IRB) / independent ethics committee (IEC)** is formed and works, the **informed consent** process, the US **HIPAA** privacy requirements that affect clinical research, and **pharmacovigilance and safety monitoring** during trials.

Indian rules quoted here (ethics committee composition, safety reporting times, audio-video consent) come from the New Drugs and Clinical Trials (NDCT) Rules, 2019 and match the B.Pharm notes (BP702T, BP804ET). US rules come from 21 CFR Parts 50, 56 and 312 and 45 CFR Parts 160 and 164. Always check the current text before applying them.

## 5.1 Clinical trials: definitions, phases and the governing framework

A **clinical trial** is a systematic study of a new drug (or other intervention) in human subjects to generate data on its clinical, pharmacological (including pharmacokinetic and pharmacodynamic) or adverse effects, with the aim of establishing its safety and efficacy.

| Phase | Purpose | Typical subjects |
| --- | --- | --- |
| Phase 0 / exploratory | Microdose PK, target engagement | Very few, healthy volunteers or patients |
| Phase I | Safety, tolerability, PK, PD; dose escalation | Healthy volunteers (patients for cytotoxic drugs) |
| Phase II | Proof of concept, dose finding, short-term safety | Patients, limited number |
| Phase III | Confirm efficacy and safety in a larger, more varied population; basis for approval | Large patient numbers, often multicentre and multinational |
| Phase IV | After approval: long-term safety, new populations, comparative effectiveness | Patients in practice |

**Framework:** Declaration of Helsinki (World Medical Association); **ICH E6 Good Clinical Practice** (R3 adopted in 2025; Annex 2 added later); ICH E8(R1) general considerations (quality by design in trials); India — NDCT Rules 2019 and the ICMR National Ethical Guidelines for Biomedical and Health Research; USA — 21 CFR 50, 56, 312, 812 and 45 CFR 46 (Common Rule) for federally funded research; EU — Clinical Trials Regulation (EU) No 536/2014.

### Principles of GCP (summarised)

1. Rights, safety and well-being of participants come first and prevail over the interests of science and society.
2. Informed consent is freely given and documented.
3. Independent ethics committee review.
4. Scientifically sound, clearly described trial design.
5. Qualified investigators and staff.
6. Quality built into design (identify factors critical to quality; proportionate, risk-based approach).
7. Reliable, accurate, traceable data; confidentiality protected.
8. Investigational products made under GMP and used per protocol.
9. Roles and responsibilities clear; sponsor keeps oversight even when tasks are delegated.

## 5.2 Developing clinical trial protocols

The **protocol** describes the objectives, design, methodology, statistical considerations and organisation of a trial. It must be approved by the regulator and the ethics committee before the trial starts, and changes are made only by approved **amendments**.

### a. Steps in protocol development

```text
Clinical question (from non-clinical data, earlier phases, unmet need)
 → Target product profile and regulatory advice (FDA/EMA/CDSCO meetings)
 → Literature review; feasibility (patients available, sites, standard of care)
 → Identify critical-to-quality factors and risks (ICH E8(R1), E6(R3))
 → Choose design, population, endpoints, comparator, sample size
 → Draft protocol + synopsis (clinicians, statisticians, PK, safety,
   regulatory, data management, QA, patient input where possible)
 → Internal review → CRF design → statistical analysis plan
 → Submission to regulator + ethics committee → approved version
 → Registration in a public registry (CTRI in India; ClinicalTrials.gov;
   EU CTIS) → amendments during the trial as needed
```

### b. Contents of a protocol

| Section | Includes |
| --- | --- |
| General information | Title, protocol number, version and date, sponsor, investigators, laboratories |
| Background and rationale | Product description, non-clinical and clinical findings, known and potential risks and benefits, justification of dose and route, population, references |
| Objectives and endpoints | Primary and secondary objectives; primary, secondary and exploratory endpoints; the estimand (what exactly is being estimated, ICH E9(R1)) |
| Design | Type (parallel, crossover, factorial, adaptive), control (placebo, active, historical), **randomisation**, **blinding**, treatment duration, stopping rules, accountability of IP, code-break procedure |
| Subjects | Inclusion, exclusion and withdrawal criteria; recruitment and follow-up |
| Treatment | IP and comparator, dosing schedule, permitted and prohibited concomitant medicines, compliance |
| Assessments | Efficacy measures, safety measures, schedule of assessments (visit table) |
| Safety | Definitions of AE/SAE, recording, causality, reporting timelines, follow-up |
| Statistics | Sample size and power, analysis sets (ITT, per-protocol, safety), methods, multiplicity, interim analyses, missing data |
| Data and quality | Source documents, data management, monitoring plan, audits |
| Ethics | Ethics committee approval, informed consent process, compensation and insurance |
| Administrative | Record retention, finance, publication policy, protocol amendments |

### c. Common design choices

- **Randomisation:** simple, block, stratified — removes selection bias.
- **Blinding:** open, single-blind, double-blind, double-dummy — removes assessment bias.
- **Control:** placebo (ethically acceptable only where no proven therapy is withheld to the patient's harm), active comparator, add-on design.
- **Superiority, non-inferiority, equivalence** hypotheses — each with its own margin and analysis.
- **Adaptive designs:** pre-planned changes (dose arms, sample size) based on interim data without undermining validity.

## 5.3 Institutional Review Board / Independent Ethics Committee: formation and working

An ethics committee is an **independent body** of medical, scientific and non-scientific members whose job is to protect the rights, safety and well-being of trial participants. In the USA it is the **IRB**; elsewhere the **IEC** or simply **ethics committee (EC)**.

### a. Formation (constitution)

| Requirement | India (NDCT Rules 2019, rule 7) | USA (21 CFR 56.107) |
| --- | --- | --- |
| Minimum members | **7** | **5** |
| Composition | Medical, non-medical, scientific and non-scientific members, including at least one lay person, one woman, one legal expert, and one independent member from a related field (such as a social scientist, voluntary organisation representative, ethicist or theologian) | Varied backgrounds; at least one scientist, one non-scientist, one member not affiliated with the institution; not all of one sex or one profession |
| Independence | At least 50% of members not affiliated with the institute; chairperson not affiliated; member secretary affiliated | Members with a conflict of interest do not take part in that review |
| Registration | Registered with the Central Licensing Authority (application Form CT-01, registration Form CT-02) | IRBs register with HHS/FDA |
| Training | As specified by the CLA | Institution's responsibility |

### b. Working procedures

```text
Written SOPs (membership, quorum, meetings, review types, records)
 → Receive submission: protocol, IB, ICF and information sheet in local
   languages, CRFs, recruitment materials, investigator CVs and site
   details, insurance/compensation, regulatory status
 → Initial review in a quorate meeting (members with conflicts withdraw)
 → Decision: approve / approve with modifications / disapprove /
   suspend or terminate an earlier approval — communicated in writing
 → Continuing review (at least yearly in most systems): progress
   reports, amendments, deviations, new safety information
 → Safety review: SAEs, deaths, SUSARs; in India, opinion on
   compensation for trial-related injury or death
 → Site monitoring visits where needed
 → Final report review; archive records for the period set by the rules
```

**Expedited review** may be used for minor amendments or minimal-risk research, as the committee's SOPs allow. Committees must keep minutes, membership lists, SOPs, correspondence and decisions.

### c. Points the committee considers

Scientific validity (poor science is unethical), risk–benefit balance, fair selection of subjects and protection of vulnerable groups, adequacy and language of the consent documents, confidentiality, payment that is not coercive, compensation for injury, qualifications of the investigator and adequacy of the site.

## 5.4 Informed consent process and procedures

**Informed consent** is the process by which a subject voluntarily confirms willingness to take part in a trial after being informed of all aspects relevant to that decision. It is documented on a written, signed and dated form, but it is a **continuing process**, not a single signature.

### a. Elements of information (ICH E6; 21 CFR 50.25; Third Schedule of the NDCT Rules)

1. The trial involves research; purpose, duration and procedures; which procedures are experimental.
2. Trial treatments and the probability of random assignment.
3. Foreseeable risks and discomforts (including to an embryo or foetus where relevant).
4. Expected benefits, or that there may be none.
5. Alternative treatments.
6. Confidentiality of records and who may access them (monitors, auditors, ethics committee, regulators).
7. Compensation and treatment for trial-related injury.
8. Contacts for questions about the trial, subjects' rights and injury.
9. Participation is **voluntary**; refusal or withdrawal at any time without penalty or loss of benefits.
10. Circumstances in which the investigator may end participation; expected number of subjects; payments and expenses.

### b. Procedure

```text
Ethics-committee-approved ICF + information sheet in a language the
subject understands
 → Explained by the investigator or a trained delegate, in plain words
 → Time to read, think, ask questions and consult family
 → No coercion or undue influence
 → Signed and dated by subject (or legally acceptable representative)
   and by the person conducting the discussion; impartial witness if
   the subject cannot read
 → Copy given to the subject
 → Re-consent when significant new information arises or the
   protocol changes in a way that affects the subject
```

### c. Special situations

- **Children:** permission of parent or legally acceptable representative plus the child's **assent** when able to understand.
- **Incapable or unconscious adults:** consent of a legally acceptable representative; emergency research only as rules and the committee allow.
- **Illiterate subjects:** impartial witness present throughout.
- **India:** **audio-video recording** of the consent process is required for vulnerable subjects in trials of a new chemical entity or new molecular entity; for anti-HIV and anti-leprosy drug trials only an audio recording is kept (NDCT Rules 2019).
- **Re-use of samples and data:** consent must cover storage and future use, or fresh consent/committee approval is needed.

## 5.5 HIPAA and its requirements for the clinical study process

The **Health Insurance Portability and Accountability Act (HIPAA), 1996** is a US law. Its **Privacy Rule** (45 CFR Part 160 and Part 164, Subparts A and E) protects individually identifiable health information. Indian students study it because global trials that include US sites must comply with it; India's own counterpart is the Digital Personal Data Protection Act, 2023, alongside the confidentiality duties in the NDCT Rules and ICMR guidelines.

### a. Key terms

| Term | Meaning |
| --- | --- |
| Covered entity | Health plans, health-care clearinghouses and health-care providers that transmit health information electronically (hospitals and clinics running trials usually are) |
| Protected health information (PHI) | Individually identifiable health information held or transmitted by a covered entity |
| Authorization | The individual's written permission for a specific use or disclosure of PHI for research |
| Privacy board | A board (alternative to the IRB) that can approve waivers of authorization |

A sponsor is not usually a covered entity itself, but it receives PHI from covered-entity sites, so HIPAA shapes what sites can send.

### b. Ways a researcher may use or disclose PHI

1. **With the subject's authorization** — usually a HIPAA authorization signed with (or within) the informed consent form, stating what PHI is used, by whom, for what purpose, an expiry, and the right to revoke.
2. **Waiver or alteration of authorization** approved by an **IRB or privacy board**: the research must pose no more than minimal risk to privacy (with a plan to protect identifiers, destroy them when possible, and not re-use them), and must be impracticable without the waiver and without the PHI.
3. **Reviews preparatory to research** (for example checking whether enough eligible patients exist): the researcher gives written assurance that PHI is used only for this, will not leave the covered entity, and is necessary.
4. **Research on decedents' information**, with similar assurances and, on request, proof of death.
5. **De-identified data** — not PHI at all. Two methods: **Safe Harbor** (remove **18 identifiers** — for example names, small geographic units, all date elements except year, phone and fax numbers, e-mail, social security, medical record and account numbers, device identifiers, URLs, IP addresses, biometric identifiers, full-face photographs and any other unique code — with no actual knowledge that the rest could identify the person) or **Expert Determination** (a qualified statistician documents that the risk of re-identification is very small).
6. **Limited data set** (direct identifiers removed but, for example, town, state, zip code and dates kept) with a **data use agreement** that limits use and forbids re-identification.

### c. Impact on the clinical study process

- Consent documents include HIPAA authorization language; IRBs check it.
- Monitors' access to source records is covered by the authorization.
- Subjects are coded (subject ID), and CRFs carry no direct identifiers.
- Security safeguards for electronic data (HIPAA Security Rule); breach notification duties.
- **Accounting of disclosures** for some research disclosures made without authorization.
- Subjects keep a right of access to their records (which can be suspended during a blinded trial if they agreed to this).

## 5.6 Pharmacovigilance: safety monitoring in clinical trials

**Pharmacovigilance (WHO):** the science and activities relating to the detection, assessment, understanding and prevention of adverse effects or any other drug-related problem. In trials, it protects subjects now and builds the safety profile used at approval.

### a. Definitions (ICH E2A)

| Term | Meaning |
| --- | --- |
| Adverse event (AE) | Any untoward medical occurrence in a subject given a pharmaceutical product, not necessarily caused by it |
| Adverse drug reaction (ADR) | Noxious and unintended response where a causal relationship is at least a reasonable possibility |
| Serious | Results in death, is life-threatening, requires or prolongs hospitalisation, causes persistent or significant disability/incapacity, or a congenital anomaly/birth defect; or other medically important event |
| Unexpected | Nature or severity not consistent with the reference safety information (IB or label) |
| SUSAR | Suspected unexpected serious adverse reaction |

Severity (mild, moderate, severe) describes intensity; **seriousness** is the regulatory criterion for reporting.

### b. Safety monitoring flow

```text
Event detected (subject report, visit, lab result)
 → Recorded in source and CRF: onset, severity, seriousness, action, outcome
 → Investigator assesses seriousness and causality (WHO-UMC or similar)
 → Serious → reported quickly to sponsor (and in India also to CLA and EC)
 → Sponsor: medical review, expectedness against RSI, coding (MedDRA),
   case report in E2B format → expedited reports to regulators,
   investigators and ethics committees
 → Aggregate review: safety review team, DSMB, signal detection
 → Actions: IB update, protocol amendment, consent update,
   dose change, enrolment pause, trial stop
 → Periodic report: DSUR (ICH E2F), yearly
```

### c. Reporting timelines

| System | Requirement |
| --- | --- |
| ICH E2A | Fatal or life-threatening SUSARs: as soon as possible, within **7 calendar days** of first knowledge (follow-up within 8 more days); other SUSARs within **15 calendar days** |
| USA (21 CFR 312.32) | IND safety reports within 15 calendar days; unexpected fatal or life-threatening suspected adverse reactions within 7 calendar days |
| India (NDCT Rules 2019) | Investigator reports every **SAE** to the CLA, sponsor and ethics committee **within 24 hours**; the analysed report goes to the CLA, ethics committee chairperson and head of institution **within 14 days**; reasons needed for delays. Deaths are examined by an independent expert committee, which also advises on compensation |

### d. Roles in safety monitoring

| Role | Safety duties |
| --- | --- |
| Investigator | Detect, record, treat and report AEs/SAEs; follow up to resolution; inform EC |
| Sponsor | Continuous safety evaluation; expedited and periodic reporting; update IB; set up DSMB when needed; provide compensation (India) |
| Monitor (CRA) | Checks AEs in source are captured in CRFs and reported on time |
| Ethics committee | Reviews SAEs and new safety data; can suspend approval |
| DSMB / DMC | Independent experts reviewing unblinded accumulating data; recommends continue, modify or stop |
| Regulator | Reviews reports, inspects, can impose clinical hold or suspend |

### e. Causality assessment

Common methods: **WHO-UMC system** (certain, probable/likely, possible, unlikely, conditional/unclassified, unassessable/unclassifiable) and the **Naranjo algorithm** (questionnaire scoring: definite, probable, possible, doubtful). Factors: time relationship, dechallenge and rechallenge, alternative causes, known pharmacology, plausibility.

### f. From trials to the market

Safety data collected in development feed the **risk management plan (RMP)** in the EU and **REMS** in the USA, and in India the post-approval PSURs (six-monthly for two years, then yearly for two years). Spontaneous reporting continues through **PvPI** (Indian Pharmacopoeia Commission, Ghaziabad), MedWatch/FAERS (USA) and the Yellow Card scheme (UK). The **DSUR** (ICH E2F) is the yearly development safety report; after approval the **PBRER** (ICH E2C(R2)) takes over in many regions.

## 5.7 Compensation, registration and quality in Indian trials (quick facts)

- Sponsor must provide **medical management** and **compensation** for trial-related injury or death; the amount follows the formula in the NDCT Rules.
- Trials must be registered in the **Clinical Trials Registry – India (CTRI)** before the first subject is enrolled.
- CDSCO inspects sites, sponsors and CROs; findings can lead to rejection of data, suspension or debarment.
- Records are kept for the period specified in the rules.

## Remember

- Phases 0–IV; GCP (ICH E6, R3 2025): participant first, consent, EC review, sound design, quality by design, reliable data.
- Protocol: background, objectives/endpoints (estimand), design (randomisation, blinding, control), subjects, treatment, assessments, safety, statistics, data/quality, ethics, administration.
- EC India: ≥7 members (lay person, woman, legal expert, independent member), ≥50% non-affiliated, non-affiliated chair; CT-01 → CT-02. US IRB: ≥5 (scientist, non-scientist, non-affiliated).
- EC decisions: approve, approve with modifications, disapprove, suspend/terminate; continuing review; SAE review.
- Informed consent: process; 10 core elements; LAR, assent, impartial witness; India audio-video for vulnerable subjects in NCE/NME trials.
- HIPAA (45 CFR 160, 164): PHI, covered entity; authorization; IRB/privacy board waiver; preparatory to research; decedents; de-identification (Safe Harbor 18 identifiers or expert determination); limited data set + data use agreement.
- PV: AE, ADR, serious, unexpected, SUSAR. ICH 7/15 days; US 312.32; India SAE 24 hours + 14 days. DSUR yearly; DSMB; WHO-UMC and Naranjo causality.
- India: compensation formula, CTRI before first enrolment, PSURs 6-monthly × 2 y then yearly × 2 y, PvPI at IPC Ghaziabad.
