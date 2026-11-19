# Unit 2: IR spectroscopy, flame photometry, atomic absorption spectroscopy and nepheloturbidimetry

This unit joins four techniques. **IR spectroscopy** looks at molecular vibrations and is the main identity test for drugs in the pharmacopoeia. **Flame photometry** and **atomic absorption spectroscopy (AAS)** look at free atoms and measure metals. **Nephelometry and turbidimetry** measure light scattered by suspended particles.

## 2.1 IR spectroscopy: introduction

Infrared radiation lies between the visible and microwave regions. Its energy is too small to move electrons but enough to make bonds **vibrate** more strongly.

| Region | Wavelength | Wavenumber | Use |
| --- | --- | --- | --- |
| Near IR | 0.8–2.5 µm | 12,500–4000 cm⁻¹ | Overtones; moisture, raw material checks |
| Mid IR | 2.5–25 µm | 4000–400 cm⁻¹ | Structure and identity (the usual range) |
| Far IR | 25–1000 µm | 400–10 cm⁻¹ | Metal–ligand and lattice vibrations |

IR spectra are plotted as **% transmittance against wavenumber** (cm⁻¹), so absorption bands point downward. Wavenumber ν̄ = 10⁴/λ (λ in µm).

**Condition for IR absorption:** a vibration absorbs IR only if it **changes the dipole moment** of the molecule. Homonuclear molecules (N2, O2, H2) are IR inactive; the symmetric stretch of CO2 is IR inactive.

**Hooke's law** treats a bond as two masses joined by a spring:

**ν̄ = (1/2πc) √(k/µ)**, where k is the force constant and µ = m1m2/(m1 + m2) is the reduced mass.

So stronger bonds (C≡C > C=C > C–C) and lighter atoms (C–H > C–D) absorb at higher wavenumbers.

## 2.2 Fundamental modes of vibration in polyatomic molecules

A molecule of N atoms has 3N degrees of freedom. Three are translational and three rotational (two for a linear molecule), so:

- **Non-linear molecule:** 3N − 6 vibrational modes (H2O: 3 × 3 − 6 = 3).
- **Linear molecule:** 3N − 5 modes (CO2: 3 × 3 − 5 = 4).

The number of bands seen is often fewer (IR-inactive modes, degenerate modes of equal energy, very weak bands, bands outside the range) or more (overtones, combination bands, Fermi resonance).

**Types of vibration**

```text
 STRETCHING (bond length changes)          BENDING (bond angle changes)
   Symmetric:   <-O=C=O->                  In-plane:  scissoring  (H-C-H close and open like scissors)
   Asymmetric:  <-O=C<- ->O (one in,                   rocking     (both H swing the same way in the plane)
                one out)                   Out-of-plane: wagging   (both H move up together)
                                                         twisting  (one H up, one H down)
```

| Vibration | Description | Typical energy |
| --- | --- | --- |
| Symmetric stretching | Both bonds lengthen and shorten together | Lower than asymmetric |
| Asymmetric stretching | One bond lengthens while the other shortens | Higher |
| Scissoring | Two atoms move toward and away from each other in the plane | |
| Rocking | Both atoms swing in the same direction in the plane | |
| Wagging | Both atoms move up and down out of the plane together | |
| Twisting | One atom moves up while the other moves down | |

Stretching needs more energy than bending, so stretching bands appear at higher wavenumbers. The CH2 group shows all six.

**Regions of the mid-IR spectrum**

| Region | Range (cm⁻¹) | Typical groups |
| --- | --- | --- |
| X–H stretching | 4000–2500 | O–H 3600–3200 (broad when hydrogen bonded), N–H 3500–3300, C–H 3100–2850 (aromatic and alkene above 3000, alkane below) |
| Triple bonds | 2500–2000 | C≡N about 2250, C≡C 2260–2100 |
| Double bonds | 2000–1500 | C=O 1800–1650 (ketone about 1715, ester about 1740, amide about 1680), C=C 1680–1600, aromatic ring 1600 and 1500 |
| Fingerprint region | 1500–400 | C–O, C–N, C–C, bending vibrations; unique for every compound |

## 2.3 Factors affecting vibrational frequencies

