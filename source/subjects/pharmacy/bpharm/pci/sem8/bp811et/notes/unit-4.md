# Unit 4: Radioimmunoassay and extraction techniques

Hormones, many drugs and tumour markers circulate in blood at nanogram or even picogram per millilitre levels, mixed with thousands of other substances. Measuring them needs two things: a method sensitive and specific enough to find a tiny amount (radioimmunoassay was the first to do this), and a way to pull the analyte out of the sample before analysis (solid-phase and liquid–liquid extraction). This unit covers both.

## 4.1 Radioimmunoassay: importance

**Radioimmunoassay (RIA)** is an analytical method that measures a substance (antigen) by its **competition with a radioactively labelled form of the same substance for a limited number of binding sites on a specific antibody**.

It was developed by **Rosalyn Yalow and Solomon Berson** around 1959–1960 to measure insulin in human plasma. Yalow received the Nobel Prize in Physiology or Medicine in 1977 for this work.

**Why it mattered**

1. **Very high sensitivity:** picogram to nanogram amounts, far below what UV or HPLC with UV detection could measure in plasma.
2. **High specificity** from the antibody–antigen reaction.
3. Works directly in small volumes of serum or plasma, often without extraction.
4. Can handle large numbers of samples.
5. It started the whole family of immunoassays (ELISA, chemiluminescence, fluorescence immunoassays) that now dominate clinical laboratories.

## 4.2 Components of RIA

| Component | Role | Notes |
| --- | --- | --- |
| **Antigen (analyte)** | The substance to be measured, in standards and samples | Hormone, drug, protein |
| **Labelled antigen (tracer)** | Same antigen carrying a radioisotope; competes with the unlabelled antigen | Must keep its ability to bind the antibody; high specific activity needed |
| **Specific antibody (antiserum)** | Binds the antigen; used in a **limited** amount so not all antigen can be bound | Raised in animals; small molecules (haptens) are first coupled to a carrier protein to make them immunogenic. Judged by **titre, affinity and specificity (low cross-reactivity)** |
| **Standards** | Known concentrations of pure antigen to build the standard curve | Prepared in the same matrix as samples |
| **Separation system** | Separates antibody-bound from free antigen | See section 4.5 |
| **Buffer and reagents** | Keep pH, ionic strength and protein content constant; prevent non-specific binding | Often contain albumin or gelatin |
| **Radioactivity counter** | Measures radioactivity of the bound (or free) fraction | **Gamma counter** for ¹²⁵I; **liquid scintillation counter** for ³H and ¹⁴C |

**Common isotopes**

| Isotope | Radiation | Half-life (approximate) | Comment |
| --- | --- | --- | --- |
| ¹²⁵I | Gamma (and X-rays) | about 60 days | Most used; easy counting without sample preparation; high specific activity |
| ³H (tritium) | Weak beta | about 12.3 years | Little change to the molecule; needs liquid scintillation counting |
| ¹⁴C | Weak beta | about 5730 years | Low specific activity, so less used |

**Iodination methods** attach ¹²⁵I to tyrosine or histidine residues: **chloramine-T** (oxidising agent), **lactoperoxidase** (enzymatic, gentler) and **Bolton–Hunter reagent** (for molecules without tyrosine). After labelling, the tracer is purified from free iodide by gel filtration.

## 4.3 Principle of RIA

The method rests on the **law of mass action** and **competitive binding**:

```text
   Ag*   +   Ab   ⇌   Ag*–Ab     (labelled antigen, bound)
    +
   Ag                ⇌   Ag–Ab   (unlabelled antigen from sample or standard, bound)

   Fixed amounts: Ag* and Ab (Ab limited)
   Variable: Ag (unknown)
   More Ag in the sample  →  fewer sites left for Ag*  →  less radioactivity in the bound fraction
```

1. A fixed, limiting amount of antibody and a fixed amount of tracer are added to each tube.
2. Standards or samples (unlabelled antigen) are added.
3. Labelled and unlabelled antigen compete for the antibody sites; the system is incubated to equilibrium.
4. Bound (B) and free (F) antigen are separated.
5. The radioactivity of the bound fraction is counted.
6. **The bound radioactivity is inversely related to the concentration of antigen in the sample.**

**Standard (dose–response) curve.** Bound radioactivity is expressed as:

- **%B/T** — bound counts as a percentage of total counts added.
- **B/B0 (%)** — bound counts in a tube divided by bound counts in the zero-standard tube (no unlabelled antigen), × 100.

