# Unit 3: Calibration and validation of instruments

A result is only as trustworthy as the instrument that produced it. A balance that reads 0.5% high or a spectrophotometer whose wavelength has drifted by 3 nm will pass or fail batches wrongly, and regulators treat that as a serious GMP failure. This unit explains the vocabulary (calibration, qualification, validation), the ICH and US FDA expectations, the parameters used to validate an analytical method, and how each common laboratory instrument is calibrated.

## 3.1 Key terms

| Term | Meaning | Example |
| --- | --- | --- |
| **Calibration** | Comparing an instrument's readings with a traceable standard of known value over its working range, and adjusting or recording the error | Checking a balance with certified weights; checking UV wavelength with holmium |
| **Qualification** | Documented proof that equipment is correctly designed, installed, operates and performs as intended | DQ, IQ, OQ, PQ of a new HPLC |
| **Validation** | Documented evidence giving a high degree of assurance that a process, method or system consistently produces a result meeting its predetermined specifications | Validating an HPLC assay method; validating a granulation process |
| **Verification** | Confirming that an already validated (for example pharmacopoeial) method works in your laboratory | Running accuracy and precision on an IP method |
| **Traceability** | An unbroken chain of comparisons linking a measurement to national or international standards | Weights certified against national standards |
| **System suitability test (SST)** | A check, run with each analysis, that the whole system (instrument + column + method) is working on that day | Resolution, tailing, RSD of replicate injections |

**Calibration vs validation.** Calibration checks **one instrument's accuracy** against standards; validation shows that a **process or method** is fit for purpose. An instrument must be qualified and calibrated before any method on it can be validated.

## 3.2 Regulatory basis

- **ICH guidelines** (International Council for Harmonisation):
  - **Q2(R1) "Validation of Analytical Procedures: Text and Methodology"**, now revised as **Q2(R2)**, together with **Q14** on analytical procedure development. These define the validation characteristics used worldwide.
  - **Q7** (GMP for active pharmaceutical ingredients) requires calibrated equipment and validated processes.
  - Q8 (pharmaceutical development), Q9 (quality risk management) and Q10 (pharmaceutical quality system) support a risk-based, lifecycle approach.
- **US FDA:**
  - **21 CFR Part 211** (cGMP for finished pharmaceuticals): equipment must be routinely calibrated, inspected or checked according to a written programme (§211.68), and laboratory controls must include calibration of instruments at suitable intervals with specifications, limits and remedial action (§211.160).
  - **Guidance for Industry: Process Validation — General Principles and Practices (2011):** a lifecycle with three stages: **Stage 1 process design, Stage 2 process qualification, Stage 3 continued process verification.**
  - **Guidance on Analytical Procedures and Methods Validation** (2015).
  - **21 CFR Part 11:** electronic records and signatures for computerised instruments (audit trail, access control).
- **USP general chapter <1058> Analytical Instrument Qualification** describes the 4Q model and classifies instruments by complexity.
- In India, **Schedule M** of the Drugs Rules requires calibrated equipment and validated processes, following WHO GMP.

## 3.3 Qualification of equipment (the 4Q model)

```text
  DQ ────────> IQ ────────> OQ ────────> PQ ────────> routine use with
 (right design) (installed    (works over   (works for the   calibration, maintenance,
                 correctly)    its ranges)   real method)    requalification after change
```

| Stage | Question answered | Typical checks |
| --- | --- | --- |
| **Design qualification (DQ)** | Is this the right instrument for our needs? | User requirement specification (URS), vendor selection, specifications match intended use |
| **Installation qualification (IQ)** | Has it been delivered and installed correctly? | Components against purchase order, site (power, gas, environment), software version, manuals, connections, serial numbers |
| **Operational qualification (OQ)** | Does it work as specified over its operating range? | Wavelength accuracy, flow-rate accuracy, temperature accuracy, detector linearity, alarms |
| **Performance qualification (PQ)** | Does it consistently perform for the intended analysis? | Running real or standard samples under routine conditions; system suitability over time |

Requalification is done after major repair, relocation or software upgrade, and periodically as per SOP.

## 3.4 Validation: types and lifecycle

**Process validation types (traditional classification)**

| Type | When done | Note |
| --- | --- | --- |
| **Prospective** | Before the product is sold; usually on consecutive validation batches | Preferred for new products |
| **Concurrent** | During routine production, batches released as they are validated | Used in special cases (limited batches, urgent need) |
| **Retrospective** | Using historical data of batches already made | No longer generally accepted for new products |
| **Revalidation** | After changes in formula, equipment, site or process, or periodically | Triggered by change control |

**Validation master plan (VMP):** the top document listing what will be validated, by whom, how and when. Each validation has a **protocol** (approved before work starts, with acceptance criteria) and a **report** (results, deviations, conclusion).

