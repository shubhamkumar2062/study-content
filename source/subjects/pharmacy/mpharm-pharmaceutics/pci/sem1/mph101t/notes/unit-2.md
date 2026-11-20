# Unit 2: NMR spectroscopy

Nuclear magnetic resonance (NMR) spectroscopy tells you how many kinds of hydrogen (or carbon) a molecule has, how many of each, what electronic environment each is in, and which atoms are next to each other. It is the single most powerful tool for proving the structure of a drug, an impurity or a degradation product, and it is increasingly used in formulation science (drug–excipient interaction, cyclodextrin inclusion, polymer composition, quantitative NMR). This unit follows the PCI topic list: quantum numbers, principle, instrumentation, solvents, relaxation, signals, chemical shift and its factors, spin–spin coupling, coupling constants, double resonance, FT-NMR, ¹³C NMR and applications.

## 2.1 Nuclear spin and quantum numbers

Protons and neutrons each have spin. A nucleus has a net **spin quantum number I** that depends on its numbers of protons and neutrons.

| Mass number | Atomic number | I | Examples | NMR active? |
| --- | --- | --- | --- | --- |
| Even | Even | 0 | ¹²C, ¹⁶O, ³²S | No |
| Odd | Even or odd | Half-integer (1/2, 3/2, 5/2) | ¹H, ¹³C, ¹⁵N, ¹⁹F, ³¹P (all I = 1/2); ¹¹B (3/2), ¹⁷O (5/2) | Yes |
| Even | Odd | Integer (1, 2, 3) | ²H, ¹⁴N (I = 1) | Yes (quadrupolar) |

A nucleus with spin has angular momentum and a **magnetic moment µ**. In an external magnetic field B0, quantum mechanics allows only **2I + 1 orientations**, described by the **magnetic quantum number m** = I, I − 1, …, −I.

- For ¹H (I = 1/2): two states, m = +1/2 (aligned with the field, lower energy, often called α) and m = −1/2 (opposed, higher energy, β).
- For ²H or ¹⁴N (I = 1): three states (+1, 0, −1).

**Quadrupolar nuclei** (I ≥ 1) have a non-spherical charge distribution; they relax very quickly, give broad lines and usually do not show clean coupling to protons. This is why N–H protons often appear as broad signals, and why deuterium (I = 1) in deuterated solvents does not split proton signals in an ordinary way.

Nuclei with I = 1/2 have spherical charge distribution, narrow lines and simple spectra — which is why ¹H, ¹³C, ¹⁹F and ³¹P are the routine nuclei.

## 2.2 Principle: resonance and the Larmor frequency

In the field B0 the magnetic moment does not simply line up; it **precesses** around the field direction like a spinning top in gravity. The precession (Larmor) frequency is:

```text
 ν0 = γ B0 / 2π           γ = gyromagnetic (magnetogyric) ratio, a constant for each nucleus
 ΔE = h ν0 = h γ B0 / 2π   (energy gap between the two spin states)
```

**Resonance** occurs when radio-frequency radiation of exactly ν0 is applied: the nucleus absorbs energy and flips from the lower to the upper spin state. The gap grows with field strength, so stronger magnets give higher frequencies.

| B0 (tesla) | ¹H frequency (MHz) |
| --- | --- |
| 1.41 | 60 |
| 7.05 | 300 |
| 9.40 | 400 |
| 11.7 | 500 |

At 9.4 T, ¹³C resonates at about 100.6 MHz, roughly a quarter of the proton frequency, because its γ is about one quarter of the proton's.

**Population difference.** The energy gap is tiny, so by the Boltzmann distribution the two spin states are almost equally populated. At 400 MHz and room temperature only about 30 extra nuclei per million sit in the lower state. NMR is therefore an insensitive technique: it needs milligram amounts, strong magnets, and many averaged scans. If the populations become equal (by too much radiofrequency power), there is no net absorption — this is **saturation**.

