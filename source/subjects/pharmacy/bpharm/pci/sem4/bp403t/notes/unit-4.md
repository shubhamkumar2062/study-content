# Unit 4: Micromeritics

**Micromeritics** is the science and technology of small particles. Most drugs and excipients are handled as powders, and the size, shape, surface area and packing of the particles decide how they dissolve, flow, mix, compress and are absorbed. The unit of particle size is the **micrometre (µm)**, 1 µm = 10⁻⁶ m = 10⁻⁴ cm (once called the micron).

## 4.1 Why particle size matters in pharmacy

| Property affected | Example |
| --- | --- |
| Dissolution and absorption | Smaller particles have more surface and dissolve faster (Noyes–Whitney). Micronised griseofulvin and digoxin give better absorption |
| Physical stability | Settling of suspensions and creaming of emulsions depend on size (Stokes) |
| Flow of powders | Fine powders are cohesive and flow poorly; granules flow well |
| Content uniformity | Low-dose drugs need fine, uniform particles to mix evenly |
| Lung deposition | Inhaled particles of about 1–5 µm reach the lower airways |
| Injections and eye preparations | Large particles cause pain, irritation or blockage of needles |
| Taste, texture, colour | Fine particles give smooth (not gritty) creams and suspensions |

## 4.2 Particle size: expressing the size of irregular particles

A sphere has one exact size, its diameter. Real particles are irregular, so their size is expressed as the diameter of an **equivalent sphere** that has the same property.

| Diameter | Definition | Measured by |
| --- | --- | --- |
| Surface diameter (ds) | Sphere with the same surface area | Adsorption, permeability |
| Volume diameter (dv) | Sphere with the same volume | Coulter counter |
| Projected diameter (dp) | Circle with the same area as the particle image seen in its most stable position | Microscope |
| Stokes diameter (dst) | Sphere that settles at the same rate in the same fluid | Sedimentation |
| Sieve diameter | Width of the smallest square aperture the particle passes through | Sieving |

In microscopy two statistical diameters are also used:

- **Feret's diameter:** the distance between two parallel tangents on opposite sides of the image, drawn in a fixed direction.
- **Martin's diameter:** the length of the line, drawn in a fixed direction, that divides the image into two equal areas.

```text
     Feret's diameter               Martin's diameter
   |    ____     |                       ____
   |   /    \__  |                      /    \__
   |  |        | |                -----|--------|----- (halves the area)
   |   \_____ /  |                      \_____ /
   |<-- d_F --->|                  
 (tangents parallel to a fixed      (line in the fixed direction that
  direction, e.g. the eyepiece scale) divides the image into 2 equal parts)
```

## 4.3 Particle size distribution

A powder contains particles of many sizes. The **distribution** is described by counting (or weighing) the particles in each size class.

- A **frequency distribution curve** plots the number (or weight) of particles in each class against size; it shows the mode.
- A **cumulative curve** plots the percentage larger (or smaller) than each size; it is S-shaped, and the **median** (50% size) is read directly from it.
- Many powders give a skewed frequency curve that becomes a normal (bell) curve when size is plotted on a log scale: a **log-normal distribution**. On log-probability paper, this gives a straight line. Two values describe it:
  - **Geometric mean diameter (dg):** the size at the 50% point (the median of the log-normal curve).
  - **Geometric standard deviation (σg):** size at 84.13% ÷ size at 50% (or 50% ÷ 15.87%). σg = 1 means all particles are the same size (monodisperse).

### Number and weight distribution

A distribution may be based on the **number** of particles in each class (from microscopy or a Coulter counter) or on the **weight** in each class (from sieving or sedimentation). The two look very different for the same powder: a few large particles carry most of the weight but are few in number. A weight distribution is shifted toward larger sizes. For a log-normal powder, the two can be interconverted with the Hatch–Choate equations, since both have the same σg.

## 4.4 Mean particle size

Different averages are used for different purposes. Edmundson's general equation:

d(mean) = [Σ n d^(p+f) / Σ n d^f]^(1/p)

where n = number of particles in a class of mean size d, p = an index related to size (1 = length, 2 = surface, 3 = volume), and f = a frequency index (0 = number, 1 = length, 2 = surface, 3 = volume or weight).

