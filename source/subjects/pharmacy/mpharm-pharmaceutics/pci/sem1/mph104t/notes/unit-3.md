# Unit 3: CMC, post-approval changes, combination products and devices, CTD/eCTD, ICH and other regulators

This unit is PCI Unit 2. It covers the **chemistry, manufacturing and controls (CMC)** part of a dossier, how products are changed after approval, how **combination products** and **medical devices** are regulated, the **CTD and eCTD** formats, how industry works with the FDA, the four families of **ICH guidelines**, and the regulators of the **EU, UK (MHRA), Australia (TGA)** and the "rest of the world" (ROW).

Figures in this unit were checked on fda.gov, ema.europa.eu, ich.org and cdsco.gov.in. Post-approval rules in the EU and UK were being revised around 2024–2025, so for real filings always read the current guideline.

## 3.1 Chemistry, Manufacturing and Controls (CMC)

**CMC** is the part of a regulatory submission that describes what the product is made of, how it is made and how its quality is controlled. In the CTD it is **Module 3 (Quality)**, summarised in the **Quality Overall Summary (Module 2.3)**. Clinical data show a drug works; CMC shows that **every batch sold is the same as the batches that were tested**.

### a. Contents of Module 3 (ICH M4Q)

| Section | Drug substance (3.2.S) | Drug product (3.2.P) |
| --- | --- | --- |
| General information | Nomenclature, structure, properties | Description and composition |
| Manufacture | Manufacturer, process description and flow chart, control of materials, critical steps and intermediates, process validation, manufacturing process development | Manufacturer, batch formula, process and controls, critical steps, process validation |
| Development | Covered under manufacturing development | **Pharmaceutical development (3.2.P.2)**: formulation and process development, overages, physicochemical and biological properties, container closure, microbiological attributes, compatibility |
| Characterisation | Proof of structure, impurities | — |
| Control | Specification, analytical procedures, validation, batch analyses, justification | Same for the finished product; control of excipients (3.2.P.4) |
| Reference standards | Yes | Yes |
| Container closure | Yes | Yes |
| Stability | Summary, post-approval protocol, data | Same |
| Appendices / regional | 3.2.A facilities and equipment, adventitious agent safety, novel excipients; 3.2.R regional information (for example executed batch records for FDA) | |

### b. Why CMC matters to regulatory affairs

1. CMC deficiencies are a frequent reason for complete response letters and delayed approvals.
2. Every later change (site, scale, supplier, specification) is judged against the approved CMC.
3. CMC links to GMP: inspectors check that the plant does what Module 3 says.
4. CMC data are built progressively: limited at Phase I (safety-related quality), fuller at Phase III, complete at NDA.

### c. Guidelines that drive CMC

ICH Q1 (stability), Q2 (validation of analytical procedures), Q3 (impurities), Q6A/Q6B (specifications), Q8 (pharmaceutical development), Q9 (quality risk management), Q10 (pharmaceutical quality system), Q11 (development and manufacture of drug substances), Q12 (product life-cycle management), Q13 (continuous manufacturing), Q14 (analytical procedure development).

## 3.2 Post-approval regulatory affairs

After approval the product has a long life: new sites, scale-up, new suppliers, specification changes, label updates, safety variations, renewals and eventually withdrawal. **Post-approval regulatory affairs** manages all of this so that the licence stays valid and every change is approved or notified correctly.

### a. Main post-approval activities

```text
Change control (internal) → regulatory assessment of each change
 → filing category decided → supplement / variation submitted
 → approval or acknowledgement → implementation → update of dossier
Parallel duties: safety reporting, periodic reports, annual reports,
labelling updates, renewals, responses to inspections, recalls,
product listing, maintenance of DMFs and certificates
```

### b. USA — changes to an approved application (21 CFR 314.70; 314.97 for ANDAs; 601.12 for biologics)

| Category | Filing | Implementation |
| --- | --- | --- |
| Major change | **Prior Approval Supplement (PAS)** | Only after FDA approval |
| Moderate change | **CBE-30** (changes being effected in 30 days) | 30 days after FDA receives it, unless FDA objects |
| Moderate change (designated) | **CBE-0** | On receipt by FDA |
| Minor change | **Annual report** | At once; reported in the next annual report |

Examples: change in qualitative formula → PAS; new container closure not affecting quality → CBE-30; strengthening a warning → CBE-0; deleting a colouring agent used only for colour → annual report. ICH **Q12** adds tools such as **established conditions** and **post-approval change management protocols** that let a firm agree the reporting category of future changes in advance.

