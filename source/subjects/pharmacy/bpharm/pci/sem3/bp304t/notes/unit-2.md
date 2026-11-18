# Unit 2: Heat transfer, evaporation and distillation

Almost every pharmaceutical process involves heating or cooling: preparing syrups, sterilising, evaporating extracts, distilling solvents, drying granules. This unit explains how heat moves, then two operations that depend on it: **evaporation** (removing a solvent to concentrate a liquid) and **distillation** (separating liquids by boiling and condensing).

## 2.1 Heat transfer

### Objectives and applications

1. Preparation of solutions and syrups (heating to dissolve).
2. Evaporation, distillation and drying.
3. Sterilisation by moist and dry heat; cooling after sterilisation.
4. Crystallisation (cooling a hot saturated solution).
5. Melting and congealing of bases (suppositories, ointments).
6. Controlling temperature in reactors and fermenters.

### Mechanisms of heat transfer

| Mode | How heat moves | Needs a medium? | Example |
| --- | --- | --- | --- |
| **Conduction** | Vibration and collision of molecules passing energy along, without the material moving | Yes (mainly solids) | Heat through the wall of a steam jacket |
| **Convection** | Bulk movement of a fluid carrying heat | Yes (liquids, gases) | Hot air in a tray dryer |
| **Radiation** | Electromagnetic waves (infrared) | No, works in vacuum | Infrared lamps, heat from a furnace |

**Convection** is *natural* when the fluid moves because warm fluid is lighter and rises, and *forced* when a pump, fan or stirrer moves it. Forced convection is much faster.

### Fourier's law (conduction)

The rate of heat flow through a material is proportional to the area and to the temperature gradient:

**dQ/dt = −k A (dT/dx)**

| Symbol | Meaning |
| --- | --- |
| dQ/dt | Rate of heat flow (W) |
| k | Thermal conductivity (W/m·K) |
| A | Area at right angles to the heat flow (m²) |
| dT/dx | Temperature gradient across the thickness (K/m) |

The minus sign shows heat flows from hot to cold. For a flat wall of thickness x with faces at T1 and T2: Q/t = k A (T1 − T2) / x.

This can be written like Ohm's law: **rate = driving force ÷ resistance**, where the resistance is x / kA. For a **composite wall** (e.g. steel lined with insulation), resistances add in series:

Q/t = (T1 − T3) / (x1/k1A + x2/k2A)

Metals (copper, aluminium) have high k; glass, air, cork and asbestos have low k and are used as insulators.

### Convection: film coefficient

When a fluid flows past a wall, a thin still layer (**film**) stays next to the surface. Most resistance to heat flow lies in this film. The rate is given by Newton's law of cooling:

**Q/t = h A ΔT**

where h is the **film (surface) heat transfer coefficient** (W/m²·K). Turbulence makes the film thinner and h larger. Scale and dirt on the wall (**fouling**) add extra resistance.

### Overall heat transfer coefficient

In a heat exchanger, heat passes from the hot fluid film → wall → cold fluid film. The three resistances add:

**1/U = 1/h1 + x/k + 1/h2** (plus fouling resistances, if any)

and the total rate is Q/t = U A ΔT. For changing temperatures along the exchanger, the **log mean temperature difference (LMTD)** is used for ΔT:

LMTD = (ΔT1 − ΔT2) / ln (ΔT1/ΔT2)

### Radiation

All bodies above absolute zero give off radiant energy. A **black body** absorbs all radiation falling on it and is the perfect emitter. Real bodies (**grey bodies**) emit less; the ratio is the **emissivity (ε)**, from 0 to 1. Polished metals have low ε; black painted surfaces have high ε.

**Stefan–Boltzmann law:** Q/t = ε σ A T⁴, where σ = 5.67 × 10⁻⁸ W/m²·K⁴ and T is in kelvin. Net exchange between a body at T1 and surroundings at T2 is ε σ A (T1⁴ − T2⁴).

**Kirchhoff's law:** at the same temperature, a body's emissivity equals its absorptivity. Good absorbers are good emitters.