| Mean diameter | Formula | Remarks |
| --- | --- | --- |
| Length–number mean, dln | Σnd / Σn | The ordinary arithmetic mean |
| Surface–number mean, dsn | √(Σnd² / Σn) | Mean surface per particle |
| Volume–number mean, dvn | ∛(Σnd³ / Σn) | Mean volume per particle; used to count particles per gram |
| Surface–length mean, dsl | Σnd² / Σnd | |
| Volume–surface mean, dvs | Σnd³ / Σnd² | Linked to specific surface; important for dissolution and adsorption |
| Weight–moment mean, dwm | Σnd⁴ / Σnd³ | Weight-based mean (from sieving or sedimentation data) |

**Worked example.** 500 particles were counted by microscopy:

| Mean size d (µm) | n | nd | nd² | nd³ |
| --- | --- | --- | --- | --- |
| 5 | 40 | 200 | 1,000 | 5,000 |
| 15 | 120 | 1,800 | 27,000 | 405,000 |
| 25 | 180 | 4,500 | 112,500 | 2,812,500 |
| 35 | 100 | 3,500 | 122,500 | 4,287,500 |
| 45 | 60 | 2,700 | 121,500 | 5,467,500 |
| Total | 500 | 12,700 | 384,500 | 12,977,500 |

dln = 12,700/500 = **25.4 µm**; dsn = √(384,500/500) = √769 = **27.7 µm**; dvn = ∛(12,977,500/500) = ∛25,955 = **29.6 µm**; dvs = 12,977,500/384,500 = **33.8 µm**. Note the order: the more the mean weights large particles, the larger it is.

## 4.5 Number of particles per unit weight

If particles are taken as spheres of diameter dvn and density ρ, the volume of one particle is πdvn³/6 and its mass is πdvn³ρ/6. The number of particles per gram is:

N = 6 / (π dvn³ ρ)

**Worked example.** dvn = 10 µm = 10⁻³ cm, ρ = 1.5 g/cm³. N = 6/(3.1416 × 10⁻⁹ × 1.5) = 6/(4.712 × 10⁻⁹) = **1.27 × 10⁹ particles per gram**.

## 4.6 Methods of determining particle size

| Method | Approximate range | Size type | Distribution |
| --- | --- | --- | --- |
| Optical microscopy | About 0.2–100 µm | Projected diameter | Number |
| Electron microscopy | Down to about 0.001 µm | Projected diameter | Number |
| Sieving | Above about 40–50 µm | Sieve diameter | Weight |
| Sedimentation (Andreasen pipette, balance) | About 1–200 µm | Stokes diameter | Weight |
| Coulter counter (electrical sensing zone) | About 0.5–500 µm | Volume diameter | Number |
| Laser light diffraction / scattering | Sub-micrometre to millimetre | Volume-equivalent | Volume |

### Microscopic method (counting method)

1. A dilute dispersion of the powder in a liquid in which it does not dissolve is placed on a slide.
2. The **eyepiece micrometer** (a scale in the eyepiece, in arbitrary divisions) is first **calibrated** against a **stage micrometer** (a slide engraved with a scale whose divisions are of known size, commonly 0.01 mm = 10 µm).
3. The particles are sized against the eyepiece scale along a fixed direction, and the number in each size class is recorded. Enough particles must be counted (usually 300–500 or more) for a reliable distribution.

**Advantages:** particles are seen directly, so shape, aggregates and contaminants are noticed; little sample needed. **Disadvantages:** slow and tiring; only two dimensions are measured (thickness is not); a small sample may not represent the batch; operator bias.

### Sieving (separation method)

A stack of standard sieves is arranged with the largest aperture at the top and a receiving pan at the bottom. A weighed sample is placed on the top sieve and shaken mechanically for a fixed time (often 10–20 minutes). The weight retained on each sieve is recorded and the **weight distribution** calculated. Sieves are described by aperture size (µm) and by sieve numbers given in the pharmacopoeia.

**Advantages:** simple, cheap, handles large samples, gives weight distribution directly. **Disadvantages:** not useful for fine powders below about 40–50 µm; cohesive particles clump; shaking time and load affect results; elongated particles may pass end-on; attrition breaks fragile particles.

### Sedimentation (Andreasen pipette)

A suspension of known concentration (usually 1–2% solids) is placed in the Andreasen cylinder, with a pipette whose tip is at a known depth h. At set times, 10 ml samples are withdrawn from depth h, dried and weighed. At time t, all particles larger than the Stokes diameter d have settled below the pipette tip, where:

d = √[18 η h / ((ρs − ρ0) g t)]

The weight in each sample, as a fraction of the original concentration, gives the cumulative weight percent undersize for that d. The **sedimentation balance** method instead records the weight of sediment collecting on a pan with time.

