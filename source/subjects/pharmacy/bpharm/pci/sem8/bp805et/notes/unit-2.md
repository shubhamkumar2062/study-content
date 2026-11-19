# Unit 2: Drug and disease classification, dictionaries and setting up a pharmacovigilance programme

Pharmacovigilance works only if a report written in Ghaziabad means exactly the same as one written in Uppsala or Tokyo. That needs standard ways of naming drugs, diseases and reactions. This unit covers the international classifications of drugs (ATC, DDD, INN) and diseases (ICD), the dictionaries used to code adverse reactions and medicines (WHO-ART, MedDRA, SMQs, WHODrug, EVMPD), where to look for drug safety information, and how a pharmacovigilance programme is set up in a hospital, in a company and in a country.

## 2.1 Why classification and coding matter

| Problem without coding | Result |
| --- | --- |
| One drug sold under hundreds of brand names | Reports on the same drug are scattered |
| Same reaction written as "rash", "skin eruption", "exanthema" | Cases cannot be counted together |
| Different languages and spellings | International data cannot be pooled |
| Free text in databases | Computer searches and signal detection fail |

**Coding** turns free text into standard terms and codes so that cases can be stored, searched, counted, compared and exchanged electronically.

## 2.2 Anatomical Therapeutic Chemical (ATC) classification

The **ATC system** classifies active substances by the organ or system on which they act and by their therapeutic, pharmacological and chemical properties. It is maintained by the **WHO Collaborating Centre for Drug Statistics Methodology, Oslo, Norway**, and is recommended by WHO for drug utilisation research.

**Five levels**

| Level | What it shows | Example: metformin A10BA02 |
| --- | --- | --- |
| 1st | Anatomical main group (one letter; 14 groups) | A — Alimentary tract and metabolism |
| 2nd | Therapeutic subgroup (two digits) | A10 — Drugs used in diabetes |
| 3rd | Pharmacological subgroup (letter) | A10B — Blood glucose lowering drugs, excluding insulins |
| 4th | Chemical subgroup (letter) | A10BA — Biguanides |
| 5th | Chemical substance (two digits) | A10BA02 — Metformin |

**The 14 anatomical main groups:** A alimentary tract and metabolism; B blood and blood-forming organs; C cardiovascular system; D dermatologicals; G genito-urinary system and sex hormones; H systemic hormonal preparations (excluding sex hormones and insulins); J anti-infectives for systemic use; L antineoplastic and immunomodulating agents; M musculo-skeletal system; N nervous system; P antiparasitic products, insecticides and repellents; R respiratory system; S sensory organs; V various.

Another example: paracetamol N02BE01 (N nervous system → N02 analgesics → N02B other analgesics and antipyretics → N02BE anilides → paracetamol).

**Principles:** a substance usually gets one ATC code per main indication and route; combinations get separate codes; a code is not a recommendation for use and does not imply therapeutic equivalence.

**Uses in pharmacovigilance:** grouping suspect drugs by class in VigiBase, finding class effects, drug utilisation studies, comparing consumption between countries.

## 2.3 Defined Daily Dose (DDD)

**DDD** is the **assumed average maintenance dose per day for a drug used for its main indication in adults**. It is a **technical unit of measurement**, set by the WHO Oslo centre together with the ATC code. It is **not** a recommended dose and may differ from the dose actually prescribed.

**Common measures**

- **DDDs per 1,000 inhabitants per day** — population consumption:

  ```text
  DDD/1000 inhabitants/day = total quantity used (mg) × 1000
                             ─────────────────────────────────────
                             DDD (mg) × number of days × inhabitants
  ```

- **DDDs per 100 bed-days** — hospital use.
- **DDDs per inhabitant per year** — for drugs used in short courses (for example anti-infectives).

**Uses:** comparing drug use between hospitals, regions and countries over time independent of price and pack size; estimating exposure (the denominator) for ADR rates; studying antibiotic consumption and resistance.

**Limitations:** does not reflect actual prescribed doses (children, renal disease), does not show indication or adherence, combination products are difficult.

## 2.4 International Classification of Diseases (ICD)

The **ICD**, published by WHO, is the global standard for recording diseases, injuries and causes of death.

