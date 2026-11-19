# Unit 4: Gas chromatography and HPLC

Gas chromatography (GC) and high performance liquid chromatography (HPLC) are the two instrumental column methods that dominate modern drug analysis. HPLC is used for the assay and impurity tests of most drugs in the pharmacopoeia; GC is used for volatile substances such as residual solvents. Both share the same theory of retention, efficiency and resolution, which is explained first.

## 4.1 Common chromatographic terms and theory

```text
 CHROMATOGRAM (detector response vs time)

 response
   ^                      peak 1      peak 2
   |                       /\          /\
   |      t0              /  \        /  \
   |   (unretained)      /    \      /    \
   |_____|_____________/______\____/______\_________> time
         t0           |<- W1 ->|  |<- W2 ->|
   |<---- tR1 -------->|
   |<------------ tR2 ------------>|
```

| Term | Symbol and formula | Meaning |
| --- | --- | --- |
| Retention time | tR | Time from injection to the peak maximum |
| Dead (void) time | t0 (tM) | Time for an unretained substance (air in GC, uracil or solvent front in HPLC) |
| Adjusted retention time | t′R = tR − t0 | Time actually spent in the stationary phase |
| Retention volume | VR = tR × F | F = flow rate |
| Capacity (retention) factor | **k = (tR − t0)/t0** | Ideally 2–10 |
| Selectivity (separation) factor | **α = k2/k1** | Must be above 1 for separation |
| Number of theoretical plates | **N = 16 (tR/W)²** = **5.54 (tR/W½)²** | Column efficiency; W = width at base, W½ = width at half height |
| Height equivalent to a theoretical plate | **HETP (H) = L/N** | Smaller H, more efficient column |
| Resolution | **Rs = 2(tR2 − tR1)/(W1 + W2)** | Rs ≥ 1.5 means baseline separation |
| Tailing (symmetry) factor | T = W0.05/2f | W0.05 = width at 5% height, f = front half-width; 1 = symmetric |

### Plate theory

Martin and Synge pictured the column as many thin layers (**theoretical plates**), in each of which the solute reaches equilibrium between the two phases. The more plates, the narrower the peaks. The theory explains peak shape and gives N, but it does not explain why peaks broaden.

### Rate theory: the van Deemter equation

**H = A + B/u + C·u**, where u is the linear velocity of the mobile phase.

- **A (eddy diffusion, multiple paths):** molecules take paths of different length round the particles; smaller, uniform particles and good packing lower A. Zero in open tubular (capillary) columns.
- **B/u (longitudinal diffusion):** molecules diffuse along the column from the zone centre; important at low flow rates and in gases.
- **C·u (resistance to mass transfer):** molecules take time to move in and out of the stationary phase; important at high flow rates; thinner films and smaller particles lower C.

```text
  H
  ^ \                    /
  |  \  B/u            / Cu
  |   \              /
  |    \____________/   <- minimum H at the optimum flow rate
  |      A (flat)
  +-----------------------> flow velocity u
```

**Worked example.** A peak with tR = 6.0 min and base width W = 0.40 min on a 250 mm column: N = 16(6.0/0.40)² = 16 × 225 = **3600 plates**; H = 250/3600 = **0.069 mm**. With t0 = 1.2 min, two peaks at 4.8 and 6.0 min (widths 0.36 and 0.40 min): k1 = 3.0, k2 = 4.0, α = 4.0/3.0 = **1.33**, Rs = 2(6.0 − 4.8)/(0.36 + 0.40) = **3.16** (fully separated).

### Quantitative methods (both GC and HPLC)

1. **External standard:** peak area of the sample compared with that of a standard of known concentration (c_test = c_std × area_test/area_std) or a calibration curve.
2. **Internal standard:** a fixed amount of a different, well-resolved compound is added to sample and standard; the ratio of analyte area to internal-standard area is used, which corrects for injection-volume errors (useful in GC).
3. **Area normalisation:** % of each component = its area / total area × 100 (for related compounds with similar response). Example: areas 1250, 3750 and 500 give 22.7%, 68.2% and 9.1%.
4. **Standard addition.**

## 4.2 Gas chromatography: introduction

In GC the **mobile phase is an inert gas** (the carrier gas) and the sample must be **volatile and thermally stable**. Two forms:

- **Gas–liquid chromatography (GLC):** the stationary phase is a non-volatile liquid coated on a solid support or on the column wall; separation by **partition**. James and Martin (1952) introduced it. This is the common form.
- **Gas–solid chromatography (GSC):** the stationary phase is a solid adsorbent (molecular sieves, porous polymers); separation by **adsorption**; used for permanent gases.

Components separate according to their **volatility (boiling point)** and their **interaction with the stationary phase** (like dissolves like: a polar phase retains polar compounds).

