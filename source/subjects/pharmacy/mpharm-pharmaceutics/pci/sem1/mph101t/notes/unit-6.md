# Unit 6: Immunological assays — RIA, ELISA and bioluminescence assays

Immunoassays use the exquisite specificity of an **antibody** for its **antigen** to measure very small amounts of a substance — hormones, drugs, proteins, viral markers — often in a complex sample like serum, without separating it first by chromatography. Bioluminescence assays use light-producing enzyme reactions (mainly firefly luciferase with ATP) as an ultra-sensitive read-out. In pharmacy these methods are used for therapeutic drug monitoring, pharmacokinetics of protein drugs, anti-drug antibody testing, potency of biologicals and vaccines, microbial and endotoxin-related testing and cell-based screening. The syllabus gives this unit only five hours, but questions on the principle and types of ELISA and on RIA are common.

## 6.1 Basic immunology needed for immunoassays

- **Antigen**: a substance that provokes an immune response and binds specifically to an antibody. Proteins and polysaccharides are good immunogens.
- **Hapten**: a small molecule (most drugs, steroids) that can bind an antibody but cannot by itself raise one; it is coupled to a carrier protein (bovine serum albumin, keyhole limpet haemocyanin) to produce antibodies against it. This is how antibodies to digoxin, morphine or theophylline are made.
- **Epitope**: the small region of an antigen that the antibody actually recognises.
- **Antibody (immunoglobulin, mostly IgG for assays)**: Y-shaped protein; two antigen-binding Fab arms and an Fc stem.
- **Polyclonal antibodies**: from immunised animals; a mixture recognising several epitopes; good for capture.
- **Monoclonal antibodies**: from a single hybridoma clone (Köhler and Milstein); one epitope, identical and unlimited supply; high reproducibility.
- **Affinity** (strength at one site, expressed by the association constant Ka, often 10⁸–10¹² L/mol for good assay antibodies) and **avidity** (overall binding strength with multiple sites) decide sensitivity.
- **Specificity and cross-reactivity**: structurally similar molecules (metabolites, related drugs) may also bind; cross-reactivity must be measured during validation.

The reaction obeys the law of mass action:

```text
 Ag + Ab  ⇌  Ag–Ab          Ka = [Ag–Ab] / ([Ag][Ab])
```

**Classification of immunoassays**

| Basis | Types |
| --- | --- |
| Label | Radio (RIA, IRMA), enzyme (EIA, ELISA, EMIT), fluorescence (FIA, FPIA), chemiluminescence (CLIA), electrochemiluminescence |
| Format | Competitive (limited reagent) vs non-competitive / sandwich (excess reagent, immunometric) |
| Separation | Heterogeneous (bound and free label separated, e.g. ELISA, RIA) vs homogeneous (no separation; label activity changes on binding, e.g. EMIT, FPIA) |

## 6.2 Radioimmunoassay (RIA)

**Origin**: developed by Rosalyn Yalow and Solomon Berson for insulin (Nobel Prize 1977) — the first assay able to measure hormones at pg–ng/mL levels in plasma.

**Principle — competitive binding (saturation analysis)**: a fixed, limited amount of antibody is incubated with a fixed amount of **radiolabelled antigen** (Ag\*, the tracer) and the sample containing unlabelled antigen (Ag). Labelled and unlabelled antigen **compete** for the limited binding sites.

```text
 Ag* + Ag + Ab (limited)  ⇌  Ag*–Ab + Ag–Ab + free Ag* + free Ag

 More Ag in the sample → less Ag* can bind → LOWER radioactivity in the bound fraction
 Bound radioactivity is INVERSELY related to analyte concentration
```

**Labels**
- **¹²⁵I** (gamma emitter, half-life about 60 days, counted in a gamma counter; easy to attach to tyrosine residues by chloramine-T or Iodogen methods; most common).
- **³H** and **¹⁴C** (beta emitters, counted by liquid scintillation; used for small molecules like steroids and drugs because they do not alter the structure; ³H half-life about 12.3 years).

**Steps**

1. **Raise the antibody** (hapten–carrier conjugate for drugs) and titrate it so that about 30–50% of the tracer binds in the absence of analyte.
2. **Prepare the tracer** (radiolabelled antigen) and check its purity and specific activity.
3. **Incubate** standards (known concentrations) and unknown samples with antibody and tracer until equilibrium (hours to overnight, often 4 °C).
4. **Separate bound from free** — the critical step:
   - Second antibody (anti-IgG) precipitation, often with polyethylene glycol (double-antibody method).
   - Solid-phase antibody (coated tubes, beads, magnetic particles) — simplest.
   - Dextran-coated charcoal adsorbs free small antigen; ammonium sulphate or PEG precipitates the bound complex.