## 2.3 Relaxation processes

After excitation, nuclei must return to the lower state for absorption to continue. NMR transitions cannot relax by spontaneous emission (far too slow at radio frequencies); they relax by interacting with fluctuating local magnetic fields.

| Process | Also called | What returns | Time constant | Effect |
| --- | --- | --- | --- | --- |
| **Spin–lattice relaxation** | Longitudinal relaxation | Population difference along the field (z) returns to equilibrium; energy goes to the surroundings ("lattice") | **T1** | Decides how long to wait between pulses; slow T1 (e.g. quaternary carbons) gives weak signals unless the delay is long |
| **Spin–spin relaxation** | Transverse relaxation | Loss of phase coherence among spins in the xy plane; no energy lost to the lattice | **T2** (≤ T1) | Decides line width: line width ≈ 1/(πT2). Short T2 → broad lines |

Relaxation is driven by molecular tumbling (dipole–dipole interaction), paramagnetic species (dissolved oxygen, metal ions shorten T1 and broaden lines), quadrupolar nuclei and chemical exchange. In solids and viscous samples T2 is short and lines are broad, which is why solution NMR needs non-viscous solutions and solid-state NMR needs magic-angle spinning.

**Heisenberg uncertainty link**: a short lifetime in a state means an uncertain energy, so fast relaxation means a broad line.

## 2.4 Instrumentation

```text
                   ┌──────────── Magnet (B0) ─────────────┐
                   │   shim coils (field homogeneity)      │
 RF transmitter →  │   probe: RF coil around spinning       │ → receiver → ADC → computer
 (pulse)           │   5 mm sample tube; lock channel (²H)  │   (FID)       (Fourier
                   └──────────────────────────────────────┘                transform)
                   sweep/field-frequency lock, temperature control
```

1. **Magnet**: permanent magnets and electromagnets (old 60–100 MHz CW instruments); modern instruments use **superconducting solenoids** (niobium–titanium wire cooled by liquid helium, surrounded by liquid nitrogen) giving 7–23 T. Benchtop instruments with permanent magnets (about 60–90 MHz) are used for reaction monitoring and teaching.
2. **Shim coils**: small electromagnets that make the field very uniform over the sample (homogeneity of about 1 part in 10⁹); poor shimming gives broad, distorted peaks.
3. **Field-frequency lock**: the instrument continuously monitors the deuterium resonance of the solvent and corrects any drift in the field. This is one reason deuterated solvents are needed.
4. **Probe**: holds the sample tube inside the RF coil, which both transmits pulses and receives the signal. Cryoprobes (cooled electronics) raise sensitivity several-fold.
5. **Sample spinning** (about 20 Hz) averages field inhomogeneity across the tube (may give small spinning sidebands).
6. **RF transmitter**: in CW instruments a fixed frequency with a slowly swept field (or vice versa); in FT instruments short, intense pulses.
7. **Receiver, ADC, computer**: detect the signal, digitise it and Fourier-transform it.

**Sample**: about 2–20 mg of a small molecule in 0.5–0.7 mL of deuterated solvent in a 5 mm precision glass tube, filtered free of particles and paramagnetic impurities, with a reference standard.

## 2.5 Solvent requirements

An ideal NMR solvent:
- contains no protons (or is deuterated) so it does not swamp the spectrum;
- provides the ²H signal for the lock;
- dissolves the sample well and is non-viscous;
- is chemically inert, non-polar enough not to shift peaks badly, and free of paramagnetic impurities;
- has residual peaks that do not overlap analyte signals.

| Solvent | Residual ¹H signal (ppm, approx.) | Use |
| --- | --- | --- |
| CDCl3 | 7.26 | Most organic compounds |
| DMSO-d6 | 2.50 (water peak about 3.3) | Polar drugs, amides, salts; shows OH/NH clearly |
| D2O | about 4.8 (HOD) | Salts, sugars, amino acids; exchanges OH/NH/COOH protons |
| CD3OD | 3.31 | Polar compounds; exchanges labile protons |
| Acetone-d6 | 2.05 | Medium polarity |
| C6D6 | 7.16 | Aromatic solvent-induced shifts to separate overlapping peaks |
| CCl4 | none (no protons) | Older non-deuterated choice |

