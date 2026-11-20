# Unit 1: NMR spectroscopy and mass spectrometry

UV and IR spectra (studied in BP701T) tell you that a molecule has a chromophore or a carbonyl group. They rarely tell you how the atoms are joined. Nuclear magnetic resonance (NMR) maps the hydrogen and carbon skeleton atom by atom, and mass spectrometry (MS) weighs the molecule and its pieces. Together they are the two main tools for proving the structure of a new drug, an impurity or a metabolite. This unit covers the theory, the instruments and the uses of both.

## 1.1 Principle of NMR

Some atomic nuclei spin. A spinning charge behaves like a tiny bar magnet with a **nuclear spin quantum number (I)**.

| Nucleus | I | Natural abundance | NMR active? |
| --- | --- | --- | --- |
| ¹H | 1/2 | about 99.98% | Yes, most sensitive |
| ¹³C | 1/2 | about 1.1% | Yes, weak signal |
| ¹⁹F, ³¹P | 1/2 | 100% | Yes |
| ²H (deuterium) | 1 | about 0.015% | Yes, used for the lock |
| ¹²C, ¹⁶O | 0 | major isotopes | No (no spin) |

Rule: a nucleus with an even number of protons **and** an even number of neutrons has I = 0 and gives no NMR signal. That is why ¹²C and ¹⁶O are "invisible" and organic spectra show only ¹H or ¹³C.

**In a magnetic field.** A nucleus with I = 1/2 can take 2I + 1 = 2 orientations in an external field B0:

```text
 Energy
   ^                     β (spin -1/2, against the field)  ---------
   |                                                          ^
   |        no field: one level         ΔE = hν = γhB0/2π     |  absorb radio waves
   |        ------------------                                |
   |                     α (spin +1/2, with the field)    ---------
   +------------------------------------------------------------> field B0
 The gap ΔE grows in direct proportion to B0.
```

The nucleus also **precesses** around the field direction, like a spinning top, at the **Larmor frequency**:

**ν = γB0 / 2π**

where γ is the magnetogyric (gyromagnetic) ratio, a constant for each nucleus. When radio-frequency radiation of exactly this frequency is applied, nuclei flip from α to β: this is **resonance**. A 7.05 T magnet gives about 300 MHz for ¹H and about 75 MHz for ¹³C; a 9.4 T magnet gives about 400 MHz for ¹H and 100 MHz for ¹³C. Spectrometers are named by their ¹H frequency ("a 400 MHz NMR").

**Why NMR is insensitive.** The energy gap is tiny, so the two levels are almost equally filled (Boltzmann distribution). At 300 MHz and 25 °C, the ratio of upper to lower population is about 0.99995: for every million nuclei in the upper level there are only about 1,000,048 in the lower level. Only this small excess gives a signal, which is why NMR needs milligram amounts and stronger magnets give better spectra.

## 1.2 Relaxation

After absorbing energy, nuclei must return to the lower level, or the small excess disappears and the signal fades (**saturation**). Two relaxation processes do this:

| Process | Also called | What happens | Symbol |
| --- | --- | --- | --- |
| Spin–lattice relaxation | Longitudinal relaxation | Excited nuclei hand energy to the surroundings (the "lattice": solvent and other molecules) | T1 |
| Spin–spin relaxation | Transverse relaxation | Nuclei exchange spin energy with neighbouring nuclei; the precessing spins lose phase coherence | T2 |

- Liquids: T1 and T2 are about 0.1 to several seconds, so lines are sharp.
- Solids and viscous samples: T2 is very short, so lines are very broad. This is why routine NMR is done in solution.
- Line width ≈ 1/(πT2): fast relaxation gives broad lines (uncertainty principle).
- Paramagnetic impurities (O2, metal ions) shorten relaxation and broaden lines.
- ¹³C nuclei without attached H (quaternary carbons) relax slowly, so their peaks are small.

## 1.3 Chemical shift

If every proton resonated at exactly γB0/2π, all would give one line and NMR would be useless. In a molecule, the electrons circulating around a nucleus create a small field that opposes B0. The nucleus feels a slightly smaller field:

**B(effective) = B0 (1 − σ)**, where σ is the shielding constant.

- **Shielded** proton: more electron density, resonates at higher field (lower frequency), to the **right** of the spectrum (upfield).
- **Deshielded** proton: less electron density, resonates at lower field, to the **left** (downfield).

Because the frequency difference depends on the magnet, the position is expressed in a field-independent unit, the **chemical shift δ** in parts per million:

**δ (ppm) = [ν(sample) − ν(TMS)] / ν(spectrometer) × 10⁶**

**Reference: tetramethylsilane (TMS), Si(CH3)4,** is set at δ 0 because:

1. All 12 protons are equivalent and give one sharp singlet.
2. Silicon is less electronegative than carbon, so its protons are more shielded than almost all organic protons; the TMS peak sits at the right edge, clear of others.
3. It is chemically inert, non-polar, soluble in most organic solvents and volatile (bp about 27 °C), so it is easy to remove.
4. In water (D2O), the water-soluble salt DSS (sodium 2,2-dimethyl-2-silapentane-5-sulfonate) is used instead.

**Worked example.** On a 300 MHz instrument a signal appears 2190 Hz downfield from TMS.
δ = 2190/300 = **7.30 ppm** (a benzene-ring proton). On a 400 MHz instrument the same proton appears 7.30 × 400 = 2920 Hz from TMS, but δ is still 7.30 ppm. That is the point of using ppm.

**Typical ¹H chemical shifts**

| Proton type | δ (ppm) |
| --- | --- |
| TMS | 0 |
| Alkyl C–H (CH3, CH2) | 0.9–1.5 |
| CH3 next to C=O (CH3–CO) | 2.0–2.6 |
| CH3 on a benzene ring | about 2.3 |
| Alkyne ≡C–H | 2–3 |
| H–C–O (alcohol, ether, ester O–CH) | 3.3–4.5 |
| Alkene =C–H | 4.5–6.5 |
| Aromatic Ar–H | 6.5–8.5 |
| Aldehyde CHO | 9–10 |
| Carboxylic acid COOH | 10–13 |
| Alcohol OH, amine NH | variable, about 1–5 (depends on concentration and H-bonding) |

## 1.4 Factors affecting chemical shift

1. **Electronegativity (inductive effect).** An electronegative atom pulls electron density away and deshields nearby protons. Methyl halides show this neatly: CH3F about 4.3, CH3Cl about 3.1, CH3Br about 2.7, CH3I about 2.2 and CH4 about 0.2 ppm. The effect weakens quickly with distance and adds up (CH2Cl2 and CHCl3 move further downfield).
2. **Magnetic anisotropy (π-electron circulation).** π electrons circulate in the field and set up their own field that shields some regions and deshields others.
   - Benzene ring current deshields the ring protons (δ about 7.3).
   - The C=O group deshields an aldehyde proton (δ 9–10).
   - Alkene protons are deshielded (δ 4.5–6.5).
   - The cylinder of π electrons in an alkyne shields the acetylenic proton along the axis (δ only 2–3, upfield of alkenes).
3. **Hybridisation.** sp² carbons hold electrons closer, so attached protons are deshielded compared with sp³ C–H.
4. **Hydrogen bonding.** H-bonded protons (OH, NH, COOH) are deshielded; their shift moves with concentration, temperature and solvent. Intramolecular H-bonds (for example in salicylic acid) give a large downfield shift that does not change on dilution.
5. **Van der Waals deshielding.** Crowded protons squeezed by nearby groups move slightly downfield.
6. **Solvent effects.** Aromatic solvents such as benzene-d6 shift signals by their own anisotropy.
7. **Exchange.** OH and NH protons exchange with D2O; adding a drop of D2O makes their signal disappear (the D2O exchange test).

## 1.5 Spin–spin coupling and coupling constant

Neighbouring non-equivalent protons influence each other's local field through the bonding electrons. Each proton "sees" the spin states of the protons on the next carbon, so its signal splits. This is **spin–spin coupling**.