### Coulter counter (electrical sensing zone)

Particles suspended in an electrolyte flow through a small orifice between two electrodes. Each particle displaces its own volume of electrolyte and causes a momentary change in resistance (a voltage pulse) proportional to its **volume**. The pulses are counted and sorted by size, giving a number distribution quickly (thousands of particles per second).

### Other separation methods

- **Elutriation:** an upward stream of liquid or air carries away particles smaller than a given size.
- **Centrifugal and cyclone separation:** for finer particles.

## 4.7 Particle shape

Shape affects flow, packing, surface area and compression. Shapes are described as spherical, cubical, acicular (needle), flaky, granular, irregular and so on. They are quantified with **shape factors**:

Surface area S = αs dp²  and  Volume V = αv dp³

where dp is the projected diameter, αs = surface area shape factor and αv = volume shape factor. For a sphere, αs = π and αv = π/6, so **αs/αv = 6**. The more αs/αv exceeds 6, the more the particle departs from a sphere.

## 4.8 Specific surface

**Specific surface** is the surface area per unit volume (Sv) or per unit weight (Sw).

Sv = (surface of all particles)/(volume of all particles) = αs/(αv dvs)

Sw = Sv / ρ = αs / (ρ αv dvs)

For spheres (αs/αv = 6): **Sw = 6 / (ρ dvs)**

**Worked example.** Spherical particles with dvs = 10 µm (10⁻³ cm) and true density 2.0 g/cm³: Sw = 6/(2.0 × 10⁻³) = **3,000 cm²/g (0.3 m²/g)**. If the size is reduced tenfold to 1 µm, Sw rises tenfold to 30,000 cm²/g.

## 4.9 Methods of determining surface area

### Adsorption method

The amount of gas (usually **nitrogen**, at its boiling point, −196 °C) adsorbed as a single layer (monolayer) on the powder surface is found. Since each nitrogen molecule covers a known area (about 16.2 Å²), the monolayer volume gives the surface area. The **BET (Brunauer, Emmett and Teller)** equation is used:

p / [y(p0 − p)] = 1/(ym b) + [(b − 1)/(ym b)] × (p/p0)

where y = volume of gas adsorbed per gram at pressure p, p0 = saturation vapour pressure, ym = volume for a complete monolayer, and b = a constant related to the heat of adsorption. A plot of p/[y(p0 − p)] against p/p0 is linear (usually for p/p0 roughly 0.05–0.3); ym = 1/(slope + intercept). Instruments such as the Quantasorb measure this by gas flow. Adsorption measures the **total surface including pores and cracks**.

### Air permeability method

The resistance to the flow of air (or a liquid) through a packed bed of powder depends on the surface area of the particles: finer powders (greater surface) resist flow more. The **Kozeny–Carman equation** relates them:

Sw = (14/ρ) √[ A ΔP t ε³ / (η L V (1 − ε)²) ]

where ρ = particle density, A = cross-sectional area of the bed, ΔP = pressure drop, t = time for volume V of air to flow, ε = porosity of the bed, η = viscosity of air, L = length of the bed. Commercial instruments (Fisher subsieve sizer, Blaine apparatus) use this principle. Permeability measures only the **external surface** through which air flows, so it gives lower values than gas adsorption for porous powders.

## 4.10 Derived properties of powders

### Porosity

**Porosity (ε)** is the fraction of the bulk volume of a powder bed that is void space:

ε = (Vb − Vp)/Vb = 1 − Vp/Vb

where Vb = bulk volume and Vp = true volume of the particles. In terms of densities, **ε = 1 − ρbulk/ρtrue**. It is often given as a percentage.

### Packing arrangements

```text
 Open (cubic) packing                 Closest (rhombohedral) packing
   O O O O                               O O O O
   O O O O    each sphere sits            O O O    spheres sit in the
   O O O O    directly above another     O O O O   hollows of the layer below
 porosity about 48%                     porosity about 26%
```

For uniform spheres, porosity ranges theoretically from about **26% (closest, rhombohedral packing)** to about **48% (open, cubic packing)**. Real powders, with irregular shapes and cohesive fines, often have higher porosities. Packing changes on tapping, vibration and compression.

### Densities

