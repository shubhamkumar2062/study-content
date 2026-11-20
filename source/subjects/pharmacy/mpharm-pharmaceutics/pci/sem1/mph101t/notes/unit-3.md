# Unit 3: Mass spectrometry

Mass spectrometry (MS) weighs molecules. It converts a sample into gas-phase ions, separates the ions by their **mass-to-charge ratio (m/z)** and counts them. From one spectrum you can get the molecular mass, often the molecular formula (from exact mass and isotope peaks), and structural pieces from the fragments. Because it needs only nanograms or less, MS coupled with chromatography (GC–MS, LC–MS/MS) is the standard tool for bioanalysis, metabolite and impurity identification, genotoxic impurity control and biologics characterisation. The PCI syllabus asks for the principle, theory, instrumentation, ionisation methods (EI, CI, FI, FAB, MALDI, APCI, ESI, APPI), quadrupole and time-of-flight analysers, fragmentation rules, metastable ions, isotope peaks and applications.

## 3.1 Principle and theory

Strictly, MS is not "spectroscopy" because no radiation is absorbed; the name mass spectrometry is preferred. The steps are:

```text
 Sample inlet → Ion source → Mass analyser → Detector → Data system
 (gas, liquid,   (make ions,    (separate by     (count ions)  (mass spectrum:
  solid, LC/GC)   fragment)       m/z, vacuum)                   relative abundance vs m/z)
```

**Theory for a magnetic sector (classical derivation)**: an ion of mass m and charge z accelerated through potential V gains kinetic energy:

```text
 zeV = ½ m v²
 In a magnetic field B the ion follows a circular path of radius r:  B z e v = m v² / r
 Eliminating v:   m/z = B² r² e / 2V
```

For a fixed radius (fixed detector slit), ions of different m/z reach the detector one after another as B (magnetic scan) or V (electric scan) is changed. Lighter ions are deflected more.

**Key terms**
- **Mass spectrum**: bar graph of relative abundance (%) against m/z.
- **Base peak**: the tallest peak, set to 100%; it is the most stable ion, not necessarily the molecular ion.
- **Molecular ion (M⁺•)**: the radical cation formed by losing one electron from the intact molecule; its m/z gives the molecular mass (for z = 1).
- **Fragment ions**: smaller ions from breaking bonds in M⁺•.
- **Nominal mass** uses integer masses (C 12, H 1, N 14, O 16); **monoisotopic exact mass** uses exact isotope masses (¹H 1.00783, ¹⁶O 15.9949, ¹⁴N 14.0031, ¹²C 12.0000).
- **Resolution**: R = m/Δm, where Δm is the smallest separable mass difference at mass m. Low-resolution instruments separate unit masses; high-resolution instruments (R above 10,000) give exact mass to a few ppm, enough to distinguish CO (27.9949), N2 (28.0061) and C2H4 (28.0313), all nominal mass 28.

**Vacuum**: the analyser is kept at high vacuum (about 10⁻⁵ to 10⁻⁷ torr or better) so that ions travel without colliding with gas molecules (long mean free path), and to protect the filament and detector.

## 3.2 Instrumentation

1. **Inlet system**
   - Batch (reservoir) inlet for gases and volatile liquids.
   - **Direct insertion probe** for solids and non-volatile samples, heated into the source.
   - **Chromatographic inlet**: GC capillary column directly into the source; LC through an atmospheric-pressure interface (ESI, APCI, APPI).
2. **Ion source** (Section 3.3).
3. **Mass analyser**: magnetic sector, double focusing (electric + magnetic), quadrupole, ion trap, time-of-flight, Orbitrap, Fourier-transform ion cyclotron resonance (FT-ICR).
4. **Detector**
   - **Electron multiplier** (discrete dynode or continuous channeltron): an ion strikes a surface, releases electrons, which cascade to give gains of about 10⁶.
   - **Faraday cup**: measures ion current directly; accurate but insensitive (isotope ratio work).
   - **Photomultiplier with phosphor (scintillation)**: ions converted to electrons, then light.
   - Microchannel plates in TOF instruments.
5. **Vacuum system**: rotary (roughing) pumps with turbomolecular or diffusion pumps.
6. **Data system**: mass calibration with reference compounds (perfluorotributylamine, PFTBA, for EI), library search, extracted-ion chromatograms.

