# Unit 2: Biopharmaceutic considerations in drug product design and in vitro drug product performance

This unit asks a practical question: how do we design an oral product so that the drug reaches the blood at the right rate and extent, and how do we prove it in the laboratory? It covers the biopharmaceutic factors that decide bioavailability, rate-limiting steps, the physicochemical nature of the drug, formulation factors, compendial and alternative dissolution tests, meeting dissolution specifications, sources of variability, in vitro–in vivo correlation (IVIVC), comparison of dissolution profiles, stability and the overall design of a drug product.

All numbers in worked examples are example numbers for hypothetical products.

## 2.1 Introduction

A **drug product** is the drug plus excipients in a dosage form made by a defined process. Two products with the same amount of the same drug can give very different plasma levels because of differences in particle size, salt, polymorph, excipients or process. **Biopharmaceutics** studies how these physicochemical and formulation variables affect the rate and extent of absorption. Its goals in product design are:

- adequate and reproducible bioavailability;
- the intended release profile (immediate, delayed, extended);
- a quality-control test (usually dissolution) that is discriminating and, ideally, predictive of in vivo behaviour;
- stability of that performance over the shelf life.

## 2.2 Biopharmaceutic factors affecting drug bioavailability

| Group | Factors |
| --- | --- |
| Drug substance | Solubility and pH–solubility profile, pKa, lipophilicity (log P, log D), particle size and surface area, crystal form (polymorphs, amorphous, solvates), salt form, chemical stability in GI fluids, complexation, molecular size |
| Drug product | Type of dosage form, excipients (diluents, binders, disintegrants, lubricants, surfactants, coating polymers), manufacturing process (granulation, compression force, drying), release mechanism |
| Patient (physiology) | GI pH, gastric emptying and transit, food, bile, fluid volume, gut-wall enzymes and transporters, first-pass metabolism, disease, age, concomitant drugs |
| Route | Oral, buccal, rectal, IM, SC, transdermal: each has its own barriers and blood flow |

## 2.3 Rate-limiting steps in drug absorption

For a solid oral product the steps are in series:

```text
 Solid dosage form ─k_dis─► particles ─k_d (dissolution)─► drug in solution ─Ka (permeation)─► blood
```

The **slowest step controls the overall rate**.

- **Dissolution rate-limited** (kd much smaller than Ka): typical for poorly soluble drugs (BCS II). Anything that speeds dissolution (micronisation, salt, solid dispersion, surfactant) speeds absorption; dissolution testing is likely to correlate with in vivo data.
- **Permeation rate-limited** (Ka much smaller than kd): typical for soluble but poorly permeable drugs (BCS III). Formulation changes in dissolution have little effect; permeation enhancers or prodrugs are needed.
- **Disintegration-limited:** for hard tablets or old capsules.
- **Gastric emptying-limited:** for rapidly dissolving, well-absorbed drugs, the rate of arrival in the intestine sets tmax.
- **For extended-release products,** release from the product is deliberately made the slowest step, so the plasma profile follows the release rate.

## 2.4 Physicochemical nature of the drug

1. **Solubility and dose.** The dose number D0 = (dose/250 mL)/Cs. If D0 is above 1, the dose cannot dissolve in a glass of water; absorption may be solubility-limited.
2. **pKa and pH–solubility profile.** Weak acids dissolve better in intestinal fluid; weak bases dissolve in the stomach but may precipitate when they enter the intestine (supersaturation and precipitation kinetics matter).
3. **Lipophilicity.** Log P of about 1–3 favours passive permeation; very high log P lowers aqueous solubility and increases binding.
4. **Particle size.** Smaller particles dissolve faster (larger area) and slightly more (Ostwald–Freundlich equation for very small particles). Nanocrystals and micronised powders are used for poorly soluble drugs.
5. **Polymorphism and amorphous forms.** Metastable forms and amorphous solids have higher apparent solubility; the risk is conversion to the stable, less soluble form during processing or storage. Regulatory filings must identify and control the form.
6. **Salt formation.** Common way to improve dissolution of ionisable drugs; the counter-ion also affects hygroscopicity, stability and manufacturability. A salt of a weak acid dissolves faster partly because it raises the pH of the diffusion layer.
7. **Hydrates, solvates and cocrystals.** Change solubility and stability.
8. **Chemical stability in GI fluids.** Acid-labile drugs need enteric coating or a stable prodrug.
9. **Complexation.** Cyclodextrins increase apparent solubility; complexes with insoluble excipients reduce availability.

## 2.5 Formulation factors affecting drug product performance

