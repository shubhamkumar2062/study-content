# Unit 3: Surface and interfacial phenomenon

The boundary between two phases is called an **interface**. When one of the phases is a gas (usually air), it is called a **surface**. Emulsions, suspensions, creams, wetting of tablets, foaming, adsorption of poisons by charcoal and the action of detergents all happen at interfaces. This unit explains why interfaces have extra energy and how surfactants and adsorbents change it.

## 3.1 Types of interfaces

| Phases in contact | Name | Pharmaceutical example |
| --- | --- | --- |
| Liquid / gas | Surface (surface tension) | Foams, spraying of liquids |
| Liquid / liquid | Interface (interfacial tension) | Emulsions |
| Solid / gas | Surface | Adsorption of gases on powders, moisture on tablets |
| Solid / liquid | Interface | Suspensions, wetting, dissolution |
| Solid / solid | Interface | Adhesion of particles, powder flow |
| Gas / gas | None | Gases always mix completely |

## 3.2 Surface tension and interfacial tension

A molecule inside a liquid is pulled equally in all directions by its neighbours. A molecule at the surface has neighbours only below and beside it, so it feels a **net inward pull**. The surface therefore behaves like a stretched skin and tends to shrink to the smallest area (this is why drops are spherical).

```text
        air
   o -> o <- o      surface molecule: pulled sideways and DOWN only
        |           -> net inward force
   o <- o -> o      bulk molecule: pulled equally in all directions
        ^           -> net force zero
       liquid
```

**Surface tension (γ)** is the force per unit length acting parallel to the surface, at right angles to a line of 1 cm drawn on it. Units: **dyne/cm** (CGS) or **mN/m** (SI); 1 dyne/cm = 1 mN/m.

**Interfacial tension** is the same force at the boundary between two immiscible liquids. It is usually **less than the larger of the two surface tensions**, because the molecules of the two liquids attract each other to some extent.

| Liquid (about 20 °C) | Surface tension (dyne/cm) |
| --- | --- |
| Water | 72.8 |
| Chloroform | 27.1 |
| Benzene | 28.9 |
| Ethanol | 22.3 |

| Interface (about 20 °C) | Interfacial tension (dyne/cm) |
| --- | --- |
| Water / benzene | 35.0 |
| Water / n-octanol | 8.5 |

**Effect of temperature:** surface tension falls as temperature rises (molecules have more energy to escape the inward pull) and becomes zero at the critical temperature. **Effect of solutes:** surfactants lower it strongly; inorganic salts raise it slightly.

## 3.3 Surface free energy

To enlarge a surface, molecules must be brought from the bulk to the surface against the inward pull, so work must be done. This work is stored as **surface free energy**:

W = γ × ΔA

W = work (ergs), γ = surface tension (dyne/cm), ΔA = increase in area (cm²). So surface tension is also the **surface free energy per unit area** (erg/cm² = dyne/cm).

**Worked example.** Work needed to enlarge the surface of water (γ = 72.8 dyne/cm) by 10 cm²: W = 72.8 × 10 = 728 ergs.

Any system tends to lower its free energy. That is why dispersed systems with huge interfacial areas (emulsions, fine suspensions) are thermodynamically unstable and need emulsifying or suspending agents.

## 3.4 Measurement of surface and interfacial tension

### Capillary rise method (surface tension only)

A liquid that wets glass rises in a narrow capillary until the upward pull of surface tension balances the weight of the liquid column.

γ = ½ r h ρ g (contact angle taken as zero, cos θ = 1)

r = radius of capillary, h = height of rise, ρ = density, g = 981 cm/s².

```text
     |  |
     |  |   <- liquid rises to height h in capillary of radius r
     |~~|
  ___|  |___
  ~~~~~~~~~~ liquid in beaker
```

**Worked example.** Water rises 2.9 cm in a capillary of radius 0.05 cm (ρ = 1.0 g/cm³):
γ = 0.5 × 0.05 × 2.9 × 1.0 × 981 = **71.1 dyne/cm**.

Not suitable for interfacial tension, and less accurate for liquids that do not wet the glass.

### Ring detachment (du Noüy tensiometer)

A platinum–iridium ring is pulled up through the surface (or through a liquid–liquid interface). The force needed to detach it is read on a torsion balance.

γ = (dial reading / 2 × circumference of ring) × β, where β is a correction factor for the shape of liquid lifted. Works for **both surface and interfacial tension**.

