# Unit 1: Flow of fluids, size reduction and size separation

Pharmaceutical engineering studies the **unit operations** of a factory: steps such as pumping, grinding, sieving, heating, drying and mixing that appear again and again, whatever product is being made. This unit covers how liquids flow through pipes and how they are measured, how solids are broken into smaller particles, and how particles are sorted by size.

For each machine the exam expects the same six headings: **principle, construction (with a sketch), working, uses, merits and demerits.** Learn every machine in that order.

## 1.1 Flow of fluids

A **fluid** is anything that flows: liquids and gases. In a plant, water, syrups, solvents, steam and air move through pipes all day, so we need to measure pressure, flow rate and the energy lost on the way.

### Manometers

A manometer measures a **pressure difference** using a column of liquid. The difference in level of the liquid tells the pressure difference.

| Type | Construction | Use |
| --- | --- | --- |
| Simple U-tube | Glass U-tube half filled with a manometric liquid (mercury, water, carbon tetrachloride) | Pressure difference between two points |
| Differential (two-fluid) | U-tube with two immiscible liquids of close density | Very small pressure differences (amplifies the reading) |
| Inclined | One limb tilted at a small angle | Small differences: the liquid moves a long way along the slope, so it is easy to read |
| Well-type | One limb replaced by a wide reservoir | Only one limb needs to be read |
| Micromanometer | Inclined tube with fine adjustment | Very small differences, e.g. low gas pressures |

```text
 Simple U-tube manometer

   P1 →  |      | ← P2
         |      |
         |      |  ─┬─
         |▓▓▓▓▓▓|   │ h  (difference in level)
         |▓▓▓▓▓▓|  ─┴─
         └▓▓▓▓▓▓┘
        manometric liquid (density ρA)
```

**Equation:** P1 − P2 = h (ρA − ρB) g

where h is the difference in level, ρA the density of the manometric liquid, ρB the density of the fluid above it and g the gravitational acceleration. If the fluid above is a gas, ρB is negligible and P1 − P2 ≈ h ρA g.

### Reynolds number and its significance

Osborne Reynolds injected a thin stream of dye into water flowing through a glass tube.

- At low velocity the dye moved as a straight thread: **laminar (streamline) flow**. Layers slide over one another without mixing.
- At high velocity the dye broke up and coloured the whole tube: **turbulent flow**. Eddies mix the fluid.

He showed that the type of flow depends on a dimensionless group, the **Reynolds number (Re)**:

**Re = D u ρ / µ**

| Symbol | Meaning | SI unit |
| --- | --- | --- |
| D | Inside diameter of the pipe | m |
| u | Average velocity | m/s |
| ρ | Density of the fluid | kg/m³ |
| µ | Viscosity of the fluid | Pa·s (kg/m·s) |

All the units cancel, so Re has no unit. It is the ratio of **inertial forces to viscous forces**.

| Re | Type of flow |
| --- | --- |
| Below about 2000 | Laminar |
| About 2000–4000 | Transition region (unstable) |
| Above about 4000 | Turbulent |

**Significance:** (1) predicts whether flow will be laminar or turbulent; (2) decides which friction equation to use for pressure loss; (3) used to design pipes, pumps and mixers; (4) in heat transfer and mixing, turbulence increases the rate of transfer, so a higher Re means faster heating or mixing; (5) used in scale-up from laboratory to plant, since two systems behave alike when their Reynolds numbers are equal.

### Bernoulli's theorem

For a steady, frictionless flow of an incompressible fluid, the **total energy per unit weight stays constant** along a streamline. Energy only changes form between pressure, velocity and height.

**P/ρg + u²/2g + Z = constant**

- P/ρg = pressure head
- u²/2g = velocity (kinetic) head
- Z = potential head (height above a reference)

Between two points 1 and 2 in a real pipe, friction loss (hf) and pump work (W) are added:

P1/ρg + u1²/2g + Z1 + W = P2/ρg + u2²/2g + Z2 + hf

**Applications:** working principle of orifice meter, venturimeter and Pitot tube; design of pumps and pipelines; vacuum aspirators and sprayers (high velocity at a narrow point lowers pressure and sucks in liquid); calculating the power a pump needs.

### Energy losses

Real fluids lose energy as heat because of friction. Losses are of two kinds.

1. **Major (frictional) losses** in straight pipes, given by the **Fanning equation**:
   hf = 4 f L u² / (2 g D), or as pressure drop ΔP = 2 f ρ u² L / D
   where f is the Fanning friction factor and L the pipe length. For laminar flow f = 16/Re (this is equivalent to the Hagen–Poiseuille equation). For turbulent flow f depends on Re and the roughness of the pipe.