| Feature | ICD-10 | ICD-11 |
| --- | --- | --- |
| Status | Endorsed in 1990; widely used, including in Indian hospitals | Adopted by the World Health Assembly in 2019; in effect from 1 January 2022 |
| Code format | Letter + digits, e.g. E11 (type 2 diabetes mellitus), I10 (essential hypertension), J45 (asthma) | Alphanumeric codes such as 5A11; electronic, linked to a foundation layer |
| Structure | 22 chapters by body system or cause (the last for special purposes) | More chapters, including new ones such as traditional medicine conditions |

**Uses in PV:** coding the indication and medical history, separating disease symptoms from ADRs, mortality and morbidity statistics, linking hospital records in pharmacoepidemiological studies. ICD also contains codes for adverse effects of drugs in therapeutic use and for poisoning.

## 2.5 International Nonproprietary Names (INN)

An **INN** is a unique, globally recognised generic name for a pharmaceutical substance, selected by WHO through the INN programme (started in 1950). INNs are public property and cannot be registered as trademarks.

**Features**

- Distinctive in sound and spelling, not too long, not confusable with existing names.
- Related substances share a **common stem**, so the name shows the class.

| Stem | Class | Example |
| --- | --- | --- |
| -olol | Beta-blockers | propranolol, atenolol |
| -pril | ACE inhibitors | enalapril, ramipril |
| -sartan | Angiotensin II receptor blockers | losartan, telmisartan |
| -dipine | Dihydropyridine calcium channel blockers | amlodipine, nifedipine |
| -statin | HMG-CoA reductase inhibitors | atorvastatin, rosuvastatin |
| -prazole | Proton pump inhibitors | omeprazole, pantoprazole |
| -oxacin | Quinolone antibacterials | ciprofloxacin, levofloxacin |
| -vir | Antivirals | acyclovir, oseltamivir |
| -mab | Monoclonal antibodies | rituximab, trastuzumab |
| -tinib | Tyrosine kinase inhibitors | imatinib, gefitinib |

**Importance for PV:** reports on many brands of one substance can be combined; prescribing and labelling by generic name reduces medication errors; avoids confusion when drugs move between countries.

## 2.6 WHO adverse reaction terminology (WHO-ART)

**WHO-ART** was developed by WHO–UMC to code adverse reaction terms in the WHO programme for several decades.

- Hierarchical: **System Organ Class → High Level Term → Preferred Term → Included Term**.
- Simple, available in several languages, linked to ICD.
- Limitations: relatively small and coarse; not detailed enough for modern regulatory needs.
- It has now largely been **replaced by MedDRA**, which is the standard for ICSRs; WHO–UMC supports MedDRA in VigiBase and VigiFlow.

## 2.7 MedDRA — Medical Dictionary for Regulatory Activities

**MedDRA** is a clinically validated, international medical terminology developed under **ICH** for regulatory communication about human medicines. It is maintained by the **MSSO (Maintenance and Support Services Organization)**, with new versions released twice a year (March and September). It is used for adverse events, medical history, indications, investigations and product-quality issues, at every stage from clinical trials to post-marketing.

**Five-level hierarchy**

```text
SOC   System Organ Class (27)            e.g. Gastrointestinal disorders
 └ HLGT  High Level Group Term            e.g. Gastrointestinal signs and symptoms
    └ HLT   High Level Term               e.g. Nausea and vomiting symptoms
       └ PT    Preferred Term             e.g. Vomiting
          └ LLT   Lowest Level Term       e.g. Throwing up, Vomiting
```

- **LLT** — the level used for coding; includes synonyms, lexical variants and common words a reporter may use ("throwing up").
- **PT** — a single distinct medical concept; the level used for counting and analysis.
- **Multiaxiality** — a PT may belong to more than one SOC (for example, "pneumonia" relates to infections and to respiratory disorders), but each PT has **one primary SOC** for counting so that cases are not double counted.

**Coding rules (good practice):** code what the reporter says, do not add a diagnosis that was not made; if a diagnosis is given, code the diagnosis rather than every symptom; select the LLT closest to the verbatim term; do not code "unknown" or lazy terms when details exist; record the MedDRA version used.

