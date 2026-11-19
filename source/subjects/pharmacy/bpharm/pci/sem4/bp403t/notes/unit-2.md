# Unit 2: Rheology and deformation of solids

**Rheology** (Greek *rheo*, to flow) is the study of the flow of liquids and the deformation of solids. In pharmacy it decides whether a syrup pours, whether a suspension stays suspended on the shelf yet pours after shaking, whether an ointment spreads on the skin, whether an injection passes through a needle, and how powders compress into tablets. It also matters in manufacturing: mixing, pumping, filling and milling all depend on flow behaviour.

**Where rheology matters**

| Area | Examples |
| --- | --- |
| Liquids | Mixing, flow through pipes and filling machines, pouring, syringeability of injections |
| Semisolids | Spreading and adhesion of ointments and creams, extrusion from tubes, "feel" on the skin |
| Disperse systems | Physical stability of suspensions and emulsions, redispersion after shaking |
| Solids | Compression of powders into tablets, capping and lamination |
| Biology | Flow of blood, mucus and synovial fluid; release of drug from a base |

## 2.1 Newtonian systems and the law of flow

Picture a liquid as a stack of parallel layers (like a pack of cards). When the top layer is pushed with a force, it slides fastest and each lower layer moves a little slower.

```text
  F (force) -->  =====================  top layer, velocity v + dv
                 ---------------------
                 ---------------------   dr = distance between layers
                 ---------------------
                 =====================  bottom layer fixed (v = 0)
```

- **Shear stress (F)** = force per unit area, F′/A (dyne/cm²).
- **Rate of shear (G)** = difference in velocity between two layers divided by the distance between them, dv/dr (units: s⁻¹).

**Newton's law of flow:** for simple liquids, the rate of shear is directly proportional to the shearing stress:

F′/A = η (dv/dr), or F = ηG

The constant **η is the viscosity**: the resistance of a liquid to flow. A plot of G (y-axis) against F (x-axis), called a **rheogram**, is a straight line through the origin, with slope = 1/η (the **fluidity**, φ).

**Units of viscosity**

| Unit | Definition |
| --- | --- |
| Poise (P) | dyne s cm⁻² = g cm⁻¹ s⁻¹ (CGS) |
| Centipoise (cP) | 0.01 poise; water at 20 °C is about 1 cP |
| Pascal second (Pa s) | SI unit; 1 Pa s = 10 P; 1 mPa s = 1 cP |

Liquids that obey Newton's law are **Newtonian**: water, simple organic liquids (ethanol, chloroform), dilute true solutions, castor oil, glycerin and very dilute suspensions. Their viscosity does not depend on the rate of shear, so **one measurement** at one shear rate fully describes them.

### Kinematic viscosity

**Kinematic viscosity = absolute viscosity / density = η/ρ**

Its CGS unit is the **stokes (S)** (cm² s⁻¹); the centistoke (cS) is 0.01 stokes. Kinematic viscosity is what capillary viscometers actually measure, because the liquid flows under its own weight (which depends on density).

### Relative and specific viscosity

| Term | Formula | Use |
| --- | --- | --- |
| Relative viscosity | ηrel = η/η0 (η0 = solvent) | Comparing a solution with its solvent |
| Specific viscosity | ηsp = ηrel − 1 | Increase caused by the solute |
| Reduced viscosity | ηsp/c | Per unit concentration |
| Intrinsic viscosity | [η] = limit of ηsp/c as c → 0 | Molecular weight and shape of polymers (Mark–Houwink [η] = KMᵃ) |

## 2.2 Effect of temperature on viscosity

The viscosity of a **liquid falls** as temperature rises; the viscosity of a **gas rises** with temperature. In a liquid, heating gives molecules more energy to overcome the attraction of their neighbours, so the layers slip past each other more easily. The relation is an Arrhenius-type equation:

η = A e^(Ev/RT)

where A = a constant for the liquid, Ev = activation energy for flow, R = gas constant, T = absolute temperature. A plot of log η against 1/T is linear. Practical meaning: viscosity must always be reported **with the temperature**, and viscometers are used in a thermostatic bath (usually ±0.1 °C); a syrup or ointment may be much thinner in a hot climate than when tested in the laboratory.

## 2.3 Non-Newtonian systems

Most pharmaceutical dispersions (suspensions, emulsions, gels, ointments, creams) do **not** obey Newton's law: their apparent viscosity changes with the rate of shear. A single-point measurement is meaningless; the whole rheogram must be measured with a **multipoint** (rotational) viscometer.