1. **Bond strength and atomic mass** (Hooke's law).
2. **Electronic effects:** electron-withdrawing groups next to C=O raise its frequency (inductive effect: acid chlorides about 1800 cm⁻¹); conjugation with C=C or an aromatic ring lowers it by about 20–40 cm⁻¹ (resonance weakens the double bond).
3. **Hydrogen bonding:** lowers the O–H or N–H stretching frequency and broadens the band. Intermolecular hydrogen bonding changes with dilution; intramolecular does not.
4. **Coupled vibrations:** two similar groups on the same atom vibrate together, giving symmetric and asymmetric bands (CH2, NH2, anhydride C=O pair).
5. **Fermi resonance:** an overtone of one vibration has nearly the same energy as a fundamental of another; the two mix, giving two bands (aldehyde C–H doublet near 2820 and 2720 cm⁻¹).
6. **Bond angle and ring strain:** smaller rings raise C=O frequency (cyclobutanone about 1780, cyclohexanone about 1715).
7. **Field effect** (through-space interaction of nearby groups) and **physical state** (solid, liquid, solution, solvent).

## 2.4 Sample handling

IR passes through NaCl, KBr and other alkali halides, not through glass or water-containing cells. Samples must be **dry**.

| Sample | Technique |
| --- | --- |
| Solids | **KBr pellet (disc):** about 1–2 mg sample ground with 100–200 mg dry KBr and pressed under high pressure into a clear disc. **Mull:** sample ground with Nujol (liquid paraffin) and spread between plates; Nujol hides C–H bands, so hexachlorobutadiene or Fluorolube is used for that region. **Solid film:** cast from a volatile solvent on a plate. |
| Liquids | **Neat film:** a drop pressed between two NaCl or KBr plates. Sealed liquid cells for volatile liquids. |
| Solutions | In CCl4, CS2 or CHCl3 using matched sample and solvent cells (0.1–1 mm); solvent bands are cancelled by the reference cell. |
| Gases | Gas cell about 10 cm long with salt windows. |
| Modern | **ATR (attenuated total reflectance):** the sample is pressed on a diamond or ZnSe crystal; little or no preparation; used widely with FTIR. |

## 2.5 IR instrumentation

```text
 DISPERSIVE DOUBLE-BEAM IR SPECTROPHOTOMETER

            +--> [Sample beam] ---+
 [Source] --+                     +--> [Chopper/rotating mirror] -> [Monochromator] -> [Detector] -> [Amplifier] -> [Recorder]
            +--> [Reference beam]-+                                 NaCl/KBr prism     thermal or
 Nernst glower / globar                                             or grating         pyroelectric
```

```text
 FTIR (Fourier transform IR)

 [Source] -> [Beam splitter] -- fixed mirror
                   |
                   +--------- moving mirror  (Michelson interferometer)
                   v
              [Sample] -> [Detector: DTGS or MCT] -> [Computer: Fourier transform interferogram -> spectrum]
```

### Sources of radiation (heated solids that glow)

| Source | Material | Temperature / notes |
| --- | --- | --- |
| **Nernst glower** | Rod of rare earth oxides (zirconium, yttrium, thorium) | About 1500–2000 °C; must be pre-heated because it conducts only when hot |
| **Globar** | Silicon carbide rod | About 1300 °C; self-starting; more energy at low wavenumbers |
| **Incandescent wire** | Nichrome or rhodium coil | Lower intensity, long life |
| Mercury arc | | Far IR |

### Wavelength selectors

**Prisms** of NaCl (common range 4000–650 cm⁻¹), KBr or CsI (for lower wavenumbers). Salt prisms absorb moisture and must be kept dry. **Diffraction gratings** give better resolution and are used in modern dispersive instruments. **Michelson interferometer** in FTIR: all wavelengths reach the detector together, giving fast scans and a better signal-to-noise ratio (Fellgett and Jacquinot advantages).

### Detectors (thermal and others)

| Detector | Principle |
| --- | --- |
| **Thermocouple** | Two dissimilar metals (bismuth and antimony) joined; a blackened junction warmed by IR produces a voltage proportional to the temperature difference. Several in series make a thermopile. |
| **Bolometer** | A thin blackened strip of metal (platinum or nickel) whose **electrical resistance changes** with temperature; placed in a Wheatstone bridge circuit. |
| **Thermistor** | A bolometer made of a semiconductor (fused metal oxides of Mn, Co, Ni); resistance falls sharply as temperature rises, so it is more sensitive than a metal bolometer. |
| **Golay cell (pneumatic detector)** | A small chamber of xenon gas with a blackened membrane at one end and a flexible mirrored diaphragm at the other; IR warms the gas, it expands and bends the diaphragm, and the change in a reflected light beam is read by a photocell. Sensitive, slow and fragile. |
| **Pyroelectric detector** | A crystal such as triglycine sulphate (TGS or deuterated DTGS) that changes its electrical polarisation (surface charge) with temperature; responds to the **rate of change** of temperature, so it is fast and suits FTIR. |
| Photoconductive (MCT) | Mercury cadmium telluride; very fast and sensitive; cooled with liquid nitrogen; used in FTIR. |

## 2.6 Applications of IR spectroscopy

1. **Identification of drugs:** the sample spectrum is matched with a reference spectrum (IP identity test). The fingerprint region makes the match specific.
2. **Functional group detection** and structure elucidation together with NMR and mass spectra.
3. **Polymorphism:** different crystal forms give different spectra in the solid state (so the IP asks to dissolve and recrystallise both sample and reference if they differ).
4. **Purity and impurities:** extra bands show impurities (for example a C=O band in an alcohol).
5. **Following reactions:** disappearance of a starting-material band or appearance of a product band.
6. **Hydrogen bonding studies**, geometric isomers, keto–enol tautomerism.
7. **Quantitative analysis** (limited): measured with the baseline method at a chosen band.
8. **Near-IR** for non-destructive checking of raw materials and moisture.

## 2.7 Flame photometry (flame emission spectroscopy)

### Principle

A solution of a metal salt is sprayed as a fine mist into a flame. The heat evaporates the solvent, vaporises the salt and breaks it into **free atoms**. Some atoms absorb heat energy and their outer electrons jump to higher levels. On returning to the ground state they emit light of a **characteristic wavelength**. The intensity of this emission is proportional to the number of excited atoms and hence to the concentration of the element.

**Events in the flame**

```text
 Solution (MX in water)
   | nebulisation        -> fine droplets
   | desolvation         -> solid salt particles
   | vaporisation        -> MX (gas)
   | atomisation         -> M (atoms) + X
   | excitation (heat)   -> M*
   v emission            -> M + hν (characteristic wavelength)
```

Alkali and alkaline earth metals are easily excited by flame heat, so flame photometry is mainly used for them.

| Element | Wavelength (nm) | Flame colour |
| --- | --- | --- |
| Sodium | 589 | Yellow |
| Potassium | 766 (filter about 767–768) | Violet (lilac) |
| Lithium | 671 | Crimson red |
| Calcium | 622 (CaOH band; Ca line 423) | Brick red |
| Barium | 554 | Apple green |

### Flames

| Fuel–oxidant | Temperature (approx.) |
| --- | --- |
| Natural gas or propane–air | 1700–1900 °C |
| Acetylene–air | 2100–2400 °C |
| Hydrogen–oxygen | about 2700 °C |
| Acetylene–oxygen | about 3000 °C |
| Acetylene–nitrous oxide | about 2700–2800 °C |

### Instrumentation

```text
 FLAME PHOTOMETER

 [Sample solution] -> [Nebuliser/atomiser] -> [Burner + flame] -> [Lens/mirror] -> [Filter or monochromator] -> [Detector] -> [Readout]
                       (compressed air)       (fuel gas + air)                    (589 nm for Na,             photocell or
                                                                                   766 nm for K)              PMT
```

- **Burners:** **total consumption (turbulent) burner**, where sample, fuel and oxidant meet at the tip and all the sample enters the flame; and **premix (laminar flow) burner**, where the mist is mixed with gases in a chamber and large drops drain away, giving a steady, quiet flame. Mecker and Lundegardh burners are named types.
- **Nebuliser:** sucks the solution up a capillary and breaks it into a fine spray using a jet of compressed air.
- **Optics and wavelength selector:** a mirror behind the flame increases light collected; **filters** in simple instruments, a monochromator in spectrophotometric models.
- **Detector:** photovoltaic cell, phototube or photomultiplier tube.

### Interferences

| Interference | Cause | Remedy |
| --- | --- | --- |
| Spectral | Emission lines or bands of other elements overlap the analyte line; flame background | Better wavelength selection, background correction |
| Ionisation | At high flame temperature, easily ionised atoms (K, Na) form ions that do not emit the atomic line, lowering the signal | Add an ionisation suppressor (excess of another easily ionised metal, such as caesium or potassium) |
| Chemical | Analyte forms a stable compound that does not atomise (Ca with phosphate, sulphate, aluminium) | Add a releasing agent (lanthanum or strontium chloride) or a protective agent (EDTA); use a hotter flame |
| Physical (matrix) | Viscosity, surface tension and dissolved solids change the spray rate | Match standards with the sample matrix; dilute |
| Self-absorption | At high concentrations, cooler outer atoms absorb emitted light | Work at low concentrations |
| Cation–anion enhancement | Other ions change atomisation | Matrix matching, standard addition |

### Methods of quantitation

1. **Calibration (standard) curve:** emission readings of standards against concentration; read the unknown.
2. **Standard addition:** known amounts of analyte added to portions of the sample; corrects for matrix effects.
3. **Internal standard:** a fixed amount of another element (lithium) is added to every solution; the ratio of analyte to lithium emission is used, which cancels flame fluctuations.

### Applications

- Sodium and potassium in serum, urine and other body fluids.
- Na, K, Li and Ca in pharmaceutical products: oral rehydration salts, intravenous fluids, lithium carbonate tablets, dialysis solutions.
- Analysis of soil, water and glass; alkali content of glass containers.

**Advantages:** simple, fast, inexpensive, good for alkali metals. **Disadvantages:** limited to easily excited elements, many interferences, flame must be very stable, cannot tell the chemical form of the element.

## 2.8 Atomic absorption spectroscopy (AAS)

### Principle

Free atoms in the **ground state** absorb light of exactly the wavelength they would emit (their **resonance line**). In a flame most atoms stay in the ground state (only a tiny fraction is excited), so absorption is far more sensitive and less temperature-dependent than emission. The absorbance follows Beer's law: **A = log (I0/I) = k × c**.

**Flame photometry vs AAS**

| Feature | Flame photometry | AAS |
| --- | --- | --- |
| Measures | Light emitted by excited atoms | Light absorbed by ground-state atoms |
| Source lamp | Not needed (flame excites) | Hollow cathode lamp of the element |
| Effect of flame temperature | Large | Small |
| Elements | Mainly alkali and alkaline earth | About 70 metals and metalloids |
| Sensitivity | Moderate (ppm) | High (ppm with flame; ppb with furnace) |

### Instrumentation

```text
 ATOMIC ABSORPTION SPECTROPHOTOMETER

 [Hollow cathode lamp] -> [Chopper] -> [Flame (laminar burner) or graphite furnace] -> [Monochromator] -> [Detector: PMT] -> [Readout]
  (cathode of the                         sample atoms absorb the resonance line         isolates the
   element to be measured)                                                               resonance line
```

- **Hollow cathode lamp (HCL):** a glass cylinder filled with neon or argon at low pressure; the cathode is a hollow cup made of (or lined with) the element being measured; the anode is tungsten or nickel. At a few hundred volts the fill gas ionises, ions strike the cathode, sputter metal atoms and excite them, so the lamp emits the sharp lines of that element. One lamp per element (multi-element lamps exist). **Electrodeless discharge lamps** give higher intensity for volatile elements (As, Se).
- **Chopper / modulation:** the lamp beam is chopped and the amplifier responds only to the modulated signal, so steady emission from the flame is ignored.
- **Atomisers:**
  - **Flame:** premix laminar-flow burner with a long slot (about 10 cm) to give a long path; air–acetylene for most metals, nitrous oxide–acetylene for refractory elements (Al, Si, Ti).
  - **Graphite furnace (electrothermal):** a small graphite tube heated electrically in steps (dry, ash, atomise); a few microlitres of sample; all of it is atomised, so detection limits are 100–1000 times lower.
  - **Cold vapour** for mercury (reduced to Hg vapour by stannous chloride) and **hydride generation** for As, Se, Sb (volatile hydrides with sodium borohydride).
- **Monochromator** (grating) and **photomultiplier detector**.

### Interferences

| Type | Example | Remedy |
| --- | --- | --- |
| Spectral | Overlap of another element's line; molecular absorption and light scattering by particles in the flame (background) | Background correction with a **deuterium lamp** or **Zeeman** correction; choose another line |
| Chemical | Phosphate lowers calcium absorption by forming refractory calcium phosphate | Releasing agent (La or Sr salt), protective agent (EDTA), hotter flame (N2O–acetylene) |
| Ionisation | Atoms ionised in hot flames do not absorb | Ionisation suppressor (excess K or Cs) |
| Physical / matrix | Viscosity, dissolved solids, organic solvents change nebulisation | Matrix-matched standards, standard addition |

### Applications

- Trace metals and **elemental impurities** in drugs and excipients: lead, cadmium, arsenic, mercury.
- Zinc in insulin preparations and zinc salts; calcium and magnesium in formulations and serum; copper, iron, lithium.
- Metals in water, food, blood (lead poisoning) and urine; catalyst residues (Pd, Ni, Pt) in drug substances.
- Environmental, clinical and toxicological analysis.

## 2.9 Nephelometry and turbidimetry

### Principle

When light passes through a suspension of fine particles, part of it is **scattered** (Tyndall effect) and the transmitted beam becomes weaker.

- **Turbidimetry** measures the intensity of the **transmitted** light (in line with the beam). It suits fairly concentrated suspensions. It follows a Beer-like relation: **S = log (I0/I) = k b c**, where S is turbidance.
- **Nephelometry** measures the **scattered** light, usually at **90°** to the beam. It suits very dilute suspensions, where the scattered intensity is proportional to concentration: **Is = Ks × c**.

Scattering depends on the number and size of particles, the wavelength of light (smaller particles scatter shorter wavelengths more strongly) and the difference in refractive index between particles and medium.

**Conditions for reproducible results:** the precipitate must form under fixed conditions of concentration, temperature, order and rate of mixing, time before reading and stirring. A **stabiliser or protective colloid** (gelatin, glycerol–ethanol mixture, gum) keeps the particles small and evenly suspended.

### Instrumentation

```text
 TURBIDIMETER                                    NEPHELOMETER

 [Lamp] -> [Filter] -> [Cell] -> [Detector]      [Lamp] -> [Filter] -> [Cell] -> (light trap)
                                 (in line,                               |
                                  transmitted)                           v 90 degrees
                                                                    [Detector] (scattered light)
```

- **Source:** tungsten lamp (white light) or a filtered or monochromatic source; shorter wavelengths give more scattering.
- **Cells:** cylindrical glass cells for nephelometers.
- **Detectors:** photovoltaic cells or photomultiplier tubes; a sensitive detector is needed for nephelometry because scattered light is weak.
- An ordinary colorimeter or spectrophotometer can work as a **turbidimeter**; a fluorimeter (90° geometry) can work as a **nephelometer**.
- Standards: freshly made suspensions of the same precipitate, or **formazin** suspensions for water turbidity (reported in NTU).

### Applications

- **Sulphate:** precipitated as barium sulphate with barium chloride in acid medium with a stabiliser; measured turbidimetrically.
- **Chloride:** precipitated as silver chloride with silver nitrate in nitric acid; measured nephelometrically. These are the instrumental form of the IP limit tests.
- **Clarity and opalescence of solutions** (pharmacopoeial comparison with reference suspensions); turbidity of water.
- **Microbiological (turbidimetric) assay** of antibiotics and vitamins: bacterial growth in broth makes it turbid.
- Phosphate, ammonia, carbon dioxide and some proteins (immunonephelometry of serum proteins).

## Remember

- IR: vibration must change the dipole moment; ν̄ = (1/2πc)√(k/µ); modes 3N − 6 (non-linear), 3N − 5 (linear).
- Stretching (symmetric, asymmetric) and bending (scissoring, rocking, wagging, twisting).
- Sample handling: KBr pellet, Nujol mull, neat film between salt plates, solution cells, gas cell, ATR.
- IR sources: Nernst glower, globar, nichrome wire. Detectors: thermocouple, bolometer, thermistor, Golay cell, pyroelectric (TGS).
- Flame photometry = emission; Na 589 nm, K 766 nm; flame events nebulisation → desolvation → atomisation → excitation → emission; lithium internal standard.
- AAS = absorption by ground-state atoms; hollow cathode lamp of the same element; chopper; flame or graphite furnace.
- Interferences: spectral, chemical (La releasing agent), ionisation (Cs suppressor), physical.
- Turbidimetry reads transmitted light; nephelometry reads scattered light at 90°.