5. **Count** radioactivity of the bound (or free) fraction.
6. **Standard curve**: plot % bound (B/B0 × 100, where B0 = binding with zero analyte) against log concentration — a sigmoid curve; the linear middle part (or a logit–log transform: logit(B/B0) vs log conc) is used. Read unknowns from the curve.

```text
 B/B0 (%)
 100 |‾‾‾‾\
     |      \
  50 |       \        ← IC50 (midpoint)
     |         \
   0 |          \______
     +------------------→ log [analyte]
```

**Immunoradiometric assay (IRMA)**: a non-competitive variant using **labelled antibody** in excess (sandwich format): signal rises with analyte; more sensitive and wider range than RIA for large proteins (TSH, thyroglobulin).

**Advantages**: extremely sensitive (pg/mL), specific, small sample volume, robust against coloured or turbid samples, the reference method for decades.

**Disadvantages**: radiation hazard and need for licensed handling (in India, regulated by the Atomic Energy Regulatory Board), radioactive waste disposal, short shelf-life of ¹²⁵I reagents, costly counters, long incubations, cannot easily be automated. These drawbacks drove the shift to enzyme and chemiluminescent labels.

**Applications**: hormones (insulin, thyroid hormones T3, T4, TSH, cortisol, steroids, growth hormone), therapeutic drug monitoring (digoxin, theophylline, aminoglycosides historically), drugs of abuse, tumour markers, vitamin B12 and folate, receptor binding studies (radioligand assays in drug discovery), pharmacokinetics of peptides.

## 6.3 Enzyme-linked immunosorbent assay (ELISA)

**Principle**: an antigen–antibody reaction on a **solid phase** (usually a 96-well polystyrene microtitre plate) is detected by an **enzyme-labelled** antibody (conjugate). The enzyme converts a colourless **substrate** into a coloured (or fluorescent or luminescent) product, measured in a plate reader. Washing steps separate bound from unbound reagents (heterogeneous assay). Developed by Engvall and Perlmann (and van Weemen and Schuurs) in 1971 as a non-radioactive alternative to RIA.

**Enzymes and substrates**

| Enzyme | Substrate | Product colour / read-out | Stop solution |
| --- | --- | --- | --- |
| Horseradish peroxidase (HRP) | TMB (3,3′,5,5′-tetramethylbenzidine) + H2O2 | Blue → yellow after acid, read at 450 nm | Dilute H2SO4 |
| HRP | OPD (o-phenylenediamine) | Orange, 492 nm | Acid |
| HRP | ABTS | Green, 405–415 nm | SDS |
| Alkaline phosphatase (ALP) | p-Nitrophenyl phosphate (pNPP) | Yellow p-nitrophenol, 405 nm | NaOH |
| β-Galactosidase | ONPG | Yellow, 420 nm | Sodium carbonate |
| HRP | Luminol + enhancer | Light (chemiluminescent ELISA) | — |

**General steps**: coating → washing → blocking (bovine serum albumin, casein or non-fat milk to cover unoccupied plastic and prevent non-specific binding) → sample/antibody incubation → washing (phosphate buffer with Tween 20) → conjugate → washing → substrate → stop → read absorbance.

### Types of ELISA

**(a) Direct ELISA**

```text
 Antigen coated on well → enzyme-labelled primary antibody → substrate → colour
```

Quick (fewer steps), no secondary-antibody cross-reactivity; but each primary antibody must be labelled, less amplification, lower sensitivity. Used for screening antibodies and antigen detection when purified antigen is available.

**(b) Indirect ELISA**

```text
 Antigen coated → unlabelled primary antibody (from the sample, e.g. patient serum)
   → enzyme-labelled secondary antibody (anti-human IgG) → substrate → colour
```

Measures **antibodies** in serum. Signal amplification (several secondary antibodies bind each primary), one labelled secondary works for many primaries. Examples: HIV antibody screening, anti-drug antibody (ADA) detection for biologicals, antibody titres after vaccination.

**(c) Sandwich ELISA (two-site, non-competitive)**