**The n + 1 rule (first-order spectra).** A proton with n equivalent neighbouring protons is split into n + 1 lines. The relative intensities follow Pascal's triangle.

```text
 Neighbours (n)   Lines   Name        Intensities
      0             1     singlet     1
      1             2     doublet     1 : 1
      2             3     triplet     1 : 2 : 1
      3             4     quartet     1 : 3 : 3 : 1
      4             5     quintet     1 : 4 : 6 : 4 : 1
      6             7     septet      1 : 6 : 15 : 20 : 15 : 6 : 1
```

**Example: ethanol, CH3–CH2–OH (in pure dry sample, ignoring OH coupling).**
- CH3 (δ about 1.2): neighbours are the 2 CH2 protons → triplet, integrating 3H.
- CH2 (δ about 3.7): neighbours are 3 CH3 protons → quartet, integrating 2H.
- OH: a broad singlet, position variable (fast exchange removes its coupling).

**Example: ethyl acetate, CH3COOCH2CH3.** Acetyl CH3 singlet near 2.0 (3H), O–CH2 quartet near 4.1 (2H), CH3 triplet near 1.3 (3H).

**Coupling constant (J)** is the distance between two adjacent lines of a multiplet, in hertz.

- J does **not** change with the magnet strength (δ in Hz does), so a 300 MHz and a 600 MHz spectrum give the same J.
- Protons that couple to each other share the same J. Matching J values tells you which groups are neighbours.
- Worked example: a triplet on a 300 MHz spectrum has lines at δ 1.262, 1.238 and 1.214. Spacing = 0.024 ppm × 300 = **7.2 Hz**, a typical free-rotating CH2–CH3 coupling.

| Coupling type | Typical J (Hz) |
| --- | --- |
| Vicinal H–C–C–H, free rotation | about 6–8 |
| Alkene, trans | about 12–18 |
| Alkene, cis | about 6–12 |
| Geminal on an sp² carbon (=CH2) | 0–3 |
| Aromatic ortho | 6–9 |
| Aromatic meta | 1–3 |
| Aromatic para | 0–1 |

**Rules.**
- Equivalent protons do not split each other (the CH3 of ethane is one singlet).
- Coupling normally reaches over three bonds (H–C–C–H); weaker long-range coupling can appear in alkenes and aromatics.
- When the shift difference between two groups (Δν in Hz) is not much larger than J, the spectrum becomes **second order**: line intensities lean towards each other ("roof effect") and the simple n + 1 rule fails. Higher-field magnets increase Δν and simplify such spectra.

**Integration.** The area under each signal is proportional to the number of protons giving it. The instrument draws a step curve; the ratio of step heights gives the proton ratio (3 : 2 : 1 for ethanol).

## 1.6 ¹³C NMR

**Differences from ¹H NMR**

| Feature | ¹H NMR | ¹³C NMR |
| --- | --- | --- |
| Natural abundance | about 99.98% | about 1.1% |
| Relative sensitivity | 1 | very low (roughly 1/5700 of ¹H at natural abundance) |
| Shift range | about 0–12 ppm | about 0–220 ppm |
| Frequency at 9.4 T | 400 MHz | about 100 MHz |
| C–C coupling | — | not seen (two ¹³C atoms are rarely next to each other) |
| Integration | reliable | not reliable (slow relaxation, NOE) |
| Sample and time | a few mg, minutes | more sample, many scans (FT essential) |

**Proton-decoupled spectra.** ¹³C couples strongly to attached protons. In routine spectra the protons are irradiated with a broad band of radio frequency (**broadband or noise decoupling**), which removes all C–H splitting. Each chemically different carbon then gives **one singlet**. Decoupling also increases peak heights through the **nuclear Overhauser effect (NOE)**.

**Off-resonance decoupling** (older) and **DEPT** (distortionless enhancement by polarisation transfer) show how many H atoms each carbon carries:

| Experiment | CH3 | CH2 | CH | Quaternary C |
| --- | --- | --- | --- | --- |
| Off-resonance (n + 1 rule on directly bonded H) | quartet | triplet | doublet | singlet |
| DEPT-90 | absent | absent | positive | absent |
| DEPT-135 | positive | negative (inverted) | positive | absent |

