# Unit 5: Drug product performance in vivo — bioavailability, bioequivalence, BCS and biosimilars

This unit covers syllabus Unit 4: the purpose and methods of bioavailability (BA) studies, design and statistical evaluation of bioequivalence (BE) studies, the submission and review process, the Biopharmaceutics Classification System (BCS) with permeability methods, generic biologics (biosimilars), clinical significance and special concerns of BE, and generic substitution.

Worked examples use example numbers for hypothetical drugs. They are not values for any real medicine.

## 5.1 Drug product performance in vivo

**Bioavailability:** the rate and extent to which the active ingredient is absorbed from a drug product and becomes available at the site of action (in practice, the systemic circulation).

**Bioequivalence:** the absence of a significant difference in the rate and extent of availability of the active ingredient from pharmaceutical equivalents (or pharmaceutical alternatives) given at the same molar dose under similar conditions in an appropriately designed study.

| Term | Meaning |
| --- | --- |
| Pharmaceutical equivalents | Same active ingredient, same amount, same dosage form, same route, meeting the same standards; excipients may differ |
| Pharmaceutical alternatives | Same active moiety but different salt, ester, dosage form or strength |
| Therapeutic equivalents | Pharmaceutical equivalents that are bioequivalent and so expected to have the same clinical effect and safety |
| Reference product | Usually the innovator (comparator) product approved on full data |
| Test product | The new or generic product being compared |

## 5.2 Purpose of bioavailability studies

1. **New drug development:** absolute bioavailability, dose proportionality, food effect, first-pass loss, choice of formulation for later trials.
2. **New formulations of an existing drug:** comparing a capsule used in trials with the final tablet ("bridging").
3. **Generic products:** BE to the reference product replaces new clinical efficacy trials.
4. **Post-approval changes:** change of manufacturing site, process, equipment or composition may need BE or a dissolution-based waiver.
5. **Modified-release products:** check that release and absorption are as designed, and that no dose dumping occurs (especially with food or alcohol).
6. **Special populations and interactions:** effect of age, disease or co-administered drugs on absorption.

## 5.3 Relative and absolute availability

**Absolute bioavailability** compares an extravascular product with an IV dose (F of IV = 1):

F = (AUCoral × DoseIV) / (AUCIV × Doseoral)

**Relative bioavailability** compares two extravascular products (for example test tablet vs reference solution or reference tablet):

Frel = (AUCtest × Doseref) / (AUCref × Dosetest)

Urinary data give the same ratios using Xu∞ (total unchanged drug excreted).

Dose correction assumes linear kinetics; if the doses differ widely and kinetics may be nonlinear, equal doses should be used.

**Worked example 1 (example numbers, Drug X):** 500 mg oral gives AUC0–∞ = 93.67 mg·h/L; 250 mg IV gives 57.70 mg·h/L.
F = (93.67 × 250)/(57.70 × 500) = **0.81**.

## 5.4 Methods for assessing bioavailability

| Method | Measures | Comments |
| --- | --- | --- |
| Plasma (blood) concentration–time data | AUC (extent), Cmax and tmax (rate) | Preferred and most widely used |
| Urinary excretion data | Cumulative amount excreted Xu∞ (extent), maximum excretion rate and its time (rate) | When the drug is excreted largely unchanged and plasma assay is difficult; needs complete urine collection |
| Acute pharmacological (pharmacodynamic) effect | Effect–time curve (for example pupil size, blood glucose, gastric pH) | When drug levels cannot be measured reliably but a quantitative, reproducible response exists |
| Comparative clinical endpoint trials | Therapeutic outcome | Least sensitive and most expensive; used for locally acting products |
| In vitro dissolution | Dissolution profiles | Can replace in vivo studies only under biowaiver rules (BCS, additional strengths, IVIVC) |

Plasma parameters:

- **AUC0–t** (to the last measurable concentration) and **AUC0–∞**: extent of absorption.
- **Cmax:** reflects both rate and extent.
- **tmax:** rate; read directly from the data (depends on sampling times).
- Partial AUC (for example AUC to the reference tmax) is sometimes required for products where early exposure matters.

## 5.5 Bioequivalence studies: design

### Choice of design

