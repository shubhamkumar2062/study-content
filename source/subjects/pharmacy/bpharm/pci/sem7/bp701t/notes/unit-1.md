# Unit 1: UV-visible spectroscopy and fluorimetry

Almost every tablet assay in the Indian Pharmacopoeia ends with "measure the absorbance at … nm". UV-visible spectroscopy is the workhorse of the quality control laboratory because it is quick, cheap and accurate. Fluorimetry uses the same kind of electronic excitation but measures the light given out again, which makes it far more sensitive. This unit covers the theory, the instrument, and the ways both methods are used in drug analysis.

## 1.1 Electromagnetic radiation and spectroscopy

**Spectroscopy** is the study of how matter interacts with electromagnetic radiation. Radiation behaves as a wave and as a stream of photons.

- Wavelength (λ): distance between two crests; nm in UV-visible work (1 nm = 10⁻⁹ m).
- Frequency (ν): waves per second (Hz). c = λν, where c = 3 × 10⁸ m/s.
- Wavenumber (ν̄): waves per cm, ν̄ = 1/λ (cm⁻¹); used in IR.
- Energy of a photon: **E = hν = hc/λ**. Shorter wavelength means higher energy.

| Region | Wavelength | What it does to molecules |
| --- | --- | --- |
| Vacuum (far) UV | 10–200 nm | σ → σ* transitions; air absorbs, needs vacuum |
| Near UV | 200–400 nm | Electronic transitions (π, n electrons) |
| Visible | 400–800 nm | Electronic transitions in coloured compounds |
| Infrared | 0.8–1000 µm | Molecular vibrations |
| Microwave | mm–cm | Molecular rotations |

When a molecule absorbs UV or visible light, an electron moves from a lower-energy molecular orbital (the ground state) to a higher-energy, empty orbital (the excited state). The **absorption spectrum** is a plot of absorbance against wavelength; the wavelength of the highest peak is **λmax**.

## 1.2 Electronic transitions

Organic molecules have three kinds of outer electrons: σ (single bonds), π (double and triple bonds) and n (non-bonding lone pairs on O, N, S, halogens).

```text
 Energy
   ^      σ*  ---------------  antibonding
   |      π*  ---------------  antibonding
   |      n   ---------------  non-bonding (lone pairs)
   |      π   ---------------  bonding
   |      σ   ---------------  bonding
 Allowed jumps: σ→σ* (largest gap) > n→σ* > π→π* > n→π* (smallest gap)
```

| Transition | Typical λ | Intensity (ε) | Example |
| --- | --- | --- | --- |
| σ → σ* | below 150 nm | high | Methane, ethane (saturated hydrocarbons; used as UV solvents) |
| n → σ* | 150–250 nm | low to medium | Methanol, methyl chloride, amines |
| π → π* | 170–250 nm (isolated); longer when conjugated | high, often above 10,000 (K band) | Alkenes, dienes, aromatics |
| n → π* | 270–350 nm | low, usually below 100 (R band) | Carbonyl, nitro groups |

Bands of benzene and its derivatives are also described as **E bands** (ethylenic) and **B bands** (benzenoid, fine structure near 255 nm). The **K band** comes from conjugated π → π* and the **R band** from n → π*.

## 1.3 Chromophores and auxochromes

**Chromophore:** an isolated covalently bonded group that absorbs UV or visible radiation, for example C=C, C≡C, C=O, C=N, N=N, NO2, and aromatic rings. Two kinds:

- Groups with π electrons only (C=C, C≡C), which give π → π*.
- Groups with both π and n electrons (C=O, NO2, N=N), which give π → π* and n → π*.

**Auxochrome:** a saturated group with lone pairs that does not absorb above 200 nm by itself but, when attached to a chromophore, shifts the absorption to a longer wavelength and usually increases its intensity. Examples: –OH, –NH2, –OR, –NHR, –SH, –Cl. The lone pair conjugates with the π system and lowers the energy gap.

**Effect of conjugation:** each extra conjugated double bond moves λmax to a longer wavelength. Ethylene absorbs near 171 nm, 1,3-butadiene near 217 nm, and β-carotene (11 conjugated double bonds) absorbs in the visible region, which is why it is orange.