```text
  Rate of shear G
      ^                     / Newtonian (straight, through origin)
      |    pseudoplastic  /  .
      |       (curves up) / .   plastic (straight after yield value f)
      |              / . /
      |           / . /      ___ dilatant (curves toward stress axis)
      |        / . /     __/
      |     / . /    ___/
      |  / . /  ___/
      +--------|--------------------> Shearing stress F
               f = yield value
```

### Plastic flow (Bingham bodies)

The rheogram is a straight line that **does not pass through the origin**; it meets the stress axis at the **yield value (f)**. Below the yield value the material behaves as an elastic solid and does not flow. Above it, it flows like a Newtonian liquid. The slope of the straight part gives the **mobility**; its reciprocal is the **plastic viscosity U**:

U = (F − f) / G

**Cause:** flocculated particles in concentrated suspensions form a loose continuous network that must be broken (by the yield stress) before flow starts. **Examples:** concentrated flocculated suspensions, ointments, pastes, some creams. A yield value helps keep particles suspended and ointments in place on the skin.

### Pseudoplastic flow (shear thinning)

The rheogram is a curve passing **through the origin**; viscosity **falls** as shear rate rises. **Cause:** long-chain polymer molecules in solution are tangled and randomly coiled at rest; when sheared they uncoil and line up in the direction of flow, and they release some immobilised solvent. Both effects lower the resistance. **Examples:** solutions of natural and synthetic gums: tragacanth, sodium alginate, methylcellulose, sodium carboxymethylcellulose.

There is no yield value, so there is no single viscosity. The **exponential (power) equation** describes the flow:

F^N = η′G, or log G = N log F − log η′

where η′ is a viscosity coefficient. For pseudoplastic systems **N > 1**; the more N exceeds 1, the more pseudoplastic the material. For Newtonian liquids N = 1.

### Dilatant flow (shear thickening)

The opposite of pseudoplastic: viscosity **rises** as shear rate rises, and the volume appears to increase when stirred. The rheogram passes through the origin and curves toward the stress axis; **N < 1** in the power equation.

**Cause:** in a concentrated **deflocculated** suspension (roughly 50% or more of small particles), particles at rest are closely packed with minimum voids, and just enough liquid fills the voids to lubricate them. When sheared, the particles take an open packing; the larger voids are not filled by the available liquid, so the particles rub against each other and resistance rises sharply. **Examples:** concentrated deflocculated suspensions such as starch in water. **Practical problem:** dilatant materials can jam mills and granulators during wet massing, so processing equipment must be chosen with care.

### Comparison

| Type | Rheogram | Yield value | Viscosity vs shear rate | Examples |
| --- | --- | --- | --- | --- |
| Newtonian | Straight through origin | No | Constant | Water, glycerin, simple syrups |
| Plastic | Straight, cuts stress axis | Yes | Constant plastic viscosity above f | Flocculated suspensions, ointments |
| Pseudoplastic | Curve through origin | No | Decreases | Gum and cellulose polymer solutions |
| Dilatant | Curve through origin, toward stress axis | No | Increases | Concentrated deflocculated suspensions |

## 2.4 Thixotropy

**Thixotropy** is an **isothermal, comparatively slow recovery, on standing, of a consistency lost through shearing**. It is seen in shear-thinning systems (plastic and pseudoplastic).

When the shear rate is increased step by step and then decreased, the **down-curve does not retrace the up-curve**. For thixotropic systems the down-curve lies to the left of the up-curve (lower viscosity at every shear rate), producing a **hysteresis loop**.

```text
  G ^          up-curve and down-curve of a thixotropic material
    |           ___ top point
    |         /  /
    |       / ./      down-curve (to the LEFT: structure broken)
    |     / ./
    |   / ./  <- area of this loop = measure of thixotropic breakdown
    | / ./        up-curve (to the right)
    +--------------------> F
```

**Mechanism:** a gel-like structure (the "card-house" network of flocculated particles, or entangled polymer chains) is broken down by shearing. When shearing stops, Brownian motion slowly rebuilds it, but not instantly, so the material stays thin for some time.

**Measuring thixotropy**

1. **Area of the hysteresis loop:** larger area = more structural breakdown.
2. **Thixotropic coefficient of breakdown (B):** the fall in plastic viscosity per unit increase in shear rate (from loops run to two different top shear rates).
3. **M:** the fall in viscosity with time at a constant shear rate.

**Related terms**