| Design | When used | Features |
| --- | --- | --- |
| Two-period, two-sequence, two-treatment crossover (2 × 2: TR/RT) | Standard design for most immediate-release products | Each subject is their own control, so between-subject variability is removed; needs a washout |
| Parallel | Very long half-life drugs (long washout impractical), studies in patients, drugs causing lasting effects | Two separate groups; more subjects needed |
| Replicate crossover (partial: TRR/RTR/RRT; full: TRTR/RTRT) | Highly variable drugs (within-subject CV of 30% or more) and narrow therapeutic index drugs | Estimates within-subject variance of the reference, allowing reference-scaled limits |
| Multiple-dose (steady-state) | Some modified-release products, drugs too toxic for healthy volunteers, nonlinear drugs | Uses AUCτ, Css,max, Css,min |
| Higher-order crossover (3 × 3, Williams designs) | Comparing more than two products | |

```text
 2 × 2 crossover
            Period 1          washout          Period 2
 Seq 1:   Test (T)   ───── ≥ 5 t½ ─────►   Reference (R)
 Seq 2:   Reference  ───── ≥ 5 t½ ─────►   Test
```

### Key elements of a BE protocol

1. **Subjects:** healthy adult volunteers (usually 18 years or older) of both sexes where possible, screened by history, examination and laboratory tests; non-smokers or as defined; patients only when the drug is unsafe for volunteers. Number set by sample-size calculation (at least 12 under most guidelines); extra subjects allowed for dropouts. Written informed consent and ethics committee approval are mandatory.
2. **Randomisation** to sequences; blinding of the bioanalytical laboratory where possible.
3. **Washout:** at least 5 elimination half-lives of the drug (or active metabolite) between periods; pre-dose levels in period 2 should be below about 5% of Cmax.
4. **Standardised conditions:** fasting overnight (about 10 h) for fasting studies, standard high-fat, high-calorie meal for fed studies; fixed water volume (about 240 mL); controlled posture, fluid intake, alcohol, caffeine and other drugs.
5. **Single dose** of the highest strength normally (unless safety or linearity requires otherwise).
6. **Sampling:** about 12–18 samples per period, dense around tmax, continued for at least 3 terminal half-lives so that AUC0–t is at least 80% of AUC0–∞; for long half-life drugs AUC0–72h may be used.
7. **Analyte:** normally the parent drug in plasma; metabolites when the parent cannot be measured or is a prodrug; enantiomers for some chiral drugs.
8. **Bioanalysis:** validated method (selectivity, accuracy, precision, linearity, sensitivity, stability, carry-over, matrix effect; ICH M10).
9. **Safety monitoring** and adverse event reporting.

## 5.6 Evaluation of the data: statistics of bioequivalence

### Why log-transform?

- AUC and Cmax are positive and right-skewed; logs give near-normal distributions.
- The model is multiplicative (a formulation changes exposure by a fraction), which becomes additive on the log scale.
- Equivalence limits 80% and 125% are symmetric on the log scale: ln 0.80 = −0.223, ln 1.25 = +0.223.

### Analysis of variance (2 × 2 crossover)

ln(response) = overall mean + sequence + subject (within sequence) + period + treatment + residual error

The residual mean square (MSE) is the within-subject variance σ²W. Intra-subject CV = √(e^MSE − 1).

### The 90% confidence interval and two one-sided tests

Average bioequivalence is accepted if the **90% confidence interval for the ratio of geometric means (test/reference)** of AUC and Cmax lies entirely within **80.00–125.00%**.

90% CI on log scale = (mean T − mean R) ± t(0.95, df) × SE

This is identical to **Schuirmann's two one-sided tests (TOST)**, each at α = 0.05: H01: ratio ≤ 0.80 and H02: ratio ≥ 1.25; both must be rejected. The consumer's risk of wrongly declaring BE is at most 5%.

- **tmax** is usually compared by non-parametric methods and is not normally a pass/fail criterion.
- **Narrow therapeutic index drugs:** tighter limits (often 90.00–111.11% for AUC, and for Cmax under some guidelines).
- **Highly variable drugs:** with a replicate design, the Cmax limits may be widened in proportion to the reference variability (EMA: up to 69.84–143.19% when CV is 50% or more; US FDA uses reference-scaled average BE), with a point estimate within 80–125%.

### Worked example 2 — 90% CI for AUC (example numbers)

Twelve subjects in a 2 × 2 crossover (6 per sequence). AUC0–∞ in mg·h/L; d = ln T − ln R.