## 3.3 Ionisation methods

Ionisation methods are described as **hard** (much energy, much fragmentation, molecular ion may be absent) or **soft** (little excess energy, strong molecular or quasi-molecular ion, little fragmentation).

### Electron impact (EI) — hard

```text
 Heated filament (W or Re) → electrons accelerated to 70 eV → cross the vapour
 M + e⁻ → M⁺• + 2e⁻ ;   M⁺• (excess energy) → fragments
 Repeller pushes ions out → accelerating and focusing plates → analyser
```

- Sample must be volatile and thermally stable (vaporised first).
- 70 eV is standard because ionisation efficiency is high and roughly constant there, so spectra are **reproducible across instruments** and can be searched against libraries (NIST, Wiley).
- Gives rich fragmentation (structure information); molecular ion weak or absent for alcohols, branched alkanes and fragile molecules.
- Used in GC–MS.

### Chemical ionisation (CI) — soft

- A reagent gas (methane, isobutane, ammonia) at about 1 torr is ionised by electrons; the reagent ions (CH5⁺, C2H5⁺, t-C4H9⁺, NH4⁺) then transfer a proton to the analyte.
- CH4 + e⁻ → CH4⁺•; CH4⁺• + CH4 → CH5⁺ + CH3•; CH5⁺ + M → [M+H]⁺ + CH4.
- Gives a strong **quasi-molecular ion [M+H]⁺** (also adducts [M+C2H5]⁺, [M+NH4]⁺), little fragmentation — confirms molecular mass when EI shows none.
- Negative CI (electron capture) is very sensitive for halogenated and nitro compounds.

### Field ionisation (FI) and field desorption (FD) — soft

- A very high electric field (about 10⁷–10⁸ V/cm) at fine tips or whiskers on an emitter pulls an electron from the molecule by quantum tunnelling.
- FI: sample in vapour; FD: sample coated on the emitter and desorbed — for non-volatile, thermally labile molecules.
- Gives almost only M⁺•; very little fragmentation.

### Fast atom bombardment (FAB) — soft, desorption

- Sample dissolved in a non-volatile liquid **matrix** (glycerol, 3-nitrobenzyl alcohol) on a probe tip, bombarded with a beam of fast neutral atoms (argon or xenon, several keV). Liquid SIMS uses caesium ions instead.
- Produces [M+H]⁺, [M−H]⁻ and cationised [M+Na]⁺ from polar, non-volatile and thermally labile compounds: peptides, glycosides, antibiotics, salts.
- Matrix gives background peaks; largely replaced by ESI and MALDI.

### Matrix-assisted laser desorption/ionisation (MALDI) — soft

```text
 Analyte mixed with a large excess of UV-absorbing matrix (sinapinic acid,
 α-cyano-4-hydroxycinnamic acid, 2,5-dihydroxybenzoic acid) → dried crystals on a plate
 → pulsed UV laser (N2 laser, 337 nm) → matrix absorbs, vaporises explosively,
 carries analyte into the gas phase and protonates it → mainly singly charged [M+H]⁺
 → naturally paired with a TOF analyser (pulsed source)
```

- Very high mass range (proteins, polymers, oligonucleotides above 100 kDa).
- Tolerant of salts and buffers; fast; used for peptide mass fingerprinting, microbial identification, polymer molecular weight distribution, imaging MS of tissues.

### Atmospheric-pressure ionisation (API) — the LC–MS sources

**Electrospray ionisation (ESI)**

```text
 LC eluent → metal capillary at 3–5 kV → Taylor cone → charged droplets
 → nebulising and drying gas (N2) evaporates solvent → droplets shrink until
   Rayleigh limit → Coulomb explosion → smaller droplets → gas-phase ions
   (ion evaporation / charged residue models) → sampling cone → vacuum
```

- Softest common technique; gives [M+H]⁺, [M+Na]⁺, [M−H]⁻.
- **Multiply charged ions** [M+nH]ⁿ⁺ for proteins and peptides: a 50 kDa protein can appear at m/z 1000–2000, so even a quadrupole can measure it; the charge-state envelope is deconvoluted to the mass.
- Best for polar, ionisable compounds (most drugs, metabolites, peptides, oligonucleotides).
- Suffers from **ion suppression** by co-eluting matrix (phospholipids, salts) in bioanalysis — controlled by sample clean-up, chromatography and stable-isotope internal standards.
- Volatile buffers only (ammonium formate or acetate, formic acid); phosphate buffers foul the source.

