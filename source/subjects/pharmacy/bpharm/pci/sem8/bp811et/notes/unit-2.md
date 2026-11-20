# Unit 2: Thermal methods of analysis and X-ray diffraction

Two batches of the same drug can have the same chemical formula and the same assay value and still behave differently in a tablet, because their solid form differs: one may be a hydrate, another a different polymorph, a third partly amorphous. Thermal methods watch what a solid does when it is heated, and X-ray diffraction looks directly at how its molecules are packed. Both are core tools of preformulation and solid-state quality control.

## 2.1 Thermal methods: the common idea

**Thermal analysis** is a group of techniques in which a property of the sample is measured while its temperature is changed (or held) on a controlled programme.

| Technique | Property measured | Plot |
| --- | --- | --- |
| Thermogravimetric analysis (TGA) | Mass | Mass (%) vs temperature |
| Differential thermal analysis (DTA) | Temperature difference between sample and reference | ΔT vs temperature |
| Differential scanning calorimetry (DSC) | Heat flow difference between sample and reference | Heat flow (mW) vs temperature |

Events seen on heating:

| Event | Mass change (TGA) | Heat (DTA/DSC) |
| --- | --- | --- |
| Loss of water or solvent (desolvation) | Loss | Endothermic |
| Melting | None | Endothermic, sharp |
| Boiling, sublimation | Loss | Endothermic |
| Crystallisation of an amorphous solid | None | Exothermic |
| Glass transition | None | Step in baseline (change in heat capacity), not a peak |
| Polymorphic transition | None | Endo or exo |
| Decomposition | Loss | Endo or exo |
| Oxidation in air | Gain (sometimes) then loss | Exothermic |

## 2.2 Thermogravimetric analysis (TGA)

**Principle.** The sample is heated at a controlled rate in a chosen atmosphere and its **mass is recorded continuously**. A loss of mass at a particular temperature shows that a volatile part (water, solvent, CO2) has left or that the substance has decomposed. Mass changes give quantitative information directly.

**Thermogram.** A TGA curve is a series of plateaus (stable compounds) and steps (mass losses). The first derivative, **DTG** (dm/dt vs T), turns each step into a peak; the peak top is the temperature of fastest loss and helps separate overlapping steps.

**Instrumentation**

```text
          Recording / computer  <── balance control unit
                    ^                     |
                    |               Thermobalance (null-point microbalance)
                    |                     | hang-down wire
    Temperature programmer ──> Furnace [ sample pan  + thermocouple ]  <── purge gas (N2, air)
```

| Part | Details |
| --- | --- |
| **Thermobalance** | Sensitive microbalance (microgram resolution), usually **null-point** type: when the pan moves, an electromagnetic force restores it, and the restoring current is proportional to the mass change. Kept outside the hot zone |
| **Sample holder (crucible)** | Platinum, alumina or quartz pan, a few mg of sample |
| **Furnace** | Electrically heated, up to about 1000–1500 °C; low thermal mass for fast, uniform heating |
| **Temperature programmer and sensor** | Thermocouple close to the sample; linear heating rate, often 5–20 °C/min |
| **Purge gas** | Nitrogen or argon (inert) or air/oxygen (oxidising); also carries away volatile products |
| **Recorder / data system** | Plots mass against temperature and computes DTG |

**Factors affecting the TGA curve**

1. **Heating rate:** faster heating shifts losses to higher temperatures and can merge steps.
2. **Sample mass and particle size:** large or coarse samples heat unevenly and release gas slowly.
3. **Atmosphere:** inert vs oxidising gas changes the reactions; flow rate matters.
4. **Crucible shape and material:** a deep crucible traps vapour; some metals catalyse reactions.
5. **Buoyancy:** the gas around the pan gets less dense on heating, giving an apparent mass gain that must be corrected by a blank run.
6. **Packing of the sample** and condensation of volatiles on the cooler parts of the balance.

**Worked example 1: calcium oxalate monohydrate**, CaC2O4·H2O (Mr about 146.1), a standard test material, loses mass in three steps:

| Step | Reaction | Mass lost | Residue left |
| --- | --- | --- | --- |
| 1 (about 100–200 °C) | CaC2O4·H2O → CaC2O4 + H2O | 18.0 g/mol → 12.3% | 87.7% |
| 2 (about 400–500 °C) | CaC2O4 → CaCO3 + CO | 28.0 g/mol → 19.2% | 68.5% |
| 3 (about 650–850 °C) | CaCO3 → CaO + CO2 | 44.0 g/mol → 30.1% | 38.4% (CaO) |

Each percentage = (mass of lost molecule / 146.1) × 100. A good match between measured and calculated losses confirms the instrument is working and the composition is right.

**Worked example 2: is a theophylline sample the monohydrate?** Anhydrous theophylline C7H8N4O2 has Mr about 180.2; the monohydrate about 198.2. Expected water loss = 18.0/198.2 × 100 = **9.1%**. A loss of about 9% below about 120 °C fits the monohydrate; much less suggests partial dehydration.

**Applications of TGA in pharmacy**

1. Water and solvent content of drugs and excipients; distinguishing **hydrates and solvates** from adsorbed surface moisture.
2. Thermal stability and decomposition temperature; temperature limits for drying and processing.
3. Composition of mixtures and of inorganic residues (ash, filler content).
4. Kinetics of decomposition (activation energy) for stability prediction.
5. Evaluating packaging polymers and excipients (cellulose derivatives, starch).
6. Combined with DSC or with an IR or mass spectrometer to identify the gas released (evolved gas analysis).

## 2.3 Differential thermal analysis (DTA)

**Principle.** The sample and an **inert reference** (calcined alumina) are heated side by side in the same furnace at the same rate. A thermocouple in each measures temperature, and the **difference ΔT = T(sample) − T(reference)** is recorded against the reference (or furnace) temperature. When nothing happens, ΔT is zero (baseline). An endothermic change makes the sample lag behind (ΔT negative, downward peak by convention); an exothermic change makes it run ahead (upward peak).

```text
    ΔT
     ^                         exothermic (crystallisation, oxidation)
     |                 /\
  0  |______    _____/  \________
     |      \  /
     |       \/   endothermic (melting, dehydration)
     +-----------------------------------> Temperature
```

**Instrumentation**

| Part | Function |
| --- | --- |
| Furnace with temperature programmer | Heats both cups at a linear rate |
| Sample and reference holders | Twin cups in a metal or ceramic block, placed symmetrically |
| Differential thermocouple | Two junctions connected in opposition so the output is proportional to ΔT |
| Second thermocouple | Measures the sample or block temperature |
| Atmosphere control | Inert or reactive gas |
| Amplifier and recorder | ΔT is small, so it is amplified and plotted |

**Factors affecting DTA:** heating rate, sample mass and packing, particle size, thermal conductivity of sample vs reference, thermocouple position, atmosphere, and the dilution of the sample with reference material.

**Applications:** melting point and purity checks, polymorphic transitions, dehydration, decomposition, identification by comparing thermograms, phase diagrams and drug–excipient interactions. Peak area is proportional to the heat change, but DTA is mostly **qualitative**, because the relation between area and enthalpy depends on the instrument and sample.

## 2.4 Differential scanning calorimetry (DSC)

**Principle.** DSC measures the **difference in heat flow** (energy per unit time, mW) needed to keep the sample and an empty reference pan on the same temperature programme. Peak area gives the enthalpy change directly, so DSC is **quantitative**.

**Two types**

| Feature | Power-compensation DSC | Heat-flux DSC |
| --- | --- | --- |
| Heaters | Separate heater and sensor for sample and reference | One furnace heats both |
| What is measured | Extra electrical power fed to keep both at the same temperature | Temperature difference across a disc of known thermal resistance, converted to heat flow |
| Response | Very fast | Robust, good baseline |
| Relation to DTA | — | A calibrated, quantitative form of DTA |

```text
 Power-compensation DSC
   [sample pan] heater S + sensor S        [reference pan] heater R + sensor R
          \                                       /
           +-------> controller keeps T(S) = T(R) <-+
                         |
                 ΔP = dH/dt  ──> recorder: heat flow vs temperature
```

**The DSC curve.** Endothermic peaks (melting) are drawn downward or upward depending on the instrument's convention, so always read the label "endo ↓" or "exo ↑". From one curve you read:

- **Onset temperature** (extrapolated start) — taken as the melting point of a pure substance.
- **Peak temperature.**
- **Peak area** → enthalpy of fusion ΔHf (J/g).
- **Glass transition (Tg):** a step in the baseline of amorphous materials.
- **Cold crystallisation:** an exotherm as amorphous material crystallises on heating.

**Calibration.** Temperature and enthalpy are calibrated with high-purity metals of known melting point and heat of fusion, most often **indium** (mp 156.6 °C, ΔHf about 28.5 J/g); zinc and tin cover other ranges. Heat capacity is calibrated with sapphire.

**Purity by DSC.** Impurities lower and broaden the melting peak. For eutectic impurities, the **van't Hoff equation** relates the sample temperature Ts to the fraction melted F:

**Ts = T0 − (R T0² x2 / ΔHf) × (1/F)**

where T0 is the melting point of pure substance and x2 the mole fraction of impurity. Plotting Ts against 1/F gives a straight line whose slope gives x2. This works for fairly pure (above about 98 mol%) substances that melt without decomposing.

**Factors affecting DSC:** heating rate, sample mass, pan type (open, crimped, hermetic, pin-holed), purge gas, particle size and contact with the pan, and thermal history of the sample.

**Pharmaceutical applications of DSC**

1. **Polymorphism:** different polymorphs show different melting points and enthalpies; transitions between forms appear as extra peaks.
2. **Purity determination** (van't Hoff).
3. **Drug–excipient compatibility** in preformulation: a peak that shifts or disappears in a physical mixture warns of interaction.
4. **Glass transition** of amorphous drugs, solid dispersions and polymers; stability of amorphous forms.
5. **Hydrates and solvates** (with TGA).
6. **Lyophilisation:** finding the collapse or eutectic temperature to design freeze-drying cycles.
7. **Liposomes and lipid excipients:** phase transition temperature of phospholipids.
8. **Protein stability:** unfolding (denaturation) temperature.

**DTA vs DSC**

| Point | DTA | DSC |
| --- | --- | --- |
| Measures | ΔT between sample and reference | Difference in heat flow (energy) |
| Output | °C vs T | mW vs T |
| Quantitative enthalpy | Approximate | Accurate |
| Temperature range | Can go very high (above 1000 °C) | Usually to about 700 °C |
| Main use | Qualitative transitions, high-temperature inorganic work | Quantitative pharmaceutical solid-state work |

## 2.5 Origin of X-rays

**X-rays** are electromagnetic radiation of very short wavelength, about 0.01–10 nm (0.1–100 Å). Wavelengths near 1 Å match the spacing between atoms in crystals, which is why crystals diffract them.

**X-ray tube (Coolidge tube).** A heated tungsten filament (cathode) emits electrons. A high voltage (about 30–50 kV) accelerates them onto a metal target (anode: copper, molybdenum, cobalt, chromium) in an evacuated tube. Only about 1% of the energy becomes X-rays; the rest is heat, so the anode is water-cooled. X-rays leave through beryllium windows.

```text
   filament (−) e⁻ e⁻ e⁻ ───────────>  target anode (+, water-cooled Cu)
   (heated W)        high voltage            │
                                             └──> X-rays out through Be window
```

Two kinds of X-rays are produced:

1. **Continuous (white) radiation, bremsstrahlung:** electrons slow down in the field of the target nuclei and give a smooth range of wavelengths. The shortest wavelength depends only on the voltage: λmin = hc/eV. At 30 kV, λmin ≈ 0.41 Å; at 40 kV, about 0.31 Å (Duane–Hunt law).
2. **Characteristic (line) radiation:** an incoming electron knocks out an inner (K-shell) electron of a target atom. An electron from the L or M shell drops into the hole and emits an X-ray of a fixed energy, characteristic of the target metal: **Kα** (L → K) and **Kβ** (M → K). Copper Kα is about 1.54 Å; molybdenum Kα about 0.71 Å.

**Moseley's law:** the square root of the frequency of a characteristic line is proportional to the atomic number (√ν ∝ Z − σ). This founded X-ray fluorescence analysis of elements.

**Monochromatic X-rays** are needed for diffraction. A **filter** removes Kβ: a nickel foil absorbs Cu Kβ much more than Cu Kα (its absorption edge lies between them). A crystal monochromator (graphite) is also used.

**Detectors:** photographic film (older cameras), Geiger–Müller and proportional counters, scintillation counters, and modern solid-state and area detectors (CCD, pixel detectors).

## 2.6 Basic aspects of crystals

A **crystal** is a solid whose atoms or molecules repeat in a regular three-dimensional pattern. An **amorphous** solid (glass) has no long-range order.

- **Lattice:** the array of points that repeats the pattern.
- **Unit cell:** the smallest repeating box, defined by edge lengths a, b, c and angles α, β, γ.
- **Seven crystal systems** and **fourteen Bravais lattices.**

| Crystal system | Edges | Angles |
| --- | --- | --- |
| Cubic | a = b = c | α = β = γ = 90° |
| Tetragonal | a = b ≠ c | all 90° |
| Orthorhombic | a ≠ b ≠ c | all 90° |
| Monoclinic | a ≠ b ≠ c | α = γ = 90°, β ≠ 90° |
| Triclinic | a ≠ b ≠ c | α ≠ β ≠ γ ≠ 90° |
| Hexagonal | a = b ≠ c | α = β = 90°, γ = 120° |
| Rhombohedral (trigonal) | a = b = c | α = β = γ ≠ 90° |

Most organic drugs crystallise in the low-symmetry monoclinic, triclinic or orthorhombic systems.

**Miller indices (h k l)** name a family of parallel lattice planes: take the intercepts of a plane on the a, b and c axes in unit-cell lengths, take reciprocals and clear fractions. For a cubic cell the spacing between (h k l) planes is

**d = a / √(h² + k² + l²)**

**Polymorphism:** the ability of one compound to crystallise in more than one arrangement. Polymorphs differ in melting point, solubility, dissolution rate, stability and sometimes bioavailability. **Pseudopolymorphs** are hydrates and solvates.

## 2.7 Bragg's law

X-rays scattered by electrons in successive parallel planes reinforce each other only when the extra path travelled by the lower ray is a whole number of wavelengths.

```text
 incident        reflected
     \   θ   θ   /
  ----\-----.---/-------  plane 1
       \    |  /            extra path = 2d sinθ
  ------\---.-/---------  plane 2       (d = spacing between planes)
 Constructive interference when 2d sinθ = nλ
```

**nλ = 2d sinθ**

where n is the order (usually 1), λ the wavelength, d the interplanar spacing and θ the glancing (Bragg) angle. Diffractometers record the angle **2θ** between the incident and diffracted beams.

**Worked examples (Cu Kα, λ = 1.5406 Å, n = 1)**

| Observed 2θ | θ | d = λ/(2 sinθ) |
| --- | --- | --- |
| 10° | 5° | 8.84 Å |
| 20° | 10° | 4.44 Å |
| 30° | 15° | 2.98 Å |

Sodium chloride is cubic with a = 5.64 Å. For the (200) planes, d = 5.64/√4 = 2.82 Å, so sinθ = 1.5406/(2 × 2.82) = 0.273, θ ≈ 15.9° and the peak appears at **2θ ≈ 31.7°**. For the (111) planes, d = 5.64/√3 = 3.26 Å, giving 2θ ≈ 27.4°.

## 2.8 X-ray crystallography and diffraction methods

| Method | Radiation | Sample | Movement | What you get |
| --- | --- | --- | --- | --- |
| **Laue method** | Polychromatic (white) | Single crystal | Stationary | Spot pattern showing symmetry and orientation of the crystal |
| **Rotating crystal method** | Monochromatic | Single crystal | Crystal rotated about one axis | Layer lines of spots on a cylindrical film; unit-cell dimensions |
| **Single crystal diffractometry** | Monochromatic | Single crystal (about 0.1–0.5 mm) | Rotated through many orientations (goniometer) | Intensities of thousands of reflections → complete 3D structure |
| **Powder method** (Debye–Scherrer; powder diffractometer) | Monochromatic | Fine powder, random orientation | Sample or detector scanned through 2θ | Rings or a diffractogram of peaks at characteristic 2θ: the fingerprint of a crystal form |

### Rotating crystal technique

A single crystal is mounted so that one of its axes is perpendicular to a monochromatic beam and is rotated (or oscillated) about that axis. A cylindrical film surrounds the crystal. As the crystal turns, each set of planes passes through its Bragg angle and gives a spot. The spots lie on horizontal **layer lines**; their spacing gives the repeat distance along the rotation axis, and their positions are used to index reflections and find the unit cell. Oscillating or Weissenberg variations reduce overlap of spots.

### Single crystal diffraction

```text
 X-ray tube ─> monochromator ─> collimator ─> crystal on goniometer head ─> area detector
                                                (rotated in 3 axes; often cooled to about 100 K)
                                  computer: indexing, intensities, structure solution, refinement
```

1. A good single crystal is mounted on a goniometer and rotated through many orientations.
2. Positions of the spots give the unit cell and crystal system; systematic absences give the space group.
3. Intensities of the spots depend on where the atoms are. Each intensity gives the amplitude of a structure factor, but the phase is lost (**the phase problem**).
4. Phases are estimated by direct methods (small molecules) or Patterson and heavy-atom methods; a Fourier synthesis then gives an **electron-density map**.
5. Atoms are placed in the density peaks and the model is refined until calculated and observed intensities agree (low R-factor).
6. Output: exact bond lengths, bond angles, conformation, absolute configuration (stereochemistry) and hydrogen-bonding packing.

### Powder diffraction (PXRD)

A finely powdered sample contains crystallites in every orientation, so for every set of planes some crystallites are always at the Bragg angle. In a **powder diffractometer** (Bragg–Brentano geometry) the sample sits flat on a holder; as the tube and detector move, the detector counts intensity against 2θ.

- **Peak positions (2θ → d)** identify the crystal form.
- **Relative peak intensities** confirm the identity (they can be distorted by preferred orientation of needle or plate crystals).
- **Peak width** relates to crystallite size; the **Scherrer equation** τ = Kλ/(β cosθ) estimates size from the extra breadth β (in radians). Example: K = 0.9, λ = 1.5406 Å, β = 0.20°, 2θ = 20° → τ ≈ 40 nm.
- **Amorphous material** gives a broad hump ("halo") with no sharp peaks.

## 2.9 Structural elucidation and applications of XRD

1. **Complete three-dimensional structure** of drugs, natural products and proteins (single crystal); absolute configuration of chiral drugs. Drug–receptor and enzyme complexes are solved this way for structure-based drug design.
2. **Identification of polymorphs and pseudopolymorphs** (PXRD fingerprint); controlling the right form in API and tablets.
3. **Degree of crystallinity** and detection of amorphous content, for example after milling or in solid dispersions.
4. **Quantitative phase analysis:** amount of an unwanted polymorph in a mixture from peak intensities.
5. **Monitoring form changes** during granulation, drying, compression and storage (stability).
6. **Identification of unknown crystalline substances** by comparing d-spacings with reference patterns.
7. **Crystallite size and strain** (Scherrer).
8. **Protecting patents:** a new crystal form is often defined by its PXRD peaks.
9. **Excipients:** crystallinity of lactose, cellulose and other excipients.

## Remember

- TGA = mass vs T (null-point thermobalance); DTG separates steps; calcium oxalate monohydrate loses 12.3%, 19.2%, 30.1%.
- DTA = ΔT vs T (qualitative); DSC = heat flow vs T (quantitative ΔH); indium calibrates DSC.
- Endothermic: melting, dehydration; exothermic: crystallisation, oxidation; Tg is a baseline step.
- DSC purity: van't Hoff, Ts vs 1/F.
- X-rays: bremsstrahlung (λmin = hc/eV) + characteristic Kα, Kβ; Ni filter removes Cu Kβ; Cu Kα about 1.54 Å.
- Seven crystal systems, fourteen Bravais lattices; cubic d = a/√(h² + k² + l²).
- Bragg: nλ = 2d sinθ; diffractometers read 2θ.
- Laue (white, stationary), rotating crystal (monochromatic, rotated), single crystal (full structure), powder (fingerprint of polymorphs).