## 1.4 Spectral shifts

```text
  Absorbance
     ^          hyperchromic (up)
     |              ^
     |   hypso  <-- * -->  batho
     |   (blue)     |      (red)
     |              v
     |          hypochromic (down)
     +------------------------------> wavelength
```

| Shift | Change | Common causes |
| --- | --- | --- |
| Bathochromic (red shift) | λmax to longer wavelength | Conjugation, auxochrome, change of solvent polarity for π → π*, ionisation of phenols in alkali |
| Hypsochromic (blue shift) | λmax to shorter wavelength | Loss of conjugation, protonation of aniline in acid, polar solvent for n → π* |
| Hyperchromic | Higher intensity (ε) | Auxochrome such as a methyl group on a pyridine ring |
| Hypochromic | Lower intensity (ε) | Distortion of the chromophore, steric hindrance (biphenyl with ortho groups) |

**Pharmaceutical example:** phenol in alkali becomes the phenoxide ion, giving a bathochromic and hyperchromic shift; aniline in acid becomes the anilinium ion, the lone pair is no longer conjugated, and the spectrum shifts towards that of benzene (hypsochromic). These shifts are used in difference spectrophotometry.

## 1.5 Solvent effects on absorption spectra

The solvent must dissolve the sample and be transparent where the sample absorbs. The lowest useful wavelength of a solvent is its **cut-off**: water about 190 nm, ethanol and methanol about 205–210 nm, chloroform about 245 nm, acetone about 330 nm.

- **π → π* transitions:** the excited state is more polar than the ground state, so a polar solvent stabilises it more and λmax moves to a **longer** wavelength (bathochromic) as solvent polarity increases.
- **n → π* transitions:** polar, hydrogen-bonding solvents stabilise the lone pair in the ground state, so more energy is needed and λmax moves to a **shorter** wavelength (hypsochromic). The carbonyl band of acetone appears at a longer wavelength in hexane than in water.
- **Fine structure:** in non-polar solvents (hexane) or the vapour state, spectra show vibrational fine structure; polar solvents blur it into a smooth band.
- **pH:** ionisable drugs give different spectra in acid and alkali, so the pharmacopoeia always states the solvent (for example 0.1 M HCl or 0.1 M NaOH).

## 1.6 Beer–Lambert law

**Lambert's law:** when monochromatic light passes through an absorbing medium, the rate of decrease of intensity with thickness is proportional to the intensity. **Beer's law:** the same holds for concentration. Combined:

**A = log (I0/I) = ε b c**

- I0 = incident intensity, I = transmitted intensity.
- **Transmittance** T = I/I0; %T = 100 T; **A = −log T = 2 − log %T**.
- b = path length (cm), c = concentration.
- ε = molar absorptivity (L mol⁻¹ cm⁻¹) when c is in mol/L. If c is in g/L, the constant is the absorptivity, a.
- **Specific absorbance A(1%, 1 cm)** (also written E1%1cm): absorbance of a 1% w/v solution (1 g/100 ml) in a 1 cm cell. The pharmacopoeia uses it: c (g/100 ml) = A / A(1%, 1 cm). The two are related by **ε = A(1%, 1 cm) × M / 10**, where M is molecular weight.

**Derivation.** Consider a thin layer of thickness db. The decrease in intensity, −dI, is proportional to I, to the number of absorbing molecules (c) and to db:

−dI/I = k c db

Integrating from I0 (b = 0) to I (b = b): ln(I0/I) = k c b. Converting to base 10: log(I0/I) = (k/2.303) c b = ε b c, so A = ε b c.

**Worked examples.**

1. A drug with ε = 15,000 L mol⁻¹ cm⁻¹ gives A = 0.45 in a 1 cm cell. c = A/(εb) = 0.45/15,000 = **3.0 × 10⁻⁵ mol/L**.
2. A solution transmits 40% of the light. A = 2 − log 40 = 2 − 1.602 = **0.398**.
3. Paracetamol has A(1%, 1 cm) = 715 at 257 nm in 0.1 M NaOH; M = 151.16. ε = 715 × 151.16/10 ≈ **10,800 L mol⁻¹ cm⁻¹**. A diluted sample reading 0.572 contains 0.572/715 = 0.0008 g/100 ml = **8 µg/ml**.