### Heat exchangers and heat interchangers

Both transfer heat from one fluid to another **through a metal wall**, without mixing them.

- **Heat exchanger:** heat is given by a heating medium such as **steam or hot gas** to a process fluid (or removed by a cooling medium). Examples: tubular heater, shell-and-tube steam heater.
- **Heat interchanger:** heat passes from **one process liquid to another** (or one gas to another), usually to recover heat, e.g. a hot product leaving a sterilizer warms the cold feed going in.

**Flow arrangement:** in **parallel (co-current)** flow both fluids move in the same direction; in **counter-current** flow they move in opposite directions. Counter-current gives a larger average temperature difference and better heat recovery.

**Main types**

1. **Double-pipe exchanger:** one pipe inside another; one fluid in the inner pipe, the other in the annulus. Simple, for small duties.
2. **Shell-and-tube exchanger:** a bundle of tubes fixed in tube sheets inside a cylindrical shell. One fluid goes through the tubes, the other around them in the shell. **Baffles** in the shell make the shell fluid cross the tubes and increase turbulence.
   - *1-1 exchanger:* one shell pass, one tube pass.
   - *1-2 exchanger:* fluid in the tubes goes down and back (two passes), giving higher velocity and better transfer.
3. **Plate heat exchanger:** thin corrugated stainless steel plates clamped together; fluids flow in alternate channels. Very efficient, compact, easy to clean; used for milk, syrups, heat-sensitive liquids.

```text
 Shell-and-tube (1-2) exchanger

  steam in ↓            baffles
 ┌────────┬─┬───┬───┬───┬───┬─┐
 │ liquid │ ║   ║   ║   ║   ║ │══ tubes
 │ in  →  │═══════════════════│
 │ out ←  │═══════════════════│
 └────────┴─┴───┴───┴───┴───┴─┘
                    ↓ condensate out
```

## 2.2 Evaporation

**Evaporation** is the removal of a solvent (usually water) from a solution by boiling, to give a **concentrated liquid**. The vapour is normally discarded.

### Objectives and applications

- Concentrating plant extracts (liquid and dry extracts, e.g. liquorice, belladonna).
- Concentrating antibiotic broths and enzyme solutions before drying or crystallisation.
- Preparing syrups and concentrated solutions.
- Recovering solvents.
- Reducing volume before spray drying or freeze drying.

### Factors influencing evaporation

1. **Temperature:** higher temperature gives faster evaporation, but many drugs (enzymes, hormones, glycosides) decompose. Use the lowest temperature that works.
2. **Temperature and time of exposure together:** a high temperature for a very short time can be safer than a low temperature for hours (basis of film evaporators).
3. **Pressure:** reducing pressure lowers the boiling point, so thermolabile liquids can be evaporated at low temperature.
4. **Surface area:** larger area of heating and liquid surface means faster evaporation.
5. **Type of product:** some liquids foam (extracts with saponins), form scale on the tubes, or become very viscous as they concentrate; these need special evaporators.
6. **Concentration and viscosity:** as the liquid concentrates, boiling point rises and circulation slows.
7. **Vapour pressure and agitation:** removing the vapour above the liquid and stirring help.
8. **Economic factors:** cost of steam, reuse of vapour heat (multiple effect).

### Evaporation compared with other heat processes

| Process | What happens | Product kept |
| --- | --- | --- |
| Evaporation | Solvent boiled off from a solution | Concentrated liquid; vapour discarded |
| Distillation | Liquid vaporised and the vapour condensed | The condensed liquid (distillate) |
| Drying | Remaining moisture removed from a solid or semisolid | Dry solid |
| Crystallisation | Solid separated as crystals from solution | Crystals |

Evaporation usually stops at a concentrated liquid or thick extract; drying carries on to a solid.

### Steam jacketed kettle (evaporating pan)

**Principle:** steam in the jacket gives up its latent heat through the wall of the pan to the liquid, which boils off its water at atmospheric pressure.