**Reference standard**: **tetramethylsilane (TMS)**, (CH3)4Si, set to 0 ppm. Reasons: 12 equivalent protons give one sharp, strong singlet; silicon is less electronegative than carbon, so the protons are strongly shielded and appear upfield of almost all organic signals; it is inert, volatile (easily removed) and soluble in organic solvents. In D2O the water-soluble **DSS** (sodium 2,2-dimethyl-2-silapentane-5-sulphonate) or TSP is used instead.

## 2.6 Chemical shift

Electrons around a nucleus circulate in the applied field and create a small opposing field. The nucleus feels a slightly smaller **effective field**: B_eff = B0(1 − σ), where σ is the **shielding constant**. Differently shielded nuclei therefore resonate at slightly different frequencies — this is what makes NMR chemically useful.

```text
 δ (ppm) = [ν(sample) − ν(TMS)] / ν(spectrometer, MHz)
 Example: a signal 300 Hz from TMS on a 400 MHz instrument → δ = 300/400 = 0.75 ppm
 CDCl3 residual peak at 7.26 ppm on 400 MHz → 7.26 × 400 = 2904 Hz from TMS
```

Expressing shifts in ppm makes them **independent of the field strength**; the same compound gives the same δ on 60 and 600 MHz instruments, while the separation in Hz grows with the field.

**Terms**
- **Shielded / upfield**: more electron density, lower δ, right of the spectrum (TMS side).
- **Deshielded / downfield**: less electron density, higher δ, left side.
- Old τ scale: τ = 10 − δ.

**Typical ¹H chemical shifts**

| Proton type | δ (ppm, approx.) |
| --- | --- |
| TMS | 0 |
| Alkyl C–H (CH3 < CH2 < CH) | 0.9–1.7 |
| Allylic, C–H next to C=O, benzylic | 2.0–2.7 |
| Alkyne C≡C–H | 2–3 |
| C–H next to N, Cl, Br | 2.5–4 |
| C–H next to O (ethers, alcohols, esters O–CH) | 3.3–4.5 |
| Alkene =C–H | 4.5–6.5 |
| Aromatic Ar–H | 6.5–8.5 |
| Aldehyde CHO | 9–10 |
| Carboxylic acid COOH | 10–13 |
| Alcohol OH, amine NH | 0.5–5, variable (H-bonding, concentration, temperature) |
| Phenol OH | 4–8 |
| Amide NH | 5–9 |

## 2.7 Factors influencing chemical shift

1. **Inductive effect (electronegativity)**: electronegative atoms pull electron density away and deshield nearby protons. CH3F (4.26) > CH3Cl (3.05) > CH3Br (2.68) > CH3I (2.16) > CH4 (0.23). The effect falls off quickly with distance and is additive (CHCl3 at 7.26 is more downfield than CH2Cl2 at 5.3).
2. **Magnetic anisotropy**: π electrons circulate in a direction-dependent way and create local fields that shield some regions and deshield others.
   - **Aromatic ring current**: protons on the ring's edge lie in the deshielding zone → 7–8 ppm. Protons held over the face of a ring (in cyclophanes, or [18]annulene inner protons) are shielded, even below 0 ppm.
   - **C=C and C=O**: protons in the plane are deshielded (alkene H about 5 ppm, aldehyde H about 9.5 ppm, where induction adds to anisotropy).
   - **C≡C**: the cylindrical electron cloud shields the acetylenic proton along the axis, so it appears at only 2–3 ppm despite sp hybridisation.