**Standardised MedDRA Queries (SMQs)** — pre-defined groupings of MedDRA terms (usually PTs) that relate to one medical condition, for example *Rhabdomyolysis/myopathy*, *Severe cutaneous adverse reactions*, *Drug-related hepatic disorders*, *Torsade de pointes/QT prolongation*.

- **Narrow scope** — terms highly likely to represent the condition (specific).
- **Broad scope** — narrow terms plus less specific terms (sensitive).
- Some are **hierarchical** (sub-SMQs) and some **algorithmic** (combinations of terms).
- Use: retrieving all relevant cases from a safety database for signal evaluation and aggregate reports.

## 2.8 WHO Drug Dictionary (WHODrug)

**WHODrug Global** (formerly the WHO Drug Dictionary and WHO Drug Dictionary Enhanced) is the international dictionary of medicinal product information maintained by **WHO–UMC**.

- Contains conventional medicines, biologicals and herbal products from many countries, with trade names, active ingredients, manufacturers and countries.
- Each record has a **drug code** that links trade names to the same active ingredient(s), plus **ATC codes**.
- Herbal products are covered by **WHODrug Herbal**, which uses a herbal ATC (HATC) classification.
- Used for coding **concomitant and suspect medications** in clinical trial databases and ICSRs, and for analysing data by ingredient or class.

## 2.9 EudraVigilance Medicinal Product Dictionary (EVMPD)

**EudraVigilance** is the European Medicines Agency's system for managing ICSRs in the European Economic Area. Its **Medicinal Product Dictionary (EVMPD)**, now the **extended version (xEVMPD)**, holds information on medicines authorised in the EU and on investigational products.

- Marketing authorisation holders must submit and update data on their authorised products (product name, substances, strength, pharmaceutical form, route, MAH, QPPV details).
- Supports accurate identification of products in ICSRs and signal detection.
- Is being aligned with the ISO **IDMP** (Identification of Medicinal Products) standards.

**Comparison of dictionaries**

| Dictionary | Owner / maintainer | Codes what |
| --- | --- | --- |
| WHO-ART | WHO–UMC | Adverse reactions (older) |
| MedDRA | ICH; MSSO | Adverse events, indications, history, investigations |
| WHODrug | WHO–UMC | Medicinal products and ingredients |
| xEVMPD | EMA | EU-authorised and investigational products |
| ICD | WHO | Diseases and causes of death |
| ATC/DDD | WHO Oslo centre | Drug classes and consumption units |

## 2.10 Information resources in pharmacovigilance

**Basic drug information resources**

- Product information: package inserts, summary of product characteristics (SmPC), prescribing information.
- Compendia and formularies: National Formulary of India, Indian Pharmacopoeia, British National Formulary, Martindale, CIMS and similar Indian indexes.
- Standard textbooks of pharmacology and therapeutics.
- Databases: Micromedex, Lexicomp, Medscape, Drugs.com; PubMed for primary literature.

**Specialised resources for ADRs**

| Resource | Use |
| --- | --- |
| Meyler's Side Effects of Drugs and Side Effects of Drugs Annual | Comprehensive reference on reported ADRs |
| Davies's Textbook of Adverse Drug Reactions | Organ-wise ADR information |
| Stockley's Drug Interactions | Interactions |
| Reactions Weekly | Abstracts of new case reports |
| WHO Pharmaceuticals Newsletter, WHO Drug Information | Regulatory safety actions worldwide |
| VigiAccess (WHO), FAERS (USA), EudraVigilance public site, Yellow Card data (UK) | Public views of spontaneous report databases |
| PvPI drug safety alerts and newsletters, CDSCO notices | Indian safety actions |
| LiverTox, LactMed | Drug-induced liver injury; drugs in breastfeeding |
| Briggs' Drugs in Pregnancy and Lactation | Pregnancy and lactation risk |

**Hierarchy of evidence:** tertiary sources (textbooks) for quick answers → secondary (indexing databases) → primary literature (case reports, studies) for new or rare reactions.

## 2.11 Establishing a pharmacovigilance programme in a hospital

**Steps**