Plotting B/B0 against log concentration gives a falling **sigmoid curve**. A **logit–log plot**, logit(B/B0) = ln[(B/B0)/(1 − B/B0)] against log concentration, straightens it for easier reading. Unknowns are read from the curve.

```text
 B/B0 (%)
 100 |*****
     |      **
  50 |        ***      <- read unknown here
     |           **
   0 |             *******
     +---------------------------> log [antigen]
```

**Worked example.** Total counts added = 20,000 cpm. Zero standard (B0) binds 8000 cpm, so B0/T = 40%. A patient sample binds 4000 cpm. B/B0 = 4000/8000 × 100 = **50%**. The concentration is read from the standard curve at 50%; this mid-point region is the most precise part of the curve.

**Controls in each assay:** total count tubes, non-specific binding (NSB) tubes (no antibody), zero standard (B0), standards, quality-control samples, and unknowns, all in duplicate.

## 4.4 Steps of a typical RIA

1. Prepare standards over the expected range in drug-free serum.
2. Pipette buffer, standards, controls and samples into labelled tubes (duplicates).
3. Add a fixed volume of tracer to every tube.
4. Add a fixed volume of antibody (except total count and NSB tubes).
5. Mix and incubate (hours to overnight, at 4 °C or room temperature) to reach equilibrium.
6. Add the separation reagent; centrifuge; remove (decant or aspirate) the supernatant.
7. Count the radioactivity of the pellet (bound fraction) in a gamma counter.
8. Calculate B/B0, draw the standard curve and read the unknowns.

## 4.5 Methods of separating bound and free antigen

| Method | How it works |
| --- | --- |
| **Adsorption** | Dextran-coated charcoal, talc or silicates adsorb the small free antigen; the large antibody–antigen complex stays in solution |
| **Precipitation with chemicals** | Ammonium sulfate, polyethylene glycol (PEG) or ethanol precipitate the antibody and its bound antigen |
| **Double antibody (second antibody) method** | A second antibody raised against the first antibody's species (for example anti-rabbit IgG made in goat) forms a precipitate with the first antibody and everything bound to it |
| **Solid-phase methods** | First antibody fixed to the tube wall, beads, or magnetic particles; free antigen simply washed away |
| **Chromatoelectrophoresis and gel filtration** | Early methods separating by charge or size |

## 4.6 Different methods (formats) of RIA

| Format | Principle | Notes |
| --- | --- | --- |
| **Classical competitive (equilibrium) RIA** | Labelled and unlabelled antigen added together and compete | Standard format described above |
| **Sequential (disequilibrium, delayed addition) RIA** | Sample incubated with antibody first; tracer added later | Unlabelled antigen gets a head start, improving sensitivity |
| **Immunoradiometric assay (IRMA)** | The **antibody**, not the antigen, is labelled and used in excess; often a "sandwich" between a solid-phase antibody and a labelled second antibody | Non-competitive; signal **rises** with antigen concentration; wider range, better sensitivity; needs large antigens with two binding sites |
| **Solid-phase RIA** | Antibody-coated tubes or beads | Easy separation, suits automation |
| **Double antibody RIA** | Separation by second antibody | Very common in kits |

## 4.7 Limitations of RIA

1. **Radiation hazard** to staff; needs shielding, monitoring and licensing (in India from the Atomic Energy Regulatory Board).
2. **Radioactive waste** needs special storage and disposal.
3. **Short shelf life** of ¹²⁵I tracers (about 60-day half-life) and radiolysis of labelled molecules.
4. **Expensive counters** and special laboratory facilities.
5. **Cross-reactivity:** metabolites or related substances may bind the antibody and give falsely high results.
6. Producing good antibodies takes time and animals.
7. Long incubation times; manual steps.
8. Measures immunoreactivity, which may not equal biological activity.

These limitations explain why many laboratories have moved to non-radioactive immunoassays (ELISA, chemiluminescence), but RIA remains a reference method for several hormones.

## 4.8 Applications of RIA

1. **Endocrinology:** insulin, growth hormone, thyroid hormones (T3, T4) and TSH, cortisol, oestradiol, progesterone, testosterone, LH, FSH, prolactin, hCG (pregnancy).
2. **Therapeutic drug monitoring:** digoxin and other drugs with a narrow therapeutic range.
3. **Pharmacokinetic and bioavailability studies** of drugs present at very low plasma levels.
4. **Drugs of abuse** screening (opiates and others) in forensic work.
5. **Tumour markers:** carcinoembryonic antigen (CEA), alpha-fetoprotein (AFP), prostate-specific antigen (PSA).
6. **Vitamins:** vitamin B12, folic acid.
7. **Infectious disease:** hepatitis B surface antigen and other viral antigens.
8. **Research:** neuropeptides, prostaglandins, cyclic nucleotides.