3. **Hybridisation**: s-character influences shift (sp2 C–H deshielded relative to sp3), combined with anisotropy.
4. **Hydrogen bonding**: removes electron density from the proton → strong deshielding; intermolecular H-bond signals move with concentration and temperature; intramolecular ones (salicylaldehyde OH about 11 ppm) do not.
5. **Van der Waals deshielding**: crowded protons in rigid molecules shift downfield.
6. **Solvent effects**: aromatic solvents (C6D6) shift signals by specific complexation (ASIS); pH changes shifts of ionisable groups.
7. **Exchange**: labile OH, NH, SH protons exchange with each other and with D2O; with fast exchange they appear as a single averaged, often broad peak, and they disappear on shaking with D2O (**D2O exchange test**).
8. **Paramagnetic shift reagents**: lanthanide complexes (europium, praseodymium) coordinate to lone pairs and spread overlapping signals; chiral shift reagents separate enantiomer signals for optical purity.

## 2.8 NMR signals in various compounds

Information read from a ¹H spectrum:

| Feature | Tells you |
| --- | --- |
| Number of signals | Number of sets of chemically equivalent protons |
| Position (δ) | Electronic environment |
| Integration (area) | Relative number of protons in each set |
| Splitting (multiplicity) | Number of neighbouring non-equivalent protons |
| Coupling constant (J) | Geometry and connectivity |

**Equivalence**: protons are **chemically equivalent** if they are interchanged by symmetry or fast rotation (the three protons of a CH3). They are **magnetically equivalent** if, in addition, each couples equally to every other nucleus (not true for the AA′BB′ protons of a para-disubstituted benzene, which gives a characteristic "two doublets with extra lines" pattern). Homotopic, enantiotopic and diastereotopic protons: diastereotopic CH2 protons next to a stereocentre are non-equivalent and can give separate signals.

Examples:
- **Ethanol (CH3CH2OH)** in CDCl3: triplet (3H, about 1.2), quartet (2H, about 3.7), broad singlet OH (1H, variable). OH does not split the CH2 because of fast exchange; in very pure, dry DMSO-d6 exchange slows and the OH becomes a triplet.
- **Ethyl acetate**: CH3 singlet (about 2.0, next to C=O), O–CH2 quartet (about 4.1), CH3 triplet (about 1.25) — integration 3:2:3.
- **Toluene**: aromatic multiplet (5H, about 7.2) and CH3 singlet (3H, about 2.35).
- **Paracetamol in DMSO-d6**: CH3 singlet near 2.0, two aromatic doublets (AA′BB′ type) between about 6.7 and 7.4, phenolic OH near 9.1 and amide NH near 9.6 (both exchangeable with D2O).

## 2.9 Spin–spin coupling

A proton's small magnetic moment is felt by neighbouring protons through the **bonding electrons**. Each neighbour can be aligned with or against the field, so the observed proton sees slightly different local fields and its signal splits. Coupling is transmitted through bonds, mainly over two (geminal) or three (vicinal) bonds, and is **not** affected by the external field strength.

**The n + 1 rule** (for first-order spectra, I = 1/2 neighbours): a proton with n equivalent neighbouring protons gives n + 1 lines, with intensities from **Pascal's triangle**.

```text
 n neighbours   pattern     intensities
 0              singlet     1
 1              doublet     1 1
 2              triplet     1 2 1
 3              quartet     1 3 3 1
 4              quintet     1 4 6 4 1
 6              septet      1 6 15 20 15 6 1   (isopropyl CH)
 General for spin I: 2nI + 1 lines (e.g. CDCl3 carbon shows a 1:1:1 triplet from one deuterium)
```

If a proton has two different sets of neighbours with different J values, the pattern is (n + 1)(m + 1) lines — e.g. a doublet of doublets.

**First-order vs second-order spectra**: the simple rules hold when the shift difference Δν (in Hz) is much larger than J (Δν/J > about 10; labelled AX systems). When Δν is comparable to J (AB, ABX systems), peaks lean towards each other ("roofing"), intensities change and extra lines appear. Higher-field magnets increase Δν in Hz but not J, so spectra become more first-order — one main reason for buying high-field instruments.

