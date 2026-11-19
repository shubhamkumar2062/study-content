# Unit 5: Electrochemical methods of analysis

Electrochemical methods measure an electrical property of a solution — conductance, potential or current — instead of watching an indicator change colour. They give end points in coloured, turbid or very dilute solutions, in mixtures, and for weak acid–weak base systems where indicators fail. The syllabus covers three: conductometry, potentiometry and polarography.

| Method | What is measured | Typical use |
| --- | --- | --- |
| Conductometry | Conductance (ease of current flow through the whole solution) | Conductometric titrations, purity of water |
| Potentiometry | Potential (emf) of a cell at nearly zero current | pH measurement, potentiometric titrations |
| Polarography (voltammetry) | Current as voltage is changed at a dropping mercury electrode | Trace metals, reducible drugs |

## 5.1 Conductometry

### Basic terms

Electrolyte solutions conduct electricity by the movement of ions. Conductance is the reciprocal of resistance.

| Term | Symbol and formula | Unit |
| --- | --- | --- |
| Resistance | R = ρ (l/A) | ohm (Ω) |
| Conductance | G = 1/R | siemens (S) = mho (Ω⁻¹) |
| Specific resistance (resistivity) | ρ | Ω cm |
| Specific conductance (conductivity) | κ = 1/ρ = G × (l/A) | S cm⁻¹ |
| Cell constant | K = l/A (distance between electrodes ÷ area) | cm⁻¹ |
| Equivalent conductance | Λeq = κ × 1000 / N | S cm² equiv⁻¹ |
| Molar conductance | Λm = κ × 1000 / M | S cm² mol⁻¹ |

- **κ = G × cell constant.** The cell constant is found by measuring the conductance of a standard KCl solution of known κ (for example 0.01 M KCl, κ about 0.001413 S cm⁻¹ at 25 °C).
- **Worked example:** a cell filled with 0.01 M KCl (κ = 0.001413 S cm⁻¹) shows a conductance of 0.001570 S. Cell constant = κ/G = 0.001413/0.001570 = **0.900 cm⁻¹**. The same cell filled with a 0.02 M solution of a salt shows 0.002800 S, so κ = 0.002800 × 0.900 = 0.002520 S cm⁻¹ and Λm = 0.002520 × 1000/0.02 = **126 S cm² mol⁻¹**.

**Factors affecting conductance:** number of ions (concentration), charge on ions, **ionic mobility** (size and hydration; H⁺ and OH⁻ are by far the fastest — about 350 and 198 S cm² mol⁻¹ respectively at 25 °C, versus 40–80 for most other ions), temperature (conductance rises about 2% per °C — keep temperature constant), viscosity of the solvent.

**Kohlrausch's law of independent migration of ions:** at infinite dilution, the molar conductance of an electrolyte is the sum of the limiting conductances of its cation and anion: Λ°m = λ°+ + λ°−. It lets Λ° of weak electrolytes (acetic acid) be calculated from strong ones and the degree of dissociation found: α = Λm/Λ°m.

### Conductivity cell and measurement

```text
      AC source (about 1 kHz)        null detector
             |                            |
     ____ R1 ____ R2 ____          Wheatstone bridge:
    |                    |         at balance R_cell = R3 x (R1/R2)
    R3                 cell
    |____________________|
                                    Conductivity cell:
     ___________                    two parallel platinum plates,
    |  |     |  |                   coated with platinum black,
    |  |plate|  |  <- fixed         fixed apart, sealed in glass;
    |  |     |  |     distance      dipped in the solution
    |__solution_|
```

- **Electrodes:** two platinum plates coated with **platinum black** (platinised), held rigidly so that l/A stays constant. Platinum black increases the effective surface area and reduces polarisation.
- **Alternating current** (about 50–1000 Hz) is used, not DC — DC would electrolyse the solution and polarise the electrodes, changing the reading.
- Measured with a **Wheatstone bridge** (null point with headphones or a magic-eye/electronic detector) or a direct-reading conductivity meter.
- Types of cell: dip-type (immersion) cell, flow-through cells, cells of different constants for low and high conductivity solutions.

### Conductometric titrations

**Principle:** during a titration the ions of the analyte are replaced by ions of different mobility, so the conductance changes. Conductance is plotted against volume of titrant; two (or more) nearly straight lines are obtained and **their point of intersection is the end point**. Points near the end point are not needed (hydrolysis and dissociation make them curve), so the method is good for weak acids and bases.

**Practical points:** use a titrant 10–20 times more concentrated than the titrand (so the volume barely changes) or apply a dilution correction: corrected G = observed G × (V + v)/V; keep temperature constant; stir after each addition.