The **annual report** (21 CFR 314.81) is submitted within 60 days of the approval anniversary and includes distribution data, labelling, CMC changes, non-clinical and clinical study updates and the status of post-marketing commitments.

### c. European Union — variations

Variations to EU marketing authorisations are governed by the Variations Regulation (Commission Regulation (EC) No 1234/2008, as amended) and its classification guideline:

| Type | Meaning | How it is handled |
| --- | --- | --- |
| Type IA | Minimal or no impact | "Do and tell": implement, then notify (some must be notified immediately — Type IA-IN) |
| Type IB | Minor, not IA or II | "Tell, wait and do": implement if no objection within the set period |
| Type II | Major impact on quality, safety or efficacy (for example new indication) | Prior assessment and approval |
| Extension | Change to active substance, strength, dosage form or route | New application procedure |

Grouping and **work-sharing** allow one assessment of the same change across several products or authorisations. The EU updated its variations framework in 2024–2025; check the current guideline.

### d. India

Changes to an approved new drug (and to licensed products) are handled under the Drugs Rules, 1945 and the NDCT Rules, 2019, with CDSCO guidance on post-approval changes classifying them as major (prior approval) or minor (notification). Check the current CDSCO guidance before filing.

## 3.3 Regulation of combination products

**Definition (21 CFR 3.2(e)):** a combination product is made of two or more regulated components (drug, device, biological product) that are:

1. physically, chemically or otherwise combined into a **single entity** (for example a drug-eluting stent, a prefilled syringe, a transdermal patch with a device element);
2. **co-packaged** in one package (for example a kit with a drug and its delivery device);
3. a **separately packaged** product intended for use only with a specific approved product, where both are needed and the labelling must change (cross-labelled);
4. a separately packaged investigational product intended only for use with another specified investigational product.

### Primary mode of action (PMOA)

- **Mode of action:** how the product achieves its therapeutic effect — as a drug, a device or a biological product.
- **PMOA (21 CFR 3.2(m)):** the single mode of action that provides the **most important therapeutic action** of the combination product.
- The FDA **Office of Combination Products (OCP)** assigns the **lead centre** (CDER, CBER or CDRH) based on the PMOA. If the PMOA is uncertain, the sponsor can file a **Request for Designation (RFD)**.

| Example | PMOA | Lead centre |
| --- | --- | --- |
| Drug-eluting coronary stent | Device (keeps vessel open) | CDRH |
| Prefilled insulin pen | Drug | CDER |
| Antibody–drug conjugate | Biological | CDER (therapeutic biologic) |

**Applications:** usually one marketing application of the lead centre's type (NDA, BLA or PMA/510(k)) with consultation by the other centres. **GMP:** 21 CFR Part 4 lets the manufacturer follow one main GMP system (drug cGMP or device quality system) plus specified extra provisions from the other.

**EU:** a medicine with an integrated device is authorised as a medicine, but the device part must meet the general safety and performance requirements of the Medical Devices Regulation (a notified body opinion is needed in many cases). **India:** drug–device combinations are regulated as drugs or as devices depending on the primary purpose; check CDSCO's classification lists.

## 3.4 Regulation of medical devices

A **medical device** is an instrument, apparatus, implant, machine, software or similar article intended for diagnosis, prevention, monitoring or treatment, which achieves its main intended action **not** by pharmacological, immunological or metabolic means.

### a. USA (CDRH)

| Class | Risk | Controls | Usual pathway |
| --- | --- | --- | --- |
| I | Low (for example bandages, examination gloves) | General controls | Most exempt; otherwise 510(k) |
| II | Moderate (for example infusion pumps, powered wheelchairs) | General + special controls | **510(k) premarket notification** (substantial equivalence to a legally marketed predicate) |
| III | High (for example implantable pacemakers, heart valves) | General controls + premarket approval | **PMA** (premarket approval with clinical evidence) |

Other routes: **De Novo** classification for novel low-to-moderate risk devices with no predicate (classified into Class I or II); **Humanitarian Device Exemption (HDE)** for devices for rare conditions; **IDE** (investigational device exemption, 21 CFR 812) for clinical studies. Quality system requirements are in 21 CFR Part 820 (now aligned with ISO 13485).

### b. European Union