Equivalent protons do not split each other (the CH3 of ethane is one singlet).

## 2.10 Coupling constant (J)

**J** is the spacing between the lines of a multiplet, in Hz. Coupled protons share the same J — this is how partners are matched.

| Type | Typical J (Hz) |
| --- | --- |
| Geminal ²J (sp3 CH2, diastereotopic) | 10–15 |
| Vicinal ³J free-rotating alkyl | about 7 |
| Alkene cis | 6–12 |
| Alkene trans | 12–18 |
| Alkene geminal | 0–3 |
| Aromatic ortho | 6–9 |
| Aromatic meta | 1–3 |
| Aromatic para | 0–1 |
| Cyclohexane axial–axial | 8–13 |
| Cyclohexane axial–equatorial, equatorial–equatorial | 2–5 |

**Karplus relationship**: the vicinal coupling constant depends on the dihedral angle φ between the two C–H bonds — large near 0° and 180°, smallest near 90°. It is used to assign conformation of sugars, steroids and cyclic drugs, and to tell cis from trans alkenes (e.g. geometric isomers of cinnamic acid derivatives).

Long-range couplings (⁴J, ⁵J) occur through rigid or π systems (W-coupling, allylic coupling) and are small (0–3 Hz).

## 2.11 Nuclear magnetic double resonance

In double resonance a second radiofrequency field is applied at the resonance frequency of one nucleus while the spectrum of another is observed.

1. **Spin decoupling (homonuclear)**: irradiating one proton signal strongly makes that proton flip so fast that its neighbours see only an average; their multiplets collapse. Collapsing a quartet to a singlet by irradiating a triplet proves the two groups are adjacent. It identifies coupling partners in complex spectra.
2. **Heteronuclear decoupling**: in ¹³C NMR all protons are irradiated (broadband decoupling) so each carbon gives a single line.
3. **Nuclear Overhauser effect (NOE)**: saturating one nucleus changes the intensity of nuclei **close in space** (within about 5 Å), even if not bonded. In ¹³C with proton decoupling, NOE increases carbon signal intensity (up to about threefold). In ¹H work, NOE difference experiments and 2D NOESY give spatial proximity — used for stereochemistry, conformation and for proving drug–cyclodextrin inclusion (ROESY cross-peaks between drug protons and the cavity H-3/H-5 protons).
4. **INDOR** and selective decoupling are older variants.

## 2.12 Principles of FT-NMR

**Continuous-wave (CW) NMR** sweeps the field or frequency slowly through the spectrum, recording one frequency at a time; a scan takes minutes, so averaging is slow.

**Pulsed Fourier-transform NMR**:

```text
 Net magnetisation M0 along z (field direction)
   → short, intense RF pulse (µs) excites ALL frequencies at once
   → M tipped into xy plane (90° pulse)
   → M precesses and decays (T2) → coil picks up a decaying signal = FID
     (free induction decay, a time-domain mixture of all frequencies)
   → digitise → Fourier transform → frequency-domain spectrum
   → wait (relaxation delay, about 5 × T1 for quantitative work) → repeat, co-add
```

Advantages:
- All nuclei excited simultaneously (multiplex), so one scan takes a few seconds.
- **Signal averaging**: signal-to-noise improves as √(number of scans); 100 scans give 10 times better S/N. This made ¹³C and dilute-sample NMR routine.
- Pulse sequences make possible DEPT, NOE experiments, relaxation measurements and **two-dimensional NMR**: COSY (H–H coupling), HSQC/HMQC (one-bond C–H), HMBC (two- and three-bond C–H), NOESY/ROESY (through-space), DOSY (diffusion; separates components by size, used for micelles and polymers).

## 2.13 ¹³C NMR