**Construction:** a **hemispherical pan** (stainless steel, copper or enamelled iron) surrounded by an outer **jacket**. Steam enters the jacket at the top; condensate leaves through an outlet at the bottom with a steam trap; a vent removes air. The pan may be tilting and have a stirrer.

```text
            open top (vapour escapes)
       ┌───────────────────────────┐
 steam │╲     liquid              ╱│ ← jacket
  in → │ ╲                       ╱ │
       │  ╲_____________________╱  │
        ╲__________________________╱
                  ↓ condensate out
```

**Working:** steam is passed into the jacket, condenses and heats the pan. The liquid boils and its vapour escapes into the room or a hood.

**Uses:** concentrating aqueous, thermostable liquids (e.g. liquorice extract); preparing syrups and ointment bases.

**Merits:** simple, cheap, easy to clean and maintain; can be stirred.

**Demerits:** small heating area that shrinks as the level falls; open pan, so vapour fills the room and the product may be contaminated; works only at atmospheric pressure, so not for thermolabile or volatile solvents (unless closed); solids deposit and may burn on the wall.

### Horizontal tube evaporator

**Principle:** steam inside horizontal tubes heats the liquid surrounding them (natural circulation).

**Construction:** a vertical cylindrical body with a bundle of **horizontal tubes** in the lower part, steam chest at the ends. The tubes are covered by the liquid. A large vapour space above; a dome at the top to separate entrained droplets.

**Working:** steam passes through the tubes and condenses; the liquid outside boils; vapour rises and leaves at the top; concentrated liquid is drawn off at the bottom.

**Uses:** concentrating thin, non-viscous, non-scaling liquids.

**Merits:** cheap, simple, small headroom, easy to remove condensate from tubes.

**Demerits:** poor circulation, so not for viscous liquids; scale outside the tubes is hard to clean; not for foaming liquids.

### Climbing film (rising film, long tube vertical) evaporator

**Principle:** liquid boiling at the bottom of long vertical tubes forms vapour bubbles that rise fast and drag the liquid up the tube wall as a thin film. A thin film heats rapidly, so contact with heat is very short.

**Construction:** a bundle of **long vertical tubes** (several metres) inside a steam jacket (calandria). Feed enters at the bottom. At the top a **vapour–liquid separator** (cyclone or baffle) separates the concentrate from the vapour.

```text
             ┌─────────┐ → vapour to condenser
             │separator│
             └────┬────┘ → concentrate out
        ┌─────────┼─────────┐
 steam →│  ║  ║  ║  ║  ║   │ long vertical tubes
        │  ║  ║  ║  ║  ║   │ (film climbs the wall)
        └─────────┬─────────┘→ condensate
                  ↑ feed in
```

**Working:** feed enters the bottom and starts boiling; expanding vapour rushes up the centre of each tube carrying a film of liquid up the wall; the mixture enters the separator, where vapour goes to the condenser and concentrate is collected.

**Uses:** thermolabile solutions (insulin, liver extracts, vitamins), foaming liquids (the high vapour speed breaks foam).

**Merits:** very short residence time; high heat transfer coefficient; continuous; handles foaming liquids.

**Demerits:** needs a large temperature difference to start the film; tall (high headroom); not for very viscous or scaling liquids; hard to control the film.

### Forced circulation evaporator

**Principle:** a **pump** drives the liquid at high velocity through the heating tubes. High velocity gives a high heat transfer coefficient and prevents scale. Liquid is kept under pressure in the tubes so it does not boil there; it **flashes** into vapour when it enters the lower-pressure vapour head.

**Construction:** a calandria (vertical or horizontal tubes, steam outside), a **vapour head** (separator) and a **circulating pump** with connecting pipes.

**Working:** the pump sends liquid up through the tubes; it is heated; in the vapour head part of it flashes off as vapour; the rest returns to the pump with fresh feed; concentrate is withdrawn continuously.

**Uses:** viscous liquids, liquids that form scale or crystals, thermolabile liquids that need short heating.

**Merits:** high heat transfer even with viscous liquids; less scaling and fouling; good for crystallising solutions.

