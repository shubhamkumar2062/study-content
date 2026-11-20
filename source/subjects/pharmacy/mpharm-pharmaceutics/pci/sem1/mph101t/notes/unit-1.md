# Unit 1: UV-visible, IR, spectrofluorimetry, flame emission and atomic absorption spectroscopy

This unit covers four optical methods. UV-visible and fluorescence spectroscopy look at electronic transitions in molecules, IR looks at molecular vibrations, and flame emission and atomic absorption look at electronic transitions in free atoms. At M.Pharm level you are expected to go beyond "principle and block diagram": explain why the laws fail, how the optics are built, why one detector or sample technique is chosen over another, and how each method supports formulation work (assay, dissolution, compatibility, impurity and trace-metal testing).

## 1.1 Electromagnetic radiation and the spectroscopic regions

Radiation has wave and particle character. The photon energy is **E = hν = hc/λ = hcν̄**, where h is Planck's constant (6.626 × 10⁻³⁴ J s), c the speed of light, λ the wavelength and ν̄ = 1/λ the wavenumber (cm⁻¹).

| Region | Range | Molecular event | Technique |
| --- | --- | --- | --- |
| X-ray | 0.01–10 nm | Inner-shell electrons, diffraction by crystal planes | XRD (Unit 5) |
| UV | 200–400 nm (vacuum UV below 200 nm) | Outer-electron (valence) transitions | UV spectroscopy |
| Visible | 400–800 nm | Valence transitions in coloured species | Colorimetry |
| Near IR | 0.8–2.5 µm (12,500–4000 cm⁻¹) | Overtones and combination bands | NIR (tablet blend, moisture) |
| Mid IR | 2.5–25 µm (4000–400 cm⁻¹) | Fundamental vibrations | IR / FTIR |
| Radio frequency | metres | Nuclear spin flips in a magnetic field | NMR (Unit 2) |

**Absorption** means the photon energy exactly matches a gap between two quantised levels. **Emission** is the reverse: an excited species loses energy as light. UV, IR and AAS are absorption methods; fluorimetry and flame emission are emission methods.

## Part A — UV-visible spectroscopy

## 1.2 Theory: electronic transitions

Valence electrons occupy σ (single bonds), π (multiple bonds) and n (lone pairs) orbitals. Absorption promotes an electron to an empty antibonding orbital (σ* or π*).

```text
 Energy
   ^   σ*  ____________
   |   π*  ____________      allowed / observed in 200–800 nm:
   |   n   ____________        π→π*  (strong, ε > 10^4, K band)
   |   π   ____________        n→π*  (weak, ε < 100, R band)
   |   σ   ____________      σ→σ* and n→σ* mostly below 200 nm
 Gap size: σ→σ* > n→σ* > π→π* > n→π*
```

- **σ → σ\***: below 150 nm; saturated hydrocarbons (hexane, cyclohexane) are therefore transparent and make good UV solvents.
- **n → σ\***: 150–250 nm; alcohols, amines, alkyl halides.
- **π → π\***: isolated C=C about 170–190 nm; moves into the measurable UV with conjugation; high ε.
- **n → π\***: carbonyl, nitro, azo groups around 270–350 nm; symmetry-forbidden, so weak.
- **Charge-transfer bands**: very intense bands where an electron moves from a donor part to an acceptor part of a complex (iron–thiocyanate, many drug–reagent complexes used in colorimetry).
- **d–d transitions**: weak bands of transition-metal complexes in the visible region.

Benzene shows three bands: E1 (about 184 nm), E2 (about 204 nm) and the fine-structured B band near 255 nm. Substituents and solvents shift and smooth them.

**Chromophore** = the group responsible for absorption (C=C, C=O, NO2, N=N, aromatic ring). **Auxochrome** = a saturated group with lone pairs (–OH, –NH2, –OR, –Cl) that does not absorb above 200 nm by itself but extends conjugation when attached to a chromophore, moving the band to longer wavelength and raising its intensity.