## 4.3 Instrumentation of GC

```text
 GAS CHROMATOGRAPH

 [Carrier gas cylinder] -> [Pressure regulator + flow controller] -> [Injection port (heated)] -> [Column in thermostatted oven] -> [Detector (heated)] -> [Amplifier + data system]
  N2, He, H2, Ar           (two-stage regulator,                     septum, syringe,              packed or capillary                FID, TCD, ECD...
                            rotameter or soap-bubble meter)          split/splitless
```

1. **Carrier gas:** nitrogen, helium, hydrogen or argon. It must be inert, dry, pure (traps remove moisture and oxygen) and suited to the detector (helium or hydrogen for TCD because of their high thermal conductivity; nitrogen for FID). Flow rate is controlled precisely because retention depends on it.
2. **Sample injection system:** a microsyringe (1–10 µl) through a silicone rubber **septum** into a heated injection port, kept about 50 °C above the boiling point of the least volatile component so that the sample flashes into vapour at once. **Split injection** sends only a small fraction (1:10 to 1:100) onto a capillary column; **splitless** for trace work. Gas samples use a gas-sampling valve; **headspace** samplers inject the vapour above a heated sample (residual solvents).
3. **Column:**

| Feature | Packed column | Capillary (open tubular) column |
| --- | --- | --- |
| Material | Stainless steel or glass | Fused silica coated outside with polyimide |
| Length | 1–3 m | 10–100 m |
| Internal diameter | 2–4 mm | 0.1–0.53 mm |
| Stationary phase | Liquid coated on an inert support (diatomaceous earth, Chromosorb) | Thin film on the inner wall (WCOT), on a support layer on the wall (SCOT), or a porous layer (PLOT) |
| Efficiency | Few thousand plates | Hundreds of thousands of plates |
| Sample capacity | Large | Small |

   **Common stationary phases:** polydimethylsiloxane (non-polar, for example OV-1, SE-30, DB-1), phenyl methyl polysiloxane (intermediate, OV-17), polyethylene glycol (polar, Carbowax 20M). A good phase is non-volatile, thermally stable and chemically inert.
4. **Column oven:** keeps the column at a precise temperature (isothermal) or raises it in a programme.
5. **Detectors:**

| Detector | Principle | Selectivity / notes |
| --- | --- | --- |
| **Flame ionisation detector (FID)** | Eluate burns in a hydrogen–air flame; organic carbon forms ions; a collector electrode measures the current | Nearly all organic compounds; very sensitive, wide linear range; destructive; does not respond to water, CO2, permanent gases; most widely used |
| **Thermal conductivity detector (TCD, katharometer)** | Heated filaments in a Wheatstone bridge; solutes change the thermal conductivity of the carrier gas and hence filament temperature and resistance | Universal (any compound different from the carrier), non-destructive, less sensitive |
| **Electron capture detector (ECD)** | A radioactive source (nickel-63) ionises the carrier gas giving a standing current; electronegative solutes capture electrons and lower the current | Very sensitive to halogens, nitro groups, organometallics; pesticide residues |
| **Nitrogen–phosphorus (thermionic) detector** | Heated alkali-metal bead | Selective for N and P compounds |
| **Flame photometric detector** | Emission of S and P compounds in a flame | Sulphur and phosphorus |
| **Mass spectrometer (GC-MS)** | Ionisation and mass analysis | Identification by molecular mass and fragments |

6. **Recorder/data system:** integrates peak areas and reports retention times.

## 4.4 Derivatization in GC

Many drugs are polar, non-volatile or decompose on heating (–OH, –COOH, –NH2, –SH groups that hydrogen bond). **Derivatization** converts them into volatile, stable derivatives.

**Purposes:** increase volatility, improve thermal stability, reduce adsorption and peak tailing, improve separation (including of enantiomers with chiral reagents) and increase detector response (halogenated derivatives for ECD).

| Method | Reagent examples | Groups converted |
| --- | --- | --- |
| **Silylation** (most common) | BSA, BSTFA, trimethylchlorosilane (TMCS), hexamethyldisilazane (HMDS) | Active hydrogens of –OH, –COOH, –NH, –SH replaced by trimethylsilyl groups; used for sugars, steroids, amino acids |
| **Acylation** | Acetic anhydride, trifluoroacetic anhydride, heptafluorobutyric anhydride | Amines, alcohols, phenols; fluorinated acyl groups help ECD detection |
| **Alkylation / esterification** | Diazomethane, BF3–methanol, methanolic HCl, tetramethylammonium hydroxide | Carboxylic acids to methyl esters (fatty acid methyl esters), phenols to ethers |
| Others | Oxime formation (hydroxylamine), cyclic boronates | Carbonyl compounds, diols |