### Drop weight and drop count methods (stalagmometer)

A drop hangs at the tip of a tube until its weight overcomes the surface tension holding it (Tate's law: weight of drop ∝ γ × radius of tip). Using water as the reference liquid in the same stalagmometer:

- **Drop weight:** γ1 / γ2 = m1 / m2 (m = mass of one drop)
- **Drop count:** γ1 / γ2 = (n2 × ρ1) / (n1 × ρ2) (n = number of drops for the same volume)

**Worked example (drop count).** A fixed volume gives 20 drops of water (γ = 72 dyne/cm, ρ = 1.0) and 35 drops of a liquid of density 0.79:
γ = 72 × (20 × 0.79) / (35 × 1.0) = **32.5 dyne/cm**.

Both methods can measure interfacial tension when the drops are formed under a second liquid.

### Wilhelmy plate method

A thin plate (platinum or glass) touches the surface; the downward pull is measured directly: γ = F / (wetted perimeter of plate × cos θ), where the wetted perimeter is 2 × (width + thickness). Useful for following changes with time.

## 3.5 Spreading coefficient

When one liquid is placed on another (e.g. an oil drop on water), it either spreads as a film or stays as a lens. Two quantities matter:

- **Work of adhesion** (between unlike liquids): Wa = γL + γS − γLS
- **Work of cohesion** (of the spreading liquid itself): Wc = 2γL

**Spreading coefficient**

S = Wa − Wc = γS − (γL + γLS)

γS = surface tension of the sublayer (e.g. water), γL = surface tension of the spreading liquid (e.g. oil), γLS = interfacial tension between them.

- **S positive** → the liquid spreads.
- **S negative** → it forms a lens (globule).

**Worked example.** Benzene on water: S = 72.8 − (28.9 + 35.0) = **+8.9 dyne/cm**, so benzene first spreads. After the two liquids saturate each other, their tensions change and S becomes negative, so the film draws back into lenses.

**Uses:** spreading of lotions and ointments on skin, wetting of powders, film coating, and choice of oils that spread on the skin (which has an oily surface layer).

## 3.6 Adsorption at liquid interfaces

**Adsorption** is the accumulation of a substance at a surface or interface, in a concentration higher (positive) or lower (negative) than in the bulk.

- **Positive adsorption:** surface-active molecules gather at the interface and lower the surface tension.
- **Negative adsorption:** inorganic electrolytes stay away from the surface and slightly raise the surface tension.

**Gibbs adsorption equation**

Γ = − (c / RT) × (dγ / dc)

Γ = surface excess (moles adsorbed per cm² of surface), c = bulk concentration. If γ falls as c rises (dγ/dc negative), Γ is positive. The equation lets us calculate how much surfactant sits at the surface and the area each molecule occupies.

```text
   AIR           tail  tail  tail     <- hydrophobic tails point out of water
   ----------    |     |     |
   WATER         O     O     O        <- polar heads stay in water
```

## 3.7 Surface-active agents (surfactants)

A **surfactant** (amphiphile) has two parts: a **hydrophilic (polar) head** and a **lipophilic (hydrocarbon) tail**. Because each part likes a different phase, the molecule sits at interfaces and lowers surface or interfacial tension.

**Classification by charge on the head**

| Class | Head | Examples | Uses |
| --- | --- | --- | --- |
| Anionic | Negative | Sodium lauryl sulfate (SLS), sodium stearate and other soaps, docusate sodium | Detergents, wetting agents, o/w emulsifiers; irritant, incompatible with cationic drugs |
| Cationic | Positive | Benzalkonium chloride, cetrimide, cetylpyridinium chloride | Mainly antiseptics and preservatives |
| Non-ionic | No charge | Sorbitan esters (Spans), polysorbates (Tweens), polyoxyethylene ethers, glyceryl monostearate | Least toxic; emulsifiers and solubilisers in oral, topical and injectable products |
| Ampholytic (zwitterionic) | Both, depending on pH | Lecithin, betaines | Emulsions for injection (lecithin), mild cleansers |

**Micelles and CMC.** At low concentration surfactant molecules go to the surface. Once the surface is full, extra molecules gather in the bulk into **micelles** — clusters with tails inside and heads facing water. The concentration at which micelles first form is the **critical micelle concentration (CMC)**. At the CMC many properties change sharply: surface tension stops falling, conductivity (for ionic surfactants) changes slope, osmotic pressure levels off, and solubilisation begins.

```text
 Surface tension
   |\
   | \
   |  \
   |   \______________   <- break = CMC (surface tension stays almost constant after it)
   |________________________ log concentration
```

```text
   Normal micelle in water          Reverse micelle in oil
        \  |  /                         heads inside, tails out
     -O  \ | /  O-
       \__\|/__/        tails in the core
        /  |  \         heads on the surface
     -O /  |  \ O-
```

- **Krafft point** — the temperature above which an ionic surfactant's solubility rises sharply and micelles form.
- **Cloud point** — the temperature at which a non-ionic surfactant solution turns cloudy on heating (it loses hydration and separates).

## 3.8 HLB scale

Griffin's **hydrophile–lipophile balance (HLB)** gives each surfactant a number (usually 1–20 for non-ionics) showing the balance between its water-loving and oil-loving parts. **Low HLB = more lipophilic; high HLB = more hydrophilic.**

| HLB range | Use |
| --- | --- |
| 1–3 | Antifoaming agents |
| 3–6 | Water-in-oil (w/o) emulsifiers |
| 7–9 | Wetting and spreading agents |
| 8–18 | Oil-in-water (o/w) emulsifiers |
| 13–15 | Detergents |
| 15–18 | Solubilisers |

Typical values: sorbitan mono-oleate (Span 80) 4.3; sorbitan monolaurate (Span 20) 8.6; polysorbate 80 (Tween 80) 15.0; polysorbate 20 (Tween 20) 16.7; sodium lauryl sulfate about 40.

**Calculating HLB**

1. **Polyhydric alcohol fatty acid esters:** HLB = 20 (1 − S/A), S = saponification number of the ester, A = acid number of the fatty acid.
   *Example:* glyceryl monostearate, S = 161, A = 198 → HLB = 20 (1 − 161/198) = **3.7** (a w/o emulsifier).
2. **When saponification number is hard to get:** HLB = (E + P) / 5, E = weight % of oxyethylene chains, P = weight % of polyhydric alcohol.
3. **Only ethylene oxide as hydrophilic part:** HLB = E / 5.
4. **Davies' group numbers:** HLB = Σ(hydrophilic group numbers) − Σ(lipophilic group numbers) + 7.

**Blending surfactants.** HLB of a mixture is the weighted average: HLBmix = fA × HLBA + (1 − fA) × HLBB.

*Worked example.* An oil needs a required HLB of 12. Using Tween 80 (15.0) and Span 80 (4.3):
fraction of Tween 80 = (12 − 4.3) / (15.0 − 4.3) = 7.7 / 10.7 = **0.72** → 72% Tween 80 and 28% Span 80.

**Required HLB** is the HLB that gives the most stable emulsion of a particular oil; mixtures of surfactants usually give more stable emulsions than one alone.

## 3.9 Solubilisation

**Micellar solubilisation** is the increase in solubility of a poorly water-soluble substance by surfactant micelles, above the CMC. The drug is taken into the micelle, so the solution stays clear.

Where the drug sits depends on its polarity:

- **Non-polar** molecules (e.g. hydrocarbons) — in the hydrocarbon **core**.
- **Semipolar** molecules (e.g. fatty alcohols, many drugs) — between the tails with their polar group near the heads (**palisade layer**).
- **Polar** molecules — at the micelle **surface**, or within the polyoxyethylene shell of non-ionic micelles.

**Factors:** surfactant type and concentration (above CMC), nature of the drug, temperature, added electrolytes.

**Pharmaceutical examples:** fat-soluble vitamins (A, D, E, K) in clear aqueous drops using polysorbates; steroids and essential oils in aqueous products; cresol and chloroxylenol disinfectant solutions made clear with soaps; poorly soluble drugs in injections (polysorbate 80 in some formulations). Drawbacks: some surfactants are toxic or haemolytic, and solubilisation may reduce preservative activity.

## 3.10 Detergency

**Detergency** is the removal of dirt (oily and particulate soil) from a surface by a surfactant. It is a combination of several actions:

1. **Wetting** of the surface and the dirt (lowered surface tension lets the solution penetrate).
2. **Adsorption** of surfactant at the dirt–surface and dirt–water interfaces, loosening the dirt.
3. **Emulsification** of oily soil into tiny droplets.
4. **Solubilisation** of oily material into micelles.
5. **Deflocculation and suspension** of solid particles so they do not redeposit.
6. **Foaming** helps carry dirt away (but is not essential).

Good detergents have HLB about 13–15. Examples: soaps, sodium lauryl sulfate. Uses: cleaning equipment, medicated shampoos, skin cleansers.

## 3.11 Adsorption at the solid interface

Solids with large surface areas (activated charcoal, kaolin, silica gel, alumina) adsorb gases and dissolved substances on their surfaces. The solid is the **adsorbent**; the substance held is the **adsorbate**.

| Feature | Physical adsorption (physisorption) | Chemical adsorption (chemisorption) |
| --- | --- | --- |
| Forces | Van der Waals | Chemical bonds |
| Heat of adsorption | Low (about 1–10 kcal/mol) | High (more than about 20 kcal/mol) |
| Reversibility | Reversible | Usually irreversible |
| Layers | Can be multilayer | Monolayer only |
| Specificity | Non-specific | Specific |
| Temperature | Favoured by low temperature | Needs some activation, occurs at higher temperature |

### Adsorption isotherms

An **isotherm** relates the amount adsorbed (x/m = mass of adsorbate per gram of adsorbent) to the pressure or concentration at constant temperature.

**Freundlich isotherm (empirical)**

x/m = k c^(1/n) → log (x/m) = log k + (1/n) log c

Plot log (x/m) against log c: slope = 1/n, intercept = log k.

**Langmuir isotherm** (assumes a monolayer and identical sites)

x/m = (ym b c) / (1 + b c) → c / (x/m) = 1/(b ym) + c/ym

Plot c/(x/m) against c: slope = 1/ym, intercept = 1/(b ym). ym = amount needed for a complete monolayer; b = constant related to the binding affinity.

**Worked example (Langmuir).** A plot of c/(x/m) against c gives slope 2.5 g/mmol and intercept 0.5 g/L. Then ym = 1/2.5 = **0.4 mmol/g**, and b = 1/(ym × intercept) = 1/(0.4 × 0.5) = **5 L/mmol**.

**BET equation** describes multilayer adsorption of gases and is used to measure the surface area of powders. Brunauer described five shapes of isotherm (types I–V); type I is the Langmuir (monolayer) shape.

**Factors affecting adsorption:** surface area and porosity of the adsorbent, nature of adsorbate (solubility — less soluble substances adsorb more), concentration, temperature (physical adsorption decreases as temperature rises), pH (un-ionised forms usually adsorb more).

### Wetting and contact angle

When a drop rests on a solid, the angle between the solid surface and the tangent to the drop at the point of contact is the **contact angle (θ)**.

- θ = 0° — complete wetting.
- θ < 90° — partial wetting (the liquid wets the solid).
- θ > 90° — poor wetting (water on waxy or hydrophobic powders).

Wetting agents (surfactants with HLB 7–9) lower θ so that hydrophobic powders such as sulfur or charcoal disperse in water in suspensions.

### Pharmaceutical applications of adsorption

1. **Activated charcoal** as an antidote for drug overdose and poisoning (adsorbs the drug in the gut).
2. Kaolin and attapulgite in antidiarrhoeal preparations.
3. Decolourising and purifying solutions, removal of pyrogens.
4. Chromatography (adsorption chromatography, TLC).
5. Loss of drugs or preservatives by adsorption onto containers, filters, rubber closures and plastic tubing.
6. Moisture adsorption on powders and tablets; desiccants such as silica gel.
7. Measuring surface area of powders (BET).

## Remember

- Surface tension: force per unit length (dyne/cm = mN/m); water 72.8 dyne/cm; falls with temperature.
- Surface free energy W = γΔA; dispersed systems are unstable because they have large interfacial area.
- Capillary rise γ = ½rhρg; drop count γ1/γ2 = (n2ρ1)/(n1ρ2); du Noüy ring measures both surface and interfacial tension.
- S = γS − (γL + γLS): positive spreads, negative forms a lens.
- Gibbs: Γ = −(c/RT)(dγ/dc); surfactants show positive adsorption.
- Surfactants: anionic (SLS), cationic (benzalkonium), non-ionic (Spans, Tweens), ampholytic (lecithin). Micelles form at the CMC.
- HLB: 3–6 w/o, 8–18 o/w, 13–15 detergents, 15–18 solubilisers; HLB = 20(1 − S/A); blend by weighted average.
- Freundlich log(x/m) = log k + (1/n)log c; Langmuir c/(x/m) = 1/(b ym) + c/ym.