Medical Devices Regulation **(EU) 2017/745 (MDR)** and In Vitro Diagnostic Regulation **(EU) 2017/746 (IVDR)**. Devices are classed **I, IIa, IIb and III** by risk. Except low-risk Class I, conformity is assessed by an independent **notified body**, after which the maker affixes the **CE mark**. Requirements include clinical evaluation, post-market surveillance, a unique device identifier (UDI) and registration in the EUDAMED database.

### c. India

The **Medical Devices Rules, 2017** (under the Drugs and Cosmetics Act) classify devices by risk into **Class A (lowest), B, C and D (highest)**.

| Licensing | Authority |
| --- | --- |
| Manufacture of Class A and B | State Licensing Authority |
| Manufacture of Class C and D | Central Licensing Authority (CDSCO) |
| Import of all classes | Central Licensing Authority |
| Non-sterile, non-measuring Class A | Exempt from licence; registration on the online portal |

CDSCO publishes class-wise lists that change over time; check the current list for a specific device.

## 3.5 CTD and eCTD

### a. Common Technical Document (ICH M4)

The CTD is the agreed **format** for organising a registration dossier. It harmonises format, not data requirements.

```text
                      /\
                     /M1\        Regional administrative information
                    /----\
                   /  M2  \      Summaries (QOS, overviews, written and
                  /--------\     tabulated summaries)
                 / M3 |M4 |M5\   Quality | Non-clinical | Clinical reports
                /-----+---+---\
```

| Module | Content |
| --- | --- |
| 1 | Regional: forms, cover letter, fees, labelling, certificates, patent and exclusivity (USA), environmental risk (EU), Indian forms under NDCT Rules |
| 2 | 2.1 contents; 2.2 introduction; 2.3 Quality Overall Summary; 2.4 non-clinical overview; 2.5 clinical overview; 2.6 non-clinical summaries; 2.7 clinical summary |
| 3 | Quality (3.2.S, 3.2.P, 3.2.A, 3.2.R) |
| 4 | Non-clinical study reports (pharmacology, PK, toxicology) |
| 5 | Clinical study reports (BA/BE, PK, PD, efficacy and safety, post-marketing data, CRFs) |

Advantages: one core dossier reused worldwide; faster review; easier exchange between regulators; basis for electronic submissions.

### b. Electronic CTD (eCTD, ICH M8 / earlier M2 work)

| Feature | Meaning |
| --- | --- |
| Folder structure | m1 to m5 folders matching the modules |
| XML backbone | Index file listing every document, its location and life-cycle status |
| Documents | PDF with bookmarks and hyperlinks; some data sets in specified formats |
| Sequences | Each submission numbered 0000, 0001 … |
| Life-cycle operations | New, replace, append, delete |
| Checksums | Detect any change or corruption of files |
| Regional Module 1 | Each regulator publishes its own specification |
| Validation | Technical validation before review |

Version 3.2.2 has been used for many years; **eCTD v4.0** is being introduced by regulators step by step. The FDA requires eCTD for NDAs, ANDAs, BLAs, commercial INDs and master files (with stated exceptions); EU centralised applications are in eCTD; CDSCO accepts CTD dossiers through SUGAM (check its notices for electronic format requirements).

## 3.6 Industry and FDA liaison

Regulatory affairs (RA) professionals are the official link between a company and the regulator. Good liaison shortens development and avoids rejections.

### a. Channels of communication

| Channel | Use |
| --- | --- |
| Formal meetings (Type A, B, C and others) | Pre-IND, end-of-Phase-II, pre-NDA/BLA, resolving disputes |
| Written responses | Answers to information requests and discipline review letters |
| Special protocol assessment (SPA) | Agreement on design of pivotal trials, carcinogenicity studies or stability protocols |
| Advisory committee meetings | Public expert discussion of an application |
| Formal dispute resolution | Appeal above the review division |
| Small business and industry assistance (CDER SBIA), guidance documents, workshops | Education and clarification |
| Inspections and responses | Form 483 response within the expected time, CAPA, follow-up |
| Comment on draft guidance and proposed rules | Docket comments via the Federal Register |

### b. Role of RA in liaison

1. Plan the regulatory strategy and the meeting schedule.
2. Prepare briefing packages with precise questions.
3. Keep minutes and track every commitment.
4. Coordinate submissions with R&D, QA, manufacturing, clinical and legal.
5. Maintain honest, timely, documented communication — credibility with the regulator is a company asset.
6. Watch for new laws, guidances and enforcement trends (regulatory intelligence).