For best accuracy, keep absorbance between about **0.2 and 0.8**; the relative error is smallest near A = 0.43.

## 1.7 Deviations from Beer's law

A plot of A against c should be a straight line through the origin. Curvature has three kinds of causes.

| Type | Cause | Example or remedy |
| --- | --- | --- |
| Real (fundamental) | At high concentration (above about 0.01 M) molecules are close enough to affect each other's charge distribution; refractive index changes with concentration | Work with dilute solutions |
| Chemical | The analyte associates, dissociates, polymerises or reacts with the solvent, so the absorbing species changes with concentration | Dichromate–chromate equilibrium depends on pH; benzoic acid dimerises; buffer the solution or measure at an isosbestic point |
| Instrumental | Polychromatic light (wide band width), stray light, wide slit, mismatched or dirty cells, detector non-linearity, fluorescence of the sample | Measure at λmax where the peak is flat, use narrow slits, matched cells |

**Positive deviation** bends the curve upward; **negative deviation** (more common, from stray light and polychromatic radiation) bends it toward the concentration axis.

## 1.8 Instrumentation

```text
 SINGLE-BEAM UV-VISIBLE SPECTROPHOTOMETER

 [Source] --> [Entrance slit] --> [Monochromator] --> [Exit slit] --> [Sample cell] --> [Detector] --> [Amplifier/Readout]
 D2 lamp (UV)                    prism or grating                     quartz cuvette     PMT or
 W-halogen (Vis)                                                     1 cm path          photodiode
```

```text
 DOUBLE-BEAM SPECTROPHOTOMETER

                                       +--> [Reference cell] --+
 [Source] -> [Monochromator] -> [Chopper/beam splitter]        +--> [Detector] -> [Ratio of I0/I] -> [Recorder]
                                       +--> [Sample cell] -----+
 Both beams pass at the same moment, so lamp drift cancels out.
```

### Sources of radiation

| Source | Range | Notes |
| --- | --- | --- |
| Hydrogen or deuterium discharge lamp | about 160–380 nm | Continuous UV; deuterium gives higher intensity; quartz window |
| Tungsten filament / tungsten-halogen lamp | about 350–2500 nm | Visible and near IR; halogen keeps the filament clean and extends life |
| Xenon arc lamp | about 200–1000 nm | Intense, used in fluorimeters and some spectrophotometers |
| Mercury vapour lamp | line source | Used for wavelength checks and in filter fluorimeters |

### Wavelength selectors

- **Filters** (colorimeters): absorption filters (coloured glass or gelatin), band width 30–50 nm; interference filters, narrower band width (10–15 nm).
- **Monochromators** (spectrophotometers): entrance slit, collimating lens or mirror, dispersing element, focusing element, exit slit.
  - **Prism:** glass for visible (glass absorbs UV), quartz or fused silica for UV. Dispersion is non-linear (better at short wavelengths).
  - **Diffraction grating:** many fine parallel grooves on a reflecting surface; linear dispersion, used in most modern instruments. Holographic gratings give less stray light.
- **Slit width** decides the spectral band width: narrow slits give better resolution, wide slits give more energy.

### Sample cells (cuvettes)

Usually rectangular with **1 cm** path length. **Quartz or fused silica** for UV (below 350 nm) and visible; **glass or plastic** only for the visible region. Cells must be matched, clean, held by the frosted sides, and free of fingerprints and air bubbles.

### Detectors

| Detector | Working | Features |
| --- | --- | --- |
| **Photovoltaic (barrier layer) cell** | Semiconductor layer (selenium) on iron, covered by a thin silver film; light releases electrons that flow as a current without an external power supply | Rugged and cheap; low sensitivity; fatigue; used in simple colorimeters |
| **Phototube (photoemissive tube)** | Evacuated tube with a light-sensitive cathode (alkali metal coating) and an anode; photons eject electrons which reach the anode under a potential (about 90 V) | More sensitive than the photovoltaic cell; needs amplification |
| **Photomultiplier tube (PMT)** | Photocathode plus a series of dynodes (9–16), each at a higher potential; each electron knocks out several more, giving a gain of about 10⁶ or more | Very sensitive and fast; used in spectrophotometers and fluorimeters; damaged by strong light when switched on |
| **Silicon photodiode** | Reverse-biased p–n junction in silicon; light creates electron–hole pairs and a current proportional to intensity | Small, wide range (about 190–1100 nm); many together form a **photodiode array** that records the whole spectrum at once |