**Typical ¹³C shifts**

| Carbon type | δ (ppm) |
| --- | --- |
| Alkyl CH3, CH2, CH | 10–50 |
| C–N | 30–65 |
| C–O (alcohol, ether) | 50–90 |
| Alkyne C≡C | 65–90 |
| Alkene and aromatic | 100–160 |
| Nitrile C≡N | 110–125 |
| Ester, acid, amide C=O | 160–185 |
| Aldehyde, ketone C=O | 190–220 |

Common solvent: CDCl3, whose residual CHCl3 shows at δ 7.26 in ¹H spectra and whose carbon gives a small triplet near δ 77 in ¹³C spectra (C–D coupling, deuterium I = 1 gives 2nI + 1 = 3 lines).

## 1.7 Instrumentation of NMR

Modern instruments are **pulsed Fourier transform (FT-NMR)** spectrometers. Older **continuous-wave (CW)** instruments swept the field or frequency slowly and took several minutes per spectrum.

```text
                 +------------------- Computer (pulse control, FT, display) ----------+
                 |                                                                    |
        RF transmitter (pulse) ----> probe coil around sample <---- RF receiver ----> ADC
                                         |   (sample tube, spun)       (FID)
                 Superconducting magnet: [ N ]  sample in probe  [ S ]
                 Shim coils (field homogeneity)   Lock channel (2H of solvent)
```

| Part | Function |
| --- | --- |
| **Magnet** | Strong, stable, uniform field. Permanent or electromagnets (60–100 MHz, old); **superconducting** solenoid (300–1000 MHz) kept at about 4 K in liquid helium, with a liquid nitrogen jacket to slow helium loss |
| **Shim coils** | Small extra coils that correct field unevenness across the sample; good shimming gives sharp lines |
| **Field–frequency lock** | Monitors the deuterium signal of the solvent and corrects any drift of the field |
| **Sample probe** | Holds the 5 mm glass tube in the centre of the field; contains the transmitter/receiver coil; air turbine spins the tube (about 20 Hz) to average field differences |
| **RF transmitter** | Gives short, intense pulses (microseconds) that excite all nuclei of one kind at once |
| **RF receiver and detector** | Picks up the decaying signal emitted by the nuclei, the **free induction decay (FID)** |
| **Computer** | Adds many scans to improve signal-to-noise (S/N rises with the square root of the number of scans), performs the **Fourier transform** (time domain → frequency domain spectrum), integrates and prints |

**Sample preparation.** About 5–20 mg (more for ¹³C) dissolved in about 0.5–0.7 ml of a deuterated solvent (CDCl3, DMSO-d6, D2O, CD3OD) with a little TMS. Deuterated solvents avoid a huge solvent proton peak and provide the lock signal. The solution must be free of solid particles and paramagnetic impurities.

**FT advantage.** One pulse excites the whole spectrum; a spectrum is collected every few seconds; hundreds of scans can be averaged. This made ¹³C NMR routine.

## 1.8 Applications of NMR

1. **Structure elucidation** of new drugs, natural products, metabolites and degradation products: number of proton types (number of signals), their environment (δ), ratio (integration) and neighbours (splitting, J).
2. **Identification and identity tests:** comparison with a reference spectrum.
3. **Distinguishing isomers:** cis/trans alkenes (J), ortho/meta/para substitution patterns, keto–enol tautomers.
4. **Quantitative NMR (qNMR):** signal area is proportional to the number of nuclei, so purity or content can be found against an internal standard of known purity without a reference standard of the analyte.
5. **Impurity profiling** and checking residual solvents.
6. **Hydrogen bonding and exchange studies** (D2O shake, temperature effects).
7. **Two-dimensional NMR** (COSY, HSQC, HMBC) to connect protons and carbons in complex molecules.
8. **Medical imaging:** magnetic resonance imaging (MRI) uses the same principle on water protons in tissue.
9. **Drug–protein binding and conformation** studies.

