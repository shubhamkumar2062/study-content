# Unit 5: Calibration, validation and warehousing

Testing a sample tells you about that sample. Validation tells you that the process, equipment and method will give the right result every time, so that a tested sample can stand for the whole batch. Calibration makes sure the instruments that measure the process tell the truth. This unit covers the definitions and principles of calibration, qualification and validation, the types of validation, the validation master plan, two worked examples (pH meter calibration and UV-visible spectrophotometer qualification), analytical method validation, and finally good warehousing practice and materials management.

## 5.1 Definitions

| Term | Definition (in plain words) |
| --- | --- |
| Calibration | The set of operations that establish, under stated conditions, the relationship between the values shown by an instrument and the known values of a reference standard, and adjust it if needed |
| Qualification | Action of proving and documenting that equipment or ancillary systems are properly installed, work correctly and actually lead to the expected results. It is part of validation, applied to equipment, utilities and facilities |
| Validation | Action of proving and documenting, in line with GMP, that any procedure, process, equipment, material, activity or system actually leads to the expected results consistently |
| Verification | Confirmation by examination and evidence that specified requirements have been met (for example verifying a pharmacopoeial method in your own lab) |

Simple way to remember: **we calibrate instruments, qualify equipment and validate processes and methods.**

## 5.2 Calibration: general principles

1. Every instrument used for measurement in production and QC is listed in a calibration master list with its identification number, range, accuracy needed and frequency of calibration.
2. Calibration follows a written SOP, against **reference standards traceable** to national or international standards (in India, through the National Physical Laboratory or an accredited calibration laboratory).
3. The standard used is more accurate than the instrument being calibrated.
4. Calibration covers the range in which the instrument is used.
5. Results are recorded; acceptance limits are set in advance.
6. A label on the instrument shows the date of calibration, the next due date and who did it.
7. If an instrument is found **out of calibration**, it is labelled "out of calibration", not used, repaired and recalibrated; the impact on results obtained since the last good calibration is investigated.
8. Calibration may be done in-house or by an outside agency (preferably NABL-accredited for that parameter).

**Typical instruments calibrated:** balances, pH meters, thermometers and temperature sensors, pressure gauges, timers, UV-visible spectrophotometers, HPLC, dissolution apparatus, disintegration testers, hardness testers, autoclaves and ovens (temperature probes).

## 5.3 Qualification

```text
V-model of qualification

 User requirement specification (URS) ----------------> Performance qualification (PQ)
      \                                                       /
   Design qualification (DQ) ---------------------> Operational qualification (OQ)
          \                                             /
     Functional / design specifications --> Installation qualification (IQ)
                         \                       /
                          ---- Build / supply ----

Left side: what we need and how it is designed.
Right side: proof that what was delivered meets each level.
```

| Stage | Question it answers | Typical checks |
| --- | --- | --- |
| Design qualification (DQ) | Is the proposed design suitable for its intended purpose? | Design and specifications compared with the URS and GMP needs; materials of construction; cleanability |
| Installation qualification (IQ) | Has it been delivered and installed correctly? | Equipment received as ordered, components, drawings, manuals, utilities connected, materials of construction certificates, calibration of built-in instruments, SOPs drafted |
| Operational qualification (OQ) | Does it work as intended across its operating ranges? | Function of controls, alarms, interlocks, speeds, temperatures at upper and lower limits, "worst case" conditions, without product |
| Performance qualification (PQ) | Does it perform consistently in actual use with product or simulated product? | Runs with product or placebo, repeated (commonly three consecutive runs), meeting acceptance criteria |

After major repair, relocation or modification, **requalification** is done. Periodic review confirms equipment remains in a qualified state.

## 5.4 Validation

### 5.4.1 Importance of validation

- Builds quality into the product instead of relying on end testing alone.
- Assures that every batch is consistent, because a sample cannot detect all defects (for example sterility tests examine only a few units).
- Reduces rejects, reprocessing and complaints, saving cost.
- Reduces risk to patients.
- Is a legal requirement of GMP (Schedule M, WHO, US FDA, EU).
- Supports process improvement and makes changes safer through revalidation.

### 5.4.2 Scope of validation