2. **Minor losses** from:
   - sudden expansion of the pipe
   - sudden contraction
   - fittings and valves (elbows, tees, globe valves), expressed as an *equivalent length* of straight pipe
   - obstructions such as flow meters.

Losses rise with velocity, length and roughness, and fall with pipe diameter.

### Orifice meter

**Principle:** a thin plate with a sharp-edged hole (orifice) is placed in the pipe. The fluid speeds up through the hole and its pressure falls. The pressure drop, read on a manometer, is related to velocity by Bernoulli's theorem.

```text
           orifice plate
               ║
  ─────────────╨─────────────
   flow →     ┌─┐   vena contracta
  ─────────────╥─────────────
               ║
     P1 tap ●          ● P2 tap
             └──U-tube──┘  (reads Δh)
```

**Equation:** u0 = C0 √(2 g Δh), where C0 (coefficient of discharge) is about 0.61. The narrowest part of the jet just after the plate is the **vena contracta**.

**Merits:** cheap, simple, small, plate is easy to change for a different range. **Demerits:** large permanent pressure loss (energy wasted), low accuracy, plate edge wears.

### Venturimeter

**Principle:** same as the orifice meter, but the change in cross-section is gradual, so very little energy is lost.

**Construction:** three parts: a short **converging cone**, a narrow **throat**, and a long, gently **diverging cone** (about 5–7°). Pressure taps at the inlet and throat are joined to a manometer.

```text
   inlet         throat         diverging cone
  ───────╲                  ╱──────────────────
          ╲_______________╱
   flow →
          ╱‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╲
  ───────╱                  ╲──────────────────
     ● P1           ● P2
```

**Equation:** u = Cv √(2 g Δh) / √(1 − β⁴), where β is the throat-to-pipe diameter ratio. The coefficient Cv is about 0.98.

**Merits:** accurate, low permanent pressure loss, solids do not collect. **Demerits:** expensive, long, cannot be changed easily for a different flow range.

### Pitot tube

**Principle:** measures the **local (point) velocity**. A tube faces the flow, so the fluid striking it is brought to rest and its kinetic energy turns into pressure (impact pressure). A second opening reads the static pressure. The difference gives velocity: u = C √(2 g Δh).

**Uses:** velocity at different points of a pipe or duct, air velocity in dryers and ventilation. **Demerit:** gives point velocity only, so many readings are needed to get the average; not suited to liquids carrying solids, which block the opening.

### Rotameter

**Principle:** a **variable-area** meter. A float sits in a vertical tapered glass tube that is wider at the top. Fluid flows upward and lifts the float until the gap around it is just big enough for the flow. The **pressure drop stays constant** while the area changes.

```text
      ↑ outlet
     ╱  ╲
    ╱    ╲   ← tapered glass tube with scale
   ╱  ▄▄  ╲  ← float rises higher at higher flow
  ╱   ▀▀   ╲
  ╲________╱
      ↑ inlet (flow upward)
```

**Merits:** flow is read directly on the scale, simple, cheap, little pressure loss. **Demerits:** must be mounted vertically, glass breaks, not for opaque liquids, calibrated for one fluid only.

## 1.2 Size reduction

**Size reduction (comminution)** is breaking solid material into smaller pieces by mechanical force.

### Objectives

1. Increase surface area, so drugs dissolve faster and act faster (better bioavailability, e.g. griseofulvin).
2. Help extraction of crude drugs (solvent reaches the cells more easily).
3. Make mixing uniform and keep tablet and capsule content uniform.
4. Improve physical stability of suspensions and emulsions (fine particles settle slowly).
5. Make drying faster (more surface).
6. Improve flow and compression of granules (sizing of wet and dry granules).
7. Make topical products smooth (ointments, creams).

### Mechanisms

| Mechanism | How force acts | Example machine |
| --- | --- | --- |
| Cutting | Sharp blade | Cutter mill |
| Compression | Squeezing between two surfaces | Roller mill, end runner mill |
| Impact | Sudden blow from a hammer or ball | Hammer mill, ball mill |
| Attrition | Rubbing between two surfaces | Fluid energy mill, edge runner |

Most mills use more than one mechanism.

### Laws of size reduction

Energy is needed to make new surface. Walker's general equation is dE/dL = −C / Lⁿ, where E is energy, L particle size and C a constant. Different values of n give the three laws.