**Shifts**: bathochromic (red, longer λ), hypsochromic (blue, shorter λ), hyperchromic (higher ε), hypochromic (lower ε). Phenol → phenoxide in alkali gives a red and hyperchromic shift; aniline → anilinium in acid gives a blue shift because the lone pair is tied up by the proton.

**Woodward–Fieser rules** let you predict λmax of conjugated dienes and α,β-unsaturated carbonyl compounds: start with a base value for the parent system and add fixed increments for each extra double bond, exocyclic double bond, ring residue and auxochrome. Fieser–Kuhn rules extend this to long polyenes such as carotenoids. These rules are used to check a proposed structure, for example of a steroid enone.

## 1.3 Laws of absorption

**Lambert's law:** each layer of equal thickness absorbs an equal fraction of the light passing through it, so intensity falls exponentially with path length.

**Beer's law:** absorbance is proportional to the concentration of the absorbing species.

Combined (**Beer–Lambert law**):

```text
 T = I/I0          A = log10(I0/I) = −log T = 2 − log(%T)
 A = ε b c         (ε in L mol⁻¹ cm⁻¹, b in cm, c in mol/L)
 A = A(1%, 1 cm) × b × c   (c in g/100 mL)
 ε = A(1%, 1 cm) × M / 10
```

**Worked example.** Paracetamol has A(1%, 1 cm) = 715 at 257 nm (in dilute alkali). A diluted tablet solution reads A = 0.572 in a 1 cm cell. c = 0.572 / 715 = 0.000800 g/100 mL = 0.800 mg/100 mL = 8.00 µg/mL. With M = 151.16, ε = 715 × 151.16 / 10 ≈ 10,800 L mol⁻¹ cm⁻¹.

Absorbance is additive: in a mixture, A(λ) = Σ εᵢ b cᵢ at each wavelength. This is the basis of multicomponent analysis.

**Deviations from Beer's law**

| Type | Cause | Remedy |
| --- | --- | --- |
| Real (fundamental) | Above about 0.01 M, molecules interact and the refractive index changes, so ε changes | Work in dilute solution |
| Chemical | Association, dissociation, polymerisation, complexation, acid–base equilibria (e.g. dichromate ⇌ chromate with pH; indicators) | Buffer the solution; measure at an isosbestic point |
| Instrumental | Polychromatic light (worst on a steep slope of the band), stray light (causes negative deviation at high A), mismatched cells, noise at very low or high A | Measure at λmax, narrow slit, keep A between about 0.2 and 0.8, matched cells |

Photometric error is smallest near A ≈ 0.43 (T ≈ 37%) for an instrument limited by constant reading error; this is why assays are designed to read in the middle of the range.

## 1.4 Instrumentation

```text
 Source → Monochromator → Sample cell → Detector → Amplifier/processor → Display
 (single-beam)

 Double-beam:          ┌→ Reference cell →┐
 Source → Mono → Chopper/beam splitter      ├→ Detector → ratio I/I0 → readout
                       └→ Sample cell ─────→┘
```

**Sources**
- Deuterium (or hydrogen) discharge lamp: continuous UV, about 160–380 nm.
- Tungsten–halogen lamp: visible and near IR, about 350–2500 nm; the halogen cycle keeps the bulb clean and lengthens life.
- Xenon arc lamp: very bright over UV and visible; used in fluorimeters and some diode-array instruments.

**Wavelength selectors**
- Filters (absorption or interference) in colorimeters.
- Prism monochromators (quartz for UV, glass for visible): dispersion is non-linear.
- Diffraction gratings (reflection, holographic): linear dispersion, used in all modern instruments. Grating equation: nλ = d(sin i ± sin r). Higher groove density gives better resolution.
- Slits set the spectral bandwidth; a narrow slit improves resolution but cuts light.

**Sample cells**: quartz or fused silica below about 350 nm; glass or plastic only in the visible. Standard path length 1 cm; matched pairs for double-beam work.