## 4.9 Extraction techniques: why extract?

Biological fluids, plant materials and formulations contain proteins, salts, lipids and excipients that interfere with analysis, clog columns, suppress MS signals and damage instruments. **Sample preparation** aims to:

- isolate the analyte from the matrix (**clean-up**),
- **concentrate** it to reach the detection limit,
- convert it into a solvent compatible with the instrument.

The two main techniques in the syllabus are **liquid–liquid extraction (LLE)** and **solid-phase extraction (SPE)**. Protein precipitation (adding acetonitrile, methanol or an acid to plasma and centrifuging) is the quickest but dirtiest option.

## 4.10 Liquid–liquid extraction (LLE)

**General principle.** A solute distributes itself between two immiscible liquids (usually water and an organic solvent) according to the **Nernst distribution law**:

**K (partition coefficient) = C(organic) / C(aqueous)**, constant at a given temperature, for the same molecular species in both phases.

When the solute ionises, only the un-ionised form usually passes into the organic layer. The **distribution ratio D** includes all forms. For a weak acid:

**D = K / (1 + 10^(pH − pKa))**

So acids are extracted from **acidified** solutions and bases from **alkaline** solutions. For a weak acid of pKa 4.5, the un-ionised fraction is 99% at pH 2.5, 50% at pH 4.5 and only 0.1% at pH 7.5.

**Efficiency of repeated extraction.** The fraction left in the aqueous phase after n extractions, each with volume V(org), is:

**q(n) = [V(aq) / (D·V(org) + V(aq))]ⁿ**

**Worked example.** D = 4, aqueous volume 50 ml, 30 ml of solvent available.
- One extraction with 30 ml: q = 50/(4 × 30 + 50) = 0.294, so **70.6%** extracted.
- Three extractions with 10 ml each: q = [50/(4 × 10 + 50)]³ = 0.171, so **82.9%** extracted.
**Several small extractions beat one large one with the same total solvent.**

**Choice of solvent:** immiscible with water; good solubility for the analyte and poor for interferences; suitable density (chloroform and dichloromethane are heavier than water and form the lower layer; ether, ethyl acetate and hexane the upper layer); low boiling point for easy evaporation; low toxicity and flammability; pure, free of peroxides (ether).

**Procedure (separating funnel)**

```text
   sample (aqueous) + buffer to adjust pH
            │
   add organic solvent ──> stopper, invert, shake, vent often ──> stand to separate
            │                                                         │
   drain lower layer / collect upper layer      repeat 2–3 times with fresh solvent
            │
   combine organic extracts ──> dry (anhydrous Na2SO4) ──> evaporate ──> reconstitute ──> analyse
```

1. Adjust pH so the analyte is un-ionised; add salt (**salting out**, for example NaCl) to push polar analytes into the organic layer.
2. Add the solvent, shake gently but thoroughly, releasing pressure through the stopcock.
3. Let the layers separate; run off the lower layer.
4. Repeat with fresh solvent; combine the extracts.
5. **Back-extraction** for clean-up: shake the organic extract with acid (for a base) so the analyte goes back into water as a salt, leaving neutral impurities behind; then basify and re-extract.
6. Dry, evaporate under nitrogen and redissolve in mobile phase.

**Problems and remedies:** **emulsions** (from proteins and surfactants) are broken by centrifugation, adding salt, filtering through glass wool, or gentle swirling instead of vigorous shaking.

**Variants:** continuous extraction for solutes with low D; Soxhlet extraction for solids; ion-pair extraction (adding a counter-ion to extract ionised drugs); supported liquid extraction (the aqueous sample is spread on an inert support and the solvent flows through, avoiding emulsions); liquid–liquid microextraction using microlitre volumes of solvent.

**Advantages:** simple, cheap equipment, wide choice of solvents, good clean-up for many drugs. **Disadvantages:** large solvent volumes, emulsions, time-consuming, hard to automate, uses toxic solvents, sometimes poor recovery of polar compounds.

## 4.11 Solid-phase extraction (SPE)

**General principle.** SPE is a small-scale form of column chromatography. The liquid sample is passed through a cartridge packed with a solid sorbent; the analyte is **retained** on the sorbent while much of the matrix passes through, interferences are **washed** off, and the analyte is then **eluted** with a small volume of a strong solvent. Retention uses the same interactions as chromatography: hydrophobic, polar, or ionic.