## 1.9 Principle of mass spectrometry

A mass spectrometer **turns molecules into gaseous ions, separates the ions by their mass-to-charge ratio (m/z) and counts them**. It does not use radiation; strictly it is not "spectroscopy", but the plot of ion abundance against m/z is called the mass spectrum.

```text
 Sample inlet ──> Ion source ──> Mass analyser ──> Detector ──> Data system
  (probe, GC,     (EI, CI, ESI,   (quadrupole,      (electron
   LC, plate)      FAB, MALDI)     TOF, magnetic)    multiplier)
                 └────────────── all under high vacuum ──────────────┘
```

**Terms used on a mass spectrum**

| Term | Meaning |
| --- | --- |
| m/z | Mass of the ion divided by its charge; for singly charged ions, m/z = mass |
| Molecular ion (M⁺•) | The molecule minus one electron: a radical cation whose m/z gives the molecular mass |
| Base peak | The tallest peak, set to 100% relative abundance; all others are scaled to it |
| Fragment ions | Smaller ions formed when M⁺• breaks |
| Isotope peaks | M + 1, M + 2 peaks from heavier isotopes (¹³C, ³⁷Cl, ⁸¹Br, ³⁴S) |
| Metastable ions | Ions that break up on the way through the analyser; broad, weak peaks at non-integer m/z |
| Quasi-molecular ion | [M + H]⁺ or [M − H]⁻ formed by soft ionisation |

**High vacuum** (about 10⁻⁵ to 10⁻⁷ torr in the analyser) is needed so that ions do not collide with air molecules before reaching the detector.

## 1.10 Ionisation techniques

| Technique | How ions form | Type | Suits | Main ion |
| --- | --- | --- | --- | --- |
| **Electron impact (EI)** | Vapour hit by a beam of 70 eV electrons from a heated filament | Hard | Volatile, thermally stable, small molecules (GC-MS) | M⁺• plus many fragments |
| **Chemical ionisation (CI)** | Reagent gas (methane, isobutane, ammonia) ionised by electrons; reagent ions (CH5⁺) transfer a proton to the sample | Soft | Molecules whose M⁺• is weak in EI | [M + H]⁺, little fragmentation |
| **Fast atom bombardment (FAB)** | Sample in a liquid matrix (glycerol, m-nitrobenzyl alcohol) hit by fast neutral atoms (Ar or Xe) | Soft | Polar, non-volatile, larger molecules (peptides, antibiotics, salts) | [M + H]⁺, [M + Na]⁺; matrix peaks |
| **MALDI** (matrix-assisted laser desorption/ionisation) | Sample mixed with a UV-absorbing matrix (sinapinic acid, α-cyano-4-hydroxycinnamic acid), dried on a plate and fired with a pulsed UV laser | Very soft | Proteins, peptides, polymers, oligonucleotides up to very high mass | Mostly singly charged [M + H]⁺; usually with TOF |
| Electrospray (ESI) and APCI | Covered under LC-MS in Unit 5 | Soft | LC-MS | [M + H]⁺, multiply charged ions |

**Electron impact in more detail.** Electrons from a hot tungsten or rhenium filament are accelerated through 70 V towards an anode (trap). Vapour molecules crossing the beam lose an electron: M + e⁻ → M⁺• + 2e⁻. About 10–15 eV is enough to ionise; the extra energy breaks bonds, giving a reproducible "fingerprint" of fragments. Repeller and accelerating plates push the ions into the analyser. Spectra at 70 eV are standard, so library searching is possible.

**Chemical ionisation.** Reagent gas at about 1 torr is ionised: CH4 → CH4⁺• → (with more CH4) CH5⁺ + CH3•. Then CH5⁺ + M → [M + H]⁺ + CH4. The [M + H]⁺ ion carries little excess energy, so it survives. Use CI to confirm the molecular mass when EI gives no M⁺•.

**MALDI.** The matrix absorbs the laser energy and vaporises, carrying the analyte with it and passing protons to it. Because ions are produced in pulses, MALDI pairs naturally with a time-of-flight analyser (MALDI-TOF).