- **Negative thixotropy (antithixotropy):** consistency **increases** on shearing and falls on standing; the down-curve lies to the right of the up-curve. Example: magnesia magma at certain shear rates.
- **Rheopexy:** a sol forms a gel **more quickly** when gently shaken or rolled than when left alone. Example: some bentonite dispersions.

### Thixotropy in formulation

| Product | Why thixotropy helps |
| --- | --- |
| Suspensions | High consistency at rest keeps particles suspended and stops caking; shaking thins them so the dose pours easily, and the structure re-forms before particles settle |
| Emulsions | High viscosity at rest slows creaming |
| Injectable suspensions | Thin when forced through the needle, then set again as a depot at the site; for example, concentrated procaine penicillin G suspensions for intramuscular use |
| Ointments, creams, gels | Spread easily when rubbed but stay in place on the skin and in the tube |

Too much thixotropy is undesirable: the product may not thin on shaking, or may not recover its structure in time. Thixotropy can also change on storage (as particles age), so it is an important stability test.

## 2.5 Determination of viscosity

Viscometers are of two kinds:

- **Single-point instruments** work at only one rate of shear. They are suitable only for **Newtonian** liquids: capillary viscometers and falling-sphere viscometers.
- **Multipoint instruments** can vary the rate of shear and give the full rheogram. They are needed for **non-Newtonian** systems and also work for Newtonian ones: rotational viscometers (cup-and-bob, cone-and-plate).

### Capillary (Ostwald) viscometer

```text
       (A)  upper mark  ---o---
           bulb          (   )
       (B)  lower mark  ---o---
                           |  capillary
                           |
                     ______|______
                    (  lower bulb  )   liquid is drawn up past mark A
                    (______________)   and the time to flow from A to B
                                       is measured
```

The time for a fixed volume of liquid to flow through the capillary under its own weight is measured. It is based on **Poiseuille's law**:

η = πr⁴tΔP / (8lV)

where r = capillary radius, t = time, ΔP = pressure head, l = capillary length, V = volume of liquid. For one instrument, r, l and V are constant, and ΔP depends on the density of the liquid. Comparing an unknown (1) with a reference liquid (2), usually water:

η1/η2 = ρ1t1 / (ρ2t2)

**Worked example.** At 25 °C water (ρ = 0.997 g/ml, η = 0.890 cP) flows in 100 s. A syrup (ρ = 1.10 g/ml) takes 150 s. η = 0.890 × (1.10 × 150)/(0.997 × 100) = 0.890 × 1.655 = **1.47 cP**.

The **Ubbelohde (suspended-level) viscometer** is a modified capillary viscometer in which the result does not depend on the volume of liquid charged; it is used in pharmacopoeial tests.

### Falling-sphere (Hoeppler) viscometer

A glass or steel ball rolls down a tilted glass tube filled with the liquid, at constant temperature. The time t for the ball to fall between two marks is measured. Based on Stokes's law:

η = t (Sb − Sf) B

where Sb = specific gravity of the ball, Sf = specific gravity of the liquid, and B = a constant for each ball. Balls of different size and density cover a range of viscosities. It is accurate for Newtonian liquids and needs only a small sample, but like the capillary method it works at a single shear rate.

### Rotational viscometers

**Cup-and-bob viscometers.** The sample is held in the annular gap between a cup and a bob (cylinder) placed in it. Either the cup rotates (**Couette type**, e.g. MacMichael) or the bob rotates (**Searle type**, e.g. Stormer). The torque or the speed is measured at several settings, giving a rheogram. In the **Stormer viscometer** a falling weight drives the bob; the rate of shear is proportional to the revolutions per minute v and the shearing stress to the driving weight w: η = Kv w/v (Kv = instrument constant). A drawback of cup-and-bob instruments is that the shear rate is not uniform across the gap, and plug flow can occur with plastic materials.

**Cone-and-plate viscometers** (e.g. Ferranti–Shirley, cone-plate Brookfield). The sample sits between a flat plate and a cone of very small angle; one turns against the other. The shear rate is **the same everywhere in the gap**, the sample needed is very small (often under 1 ml), and temperature is controlled easily. For Newtonian liquids η = C T / v, where C = instrument constant, T = torque and v = speed (rpm). Plastic viscosity and yield value can also be calculated.

**Brookfield (spindle) viscometer.** A spindle of a chosen size rotates in the sample at a selected speed; the drag on the spindle (torque) is shown on a dial or display and converted to viscosity using a factor for that spindle and speed (digital models display cP directly). Readings at several speeds, going up and then down, show pseudoplastic or thixotropic behaviour. The helipath stand moves a T-bar spindle slowly down through very stiff materials (creams, gels) so it always cuts fresh material. It is the common instrument for semisolids in pharmacy laboratories.