## 4.5 Temperature programming

In **isothermal** operation a single column temperature is chosen. For a mixture with a wide boiling range, a low temperature separates the light components but the heavy ones take very long and come out as broad, flat peaks; a high temperature elutes the heavy ones well but crowds the light ones together. **Temperature programming** raises the oven temperature during the run (for example 50 °C held 2 min, then 10 °C/min to 250 °C).

```text
  Temp
   ^              ______ final hold
   |             /
   |            /  linear ramp (e.g. 10 C/min)
   |   ________/
   |   initial hold
   +----------------------------> time
```

**Advantages:** all components elute as sharp peaks in a shorter total time; better resolution of early peaks and better detection of late ones; useful for unknown mixtures. **Points to watch:** baseline drift from **column bleed** at high temperature, the oven must cool again before the next run, and the carrier gas flow must be controlled because gas viscosity rises with temperature.

## 4.6 Advantages, disadvantages and applications of GC

**Advantages**

- Very high resolution and efficiency (capillary columns); fast analysis.
- High sensitivity (ppm to ppb) with small samples (µl).
- Good quantitative precision; simple to automate; GC-MS gives identification.

**Disadvantages**

- Only volatile, thermally stable compounds (or those that can be derivatized), roughly 20% of drugs.
- Non-volatile, ionic and high-molecular-weight substances (proteins, salts) cannot be analysed directly.
- Most detectors destroy the sample; preparative use is limited.

**Applications**

- **Residual solvents** in drug substances and products (IP/ICH limits), usually by headspace GC.
- Assay of volatile drugs and anaesthetics, ethanol content in tinctures and elixirs, menthol, camphor.
- Essential oils and their constituents; fatty acid profiles of oils (as methyl esters).
- Purity and impurity profiling of solvents and intermediates.
- Toxicology and forensic analysis (drugs of abuse, alcohol in blood), pesticide residues, steroids in sport testing (GC-MS).

## 4.7 HPLC: introduction

**High performance liquid chromatography** is column liquid chromatography in which a liquid mobile phase is pumped under **high pressure** (often up to about 400 bar, roughly 6000 psi) through a column packed with very small particles (3–10 µm, usually 5 µm). The small particles give a large number of plates, and the pump gives a fast flow despite their resistance. It handles non-volatile, polar, ionic and thermally unstable compounds, which is why it is the main assay method in the pharmacopoeia.

**Modes of HPLC**

| Mode | Stationary phase | Mobile phase | Elution order |
| --- | --- | --- | --- |
| **Normal phase** | Polar (silica, cyano, amino) | Non-polar (hexane with a little isopropanol) | Non-polar first |
| **Reversed phase (most used)** | Non-polar: octadecylsilane (C18, ODS), C8, phenyl bonded to silica | Polar: water or buffer with methanol or acetonitrile | Polar first |
| Ion exchange | Charged resin or bonded groups | Aqueous buffer | By charge |
| Size exclusion | Porous gel | Aqueous or organic | Large molecules first |
| Chiral | Chiral selector bonded to silica | Varies | Separates enantiomers |
| Ion-pair | C18 | Buffer with ion-pair reagent (alkyl sulphonate, tetrabutylammonium) | Retains ionic drugs |

**Theory:** the same as in 4.1 (k, α, N, H, Rs, van Deemter). In HPLC the B term is small because diffusion in liquids is slow, so efficiency stays good at practical flow rates; small particles lower the A and C terms. Resolution is improved by changing the mobile-phase composition (which changes k and α), using a longer column or smaller particles (more N), or changing temperature.

## 4.8 Instrumentation of HPLC

```text
 HPLC SYSTEM

 [Solvent reservoirs A, B] -> [Degasser] -> [High-pressure pump (+ gradient mixer)] -> [Injector (loop valve or autosampler)]
                                                                                              |
 [Data system / integrator] <- [Detector (UV, PDA...)] <- [Analytical column in oven] <- [Guard column]
                                     |
                                  [Waste]
```

1. **Solvent reservoirs:** glass bottles with inlet filters. Solvents are HPLC grade, filtered through 0.45 µm membranes.
2. **Degassing:** dissolved air forms bubbles in the pump and detector (noisy baseline, flow errors). Methods: helium sparging, vacuum filtration, sonication, or an in-line vacuum degasser.
3. **Pumps:** must give a pulse-free, constant, reproducible flow (0.1–10 ml/min) at high pressure and resist corrosion.
   - **Reciprocating (piston) pump:** most common; small chamber, continuous delivery; pulse damper or dual pistons smooth the pulses.
   - **Syringe (displacement) pump:** pulse-free but limited volume.
   - **Constant-pressure (pneumatic) pump:** simple, flow changes with column resistance.
   - **Isocratic elution** uses constant mobile-phase composition; **gradient elution** changes it during the run (low- or high-pressure mixing), like temperature programming in GC.
