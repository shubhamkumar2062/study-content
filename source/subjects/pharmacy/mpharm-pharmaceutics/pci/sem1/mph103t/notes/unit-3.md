# Unit 3: Pharmaceutical validation and qualification

Syllabus item 2: introduction to pharmaceutical validation, scope and merits of validation, validation and calibration master plan, ICH and WHO guidelines for calibration and validation of equipment, validation of specific dosage forms, types of validation, government regulation, manufacturing process model, URS, DQ, IQ, OQ and PQ of facilities.

## 3.1 Introduction and definitions

**Validation** (classical WHO wording, in plain terms) is documented evidence, obtained by planned studies, that a procedure, process, piece of equipment, material, activity or system actually and consistently leads to the expected results.

**Process validation (US FDA guidance, 2011)** is the collection and evaluation of data, from the process design stage through commercial production, which establishes scientific evidence that a process is capable of consistently delivering quality product.

Related terms:

| Term | Meaning |
| --- | --- |
| **Qualification** | Proving that equipment, utilities or facilities are properly installed, work correctly and give expected results. Qualification is part of validation; we "qualify" equipment and "validate" processes |
| **Calibration** | Set of operations that establish, under specified conditions, the relationship between values shown by an instrument and the corresponding known values of a reference standard, traceable to national or international standards |
| **Verification** | Confirmation by examination and provision of objective evidence that specified requirements have been met (for example verifying a pharmacopoeial method in your laboratory) |
| **Revalidation** | Repeating validation after a change or at defined intervals to show the validated state is maintained |
| **Worst case** | Conditions at the upper and lower limits of operating ranges that pose the greatest chance of failure compared with ideal conditions |
| **Critical process parameter (CPP)** | A process parameter whose variability affects a CQA and should therefore be monitored or controlled |

**Why "quality cannot be tested into a product":** end-product testing examines only a small sample and is often destructive (sterility, dissolution). Confidence that every unit is acceptable comes from a process that is designed, understood, validated and controlled. Validation is therefore the foundation of GMP.

## 3.2 Scope and merits of validation

**Scope** — validation applies to:

- Manufacturing processes (granulation, blending, compression, coating, filling, sterilisation, lyophilisation)
- Equipment, utilities and facilities (HVAC, purified water and WFI systems, compressed air, nitrogen, steam, clean rooms)
- Cleaning procedures
- Analytical methods
- Computerised systems (manufacturing execution, LIMS, chromatography data systems; GAMP 5 approach)
- Packaging processes, transport and cold chain (temperature mapping of warehouses and shippers)
- Vendors (supplier qualification) and personnel (aseptic operator qualification, media fills)

**Merits:**

1. Assurance of consistent product quality, batch after batch.
2. Fewer rejections, reworks, recalls and complaints → lower cost of quality.
3. Better process understanding; faster troubleshooting and scale-up.
4. Reduced end-product testing; a basis for **real-time release testing** where justified.
5. Legal and regulatory compliance (licence, export registration, inspections).
6. Increased output and optimum use of equipment, because process limits are known.
7. Safer, more effective products for patients.

## 3.3 Government regulation

| Regulator / guidance | Validation requirement (in brief) |
| --- | --- |
| **India — Schedule M (Drugs Rules, 1945)** | GMP and requirements of premises, plant and equipment. The **revised Schedule M** notified in December 2023 brings Indian GMP close to WHO GMP and adds a pharmaceutical quality system, quality risk management, product quality review, qualification and validation, and computerised systems |
| **US FDA — 21 CFR 210/211** | 211.100: written procedures for production and process control designed to assure products have the identity, strength, quality and purity they purport; 211.63–211.68 equipment design, cleaning, calibration; 2011 Process Validation guidance (lifecycle) |
| **EU GMP Annex 15** | Qualification and validation: URS, DQ, FAT/SAT, IQ, OQ, PQ; process validation (traditional, continuous, hybrid); cleaning validation; change control |
| **WHO** | WHO GMP supplementary guidelines on validation and its appendices (HVAC, water systems, cleaning, analytical, computerised systems, qualification, non-sterile process validation) in the WHO Technical Report Series |
| **ICH** | Q2(R2) analytical procedure validation; Q7 GMP for APIs (chapter on validation and qualification); Q8(R2) pharmaceutical development; Q9 quality risk management; Q10 pharmaceutical quality system |
| **PIC/S** | Recommendations on the validation master plan, IQ/OQ, non-sterile process validation and cleaning validation |