```text
 PHOTOMULTIPLIER TUBE
  light
    \
     v
  [Photocathode] -> e- -> [D1] -> [D2] -> [D3] -> ... -> [D9] -> [Anode] -> current
                         +100 V  +200 V  +300 V          (each dynode multiplies electrons)
```

## 1.9 Applications of UV-visible spectroscopy

1. **Identification:** λmax, the shape of the spectrum and the ratio of absorbances at two wavelengths are pharmacopoeial identity tests.
2. **Quantitative assay** of single drugs: by A(1%, 1 cm), by comparison with a standard (c_test = c_std × A_test/A_std) or from a calibration curve. Example: paracetamol tablets at 257 nm.
3. **Colorimetric assays** after making a coloured derivative (sulphonamides by diazotisation and coupling, dextrose with anthrone or DNS reagent).
4. **Purity and impurity tests:** limit tests by absorbance (for example related substances that absorb where the drug does not).
5. **Determination of pKa**, dissociation constants and stability constants of complexes.
6. **Reaction kinetics and stability studies**, dissolution testing of tablets.
7. **Structure clues:** conjugation, presence of chromophores (Woodward–Fieser rules predict λmax of dienes and enones; not required in detail here).

### Spectrophotometric titrations

The end point is found by following absorbance during a titration. Absorbance (corrected for dilution) is plotted against titrant volume; the end point is where the two straight-line parts cross.

```text
  A  (a) titrant absorbs      (b) analyte absorbs     (c) product absorbs
  ^         /                 \                         ____
  |        /                   \                       /
  |  _____/                     \______               /
  +--------------> volume   +--------------> volume  +--------------> volume
       end point = break in the line
```

Advantages: works for very dilute solutions, coloured solutions and weak reactions where indicators fail; measures many points, so accuracy is good. Examples: titration of copper(II) with EDTA, iron(III) with EDTA using salicylic acid.

### Single-component analysis

Measure the absorbance at λmax and calculate the concentration by A(1%, 1 cm), against a standard, or from a calibration curve (absorbance of 5–6 standard solutions plotted against concentration).

### Multicomponent analysis

When two drugs absorb in the same region:

1. **Simultaneous equation (Vierordt's) method.** Measure the mixture at λ1 (λmax of X) and λ2 (λmax of Y). Absorbance is additive:
   - A1 = ax1·Cx + ay1·Cy
   - A2 = ax2·Cx + ay2·Cy
   - Solving: **Cx = (A2·ay1 − A1·ay2)/(ax2·ay1 − ax1·ay2)** and **Cy = (A1·ax2 − A2·ax1)/(ax2·ay1 − ax1·ay2)**, where a values are the absorptivities of the pure drugs at each wavelength (1 cm cell).
   - Condition for good results: the ratios (A2/A1)/(ax2/ax1) and (ay2/ay1)/(A2/A1) should lie outside about 0.1–2.0.
2. **Absorbance ratio (Q-value) method:** one wavelength is the **isosbestic point** (where both drugs have the same absorptivity) and the other is λmax of one drug.
3. **Derivative spectroscopy:** first or second derivative spectra resolve overlapping peaks; at the zero-crossing point of one drug only the other contributes.
4. **Difference spectrophotometry:** the drug is measured in two different forms (acid and alkali); interfering excipients that do not change cancel out.
5. **Geometric correction (Morton–Stubbs)**, used for vitamin A, and **multi-wavelength chemometric** methods.

Example (simultaneous equations, values for illustration only): with ax1 = 650, ay1 = 30, ax2 = 300, ay2 = 450 (A 1%, 1 cm) and mixture absorbances A1 = 0.540, A2 = 0.660, Cx = 0.000787 g/100 ml (**7.87 µg/ml**) and Cy = 0.000942 g/100 ml (**9.42 µg/ml**).

## 1.10 Fluorimetry: theory

Some molecules, after absorbing UV or visible light, give out part of the energy as light of a **longer** wavelength. This is **photoluminescence**: **fluorescence** if emission stops almost at once (about 10⁻⁹ to 10⁻⁶ s) and **phosphorescence** if it continues longer (10⁻⁴ s to many seconds).

### Singlet, doublet and triplet states

**Multiplicity = 2S + 1**, where S is the total spin.

| State | Electron spins | Multiplicity | Note |
| --- | --- | --- | --- |
| Singlet (S) | All paired (↑↓) | 2(0) + 1 = 1 | Ground state of most molecules (S0) and the first excited state S1 after absorption, spin unchanged |
| Doublet (D) | One unpaired electron | 2(½) + 1 = 2 | Free radicals |
| Triplet (T) | Two unpaired electrons with parallel spins (↑↑) | 2(1) + 1 = 3 | Excited state reached by spin inversion; lower in energy than the related singlet; paramagnetic |

### Jablonski diagram and energy-loss routes

```text
  S2 ======  (vibrational levels)
      |  internal conversion (IC)
  S1 ======-------- intersystem crossing (ISC) -------> T1 ======
      |      |                                           |     |
  abs |      | fluorescence (10^-9 to 10^-6 s)          phosph-|
  orp-|      |                                          orescence (slow)
  tion|      v                                           v     v
  S0 ======================================================  (ground state)
  Vibrational relaxation in each state is very fast (about 10^-12 s).
```

- **Vibrational relaxation:** loss of excess vibrational energy to the solvent within an electronic state.
- **Internal conversion:** radiationless move from a higher to a lower electronic state of the same multiplicity (S2 → S1).
- **External conversion:** radiationless loss of energy by collision with solvent or other molecules; increased by heat and low viscosity.
- **Intersystem crossing:** radiationless move between states of different multiplicity (S1 → T1); helped by heavy atoms (Br, I) and paramagnetic species.
- **Fluorescence:** S1 → S0 with emission. Because energy is lost first by vibrational relaxation, the emitted light has a longer wavelength than the absorbed light (**Stokes shift**). The emission spectrum is roughly a mirror image of the absorption band.
- **Phosphorescence:** T1 → S0, spin-forbidden and therefore slow.

**Quantum yield (φ)** = photons emitted/photons absorbed (0 to 1). For dilute solutions (absorbance below about 0.05):

**F = K φ I0 ε b c**, so fluorescence intensity is directly proportional to concentration. At higher concentrations the plot bends (inner filter effect, self-quenching).

## 1.11 Factors affecting fluorescence

1. **Structure and conjugation:** aromatic and fused rings with π → π* transitions fluoresce well (anthracene, quinine); aliphatic compounds rarely do.
2. **Rigidity:** rigid planar molecules fluoresce strongly because they cannot lose energy by internal vibrations (fluorescein is much more fluorescent than phenolphthalein, which has the same groups but no bridging oxygen).
3. **Substituents:** electron-donating groups (–OH, –NH2, –OCH3) usually increase fluorescence; electron-withdrawing groups (–NO2, –COOH) and heavy atoms (–Br, –I) decrease it.
4. **pH:** ionised and un-ionised forms fluoresce differently (aniline fluoresces in neutral or alkaline solution but not as the anilinium ion; quinine is measured in dilute sulphuric acid).
5. **Temperature:** rise in temperature increases collisions and lowers fluorescence.
6. **Viscosity:** higher viscosity lowers collisions and raises fluorescence.
7. **Dissolved oxygen:** paramagnetic oxygen quenches fluorescence; deaerate if needed.
8. **Concentration:** linear only at low concentration (inner filter effect and self-quenching at high concentration).
9. **Light exposure:** photodecomposition on long exposure to the exciting beam.
10. **Solvent:** polarity, hydrogen bonding and heavy-atom solvents change intensity and wavelength.

## 1.12 Quenching

**Quenching** is any process that lowers fluorescence intensity.

| Type | How it works | Example |
| --- | --- | --- |
| Collisional (dynamic) | The quencher collides with the excited molecule and takes its energy | Halide ions (Cl⁻, Br⁻, I⁻) with quinine; dissolved oxygen |
| Static | Quencher forms a non-fluorescent complex with the ground-state molecule | Complexes of fluorophores with metal ions |
| Concentration (self-quenching) | At high concentration, excited and ground-state molecules of the same substance interact; the solution also reabsorbs its own emission (inner filter) | Concentrated fluorescein |
| Chemical | The substance reacts and changes to a non-fluorescent form | pH change, oxidation |
| Temperature | Heat increases collisional deactivation | Warm solutions read lower |

**Stern–Volmer equation** (collisional quenching): **F0/F = 1 + Ksv[Q]**, where F0 and F are intensities without and with quencher and Ksv is the Stern–Volmer constant. A plot of F0/F against [Q] is a straight line with slope Ksv. Example: F0 = 100, F = 80 at [Cl⁻] = 0.01 M gives F0/F = 1.25 and Ksv = 25 M⁻¹; at 0.04 M, F = 50 gives the same Ksv.

## 1.13 Instrumentation of fluorimetry

```text
 FLUORIMETER / SPECTROFLUORIMETER

 [Source] -> [Excitation filter or monochromator] -> [Sample cell (all 4 sides clear)]
 xenon arc or                                               |
 mercury lamp                                               | emitted light taken at 90 degrees
                                                            v
                                  [Emission filter or monochromator] -> [Detector: PMT] -> [Readout]
```

- **Source:** xenon arc lamp (continuous, intense, 250–600 nm) or mercury vapour lamp (lines at 254, 365, 405, 436 nm).
- **Excitation and emission selectors:** filters in a **filter fluorimeter**; grating monochromators in a **spectrofluorimeter**, which can record both excitation and emission spectra.
- **Sample cell:** quartz (or glass for visible work) with **all four sides polished**, because emission is collected at 90°.
- **Geometry:** the detector is placed at **right angles** to the incident beam so that transmitted exciting light does not reach it.
- **Detector:** photomultiplier tube (fluorescence signals are weak).
- **Double-beam fluorimeters** split the source beam to a reference to correct for lamp fluctuation.
- Calibrate with a standard such as **quinine sulphate in 0.05 M (0.1 N) sulphuric acid** (excitation about 350 nm, emission about 450 nm).

## 1.14 Applications of fluorimetry

1. **Very sensitive assays** (ng/ml range, often 10–1000 times more sensitive than absorption): quinine, riboflavin, thiamine (oxidised to fluorescent thiochrome), vitamin A, adrenaline and noradrenaline (trihydroxyindole method), reserpine, LSD.
2. **Drugs in biological fluids** at low levels, and enzyme assays using fluorogenic substrates.
3. **Derivatisation** of non-fluorescent compounds: amino acids and amines with fluorescamine, dansyl chloride or o-phthalaldehyde.
4. **Fluorescence detectors in HPLC** and fluorescence in TLC visualisation.
5. **Inorganic analysis** using fluorescent chelates (aluminium with morin, zinc with 8-hydroxyquinoline).
6. **Fluorescence quenching** to estimate halides and to study drug–protein binding.

**Advantages:** high sensitivity and selectivity (two wavelengths are chosen). **Limitations:** few compounds fluoresce naturally, results are affected by temperature, pH, impurities and quenchers, and calibration is linear over a narrow range.

## Remember

- E = hc/λ; A = εbc = 2 − log %T; ε = A(1%, 1 cm) × M/10; keep A between 0.2 and 0.8.
- Transition energy order: σ → σ* > n → σ* > π → π* > n → π*; K band intense, R band weak.
- Polar solvent: π → π* red shift, n → π* blue shift.
- Deviations: real, chemical, instrumental (stray light and polychromatic light give negative deviation).
- Sources D2 (UV) and tungsten-halogen (visible); quartz cells for UV; detectors photovoltaic cell, phototube, PMT, silicon photodiode.
- Simultaneous equation: Cx = (A2ay1 − A1ay2)/(ax2ay1 − ax1ay2).
- Fluorescence S1 → S0 fast; phosphorescence T1 → S0 slow; emission at a longer wavelength (Stokes shift); detector at 90°.
- F = Kφ I0 εbc in dilute solution; Stern–Volmer F0/F = 1 + Ksv[Q].