**Atmospheric pressure chemical ionisation (APCI)**

- The eluent is vaporised in a heated tube (about 350–500 °C); a **corona discharge needle** ionises solvent vapour, which then ionises the analyte by gas-phase proton transfer (as in CI).
- Suited to less polar, thermally stable small molecules (steroids, some lipids) at higher LC flow rates; mostly singly charged ions; less matrix suppression than ESI.

**Atmospheric pressure photoionisation (APPI)**

- A krypton discharge lamp emits photons (about 10 eV) that ionise analytes directly (M + hν → M⁺• + e⁻) or via a **dopant** (toluene, acetone) that is ionised first and then transfers charge or a proton.
- Extends LC–MS to non-polar compounds: polyaromatic hydrocarbons, steroids, fat-soluble vitamins, some excipients.

**Choosing a source**

| Analyte | Best source |
| --- | --- |
| Volatile, small, thermally stable (GC) | EI (library), CI (molecular mass) |
| Polar drugs, metabolites, peptides, proteins | ESI |
| Moderately polar to non-polar small molecules | APCI |
| Non-polar, aromatic | APPI |
| Large biomolecules, polymers, tissue imaging | MALDI |
| Non-volatile, labile (older) | FAB, FD |

## 3.4 Mass analysers

### Quadrupole

```text
        (+)  rod   rod (−)
             ion beam →  →  →   detector
        (−)  rod   rod (+)
 Four parallel rods; opposite rods connected.
 Applied voltage = DC (U) + RF (V cos ωt).
 For a given U and V only ions of one m/z have a stable path through the rods;
 others oscillate with growing amplitude and hit the rods.
 Scanning U and V together (constant U/V ratio) brings successive m/z values to the detector.
```

- A **mass filter**, not a dispersive analyser; unit resolution; mass range typically up to about 2000–4000.
- Compact, cheap, fast scanning, tolerant of relatively poor vacuum — ideal for GC–MS and LC–MS.
- **Selected ion monitoring (SIM)**: the filter jumps to a few chosen m/z values, improving sensitivity.
- **Triple quadrupole (QqQ)**: Q1 selects a precursor ion, q2 is an RF-only **collision cell** (argon or nitrogen; collision-induced dissociation, CID), Q3 selects a product ion. **Multiple reaction monitoring (MRM)** — precursor → product transitions — gives exceptional selectivity and sensitivity; it is the standard for quantitative bioanalysis (pharmacokinetic and bioequivalence studies) and trace genotoxic impurities.
- Ion trap (3D or linear) is a related device that stores ions and ejects them by m/z; allows MSⁿ.

### Time-of-flight (TOF)

```text
 Pulse of ions all given the same kinetic energy zeV → field-free drift tube (about 1–2 m)
 ½ m v² = zeV  →  v = √(2zeV/m)  →  flight time t = L √(m / 2zeV)   so  t ∝ √(m/z)
 Light ions arrive first.  Reflectron (ion mirror) corrects the spread in initial
 kinetic energy: faster ions penetrate deeper into the mirror and travel further,
 so ions of the same m/z arrive together → higher resolution.
```

- Needs a pulsed source (MALDI) or orthogonal acceleration of a continuous beam (ESI-TOF).
- **Unlimited theoretical mass range**, very fast acquisition (whole spectrum per pulse), high sensitivity, and with a reflectron high resolution and accurate mass (a few ppm).
- **Q-TOF** (quadrupole + collision cell + TOF): accurate-mass MS/MS for unknown metabolites and impurities.

**Other high-resolution analysers** (beyond the syllabus list, but useful): double-focusing magnetic sector (electrostatic analyser + magnet), **Orbitrap** (ions orbit a spindle electrode; frequency of axial oscillation gives m/z) and FT-ICR (cyclotron frequency in a strong magnet; highest resolution).

## 3.5 Mass fragmentation and its rules

The molecular ion has excess energy and breaks into a positive fragment (detected) and a neutral radical or molecule (not detected). Fragmentation follows chemistry: bonds break to give the **most stable cations and neutral species**.