| Law | n | Equation | Best for |
| --- | --- | --- | --- |
| **Rittinger's** | 2 | E = KR (1/L2 − 1/L1) | Fine grinding (energy ∝ new surface area) |
| **Kick's** | 1 | E = KK ln (L1/L2) | Coarse crushing (equal energy for equal reduction ratio) |
| **Bond's** | 1.5 | E = KB (1/√L2 − 1/√L1) | Intermediate range, most practical mills |

L1 is the feed size and L2 the product size. Bond's law uses the **work index**, the energy needed to reduce unit weight of a material from a very large size to 100 µm.

Only a very small fraction of the energy supplied actually makes new surface. Most is lost as heat, noise and wear.

### Factors affecting size reduction

1. **Hardness:** hard materials (Mohs scale) need more energy and wear the mill.
2. **Toughness:** fibrous crude drugs (ginger, liquorice) resist breaking. Drying or freezing them first makes them brittle.
3. **Stickiness:** gummy materials clog screens. Add an inert powder or chill them.
4. **Softening temperature:** waxy substances (stearic acid) melt from the heat of milling. Cool the mill.
5. **Moisture content:** grind dry (below about 5% water) or wet (above about 50%). In between, the mass becomes sticky.
6. **Material structure:** crystalline solids break along cleavage planes; vegetable drugs have cellular structure.
7. **Physiological effects:** potent or irritant drugs need closed mills.
8. **Purity required:** wear of the mill may contaminate the product.
9. **Bulk density and ratio of feed size to product size.**

### Hammer mill

**Principle:** impact. Rapidly rotating hammers strike the material.

**Construction:** a steel casing holding a central shaft (rotor). Swinging or fixed hammers are attached to the rotor. A **screen** at the bottom sets the product size. Material enters through a hopper at the top. Hammers may have flat (impact) faces for brittle material or knife edges for cutting.

```text
          hopper
          │ ▼ │
   ┌──────┴───┴──────┐
   │    ╲  │  ╱      │  ← casing
   │   ─── ● ───     │  ← rotor with swinging hammers
   │    ╱  │  ╲      │
   │ ░░░░░░░░░░░░░░░ │  ← screen
   └────────┬────────┘
            ▼ product
```

**Working:** the rotor spins at high speed. Hammers hit the particles and throw them against the casing. They keep breaking until small enough to pass through the screen.

**Uses:** dry granules and powders, crude drugs (barks, roots, leaves), sizing of wet granules in tablet making, filter-press cakes.

**Merits:** rapid, continuous, small, easy to clean, product size controlled by changing the screen or speed, handles many materials.

**Demerits:** heat build-up damages thermolabile drugs; screen may clog with sticky material; hammers wear and contaminate; not for very hard abrasive materials; noisy.

### Ball mill

**Principle:** impact and attrition. Falling balls hit the material, and balls rubbing against each other grind it.

**Construction:** a hollow cylinder (stainless steel or porcelain-lined) mounted horizontally that rotates about its axis. It is filled to about 30–50% of its volume with balls of steel, stoneware or porcelain. Balls of mixed sizes are used: large balls break coarse feed, small balls finish fine grinding.

**Working:** the cylinder rotates and the balls are lifted on the rising side, then fall or roll back. Speed decides what happens:

| Speed | Ball movement | Result |
| --- | --- | --- |
| Too low | Balls slide and roll over each other | Mainly attrition, slow |
| Optimum (about 0.5–0.75 of critical) | Balls are carried up and fall in a cascade | Impact + attrition, best grinding |
| At or above critical | Balls stick to the wall by centrifugal force | No grinding |

**Critical speed** is the speed at which the balls just begin to stick to the wall:

Nc = (1 / 2π) √( g / (R − r) ) revolutions per second

where R is the radius of the mill and r the radius of a ball. With diameters in metres, this works out to about Nc ≈ 42.3 / √(D − d) rpm.

**Uses:** fine grinding of hard and soft drugs, dyes and pigments, wet grinding to make suspensions, sterile grinding (closed mill).

**Merits:** very fine product (down to about 10 µm or less); wet or dry milling; closed system for toxic or sterile products; simple to install.

**Demerits:** slow and noisy; ball and wall wear contaminate the product; hard to clean; not for soft or sticky materials; heat build-up in long runs.

### Fluid energy mill (jet mill, micronizer)

**Principle:** attrition and impact between particles moving at very high speed in a stream of compressed air or inert gas.