## 3.5 Analytical method validation (ICH Q2)

**Validation characteristics**

| Characteristic | Definition | How it is usually shown |
| --- | --- | --- |
| **Specificity** | Ability to measure the analyte unequivocally in the presence of impurities, degradants and matrix | Placebo and spiked samples; forced degradation (acid, base, oxidation, heat, light); peak purity with a PDA detector; resolution from nearest peak |
| **Accuracy** | Closeness of the result to the true value | % recovery of known amounts spiked into placebo; at least 9 determinations over 3 levels (for example 80, 100, 120%, 3 replicates each) |
| **Precision** | Closeness of agreement among repeated results (expressed as SD or RSD) | See the three levels below |
| – Repeatability | Same analyst, same day, same instrument | At least 9 determinations over the range, or 6 at 100% |
| – Intermediate precision | Within one laboratory: different days, analysts, instruments | Compare RSD across the variations |
| – Reproducibility | Between laboratories | Collaborative studies; for standardising methods |
| **Detection limit (LOD)** | Lowest amount that can be detected, not necessarily quantified | Signal-to-noise about 3 : 1, or 3.3σ/S |
| **Quantitation limit (LOQ)** | Lowest amount that can be measured with acceptable accuracy and precision | Signal-to-noise about 10 : 1, or 10σ/S |
| **Linearity** | Results directly proportional to concentration within a range | At least 5 concentrations; regression line, correlation coefficient, slope, intercept, residuals |
| **Range** | Interval between upper and lower concentration with suitable accuracy, precision and linearity | Assay: usually 80–120% of test concentration; content uniformity 70–130%; dissolution ±20% over the specified range; impurities from reporting level to 120% of the limit |
| **Robustness** | Capacity to stay unaffected by small deliberate changes | Vary pH, mobile-phase ratio, flow rate, column temperature, column lot, wavelength |

In LOD and LOQ, σ is the standard deviation of the response (of the blank or of the y-intercept) and S is the slope of the calibration line.

**Which characteristics are needed?**

| Characteristic | Identification | Impurity: quantitative | Impurity: limit test | Assay (content, dissolution) |
| --- | --- | --- | --- | --- |
| Accuracy | − | + | − | + |
| Repeatability | − | + | − | + |
| Intermediate precision | − | + | − | + |
| Specificity | + | + | + | + |
| Detection limit | − | − (may be needed) | + | − |
| Quantitation limit | − | + | − | − |
| Linearity | − | + | − | + |
| Range | − | + | − | + |

**Worked example 1: LOD and LOQ.** A UV calibration line has slope S = 0.052 absorbance per µg/ml, and the standard deviation of the blank response is σ = 0.0021.
LOD = 3.3 × 0.0021/0.052 = **0.13 µg/ml**; LOQ = 10 × 0.0021/0.052 = **0.40 µg/ml**.

**Worked example 2: accuracy.** Placebo spiked with 10.00 mg of drug; found 9.87 mg. Recovery = 9.87/10.00 × 100 = **98.7%**.

**Worked example 3: repeatability.** Six assays at 100% give 99.6, 100.4, 99.1, 100.8, 100.2 and 99.5% of label claim. Mean = 99.93%; SD = 0.64; **RSD = SD/mean × 100 = 0.64%**, well within a typical limit of 2% for an assay.

**System suitability (chromatographic methods).** Before each run, a standard is injected and typical checks are made: resolution between the critical pair (baseline separation needs Rs of at least 1.5; many methods ask for 2), tailing factor (commonly not more than 2), theoretical plates (N), and RSD of replicate standard injections (commonly not more than 2% for 5–6 injections). Exact limits are written in each monograph or method.

## 3.6 General calibration programme

1. A **master list** of instruments, each with a unique ID and calibration frequency.
2. **Written SOP** for each instrument: standards, procedure, acceptance limits, frequency (daily check, monthly, six-monthly, after repair).
3. **Certified reference standards** traceable to national standards.
4. **Records:** date, standards used, readings, pass/fail, signature, next due date.
5. **Status label** on the instrument ("Calibrated on … Due on …"; "Under maintenance; do not use").
6. **Out-of-calibration action:** remove from use, investigate the impact on results since the last good calibration, repair, recalibrate, and record the deviation.

## 3.7 Calibration of an electronic balance

**Before calibration:** place on a firm, vibration-free bench away from draughts and direct sunlight; check the level bubble; switch on and allow warm-up; clean the pan; use tweezers to handle weights; use certified weights of suitable accuracy class (for example OIML E2 or F1).