**General rules**
1. **Nitrogen rule**: a compound containing C, H, O, S, halogens with an **even** number of nitrogen atoms (including zero) has an **even** nominal molecular mass; an **odd** number of nitrogens gives an **odd** molecular mass. (Aniline C6H7N: M = 93.) In ESI the [M+H]⁺ is one higher, so the rule reverses for the observed ion.
2. **Even-electron rule**: even-electron ions (cations, [M+H]⁺) tend to lose even-electron neutrals (H2O, CO, NH3, C2H4) rather than radicals.
3. **Stevenson's rule**: when a bond cleaves, the positive charge stays on the fragment with the lower ionisation energy.
4. **Stability of the cation**: tertiary > secondary > primary carbocations; allylic, benzylic and resonance-stabilised ions (acylium R–C≡O⁺, oxonium, iminium) give strong peaks. Branched alkanes cleave at the branch point.
5. **Loss of small stable neutrals** gives characteristic mass differences: −15 (CH3), −17 (OH), −18 (H2O), −28 (CO or C2H4), −29 (CHO or C2H5), −31 (OCH3), −43 (CH3CO or C3H7), −44 (CO2), −45 (COOH). A loss of 4–14 or 21–25 from M is unlikely, which helps decide whether a peak is really the molecular ion.
6. **Rings plus double bonds (degree of unsaturation)** for CcHhNnXx: DBE = c − h/2 + n/2 + 1 (halogens count as H). Aspirin C9H8O4: 9 − 4 + 1 = 6 (ring 4, two C=O 2).

**Main fragmentation pathways**

| Pathway | What happens | Example |
| --- | --- | --- |
| Simple (σ) cleavage | A single bond breaks; charge on the more stable fragment | Branched alkanes; loss of the largest alkyl group |
| α-Cleavage | Bond next to a heteroatom or carbonyl breaks; charge stabilised on the heteroatom | Ketones → acylium ions (acetophenone m/z 105 → 77); amines → iminium ions (m/z 30 for primary amines); alcohols → oxonium ions (m/z 31 for primary alcohols) |
| Benzylic cleavage | Gives benzyl cation, rearranging to the stable **tropylium ion** C7H7⁺ | m/z 91 in toluene and alkylbenzenes |
| **McLafferty rearrangement** | Carbonyl (or similar) with a γ-hydrogen: six-membered transition state transfers γ-H to O, β-bond breaks, alkene lost | Butanal → m/z 44; methyl esters → m/z 74; gives even-mass ions from even-mass M |
| Retro-Diels–Alder | Cyclohexene ring splits into a diene ion and an alkene | Terpenes, steroids, flavonoids |
| Loss of water / small neutrals | Dehydration of alcohols (M − 18), decarboxylation (M − 44) | Alcohols, acids |
| Inductive cleavage | Charge moves to the alkyl group as the heteroatom leaves | Halides, ethers |

**Characteristic ions**: m/z 77 (C6H5⁺), 91 (C7H7⁺), 105 (C6H5CO⁺), 43 (CH3CO⁺ or C3H7⁺), 29, 30 (CH2=NH2⁺), 31 (CH2=OH⁺), 149 (phthalate contamination).

## 3.6 Metastable ions

Some ions are formed in the source with just enough energy to fragment **after acceleration but before reaching the analyser** (in a field-free region of a sector instrument). The daughter ion then has less kinetic energy than a normal ion of the same mass and appears as a **broad, weak, often non-integral peak** at:

```text
 m* = (m2)² / m1          m1 = parent ion, m2 = daughter ion
 Example: m/z 105 → m/z 77 (loss of CO from benzoyl ion):
 m* = 77² / 105 = 56.5
```

Significance: a metastable peak **proves a direct one-step relationship** between a parent and a daughter ion, helping to map fragmentation pathways. In modern instruments the same information is obtained deliberately by MS/MS (precursor and product-ion scans).

## 3.7 Isotope peaks

Most elements have heavier natural isotopes, so every ion is accompanied by smaller peaks at m+1, m+2 and so on.