4. **Injector:** **Rheodyne-type six-port loop valve** with a fixed loop (usually 20 µl): in the "load" position the loop is filled with a syringe at normal pressure; turning to "inject" puts the loop in the high-pressure flow. Autosamplers do this automatically.
5. **Guard column:** short column of the same packing before the analytical column; traps particles and strongly retained material and protects the costly column.
6. **Analytical column:** stainless steel, typically **250 mm × 4.6 mm, 5 µm** C18 packing; also 150 mm and shorter columns with smaller particles. A **column oven** keeps temperature constant (retention times shift with temperature).
7. **Detectors:**

| Detector | Principle | Notes |
| --- | --- | --- |
| **UV-visible (variable wavelength)** | Absorbance in a small flow cell (about 8 µl, 10 mm path) | Most used; drugs with chromophores; mobile phase must be UV-transparent |
| **Photodiode array (PDA/DAD)** | Records the whole spectrum of each peak | Peak purity, identity by spectrum |
| **Fluorescence** | Excitation and emission wavelengths | Very sensitive and selective; derivatization if needed |
| **Refractive index (RI)** | Change in refractive index of the eluate | Universal (sugars, polymers); not for gradients; temperature sensitive |
| **Electrochemical (amperometric)** | Oxidation or reduction current at an electrode | Catecholamines, phenols; very sensitive |
| **Conductivity** | Conductance | Ions (ion chromatography) |
| **Evaporative light scattering (ELSD)** | Light scattered by particles after evaporating the mobile phase | Non-volatile compounds without chromophores |
| **Mass spectrometer (LC-MS)** | Mass of ions | Identification, bioanalysis |

8. **Data system:** records the chromatogram, integrates peaks, calculates results.

### System suitability (pharmacopoeial checks before analysis)

Before the samples are run, replicate injections of a standard must meet set limits, typically: relative standard deviation of peak areas not more than 2.0% (often for 5 or 6 injections), tailing factor not more than 2.0, a minimum number of theoretical plates, and a minimum resolution between named peaks. The exact limits are given in each monograph.

## 4.9 Advantages and applications of HPLC

**Advantages**

- Suits non-volatile, polar, ionic and heat-sensitive compounds (most drugs, peptides, proteins, vitamins).
- High resolution, speed, sensitivity and precision; automation with autosamplers.
- Many modes and detectors; the sample can be recovered (preparative HPLC).
- Quantitation of the drug and its impurities in one run.

**Limitations:** costly equipment, columns and solvents; needs trained staff; no universal and sensitive detector; solvent waste.

**Applications**

1. **Assay** of drugs in raw materials and dosage forms (most IP monographs).
2. **Related substances and impurity profiling**; **stability-indicating methods** that separate the drug from its degradation products.
3. **Dissolution testing** and content uniformity.
4. **Bioanalysis:** drug levels in plasma for pharmacokinetic and bioequivalence studies (often LC-MS).
5. Analysis of vitamins, amino acids, peptides, proteins, antibiotics and herbal marker compounds.
6. **Chiral separation** of enantiomers; **preparative purification** of drugs and natural products.
7. Cleaning validation and environmental analysis.

**GC vs HPLC**

| Feature | GC | HPLC |
| --- | --- | --- |
| Mobile phase | Inert gas | Liquid pumped at high pressure |
| Sample | Volatile, heat stable | Non-volatile, polar, heat-sensitive possible |
| Temperature | High (oven up to about 350 °C) | Near room temperature (column oven 25–40 °C) |
| Elution control | Temperature programming | Gradient elution (solvent composition) |
| Common detector | FID | UV / PDA |
| Typical use | Residual solvents, volatile oils | Assay and impurities of most drugs |

## Remember

- k = (tR − t0)/t0; α = k2/k1; N = 16(tR/W)² = 5.54(tR/W½)²; H = L/N; Rs = 2(tR2 − tR1)/(W1 + W2), 1.5 = baseline separation.
- van Deemter H = A + B/u + Cu (eddy diffusion, longitudinal diffusion, mass transfer).
- GC: carrier gas → injector → column in oven → detector; FID most common, TCD universal, ECD for halogens.
- Derivatization: silylation, acylation, alkylation/esterification to make compounds volatile and stable.
- Temperature programming for wide-boiling mixtures; gradient elution is its HPLC counterpart.
- HPLC: reservoir → degasser → pump → loop injector → guard + analytical column → detector → data; reversed phase C18 most used.
- Quantitation: external standard, internal standard, area normalisation.