**Demerits:** costly pump and power; more maintenance (pump seals); liquid stays in the system a long time (hold-up).

### Multiple effect evaporator

**Principle:** the vapour produced in one evaporator (one **effect**) is used as the heating steam for the next effect, which is kept at a **lower pressure** so its liquid boils at a lower temperature. Latent heat is used again and again, so less fresh steam is needed.

**Construction:** two or more evaporators connected in series. Steam heats only the first effect; a condenser and vacuum pump on the last effect keep the pressure falling from first to last.

```text
  steam → [Effect 1] ─vapour→ [Effect 2] ─vapour→ [Effect 3] ─vapour→ condenser → vacuum
   (highest P, T)          (lower P, T)        (lowest P, T)
  feed →  ──────liquid──→  ──────liquid──→  → concentrate (forward feed)
```

**Methods of feeding:**

- **Forward feed:** feed and steam travel the same way (effect 1 → 3). No pumps needed between effects because pressure falls, but the most concentrated (most viscous) liquid is in the coldest effect.
- **Backward feed:** feed enters the last effect and moves to the first; pumps needed; the thickest liquid is in the hottest effect, good for viscous products.
- **Mixed feed:** a combination of both.
- **Parallel feed:** fresh feed to every effect; used when crystals form.

**Economy of multiple effect evaporator:**

**Economy = kg of water evaporated ÷ kg of steam supplied**

A single effect gives an economy slightly less than 1. With n effects the economy is roughly n times larger (a little less, because of losses and boiling point rise), so a triple effect gives about 2.5. **Capacity**, however, does not increase: the total temperature difference is shared between the effects, so a triple effect evaporates about as much per hour as a single effect with the same area per effect. Multiple effects save steam, not time.

**Uses:** large-scale evaporation where steam cost matters (sugar, salt, large extract plants).

**Merits:** large steam saving; low operating temperature in later effects. **Demerits:** high initial cost; complex control; more space.

## 2.3 Distillation

**Distillation** separates the components of a liquid mixture by vaporising the liquid and condensing the vapour. It works because components have different **volatilities**.

### Basic principles

- **Raoult's law:** the partial vapour pressure of a component in an ideal solution equals its mole fraction × vapour pressure of the pure component: pA = xA PA°.
- **Dalton's law:** total vapour pressure = sum of partial pressures; the mole fraction of A in the vapour is yA = pA / P.
- The vapour is richer in the more volatile component than the liquid. Repeated vaporisation and condensation improve the separation.
- **Relative volatility** α = (yA/xA) ÷ (yB/xB). Separation is easy if α is large; impossible if α = 1.
- **Azeotropes** are mixtures that boil at a constant composition (e.g. ethanol about 95.6% w/w with water); they cannot be separated by ordinary distillation.

```text
 Simple distillation set-up

        thermometer
            ┃
   ┌────────┸────┐ condenser (water out ↑)
   │  flask       ╲══════════════════╗
   │ (liquid)      ╲   ← water in    ║
   └──────────────┘                  ▼ receiver
        burner / mantle
```

### Simple distillation

**Principle:** the liquid is boiled and the vapour is condensed and collected in one step.

**Method:** a distillation flask, thermometer at the side arm, water condenser and receiver. Heat steadily; collect the distillate at its boiling point.

**Uses:** liquids with very different boiling points, or separating a volatile liquid from non-volatile solids; preparing purified water; recovering alcohol and solvents.

**Limitation:** cannot separate liquids with close boiling points.

### Flash (equilibrium) distillation

**Principle:** a liquid mixture is heated under pressure and then suddenly released into a separator at lower pressure. Part of it vaporises ("flashes") at once. The vapour and the remaining liquid are in equilibrium and are removed separately.

**Method:** pump the feed through a heater, then through a pressure-reducing valve into a separator; vapour leaves at the top to a condenser and liquid at the bottom. It is **continuous** and a single-stage separation.

**Uses:** separating components with widely different boiling points; multicomponent mixtures such as petroleum fractions; as a first step before fractionation.