**(a) Strong acid with strong base (HCl × NaOH)**

H⁺ Cl⁻ + Na⁺ OH⁻ → Na⁺ Cl⁻ + H2O

Fast H⁺ ions are replaced by slow Na⁺, so conductance **falls steeply** to a minimum at the end point; after it, excess Na⁺ and fast OH⁻ make it **rise** again. **V-shaped** curve.

**(b) Weak acid with strong base (CH3COOH × NaOH)**

Weak acid conducts poorly at first. Initially a small fall (common-ion effect of acetate suppresses ionisation) may appear, then conductance **rises slowly** as highly ionised sodium acetate forms; after the end point it rises **steeply** (excess OH⁻). The intersection gives the end point.

**(c) Strong acid with weak base (HCl × NH3)**

Falls steeply as H⁺ is replaced by NH4⁺; after the end point the excess weak base hardly ionises, so the curve stays **almost flat**.

**(d) Weak acid with weak base (CH3COOH × NH3)**

Rises as ammonium acetate forms; after the end point stays nearly constant. A clear break even though no indicator can be used — a major advantage of conductometry.

**(e) Mixture of strong and weak acid (HCl + CH3COOH) with NaOH**

1. First the strong acid reacts: steep **fall** (H⁺ replaced by Na⁺) — first end point.
2. Then the weak acid: slow **rise** (sodium acetate formed) — second end point.
3. Then excess NaOH: steep **rise**.

The first break gives the HCl; the volume between the first and second breaks gives the acetic acid.

**(f) Precipitation titrations** — e.g. KCl with AgNO3: K⁺Cl⁻ + Ag⁺NO3⁻ → AgCl + K⁺NO3⁻; Cl⁻ replaced by NO3⁻ of similar mobility, so the line is nearly flat, then rises after the end point. Also BaCl2 with Li2SO4/ MgSO4.

**(g) Displacement and complexometric titrations** — salts of weak acids (sodium acetate with HCl) and some EDTA titrations.

```text
 G                                       G
 |\                /                     |               /
 | \              /    HCl vs NaOH       |\            /   HCl + CH3COOH
 |  \            /     (V shape)         | \       ___/    vs NaOH
 |   \          /                        |  \  ___/        two breaks
 |    \________/                         |   \/
 +-------|------------ volume            +---|----|------- volume
       end point                            EP1  EP2
```

### Advantages and limitations of conductometric titrations

| Advantages | Limitations |
| --- | --- |
| Coloured, turbid and very dilute solutions | Not suitable when large amounts of other (foreign) electrolytes are present — they mask the change |
| Weak acid/weak base and mixtures titrated | Temperature must be controlled |
| No indicator needed; end point from graph, objective | Fewer applications in redox titrations |
| Points away from the end point are used, so slow or incomplete reactions near equivalence do not matter much | Needs several readings and plotting |

**Applications:** acid–base, precipitation, complexometric and non-aqueous titrations; checking purity of distilled/deionised water (conductivity limits in IP for purified water and water for injections); solubility of sparingly soluble salts; degree of dissociation, Ka of weak acids; basicity of acids; kinetics of reactions involving ions.

## 5.2 Potentiometry

**Potentiometry** measures the emf of an electrochemical cell, made of an **indicator electrode** (whose potential depends on the analyte concentration) and a **reference electrode** (constant potential), at practically zero current.

### Electrochemical cell

```text
   Reference electrode | salt bridge | test solution | indicator electrode
   (constant E)          (KCl, joins     (analyte)       (E changes with
                          solutions)                       analyte activity)
   E(cell) = E(indicator) - E(reference) + E(junction)
```

- **Galvanic cell:** produces electricity from a spontaneous reaction (used in potentiometry). **Electrolytic cell:** current applied from outside drives a reaction (polarography, electrolysis).
- **Anode** = oxidation; **cathode** = reduction.
- **Salt bridge** (saturated KCl in agar) completes the circuit and keeps the liquid junction potential small (K⁺ and Cl⁻ move at nearly equal speed).

**Nernst equation** for Mⁿ⁺ + ne⁻ ⇌ M at 25 °C:

E = E° + (0.0591/n) log a(Mⁿ⁺)

For a general couple E = E° + (0.0591/n) log [Ox]/[Red]. A tenfold change in ion activity changes E by 59.1/n mV.

### Reference electrodes

A good reference electrode has a known, constant, reproducible potential that is not affected by the test solution, and is easy to make.