## 1.11 Fragmentation

The molecular ion has extra energy and breaks at its weakest bonds and to give the most stable ions. Common patterns:

1. **α-cleavage:** bond next to a heteroatom or carbonyl breaks, giving a resonance-stabilised cation. Ketones lose an alkyl radical to give an acylium ion (R–C≡O⁺).
2. **Benzylic cleavage:** alkylbenzenes give m/z 91, the very stable **tropylium ion** C7H7⁺ (toluene, M 92, base peak 91).
3. **McLafferty rearrangement:** carbonyl compounds with a γ-hydrogen transfer that hydrogen to the carbonyl oxygen through a six-membered transition state and split off a neutral alkene.
4. **Loss of small neutral molecules:** H2O (18) from alcohols, CO (28) from aldehydes and phenols, CO2 (44) from acids, NH3 (17), HCN (27), ketene CH2=C=O (42) from acetanilides.
5. **Retro-Diels–Alder** cleavage of cyclohexene rings.
6. Stevenson's rule: when a bond breaks, the positive charge stays on the fragment with the lower ionisation energy.

**Worked example: acetophenone, C6H5COCH3 (M = 120).**
- M⁺• at m/z 120.
- α-cleavage loses CH3• (15): C6H5CO⁺ at **m/z 105** (base peak, benzoyl cation).
- Loss of CO (28) from m/z 105 gives C6H5⁺ at **m/z 77** (phenyl cation).

**Isotope patterns and useful rules**

| Rule | What it tells you |
| --- | --- |
| Nitrogen rule | A molecule with an odd molecular mass contains an odd number of N atoms; even mass means zero or an even number of N |
| M + 1 peak | About 1.1% of M for each carbon (from ¹³C); C8 compound: about 8.8% |
| Chlorine | One Cl gives M and M + 2 in about 3 : 1 ratio (³⁵Cl : ³⁷Cl); chlorobenzene shows m/z 112 and 114 |
| Bromine | One Br gives M and M + 2 in about 1 : 1 ratio (⁷⁹Br : ⁸¹Br) |
| Sulfur | M + 2 about 4.4% per S (³⁴S) |
| Degree of unsaturation | (2C + 2 + N − H − X)/2 rings plus double bonds, from the formula |

**High-resolution MS** measures m/z to four decimal places. Because exact atomic masses are not whole numbers (¹H 1.0078, ¹⁶O 15.9949, ¹⁴N 14.0031), the exact mass fixes the molecular formula. Example: paracetamol C8H9NO2 has nominal mass 151 and monoisotopic mass 151.0633; its protonated ion [M + H]⁺ is m/z 152.0706.

**Resolution (R) = m/Δm**, where Δm is the smallest mass difference that can be separated at mass m. Separating m/z 500.0 from 500.5 needs R = 500/0.5 = 1000.

## 1.12 Mass analysers

### Quadrupole

```text
        rod A (+)          Ions enter along the axis
   ion  ===========  ──>  only ions of one chosen m/z have a stable path
  beam  ===========        and reach the detector; others spiral out
        rod B (−)          and hit the rods
   Four parallel rods: opposite pairs joined; DC voltage + RF voltage applied
```

- Four parallel metal rods; one opposite pair carries +(U + V cos ωt), the other −(U + V cos ωt), where U is a DC voltage and V cos ωt a radio-frequency voltage.
- For a given U and V, only ions of one m/z oscillate stably and pass through; all others collide with the rods. The quadrupole is a **mass filter**.
- Scanning U and V together (keeping U/V constant) brings each m/z through in turn.
- Advantages: small, cheap, fast scanning, tolerant of higher pressure, easy to couple with GC and LC; ideal for selected ion monitoring.
- Limitations: unit resolution only; mass range up to a few thousand.
- A **triple quadrupole** (Q1–q2–Q3) is used for MS/MS (Unit 5).

### Time of flight (TOF)

All ions are given the same kinetic energy by an accelerating voltage V and then drift through a field-free tube of length L:

zeV = ½mv², so the flight time **t = L √(m / 2zeV)**. Heavier ions are slower.