```text
 Capture antibody coated → sample antigen binds → detection antibody (labelled,
 or biotinylated + streptavidin–HRP) binds a second epitope → substrate → colour
 Signal ∝ antigen concentration (directly proportional)
```

The antigen must have at least two epitopes (proteins, not small haptens). Most specific and sensitive format; used for cytokines, hormones (hCG pregnancy tests), hepatitis B surface antigen, therapeutic proteins and monoclonal antibodies in serum (pharmacokinetics), host-cell protein impurities in biologics. The **high-dose hook effect** (very high antigen saturates both antibodies separately, giving a falsely low signal in one-step assays) is a known pitfall.

**(d) Competitive (inhibition) ELISA**

```text
 Antigen (or antigen–enzyme conjugate) and sample antigen compete for a limited
 amount of coated antibody (or vice versa) → wash → substrate
 Signal is INVERSELY proportional to analyte concentration (as in RIA)
```

Suited to **small molecules (haptens)** with one epitope: drugs, steroids, mycotoxins, pesticide residues, drugs of abuse, antibiotic residues in milk.

**Homogeneous enzyme immunoassay (EMIT)**: a drug–enzyme conjugate (glucose-6-phosphate dehydrogenase) loses activity when antibody binds it; free drug in the sample competes and restores enzyme activity, measured by NADH absorbance at 340 nm. No washing step, easily automated on clinical analysers — common for therapeutic drug monitoring (phenytoin, carbamazepine, digoxin) and drug-of-abuse screening.

**Calibration and data analysis**: standards on each plate; four-parameter logistic (4PL) curve fitting; samples run in duplicate or triplicate; quality controls at low, medium and high levels.

**Validation (bioanalytical)**: accuracy, precision, sensitivity (LLOQ), specificity and selectivity (matrix effects), parallelism, dilution linearity, stability, and cross-reactivity, following bioanalytical method validation guidance (ICH M10).

**Advantages of ELISA**: no radioactivity, long-shelf-life reagents, cheap, high throughput (96- and 384-well plates), automation, visual read-out possible (dip-sticks, lateral-flow tests use the same principle with gold or coloured particles).

**Limitations**: many steps and washes, edge effects and temperature dependence, matrix interference (heterophilic antibodies, rheumatoid factor), hook effect, narrower dynamic range than chemiluminescence.

**Applications in pharmacy and healthcare**
1. Diagnostics: HIV, hepatitis B and C, dengue, typhoid, pregnancy (hCG), thyroid hormones, tumour markers (PSA, CEA).
2. Pharmacokinetics and immunogenicity of biologicals (insulin, monoclonal antibodies, erythropoietin); biosimilar comparability.
3. Potency and identity testing of vaccines and biologicals (antigen content), residual host-cell proteins and protein A in purified antibodies.
4. Therapeutic drug monitoring and drugs of abuse (competitive formats).
5. Food and drug safety: aflatoxins, antibiotic residues, allergens.
6. Research: cytokine profiling, biomarker discovery, receptor and protein binding.

**Related advanced formats**: chemiluminescent immunoassay (CLIA; acridinium ester or luminol labels) and electrochemiluminescence (ruthenium complex labels) give wider dynamic range and higher sensitivity on automated analysers; fluorescence polarisation immunoassay (FPIA) is homogeneous and used for small drugs; time-resolved fluorescence (europium chelates) removes background fluorescence; multiplex bead assays measure many analytes in one well.

## 6.4 Bioluminescence assays

**Bioluminescence** is light emitted by a chemical reaction catalysed by an enzyme in a living organism (fireflies, some bacteria, jellyfish). Unlike fluorescence, no excitation light is needed, so there is **almost no background** — the main reason for its very high sensitivity.

**Firefly luciferase reaction**

```text
 D-luciferin + ATP + O2  —(firefly luciferase, Mg²⁺)→
     oxyluciferin + AMP + PPi + CO2 + light (yellow-green, about 560 nm)
 Light output is proportional to ATP when luciferin and enzyme are in excess
 Measured with a luminometer (PMT detector, light-tight chamber)
```

- Quantum yield is high; as little as femtomoles of ATP can be detected.
- **Flash-type** (rapid peak then decay) and **glow-type** (stabilised enzyme and reagents giving steady light for hours) kits.

**Bacterial luciferase**: reduced flavin mononucleotide (FMNH2) + a long-chain aldehyde + O2 → light (about 490 nm); used to measure NADH/NADPH via coupled reactions and in toxicity tests (Vibrio fischeri / Aliivibrio light inhibition).