| Subject | Sequence | AUC T | AUC R | d |
| --- | --- | --- | --- | --- |
| 1 | TR | 82 | 95 | −0.1472 |
| 2 | TR | 108 | 96 | 0.1178 |
| 3 | TR | 70 | 84 | −0.1823 |
| 4 | TR | 99 | 90 | 0.0953 |
| 5 | TR | 104 | 124 | −0.1759 |
| 6 | TR | 80 | 91 | −0.1288 |
| 7 | RT | 93 | 104 | −0.1118 |
| 8 | RT | 126 | 115 | 0.0913 |
| 9 | RT | 78 | 95 | −0.1972 |
| 10 | RT | 96 | 86 | 0.1100 |
| 11 | RT | 101 | 114 | −0.1211 |
| 12 | RT | 104 | 96 | 0.0800 |

Steps (period effect removed by averaging the two sequence means):

1. Mean d in sequence TR = −0.0702; in sequence RT = −0.0248.
2. Point estimate of ln(GMR) = (−0.0702 + −0.0248)/2 = **−0.0475** → GMR = e^−0.0475 = **95.36%**.
3. Pooled variance of d within sequences: sum of squares 0.1850 with 10 df → s²d = 0.01850; MSE = s²d/2 = 0.00925.
4. SE = √[(s²d/4) × (1/6 + 1/6)] = **0.0393**.
5. t(0.95, 10) = 1.8125 → 90% CI on log scale = −0.0475 ± 0.0712 = −0.1187 to 0.0237.
6. Back-transform: **88.81% to 102.40%**, inside 80.00–125.00% → bioequivalent for AUC (Cmax must also pass).
7. Intra-subject CV = √(e^0.00925 − 1) = **9.6%**.

### Sample size and power

The number of subjects depends on the expected within-subject CV, the expected GMR (usually 0.95), the limits and the desired power (80–90%). Higher CV or a GMR further from 1 needs more subjects; for CVs above about 30%, replicate designs with scaled limits keep studies feasible. Under-powered studies fail even with truly equivalent products.

### Bioequivalence example: interpretation of failures

- CI entirely outside 80–125%: products are bioinequivalent.
- CI straddling a limit (for example 78–99%): equivalence not shown; the study may be under-powered or the products differ.
- Check outliers, protocol deviations, period or carry-over effects (pre-dose concentrations), and analytical problems. Subjects cannot be excluded simply because their results are unfavourable.

## 5.7 Study submission and drug review process

**General flow**

```text
 Protocol + investigator's brochure ─► ethics committee approval ─► regulatory permission
   ─► trial registration ─► clinical conduct ─► bioanalysis ─► PK and statistical analysis
   ─► clinical study report ─► dossier (CTD) ─► regulatory review (and inspection)
   ─► approval / queries
```

**India**

- The Central Drugs Standard Control Organisation (CDSCO), headed by the Drugs Controller General (India), regulates BA/BE studies under the Drugs and Cosmetics Act, 1940 and the New Drugs and Clinical Trials Rules, 2019.
- BA/BE studies need regulatory permission, approval of a registered ethics committee, and registration in the Clinical Trials Registry – India (CTRI) before enrolment. BA/BE study centres must be registered with the licensing authority.
- CDSCO's "Guidelines for Bioavailability and Bioequivalence Studies" (2005) describe design, conduct and evaluation; good clinical practice (Indian GCP and ICH E6) and good laboratory practice apply.
- The application for a generic (or new formulation) includes CMC data, comparative dissolution and the BE study report in Common Technical Document format (Module 2 summaries, Module 3 quality, Module 5 clinical study reports).
- Inspection of the clinical and bioanalytical sites may be carried out.

**United States (for comparison):** generics are filed as an abbreviated new drug application (ANDA) referring to a reference listed drug; FDA's Office of Generic Drugs reviews BE, chemistry and labelling; approved therapeutic equivalents are listed in the "Orange Book" with codes (an "AB" rating means BE has been shown). FDA publishes product-specific guidances describing the BE study expected for each drug.

## 5.8 The Biopharmaceutics Classification System (BCS)

Proposed by Amidon and co-workers (1995); now harmonised in **ICH M9 (2019)** for biowaivers.

| Class | Solubility | Permeability | Absorption-limiting factor | Typical formulation approach |
| --- | --- | --- | --- | --- |
| I | High | High | Gastric emptying | Conventional; biowaiver possible |
| II | Low | High | Dissolution | Particle size reduction, salts, solid dispersions, lipid systems, nanocrystals |
| III | High | Low | Permeability | Permeation enhancers, prodrugs; biowaiver possible with strict excipient rules |
| IV | Low | Low | Both | Difficult; often parenteral or major reformulation |