```text
 pulsed ion source ──> accelerating grid (V) ──> field-free drift tube (L) ──> detector
                         light ions arrive first ............ heavy ions arrive last
 Reflectron: an ion mirror at the end that corrects small energy spreads and improves resolution
```

- Worked example: L = 1.0 m, V = 20 kV, singly charged ions. m/z 1000 arrives in about 16.1 µs; m/z 500 in about 11.4 µs; m/z 1001 only about 0.008 µs after m/z 1000. Fast electronics are therefore essential.
- Advantages: practically unlimited mass range (proteins), very fast, whole spectrum from every pulse, high sensitivity; best partner for MALDI.
- Limitation: needs pulsed ionisation; resolution depends on energy spread (improved by the reflectron and delayed extraction).

| Feature | Quadrupole | Time of flight |
| --- | --- | --- |
| Separation by | Stability of path in DC + RF field | Flight time in drift tube |
| Mode | Scanning filter | All ions per pulse |
| Mass range | Up to about a few thousand | Very large |
| Resolution | Unit | High (with reflectron) |
| Common partners | EI, CI, ESI; GC-MS, LC-MS/MS | MALDI, ESI (Q-TOF) |

Other analysers met in books: magnetic sector (ions bent in a magnetic field, radius depends on m/z; double-focusing with an electrostatic sector gives high resolution), ion trap, and Orbitrap.

## 1.13 Instrumentation of a mass spectrometer

| Component | Details |
| --- | --- |
| **Sample inlet** | Batch inlet for gases and volatile liquids; direct insertion probe for solids; GC or LC interface; MALDI plate |
| **Ion source** | EI, CI, FAB, MALDI, ESI or APCI (above) |
| **Mass analyser** | Quadrupole, TOF, magnetic sector, ion trap |
| **Detector** | **Electron multiplier** (ion strikes a dynode, releases electrons, which cascade down a series of dynodes, giving about 10⁶ gain); Faraday cup (collects charge directly, very accurate but less sensitive); microchannel plate (TOF) |
| **Vacuum system** | Rotary pump (rough vacuum) plus turbomolecular or diffusion pump (high vacuum) |
| **Data system** | Records m/z and intensity, normalises to base peak, compares with libraries |

## 1.14 Applications of mass spectrometry

1. **Molecular mass** from M⁺• or [M + H]⁺; **molecular formula** from exact mass (HRMS) and isotope pattern.
2. **Structure elucidation** from fragmentation, with NMR and IR.
3. **Identification of impurities and degradation products** at trace levels.
4. **Drug metabolism and pharmacokinetics:** metabolites and plasma drug levels (LC-MS/MS).
5. **Proteins and peptides:** molecular mass of biologics, peptide mapping and sequencing (MALDI-TOF, ESI).
6. **Isotope ratio and labelling studies** (¹³C, ²H, ¹⁵N tracers).
7. **Forensic and doping analysis,** drugs of abuse, pesticide residues (GC-MS).
8. **Microbial identification** by MALDI-TOF protein fingerprints.

## Remember

- ν = γB0/2π; δ = (ν sample − ν TMS)/ν spectrometer × 10⁶; TMS = δ 0.
- Deshielding (electronegative atoms, ring current, H-bonding) moves signals downfield (left).
- n + 1 rule with Pascal's triangle; J in Hz does not change with field strength.
- T1 spin–lattice, T2 spin–spin; short T2 means broad lines.
- ¹³C: 1.1% abundance, 0–220 ppm, broadband decoupled singlets; DEPT-135: CH2 down, CH and CH3 up, quaternary absent.
- MS: ions separated by m/z under high vacuum; base peak = 100%.
- EI is hard (70 eV); CI, FAB and MALDI are soft and give [M + H]⁺.
- Quadrupole = DC + RF mass filter; TOF: t = L√(m/2zeV), light ions arrive first.
- Nitrogen rule; Cl 3 : 1 and Br 1 : 1 M/M + 2; tropylium m/z 91; acetophenone 120 → 105 → 77.