| Electrode | Construction | Half reaction | Potential vs SHE at 25 °C |
| --- | --- | --- | --- |
| **Standard hydrogen electrode (SHE)** | Platinum foil coated with platinum black, dipped in 1 M H⁺ (unit activity), hydrogen gas bubbled at 1 atm | 2H⁺ + 2e⁻ ⇌ H2 | 0.000 V (by definition) |
| **Saturated calomel electrode (SCE)** | Mercury in contact with a paste of mercurous chloride (calomel, Hg2Cl2) and mercury, in saturated KCl; platinum wire contact; porous fibre or sintered junction | Hg2Cl2 + 2e⁻ ⇌ 2Hg + 2Cl⁻ | about +0.242 V (depends on KCl concentration: 1 M about 0.280 V; 0.1 M about 0.334 V) |
| **Silver–silver chloride electrode** | Silver wire coated with AgCl dipping in KCl solution (saturated or 3.5 M) | AgCl + e⁻ ⇌ Ag + Cl⁻ | about +0.197–0.20 V (saturated KCl) |

```text
  SATURATED CALOMEL ELECTRODE          Ag/AgCl ELECTRODE
       | Pt wire                          | Ag wire
   ____|____                          ____|____
  |  Hg     |  <- inner tube         |   |     |
  | Hg/Hg2Cl2 paste                  |  AgCl   | <- coating on wire
  |_________|                        |  coat   |
  | sat. KCl + KCl crystals |        | KCl soln|
  |______  _______|                  |___  ____|
         ||  <- porous plug               ||  <- porous junction
```

**SHE limitations:** hard to set up, needs pure hydrogen and a platinised surface that is easily poisoned (by arsenic, sulphide, proteins), can't be used with oxidising agents — so it is the primary standard but not used routinely. The SCE and Ag/AgCl are used in practice (Ag/AgCl preferred where mercury is unwanted and at higher temperatures).

### Indicator electrodes

**(a) Metal electrodes**

| Kind | Description | Example |
| --- | --- | --- |
| First kind | Metal in contact with its own ions; responds to their activity | Ag in Ag⁺ (argentometric titrations), Cu in Cu²⁺ |
| Second kind | Metal coated with its sparingly soluble salt; responds to the anion | Ag/AgCl responds to Cl⁻ |
| Third kind | Responds to a different cation through linked equilibria | Hg/Hg–EDTA for metal ions in EDTA titrations |
| Inert (redox) electrodes | Platinum or gold wire; senses the ratio of oxidised to reduced forms | Pt in Fe²⁺/Fe³⁺, Ce⁴⁺ titrations |
| Antimony electrode | Sb/Sb2O3 responds to pH | Rough pH, unaffected by HF |

**(b) Glass electrode (membrane electrode for H⁺)**

```text
        | lead to meter
        |
   _____|_____
  |     |     |   <- glass or plastic stem
  |   Ag/AgCl |   internal reference electrode
  |   wire    |
  |  0.1 M HCl|   internal solution (constant pH)
   \_________/
    \_______/     <- thin bulb of special pH-sensitive glass
                     (Na2O / CaO / SiO2 type), hydrated surface layers
```

- **Working:** the thin glass membrane has hydrated gel layers on both faces. H⁺ ions exchange with Na⁺ in the gel; a potential develops across the membrane that depends on the difference in H⁺ activity between the inside (fixed) and outside (sample). E = constant + 0.0591 log a(H⁺) = constant − 0.0591 pH (25 °C).
- It is used together with an SCE or Ag/AgCl reference (often built into one **combination electrode**) and a high-impedance pH meter (the membrane resistance is very high).
- **Calibration** with standard buffers (pH 4.0, 7.0, 9.2) because of the **asymmetry potential** (small potential even when solutions on both sides are the same).
- **Advantages:** not affected by oxidising or reducing agents, by colour or turbidity; works in small volumes; fast; not poisoned easily.
- **Limitations:** **alkaline (sodium) error** above about pH 10 with high Na⁺ (reads low); **acid error** below about pH 1; fragile; must be kept hydrated; slow in non-aqueous solvents.
- **Ion-selective electrodes** (F⁻, Ca²⁺, K⁺ etc.) work on the same membrane principle.

### Potentiometric titrations

**Principle:** the emf of indicator + reference electrodes is recorded after each addition of titrant. Near the equivalence point the analyte concentration changes by several powers of ten, so the potential (or pH) jumps sharply; the end point is found from the graph.

**Methods of locating the end point**

1. **Direct plot (E or pH vs V):** S-shaped curve; end point = point of inflection (middle of the steep rise).
2. **First derivative (ΔE/ΔV vs mean V):** a peak; the maximum is the end point.
3. **Second derivative (Δ²E/ΔV² vs V):** the curve crosses zero at the end point; most precise.
4. **Gran's plot:** a function of E (e.g. V × 10^(E/0.059)) plotted against V gives straight lines that cut the axis at the end point; uses points before the end point.
5. **Titration to a preset potential/pH** with automatic titrators.