## 3.4 Validation master plan (VMP) and calibration master plan

A **validation master plan** is a high-level document that summarises the firm's overall philosophy, intentions and approach to validation. It is approved by senior management and quality assurance and is the first document an inspector usually asks for.

**Typical contents of a VMP:**

1. Introduction, objectives and validation policy of the site.
2. Organisational structure: responsibilities of the validation team, QA, production, engineering, QC.
3. Summary of facilities, systems, equipment and processes to be validated, with their current status.
4. Documentation format: protocols, reports, numbering, approval.
5. Planning and scheduling (validation matrix/timeline).
6. Change control system and requalification/revalidation policy.
7. Approach to risk assessment (which items are critical and need most work).
8. Reference to SOPs, acceptance criteria philosophy, deviation handling.
9. Training requirements.
10. Glossary and references.

**Calibration master plan / programme:** list of all instruments and gauges (critical, non-critical, reference-only), their calibration ranges and tolerances, frequency, method SOP, reference standards with traceability (in India to the National Physical Laboratory or an accredited NABL laboratory), status labels (calibrated / due date / out of calibration), and the procedure when an instrument is found out of tolerance (impact assessment on product made since the last good calibration).

## 3.5 Qualification of facilities and equipment: URS, DQ, IQ, OQ and PQ

### The V-model

```text
 URS (what we need) ─────────────────────────────────── PQ (does it do what we need,
   │                                                        with product/placebo, real conditions?)
   └ Functional specification ──────────────────── OQ (does each function work over
        │                                               its operating ranges?)
        └ Design specification (DQ) ──────── IQ (is it installed as designed?)
              │
              └──── Build / fabrication → FAT at vendor → SAT at site
```

Each specification on the left is verified by the qualification step opposite it on the right.

| Stage | Definition | Typical content |
| --- | --- | --- |
| **URS — User Requirement Specification** | Written statement of what the user requires the equipment/facility to do | Capacity, output, materials of construction (product-contact SS 316L), cleanability, safety, GMP needs (no dead legs, smooth finish), utilities, controls and alarms, documentation and 21 CFR Part 11 needs, training |
| **DQ — Design Qualification** | Documented verification that the proposed design is suitable for the intended purpose and meets the URS | Design drawings, P&ID, vendor selection, comparison of design specification with URS, risk assessment |
| **FAT / SAT** | Factory acceptance test at the vendor; site acceptance test after delivery | Functional checks before shipping and after arrival |
| **IQ — Installation Qualification** | Documented verification that equipment or systems, as installed or modified, comply with the approved design and the manufacturer's recommendations | Model and serial number, components list, materials certificates, utilities connection, drawings as-built, calibration of critical instruments, manuals, spare parts list, environmental conditions |
| **OQ — Operational Qualification** | Documented verification that the equipment or system performs as intended **throughout the anticipated operating ranges** | Function of controls, interlocks, alarms; speed, temperature, pressure ranges at limits; power failure recovery; usually without product |
| **PQ — Performance Qualification** | Documented verification that equipment and ancillary systems, connected together, perform effectively and reproducibly on the approved process method and specification | Run with product or placebo/surrogate under routine conditions for several runs; results meet specification consistently |

### Examples of facility qualification