## 3.7 ICH guidelines: Q, S, E and M

The **International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use (ICH)** brings together regulators and industry to harmonise technical requirements. It began in 1990 (EU, USA, Japan) and became an international association in 2015; many regulators have since joined (for example Health Canada, Swissmedic, ANVISA Brazil, NMPA China and others). CDSCO India is an observer. Guidelines pass through a five-step process (Step 4 = adoption by ICH; Step 5 = implementation by each regulator).

### a. Quality (Q)

| Guideline | Topic |
| --- | --- |
| Q1A–Q1E | Stability testing (Q1B photostability) |
| Q2 | Validation of analytical procedures |
| Q3A–Q3D | Impurities in drug substances, products, residual solvents, elemental impurities |
| Q4B | Pharmacopoeial harmonisation |
| Q5A–Q5E | Quality of biotechnological products (viral safety, comparability Q5E) |
| Q6A, Q6B | Specifications |
| Q7 | GMP for APIs |
| Q8 | Pharmaceutical development (QbD) |
| Q9 | Quality risk management |
| Q10 | Pharmaceutical quality system |
| Q11 | Development and manufacture of drug substances |
| Q12 | Product life-cycle management |
| Q13 | Continuous manufacturing |
| Q14 | Analytical procedure development |

### b. Safety (S)

S1 carcinogenicity; S2 genotoxicity; S3 toxicokinetics; S4 duration of chronic toxicity studies; S5 reproductive toxicity; S6 pre-clinical safety of biotechnology products; S7A safety pharmacology and S7B QT (non-clinical); S8 immunotoxicity; S9 anticancer pharmaceuticals; S10 photosafety; S11 juvenile animal studies; S12 biodistribution for gene therapy products.

### c. Efficacy (E)

E1 extent of exposure for long-term treatment; E2A–E2F pharmacovigilance (E2A expedited reporting, E2B electronic case reports, E2C periodic benefit-risk evaluation report, E2D post-approval safety data, E2E pharmacovigilance planning, E2F development safety update report); E3 clinical study reports; E4 dose-response; E5 ethnic factors and bridging; **E6 Good Clinical Practice** (R3 adopted in 2025, with Annex 2 added later); E7 geriatrics; E8 general considerations; E9 statistical principles; E10 choice of control group; E11 paediatrics; E14 QT/QTc (clinical); E15–E16 pharmacogenomics and biomarkers; E17 multi-regional trials; E18 genomic sampling; E19 selective safety data collection.

### d. Multidisciplinary (M)

M1 MedDRA (medical dictionary for regulatory activities); M2 electronic standards; M3 non-clinical studies needed to support clinical trials; **M4 CTD**; M7 mutagenic impurities; **M8 eCTD**; M9 BCS-based biowaivers; M10 bioanalytical method validation; M11 structured clinical protocol; M12 drug interaction studies; M13 bioequivalence for immediate-release oral solid forms.

ICH adds and revises guidelines regularly; check the list and status on ich.org.

## 3.8 Regulatory requirements of the EU

- **EMA** (Amsterdam) coordinates scientific evaluation through committees: **CHMP** (opinions on human medicines), **PRAC** (pharmacovigilance), **CAT** (advanced therapies), **COMP** (orphans), **PDCO** (paediatrics), HMPC (herbal). The **European Commission** grants the binding authorisation; national competent authorities run national procedures.
- **Procedures:** centralised (compulsory for biotech products, ATMPs, orphan drugs and new substances for certain diseases; one EU-wide authorisation), decentralised, mutual recognition and national.
- **Centralised timeline:** CHMP evaluation up to **210 active days** (clock stops for questions), then Commission decision within **67 days** of the opinion.
- Validity five years, then renewal (usually unlimited after that).
- Requirements: **Qualified Person (QP)** batch release in the EU; **paediatric investigation plan (PIP)**; **risk management plan (RMP)**; pharmacovigilance system master file; GMP certificate of each site.
- Clinical trials under the **Clinical Trials Regulation (EU) No 536/2014**, applying since 31 January 2022 through CTIS (Unit 4).

## 3.9 Regulatory requirements of the UK (MHRA)