**Challenges**: natural abundance only 1.1%, and γ is about one quarter of ¹H, so sensitivity is about 1/5700 of ¹H — FT and many scans are essential. ¹³C–¹³C coupling is negligible because two ¹³C atoms are rarely adjacent.

**Features**
- Chemical shift range about 0–220 ppm (vs about 0–12 for ¹H), so signals rarely overlap; each unique carbon usually gives its own line.
- **Broadband proton-decoupled spectra**: one singlet per unique carbon; signals are enhanced by NOE.
- Intensities are not proportional to the number of carbons (unequal NOE and long T1, especially for quaternary carbons). For quantitative ¹³C, use **inverse-gated decoupling** and long delays.
- **Off-resonance decoupling** (older) and **DEPT** (distortionless enhancement by polarisation transfer) show multiplicity: DEPT-135 shows CH and CH3 up, CH2 down, quaternary C absent; DEPT-90 shows only CH.

| Carbon type | δ (ppm, approx.) |
| --- | --- |
| Alkyl CH3, CH2, CH | 10–50 |
| C–N | 30–65 |
| C–O (alcohols, ethers, esters) | 50–90 |
| Alkyne | 65–90 |
| Alkene, aromatic | 100–160 |
| Nitrile C≡N | 115–125 |
| Carbonyl of acids, esters, amides | 160–185 |
| Aldehyde, ketone C=O | 190–220 |

## 2.14 Applications of NMR

1. **Structure elucidation** of new drugs, synthetic intermediates, natural products and metabolites (with MS and IR).
2. **Identification of impurities and degradation products** in stability studies, often after isolation or by LC–NMR.
3. **Quantitative NMR (qNMR)**: signal area is directly proportional to the number of nuclei, independent of compound, so purity can be assayed against an internal standard (maleic acid, dimethyl sulphone) without a reference standard of the drug itself. Used to certify reference materials.
4. **Stereochemistry**: cis/trans by J; relative configuration by NOE; enantiomeric excess with chiral shift reagents or chiral solvating agents.
5. **Tautomerism, conformation and kinetics** (variable-temperature NMR, coalescence of exchanging signals).
6. **Formulation science**: drug–cyclodextrin inclusion (shift changes of cavity protons H-3 and H-5, ROESY), drug–polymer and drug–excipient interactions, micelle and liposome characterisation, PEG content and degree of substitution of polymers (e.g. ratio of lactide to glycolide in PLGA from ¹H integrals), counter-ion stoichiometry of salts.
7. **Solid-state NMR** (magic-angle spinning, cross-polarisation): polymorphs, amorphous content, drug state inside solid dispersions.
8. **Other nuclei**: ¹⁹F for fluorinated drugs (no background), ³¹P for phosphates, phospholipids and nucleotides.
9. **Metabolomics and biofluids**; **MRI** in diagnosis is based on the same principle (water proton relaxation).

## Remember

- I = 0 when both mass and atomic numbers are even; 2I + 1 orientations; ¹H, ¹³C, ¹⁹F, ³¹P have I = 1/2.
- ν0 = γB0/2π; 9.4 T ≈ 400 MHz for ¹H, about 100 MHz for ¹³C; tiny Boltzmann excess makes NMR insensitive.
- T1 spin–lattice (energy to surroundings, sets delay); T2 spin–spin (dephasing, sets line width).
- δ = (Δν in Hz)/(spectrometer MHz), field-independent; TMS = 0; CDCl3 residual 7.26.
- Shift factors: induction, anisotropy (ring current, C=O, C≡C shielding), H-bonding, exchange, solvent.
- n + 1 rule, Pascal's triangle; J in Hz, field-independent; trans 12–18, cis 6–12, ortho 6–9 Hz; Karplus curve.
- Double resonance = decoupling + NOE; FT-NMR = pulse → FID → Fourier transform, S/N ∝ √scans.
- ¹³C: 1.1% abundance, 0–220 ppm, broadband decoupled singlets, DEPT for CH/CH2/CH3.