```text
 E or pH          dE/dV                 d2E/dV2
   |      ___       |     /\              |    /\
   |     /          |    /  \             |___/  \______
   |    |           |   /    \            |        \/
   |___/            |__/      \___        |
   +----|------ V   +----|------- V       +----|------- V
       EP                EP                    EP (zero crossing)
```

**Worked example (first derivative).** Near the end point of 0.1 M HCl vs 0.1 M NaOH:

| V (ml) | pH | ΔpH/ΔV | Mean V |
| --- | --- | --- | --- |
| 24.6 | 4.0 | — | — |
| 24.8 | 4.3 | 1.5 | 24.7 |
| 25.0 | 7.0 | 13.5 | 24.9 |
| 25.2 | 9.7 | 13.5 | 25.1 |
| 25.4 | 10.0 | 1.5 | 25.3 |

The maximum ΔpH/ΔV lies between 24.9 and 25.1 ml, so the end point is about **25.0 ml**.

**Electrode pairs for each titration**

| Titration | Indicator electrode | Reference |
| --- | --- | --- |
| Acid–base (aqueous and non-aqueous) | Glass | SCE or Ag/AgCl |
| Redox | Platinum | SCE |
| Precipitation (argentometric) | Silver | SCE with a KNO3 salt bridge (Cl⁻ must not leak) or glass |
| Complexometric | Mercury (third kind) or ion-selective | SCE |

**Advantages:** coloured, turbid, dilute solutions; no indicator; weak acids and mixtures; non-aqueous titrations; can be automated; more accurate than visual. **Applications:** pH measurement of preparations (IP requirement for many injections and eye drops), pKa determination, assay of drugs by potentiometric acid–base, redox, precipitation and non-aqueous titrations, diazotisation end points, Karl Fischer water determination (biamperometric variant).

## 5.3 Polarography

**Polarography** is a voltammetric method in which a gradually increasing voltage is applied to a cell containing a **dropping mercury electrode (DME)** as the working (micro)electrode and a large reference electrode (SCE or a mercury pool), and the resulting current is recorded. The current–voltage curve is a **polarogram**. Developed by **Jaroslav Heyrovský** (1922), who received the Nobel Prize in Chemistry in 1959.

**Principle:** at the tiny mercury drop, the electroactive substance is reduced (or oxidised) at a potential characteristic of it. Once the potential is high enough, every molecule that reaches the drop reacts at once, so the current is limited by the rate of **diffusion** of the analyte to the drop and becomes proportional to its concentration.

### The polarogram

```text
 current (µA)
   |                       ___________  <- limiting current
   |                      /
   |                     /   } id = diffusion current
   |                    /      (proportional to concentration)
   |              ____./______  E1/2 = half-wave potential
   |   __________/              (at id/2; identifies the substance)
   |__/  residual current
   +------------------------------------- applied voltage (-E)
```

| Term | Meaning |
| --- | --- |
| **Residual current** | Small current before reduction starts: charging (condenser) current of each new drop plus traces of impurities |
| **Migration current** | Current from electrostatic attraction of ions to the electrode; removed by adding a large excess of an inert **supporting electrolyte** (e.g. KCl, tetraalkylammonium salts), which carries the current instead |
| **Diffusion current (id)** | Limiting current − residual current; controlled only by diffusion; proportional to concentration |
| **Limiting current** | Plateau current when every molecule reaching the drop is reduced |
| **Half-wave potential (E½)** | Potential at which the current is half the diffusion current; characteristic of each substance in a given medium, independent of concentration — used for **qualitative** analysis |

**Ilkovic equation** (relates diffusion current to concentration):

**id = 607 n D^(1/2) m^(2/3) t^(1/6) C**

| Symbol | Meaning (usual units) |
| --- | --- |
| id | Average diffusion current (µA) |
| n | Electrons transferred per molecule |
| D | Diffusion coefficient of the analyte (cm² s⁻¹) |
| m | Rate of flow of mercury (mg s⁻¹) |
| t | Drop time (s) |
| C | Concentration (millimoles per litre) |
| 607 | Constant (at 25 °C, for average current; 708 when the maximum current is used) |

For a given capillary and medium, everything except C is constant, so **id = k × C** — the basis of quantitative polarography (by calibration curve, standard addition or internal/pilot ion method). The term m^(2/3) t^(1/6) is the **capillary characteristic**.