**Aequorin** (jellyfish photoprotein): emits blue light when it binds calcium — used to measure intracellular calcium in receptor studies. Related engineered enzymes (Renilla luciferase, NanoLuc) are used in reporter assays.

**Instrumentation: luminometer**

```text
 Sample + reagent injector → light-tight sample chamber (tube or microplate)
 → photomultiplier tube (photon counting) → signal integration over set time
 → relative light units (RLU)
```

**Applications**
1. **ATP determination**: cell viability and cytotoxicity assays (cell number ∝ ATP), drug screening in cancer cell lines, proliferation tests.
2. **Rapid microbiological testing**: total viable count in water, raw materials and surfaces (hygiene monitoring by ATP swabs), sterility and preservative efficacy screening, antibiotic susceptibility (ATP drop on killing). Results in minutes to hours instead of days.
3. **Reporter gene assays**: a luciferase gene placed under the control of a promoter of interest; light output reports receptor activation, gene expression or transfection efficiency — widely used in drug discovery (nuclear receptor and GPCR assays) and to test **gene delivery systems** (plasmid, lipid nanoparticle, viral vectors) in formulation research.
4. **In vivo bioluminescence imaging**: luciferase-expressing tumour cells or bacteria tracked in live animals to follow tumour growth, infection and drug or nanocarrier efficacy.
5. **Enzyme and metabolite assays** coupled to ATP or NADH: creatine kinase, ADP, glucose (via coupled enzymes).
6. **Immunoassay labels**: luciferase or aequorin conjugates in bioluminescent immunoassays; chemiluminescent (non-enzymatic) labels such as acridinium esters in automated CLIA.
7. **Toxicity and environmental testing** with luminous bacteria.

**Advantages**: extreme sensitivity, wide linear range (several orders of magnitude), no excitation light so little background, fast, simple, easily automated.

**Limitations**: enzyme inhibition by some sample components (coloured or quenching compounds, detergents, some drugs inhibit luciferase — false hits in screening), temperature and pH sensitivity, reagent cost, light output decays (timing must be controlled), ATP contamination from the environment.

## 6.5 Comparison of the three methods

| Feature | RIA | ELISA | Bioluminescence |
| --- | --- | --- | --- |
| Label / signal | Radioisotope (¹²⁵I, ³H) | Enzyme → colour (or fluorescence/light) | Enzymatic light emission |
| Detection | Gamma or scintillation counter | Microplate spectrophotometer (450 nm for TMB) | Luminometer |
| Sensitivity | Very high (pg/mL) | High (pg–ng/mL) | Very high (fmol ATP) |
| Hazard | Radiation, waste, licence | None significant | None significant |
| Reagent shelf-life | Short (¹²⁵I decay) | Long | Moderate |
| Automation, throughput | Limited | High | High |
| Typical use | Hormones, legacy TDM, radioligand binding | Diagnostics, biologics PK, ADA, vaccines | ATP, viability, reporter genes, rapid microbiology |

## 6.6 Points to cover in exam answers

- Draw a labelled scheme (wells, antibodies as Y shapes, enzyme, substrate) for each ELISA type.
- State the relation between signal and concentration: **direct** in sandwich and indirect formats, **inverse** in competitive ELISA and RIA.
- Name the separation step (washing in ELISA; second antibody, charcoal, solid phase in RIA).
- Give at least four applications with pharmaceutical relevance.

## Remember

- Haptens need a carrier protein to raise antibodies; monoclonal antibodies give one epitope and reproducible assays.
- RIA = competitive binding of labelled and unlabelled antigen to limited antibody; bound counts fall as analyte rises; ¹²⁵I (gamma) or ³H (beta); separate bound from free; B/B0 vs log conc.
- IRMA = labelled antibody in excess, sandwich, signal rises with analyte.
- ELISA = solid phase + enzyme conjugate + substrate; HRP/TMB read at 450 nm after acid stop; ALP/pNPP at 405 nm.
- Direct (labelled primary), indirect (labelled secondary, detects antibodies), sandwich (two epitopes, most sensitive), competitive (small molecules, inverse signal); EMIT is homogeneous.
- Bioluminescence: luciferin + ATP + O2 → light about 560 nm with firefly luciferase; no excitation, very low background; ATP viability, reporter genes, rapid microbiology, in vivo imaging.