**Detectors**
- Barrier-layer (photovoltaic) cell: cheap colorimeters, no power supply, low sensitivity.
- Phototube: photoemissive cathode, current proportional to light.
- **Photomultiplier tube (PMT)**: the photoelectron is multiplied through 9–10 dynodes, giving very high gain; the standard for scanning instruments and fluorimeters.
- **Photodiode array (PDA/DAD)**: hundreds of diodes record the whole spectrum at once after the sample (reversed optics, polychromator after the cell). Fast, used as an HPLC detector and for peak-purity checks.
- Charge-coupled devices (CCD) in compact spectrometers.

**Single vs double beam**: double beam compensates for source drift and solvent absorbance continuously, so it gives stable baselines for scanning; single beam is simpler and has more energy throughput.

**Instrument qualification (IP general chapter)**: wavelength accuracy (holmium oxide filter or solution, deuterium lines), absorbance accuracy (potassium dichromate in 0.005 M H2SO4), stray light (potassium chloride 1.2% w/v cuts off below about 200 nm), and resolution (toluene in hexane, ratio of peak to trough).

## 1.5 Choice of solvent and solvent effects

A UV solvent must be transparent at the working wavelength, dissolve the drug, not react with it, and be of spectroscopic grade. The **UV cut-off** is the wavelength below which the solvent itself absorbs strongly.

| Solvent | Approximate cut-off (nm) |
| --- | --- |
| Water | 190 |
| Acetonitrile | 190 |
| Hexane, cyclohexane | 200–210 |
| Methanol, ethanol | 205–210 |
| Chloroform | 245 |
| Acetone | 330 |