**Construction:** a hollow oval loop of pipe (about 20–200 mm in diameter and 1–2 m high). Air or gas at high pressure enters through **nozzles** at the bottom. Feed enters through a venturi injector. A **classifier** at the outlet lets only fine particles leave; coarse ones keep circulating.

```text
        ┌──────────────────┐
        │  ╭────────────╮  │ → fine particles out
        │  │            │  │   (classifier)
        │  │   loop     │  │
 feed → │  │            │  │
        │  ╰────────────╯  │
        └──▲──▲──▲──▲──────┘
           compressed air nozzles
```

**Working:** gas from the nozzles makes the particles race around the loop. They collide with each other and with the wall. Centrifugal force keeps coarse particles in the outer path, while fine particles are carried to the outlet.

**Uses:** micronising drugs to 1–20 µm (often below 5 µm): antibiotics, corticosteroids, vitamins, and drugs for inhalation.

**Merits:** very fine and uniform product; no heating (expanding gas cools), so suitable for thermolabile drugs; no moving parts, so little contamination; inert gas protects oxidisable drugs; size classification built in.

**Demerits:** high running cost (compressed gas); feed must already be fine (pre-milled); dust and fine product loss; risk of dust explosion; not economical for small batches.

### Edge runner mill

**Principle:** crushing (compression) by the weight of heavy rollers plus attrition (shearing) as they turn.

**Construction:** one or two heavy stone or granite **rollers mounted on their edge**, moving on a stone or granite bed (pan). The rollers are fixed on a horizontal shaft that is rotated around a central vertical shaft. A scraper keeps the material in the path of the rollers.

**Working:** each roller turns on its own axis and also travels around the pan. The weight crushes the material and the turning rubs it. The scraper returns material to the track. The powder is sieved and the coarse part returned.

**Uses:** fine grinding of tough, fibrous crude drugs; mixing of semisolid masses.

**Merits:** needs little attention; gives fine powder; can grind tough materials.

**Demerits:** slow and bulky (takes much floor space); not for sticky materials; noisy; can contaminate if the stone wears.

### End runner mill

**Principle:** crushing and shearing between a heavy pestle and a rotating mortar.

**Construction:** a large steel **mortar** rotated by a motor. A heavy steel **pestle** is mounted **off-centre** (eccentrically) inside it, so it turns by friction with the material and the mortar. A scraper keeps the material under the pestle. The pestle can be raised for emptying and cleaning.

**Working:** as the mortar turns, the pestle rolls and grinds the material by compression and shear.

**Uses:** fine grinding of drugs and chemicals.

**Merits:** gives fine powder; simple. **Demerits:** not for sticky or moist materials; batch process; slow.

## 1.3 Size separation

**Size separation (sifting, screening)** divides a powder into fractions of different particle size.

### Objectives and applications

1. Get powders of the size grade the pharmacopoeia requires.
2. Improve uniformity of mixing and dosing (tablet weight, capsule fill).
3. Remove oversize lumps and foreign matter.
4. Grade granules before compression.
5. Analyse particle size distribution (quality control).
6. Collect fine dust from mills and dryers.

### Mechanisms

- **Agitation:** oscillation, vibration or gyration of the sieve.
- **Brushing:** a brush moves particles over the mesh and pushes them through.
- **Centrifugal:** high-speed rotor throws particles against the sieve.
- **Fluid methods:** air or water currents separate particles by settling velocity (cyclone, air separator, elutriation).

### Standard sieves and official grades

IP sieves are made of woven wire (stainless steel, brass or bronze). The **sieve number** is roughly the number of meshes in a length of 25.4 mm. A higher number means a smaller opening.

| Sieve number | Nominal aperture |
| --- | --- |
| 10 | 1700 µm |
| 22 | 710 µm |
| 44 | 355 µm |
| 60 | 250 µm |
| 85 | 180 µm |
| 120 | 125 µm |

**Official grades of powders (IP):**

| Grade | Description |
| --- | --- |
| Coarse powder | All passes sieve 10, not more than 40% passes sieve 44 |
| Moderately coarse | All passes sieve 22, not more than 40% passes sieve 60 |
| Moderately fine | All passes sieve 44, not more than 40% passes sieve 85 |
| Fine powder | All passes sieve 85 |
| Very fine powder | All passes sieve 120 |

### Sieve shaker

**Principle:** particles pass through the openings of a sieve when shaken; larger ones are retained.

**Construction:** a nest of standard sieves, the coarsest on top and the finest at the bottom, with a lid and a receiving pan. The nest is clamped on a motor-driven shaker that gives vibration, gyration or tapping.