**Other practical points**

- **Removal of oxygen:** dissolved O2 is reduced at the DME in two steps and gives its own waves; it is removed by bubbling pure **nitrogen** (or hydrogen) for 10–15 minutes before recording (sodium sulphite in alkaline solution is an alternative).
- **Polarographic maxima:** sharp peaks above the limiting current caused by streaming of solution round the drop; suppressed by **maximum suppressors** such as gelatin, Triton X-100 or methyl red (in small amounts).
- Temperature controlled to about ±0.5 °C (diffusion current rises about 1–2% per °C).

### Dropping mercury electrode (DME)

```text
       mercury reservoir (height adjustable)
              |
              |  flexible tubing
              |
          ____|____
         |  glass  |  <- fine glass capillary
         |capillary|     (bore about 0.05 mm, length 5-10 cm)
              |
              o   <- mercury drop grows and falls every 2-6 s
          solution with supporting electrolyte (N2 purged)
          counter/reference: SCE or mercury pool
```

**Advantages of the DME**

1. A **fresh, clean surface** forms with each drop, so results are reproducible and the electrode is not poisoned.
2. The surface area is small and reproducible, giving a small, reproducible current.
3. Mercury has a **high overpotential for hydrogen**, so many metal ions and organic compounds can be reduced (up to about −2 V vs SCE) before hydrogen is evolved.
4. Many metals dissolve in mercury forming amalgams, lowering their reduction potentials.
5. The diffusion current reaches a steady value quickly.

**Limitations:** mercury is toxic (careful handling and disposal); mercury is oxidised at about +0.4 V vs SCE, so the DME cannot be used for oxidations at positive potentials; the capillary can block; charging current limits sensitivity (improved in modern pulse methods).

### Rotating platinum electrode (RPE)

- A short platinum wire sealed into a glass tube, rotated at a constant speed (about 600 rpm) by a motor.
- Rotation stirs the solution, so the diffusion layer is thin and a steady limiting current is reached quickly — currents are much larger than at a stationary electrode.
- **Used for positive (oxidation) potentials** where mercury cannot be used (up to about +0.9 V vs SCE), and in **amperometric titrations**.
- **Limitations:** surface not renewed (can be poisoned or oxidised; needs cleaning); low hydrogen overpotential, so not useful at negative potentials; current less reproducible than DME.

### Amperometric titrations (application of polarography)

The applied potential is fixed at a value on the diffusion-current plateau of the analyte (or titrant), and the current is measured after each addition of titrant. The plot of current vs volume gives two straight lines meeting at the end point. Examples: lead with sulphate or dichromate, sulphate with lead, nitrite with sulphanilic acid; **biamperometric (dead-stop)** end points with two small platinum electrodes are used in diazotisation and Karl Fischer titrations.

### Applications of polarography

1. **Inorganic:** trace metals (Pb, Cd, Zn, Cu, Ni) in drugs, water, food and biological fluids; several metals in one run if their E½ differ by about 0.2 V.
2. **Organic and pharmaceutical:** compounds with reducible groups — nitro, nitroso, azo, carbonyl (aldehydes, ketones), quinones, disulphides, halogenated compounds. Examples: chloramphenicol, nitrofurantoin, metronidazole, menadione, vitamin C (oxidation), vitamin B1 and B2, steroids with conjugated ketone, chlorpromazine, penicillins (after treatment), tetracyclines.
3. **Determination of dissolved oxygen** (Clark-type electrode) and peroxides.
4. **Physicochemical studies:** stability constants and composition of complexes (shift of E½), number of electrons, reaction kinetics.
5. Detection in HPLC (electrochemical detectors).

**Remember**

- κ = G × cell constant (l/A); Λm = κ × 1000/M; AC and platinised Pt electrodes; constant temperature.
- Conductometric curves: strong/strong V shape; strong + weak acid mixture gives two breaks; weak/weak gives a clear break where indicators fail.
- Nernst: E = E° + (0.0591/n) log a; 59.1 mV per pH unit for the glass electrode.
- Reference electrodes: SHE (0.000 V), SCE (about +0.242 V), Ag/AgCl (about +0.197 V, saturated KCl).
- Indicator electrodes: metal (Ag, Pt), glass (pH); sodium error above pH 10.
- End point: inflection, peak of ΔE/ΔV, zero of Δ²E/ΔV², Gran's plot.
- Polarography: DME, supporting electrolyte removes migration current, N2 removes O2, gelatin suppresses maxima, E½ for identity, id for amount.
- Ilkovic: id = 607 n D^½ m^⅔ t^⅙ C.
- RPE for positive potentials and amperometric titrations.