- **HVAC / clean room:** airflow velocity and air changes per hour, HEPA filter integrity (aerosol challenge), pressure differentials, airflow visualisation (smoke study), recovery time, non-viable particle counts at rest and in operation, viable monitoring (settle plates, active air sampling, contact plates), temperature and humidity mapping.
- **Water system (purified water / WFI):** IQ of pipework (slope, welding records, passivation, no dead legs), OQ of each unit operation, PQ in three phases over about a year: intensive daily sampling (phase 1, about 2–4 weeks), continued intensive sampling with SOPs in use (phase 2), and routine monitoring over a full year to cover seasonal variation (phase 3).
- **Autoclave / dry-heat steriliser:** empty-chamber heat distribution, loaded-chamber heat penetration with thermocouples in the coldest spots, biological indicators (Geobacillus stearothermophilus spores for moist heat), F0 calculation, endotoxin challenge for depyrogenation tunnels.

## 3.6 Types of process validation

| Type | When done | Remarks |
| --- | --- | --- |
| **Prospective** | Before commercial distribution of a new product or after a major change | Planned protocol; batches released only after validation is complete; the preferred approach |
| **Concurrent** | During routine production, batches released as validation proceeds | Acceptable in exceptional cases (low-volume products, orphan drugs, urgent public-health need) with strong justification |
| **Retrospective** | Using historical data of batches already made | Old approach for long-marketed products; needs many consistent batches (often 10–30) with complete records; no longer acceptable for new products |
| **Revalidation** | After changes (formula, equipment, site, supplier, batch size) or periodically | Driven by change control and product quality review |

**Process validation lifecycle (US FDA 2011, broadly reflected in EU Annex 15 and WHO):**

1. **Stage 1 — Process design:** knowledge from development and scale-up (DoE, risk assessment) defines the commercial process and the control strategy.
2. **Stage 2 — Process qualification:** facility and equipment qualification, then **process performance qualification (PPQ)** batches under a protocol, often with heightened sampling. The number of batches must be justified scientifically; three consecutive successful batches has been the traditional minimum.
3. **Stage 3 — Continued process verification (CPV):** ongoing monitoring of CPPs and CQAs with statistical tools (control charts, process capability) to show the process stays in control.

**Process capability** — a quantitative check used in Stages 2 and 3:

Cp = (USL − LSL)/6σ and Cpk = the smaller of (USL − mean)/3σ and (mean − LSL)/3σ.

**Worked example:** assay specification 95.0–105.0% of label claim; PPQ data mean 100.6%, standard deviation 1.2%. Cp = 10/(6 × 1.2) = **1.39**; Cpk = (105.0 − 100.6)/(3 × 1.2) = **1.22**. Cpk of 1.33 or more is commonly taken as a capable process; 1.22 shows the process is acceptable but off-centre and slightly too variable, so it should be watched.

**Other categories of validation:**

- **Cleaning validation:** proves that the cleaning procedure removes product residue, cleaning agent and microbes to acceptable levels. Steps: worst-case product selection (least soluble, most potent, hardest to clean), acceptance limits (visually clean, a carry-over limit based on the health-based exposure limit (PDE) or older criteria such as not more than 10 ppm of the previous product in the next, or 1/1000 of its smallest therapeutic dose in the largest daily dose of the next), sampling (swab for direct surfaces, rinse for inaccessible areas, with recovery studies), validated analytical method (HPLC, TOC), dirty and clean hold times.
- **Analytical method validation (ICH Q2(R2)):** specificity, linearity, range, accuracy (recovery), precision (repeatability, intermediate precision, reproducibility), detection limit (LOD = 3.3σ/S), quantitation limit (LOQ = 10σ/S), robustness. Assay methods need accuracy, precision, specificity, linearity and range; identification tests need only specificity.
- **Computerised system validation:** GAMP 5 risk-based approach, data integrity principles (ALCOA+: attributable, legible, contemporaneous, original, accurate, plus complete, consistent, enduring, available), audit trails and electronic signatures (21 CFR Part 11).

## 3.7 Manufacturing process model

A manufacturing process is viewed as a system that converts **inputs** into **outputs** under **controls**:

```text
           Process parameters (CPPs): time, temperature, speed, force, spray rate
                         │
 Inputs ────────────►  UNIT OPERATION  ────────────► Output (intermediate / product)
 materials (CMAs):          ▲                          quality attributes (CQAs)
 API particle size,         │
 moisture, excipient    Environment, people, equipment state, methods
 grade                  (noise factors)
```

