# Unit 1: Documentation in industry and generic drug product development

This unit covers the first half of PCI Unit 1 (part a). It starts with the documents that every pharmaceutical plant must keep, then follows a generic medicine from idea to approval and beyond: the US law that created the generic route (Hatch-Waxman), the Code of Federal Regulations, how product performance is shown in vitro and in vivo, the ANDA and NDA processes, changes after scale-up, post-marketing surveillance, and how bioavailability (BA) and bioequivalence (BE) work is outsourced to contract research organisations (CROs).

The USA is used as the model because the syllabus and the reference books follow the FDA system. Indian equivalents are given where they matter. Numbers below (exclusivity periods, reporting days) were checked against FDA sources and the Code of Federal Regulations; regulations change, so in real work always read the current text on fda.gov, ecfr.gov or cdsco.gov.in.

## 1.1 Why documentation matters

A regulator cannot stand in a factory every day. It judges quality from records. The GMP principle is simple: **"if it is not written down, it was not done."** Good documentation:

1. Defines what must be done (specifications, master formula, SOPs).
2. Proves what was actually done for each batch (batch records, logbooks, test reports).
3. Allows any batch to be traced from raw material to patient (and back again in a recall).
4. Supports investigations of deviations, complaints and out-of-specification results.
5. Forms the evidence submitted in dossiers and checked during inspections.

Good documentation practice is often summarised as **ALCOA+**: records must be Attributable, Legible, Contemporaneous, Original and Accurate, plus Complete, Consistent, Enduring and Available. In India the documentation requirements are part of Schedule M of the Drugs Rules, 1945 (revised Schedule M notified in 2023); in the USA they are in 21 CFR Part 211 (cGMP for finished pharmaceuticals).

### Hierarchy of GMP documents

```text
            Quality manual / Site Master File
                        │
     Specifications ── Master Formula Record ── SOPs
                        │
       Batch Manufacturing Record / Batch Packaging Record
                        │
   Logbooks, test records, CoA, distribution records, reports
```

## 1.2 Master Formula Record (MFR)

**Definition:** the MFR (also called master production record or master manufacturing instruction) is the approved master document that states, for one product and one batch size, the complete formula and the full manufacturing and packaging instructions. Every batch manufacturing record (BMR) is a copy of the MFR filled in during production.

### Contents of an MFR

| Part | Details |
| --- | --- |
| Product identity | Name, strength, dosage form, product code, batch size, shelf life, storage |
| Preparation and approval | Prepared, checked and approved by named, qualified persons with dates; version number |
| Formula | Each ingredient by name and reference code, quantity per unit and per batch, including overages with justification; grade (IP/BP/USP) |
| Equipment | List of equipment and its size or type; line clearance requirements |
| Process instructions | Step-by-step method: dispensing, sieving, mixing times and speeds, granulation, drying temperature and end-point, compression or filling parameters, coating |
| In-process controls | Tests, limits and frequency (weight variation, hardness, LOD, pH, fill volume) |
| Yield | Theoretical yield and acceptable limits at stated stages |
| Packaging | Packaging materials with codes and quantities, packaging instructions, specimen of printed materials, batch coding |
| Precautions | Safety, environmental conditions, special handling (light, moisture) |
| Sampling and release | Samples to QC; final release requirements |

**Uses:** keeps every batch the same; is the basis of process validation; is referenced in the dossier (Module 3.2.P.3) and is one of the first documents an inspector asks for.

## 1.3 Drug Master File (DMF)

**Definition:** a DMF is a confidential, detailed document that a manufacturer submits to a regulator about the facilities, processes or materials used in making a drug component (usually the active pharmaceutical ingredient, API). It lets the supplier keep its know-how secret from its customers while the regulator can still review it.

### How it works (US system)

```text
API maker (DMF holder) ─ files DMF ─→ FDA (DMF number)
        │
        └─ Letter of Authorisation (LoA) ─→ finished product company
                                              │
                                              └─ cites DMF number + LoA
                                                 in its ANDA/NDA → FDA
                                                 reviews DMF with the application
```

- The FDA does **not approve or disapprove** a DMF on its own; it reviews it when an application refers to it. Deficiencies are sent to the holder, not to the applicant.
- The holder keeps it current with amendments and annual updates.
- For generic APIs, a DMF fee and a "completeness assessment" apply under the generic drug user-fee programme (GDUFA).