| Area | Examples |
| --- | --- |
| Process validation | Granulation, compression, coating, mixing, filling, sterilisation (autoclave, dry heat), aseptic filling (media fill), lyophilisation |
| Cleaning validation | Proof that cleaning removes residues of product and detergent and controls microbes, to an acceptable limit |
| Analytical method validation | Assay, impurity, dissolution and identification methods |
| Equipment and facility qualification | Production and laboratory equipment, clean rooms, HVAC |
| Utility qualification | Purified water, water for injections, compressed air, nitrogen, clean steam |
| Computer system validation | Software controlling processes or holding GMP records (data integrity) |
| Transport and storage validation | Cold chain, warehouse temperature mapping |
| Packaging validation | Sealing of blisters, container closure integrity |

### 5.4.3 Types of process validation

| Type | When done | Description | Notes |
| --- | --- | --- | --- |
| Prospective validation | Before a new product or process is released for sale | Planned studies on (commonly) three consecutive batches under a pre-approved protocol; batches released only after the report is approved | The preferred approach |
| Concurrent validation | In exceptional cases (for example low-volume products, urgent supply) | Validation done during routine production; batches may be released one by one after testing, while data are collected | Must be justified and approved by QA |
| Retrospective validation | For products long in production, not validated before | Review of historical batch records, in-process and final test data of many batches (often 10–30) to show consistency | No longer accepted as the normal approach for new work by most regulators |
| Revalidation | After changes or periodically | Repeat of validation after a change in formula, process, equipment, site, batch size or supplier, or after trends show drift | Driven by change control |

**Modern lifecycle approach** (as described in US FDA process validation guidance, 2011): Stage 1 process design, Stage 2 process qualification (including PQ of the process), Stage 3 continued process verification during routine production.

**Typical process validation protocol contents:** objective, scope, responsibilities, description of process and equipment, critical process parameters and quality attributes, sampling plan (where, how many, when), tests and acceptance criteria, number of batches, deviation handling, and report format.

### 5.4.4 Validation master plan (VMP)

A **VMP** is a high-level document that summarises the company's overall philosophy, intentions and approach to validation, and lists what will be validated, by whom and when.

**Contents of a VMP**

1. Introduction and validation policy of the site.
2. Scope: products, processes, facilities and systems covered.
3. Organisation: validation team and responsibilities.
4. Plant, process and product description (brief).
5. Specific process considerations: critical parameters.
6. List of items to be qualified or validated (facilities, utilities, equipment, processes, cleaning, methods, computer systems).
7. Key acceptance criteria.
8. Documentation format: protocols and reports, numbering.
9. Required SOPs.
10. Planning and scheduling (time plan, priorities).
11. Change control and revalidation policy.
12. Training needs.

## 5.5 Calibration of a pH meter

**Principle.** A pH meter measures the potential difference between a glass electrode (sensitive to H+ ions) and a reference electrode. The response is linear with pH; the theoretical slope is about 59.16 mV per pH unit at 25 °C. Calibration with standard buffers sets the zero point (intercept) and the slope.

**Standard buffers (commonly used, values at 25 °C)**

| Buffer | Approximate pH |
| --- | --- |
| Potassium hydrogen phthalate (0.05 M) | 4.01 |
| Mixed phosphate (equimolar KH2PO4 and Na2HPO4) | 6.86 |
| Sodium borate (borax, 0.01 M) | 9.18 |

Many laboratories also use commercial certified buffers of pH 4.00, 7.00 and 10.00. Use the pharmacopoeial values for the buffer and temperature in use.

**Procedure**

1. Switch on and allow to warm up as per the SOP; check the electrode is filled and clean.
2. Rinse the electrode with purified water and blot dry (do not rub).
3. Set the temperature or use automatic temperature compensation; buffers at about 25 °C.
4. Immerse in the neutral buffer (pH about 7) and standardise (set the zero/offset).
5. Rinse, immerse in the acidic buffer (pH about 4) and set the slope.
6. Rinse, immerse in the alkaline buffer (pH about 9.2) and check the reading (or set as third point).
7. Read each buffer again as a sample; the reading must agree with the stated value within the limit set in the SOP (commonly ±0.05 pH unit).
8. Record the slope; acceptance commonly 95–105% of theoretical (follow the SOP).
9. Record results and affix the calibration label. Daily calibration before use is usual; a full calibration with more checks is done at longer intervals.