| Factor | Typical effect |
| --- | --- |
| Diluent | Hydrophilic diluents aid wetting; calcium salts can form insoluble complexes with some drugs (tetracyclines) |
| Binder | Concentration and type affect hardness and disintegration time |
| Disintegrant | Amount and position (intra- vs extra-granular) control break-up; superdisintegrants act at low levels |
| Lubricant | Hydrophobic magnesium stearate forms a film; over-mixing slows dissolution; hydrophilic lubricants are alternatives |
| Surfactant | Improves wetting and solubilisation; may also affect membrane permeability |
| Polymer (release-controlling) | Matrix (HPMC, ethylcellulose) or membrane coat controls release rate; viscosity grade and amount critical |
| Solubility enhancers | Solid dispersions, lipid-based systems (SEDDS), cyclodextrins, nanosuspensions |
| Process | Granulation, drying temperature, compression force, coating thickness and curing |

Excipient interactions can also change permeability (for example some surfactants inhibit P-gp) or stability.

## 2.6 In vitro dissolution and drug release testing

**Purpose:** quality control (batch-to-batch consistency), guide formulation development, detect process or stability changes, support biowaivers and, where an IVIVC exists, predict in vivo performance.

**Terms**

- **Dissolution test:** for immediate-release products.
- **Drug release test:** for modified-release products (delayed and extended release), usually multi-point.
- **Intrinsic dissolution rate (IDR):** dissolution rate per unit area of a pure drug compact with constant area (rotating disc, Wood's apparatus), in mg/min/cm². As a rough guide, an IDR above about 1 mg/min/cm² rarely gives dissolution-limited absorption, while one below about 0.1 mg/min/cm² usually does.

### Compendial methods of dissolution

| USP apparatus | Description | Typical use and conditions |
| --- | --- | --- |
| 1 Basket | Rotating mesh basket holding the unit | Capsules, floating products; often 50–100 rpm |
| 2 Paddle | Paddle stirrer in a round-bottom vessel; sinker for floating units | Most tablets; often 50–75 rpm |
| 3 Reciprocating cylinder | Glass cylinders move up and down through rows of media | Extended-release products; easy pH changes along the "GI tract" |
| 4 Flow-through cell | Fresh medium pumped through a cell holding the unit | Poorly soluble drugs (maintains sink), implants, powders, microspheres |
| 5 Paddle over disc | Paddle with the patch held on a disc | Transdermal patches |
| 6 Rotating cylinder | Patch fixed on a cylinder | Transdermal patches |
| 7 Reciprocating holder | Small units on a holder moving up and down | Small transdermal systems, implants, osmotic products |

The Indian Pharmacopoeia describes the basket (Apparatus I) and paddle (Apparatus II) and other apparatus for special products.

**Standard conditions (immediate-release, typical):** 900 mL medium (500–1000 mL), 37 ± 0.5 °C, deaerated medium, media of pH 1.2 (0.1 M HCl), 4.5 (acetate) and 6.8 (phosphate). Surfactants (for example sodium lauryl sulphate) may be added for poorly soluble drugs with justification. Sampling at fixed times, filtered immediately, assayed by UV or HPLC.

**Sink conditions:** the medium volume should be at least about three times the volume needed to saturate the dose, so that dissolution is not slowed by build-up of drug.

**Example (example numbers):** a 50 mg dose with Cs = 0.02 mg/mL needs 2,500 mL to dissolve; 900 mL would reach 2.8 × Cs, so sink is not possible (some drug cannot dissolve at all). With 0.5% surfactant raising Cs to 0.2 mg/mL, complete dissolution in 900 mL gives only 0.28 × Cs: sink conditions are met.

### Alternative methods of dissolution testing

- **Rotating-disc (intrinsic dissolution) and static-disc methods** for drug substance characterisation.
- **Beaker method (Levy) and flask–stirrer methods:** early simple designs.
- **Rotating bottle method:** for extended-release beads; bottles tumble end over end in a water bath.
- **Dialysis-bag and reverse-dialysis methods:** separate released drug from nanoparticles, liposomes and emulsions.
- **Biphasic dissolution:** an aqueous layer under an organic layer (octanol) that removes dissolved drug, mimicking absorption; useful for poorly soluble drugs.
- **Transfer models:** drug dissolved in simulated gastric fluid is pumped into simulated intestinal fluid to study precipitation of weak bases.
- **Biorelevant media:** FaSSGF, FaSSIF and FeSSIF contain bile salt and lecithin; they predict food effects better.
- **Dynamic GI models:** multi-compartment systems (for example the TNO gastro-intestinal model) mimic peristalsis, emptying, secretions and absorption.
- **Combined dissolution–permeation systems:** dissolution vessel linked to Caco-2 or artificial membranes.
- **Stress-test devices:** mimic mechanical forces of gastric emptying for extended-release products (dose dumping).

### Meeting dissolution requirements (USP-type acceptance tables)

**Immediate-release (Q = amount dissolved, as % of label claim, at the specified time):**

| Stage | Units tested | Acceptance criteria |
| --- | --- | --- |
| S1 | 6 | Each unit not less than Q + 5% |
| S2 | 6 more (12 total) | Average of 12 ≥ Q, and no unit below Q − 15% |
| S3 | 12 more (24 total) | Average of 24 ≥ Q, not more than 2 units below Q − 15%, and no unit below Q − 25% |

**Extended-release** uses levels L1 (6 units), L2 (12) and L3 (24) with limits at several time points (a range at each time and a minimum at the last point). **Delayed-release (enteric)** products are tested in an acid stage (A1–A3, limited release in 0.1 M HCl) followed by a buffer stage (B1–B3, Q in pH 6.8 buffer).

### Problems of variable control in dissolution testing

| Source | Examples | Control |
| --- | --- | --- |
| Apparatus | Vessel shape and finish, shaft wobble and centring, paddle or basket height, basket mesh damage, vibration from the bench or water bath | Mechanical calibration (dimensions, speed, wobble, centring, temperature) and performance verification with reference tablets |
| Medium | Wrong pH or ionic strength, dissolved gases forming bubbles on the unit, surfactant quality, evaporation | Prepare and check pH, deaerate, cover vessels |
| Hydrodynamics | "Coning" (a mound of undissolved powder under the paddle in Apparatus 2), unit sticking to the vessel, floating | Change speed with justification, use sinkers, consider Apparatus 1 |
| Sampling and analysis | Sampling position, filter adsorption or leaching, delayed filtration (continued dissolution), drug degradation in medium | Validated sampling zone, filter compatibility study, stability of samples |
| Product | Capsule cross-linking, hardening on storage | Enzymes (pepsin, pancreatin) in the medium for cross-linked gelatin; stability monitoring |
| Human | Timing errors, wrong calculations | Automation, training, second-person checks |

A **discriminating** method detects meaningful formulation or process changes; it should not be so harsh that every product passes or so mild that good batches fail.

## 2.7 Kinetics of drug release (models used to describe profiles)

| Model | Equation | Typical system |
| --- | --- | --- |
| Zero order | Q = Q0 + k0 t | Osmotic pumps, reservoir systems, ideal extended release |
| First order | ln(100 − Q) = ln 100 − k1 t | Many immediate-release and porous matrix products |
| Higuchi | Q = kH √t | Drug diffusing from an insoluble matrix |
| Hixson–Crowell | W0^(1/3) − W^(1/3) = κ t | Erosion or dissolution with shrinking area |
| Korsmeyer–Peppas | Mt/M∞ = k tⁿ (first 60% of release) | Polymeric systems; n tells the mechanism |
| Weibull | M = 1 − exp[−(t − Ti)^b / a] | Empirical fit for many profiles |

For a thin film (slab), Korsmeyer–Peppas n = 0.5 means Fickian diffusion, 0.5 < n < 1 anomalous (diffusion plus swelling or erosion), and n = 1 Case II (zero-order, relaxation-controlled) transport. The limits are lower for cylinders (0.45 and 0.89) and spheres (0.43 and 0.85).

## 2.8 Performance of drug products: in vitro–in vivo correlation (IVIVC)

**Definition (US FDA, 1997 guidance on extended-release oral dosage forms):** a predictive mathematical model describing the relationship between an in vitro property of a dosage form (usually rate or extent of dissolution) and a relevant in vivo response (plasma concentration or amount absorbed).

| Level | What is correlated | Strength and use |
| --- | --- | --- |
| A | Point-to-point: fraction dissolved in vitro vs fraction absorbed in vivo at each time (often 1:1 line) | Highest; whole plasma profile can be predicted; supports biowaivers for many changes and dissolution specifications |
| B | Mean in vitro dissolution time (MDT) vs mean residence time (MRT) or mean absorption time (MAT) | Uses all data but not point-to-point; different profiles can give the same mean; not for regulatory waivers |
| C | One dissolution parameter (t50, % at 4 h) vs one PK parameter (AUC, Cmax) | Weakest; useful in early development |
| Multiple C | Several dissolution time points each vs one or more PK parameters | Can be as useful as Level A if it covers the profile |
| D | Rank order (qualitative) | Not a true correlation; development aid only |

### Developing a Level A correlation

1. Make at least two, preferably three, formulations with different release rates (slow, medium, fast).
2. Obtain dissolution profiles with a discriminating method.
3. Give each formulation (and usually an IV solution or immediate-release reference) to the same subjects and measure plasma profiles.
4. Find the in vivo fraction absorbed over time by **deconvolution**: Wagner–Nelson (one-compartment drugs), Loo–Riegelman (two-compartment) or numerical deconvolution using the unit impulse response (Unit 3).
5. Plot fraction absorbed vs fraction dissolved, fit the relationship (linear; time scaling or shifting if needed).
6. **Validate predictability:** use the model to predict Cmax and AUC by convolution. Internal predictability (formulations used to build the model): mean absolute prediction error (%PE) of 10% or less, and no single formulation above 15%. External predictability uses a new formulation.

%PE = [(observed − predicted)/observed] × 100

### Worked example 1 — Level A correlation (example numbers)

| Time (h) | Fraction dissolved (FD) | Fraction absorbed (FA, by Wagner–Nelson) |
| --- | --- | --- |
| 1 | 0.15 | 0.12 |
| 2 | 0.32 | 0.30 |
| 4 | 0.50 | 0.47 |
| 6 | 0.66 | 0.65 |
| 8 | 0.80 | 0.78 |
| 12 | 0.92 | 0.90 |

Linear regression of FA on FD gives slope = 1.013, intercept = −0.029, r = 0.9998. Slope near 1 and intercept near 0 mean in vitro dissolution matches in vivo absorption almost 1:1, so the method is predictive.

If the observed Cmax of a validation batch is 11.5 mg/L and the model predicts 10.9 mg/L, %PE = (11.5 − 10.9)/11.5 × 100 = **5.2%**, within the 10% limit.

### Uses of a validated IVIVC

- Biowaiver for certain manufacturing changes (site, equipment, process, minor composition changes) without a new bioequivalence study.
- Setting clinically relevant dissolution specifications (the range at each time point linked to acceptable Cmax and AUC).
- Reducing human studies during development.

**When IVIVC is likely:** dissolution is rate-limiting (BCS II), extended-release products. **Unlikely:** permeability-limited drugs (BCS III), drugs with saturable absorption or variable first pass, very rapidly dissolving immediate-release products (dissolution not limiting).

## 2.9 Dissolution profile comparisons

Used for post-approval changes, comparing a test product with a reference, comparing strengths, and supporting biowaivers.

### Model-independent: difference factor f1 and similarity factor f2 (Moore and Flanner)

f1 = {Σ|Rt − Tt| / Σ Rt} × 100

f2 = 50 × log { [1 + (1/n) Σ (Rt − Tt)²]^(−0.5) × 100 }

where Rt and Tt are mean % dissolved of reference and test at time t, and n the number of time points.

- **f1 of 0–15 and f2 of 50–100** indicate similar profiles; f2 = 100 when profiles are identical; f2 = 50 corresponds to an average difference of about 10% at every point.
- Conditions: 12 units of each product; same test conditions; at least three time points (excluding zero); only **one** point after 85% dissolution of either product (EU guidance: up to the first point where either product reaches 85%); coefficient of variation not more than 20% at early points (for example 10–15 min) and not more than 10% at later points.
- If both products dissolve 85% or more within 15 min, the profiles are accepted as similar without f2.
- If variability is too high for f2, use multivariate statistical distance or bootstrap f2.

### Worked example 2 — f1 and f2 (example numbers)

| Time (min) | Reference R (%) | Test 1 T (%) | R − T | (R − T)² |
| --- | --- | --- | --- | --- |
| 10 | 42 | 36 | 6 | 36 |
| 15 | 58 | 51 | 7 | 49 |
| 20 | 71 | 65 | 6 | 36 |
| 30 | 86 | 82 | 4 | 16 |
| Sum | 257 | | 23 | 137 |

- f1 = 23/257 × 100 = **8.9** (within 0–15).
- f2 = 50 × log[100/√(1 + 137/4)] = 50 × log(100/5.937) = 50 × 1.226 = **61.3** → similar.

A second test product dissolving 25, 38, 52 and 70% at the same times gives differences 17, 20, 19, 16 (sum of squares 1306): f1 = 28.0 and f2 = 50 × log(100/√327.5) = **37.1** → not similar.

### Model-dependent and other approaches

- Fit a model (Weibull, first order, Korsmeyer–Peppas) to each profile and compare parameters with confidence regions.
- **Mean dissolution time (MDT)** and **dissolution efficiency (DE)** summarise a profile in one number.

MDT = Σ (tmid × ΔM) / Σ ΔM     DE = [AUC of the dissolution curve from 0 to t / (100% × t)] × 100

### Worked example 3 — MDT and DE (example numbers)

Reference profile: 0, 42, 58, 71, 86, 94% at 0, 10, 15, 20, 30, 45 min.

| Interval (min) | tmid | ΔM (%) | tmid × ΔM |
| --- | --- | --- | --- |
| 0–10 | 5.0 | 42 | 210.0 |
| 10–15 | 12.5 | 16 | 200.0 |
| 15–20 | 17.5 | 13 | 227.5 |
| 20–30 | 25.0 | 15 | 375.0 |
| 30–45 | 37.5 | 8 | 300.0 |
| Sum | | 94 | 1312.5 |

MDT = 1312.5/94 = **14.0 min**. Area under the dissolution curve (trapezoidal) = 2917.5 %·min, so DE(45 min) = 2917.5/(100 × 45) × 100 = **64.8%**.

## 2.10 Drug product stability and performance

Stability is part of performance: a product that dissolves well at release but slowly after six months is not a good product.

- **Physical changes:** polymorphic conversion, recrystallisation of amorphous drug, moisture uptake, tablet hardening, gelatin cross-linking, film-coat curing changes in extended-release products.
- **Chemical changes:** degradation of drug; degradants may be toxic.
- **Stability testing (ICH Q1A(R2)):** long-term, intermediate and accelerated conditions; accelerated is 40 °C/75% RH for 6 months. India is treated as climatic zone IVb (hot and very humid), so CDSCO expects long-term studies at 30 °C/75% RH. Dissolution is a stability-indicating test for solid oral products; packaging (blister material, desiccant) is chosen to protect performance.
- **In-use and photostability** where relevant (ICH Q1B).

## 2.11 Considerations in the design of a drug product

A systematic design starts from the patient and works back to the formulation:

1. **Pharmacodynamic and pharmacokinetic considerations:** therapeutic window, half-life, need for rapid onset or prolonged action, first-pass metabolism (may favour sublingual, transdermal or parenteral routes), variability.
2. **Drug substance properties:** solubility, permeability (BCS class), stability, particle and solid-state properties, dose.
3. **Route and dosage form:** patient age (paediatric liquids, orally disintegrating tablets for the elderly), compliance (once-daily extended release), local vs systemic effect.
4. **Bioavailability targets:** need for solubility enhancement for BCS II and IV; need for enteric protection; food effect.
5. **Manufacturability and cost:** robust process, scale-up, stability, packaging.
6. **Quality by design (ICH Q8–Q10):** define the quality target product profile (QTPP), identify critical quality attributes (CQAs, such as dissolution and assay), link them to critical material attributes and critical process parameters by risk assessment and design of experiments, set a design space and a control strategy.
7. **Regulatory strategy:** bioequivalence or biowaiver route for generics, IVIVC for extended-release products.

```text
 QTPP ─► CQAs (dissolution, assay, impurities) ─► risk assessment
     ─► DoE on material attributes and process parameters ─► design space
     ─► control strategy (specifications, in-process controls) ─► lifecycle management
```

## Remember

- Rate-limiting step decides which formulation change matters: dissolution-limited (BCS II) vs permeation-limited (BCS III).
- Dose number D0 = (dose/250)/Cs; above 1 means solubility-limited risk.
- USP apparatus 1 basket, 2 paddle, 3 reciprocating cylinder, 4 flow-through cell, 5 paddle over disc, 6 rotating cylinder, 7 reciprocating holder; 37 ± 0.5 °C, 900 mL, pH 1.2/4.5/6.8.
- S1: each ≥ Q + 5%; S2: mean of 12 ≥ Q, none < Q − 15%; S3: mean of 24 ≥ Q, ≤ 2 below Q − 15%, none below Q − 25%.
- IVIVC Level A point-to-point (best), B MDT vs MRT, C single point; validation %PE ≤ 10% average, ≤ 15% each.
- f1 0–15, f2 50–100 = similar; 12 units, ≥ 3 points, one point after 85%; no f2 needed if both ≥ 85% in 15 min.
- MDT = Σ tmid ΔM / Σ ΔM; DE = area under dissolution curve / (100 × t).
- Korsmeyer–Peppas n (slab): 0.5 Fickian, 0.5–1 anomalous, 1 Case II.
- India = zone IVb: long-term 30 °C/75% RH; accelerated 40 °C/75% RH.