- **MHRA** (executive agency of the Department of Health and Social Care) regulates medicines, devices and blood components; the **Commission on Human Medicines** advises.
- Since leaving the EU, the UK grants its own marketing authorisations. Routes include full national applications and reliance routes such as the **International Recognition Procedure**, which uses approvals of trusted reference regulators; the UK also joins the **Access Consortium** and **Project Orbis** (oncology) work-sharing.
- **Yellow Card** scheme for adverse reaction reporting; MHRA inspects GMP, GDP, GCP and GLP.
- The legal base is the Human Medicines Regulations 2012; Northern Ireland arrangements differ — check current MHRA guidance.

## 3.10 Regulatory requirements of Australia (TGA)

- **Therapeutic Goods Administration (TGA)**, part of the Department of Health, under the **Therapeutic Goods Act 1989**.
- Every therapeutic good must be on the **Australian Register of Therapeutic Goods (ARTG)** before supply.

| Category | Risk | Label number |
| --- | --- | --- |
| Registered medicines (prescription, many OTC) | Higher; full evaluation | AUST R |
| Listed medicines (mainly complementary) | Low; permitted ingredients and claims only | AUST L |
| Medical devices | Classified by risk | ARTG entry |

- Prescription medicines are evaluated in CTD format with an Australian Module 1; pathways include standard, priority, provisional approval and work-sharing (Access Consortium with Canada, Singapore, Switzerland and the UK).
- Clinical trials run under the **CTN** (notification) or **CTA** (approval) scheme.

## 3.11 Rest of the world (ROW) markets

"ROW" usually means markets outside the USA, EU, UK, Japan, Canada and Australia: Asia, Africa, Latin America, the Middle East and the CIS. They matter greatly to Indian exporters.

| Region / body | Key points |
| --- | --- |
| ASEAN | **ACTD** (four parts: administrative, quality, non-clinical, clinical) with ACTR; national registration in each member state |
| Gulf Cooperation Council | Gulf centralised registration plus national registration; CTD with regional Module 1 |
| Africa | National authorities (for example SAHPRA in South Africa); regional harmonisation programmes; the African Medicines Agency is being set up |
| Latin America | ANVISA (Brazil), COFEPRIS (Mexico) and others; local BE and stability (climatic zone IV) often required |
| China, Japan | NMPA (China) and PMDA/MHLW (Japan) — ICH members using CTD with regional Module 1; Japan may need bridging data (ICH E5) |
| Eurasian Economic Union | Common rules for member states such as Russia |
| WHO prequalification | Assesses medicines for UN procurement (HIV, TB, malaria, vaccines); many African and Asian regulators rely on it |

Common ROW requirements: **Certificate of Pharmaceutical Product (COPP)** in the WHO format from the exporting country's authority, free sale certificate, GMP certificate, local agent, labelling in the local language, stability for the local climatic zone, samples and reference standards, and sometimes local testing or inspection. Indian firms usually keep one core CTD and adapt Module 1 (or ACTD Part I) country by country.

## Remember

- CMC = Module 3 (3.2.S, 3.2.P, 3.2.A, 3.2.R) + QOS 2.3; shows every batch matches the tested batches.
- US post-approval: PAS, CBE-30, CBE-0, annual report (314.70/314.97/601.12; annual report 314.81 within 60 days of anniversary). ICH Q12 established conditions and PACMPs.
- EU variations: IA (do and tell), IB (tell, wait, do), II (prior approval), extension; work-sharing.
- Combination product: 4 types (21 CFR 3.2(e)); PMOA (3.2(m)) decides lead centre; OCP; RFD; Part 4 GMP.
- Devices: US Class I/II/III; 510(k), De Novo, PMA, HDE, IDE; Part 820. EU MDR 2017/745 (I, IIa, IIb, III; CE mark; notified body). India MDR 2017 Class A–D; SLA for A/B manufacture, CLA for C/D and all imports.
- CTD M4: five modules; M1 regional. eCTD: m1–m5, XML backbone, sequences, new/replace/append/delete, checksums; v3.2.2 → v4.0.
- FDA liaison: Type A/B/C meetings, SPA, advisory committees, dispute resolution, 483 responses.
- ICH: Q (Q1–Q14), S (S1–S12), E (E1–E19; E6 GCP R3 2025), M (M1 MedDRA, M4 CTD, M7, M8 eCTD, M9, M10, M13).
- EU: EMA committees; centralised 210 + 67 days; QP release; PIP; RMP. UK MHRA: IRP, Yellow Card. Australia TGA: ARTG, AUST R/L, CTN/CTA.
- ROW: ACTD, GCC, WHO PQ, COPP, climatic zone IV stability, local agent and labelling.