Each unit operation is mapped this way (process flow diagram), risk is assessed (fishbone/Ishikawa, FMEA), critical steps are identified, and the validation protocol defines what to monitor, how many samples and the acceptance criteria. The output of one step is the input of the next, so control is built up step by step.

## 3.8 Validation of specific dosage forms

### Tablets (wet granulation process)

| Unit operation | Critical parameters | Tests / acceptance |
| --- | --- | --- |
| Dispensing and sifting | Mesh size, API particle size | Identity, particle size |
| Dry mixing | Mixer speed, time, load | Blend uniformity (often 10 locations, sample about 1–3 times unit weight) |
| Wet granulation | Binder quantity and addition rate, impeller and chopper speed, kneading time, end point (power consumption) | Granule appearance, bulk density |
| Drying (FBD) | Inlet temperature, airflow, time | Loss on drying |
| Milling / sizing | Screen size, speed | Particle size distribution |
| Lubrication | Blending time, lubricant amount | Blend uniformity, flow, bulk/tapped density |
| Compression | Force, speed, feeder speed, hopper level | Weight variation, hardness, thickness, friability, disintegration, dissolution, content uniformity (sampled at start, middle, end, and at high/low speed and force) |
| Coating | Pan speed, spray rate, inlet/exhaust temperature, atomisation pressure | Weight gain, appearance, dissolution |

### Liquids (oral solutions and suspensions)

Mixing time and speed, order of addition, dissolution of solutes (clarity), pH, viscosity, homogeneity of suspension at top-middle-bottom of the holding tank and during filling, preservative content, fill volume, microbial limits.

### Semisolids (creams, ointments)

Heating and cooling temperatures and rates, homogeniser speed and time, phase addition rate, vacuum, content uniformity (top, middle, bottom of the vessel), viscosity, pH, globule size, fill weight and tube uniformity.

### Parenterals (sterile products)

Validation of WFI and clean steam, HVAC and clean rooms, filter validation (bacterial retention with Brevundimonas diminuta challenge, compatibility, extractables), sterilisation cycles (moist heat, dry heat, depyrogenation), **aseptic process simulation (media fills)** — filling a growth medium instead of product through the whole aseptic process; contamination limits are set very low (for small runs, zero contaminated units), container closure integrity, lyophilisation cycle, visual inspection qualification.

## 3.9 Documentation and change control

- **Protocol** (approved before work starts): objective, scope, responsibilities, equipment, process description, CPPs, sampling plan, tests, acceptance criteria, deviation handling.
- **Report:** results, deviations and their investigation, conclusion and approval.
- **Change control:** any proposed change is assessed for its effect on the validated state; it may need no action, partial or full revalidation, or regulatory notification.
- **Annual product quality review** confirms the process remains in a state of control and triggers revalidation where needed.

## Remember

- Validation = documented evidence of consistency; qualification = equipment/facility part of it; calibration = instrument vs traceable standard.
- V-model: URS ↔ PQ, functional spec ↔ OQ, design spec (DQ) ↔ IQ; FAT and SAT in between.
- IQ: installed as designed; OQ: works across operating ranges (no product); PQ: performs reproducibly with product/placebo under routine conditions.
- Types: prospective (preferred), concurrent (exceptional), retrospective (historical), revalidation.
- FDA 2011 lifecycle: process design → process qualification (PPQ) → continued process verification.
- Cpk = min(USL − mean, mean − LSL)/3σ; worked example Cp 1.39, Cpk 1.22; ≥ 1.33 = capable.
- Regulations: revised Schedule M (December 2023), 21 CFR 211, EU Annex 15, WHO TRS validation appendices, ICH Q2(R2), Q7–Q10.
- Cleaning validation: worst-case product, PDE-based or 10 ppm / 1/1000 dose criteria, swab and rinse with recovery; media fills for aseptic processing.