**Solvent effects**
- π → π\*: the excited state is more polar than the ground state, so a polar solvent stabilises it more → **red shift** on going from hexane to ethanol.
- n → π\*: the lone pair is hydrogen-bonded and stabilised in polar protic solvents → larger gap → **blue shift**. This difference is a classic test to identify the type of transition.
- Polar solvents also smooth out vibrational fine structure (benzene's B band is sharp in hexane, blurred in ethanol).
- pH is a "solvent effect" for ionisable drugs. IP and BP monographs often specify 0.1 M HCl or 0.1 M NaOH for this reason.

## 1.6 Applications of UV-visible spectroscopy

1. **Assay** of drugs by A(1%, 1 cm), by comparison with a reference standard, or by a calibration curve.
2. **Multicomponent analysis** of combination dosage forms:
   - Simultaneous equations (Vierordt's method): measure A at λmax of each drug and solve two equations in two unknowns.
   - Absorbance ratio (Q-value) method using an isoabsorptive point.
   - Derivative spectrophotometry (first to fourth derivative) to resolve overlapping bands and remove background.
   - Difference spectrophotometry (ΔA between acid and alkaline solutions) to remove interference from excipients.
   - Area under curve and chemometric (multivariate) methods.
3. **Dissolution testing** and release kinetics — the most common use in formulation research.
4. **Drug–excipient and drug–cyclodextrin interaction** studies; stability constants of complexes (Job's method of continuous variation, mole-ratio method, Benesi–Hildebrand plot).
5. **pKa determination** from absorbance at different pH values.
6. **Kinetics and stability** studies (rate of degradation followed by absorbance).
7. **Purity**: limit tests based on absorbance (e.g. a specified impurity absorbing at another wavelength), peak purity with a diode array.
8. **Colorimetry** after derivatisation: Bratton–Marshall for primary aromatic amines (sulphonamides), ferric chloride for phenols, ninhydrin for amino acids, MBTH, folin reagents.
9. **Structure support**: conjugation, Woodward–Fieser predictions, cis/trans isomers (trans usually has higher λmax and ε).

## Part B — Infrared spectroscopy

## 1.7 Theory

Atoms in a bond vibrate like balls on a spring. A vibration absorbs IR only if it **changes the dipole moment** of the molecule (selection rule). Symmetric stretching of CO2 and the stretching of homonuclear diatomic molecules (N2, O2) are IR-inactive but Raman-active.

**Hooke's law** gives the stretching wavenumber:

```text
 ν̄ = (1 / 2πc) × √(k / µ)          µ = m1·m2 / (m1 + m2)
 k = force constant (N/m),  µ = reduced mass (kg),  c in cm/s
```

Worked check (k values are typical): C=O with k ≈ 1200 N/m gives about 1720 cm⁻¹; C–H with k ≈ 500 N/m gives about 3030 cm⁻¹; C–C with k ≈ 500 N/m gives about 1190 cm⁻¹. Replacing H by D in C–H drops the band by a factor of about 1.36 (to about 2225 cm⁻¹) because µ nearly doubles; deuterium exchange is used to confirm O–H and N–H bands.

Real bonds are **anharmonic**, so overtones (2ν, 3ν, weak) and combination bands appear, and the energy gaps narrow at higher levels.

## 1.8 Modes of molecular vibration

Number of fundamental vibrations: **3N − 6** for a non-linear molecule, **3N − 5** for a linear one (N = atoms). Water has 3, CO2 has 4, benzene has 30.

```text
 Stretching (bond length changes)        Bending (bond angle changes)
   symmetric   ← O →  ← O →                in-plane:  scissoring, rocking
   asymmetric  → O ←  ← O                  out-of-plane: wagging, twisting
 Stretching needs more energy (higher ν̄) than bending.
```

Fewer bands are seen than predicted because some modes are IR-inactive, degenerate (same energy), too weak, or outside the instrument range. Extra bands come from overtones, combination bands and **Fermi resonance** (a fundamental and an overtone of similar energy and same symmetry mix and split — the aldehyde C–H doublet near 2820 and 2720 cm⁻¹ is the classic example).

**Regions of the spectrum**

| Region (cm⁻¹) | Assignment |
| --- | --- |
| 3650–3200 | O–H (free sharp near 3600; H-bonded broad), N–H |
| 3300–2700 | C–H (≡C–H ~3300, =C–H above 3000, sp3 C–H below 3000), carboxylic O–H very broad 3300–2500 |
| 2260–2100 | C≡N, C≡C |
| 1850–1650 | C=O (anhydride, acid chloride high; ester ~1735; ketone ~1715; amide ~1650) |
| 1680–1450 | C=C, aromatic ring, N–H bending |
| 1500–600 | **Fingerprint region**: C–O, C–N, C–X, skeletal bending — unique to each molecule |

## 1.9 Factors affecting vibrational frequencies

1. **Bond strength and atomic mass** (Hooke's law): triple > double > single; lighter atoms higher.
2. **Coupled vibrations**: two identical groups sharing an atom give symmetric and asymmetric bands (CH2, NH2, anhydride C=O doublet near 1820 and 1760 cm⁻¹).
3. **Electronic effects**: electron-withdrawing groups by induction raise C=O frequency (acid chloride ~1800); **conjugation/resonance** lowers it (α,β-unsaturated ketone ~1675, aryl ketone ~1690); amide C=O is low (~1650) because of resonance with the nitrogen lone pair.
4. **Hydrogen bonding**: lowers and broadens O–H and N–H bands. Intermolecular H-bonds weaken on dilution (band moves back towards the free value); intramolecular H-bonds do not change with dilution — a test to tell them apart.
5. **Ring strain**: small-ring ketones absorb higher (cyclobutanone ~1780, cyclopentanone ~1745, cyclohexanone ~1715).
6. **Fermi resonance** and **field effects** (through-space interaction of nearby dipoles).
7. **Physical state and solvent**: solid-state spectra differ from solution; polymorphs give different spectra in the solid state.

## 1.10 Sample handling

| Sample | Technique | Notes |
| --- | --- | --- |
| Solid | KBr pellet (about 1 mg drug ground with 100–200 mg dry KBr, pressed into a disc) | KBr is IR-transparent; must be dry (water bands at 3450 and 1640 cm⁻¹); grinding and pressure can convert polymorphs or cause ion exchange with hydrochlorides |
| Solid | Nujol mull (paraffin oil paste between salt plates) | Nujol bands hide C–H regions; hexachlorobutadiene mull covers them |
| Solid | Solid film cast from a volatile solvent | For polymers and films |
| Liquid | Neat film between NaCl or KBr plates | Plates are water-soluble; keep dry |
| Solution | Sealed cell (0.1–1 mm) with CCl4, CS2 or CHCl3 | Solvent bands must be subtracted |
| Gas | Long-path cell (10 cm or multi-pass) | Residual solvents, gases |
| Any surface | **ATR** (attenuated total reflectance; diamond or ZnSe crystal) | No preparation; evanescent wave penetrates a few µm; standard for tablets, films, polymers |
| Powders | Diffuse reflectance (DRIFTS) | Minimal preparation |

## 1.11 Instrumentation: dispersive vs FTIR

**IR sources**: Nernst glower (rare-earth oxides heated electrically), globar (silicon carbide rod), nichrome coil. All emit as hot bodies.

**Detectors**
- Thermal: thermocouple/thermopile, bolometer (resistance change), Golay cell (gas expansion moves a mirror). Slow; used in dispersive instruments.
- Pyroelectric: deuterated triglycine sulphate (DTGS) — fast enough for FTIR, works at room temperature.
- Photon (quantum): mercury cadmium telluride (MCT), cooled with liquid nitrogen; fastest and most sensitive.

**Dispersive (double-beam, optical null) spectrometer**

```text
 Source → splits → sample beam  ─┐
               → reference beam ─┴→ rotating sector mirror (chopper) → grating
               monochromator → slit → thermal detector → amplifier
               → servo moves an attenuator (comb) in the reference beam until
                 both beams are equal → pen records %T vs wavenumber
```

**Fourier-transform IR (FTIR)** uses a **Michelson interferometer**.

```text
            Fixed mirror
                 |
 Source → Beam splitter ⇄ Moving mirror (path difference δ)
                 |
            Sample → Detector (DTGS/MCT) → interferogram I(δ)
            → Fourier transform (computer) → spectrum I(ν̄)
 He–Ne laser fringes give the exact mirror position (wavenumber accuracy).
```

**Advantages of FTIR**
- **Fellgett (multiplex) advantage**: all wavelengths measured at once → many scans averaged quickly → better signal-to-noise.
- **Jacquinot (throughput) advantage**: no slits, more energy reaches the detector.
- **Connes advantage**: laser-referenced wavenumber accuracy, so spectra can be co-added and subtracted.
- Fast scanning allows hyphenation (GC–IR, TGA–IR), ATR and microscopy.

## 1.12 Applications of IR

1. **Identification** of drugs by comparison with a reference spectrum (IP identity test A for many drugs); the fingerprint region is decisive.
2. **Functional group and structure** elucidation together with NMR and MS.
3. **Polymorphism and solvates** in the solid state; **drug–excipient compatibility** (disappearance or shift of a band in a physical mixture); drug–polymer interaction in solid dispersions and complexes (hydrogen-bond shifts).
4. Following reactions and degradation (loss of ester C=O, appearance of acid O–H).
5. Quantitative analysis (baseline method) — less common than UV because of lower precision.
6. **NIR** in process analytical technology: blend uniformity, moisture, raw material identification through packaging.
7. Hydrogen-bond studies, cis/trans isomers, residual solvent in gases.

## Part C — Spectrofluorimetry

## 1.13 Theory of fluorescence

After absorption, a molecule is in a vibrational level of an excited singlet state (S1 or S2). It loses energy by several routes, shown in the **Jablonski diagram**.

```text
 S2 ────────           
    ↓ internal conversion (non-radiative, fast)
 S1 ────────   ── intersystem crossing (spin flip) ──→  T1 ────────
  ↑    │                                                  │
  │ absorption   fluorescence (10⁻⁹–10⁻⁷ s)           phosphorescence
  │    ↓                                               (10⁻⁴ s to seconds)
 S0 ────────  ←───────────────────────────────────────────┘
 Vibrational relaxation in each state occurs before emission.
```

- **Fluorescence**: emission from S1 to S0, same spin multiplicity, very fast.
- **Phosphorescence**: emission from T1 to S0, spin-forbidden, slow, needs rigid media or low temperature (liquid nitrogen) to be seen.
- **Stokes shift**: emission occurs at a longer wavelength than excitation because energy is lost by vibrational relaxation. The emission spectrum is often a mirror image of the absorption band.
- **Quantum yield (Φ)** = photons emitted / photons absorbed (0 to 1).
- **Fluorescence intensity**: F = K Φ I0 (1 − 10^(−εbc)); for dilute solutions (A below about 0.05), F ≈ 2.303 K Φ I0 ε b c, i.e. linear in concentration. At higher concentrations it bends and then falls.

**Why fluorimetry is more sensitive than absorption**: the signal is measured against a dark background (at 90° to the incident beam) and can be increased by increasing source intensity, whereas absorption measures a small difference between two large signals. Fluorimetry often reaches ng/mL levels, 10–1000 times lower than UV. It is also more selective because both excitation and emission wavelengths are chosen.

## 1.14 Factors affecting fluorescence

1. **Structure**: rigid, planar, conjugated aromatic systems fluoresce (fluorescein, quinine, anthracene). Rigidity reduces loss by vibration. Electron-donating groups (–OH, –NH2, –OCH3) usually enhance; electron-withdrawing groups (–NO2, –COOH) and heavy atoms (Br, I) reduce it — heavy atoms promote intersystem crossing to the triplet (heavy-atom effect).
2. **Temperature**: higher temperature → more collisions → lower fluorescence.
3. **Solvent**: viscosity (higher viscosity → fewer collisions → more fluorescence); heavy-atom solvents quench; polarity shifts bands.
4. **pH**: ionised and un-ionised forms fluoresce differently (quinine fluoresces strongly in dilute sulphuric acid).
5. **Dissolved oxygen**: paramagnetic quencher.
6. **Concentration**: self-quenching and the **inner-filter effect** — at high concentration the solution absorbs most of the exciting light near the front of the cell (primary inner filter) or re-absorbs emitted light (secondary), so the plot bends.
7. **Photodecomposition** under intense light — use short exposure.
8. **Scattering**: Rayleigh scatter at the excitation wavelength and Raman scatter of the solvent can appear in the emission spectrum.

## 1.15 Quenchers and quenching

**Quenching** is any process that reduces fluorescence intensity.

| Type | Mechanism | Example |
| --- | --- | --- |
| Dynamic (collisional) | The quencher collides with the excited molecule during its lifetime; lifetime falls | Halide ions (iodide > bromide > chloride) quench quinine; oxygen |
| Static | The quencher forms a non-fluorescent ground-state complex; lifetime of the remaining fluorophore unchanged | Complexation with metal ions |
| Self-quenching / concentration | Fluorophore molecules quench each other; inner filter | Concentrated solutions |
| Energy transfer (FRET) | Non-radiative transfer to a nearby acceptor, distance-dependent (r⁻⁶) | Used as a molecular ruler in biophysics and assays |

**Stern–Volmer equation**: F0/F = 1 + K_SV [Q] = 1 + kq τ0 [Q]. A plot of F0/F against [Q] is linear for one type of quenching. Example: F0 = 100, F = 60 at [Q] = 0.02 M gives K_SV = (100/60 − 1)/0.02 = 33.3 L/mol. Dynamic quenching falls at low temperature and lowers lifetime; static quenching rises at low temperature (complexes more stable).

## 1.16 Instrumentation

```text
                     Emission monochromator → PMT → amplifier → readout
                              ↑ (at 90°)
 Xenon lamp → Excitation monochromator → Sample cell (quartz, 4 clear sides)
                                         → transmitted beam to a light trap
 (Fluorimeter: filters instead of monochromators.
  Spectrofluorimeter: two grating monochromators; ratio mode with a reference PMT.)
```

- Source: xenon arc (continuous, intense); mercury vapour lamp (line source) in filter fluorimeters; lasers and LEDs in detectors.
- Two wavelength selectors: excitation and emission.
- Cell: quartz, polished on all four sides; 90° geometry minimises the transmitted and scattered light reaching the detector. Front-face geometry is used for opaque or very concentrated samples.
- Detector: PMT, often photon counting.
- Corrected spectra need the lamp output and detector response to be accounted for.

## 1.17 Applications of fluorimetry

1. Assay of naturally fluorescent drugs: quinine, riboflavin, thiamine (as thiochrome after oxidation), adrenaline and noradrenaline (as trihydroxyindoles), morphine, tetracyclines, reserpine, warfarin.
2. **Derivatisation** of non-fluorescent drugs: dansyl chloride, fluorescamine and o-phthalaldehyde (OPA) with primary amines; NBD-Cl.
3. **Bioanalysis** at ng/mL levels; fluorescence detectors in HPLC.
4. Inorganic analysis with fluorescent chelates (aluminium with alizarin garnet R, etc.).
5. **Protein binding and conformation** (intrinsic tryptophan fluorescence quenching by a drug), membrane studies with probes.
6. **Formulation research**: critical micelle concentration with pyrene, encapsulation and release from liposomes/nanoparticles (calcein, FITC-dextran), FRET-based stability of nanocarriers.
7. Immunoassays (fluorescence polarisation, time-resolved fluorescence).

## Part D — Flame emission and atomic absorption spectroscopy

## 1.18 Principle

Both methods turn the sample into a cloud of free, ground-state atoms (atomisation) and then look at sharp **atomic lines** (line width about 0.002–0.005 nm).

```text
 Solution → nebuliser → fine aerosol → flame:
   desolvation (solvent lost) → vaporisation (solid particles) →
   atomisation (MX → M + X) → some atoms excited (M*) or ionised (M⁺)
 FES/flame photometry: measures light EMITTED as M* → M (intensity ∝ concentration)
 AAS: measures light ABSORBED by ground-state M from a line source (A ∝ concentration)
```

The **Boltzmann distribution** decides how many atoms are excited: Nj/N0 = (gj/g0) e^(−ΔE/kT). At flame temperatures, only a tiny fraction (about 10⁻⁴ for sodium, far less for zinc) is excited. So:
- Emission depends strongly on flame temperature (sensitive to fluctuations) and works best for easily excited alkali and alkaline-earth metals (Na 589 nm, K 766.5 nm, Li 670.8 nm, Ca 622 nm band of CaOH).
- Absorption uses the large ground-state population, so AAS is less temperature-dependent and works for about 70 elements.

## 1.19 Instrumentation

**Flame photometer / flame emission spectrometer**

```text
 Fuel + oxidant → burner ← nebuliser ← sample
        flame → lens → filter or monochromator → photocell/PMT → readout
```

**Atomic absorption spectrometer**

```text
 Hollow cathode lamp → chopper → flame (or graphite furnace) → monochromator
   (element-specific)  (modulates)   (atomic vapour)          → PMT → lock-in
   + deuterium lamp for background correction                   amplifier → A
```

- **Hollow cathode lamp (HCL)**: cathode made of the element being measured, filled with neon or argon at low pressure. Gas ions sputter metal atoms from the cathode and excite them, so the lamp emits the element's own narrow lines — narrower than the absorption line, which is why Beer's law can apply to atoms. Electrodeless discharge lamps give more intensity for volatile elements (As, Se).
- **Chopper and modulation**: the lamp signal is pulsed and the amplifier responds only to the pulsed signal, so the steady emission from the flame itself is rejected.
- **Nebuliser–burner**: premix (laminar flow) burner with a long slot (about 10 cm) for a long absorption path. Total-consumption burners are used in older flame photometers.
- **Flames**: air–acetylene (about 2300 °C) for most metals; nitrous oxide–acetylene (about 2700–2800 °C) for refractory elements (Al, Si, Ti, V) that form stable oxides; air–propane/natural gas (about 1700–1900 °C) in flame photometers.
- **Electrothermal (graphite furnace) AAS**: a small volume (µL) is dried, ashed and atomised in a graphite tube; detection limits 100–1000 times lower than flame (µg/L). **Hydride generation** (As, Se, Sb, Bi) and **cold vapour** (Hg) are special atomisers.
- Monochromator: grating; detector: PMT.

## 1.20 Interferences and their control

| Interference | What happens | Control |
| --- | --- | --- |
| Spectral | Overlap of another line or band, molecular absorption, scattering by particles | Narrow bandpass, alternative line; **background correction** with a deuterium lamp, Zeeman effect or Smith–Hieftje (self-reversal) |
| Chemical | Formation of stable, non-volatile compounds: phosphate or sulphate with calcium (Ca₃(PO₄)₂) | **Releasing agent** (lanthanum or strontium chloride binds phosphate); **protective agent** (EDTA, 8-hydroxyquinoline); hotter N2O–acetylene flame |
| Ionisation | In hot flames easily ionised atoms (K, Na) lose electrons, reducing neutral atoms | Add an **ionisation suppressor** (excess of a more easily ionised element such as caesium or potassium chloride); cooler flame |
| Physical / matrix | Differences in viscosity, surface tension, dissolved solids change nebulisation rate | Matrix-matched standards, **standard addition method**, internal standard (lithium in flame photometry), dilution |
| Self-absorption (emission) | Cooler outer flame atoms absorb emitted light at high concentration → curve bends | Work at low concentration |

**Standard addition**: add known increments of analyte to equal portions of the sample, plot signal against added amount and extrapolate to zero signal; the x-intercept gives the sample concentration. It compensates for matrix effects.

**Comparison**

| Feature | Flame photometry (FES) | AAS |
| --- | --- | --- |
| Measures | Emitted light from excited atoms | Light absorbed by ground-state atoms |
| Source | The flame itself | Hollow cathode lamp for each element |
| Temperature dependence | High | Low |
| Elements | Mainly Na, K, Li, Ca, Ba | About 70 metals and metalloids |
| Sensitivity | Good for alkali metals | Generally better; graphite furnace much better |
| Cost | Low | Higher |

## 1.21 Applications

1. **Na, K, Ca, Li** in IV fluids, oral rehydration salts, dialysis solutions, serum (flame photometry).
2. **Trace and toxic metals** by AAS: Pb, Cd, As, Hg in raw materials and herbal products; elemental impurities testing following ICH Q3D risk assessment (ICP-MS and ICP-OES are now preferred for multi-element work).
3. Metals in drugs: zinc in insulin preparations, calcium in calcium salts, magnesium in antacids, iron in haematinics, platinum in cisplatin, lithium in lithium carbonate tablets.
4. Catalyst residues (Pd, Ni, Pt) in APIs.
5. Biological and environmental samples; water quality.

## Remember

- E = hν = hc/λ; UV electronic, IR vibrational, NMR nuclear spin.
- A = εbc = 2 − log %T; ε = A(1%, 1 cm) × M/10; best precision around A 0.2–0.8; deviations are real, chemical and instrumental.
- π→π\* red-shifts and n→π\* blue-shifts in polar solvents; quartz cells below 350 nm; D2 lamp for UV, tungsten–halogen for visible.
- 3N − 6 / 3N − 5 modes; IR needs a change in dipole moment; ν̄ = (1/2πc)√(k/µ); FTIR = Michelson interferometer with Fellgett, Jacquinot and Connes advantages.
- Fluorescence S1 → S0 in nanoseconds; Stokes shift; detector at 90°; F linear only for A below about 0.05; F0/F = 1 + K_SV[Q].
- FES measures emission and is temperature-sensitive; AAS measures absorption by ground-state atoms from a hollow cathode lamp; releasing agents for phosphate, ionisation suppressors for alkali metals, standard addition for matrix effects.