**Definitions (ICH M9)**

- **High solubility:** the highest single therapeutic dose dissolves completely in 250 mL or less of aqueous media over pH 1.2–6.8 at 37 ± 1 °C (tested at pH 1.2, 4.5, 6.8 and the pH of lowest solubility if within the range).
- **High permeability:** extent of absorption (fa) in humans of 85% or more, from mass-balance or absolute bioavailability studies; supportive in vitro data (validated Caco-2) can be used.
- **Very rapidly dissolving:** 85% or more in 15 min; **rapidly dissolving:** 85% or more in 30 min, in pH 1.2, 4.5 and 6.8 media, 900 mL or less, paddle at 50 rpm or basket at 100 rpm.

**BCS-based biowaiver (ICH M9)**

- Class I: drug product very rapidly or rapidly dissolving (f2 comparison needed if only rapidly dissolving).
- Class III: drug product very rapidly dissolving, and excipients qualitatively the same and quantitatively very similar to the reference.
- Not applicable to narrow therapeutic index drugs, buccal or sublingual products, or where excipients may affect absorption (for example certain sugar alcohols, surfactants in large amounts).

**Dimensionless numbers behind the BCS**

- **Dose number** D0 = (M0/V0)/Cs, with V0 = 250 mL; D0 ≤ 1 means high solubility.
- **Dissolution number** Dn = time in the intestine / time to dissolve; Dn ≥ 1 means dissolution is fast enough.
- **Absorption number** An = Peff × residence time / radius; An ≥ 1 means permeation is fast enough.

**Example (example numbers):** a 200 mg dose of a drug whose lowest solubility between pH 1.2 and 6.8 is 0.05 mg/mL: D0 = (200/250)/0.05 = 16 → low solubility. A 100 mg dose of a drug soluble at 1 mg/mL: D0 = 0.4 → high solubility.

**Related system:** the Biopharmaceutics Drug Disposition Classification System (BDDCS, Wu and Benet) replaces permeability with extent of metabolism (70% or more metabolised = high permeability class) and predicts the role of transporters and food effects.

### Permeability for BCS: in vitro, in situ and in vivo methods (summary)

(Details in Unit 1, section 1.8.)

- **In vivo (preferred):** mass balance with labelled drug; absolute bioavailability; human intestinal perfusion (Loc-I-Gut) giving Peff.
- **In situ:** rat single-pass intestinal perfusion with marker correction.
- **In vitro:** Caco-2 monolayers validated with a set of model drugs of known human absorption, showing a rank-order relationship; PAMPA for passive screening only. Efflux must be considered; the method must be shown to be suitable.

## 5.9 Generic biologics (biosimilar drug products)

A **biosimilar** ("similar biologic" in India) is a biological product highly similar in quality, safety and efficacy to an already approved reference biologic, with no clinically meaningful differences.

**Why BE alone is not enough**

- Large, complex molecules (proteins, glycoproteins, antibodies) made in living cells; the structure (folding, glycosylation, charge variants, aggregates) depends on the cell line and process, so "the process is the product".
- Two products cannot be shown identical; only highly similar.
- Immunogenicity can differ and cannot be predicted from structure alone.
- PK often nonlinear (target-mediated, Unit 6).

**Stepwise comparability exercise**

```text
 Extensive analytical characterisation (structure, function, impurities) — the foundation
        │
 Non-clinical studies (in vitro bioassays, receptor binding; animal studies only if needed)
        │
 Comparative PK (and PD) study, usually in healthy volunteers or patients
        │
 Confirmatory comparative clinical efficacy and safety trial (equivalence margins), when needed
        │
 Immunogenicity assessment (anti-drug antibodies, neutralising antibodies)
        │
 Post-marketing risk management and pharmacovigilance
```

- PK comparison of biosimilars uses the same log-scale 90% CI approach (often 80–125%) for AUC and Cmax.
- **Extrapolation** of indications is possible with scientific justification (same mechanism of action).
- **Interchangeability** (automatic substitution) needs additional evidence in some jurisdictions.
- **India:** "Guidelines on Similar Biologics" issued by CDSCO and the Department of Biotechnology (2012, revised 2016) set the regulatory pathway; the Review Committee on Genetic Manipulation (RCGM) oversees preclinical aspects.

## 5.10 Clinical significance of bioequivalence studies