1. **Approval and policy** — hospital management and the Pharmacy and Therapeutics Committee approve an ADR monitoring programme; ideally register as or link to a PvPI AMC.
2. **Pharmacovigilance committee** — physicians, pharmacologists, clinical pharmacists, nurses; defines scope and meets regularly.
3. **Responsible staff** — a PV coordinator (often a clinical pharmacist or pharmacologist).
4. **Tools** — PvPI reporting forms in wards, drop boxes, helpline and app information, an ADR register.
5. **Training and awareness** — CMEs, ward rounds, posters; make reporting easy and non-punitive.
6. **Detection methods** — spontaneous reporting plus active methods (ward rounds, trigger tools, review of antidote use and laboratory alerts).
7. **Assessment** — causality (WHO–UMC, Naranjo), severity (Hartwig), preventability (Schumock–Thornton).
8. **Reporting** — forward to AMC/PvPI through VigiFlow.
9. **Feedback and action** — acknowledgement to reporters, bulletins, formulary changes, allergy alert system.
10. **Evaluation** — number and quality of reports, preventable ADRs reduced.

## 2.12 Drug safety department in industry

A **marketing authorisation holder (MAH)** must run a pharmacovigilance system for its products.

**Organisation**

```text
Head of drug safety / Qualified person responsible for PV
        │
 ┌──────┼──────────────┬───────────────┬──────────────┐
Case     Aggregate      Signal          Risk           Quality,
processing reports      management      management     SOPs, audits
(ICSRs)  (PSUR/PBRER,   (detection,     (RMP,          and training
          DSUR)          evaluation)     minimisation)
```

**Case processing workflow:** case receipt (doctors, patients, literature, partners, social media, trials) → duplicate check → validity check (four minimum criteria) → triage (serious/non-serious, expected/unexpected) → data entry in a safety database → MedDRA and WHODrug coding → medical review and causality → narrative writing → quality check → submission to regulators within timelines → follow-up.

**Other functions:** literature surveillance, maintaining reference safety information, safety data exchange agreements with partners, inspection readiness, PV system master file (where required), training of all staff (including sales staff, who must pass on any ADR they hear about).

## 2.13 Contract Research Organisations (CROs)

A **CRO** is a company contracted by a sponsor to perform trial- or PV-related duties.

- PV services offered: case processing, literature screening, aggregate report writing, signal detection, medical review, call-centre intake.
- The **sponsor/MAH stays legally responsible**; duties are defined in written contracts and agreements.
- Quality is ensured by SOPs, audits, timelines (key performance indicators) and data-protection rules.
- India has a large PV outsourcing industry, which offers careers for B.Pharm graduates as drug safety associates.

## 2.14 Establishing a national pharmacovigilance programme

Basic requirements for a national system:

1. A **national PV centre** with trained staff, an official mandate and stable funding.
2. A **national reporting system** with a standard ICSR form and easy channels (paper, online, app, helpline).
3. A **national database** compatible with international standards (E2B, MedDRA) and links to the WHO programme.
4. An **expert advisory committee** for causality and signal review.
5. A **clear link with the regulator** so that findings lead to action.
6. **Regional/peripheral centres** to collect reports (like AMCs in India).
7. A **communication strategy** for feedback, alerts and public information.
8. Training and promotion of reporting among health professionals and consumers.
9. Collaboration with public health programmes (TB, HIV, malaria, immunisation).

**Phases:** plan and get government support → set up the centre and tools → pilot in a few hospitals → expand nationally → join the WHO programme → integrate with regulatory decisions.

## Remember

- ATC: 5 levels, 14 main groups; WHO Oslo centre. Metformin A10BA02.
- DDD = assumed average maintenance dose per day for the main indication in adults; a measuring unit, not a recommended dose.
- ICD-10 in use; ICD-11 effective 1 January 2022.
- INN stems: -olol, -pril, -sartan, -statin, -mab, -tinib.
- MedDRA: SOC (27) → HLGT → HLT → PT → LLT; code at LLT, analyse at PT; one primary SOC; maintained by MSSO; SMQs narrow and broad.
- WHODrug (WHO–UMC) codes medicines; xEVMPD (EMA) codes EU products; WHO-ART is older and replaced by MedDRA.
- Industry PV: case processing, aggregate reports, signals, RMP; MAH remains responsible even when a CRO does the work.