**Precautions:** fresh buffers within expiry; do not pour used buffer back; keep the glass bulb wet (store in the recommended solution); calibrate with buffers that bracket the expected sample pH.

## 5.6 Qualification of a UV-visible spectrophotometer

The pharmacopoeia lists performance checks that show the instrument gives correct wavelength and absorbance readings. Exact limits must be taken from the current IP.

| Parameter | Usual method | What it shows |
| --- | --- | --- |
| Control of wavelength (wavelength accuracy) | Holmium oxide filter or holmium perchlorate solution (sharp peaks at known wavelengths, for example near 241, 287, 361 and 536 nm), or emission lines of a deuterium or mercury lamp | The wavelength scale is correct; tolerance is tighter in the UV range than in the visible range |
| Control of absorbance (photometric accuracy) | Potassium dichromate dried and dissolved in dilute sulfuric acid (about 0.005 M), read at 235, 257, 313 and 350 nm; specific absorbance compared with the stated values | Absorbance readings are accurate |
| Limit of stray light | Potassium chloride solution (about 1.2% w/v), absorbance read near 198–200 nm must be greater than a stated value (2.0) | Little light of other wavelengths reaches the detector, so high absorbances are reliable |
| Resolution (spectral bandwidth) | Toluene (0.02% v/v) in hexane: the ratio of absorbance at the maximum near 269 nm to the minimum near 266 nm must be not less than the stated value | The instrument can separate close peaks |
| Cells | Matched cuvettes checked with the same solvent | Cell errors are small |

**IQ** of the instrument covers delivery, installation, software and documents; **OQ** covers the tests above plus noise, baseline flatness and drift; **PQ** checks performance in routine use (for example a known standard measured regularly).

## 5.7 General principles of analytical method validation (ICH Q2(R2))

**Purpose:** to show that an analytical procedure is suitable for its intended use. The current guideline is ICH Q2(R2), adopted with the related guideline ICH Q14 on analytical procedure development; check ich.org for the version in force.

**Validation characteristics**

| Characteristic | Meaning | Usual approach |
| --- | --- | --- |
| Specificity / selectivity | Ability to measure the analyte without interference from impurities, degradants, excipients | Analyse placebo, spiked samples, stressed (degraded) samples; peak purity |
| Accuracy | Closeness of the result to the true value | Recovery of known amounts, commonly 3 levels × 3 replicates across the range |
| Precision | Closeness of results of repeated measurements | **Repeatability** (same analyst, short time: at least 9 determinations over the range or 6 at 100%), **intermediate precision** (different days, analysts, equipment), **reproducibility** (between laboratories); expressed as % RSD |
| Linearity (response) | Results proportional to concentration in the range | At least 5 concentrations; correlation coefficient, slope, intercept |
| Range | Interval between upper and lower concentration with suitable accuracy, precision and linearity | Assay typically 80–120% of the test concentration |
| Detection limit (DL/LOD) | Lowest amount that can be detected, not necessarily quantified | Signal-to-noise about 3:1 or DL = 3.3σ/S |
| Quantitation limit (QL/LOQ) | Lowest amount that can be quantified with suitable precision and accuracy | Signal-to-noise about 10:1 or QL = 10σ/S |
| Robustness | Reliability when method conditions vary slightly (pH of mobile phase, temperature, flow rate) | Studied during development (Q14) |

(σ = standard deviation of the response; S = slope of the calibration curve.)

**Which characteristics for which test**

| Type of test | Specificity | Accuracy | Precision | Linearity/range | DL | QL |
| --- | --- | --- | --- | --- | --- | --- |
| Identification | Yes | No | No | No | No | No |
| Impurities – quantitative | Yes | Yes | Yes | Yes | No | Yes |
| Impurities – limit test | Yes | No | No | No | Yes | No |
| Assay (content, dissolution) | Yes | Yes | Yes | Yes | No | No |

**System suitability tests** (for example resolution, tailing factor, plate count and repeatability of replicate injections in HPLC) are run with each analysis to show the system works on the day.

## 5.8 Warehousing: good warehousing practice (GWP)

A warehouse stores raw materials, packing materials and finished goods under conditions that keep their quality, and makes sure the right material goes out.

**Principles of GWP**