- BE studies are a **surrogate** for clinical trials: if exposure is equivalent, efficacy and safety are expected to be equivalent (therapeutic equivalence = pharmaceutical equivalence + bioequivalence).
- They allow affordable generics with confidence in quality, and safe post-approval changes.
- Failures in history (products with poor bioavailability causing toxicity or failure when formulation changed, such as the classic phenytoin and digoxin formulation problems of the 1960s–70s) are why BE requirements exist.
- Limits of 80–125% describe the CI, not the allowed difference between products: real approved generics usually differ from the reference by only a few percent in mean exposure.
- For narrow therapeutic index drugs, even small differences matter: tighter limits, monitoring when switching.

## 5.11 Special concerns in bioavailability and bioequivalence studies

| Situation | Concern | Approach |
| --- | --- | --- |
| Highly variable drugs (CV ≥ 30%) | Very large sample size | Replicate design, reference-scaled limits |
| Narrow therapeutic index drugs | Small changes cause toxicity or failure | Tightened limits (90–111%), sometimes replicate design to compare variances |
| Long half-life drugs | Very long washout | Parallel design; truncated AUC0–72h |
| Endogenous substances (hormones, electrolytes) | Baseline levels | Baseline correction; standardised diet |
| Nonlinear kinetics | Dose choice affects sensitivity | Study at the dose most sensitive to formulation differences |
| Modified-release products | Dose dumping, food effect | Fasted and fed studies; multiple-dose studies where needed; alcohol dose-dumping test in vitro |
| Drugs with active metabolites or prodrugs | What to measure | Parent preferred; metabolite when justified |
| Chiral drugs | Enantiomers with different activity and kinetics | Enantioselective assay when needed |
| Locally acting products (inhalers, topical, GI-acting) | Plasma levels may not reflect local availability | Pharmacodynamic, clinical endpoint or in vitro methods |
| Food effects | Drugs whose absorption changes with food | Fed studies per guidance |
| Drugs unsafe in healthy volunteers (cytotoxics, antipsychotics) | Ethics | Studies in patients, often steady state |
| Fixed-dose combinations | Each component | BE shown for every active ingredient |

## 5.12 Generic substitution

**Generic substitution** means dispensing a therapeutically equivalent generic product in place of the prescribed brand (or another generic).

- **Benefits:** lower cost, wider access, savings for health systems.
- **Requirements:** proven pharmaceutical equivalence and bioequivalence; quality manufacturing (GMP); clear labelling.
- **Concerns:** narrow therapeutic index drugs (antiepileptics, immunosuppressants, anticoagulants, thyroid hormone) where switching between products calls for monitoring; differences in appearance or excipients (allergy, patient confusion); "switchability" between different generics (each is compared with the reference, not with each other); perception and trust of patients and prescribers.
- **In India:** many products are "branded generics"; public policy promotes prescribing by generic name and supplying quality-assured generics through schemes such as the Pradhan Mantri Bhartiya Janaushadhi Pariyojana. The strength of generic substitution depends on regulators insisting on BE and GMP for every generic.
- Biosimilar substitution is not automatic; it depends on the regulator's view of interchangeability.

## Remember

- F (absolute) = (AUCoral × DoseIV)/(AUCIV × Doseoral); relative compares two extravascular products.
- Methods in order of preference: plasma levels > urinary excretion > acute PD effect > clinical endpoint > in vitro (biowaiver only).
- Standard design: randomised 2 × 2 crossover, single dose, healthy volunteers, washout ≥ 5 t½, sampling ≥ 3 t½, AUC0–t ≥ 80% of AUC0–∞.
- Log-transform AUC and Cmax; 90% CI of GMR within 80.00–125.00% (= TOST at 5% each); NTI 90.00–111.11%; HVD scaled limits up to 69.84–143.19% for Cmax (EMA).
- Example: GMR 95.36%, 90% CI 88.81–102.40%, CVw 9.6% → BE.
- India: CDSCO, NDCT Rules 2019, CTRI registration, ethics committee, 2005 BA/BE guideline.
- BCS (ICH M9): high solubility = highest dose in ≤ 250 mL at pH 1.2–6.8; high permeability = fa ≥ 85%; rapid = 85% in 30 min, very rapid = 85% in 15 min; waivers for Class I and III.
- Biosimilars: stepwise comparability; analytical foundation; comparative PK/PD; immunogenicity; India: Similar Biologics guidelines 2012/2016.