**Working:** a weighed sample is put on the top sieve and shaken for a fixed time (e.g. 10–20 minutes). Each sieve is weighed to find the amount retained.

**Uses:** particle size analysis of powders and granules; grading of granules.

**Merits:** simple, cheap, reproducible, standardised. **Demerits:** batch; fine cohesive powders clog the mesh; long shaking wears particles; not for particles below about 40 µm.

### Cyclone separator

**Principle:** centrifugal force. A gas stream carrying particles spins inside a cone, throwing heavier particles to the wall.

**Construction:** a short vertical cylinder with a cone below. The feed (air + solids) enters **tangentially** at the top. A central outlet pipe at the top lets clean air leave. Solids leave at the bottom of the cone.

```text
   air out ↑
       ┌──┴──┐
 feed →│  │  │  ← tangential inlet, gas spirals down
       │  │  │
        ╲   ╱    ← cone
         ╲ ╱
          ▼ coarse solids out
```

**Working:** the stream spirals down along the wall; particles hit the wall, lose speed and fall to the bottom. The gas reverses near the bottom and leaves through the central pipe, carrying the very fine particles.

**Uses:** collecting product from spray dryers and fluid energy mills; separating coarse from fine powder; removing dust from exhaust air.

**Merits:** no moving parts, cheap, continuous, little maintenance. **Demerits:** poor at collecting very fine particles; wall erosion with abrasive solids; needs a bag filter after it for fine dust.

### Air separator

**Principle:** particles of different size have different settling velocities in a rising air current, combined with centrifugal action.

**Construction:** a cylindrical vessel with a **rotating disc** that spreads the feed and a **fan** that drives air upward and around. Coarse particles fall into an inner cone; fine particles are carried by the air to an outer cone where they settle.

**Working:** feed falls onto the spinning disc and is thrown outward into the air current. Heavy particles drop back; fine ones are lifted and collected separately.

**Uses:** classifying fine powders; often fitted after ball and hammer mills so oversize can be returned.

**Merits:** continuous, sharp separation of fines. **Demerits:** power for the fan; not for sticky powders.

### Bag filter

**Principle:** air carrying dust passes through fabric bags; the cloth acts as a sieve and the dust layer itself becomes a fine filter.

**Construction:** a chamber containing many long cloth bags (cotton, wool or synthetic). A fan draws dusty air into the bags and out through the cloth. A shaker (or reverse air jet) knocks the dust off into a hopper.

**Working:** air passes through the bags and leaves clean; dust collects on the inner surface. At intervals the bags are shaken or air is blown back to drop the dust.

**Uses:** final collection of very fine dust (down to about 1 µm) from spray dryers, fluidised bed dryers, mills; dust control in powder rooms.

**Merits:** very efficient for fine particles; recovers valuable product. **Demerits:** bags tear and must be replaced; not for wet or sticky gases; fire risk with some dusts.

### Elutriation tank

**Principle:** particles settle in a fluid at a speed given by **Stokes' law**: v = d² (ρs − ρf) g / 18 η. In an upward-flowing fluid, particles whose settling velocity is less than the fluid velocity are carried up and out; larger ones settle.

**Construction:** a series of tanks of increasing diameter (and so decreasing upward velocity), joined so the overflow of one feeds the next.

**Working:** the suspension enters the first, narrowest tank, where only the coarsest particles settle. Finer particles pass on and settle in later, wider tanks where the velocity is lower.

**Uses:** separating fine particles in suspension, grading insoluble powders (e.g. kaolin, calamine) by levigation and elutriation.

**Merits:** gentle, continuous, separates very fine particles. **Demerits:** wet product must then be dried; slow; needs large volume of fluid.

## Remember

- Re = Duρ/µ; laminar below about 2000, turbulent above about 4000.
- Bernoulli: P/ρg + u²/2g + Z = constant. It is the principle of the orifice meter, venturimeter and Pitot tube.
- Rotameter = constant pressure, variable area. Orifice and venturi = constant area, variable pressure.
- Rittinger (fine, n = 2), Kick (coarse, n = 1), Bond (intermediate, n = 1.5).
- Hammer mill = impact; ball mill = impact + attrition; fluid energy mill = attrition, no heat.
- Ball mill works best at about 0.5–0.75 of the critical speed; Nc = (1/2π)√(g/(R − r)).
- Higher sieve number = smaller aperture; fine powder passes sieve 85, very fine passes 120.
- Cyclone (centrifugal, coarse) → bag filter (fine dust); elutriation uses Stokes' law.