1. **Adequate space and design:** separate areas for receipt, quarantine, sampling, approved stock, rejected, returned and recalled goods; loading bays protected from weather.
2. **Storage conditions:** as stated on the label (room temperature, "store below 25 °C", 2–8 °C cold room, freezer). Warehouses are **temperature-mapped** to find hot and cold spots, and conditions are monitored and recorded continuously with alarms.
3. **Status control:** quarantine, approved and rejected status shown by labels or by a validated computer system.
4. **Stock rotation:** **FEFO** (first expiry, first out), or FIFO (first in, first out) where expiry is the same.
5. **Cleanliness and pest control:** pallets off the floor, gaps from walls, pest control records.
6. **Security:** restricted access; special secure storage for narcotics, psychotropics, high-value and printed materials; flammables in a separate store.
7. **Records:** receipts, issues, stock balance and reconciliation; physical stock checks at intervals.
8. **Handling:** materials not damaged during movement; spills cleaned at once with records; damaged containers segregated.
9. **Dispatch:** check the right product, batch and quantity; suitable vehicles; cold-chain packaging validated.

```text
Warehouse zones

[Receiving bay] -> [Quarantine] -> [Sampling booth] -> [Approved storage]
                                                         |   (FEFO issue)
                                                         v
 [Rejected - locked]   [Returned/recalled - locked]   [Dispensing / Issue]

[Cold room 2-8 °C]   [Flammables store]   [Secure store for controlled drugs]
[Finished goods quarantine] -> QA release -> [Finished goods store] -> [Dispatch bay]
```

## 5.9 Materials management

**Materials management** plans, buys, stores and controls materials so that the right material in the right quantity and quality is available at the right time and lowest total cost.

**Functions:** material planning, purchasing, receipt and inspection, storage, inventory control, issue, and disposal of surplus or obsolete stock.

**Inventory control techniques**

| Technique | Basis | Use |
| --- | --- | --- |
| ABC analysis | Annual consumption value. A items: few items (roughly 10–20%) taking most of the value (roughly 70%); B items: middle; C items: many items of low value | Tight control and frequent review for A items |
| VED analysis | Criticality: Vital, Essential, Desirable | Never run out of vital items (life-saving drugs, critical raw materials) |
| FSN analysis | Movement: Fast, Slow, Non-moving | Find dead stock to clear |
| HML analysis | Unit price: High, Medium, Low | Purchasing decisions |
| SDE analysis | Availability: Scarce, Difficult, Easy | Plan long lead-time items early |

**Key quantities**

- **Economic order quantity (EOQ):** the order size that keeps the total of ordering and holding costs lowest. EOQ = √(2DS/H), where D = annual demand (units), S = cost of placing one order, H = holding cost per unit per year.
  - Example: D = 10,000 units, S = ₹200 per order, H = ₹4 per unit per year → EOQ = √(2 × 10,000 × 200 / 4) = √1,000,000 = 1,000 units per order (10 orders a year).
- **Safety stock (buffer stock):** extra stock kept to cover delays or unexpected demand.
- **Reorder level:** stock level at which a new order is placed = (average daily use × lead time in days) + safety stock.
  - Example: use 100 units/day, lead time 15 days, safety stock 500 → reorder level = 1,500 + 500 = 2,000 units.
- **Maximum and minimum stock levels** set limits so that money is not tied up in excess stock and production never stops.

## Remember

- Calibrate instruments, qualify equipment (DQ → IQ → OQ → PQ), validate processes and methods.
- Calibration uses traceable standards; an out-of-calibration instrument triggers an impact assessment.
- Types of validation: prospective (preferred), concurrent (exceptional), retrospective (historical data), revalidation (after change); lifecycle: design → qualification → continued verification.
- VMP: policy, scope, responsibilities, list of items, acceptance criteria, schedule, change control.
- pH meter: buffers about 4.01, 6.86, 9.18 at 25 °C; slope about 59.16 mV/pH at 25 °C.
- UV-visible checks: wavelength (holmium), absorbance (potassium dichromate), stray light (KCl), resolution (toluene in hexane).
- Method validation (ICH Q2(R2)): specificity, accuracy, precision, linearity, range, DL (3.3σ/S), QL (10σ/S), robustness.
- GWP: zones, status labels, temperature mapping, FEFO, security, records. EOQ = √(2DS/H); reorder level = use × lead time + safety stock.