| Test | Procedure | What it detects |
| --- | --- | --- |
| **Daily check (sensitivity / accuracy)** | Weigh one or two certified weights (for example near the usual load) after internal or external adjustment | Drift in span |
| **Repeatability** | Weigh the same weight about 10 times, taring between readings; calculate SD | Random scatter |
| **Eccentricity (corner load)** | Place a weight in the centre, then at four corners of the pan; compare | Error when sample is off-centre |
| **Linearity** | Weigh certified weights across the range (for example 10%, 25%, 50%, 100% of capacity) | Non-proportional response |
| **Minimum weight** | From the repeatability SD | Smallest sample that can be weighed accurately |

**USP <41> criteria (used widely for analytical weighing):**
- Repeatability is satisfactory if 2 × SD / (smallest net weight intended) ≤ 0.10%. If the SD is below 0.41d (d = readability), 0.41d is used instead.
- Accuracy is satisfactory if the weight reading is within 0.10% of the test weight's value.

**Worked example: minimum weight.** A balance with readability d = 0.01 mg gives SD = 0.008 mg for 10 weighings. Because 0.008 is greater than 0.41 × 0.01 = 0.0041, use 0.008. Minimum weight = 2 × 0.008/0.001 = **16 mg**. Samples below 16 mg should not be weighed on this balance for assays.

## 3.8 Calibration of a UV-visible spectrophotometer

The Indian Pharmacopoeia and other pharmacopoeias prescribe these checks:

| Parameter | Standard | Procedure and acceptance |
| --- | --- | --- |
| **Control of wavelength** | Holmium perchlorate solution (maxima at 241.15, 287.15, 361.5 and 536.3 nm), holmium oxide glass filter, mercury lamp lines, or the deuterium lamp lines at 486.0 and 656.1 nm | Scan and note peak positions. Permitted tolerance: ±1 nm in the ultraviolet and ±3 nm in the visible region |
| **Control of absorbance (photometric accuracy)** | Potassium dichromate dried to constant weight at 130 °C; about 57–63 mg dissolved in 0.005 M H2SO4 and diluted to 1000 ml | Measure absorbance at 235, 257, 313 and 350 nm and calculate A(1%, 1 cm). Nominal values: about 124.5, 144.5, 48.6 and 106.6 respectively, each within the narrow range given in the pharmacopoeia |
| **Limit of stray light** | Potassium chloride 1.2% w/v in water | Absorbance at about 200 nm (1 cm cell, water as blank) should be greater than 2.0 |
| **Resolution (spectral bandwidth)** | Toluene 0.02% v/v in hexane | Ratio of absorbance at the maximum near 269 nm to the minimum near 266 nm should be at least 1.5 |
| **Cells** | Fill matched cells with the same solvent | Absorbance difference within the tolerance in the SOP; clean, unscratched, quartz below about 350 nm |
| **Baseline flatness, noise, drift** | Air or solvent vs solvent | As per manufacturer and SOP |