| Density | Volume used | How measured |
| --- | --- | --- |
| True density (ρt) | Volume of the solid alone, excluding all pores and voids | Helium pycnometer (helium penetrates the finest pores) or liquid displacement in a specific gravity bottle using a liquid in which the solid is insoluble |
| Granule density (ρg) | Volume of granules including their internal pores, excluding spaces between granules | Mercury displacement (mercury fills spaces between granules but not small pores) |
| Bulk density (ρb) | Total volume of the bed, including voids between particles | Weighed powder poured gently into a graduated cylinder; volume read |
| Tapped density | Volume after mechanical tapping to a constant volume | Tap density tester |

**Bulkiness** = 1/bulk density (specific bulk volume). It rises as particle size falls, because fine particles pack loosely with many voids. It matters in choosing the size of capsules and containers and in packaging of powders.

**Worked example.** 25 g of powder occupies 40 ml when poured and 33 ml after tapping. True density = 1.536 g/ml.
Bulk density = 25/40 = 0.625 g/ml; tapped density = 25/33 = 0.758 g/ml; bulkiness = 1/0.625 = 1.6 ml/g.
Porosity (poured) = 1 − 0.625/1.536 = 0.593 = **59.3%**.

## 4.11 Flow properties

Good flow is needed for uniform die filling in tablet presses and capsule fillers, and so for uniform weight and content. Flow is reduced by small size (below about 100 µm powders become cohesive), irregular shape, rough surfaces, moisture and electrostatic charge.

### Angle of repose

Powder is allowed to flow through a funnel held at a fixed height onto a flat surface until the cone reaches the funnel tip (fixed funnel method). The **angle of repose (θ)** is the maximum angle between the surface of the cone and the horizontal:

tan θ = h / r

where h = height and r = radius of the base of the cone. A lower angle means better flow.

### Compressibility (Carr's) index and Hausner ratio

Carr's index = (tapped density − bulk density) / tapped density × 100

Hausner ratio = tapped density / bulk density

Free-flowing powders pack little on tapping, so their two densities are close.

**Scale of flowability (as used in the US Pharmacopeia; check the scale used in your college)**

| Flow | Angle of repose (°) | Carr's index (%) | Hausner ratio |
| --- | --- | --- | --- |
| Excellent | 25–30 | ≤10 | 1.00–1.11 |
| Good | 31–35 | 11–15 | 1.12–1.18 |
| Fair | 36–40 | 16–20 | 1.19–1.25 |
| Passable | 41–45 | 21–25 | 1.26–1.34 |
| Poor | 46–55 | 26–31 | 1.35–1.45 |
| Very poor | 56–65 | 32–37 | 1.46–1.59 |
| Very, very poor | >66 | >38 | >1.60 |

**Worked example (continued).** Carr's index = (0.758 − 0.625)/0.758 × 100 = **17.5%** (fair); Hausner ratio = 0.758/0.625 = **1.21** (fair). A cone 2.4 cm high with a 4.0 cm base radius gives tan θ = 0.6, θ = **31°** (good).

Other flow tests: flow rate through an orifice (g/s), shear cell measurements.

### Improving flow

1. **Granulation** (larger, more spherical particles).
2. **Glidants:** colloidal silicon dioxide, talc, magnesium stearate in small amounts; they coat particles, reduce friction and separate cohesive particles. Too much of a lubricant such as magnesium stearate may reduce flow again.
3. Removing fines; changing shape (spray drying gives spheres).
4. Drying to reduce moisture; controlling static charge.
5. Mechanical aids: vibrating hoppers, forced feeders.

## Remember

- 1 µm = 10⁻⁴ cm; size expressed as equivalent sphere diameters (ds, dv, dp, dst); Feret's and Martin's diameters in microscopy.
- Log-normal distribution: dg (50%) and σg (84.13%/50%).
- Edmundson means: dln = Σnd/Σn, dvs = Σnd³/Σnd², dwm = Σnd⁴/Σnd³.
- Particles per gram N = 6/(πdvn³ρ); for spheres Sw = 6/(ρdvs).
- Methods: microscope 0.2–100 µm (number), sieving above ~40 µm (weight), Andreasen d = √[18ηh/((ρs − ρ0)gt)], Coulter counter (volume).
- Surface area: BET gas adsorption (total, including pores), Kozeny–Carman permeability (external surface).
- Porosity ε = 1 − ρbulk/ρtrue; uniform spheres 26% (closest) to 48% (open).
- Densities: true (helium), granule (mercury), bulk, tapped; bulkiness = 1/bulk density.
- Flow: tan θ = h/r; Carr's index and Hausner ratio; improve with granulation and glidants.
