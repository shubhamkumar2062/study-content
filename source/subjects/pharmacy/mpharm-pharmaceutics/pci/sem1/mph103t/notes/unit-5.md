# Unit 5: Compression and compaction

Syllabus item 4: physics of tablet compression; compression; consolidation; effect of friction; distribution of forces; compaction profiles; solubility. Heckel and Kawakita analysis are introduced here and worked fully in Unit 6 (consolidation parameters).

## 5.1 Basic terms

| Term | Meaning |
| --- | --- |
| **Compression** | Reduction in the bulk volume of a powder (decrease in porosity) under an applied stress |
| **Consolidation** | Increase in the mechanical strength of the mass caused by particle–particle interactions (bond formation) as particles are pressed together |
| **Compaction** | Compression and consolidation of a two-phase (solid + air) system by an applied force — the overall process of making a coherent tablet |
| **Compressibility** | Ability of a powder to decrease in volume under pressure |
| **Compactibility** | Ability of a powder to form a strong compact (tablet of adequate tensile strength) at a given porosity or pressure |
| **Tabletability** | Ability to form a tablet of given strength at a given compaction pressure (tensile strength vs pressure plot) |
| **Porosity (ε)** | Fraction of tablet volume that is void: ε = 1 − (apparent density/true density) |
| **Relative density (D)** | Apparent density ÷ true density = 1 − ε |

## 5.2 Physics of tablet compression: stages

When a punch presses powder in a die, the following stages overlap:

```text
Applied pressure ↑
  1. Die filling and particle rearrangement
       particles slide past each other into a closer packing (low pressure)
  2. Particle deformation at contact points
       ├─ elastic deformation (reversible)
       ├─ plastic deformation (permanent flow, above yield stress)
       └─ brittle fracture / fragmentation (new clean surfaces, smaller particles)
  3. Bond formation (consolidation) over the new contact area
  4. Decompression: punch withdraws; elastic recovery (tablet expands axially)
  5. Ejection: lower punch pushes tablet out against die-wall friction;
     further radial expansion as tablet leaves the die
```

### Particle rearrangement

At low pressures particles move into voids. Small, irregular, cohesive particles rearrange less efficiently. The extent of rearrangement shows up as the difference between the initial packing density and the density reached at low pressure (DB in the Heckel analysis).

### Deformation behaviour

| Behaviour | What happens | Examples | Practical consequence |
| --- | --- | --- | --- |
| **Elastic** | Reversible change of shape, obeying Hooke's law (stress = E × strain) | Paracetamol (crystalline), some starches partly | Energy stored is released on decompression → breaks bonds → **capping and lamination** |
| **Plastic** | Permanent flow once stress exceeds the yield stress; large contact areas | Microcrystalline cellulose, sodium chloride, starch, many polymers | Strong tablets; **time-dependent** (strain rate sensitive) — weaker at high press speed |
| **Brittle (fragmenting)** | Particles fracture into smaller ones, creating many new clean surfaces | Dicalcium phosphate dihydrate, sucrose, lactose (partly) | Strength less sensitive to press speed and to lubricant (new lubricant-free surfaces form) |
| **Viscoelastic** | Combination of viscous flow and elastic recovery, depends on time | Many polymers, MCC | Dwell time matters; pre-compression helps |

Most materials show a mixture. **Fragmentation** creates new surfaces that are not covered by magnesium stearate, so brittle materials are **less lubricant-sensitive**; plastic materials such as MCC lose strength with over-lubrication because the lubricant film stays on the deforming surface.

### Strain-rate sensitivity (speed effect)

Plastic flow takes time. At high turret speed the **dwell time** (time the punch head flat is under the compression roller at maximum force) shortens, so plastic materials deform less and give weaker tablets or capping.

Dwell time = flat length of punch head ÷ linear speed of punch; linear speed = π × pitch-circle diameter × turret rpm/60.

**Worked example:** pitch-circle diameter 410 mm, turret 30 rpm → punch speed = π × 0.41 × 30/60 = 0.644 m/s. With a 10 mm flat on the punch head, dwell time = 0.010/0.644 = **15.5 ms**. At 60 rpm it halves to **7.8 ms** — enough to cause capping with a strongly plastic or viscoelastic blend.