```text
   ┌──────┐   1. Condition   2. Equilibrate   3. Load sample   4. Wash        5. Elute
   │ frit │   methanol       water/buffer      analyte (●)      weak solvent   strong solvent
   │▒▒▒▒▒▒│ ← sorbent bed    wets sorbent      retained;        removes        collects ● in
   │▒▒▒▒▒▒│   (C18, silica,                    matrix (○) passes interferences small volume
   │ frit │    ion exchange)
   └──┬───┘ → to waste / collection (vacuum manifold or positive pressure)
```

**The five steps**

1. **Conditioning:** solvate the sorbent (for reversed phase, methanol opens the alkyl chains).
2. **Equilibration:** water or buffer at the sample's pH replaces the methanol; do not let the bed dry.
3. **Sample loading:** apply the pre-treated sample slowly (diluted, pH-adjusted, centrifuged plasma); the analyte is retained.
4. **Washing:** a weak solvent (water or 5% methanol) removes salts, proteins and weakly held interferences.
5. **Elution:** a small volume of strong solvent (methanol, acetonitrile; for ion exchange, a solvent that neutralises the charge) releases the analyte. The eluate is evaporated and reconstituted, or injected directly.

**Sorbents**

| Type | Examples | Retains | Typical elution |
| --- | --- | --- | --- |
| Reversed phase | C18, C8, phenyl, polymeric (hydrophilic–lipophilic balanced) | Non-polar and moderately polar drugs from aqueous samples | Methanol, acetonitrile |
| Normal phase | Silica, alumina, Florisil, diol, cyano, amino | Polar compounds from non-polar solvents | More polar solvent |
| Ion exchange | Strong cation exchange (SCX, sulfonic acid), strong anion exchange (SAX, quaternary amine), weak exchangers | Charged acids or bases | Change pH or ionic strength |
| Mixed mode | Reversed phase + ion exchange in one bed | Basic or acidic drugs with very clean extracts | Organic solvent with acid or base |

**Formats:** syringe-barrel cartridges (for example 1–6 ml), disks, 96-well plates for automation, pipette tips, and **solid-phase microextraction (SPME)**, in which a coated fibre absorbs analytes from a liquid or headspace and is desorbed directly in a GC injector.

**Important terms:** **capacity** (how much the bed can hold), **breakthrough volume** (sample volume at which analyte starts to pass through unretained), **recovery** (% of analyte collected) and **concentration factor** (sample volume ÷ eluate volume).

**Applications of SPE**

1. Bioanalysis of drugs and metabolites from plasma and urine before HPLC or LC-MS/MS.
2. Concentration of trace pollutants and pesticides from water.
3. Clean-up of herbal and food extracts.
4. Removal of salts and proteins (desalting peptides).
5. Fractionation of complex mixtures by class.

## 4.12 LLE vs SPE

| Point | Liquid–liquid extraction | Solid-phase extraction |
| --- | --- | --- |
| Principle | Partition between two immiscible liquids | Adsorption/partition on a solid sorbent |
| Solvent use | Large volumes | Small volumes |
| Emulsions | Common problem | Do not occur |
| Selectivity | Controlled by solvent and pH | Wide range of sorbent chemistries; very selective |
| Concentration of analyte | Limited | High concentration factors |
| Automation | Difficult | Easy (96-well, robots, online SPE) |
| Time | Longer | Shorter, many samples in parallel |
| Cost | Cheap materials | Cartridges add cost |
| Reproducibility | Operator-dependent | Better |

## Remember

- RIA (Yalow and Berson): labelled and unlabelled antigen compete for a limited antibody; bound radioactivity falls as sample antigen rises.
- Components: antigen, tracer (¹²⁵I gamma about 60 days; ³H beta), limited antibody, standards, separation system, counter.
- B/B0 vs log concentration is sigmoid; logit–log is linear; read unknowns in the middle region.
- Separation: charcoal, PEG/ammonium sulfate, double antibody, solid phase. IRMA = labelled antibody in excess, non-competitive.
- Limitations: radiation, waste, short tracer life, cross-reactivity.
- LLE: K = Corg/Caq; acids from acid, bases from base; q(n) = [Vaq/(D·Vorg + Vaq)]ⁿ; several small extractions are better.
- SPE steps: condition → equilibrate → load → wash → elute; sorbents reversed phase, normal phase, ion exchange, mixed mode.