| Type | Content |
| --- | --- |
| Type I | Manufacturing site, facilities, procedures and personnel — no longer accepted |
| Type II | Drug substance, intermediate and materials used in their preparation, or drug product |
| Type III | Packaging material |
| Type IV | Excipient, colourant, flavour, essence or materials used in their preparation |
| Type V | FDA-accepted reference information (for example sterile manufacturing site data) |

A Type II DMF is now written in CTD format (mainly Module 3.2.S). Equivalent systems elsewhere: the EU **Active Substance Master File** (ASMF, with an applicant's part and a restricted part) or a **Certificate of Suitability (CEP)** from the EDQM; master file procedures in Canada, Japan and WHO prequalification.

## 1.4 Distribution records

**Definition:** records showing where each batch of a product was sent, so that it can be traced and recalled quickly.

- **Contents:** product name and strength, batch number, quantity, date of dispatch, name and address of consignee, mode of transport and invoice number, and (for cold-chain products) temperature records.
- **Purpose:** rapid and complete **recall**; handling complaints; checking returns; preventing diversion and counterfeits.
- **Retention:** kept at least as long as the law requires (in the USA, 21 CFR 211.196 links distribution records to the expiry date; in India Schedule M sets the period — check the current text).

Recall classes (FDA): **Class I** (reasonable probability of serious harm or death), **Class II** (temporary or reversible harm), **Class III** (unlikely to cause harm). Distribution records decide how deep a recall goes: to wholesaler, retailer or patient level.

## 1.5 Generic drug product development: introduction

A **generic drug** is a copy of an innovator (brand) product whose patents and exclusivities have expired or been challenged. To be approved it must be **pharmaceutically equivalent** (same active ingredient, strength, dosage form, route) and **bioequivalent** to the reference product. Pharmaceutical equivalence plus bioequivalence gives **therapeutic equivalence**, which the FDA lists in the Orange Book with "A" codes (for example AB).

### Stages of generic development

```text
Product selection (market, patents, exclusivity, technical difficulty)
 → Reference product characterisation (reverse engineering: composition,
   particle size, polymorph, dissolution in several media, impurities)
 → API sourcing (DMF holder, LoA) and excipient selection
 → Pre-formulation and formulation development (QbD: QTPP, CQAs, DoE)
 → Pilot BE study (often) → process optimisation and scale-up
 → Exhibit batch (pivotal) + stability + pivotal BE study
 → ANDA (CTD) filing → review, inspection → approval → launch
```

Key terms from ICH Q8 used in generic development: **QTPP** (quality target product profile — what the product must be), **CQA** (critical quality attributes such as assay, dissolution, impurities), **CPP** (critical process parameters) and the **design space**.

### Patent and exclusivity check

Before starting, the company reads the **Orange Book** ("Approved Drug Products with Therapeutic Equivalence Evaluations"), which lists approved drugs, their patents and exclusivity periods. Patent strategy decides whether the generic waits for expiry or files a Paragraph IV challenge.

## 1.6 Hatch-Waxman Act and amendments

The **Drug Price Competition and Patent Term Restoration Act, 1984**, known as the **Hatch-Waxman Act**, amended the Federal Food, Drug, and Cosmetic (FD&C) Act. It was a bargain between generic companies and innovators.

| For generic companies | For innovators |
| --- | --- |
| ANDA route under section 505(j): no repeat of safety and efficacy trials; BE to the reference listed drug (RLD) is enough | **Patent term restoration** for time lost in FDA review (patent term extension) |
| "Safe harbour": using a patented drug to develop data for FDA submission is not infringement | Data exclusivity periods during which generics cannot be approved (or filed) |
| 180-day exclusivity for the first applicant to file a successful Paragraph IV challenge | Patent listing in the Orange Book and an automatic **30-month stay** when they sue a Paragraph IV filer in time |

### Exclusivity periods (FDA)

| Exclusivity | Length |
| --- | --- |
| New chemical entity (NCE) | 5 years |
| New clinical investigation (new indication, dosage form etc. needing new clinical studies) | 3 years |
| Orphan drug | 7 years |
| Paediatric | 6 months added to existing patents and exclusivities |
| 180-day patent challenge (generic) | 180 days |
| Competitive generic therapy (generic) | 180 days |
| GAIN (qualifying infectious disease products) | 5 years added to certain exclusivities |

A US patent normally runs 20 years from the filing date of the application. During NCE exclusivity an ANDA with a Paragraph IV certification may be submitted only after four years (the "NCE-1" date); the exact statutory rules are in section 505(j)(5) of the FD&C Act.

### Patent certifications in an ANDA

| Certification | Meaning |
| --- | --- |
| Paragraph I | No patent information filed |
| Paragraph II | Patent has expired |
| Paragraph III | Patent will expire on a stated date; approval after that date |
| Paragraph IV | Patent is invalid or will not be infringed; notice to patent owner; suit within 45 days triggers the 30-month stay |
| Section viii statement | A patented method of use is "carved out" of the generic label |

### Later amendments that changed the scheme

| Law | Main change for generics |
| --- | --- |
| Medicare Prescription Drug, Improvement and Modernization Act (MMA), 2003 | Limited the innovator to one 30-month stay per ANDA; introduced forfeiture events for the 180-day exclusivity; declaratory judgement actions |
| FDA Amendments Act (FDAAA), 2007 | Rules on citizen petitions (section 505(q)) that delay generics; REMS |
| FDA Safety and Innovation Act (FDASIA), 2012 | Created the **Generic Drug User Fee Amendments (GDUFA)**: fees in return for review goals and inspections |
| FDA Reauthorization Act (FDARA), 2017 | Competitive generic therapy designation with 180-day exclusivity; GDUFA II |
| Biologics Price Competition and Innovation Act, 2009 | The biological counterpart: abbreviated route for biosimilars under section 351(k) of the Public Health Service Act |

## 1.7 Code of Federal Regulations (CFR)

The **CFR** is the codification of the permanent rules published in the **Federal Register** by US federal agencies. It has 50 **titles**; **Title 21** covers Food and Drugs and is mostly FDA rules. A citation such as **21 CFR 314.94** means Title 21, Part 314, Section 94. The Federal Register is the daily publication where proposed and final rules first appear; the electronic CFR (eCFR) is updated continuously.

| Part (Title 21) | Subject |
| --- | --- |
| 11 | Electronic records and electronic signatures |
| 50 | Protection of human subjects (informed consent) |
| 54 | Financial disclosure by clinical investigators |
| 56 | Institutional review boards |
| 58 | Good laboratory practice for non-clinical studies |
| 201 | Labelling |
| 210, 211 | cGMP (general; finished pharmaceuticals) |
| 312 | Investigational new drug application |
| 314 | Applications for FDA approval to market a new drug (NDA, ANDA) |
| 320 | Bioavailability and bioequivalence requirements |
| 600–680 | Biologics |
| 800 onwards | Medical devices (for example 807 for 510(k), 814 for PMA, 820 quality system) |

## 1.8 Drug product performance: in vitro

**Drug product performance** means the release of the drug from the dosage form leading to systemic availability. In vitro it is measured by **dissolution testing**.

1. **Dissolution method development:** apparatus (USP I basket, II paddle, IV flow-through), medium (pH 1.2, 4.5, 6.8, with surfactant if needed), volume, rotation speed, sampling times; must be discriminating (able to detect meaningful formulation changes).
2. **Comparison with the reference product:** profiles compared at several pH values. The **similarity factor f2** is used; **f2 between 50 and 100** means the profiles are similar (a mean difference of not more than 10% at each point).

```text
f2 = 50 × log { [1 + (1/n) Σ (Rt − Tt)²]^(−0.5) × 100 }
R, T = % dissolved of reference and test at time t; n = number of points
```

3. **Biopharmaceutics Classification System (BCS):** Class I high solubility–high permeability; II low–high; III high–low; IV low–low. For immediate-release products, a **BCS-based biowaiver** may replace an in vivo BE study for Class I (and, with stricter conditions, Class III) drugs, as set out in ICH M9.
4. **IVIVC (in vitro–in vivo correlation):** Level A (point-to-point) is the most useful; it can justify waivers for some changes of modified-release products.
5. **Biowaivers for lower strengths:** where the strengths are proportional in composition and dissolution is similar, BE on one strength may support the others.

## 1.9 Bioequivalence and drug product assessment: in vivo

**Bioavailability (BA):** the rate and extent to which the active ingredient is absorbed and becomes available at the site of action. **Bioequivalence (BE):** absence of a significant difference in the rate and extent of availability of two pharmaceutically equivalent products given at the same molar dose under similar conditions (21 CFR 320).

### Typical BE study design

| Element | Usual choice |
| --- | --- |
| Design | Randomised, two-period, two-sequence, crossover, single dose; washout ≥ 5 elimination half-lives |
| Subjects | Healthy adult volunteers (patients for toxic drugs such as many anticancer agents); number from a power calculation |
| Conditions | Fasting; fed study also for many products (as the product-specific guidance requires) |
| Sampling | Enough points to define Cmax and to cover at least 80% of AUC |
| Bioanalysis | Validated method (ICH M10) |
| Parameters | Cmax (rate), AUC0–t and AUC0–∞ (extent), Tmax |
| Statistics | Log-transformed data; ANOVA; **90% confidence interval of the test/reference ratio within 80.00–125.00%** for Cmax and AUC |

Special cases: highly variable drugs (reference-scaled average BE), narrow therapeutic index drugs (tighter limits in some regulators), replicate designs, steady-state studies, and clinical endpoint or pharmacodynamic studies when blood levels cannot be measured (for example locally acting products). The FDA publishes **product-specific guidances** describing the BE study expected for each drug.

**Drug product assessment** in the ANDA brings together: pharmaceutical equivalence, BE, CMC quality, stability, labelling sameness and GMP of all sites.

## 1.10 ANDA regulatory approval process

```text
ANDA in eCTD (Module 1 to 5; Modules 4 and 5 mainly BE)
 → Filing review / receipt (completeness, fees paid, DMF complete)
      → "refuse to receive" if seriously incomplete
 → Discipline reviews: bioequivalence, chemistry/manufacturing
   (drug substance via DMF, drug product), microbiology (sterile),
   labelling (same as RLD)
 → Pre-approval inspections of manufacturing and testing sites,
   and of the BE clinical and analytical sites
 → Information requests / discipline review letters
 → Action: APPROVAL, TENTATIVE APPROVAL (blocked only by patent or
   exclusivity) or COMPLETE RESPONSE LETTER
```

Review is done by the **Office of Generic Drugs** (OGD) in CDER. Review goals are agreed under GDUFA; check the current commitment letter for exact months. ANDA requirements are in **21 CFR 314.94**.

## 1.11 NDA approval process (overview)

An **NDA** (21 CFR 314; form FDA 356h) asks for approval of a new drug and must prove safety and efficacy with full non-clinical and clinical data.

```text
Pre-IND meeting → IND → Phase I–III → end-of-Phase-II meeting
 → pre-NDA meeting → NDA submission (eCTD)
 → filing decision within 60 days ("refuse to file" possible)
 → review (medical, statistics, clinical pharmacology, pharm/tox,
   CMC, microbiology), advisory committee if needed,
   pre-approval inspection, labelling negotiation
 → approval letter or complete response letter
```

Review goals under PDUFA: **standard 10 months, priority 6 months** (for new molecular entities, counted from the 60-day filing date). Routes: 505(b)(1) full NDA; 505(b)(2) NDA relying partly on literature or FDA's earlier findings (new salt, new dosage form, new combination). Details are in Units 2 and 4.

## 1.12 Scale-up and post-approval changes (SUPAC)

Generic exhibit batches are often smaller than commercial batches. After approval, firms scale up, move sites, change equipment or suppliers. The FDA **SUPAC** guidances (SUPAC-IR for immediate-release solid oral forms, SUPAC-MR for modified release, SUPAC-SS for semisolids) classify such changes into levels by their likely effect on quality and performance.

| Level | Likely effect | Typical filing | Data usually needed |
| --- | --- | --- | --- |
| 1 | Unlikely to have a detectable effect | Annual report | Application or compendial tests, stability on one batch in the annual report |
| 2 | Could have a significant effect | Changes-being-effected supplement (CBE-30) or prior approval supplement, depending on change | Multi-point dissolution comparison, stability |
| 3 | Likely to have a significant effect | Prior approval supplement | Dissolution, stability, and often an in vivo BE study |

Change types covered: **components and composition**, **site of manufacture**, **batch size (scale-up or scale-down)**, **manufacturing equipment** and **manufacturing process**. For SUPAC-IR a batch-size change of more than ten times the pilot or bio-batch is Level 2. The general rule for reporting categories is 21 CFR 314.70 (NDA) and 314.97 (ANDA): prior approval supplement for major changes, CBE-30 or CBE-0 for moderate, annual report for minor.

## 1.13 Post-marketing surveillance (PMS)

Clinical trials are too small and too short to find rare or delayed adverse reactions, so safety monitoring continues after approval.

**US requirements (21 CFR 314.80, applies to NDA and, via 314.98, ANDA holders):**

| Report | Timing |
| --- | --- |
| 15-day "alert report" | Each serious and unexpected adverse drug experience, within **15 calendar days** of first receipt; follow-ups within 15 days of new information |
| Periodic report | **Quarterly for 3 years** from approval (due within 30 days of the close of each quarter), then **annually** (within 60 days of the approval anniversary) |
| Records | Kept for **10 years** |

Other tools: FDA Adverse Event Reporting System (FAERS) and **MedWatch** (voluntary reporting by health professionals and patients); **Risk Evaluation and Mitigation Strategies (REMS)** for high-risk drugs; post-marketing requirements and commitments (Phase IV studies); the Sentinel system for active surveillance using health-care data.

**India:** periodic safety update reports every six months for the first two years after approval and annually for the next two years (NDCT Rules, 2019); spontaneous reporting through the **Pharmacovigilance Programme of India (PvPI)**, coordinated by the Indian Pharmacopoeia Commission, Ghaziabad.

## 1.14 Outsourcing BA and BE studies to CROs

Most generic companies do not run their own clinical units; they contract **CROs** (contract research organisations) that have clinical facilities, bioanalytical laboratories and biostatistics teams.

### Steps in outsourcing

```text
Need identified (pilot or pivotal BE) → shortlist CROs
 → confidentiality agreement → request for proposal → technical and
   cost evaluation → qualification audit (facility, GCP, GLP,
   regulatory inspection history, data integrity, SOPs)
 → contract + quality agreement (who does what, data ownership,
   audit rights, timelines, subcontracting rules)
 → protocol finalised → ethics committee and regulator approvals
 → study conduct with sponsor monitoring → bioanalysis → statistics
 → clinical study report → sponsor audit → dossier
```

### Points to consider when choosing a CRO

1. Inspection history with the target regulators (FDA, EMA, MHRA, WHO, CDSCO); any untitled letters or warning letters.
2. Registration with the national authority (in India, BA/BE study centres need registration with the Central Licensing Authority under the NDCT Rules, 2019 — check the current rule) and a registered ethics committee.
3. Validated bioanalytical methods (ICH M10), calibrated instruments, LIMS and audit trails (21 CFR Part 11).
4. Volunteer database and safeguards against over-volunteering.
5. Quality assurance unit independent of operations; archiving of samples and data.

**Sponsor remains responsible:** under ICH E6, duties can be transferred to a CRO, but the sponsor stays ultimately responsible for the quality and integrity of the trial data. Regulators have rejected BE data from CROs with data integrity failures, which shows why audits matter.

## Remember

- Documents: quality manual → specifications, MFR, SOPs → BMR/BPR → records. ALCOA+. MFR = master; BMR = copy filled for each batch.
- DMF: confidential; LoA; FDA neither approves nor disapproves; Types II (API), III (packaging), IV (excipient), V (reference); Type I no longer used. EU: ASMF, CEP.
- Distribution records: batch-wise consignees for recall; FDA recall Classes I–III.
- Hatch-Waxman 1984: ANDA 505(j), patent term restoration, safe harbour, Paragraph I–IV, 30-month stay, 180-day exclusivity. NCE 5 y, new clinical investigation 3 y, orphan 7 y, paediatric 6 months.
- Amendments: MMA 2003, FDAAA 2007, FDASIA/GDUFA 2012, FDARA 2017 (CGT 180 days); BPCI Act 2009 for biosimilars.
- CFR Title 21: 11, 50, 56, 58, 211, 312, 314, 320; Federal Register publishes rules.
- In vitro: discriminating dissolution, f2 50–100, BCS biowaiver (ICH M9), IVIVC Level A.
- In vivo BE: crossover, Cmax and AUC, 90% CI 80.00–125.00%.
- ANDA: 21 CFR 314.94; OGD; tentative approval. NDA: 60-day filing, 10/6 months review.
- SUPAC Levels 1–3; 314.70: PAS, CBE-30, CBE-0, annual report.
- PMS (314.80): 15-day alert reports; quarterly 3 years then annual; records 10 years. India: PSUR 6-monthly × 2 y, yearly × 2 y; PvPI.
- CRO outsourcing: audit, contract, quality agreement; sponsor stays responsible.