**Strain-rate sensitivity (SRS)** from Heckel yield pressures measured at low and high punch speeds: SRS = (Py at high speed − Py at low speed)/Py at high speed × 100. Example: Py 90 MPa at low speed and 120 MPa at high speed → SRS = **25%**. Plastic materials show high SRS; brittle materials show low SRS.

### Practical remedies for elastic recovery and capping

Pre-compression stage, slower press speed, plastic binders or fillers (MCC, PVP), moist granulation (moisture acts as plasticiser), larger dwell time (larger punch head flats), tapered dies, optimum lubrication, lower final force (over-compression can increase capping).

## 5.3 Consolidation: how bonds form

Bonds form only when surfaces come close enough (within about the range of intermolecular forces) over a sufficient area. Mechanisms (Rumpf's classification, simplified):

1. **Solid bridges** — at contact points, high local stress and frictional heat can melt asperities, which re-solidify (**fusion bonding**); or a soluble component dissolves in adsorbed moisture or granulating liquid and recrystallises as a bridge (crystallisation, hardening on storage).
2. **Intermolecular forces** — van der Waals forces and hydrogen bonds across close contact; the dominant mechanism for most dry-compressed tablets (MCC, lactose). **Cold welding** — when clean surfaces approach to within molecular distance, they join without heat; important for metals and some brittle crystals.
3. **Mechanical interlocking** — entanglement of irregular or fibrous particles; important for fibrous materials and some cellulose grades.
4. **Liquid bridges and capillary forces** — moisture films; mainly in granules before drying and in hygroscopic tablets.
5. **Electrostatic forces** — small contribution.

**Theories of consolidation** therefore include the **cold welding theory** (surfaces in close contact bond like metals), the **fusion bonding theory** (local melting from frictional heat at asperities — local temperatures far above the bulk temperature are possible for very short times) and the dissolution–recrystallisation (solid bridge) theory.

**Factors affecting consolidation and tablet strength:** deformation mechanism, particle size (smaller particles → more contact points; for brittle materials size effect is small), moisture content (optimal level), binder type and amount, lubricant (amount and mixing time), compression force and speed, crystal form and amorphous content, temperature.

### Measuring the strength of a compact

**Diametral compression (Brazilian) test:** a cylindrical tablet is crushed across its diameter; it fails by tension along the loaded diameter. **Tensile strength (Fell and Newton):** σt = 2F/(πDt), where F = breaking force, D = diameter, t = thickness.

**Worked example:** breaking force 80 N, D = 10 mm, t = 4 mm: σt = 2 × 80 / (π × 10 × 4) = **1.27 MPa** (N/mm²). Tensile strength, unlike "hardness" in kg, allows tablets of different sizes to be compared; about 1.7 MPa or more is often targeted for tablets that must withstand coating and packing, though values around 1 MPa may be acceptable for some products.

**Porosity worked example:** a 400 mg tablet of D = 10 mm, t = 4 mm has volume π × 5² × 4 = 314.2 mm³ = 0.3142 cm³; apparent density = 0.400/0.3142 = 1.273 g/cm³. With true density 1.50 g/cm³ (helium pycnometer): relative density = 0.849, porosity = **15.1%**.

**Tabletability, compressibility and compactibility (TCC) profiles:** tensile strength vs pressure (tabletability), porosity vs pressure (compressibility), tensile strength vs porosity (compactibility). Together they show whether a weak tablet comes from too little densification or from poor bonding.

## 5.4 Effect of friction

Friction acts at two levels:

1. **Interparticulate friction** — resists rearrangement and sliding of particles; reduced by **glidants** (colloidal silicon dioxide, talc), which improve flow and die filling.
2. **Die-wall friction** — between the powder and the die wall; it absorbs part of the applied force, causes uneven density, raises ejection force and causes sticking, scoring and capping; reduced by **lubricants**.

**Lubricant types:**

| Type | Mechanism | Examples |
| --- | --- | --- |
| Boundary lubricants | Adhere to metal and particle surfaces as a thin film with low shear strength | Magnesium stearate, calcium stearate, sodium stearyl fumarate |
| Fluid (hydrodynamic) lubricants | Melt or flow under pressure to form a liquid film | Stearic acid, hydrogenated vegetable oils, PEG 4000/6000 (water-soluble) |

**Over-lubrication** (too much magnesium stearate or too long mixing) coats particles with a hydrophobic film: weaker bonding (especially plastic materials), slower disintegration and dissolution.

### Measures of friction from an instrumented press

- **Force transmission ratio R = FL/FU** (lower punch force ÷ upper punch force). R = 1 means no die-wall loss. Unlubricated granules may give R well below 0.8; well-lubricated ones 0.9 or more.
- **Die-wall force (FD):** in single-ended (upper punch) compression, FD = FU − FL.
- **Ejection force:** peak force needed to push the tablet out; rises with die-wall friction, tablet thickness and residual radial pressure.
- **Coefficient of die-wall friction (µ)** = die-wall shear force ÷ radial die-wall force.

**Worked example:** upper punch 10.0 kN, lower punch 8.5 kN → R = 0.85, force lost to the die wall FD = 1.5 kN, mean compaction force FM = (FU + FL)/2 = 9.25 kN (often used as the "effective" force).

## 5.5 Distribution of forces

In an eccentric (single-punch) press only the upper punch moves; in a rotary press both punches move towards each other between pressure rollers. Either way:

**Axial force balance (single-ended compression):** FA = FL + FD — the applied (upper) force equals the force reaching the lower punch plus the force lost to the die wall.

**Radial force:** as the powder is pressed axially, it pushes outward on the die wall (radial stress σr). The ratio of radial to axial stress (K) depends on the material: a liquid would transmit pressure equally (K = 1); a rigid solid would not transmit sideways at all. Radial die-wall pressure that remains after the upper punch is removed (**residual radial pressure**) must be overcome on ejection.

**Exponential loss of axial force with depth (Shaxby–Evans/Janssen type relation):** FL = FA × e^(−4µKH/D), where µ = die-wall friction coefficient, K = radial-to-axial stress ratio, H = compact height, D = diameter. So force loss increases with friction and with the height-to-diameter ratio. Example: µ = 0.3, K = 0.4, H/D = 0.4 → FL/FA = e^(−0.192) = **0.83**. This is why tall tablets and poorly lubricated blends are harder to make uniform.

**Density distribution within the tablet:** studies with coloured layers and later X-ray tomography show the compact is not uniform. In single-ended compression, regions of high density form near the upper punch edges (where die-wall friction concentrates stress) and lower density near the lower centre; in double-ended (rotary) compression the pattern is more symmetric. Uneven density leads to uneven strength, capping at weak planes, and variation in dissolution.

**Stress during ejection:** as the tablet leaves the die, the sudden release of radial pressure lets it expand; weak planes may fail (lamination). Tapered dies allow gradual release.

## 5.6 Compaction profiles

**Instrumented tablet presses** record force and displacement during compression:

- **Force:** strain gauges bonded to the punch holders, eye-bolt or compression rollers (Wheatstone bridge circuit) or piezoelectric transducers.
- **Displacement:** linear variable differential transformers (LVDT) or linear encoders on the punches; corrected for punch and machine deformation.
- **Die-wall force:** strain gauges on an instrumented die.
- **Compaction simulators:** single-station machines that reproduce the punch movement of any production press at real speeds using small quantities of material — very useful early in development and for scale-up.

### Main profiles

**1. Force–time profile**

```text
Force ↑          ____  dwell (rotary: flat on punch head under the roller)
     |         /    \
     |        /      \
     |  ____/        \______
     +------------------------→ time
       consolidation time | dwell | decompression
```

Gives peak force, contact time, dwell time, rate of loading and unloading. Rotary presses show a short dwell plateau; eccentric presses a sharp peak. Comparing upper and lower punch traces shows friction (R value). In plastic materials the peak of the lower punch can lag behind the upper (stress relaxation during dwell).

**2. Force–displacement profile (work of compaction)**

```text
Force ↑         A ●
     |         /|
     |        / |   area under rising curve = gross work of compaction
     |       /  |   area under falling curve = elastic (recovered) work
     |      /   |
     |  ___/____|___→ upper punch displacement
```

- Gross (total) work = area under the loading curve.
- Elastic work (E3) = area under the unloading curve (energy returned).
- Net work of compaction = gross work − elastic work — energy used for plastic deformation, fragmentation and bonding (with a small part lost to friction, E1, measured by comparison with a lubricated die run).
- **Plasticity factor (Stamm and Mathis):** PF = E2/(E2 + E3) × 100, where E2 = net work of compaction. Example: net work 4.2 J, elastic work 0.6 J → PF = 4.2/4.8 × 100 = **87.5%** (a mainly plastic material).

**3. Radial (die-wall) force vs axial force profile** — a hysteresis loop during loading and unloading; the residual radial force at zero axial force predicts ejection difficulty; the slope of the loading line relates to the Poisson ratio of the material.

**4. Porosity (or relative density)–pressure profiles** — Heckel plot (ln[1/(1 − D)] vs P) and Kawakita plot (P/C vs P) — used to classify materials (plastic vs fragmenting) and to obtain yield pressure. Worked in Unit 6.

**5. Ejection profile** — ejection force vs time or displacement; high peaks indicate need for more lubricant or a sticking tendency.

**6. Elastic recovery (axial):** ER% = (t_after − t_min)/t_min × 100, where t_min is the minimum compact thickness under load and t_after the thickness after ejection. Example: 3.70 mm under load, 3.92 mm after ejection → ER = **5.9%**. High values warn of capping.

### Uses of compaction profiles

- Classify excipients and API by deformation mechanism; choose fillers to balance plastic and brittle behaviour.
- Select process: direct compression versus granulation.
- Set compression force and speed; predict capping and lamination.
- Scale-up from R&D (single-station) to production rotary presses using matched dwell times on a compaction simulator.
- Monitor production (force control loops reject tablets of wrong weight, since weight is proportional to compression force at constant thickness).

## 5.7 Solubility in compression and compaction

The syllabus lists solubility under this heading because solubility of the drug and excipients affects both how a tablet is made and how it performs:

1. **Bonding:** soluble components (sugars, sodium chloride, lactose) can dissolve in surface moisture and recrystallise as **solid bridges**, so hardness of such tablets may rise during storage (post-compression hardening).
2. **Choice of filler and disintegration mechanism:** soluble fillers (lactose, mannitol, sucrose) dissolve and erode; insoluble fillers (dicalcium phosphate, MCC) need disintegrants to break the tablet. A poorly soluble drug in a soluble filler dissolves faster after disintegration because the filler creates a hydrophilic micro-environment.
3. **Compaction-induced change of solid form:** pressure and frictional heat can convert polymorphs, form amorphous regions or dehydrate hydrates; the new form may have a different solubility and dissolution rate.
4. **Dissolution of the compact:** higher compression force lowers porosity and slows water penetration — dissolution slows; but very high force may fracture granules and expose new surface, so the effect can be non-linear. Water-soluble lubricants (PEG, sodium lauryl sulphate in small amounts, sodium stearyl fumarate is less hydrophobic than magnesium stearate) reduce the delay.
5. **Wet granulation:** solubility of drug in the granulating liquid decides whether drug migrates during drying (soluble drug moves with evaporating solvent to granule surfaces → content non-uniformity) and whether solid bridges form.
6. **Solubility-limited bioavailability (BCS II):** compaction parameters must not reduce the dissolution rate so much that bioequivalence fails; dissolution is therefore a CQA linked to compaction CPPs in QbD.

## Remember

- Compression = volume reduction; consolidation = strength increase; compaction = both.
- Stages: rearrangement → elastic/plastic/brittle deformation → bonding → decompression (elastic recovery) → ejection.
- Plastic (MCC, NaCl) — strong but speed-sensitive and lubricant-sensitive; brittle (DCP, sucrose) — insensitive to speed and lubricant; elastic (paracetamol) — capping.
- Bonding: solid bridges (fusion, recrystallisation), intermolecular forces/cold welding, mechanical interlocking.
- Tensile strength σ = 2F/(πDt): 80 N, 10 × 4 mm → 1.27 MPa. Porosity example 15.1%.
- R = FL/FU; FA = FL + FD; FL = FA·e^(−4µKH/D) → loss grows with friction and H/D.
- Dwell time = punch flat ÷ punch speed: 15.5 ms at 30 rpm, 7.8 ms at 60 rpm (410 mm PCD, 10 mm flat).
- Profiles: force–time, force–displacement (net work, plasticity factor), radial vs axial, Heckel/Kawakita, ejection, elastic recovery.
