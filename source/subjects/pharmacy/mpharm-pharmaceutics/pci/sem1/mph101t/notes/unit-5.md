# Unit 5: Electrophoresis and X-ray crystallography

This unit joins two very different methods. **Electrophoresis** separates charged molecules by how fast they move in an electric field — the main tool for proteins, peptides, nucleic acids and charge variants of biotherapeutics. **X-ray crystallography/diffraction** uses the scattering of X-rays by the regular arrangement of atoms in a crystal — the main tool for crystal structure, polymorph identification and crystallinity, which matter greatly in pre-formulation and formulation work (solubility, stability, solid dispersions).

## Part A — Electrophoresis

## 5.1 Principle and theory

A charged particle in an electric field E feels a force qE and moves towards the electrode of opposite charge. The medium resists the motion with a frictional force f v (for a sphere, f = 6πηr by Stokes' law). At steady state:

```text
 q E = 6 π η r v           →     v = q E / (6 π η r)
 Electrophoretic mobility  µ = v / E = q / (6 π η r)   (units cm² V⁻¹ s⁻¹)
 Example: a band moves 4.0 cm in 2.0 h in a field of 10 V/cm
   v = 4.0 / 7200 = 5.6 × 10⁻⁴ cm/s;  µ = v/E = 5.6 × 10⁻⁵ cm² V⁻¹ s⁻¹
```

So mobility increases with **charge** and decreases with **size** (radius) and **viscosity**. Proteins and amino acids are amphoteric: their net charge depends on pH relative to their **isoelectric point (pI)**. Below pI they are positive and move to the cathode; above pI negative, moving to the anode; at pI they do not move.

**Electro-osmosis (electro-osmotic flow, EOF)**: a charged support surface (paper, agar, the silica wall of a capillary) attracts counter-ions; the field drags this layer of mobile ions and with it the bulk liquid. In fused-silica capillaries above about pH 3, the wall is negative and EOF moves the whole liquid towards the cathode. EOF is a nuisance in gel and paper electrophoresis but an essential pumping mechanism in capillary electrophoresis.

## 5.2 General instrumentation and working conditions

```text
 DC power supply (constant voltage, current or power)
    ├── + Anode ──── buffer tank ┐
    │                            ├── support medium (paper/gel/capillary) with sample
    └── − Cathode ── buffer tank ┘
 Cooling plate or circulating coolant  →  then staining / detection / densitometry
```

**Working conditions**
- **Buffer**: sets pH (charge) and ionic strength. Common: Tris–glycine, Tris–borate–EDTA (TBE), Tris–acetate–EDTA (TAE), barbitone (veronal) buffer pH 8.6 for serum proteins, phosphate.
- **Ionic strength**: low ionic strength gives faster migration but broader bands and lower buffering; high ionic strength gives sharp bands but more current and heat. A moderate value (about 0.05–0.1) is usual.
- **Voltage and current**: higher voltage speeds the run but produces **Joule heating** (heat ∝ I²R). Heating causes evaporation, convection, band distortion ("smiling"), denaturation. Control by cooling, lower current, thinner gels, or capillaries (efficient heat loss).
- **Support medium**: paper, cellulose acetate, starch, agarose, polyacrylamide, or free solution in a capillary.
- **Detection**: staining (Coomassie Brilliant Blue, silver stain, Ponceau S for proteins; ethidium bromide or safer dyes such as SYBR for DNA; ninhydrin for amino acids), UV absorbance, fluorescence, autoradiography, densitometry for quantitation.

## 5.3 Factors affecting electrophoretic separation

| Factor | Effect |
| --- | --- |
| Charge of the molecule | More charge → faster |
| Size and shape | Larger or more elongated → slower; sieving media add a size effect |
| pH of the buffer | Controls net charge of amphoteric molecules |
| Ionic strength | High → slower, sharper bands, more heat; low → faster, diffuse bands |
| Voltage / field strength | Higher → faster, more heat |
| Temperature | Higher → lower viscosity, faster but more diffusion and possible denaturation |
| Viscosity of medium | Higher → slower |
| Pore size of gel | Smaller pores retard large molecules more (molecular sieving) |
| Electro-osmosis | Adds a bulk flow towards one electrode |
| Adsorption to the support | Causes tailing (paper, uncoated capillary walls) |
| Time of run | Longer → better separation but more diffusion |

## 5.4 Types of electrophoresis

### (a) Paper electrophoresis

- Strip of filter paper soaked in buffer, ends dipping into buffer tanks; sample applied as a narrow line; low-voltage (100–500 V) or high-voltage (up to several kV, with cooling) runs.
- After the run the paper is dried and stained (ninhydrin for amino acids; bromophenol blue for proteins).
- Simple and cheap; limitations: adsorption, electro-osmosis, poor resolution.
- Uses: amino acids, peptides, serum proteins (historical), nucleotides. Cellulose acetate film replaced paper for clinical serum protein patterns (albumin, α1, α2, β and γ-globulins).

### (b) Gel electrophoresis

**Agarose gel**: a polysaccharide from seaweed forming large pores; 0.5–2% gels; horizontal submerged ("submarine") format. Separates DNA and RNA fragments (100 bp to several kb) by size — DNA is uniformly negative (phosphate backbone), so it all runs to the anode and separation is by sieving. Size estimated against a DNA ladder.

**Polyacrylamide gel electrophoresis (PAGE)**: acrylamide polymerised with N,N′-methylene-bisacrylamide (cross-linker), initiated by ammonium persulphate and catalysed by TEMED. Pore size controlled by total acrylamide (%T) and cross-linker (%C); usually vertical slabs.
- **Native PAGE**: proteins keep their structure; separation by charge, size and shape; activity can be detected after the run (zymography).
- **SDS-PAGE**: sodium dodecyl sulphate denatures proteins and binds about 1.4 g per g of protein, giving all proteins a similar negative charge-to-mass ratio; a reducing agent (β-mercaptoethanol or dithiothreitol) breaks disulphide bonds. Separation is then by **molecular weight** alone. A plot of log MW of marker proteins against relative mobility is linear and gives the MW of unknowns.
- **Discontinuous (Laemmli) system**: a large-pore stacking gel (pH 6.8) concentrates proteins into a thin band between leading chloride and trailing glycinate ions, then the resolving gel (pH 8.8) separates them — sharp bands.
- **Gradient gels** (for example 4–20%) resolve a wide MW range.
- **Western blotting**: proteins transferred from the gel to a membrane and detected with antibodies.

**Starch gel**: older medium for isoenzymes.

### (c) Capillary electrophoresis (CE)

```text
 High-voltage supply (up to 30 kV)
 Buffer vial (+) ── fused-silica capillary (25–100 µm id, 30–100 cm) ── Buffer vial (−)
          sample injected by pressure or voltage at one end
          on-capillary window → UV/PDA, fluorescence (LIF) or MS detector
```

- Very high field possible because the narrow capillary loses heat efficiently → fast runs, **very high efficiency** (hundreds of thousands of plates), tiny sample and solvent volumes.
- EOF carries all species (cations, neutrals, anions) towards the cathode past the detector: cations first, then neutrals (with EOF), then anions.
- Modes:
  - **Capillary zone electrophoresis (CZE)**: free solution, separation by charge-to-size ratio.
  - **Micellar electrokinetic chromatography (MEKC)**: SDS micelles in the buffer act as a pseudo-stationary phase, so **neutral** molecules separate by partition into micelles.
  - **Capillary gel electrophoresis (CGE)**: sieving polymer inside the capillary; CE-SDS for antibody purity and fragments; DNA sequencing.
  - **Capillary isoelectric focusing (cIEF)**: charge variants of proteins.
  - **Capillary isotachophoresis** and **capillary electrochromatography** (packed capillary).
  - **Chiral CE**: cyclodextrins added to the buffer resolve enantiomers.
- Applications: chiral purity, small ionic drugs and counter-ions, impurity profiling, monoclonal antibody purity (CE-SDS) and charge heterogeneity (cIEF), DNA analysis.

### (d) Zone electrophoresis

- The sample is applied as a narrow **zone** on a stabilising support (paper, cellulose acetate, gel); each component migrates as a separate band (zone) that can be stained and cut out. Paper, gel and CZE are all forms of zone electrophoresis.
- Advantage over moving boundary: complete separation of components, small sample, simple apparatus. Uses: serum proteins, lipoproteins, isoenzymes, haemoglobin variants.

### (e) Moving boundary electrophoresis (Tiselius method)

```text
       ┌───┐           ┌───┐
       │ − │  buffer   │ + │
       └─┬─┘           └─┬─┘
         │   U-tube with protein solution below buffer,
         │   sharp boundaries in each limb
         └──────┬──────┘
 Under the field, each protein's boundary moves; boundaries detected by
 refractive index changes (schlieren optics) → peaks = components
```

- Free solution, no support medium; the protein solution forms sharp boundaries with buffer in a U-shaped cell (Tiselius apparatus, which earned a Nobel Prize).
- Only the fastest component is obtained pure (at the leading edge); components are not completely separated.
- Used historically to measure mobilities and pI of proteins and to show the major serum protein fractions. Requires large samples and careful temperature control (about 4 °C, where water's density is highest, to minimise convection).

### (f) Isoelectric focusing (IEF)

- Separation by **isoelectric point**. A stable **pH gradient** is formed in the gel by carrier ampholytes (mixtures of small polyamino–polycarboxylic acids) or by immobilised pH gradient (IPG) strips (buffering groups bonded into the gel).
- Anode in acid, cathode in alkali. A protein moves until it reaches the pH equal to its pI, where its net charge is zero and it stops — it is **focused** into a very sharp band (diffusion away gives it charge and it moves back).
- Resolves proteins differing in pI by about 0.01–0.02 pH units.
- **Two-dimensional electrophoresis**: IEF in the first dimension (pI) then SDS-PAGE in the second (MW) — resolves thousands of proteins (proteomics).
- Applications: charge variants of monoclonal antibodies and insulin analogues, identity of protein drugs, isoenzymes, pI determination.

## 5.5 Applications of electrophoresis in pharmacy

1. Purity and identity of protein and peptide drugs (SDS-PAGE, IEF, CE-SDS) — pharmacopoeial tests for biologics such as insulin, interferons and vaccines.
2. Molecular weight determination of proteins (SDS-PAGE).
3. Charge heterogeneity of monoclonal antibodies (cIEF), glycoform analysis.
4. DNA and RNA analysis: plasmid DNA for gene therapy, PCR products, mRNA integrity in lipid nanoparticle vaccines.
5. Clinical diagnosis: serum protein patterns, haemoglobin variants, isoenzymes.
6. Chiral and small-molecule analysis by CE; counter-ion assay.
7. Protein–drug and protein–excipient interaction; stability of protein formulations (aggregation and fragmentation bands).

## Part B — X-ray crystallography

## 5.6 Production of X-rays

X-rays are electromagnetic radiation of wavelength about 0.01–10 nm (0.1–100 Å), comparable to interatomic distances — which is why crystals diffract them.

```text
 Coolidge (X-ray) tube, under vacuum:
 Heated tungsten filament (cathode) → electrons accelerated by 30–50 kV
   → strike a metal target (anode: Cu, Mo, Co, Cr) cooled by water
   → about 1% of energy becomes X-rays, the rest heat
   → X-rays leave through a beryllium window
```

The emitted spectrum has two parts:
- **Continuous (white) radiation, Bremsstrahlung**: electrons decelerating in the target emit a continuous range with a sharp short-wavelength limit set by the accelerating voltage (λmin in nm ≈ 1.24/kV).
- **Characteristic lines**: an incoming electron ejects an inner (K-shell) electron; an outer electron falls in and emits a photon of fixed energy. L → K gives **Kα**, M → K gives **Kβ**. For copper, Kα ≈ 1.5406 Å (0.154 nm), the most common wavelength in pharmaceutical powder diffraction; molybdenum Kα ≈ 0.71 Å for single crystals.
- **Filters** remove unwanted Kβ: a nickel foil absorbs Cu Kβ much more than Cu Kα (absorption edge between them). Monochromator crystals give purer radiation.

Other sources: synchrotrons (very intense, tunable); X-ray detectors include film, scintillation and proportional counters, and modern solid-state area detectors.

Safety: X-rays ionise tissue; instruments are shielded and interlocked.

## 5.7 Bragg's law

A crystal is a regular three-dimensional array of atoms forming parallel planes separated by a spacing d. X-rays reflected from successive planes travel different distances. They reinforce (constructive interference, a diffraction peak) only when the extra path equals a whole number of wavelengths.

```text
  incident  \   θ   / reflected
             \     /
  -------------•-------------  plane 1
              /|\   path difference = 2 d sin θ
  -------------•-------------  plane 2 (spacing d)

  Bragg's law:   n λ = 2 d sin θ        (n = order of reflection, θ = glancing angle)
```

**Worked examples** (Cu Kα, λ = 1.5406 Å, n = 1):
- A peak at 2θ = 20.0° → θ = 10.0° → d = 1.5406 / (2 × sin 10°) = 4.44 Å.
- A plane spacing d = 3.50 Å → sin θ = 1.5406/7.00 → θ = 12.7° → peak at 2θ ≈ 25.4°.

Because sin θ cannot exceed 1, only planes with d ≥ λ/2 can diffract. Each crystal form has its own set of d spacings, and therefore its own diffraction pattern — a **fingerprint** of the crystal lattice.

**Miller indices (h k l)** label lattice planes by the reciprocals of their intercepts on the unit-cell axes; for a cubic cell d = a/√(h² + k² + l²).

## 5.8 Types of crystals

**Crystal systems** (seven), defined by unit-cell edge lengths (a, b, c) and angles (α, β, γ):

| System | Edges | Angles | Example |
| --- | --- | --- | --- |
| Cubic | a = b = c | all 90° | NaCl |
| Tetragonal | a = b ≠ c | all 90° | — |
| Orthorhombic | a ≠ b ≠ c | all 90° | Paracetamol form II, sulphur |
| Hexagonal | a = b ≠ c | 90°, 90°, 120° | Graphite, ice |
| Trigonal (rhombohedral) | a = b = c | equal, not 90° | Calcite |
| Monoclinic | a ≠ b ≠ c | two 90°, one not | Paracetamol form I, sucrose |
| Triclinic | a ≠ b ≠ c | none 90° | — |

These combine with lattice centring (primitive, body-centred, face-centred, base-centred) into the **14 Bravais lattices**; with symmetry elements they give 230 space groups (most drugs crystallise in a few, e.g. P2₁/c).

**Crystals by bonding**: ionic (NaCl, hard, high melting), covalent network (diamond, quartz), metallic, and **molecular** crystals held by van der Waals forces and hydrogen bonds — almost all organic drugs.

**Pharmaceutically important solid forms**
- **Polymorphs**: same molecule, different crystal packing; differ in solubility, dissolution rate, melting point, stability and compressibility (ritonavir's late-appearing less soluble form is a famous case; chloramphenicol palmitate form B is better absorbed than form A).
- **Solvates and hydrates** (pseudo-polymorphs): solvent built into the lattice; anhydrous forms usually dissolve faster than hydrates (theophylline, ampicillin).
- **Co-crystals and salts**: drug with a co-former or counter-ion, to improve solubility or stability.
- **Amorphous solids**: no long-range order, so no sharp peaks — a broad "halo"; higher solubility but physically unstable (may crystallise).

## 5.9 X-ray diffraction methods

| Method | Radiation | Sample | Varies | Use |
| --- | --- | --- | --- | --- |
| **Laue method** | Continuous (white) | Stationary single crystal | λ | Orientation and symmetry of crystals |
| **Rotating crystal method** | Monochromatic | Single crystal rotated about an axis | θ | Unit-cell dimensions and full structure |
| **Powder method (Debye–Scherrer, diffractometer)** | Monochromatic | Fine powder of randomly oriented crystallites | θ (all orientations present) | Identification, polymorphs, crystallinity |

### Rotating crystal technique

```text
 Monochromatic X-ray beam → single crystal (about 0.1–0.5 mm) mounted on a
 goniometer head, rotated about one axis → as it turns, different planes meet
 Bragg's condition → diffracted spots recorded on a cylindrical film or area
 detector around the crystal → spots fall on layer lines; spacing of layer lines
 gives the cell edge along the rotation axis; spot positions and intensities give
 the full lattice and, after solving the "phase problem", the electron density map
 → atomic positions, bond lengths and angles, absolute configuration
```

Modern **single-crystal X-ray diffraction (SCXRD)** uses four-circle diffractometers or area detectors (variants: oscillation, Weissenberg, precession methods). It gives the definitive three-dimensional structure, absolute stereochemistry of chiral drugs, hydrogen-bond networks and the packing that explains polymorph behaviour.

### X-ray powder technique (PXRD)

```text
 Debye–Scherrer camera: powder in a thin capillary at the centre of a
 cylindrical film; each set of planes diffracts into a cone (2θ) → arcs on film.
 Powder diffractometer (Bragg–Brentano): flat powder sample; X-ray tube and
 detector move on a goniometer (θ–2θ) → plot of intensity vs 2θ.
```

- Sample: finely powdered (about 10 µm) to give random orientation and smooth intensities; careful packing to avoid **preferred orientation** (needle and plate crystals distort relative intensities).
- Output: peak positions (2θ → d by Bragg's law), intensities, widths.
- **Crystallite size** from peak broadening by the Scherrer equation, τ = Kλ/(β cos θ), where β is the peak width in radians (corrected for instrument broadening) and K about 0.9.
- **Percent crystallinity** from the ratio of crystalline peak area to total (crystalline + amorphous halo) area.
- Quantitative analysis of polymorph mixtures by calibration or Rietveld refinement.
- Variable-temperature and humidity PXRD follow transitions and hydrate formation.

## 5.10 Applications of X-ray diffraction

1. **Crystal structure determination** (SCXRD): bond lengths, angles, conformation, absolute configuration, hydrogen bonding; protein crystallography for structure-based drug design.
2. **Polymorph and solvate identification** (PXRD fingerprint) — required in pre-formulation and in regulatory filings; polymorph control in the API specification.
3. **Detecting polymorphic changes during processing**: milling, granulation, drying, compression, storage.
4. **Amorphous vs crystalline**: confirming amorphous solid dispersions (halo with no peaks), detecting recrystallisation on stability.
5. **Drug–excipient interaction** and co-crystal or salt formation (new peaks not present in either component).
6. **Degree of crystallinity** of polymers (PLGA, PEG) and lipids in nanoparticles; crystallite size.
7. **Identification of excipients and inorganic materials** (talc, titanium dioxide, magnesium stearate forms, calcium phosphates) and counterfeit detection.
8. **Patent protection** of new crystal forms (PXRD patterns are the usual evidence).
9. Small-angle X-ray scattering (SAXS) for liposomes, micelles and liquid crystalline phases (related technique).

## Remember

- Mobility µ = v/E = q/6πηr; faster with more charge, slower with size and viscosity; at pI no movement.
- Electro-osmosis drives liquid towards the cathode in silica capillaries; Joule heating limits voltage.
- SDS-PAGE separates by MW (SDS gives uniform charge; log MW vs mobility linear); native PAGE by charge, size and shape; agarose for DNA.
- CE: high voltage, tiny capillary, very high efficiency; CZE, MEKC (neutrals), CGE, cIEF, chiral CE.
- Zone = discrete bands on a support; moving boundary = Tiselius, free solution, only fastest component pure.
- IEF focuses proteins at their pI in a pH gradient; 2D = IEF then SDS-PAGE.
- X-rays: Coolidge tube, continuous + characteristic (Kα, Kβ) lines; Cu Kα 1.5406 Å; Ni filter removes Kβ.
- Bragg: nλ = 2d sin θ; 2θ 20° → d 4.44 Å with Cu Kα.
- Laue (white, stationary crystal), rotating crystal (single crystal structure), powder method (polymorph fingerprint, crystallinity, Scherrer size).
- Seven crystal systems, 14 Bravais lattices; polymorphs, solvates, co-crystals and amorphous forms differ in solubility and stability.