**Why each test matters:** wrong wavelength puts you off the λmax, where absorbance changes steeply; wrong absorbance scale gives wrong assays directly; stray light makes high absorbances read too low (negative deviation from Beer's law); poor resolution flattens sharp bands.

## 3.9 Calibration of an IR spectrophotometer

| Parameter | Standard | Procedure |
| --- | --- | --- |
| **Wavenumber accuracy** | Polystyrene film (about 35 µm thick) | Record the spectrum; check positions of reference bands such as 3060.0, 2849.5, 1942.9, 1601.2, 1583.0, 1154.5 and 1028.3 cm⁻¹ within the tolerances given in the pharmacopoeia (about ±1 to ±2 cm⁻¹) |
| **Resolution** | Polystyrene film | Depth of the trough between closely spaced bands (for example between 2870 and 2849.5 cm⁻¹, and between 1589 and 1583 cm⁻¹) in %T must exceed the stated values |
| **Transmittance (100% line), noise** | Empty beam | Flat line near 100% T; noise within limits |
| **Energy / throughput** | Single-beam energy at set wavenumbers (FTIR) | Compared with installation values to check source and detector ageing |

Keep the KBr, cells and instrument dry: water vapour and CO2 bands (near 3700, 1600 and 2350 cm⁻¹) are a common source of error. FTIR instruments also run an internal laser reference that keeps the wavenumber scale accurate.

## 3.10 Calibration of a fluorimeter

| Parameter | Standard | Procedure |
| --- | --- | --- |
| **Wavelength accuracy** | Xenon or mercury lamp emission lines; Raman band of water | With excitation at 350 nm, the water Raman band appears near 397 nm (the O–H stretch of about 3400 cm⁻¹ subtracted from the excitation wavenumber: 28,571 − 3400 = 25,171 cm⁻¹ → about 397 nm). Its position checks the emission scale |
| **Sensitivity (signal-to-noise)** | Water Raman band | Ratio of the Raman peak to the noise must exceed the manufacturer's value |
| **Linearity of response** | **Quinine sulfate** in 0.05 M (0.1 N) H2SO4 at several concentrations; excitation about 350 nm, emission about 450 nm | Plot fluorescence vs concentration; check the correlation coefficient; check the low-concentration range, since self-absorption bends the line at high concentration |
| **Stability** | Standard solution read over time | Drift within limits |
| **Blank** | Solvent and cell | Low, constant background; clean, fluorescence-free cells |

Halides quench quinine fluorescence, so the dilutions must be made in sulfuric acid, not hydrochloric acid.

## 3.11 Calibration of a flame photometer

1. Check gas supply, air pressure and flame steadiness; let the burner warm up.
2. Check the filters: sodium at 589 nm, potassium at 766 nm (lithium at 671 nm if used).
3. Aspirate distilled water and set zero; aspirate the top standard and set full scale.
4. **Linearity:** aspirate a series of standard solutions of NaCl or KCl (for example 10–100 ppm of the metal) and plot emission vs concentration; the working range must be linear (self-absorption bends the curve at high concentration).
5. **Repeatability:** aspirate one standard several times; RSD within the SOP limit.
6. **Interference check:** measure sodium in the presence of potassium and vice versa; mutual excitation and ionisation can raise or lower readings.
7. **Response time and drift:** re-check zero and the top standard after every few samples and at the end.

## 3.12 Calibration of HPLC

Each module is calibrated separately and then the system as a whole.

| Module | Parameter | Typical method (limits as per SOP or manufacturer) |
| --- | --- | --- |
| **Pump** | Flow-rate accuracy | Pump water or methanol at set flows (for example 0.5, 1.0, 2.0 ml/min); collect into a volumetric flask and time it, or weigh the eluate; measured flow commonly within ±2% of set value |
| | Flow precision | RSD of retention times of repeated injections |
| | Gradient composition accuracy | Channel A water, channel B water containing a UV tracer (acetone or caffeine); run step gradients (for example 10, 50, 90% B) and compare step heights with expected values |
| | Pressure test | Block the outlet and check pressure holding (leak test) |
| **Injector / autosampler** | Precision | 6 injections of a standard; RSD of peak area (commonly not more than 1%) |
| | Linearity of injection volume | Inject different volumes; area vs volume should be linear |
| | Carry-over | Inject blank after a concentrated standard; peak in blank below a set % |
| **Detector (UV/PDA)** | Wavelength accuracy | Caffeine solution (maxima near 205 and 273 nm) or built-in holmium filter |
| | Linearity | Caffeine solutions over the range; correlation coefficient close to 1 |
| | Noise and drift | Mobile phase flowing, no injection, over a fixed time |
| **Column oven** | Temperature accuracy | Calibrated thermometer or probe at set temperatures; commonly within ±2 °C |
| **Whole system** | System suitability | Plates, tailing, resolution, RSD with a test mixture |

## 3.13 Calibration of GC

| Part | Parameter | Method |
| --- | --- | --- |
| **Carrier gas** | Flow-rate accuracy | Bubble flowmeter or digital flowmeter at the column or detector outlet; compare with set flow |
| **Oven** | Temperature accuracy and stability | Calibrated probe at several set temperatures; check isothermal stability and programmed ramp rate |
| **Injector** | Temperature; split ratio; injection precision | Probe; replicate injections of a standard (for example a mixture of n-alkanes or a solvent mixture); RSD of area and retention time |
| **Detector (FID)** | Sensitivity and linearity | Inject a series of concentrations of a test compound; check detector response, noise and linear range; check hydrogen and air flows |
| **Whole system** | Retention time reproducibility, resolution | Test mixture with known peaks |

Leak checks of the gas lines and septum and replacement of the septum and liner are part of routine GC maintenance.

## Remember

- Calibration = instrument vs traceable standard; qualification = DQ, IQ, OQ, PQ; validation = documented evidence a method or process works consistently.
- ICH Q2(R1)/Q2(R2) parameters: specificity, accuracy, precision (repeatability, intermediate, reproducibility), LOD, LOQ, linearity, range, robustness.
- LOD = 3.3σ/S; LOQ = 10σ/S; assay range 80–120%; at least 5 levels for linearity, 9 determinations for accuracy.
- US FDA: 21 CFR 211.68 and 211.160; 2011 process validation = design, qualification, continued verification.
- Balance: repeatability, eccentricity, linearity; USP <41>: 2 × SD/weight ≤ 0.10%; minimum weight = 2000 × SD.
- UV: holmium (wavelength), potassium dichromate (absorbance), KCl (stray light), toluene in hexane (resolution, ratio ≥ 1.5).
- IR: polystyrene film; fluorimeter: quinine sulfate and water Raman band; flame: NaCl and KCl standards.
- HPLC: flow rate, gradient, injector precision, detector wavelength and linearity, oven temperature; GC: gas flow, oven temperature, injector, FID linearity.