| Element | Isotopes (approximate natural abundance) | Peak pattern |
| --- | --- | --- |
| Carbon | ¹²C 98.9%, ¹³C 1.1% | M+1 ≈ 1.1% × number of C atoms |
| Hydrogen | ²H 0.015% | negligible |
| Nitrogen | ¹⁵N 0.37% | adds about 0.37% per N to M+1 |
| Oxygen | ¹⁸O 0.2% | small M+2 |
| Sulphur | ³⁴S 4.2% (³³S 0.8%) | M+2 about 4.4% per S |
| Chlorine | ³⁵Cl 75.8%, ³⁷Cl 24.2% | M : M+2 ≈ 3 : 1 for one Cl |
| Bromine | ⁷⁹Br 50.7%, ⁸¹Br 49.3% | M : M+2 ≈ 1 : 1 for one Br |

**Uses**
1. **Counting carbons**: number of C ≈ (M+1 intensity / M intensity) × 100 / 1.1. A compound with ten carbons shows an M+1 of about 11% of M.
2. **Recognising halogens**: two Cl atoms give M : M+2 : M+4 of about 9 : 6 : 1 (100 : 64 : 10 with exact abundances); two Br atoms give about 1 : 2 : 1; one Cl + one Br gives about 3 : 4 : 1.
3. **Sulphur** shows a larger M+2 than expected from C, H, O alone.
4. **Molecular formula** from accurate mass plus the isotope pattern ("isotopic fidelity").
5. **Stable isotope labels** (²H, ¹³C, ¹⁵N) are used as internal standards and in metabolism studies; the label shifts the mass by a known amount.

## 3.8 Tandem mass spectrometry (MS/MS) — brief

| Scan | Q1 | Q3 | Use |
| --- | --- | --- | --- |
| Product-ion scan | Fixed precursor | Scanned | Fragmentation pattern of one ion (structure) |
| Precursor-ion scan | Scanned | Fixed product | Find all compounds giving a common fragment (e.g. a drug class) |
| Neutral-loss scan | Scanned | Scanned with fixed offset | Find conjugates (loss of 176 for glucuronides, 80 for sulphates) |
| MRM | Fixed | Fixed | Quantitation |

## 3.9 Applications of mass spectrometry

1. **Molecular mass and formula** of new drugs, intermediates and natural products (high-resolution exact mass).
2. **Structure elucidation** from fragmentation, together with NMR and IR.
3. **Bioanalysis**: LC–MS/MS quantification of drugs and metabolites in plasma for pharmacokinetic, bioavailability and bioequivalence studies; therapeutic drug monitoring.
4. **Impurity profiling and degradation products**: identifying unknown peaks from forced-degradation studies; trace **genotoxic/nitrosamine impurities** at ppb levels by GC–MS or LC–MS/MS.
5. **Metabolite identification** (accurate mass, neutral-loss and precursor scans, mass defect filtering).
6. **Biologics**: intact mass of monoclonal antibodies (ESI, deconvolution), peptide mapping, glycosylation, disulphide bridges; MALDI for proteins.
7. **Residual solvents and volatile impurities** by headspace GC–MS; leachables and extractables from packaging.
8. **Isotope ratio and labelled studies**; doping control; forensic toxicology; herbal fingerprinting.
9. **Formulation science**: polymer molecular weight distribution (MALDI-TOF of PEG, PLGA), drug content in nanoparticles, excipient identification, mass spectrometry imaging of drug distribution in skin or tissue.

## Remember

- MS separates ions by m/z under high vacuum; m/z = B²r²e/2V for a magnetic sector; resolution R = m/Δm.
- Base peak = tallest (100%); molecular ion M⁺• = molecular mass; nitrogen rule (odd N → odd M).
- EI 70 eV hard, reproducible, library; CI gives [M+H]⁺; FAB uses glycerol matrix and fast atoms; MALDI = matrix + laser, pairs with TOF; ESI multiply charged, polar; APCI corona discharge, less polar; APPI photons with dopant, non-polar.
- Quadrupole = DC + RF mass filter, QqQ/MRM for quantitation; TOF t ∝ √(m/z), reflectron improves resolution.
- Fragmentation: α-cleavage, McLafferty (γ-H, m/z 44 or 74), tropylium 91, acylium 105 → 77.
- Metastable m* = m2²/m1 (105 → 77 gives 56.5) proves a one-step pathway.
- Isotopes: M+1 ≈ 1.1% per C; Cl 3:1; Br 1:1; Cl2 9:6:1; Br2 1:2:1.