| Viscometer | Shear | Suitable for | Notes |
| --- | --- | --- | --- |
| Ostwald / Ubbelohde (capillary) | Single point | Newtonian only | Cheap, accurate, compare with water |
| Hoeppler (falling sphere) | Single point | Newtonian only | Small sample, wide range with different balls |
| Cup-and-bob (Stormer, MacMichael) | Multipoint | Newtonian and non-Newtonian | Shear not uniform in gap |
| Cone-and-plate (Ferranti–Shirley) | Multipoint | Both | Uniform shear, small sample |
| Brookfield (spindle) | Multipoint | Both, especially semisolids | Quick, widely used |

## 2.6 Deformation of solids

When a force acts on a solid, it changes the solid's shape (deformation). This is central to **tablet compression**.

- **Stress** = force applied per unit area (dyne/cm² or N/m², i.e. Pa). It may be tensile (pulling), compressive (pushing) or shear (sliding).
- **Strain** = the change in dimension divided by the original dimension (for example ΔL/L). It has no unit.
- **Elastic modulus (Young's modulus, E)** = stress / strain within the elastic range (**Hooke's law**). A high E means a stiff material that strains little under a given stress.

```text
  Stress ^                    x fracture
         |              ____/
         |         ___/      plastic region (permanent deformation)
         |       /  <- yield point
         |      /
         |     /   elastic region: straight line, slope = E (Hooke's law)
         |    /
         +--------------------------------> Strain
```

### Elastic and plastic deformation

| Elastic deformation | Plastic deformation |
| --- | --- |
| Reversible: the solid returns to its original shape when the stress is removed | Permanent: the solid keeps its new shape after the stress is removed |
| Occurs below the **yield point** | Occurs above the yield point |
| Stress proportional to strain (Hooke's law) | Particles flow, slide and form new contacts (bonds) |
| Stored energy is released on decompression and can push particles apart (cause of capping and lamination in tablets) | Helps form strong bonds and hard tablets |

Some materials deform mainly plastically (for example microcrystalline cellulose, sodium chloride), while others fail by **brittle fracture**, breaking into smaller particles that create fresh surfaces for bonding (for example dicalcium phosphate, lactose). Many materials also show **viscoelastic** behaviour: their response depends on how long and how fast the load is applied, which is why slower presses can give stronger tablets of some materials.

### Heckel equation

Heckel treated the reduction in the voids of a powder bed under pressure as a first-order process:

ln [1/(1 − D)] = KP + A

where D = relative density of the compact (density of compact / true density of the powder) at pressure P, 1 − D = porosity, K = slope and A = intercept. The **mean yield pressure Py = 1/K**.

```text
 ln[1/(1-D)] ^
             |           ____ soft, plastic material: steep slope, low Py
             |       ___/
             |   ___/  ______ hard, brittle material: gentle slope, high Py
             | _/____/
             +----------------------> Compression pressure P
```

- A **steep slope (large K, low Py)** means the powder densifies easily by **plastic deformation**.
- A **gentle slope (small K, high Py)** indicates **brittle fracture** materials.
- The intercept A reflects densification by rearrangement of particles at low pressure.

Heckel plots help in choosing excipients, comparing batches of a drug and predicting compression behaviour.

## Remember

- Newton's law: F = ηG; poise = dyne s cm⁻²; 1 cP = 1 mPa s; kinematic viscosity = η/ρ (stokes).
- Viscosity of liquids falls with temperature: η = A e^(Ev/RT).
- Plastic: yield value, U = (F − f)/G (flocculated suspensions); pseudoplastic: shear thinning, N > 1 (gum solutions); dilatant: shear thickening, N < 1 (≥50% deflocculated particles).
- Thixotropy: slow isothermal recovery of consistency after shear; hysteresis loop; useful in suspensions, depot injections, ointments.
- Capillary and falling-sphere viscometers = single point, Newtonian only; cup-and-bob, cone-and-plate and Brookfield = multipoint.
- Ostwald: η1/η2 = ρ1t1/ρ2t2. Hoeppler: η = t(Sb − Sf)B.
- Stress = F/A, strain = ΔL/L, E = stress/strain; elastic = reversible, plastic = permanent.
- Heckel: ln[1/(1 − D)] = KP + A; Py = 1/K; low Py = plastic material.