### Fractional distillation (rectification)

**Principle:** used for liquids with **close boiling points**. Vapour rising through a **fractionating column** meets liquid flowing down. At each stage the vapour gets richer in the more volatile component and the liquid in the less volatile one. Part of the condensate is returned to the column as **reflux**.

**Method:** a still at the bottom, a column above it, condenser and reflux divider at the top. Columns are of two kinds:

- **Plate (tray) columns:** bubble-cap or sieve plates, each giving one stage of contact.
- **Packed columns:** filled with Raschig rings, Berl saddles or glass beads to give a large contact surface.

**Uses:** separating alcohol and water (up to the azeotrope), purifying organic solvents, separating volatile oil components, recovering solvents.

### Distillation under reduced pressure (vacuum distillation)

**Principle:** a liquid boils when its vapour pressure equals the external pressure. Lowering the pressure with a vacuum pump **lowers the boiling point**, so heat-sensitive liquids can be distilled without decomposition.

**Method:** a Claisen flask (two necks), a fine **capillary** that lets in a stream of tiny air bubbles to prevent bumping, condenser, receiver, manometer and vacuum pump. Heat with a water or oil bath, not a direct flame.

**Uses:** concentrating thermolabile extracts (e.g. in preparing dry extracts), purifying high-boiling liquids, recovering solvents from extracts.

### Steam distillation

**Principle:** for two **immiscible** liquids (e.g. water and a volatile oil), each exerts its own full vapour pressure regardless of the other. The mixture boils when the **sum** of the two vapour pressures equals atmospheric pressure, so it boils **below 100 °C** and below the boiling point of the oil. The oil distils with steam without decomposing.

Ratio of the two in the distillate:

**mA / mB = (pA × MA) / (pB × MB)**

where m is the mass, p the vapour pressure and M the molecular weight of each liquid. Because water has a low molecular weight, an oil of high molecular weight distils in useful amounts even though its vapour pressure is small.

**Method:** steam from a generator is passed into a flask containing the drug and water; the vapour mixture goes to a condenser; the distillate separates into an oil layer and a water layer (Florentine receiver).

**Uses:** extracting volatile oils (clove, eucalyptus, peppermint, cinnamon), preparing aromatic waters, purifying high-boiling substances insoluble in water.

### Molecular distillation

**Principle:** carried out at a very high vacuum (about 10⁻³ mm Hg or lower). The **distance between the evaporating surface and the condensing surface is less than the mean free path** of the molecules, so molecules leaving the hot surface travel straight to the cold surface without colliding with gas molecules. There is no boiling; the liquid is spread as a very thin film.

**Equipment:**

- **Falling film molecular still:** the liquid flows down the inner wall of a heated cylinder as a thin film; a cooled condenser sits a very short distance away.
- **Centrifugal molecular still:** liquid is fed to the centre of a rapidly spinning heated cone and spreads into an extremely thin film; vapour condenses on a nearby cooled surface.

**Uses:** purification of very heat-sensitive substances of high molecular weight: vitamin A and vitamin E from fish liver oils, refining oils, separating monoglycerides.

**Merits:** very low temperature and very short heating time. **Demerits:** expensive, very high vacuum needed, low throughput.

## Remember

- Conduction: Fourier's law, Q/t = −kA dT/dx. Convection: Q/t = hAΔT. Radiation: Q/t = εσAT⁴.
- Resistances in series add; 1/U = 1/h1 + x/k + 1/h2.
- Heat exchanger: steam/hot gas → process fluid. Heat interchanger: process fluid → process fluid.
- Counter-current flow gives better heat transfer than parallel flow.
- Climbing film = short contact, thermolabile and foaming liquids. Forced circulation = viscous and scaling liquids.
- Economy = water evaporated ÷ steam used; multiple effect raises economy, not capacity.
- Steam distillation works for immiscible liquids and boils below 100 °C; mA/mB = pA MA / pB MB.
- Molecular distillation: gap between surfaces less than the mean free path; vitamins A and E.
