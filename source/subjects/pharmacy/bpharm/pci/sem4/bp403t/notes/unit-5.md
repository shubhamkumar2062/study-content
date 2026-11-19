# Unit 5: Drug stability and reaction kinetics

**Stability** of a pharmaceutical product is its ability to stay within its specifications (identity, strength, quality and purity) throughout its shelf life, in the container in which it is sold. A product may become unsafe or ineffective because the drug degrades chemically (hydrolysis, oxidation, photolysis), because the dosage form changes physically (caking, cracking, crystal growth), or because microbes grow. This unit uses **chemical kinetics** (the study of reaction rates) to predict how fast a drug degrades and to set its **expiry date**.

**Key terms**

| Term | Meaning |
| --- | --- |
| Rate of reaction | Change in concentration of a reactant (or product) per unit time, −dC/dt |
| Rate constant (k) | Proportionality constant in the rate equation; fixed at a given temperature |
| Order of reaction | Sum of the exponents of the concentration terms in the rate equation (found by experiment) |
| Molecularity | Number of molecules taking part in a single elementary step (uni-, bi-, termolecular) |
| Half-life (t½) | Time for the concentration to fall to half its initial value |
| Shelf life (t90) | Time for the drug content to fall to 90% of the labelled amount (10% degradation), under stated storage conditions |
| Expiry date | The date, based on the shelf life, after which the product should not be used |

## 5.1 Zero-order reactions

The rate does **not depend on concentration**; the drug is lost at a constant rate.

−dA/dt = k0

Integrating: **A = A0 − k0t**

- A plot of **A against t is a straight line** with slope −k0.
- **Units of k0:** concentration/time (mol L⁻¹ s⁻¹, mg ml⁻¹ day⁻¹, % per month).
- **Half-life:** t½ = A0 / (2k0) (depends on the starting concentration).
- **Shelf life:** t90 = 0.1A0 / k0.

Examples: some solid-state reactions; photochemical reactions where light, not drug concentration, limits the rate; colour fading in some tablets; drug release from some controlled-release systems.

## 5.2 Pseudo (apparent) zero-order reactions: suspensions

In a **suspension**, only the dissolved drug degrades. As dissolved drug breaks down, more dissolves from the suspended particles, so the concentration in solution stays fixed at the **solubility (Cs)** as long as solid drug remains. The reaction, really first order in the dissolved drug, therefore appears zero order in total drug:

−d[A]/dt = k1[A]solution = k1Cs = k0

So **k0 = k1 × Cs**, and A = A0 − k0t.

**Worked example.** A suspension contains 5 g of drug per 100 ml. Solubility = 0.5 g/100 ml. The first-order rate constant in solution = 2 × 10⁻⁶ s⁻¹.
k0 = 2 × 10⁻⁶ × 0.5 = 1 × 10⁻⁶ g/100 ml per second.
t90 = 0.1A0/k0 = (0.1 × 5)/(1 × 10⁻⁶) = 5 × 10⁵ s = **5.8 days**.
If the drug had been in solution at 5 g/100 ml, t90 would be 0.105/(2 × 10⁻⁶) = 52,500 s (about 14.6 hours). Suspending the drug greatly extends shelf life; this is one reason unstable drugs are given as suspensions.

## 5.3 First-order reactions

The rate is proportional to the **concentration of one reactant**:

−dA/dt = kA

Integrating: **ln A = ln A0 − kt**, or **log A = log A0 − kt/2.303**, or **A = A0 e^(−kt)**

- A plot of **log A against t is a straight line** with slope −k/2.303.
- **Units of k:** time⁻¹ (s⁻¹, h⁻¹, day⁻¹), independent of concentration units.
- **Half-life:** t½ = 0.693/k (does **not** depend on initial concentration).
- **Shelf life:** t90 = 0.105/k (since 2.303 log(100/90) = 0.105).
- The rate constant can also be written k = (2.303/t) log (A0/A).

Most drug decompositions in solution (hydrolysis of esters in buffered solution, many oxidations) behave as first order or **pseudo-first order**: in hydrolysis, water is present in great excess and its concentration hardly changes, so the reaction follows first-order kinetics even though it is bimolecular.

**Worked example.** A drug solution containing 100 mg/ml falls to 80 mg/ml after 60 days at room temperature (first order).
k = (2.303/60) × log(100/80) = 0.03838 × 0.0969 = **3.72 × 10⁻³ day⁻¹**
t½ = 0.693/0.00372 = **186 days**; t90 = 0.105/0.00372 = **28 days**.

## 5.4 Second-order reactions

The rate depends on the concentrations of **two reactants** (or the square of one):

−dA/dt = k[A][B]

**When both concentrations are equal (a):**

1/(a − x) − 1/a = kt, or **k = x / [a t (a − x)]**

where x = amount reacted at time t.

- A plot of **1/(a − x) against t is a straight line**, slope = k.
- **Units of k:** concentration⁻¹ time⁻¹ (M⁻¹ s⁻¹, L mol⁻¹ s⁻¹).
- **Half-life:** t½ = 1/(ka) (inversely proportional to initial concentration).

**When the concentrations differ (a and b):**

k = [2.303 / (t(a − b))] × log [b(a − x) / (a(b − x))]

**Example of a second-order reaction:** alkaline hydrolysis (saponification) of ethyl acetate by sodium hydroxide: CH3COOC2H5 + NaOH → CH3COONa + C2H5OH.

**Worked example.** Ethyl acetate and NaOH, each 0.02 M, react with k = 5 M⁻¹ min⁻¹. t½ = 1/(5 × 0.02) = **10 min**. Doubling both concentrations to 0.04 M halves t½ to 5 min.

### Summary of orders

| Order | Integrated equation | Linear plot | Units of k | t½ | t90 |
| --- | --- | --- | --- | --- | --- |
| Zero | A = A0 − k0t | A vs t | conc time⁻¹ | A0/2k0 | 0.1A0/k0 |
| First | log A = log A0 − kt/2.303 | log A vs t | time⁻¹ | 0.693/k | 0.105/k |
| Second (equal conc.) | 1/(a − x) − 1/a = kt | 1/(a − x) vs t | conc⁻¹ time⁻¹ | 1/ka | 1/(9ka) |

(For second order, t90 = 0.1a/[ka × 0.9a] = 1/(9ka).)

## 5.5 Determination of the order of reaction

1. **Substitution method:** concentrations measured at various times are substituted into the integrated equation of each order. The equation that gives a **constant k** at all times shows the order.
2. **Graphical method:** plot A, log A and 1/(a − x) against t. The plot that gives a **straight line** shows the order (zero, first or second respectively).
3. **Half-life method:** for a reaction of order n, t½ ∝ 1/a^(n−1). With two starting concentrations a1 and a2:

   n = 1 + log(t½,1 / t½,2) / log(a2 / a1)

   **Worked example.** t½ = 40 min when a = 0.1 M and 20 min when a = 0.2 M. n = 1 + log(40/20)/log(0.2/0.1) = 1 + 0.301/0.301 = **2** (second order). If t½ had not changed with a, the reaction would be first order.
4. **Initial rate method:** the initial rate is measured at different starting concentrations; rate = k[A]ⁿ, so the slope of log(rate) vs log[A] gives n.

## 5.6 Factors influencing chemical degradation

### Temperature

The rate of most reactions rises with temperature. The **Arrhenius equation**:

k = A e^(−Ea/RT), or **log k = log A − Ea / (2.303 RT)**

where A = frequency factor, Ea = activation energy, R = gas constant (1.987 cal mol⁻¹ K⁻¹ or 8.314 J mol⁻¹ K⁻¹), T = absolute temperature. A plot of **log k against 1/T** is a straight line with slope −Ea/(2.303R).

For two temperatures:

log (k2/k1) = Ea (T2 − T1) / (2.303 R T1 T2)

**Worked example.** A drug degrades by first-order kinetics with k = 0.020 day⁻¹ at 60 °C (333 K) and 0.050 day⁻¹ at 70 °C (343 K).
log(0.050/0.020) = log 2.5 = 0.398.
Ea = 0.398 × 2.303 × 1.987 × 333 × 343 / (343 − 333) = 0.398 × 4.576 × 114,219 / 10 ≈ **20,800 cal/mol (20.8 kcal/mol)**.
At 25 °C (298 K): log k25 = log 0.020 − 20,800 × (333 − 298)/(2.303 × 1.987 × 333 × 298) = −1.699 − 1.603 = −3.302, so k25 = **5.0 × 10⁻⁴ day⁻¹**.
Shelf life at 25 °C: t90 = 0.105/0.0005 = **210 days** (about 7 months).

**Q10 approach.** Q10 is the factor by which the rate constant rises for a 10 °C rise in temperature. For activation energies typical of drug degradation, Q10 is roughly 2 to 4 near room temperature. The shelf life at a new temperature: t90(T2) = t90(T1) / Q10^(ΔT/10). **Example:** a product with t90 = 2 years at 25 °C, stored at 35 °C with Q10 = 3, has t90 = 2/3 years = 8 months. Q10 is useful for a quick estimate (for example, the effect of a temperature excursion during transport).

### Solvent and dielectric constant

For a reaction between two ions A and B, the effect of the solvent's dielectric constant (ε) is:

log k = log k(ε=∞) − K ZA ZB / ε

where ZA and ZB are the charges on the ions and K is a constant for the reaction at a given temperature. A plot of log k against 1/ε is linear.

- **Ions of the same sign** (ZA ZB positive): lowering ε (adding alcohol, glycerin, propylene glycol to water) **decreases** the rate.
- **Ions of opposite sign** (ZA ZB negative): lowering ε **increases** the rate.

Replacing water with a less polar solvent also lowers the concentration of water itself, which slows hydrolysis; but the result must be checked, because the dielectric effect may oppose it. Solvents can also change the pKa and solubility of a drug.

### Ionic strength (primary salt effect)

In dilute aqueous solution at 25 °C, the **Brønsted–Bjerrum equation** gives:

log k = log k0 + 1.02 ZA ZB √µ

where k0 = rate constant at zero ionic strength and µ = ionic strength = ½Σ cᵢzᵢ². At higher ionic strengths √µ is replaced by √µ/(1 + √µ).

- **Same-sign ions:** rate **increases** with ionic strength.
- **Opposite-sign ions:** rate **decreases**.
- **Ion and neutral molecule:** little effect in dilute solution.

**Worked example.** Reaction between two univalent ions of the same sign (ZA ZB = +1) at µ = 0.01: log(k/k0) = 1.02 × 1 × 0.1 = 0.102, so k/k0 = **1.26** (26% faster than at zero ionic strength). Buffer salts, isotonic sodium chloride and other electrolytes added to a formulation can therefore change the degradation rate.

### Specific and general acid–base catalysis

**Specific acid–base catalysis:** the reaction is catalysed only by **H⁺ (H3O⁺)** or **OH⁻** ions. The rate depends on pH but not on the concentration of the buffer used to hold that pH. The observed first-order rate constant is:

kobs = k0 + kH[H⁺] + kOH[OH⁻]

where k0 is the rate due to water (solvent) alone. A plot of log kobs against pH (the **pH–rate profile**) shows the pH at which the drug is most stable.

```text
 log k ^
       | \                         /
       |  \ acid-catalysed        / base-catalysed
       |   \ (slope -1)          / (slope +1)
       |    \                   /
       |     \_______________ /
       |        region where water (k0) dominates
       |            ^ pH of maximum stability
       +--------------------------------------> pH
   (V-shaped or U-shaped profile; for example, many esters)
```

**General acid–base catalysis:** the reaction is also catalysed by the **other acids and bases present**, such as the components of the buffer (acetate, phosphate, citrate, borate). At constant pH and ionic strength, the rate **rises with buffer concentration**. To test for it, the reaction is run at the same pH with several buffer concentrations (keeping ionic strength constant); if k changes, general catalysis is present.

**Practical meaning:** choose the pH of maximum stability (if compatible with solubility, comfort and activity) and use the **lowest effective buffer concentration**, choosing a buffer that does not catalyse the reaction.

### Other factors

Light (photolysis), oxygen (oxidation), moisture (solid dosage forms), trace metal ions (catalyse oxidation), presence of other drugs and excipients, and the container (alkali from glass, sorption into plastics).

## 5.7 Stabilisation against hydrolysis

**Hydrolysis** is the reaction of a drug with water; it is the most common cause of degradation of drugs in liquid dosage forms.

| Labile group | Example drugs |
| --- | --- |
| Esters | Aspirin, procaine, benzocaine, atropine, physostigmine |
| Amides | Chloramphenicol, paracetamol (slow), lidocaine (very stable) |
| Lactams | Penicillins, cephalosporins |
| Imides and others | Barbiturates |

**Methods of preventing hydrolysis**

1. **pH control with buffers:** formulate at the pH of maximum stability found from the pH–rate profile.
2. **Reducing water:** supply as dry powders for reconstitution (antibiotic syrups, injections), use non-aqueous or mixed solvents, protect solid dosage forms from moisture with desiccants and suitable packaging, use film coating.
3. **Suspensions:** keep most of the drug undissolved (apparent zero order, see 5.2), or use a less soluble salt or ester.
4. **Complexation:** a complexing agent can shield the labile group; for example, caffeine complexed with benzocaine slows its hydrolysis.
5. **Micelles (surfactants):** a drug held inside micelles is protected from attack by water or OH⁻; benzocaine in solutions of nonionic surfactants is an example.
6. **Low temperature:** refrigerated storage of products such as some reconstituted antibiotics and insulin.
7. **Choice of solvent with suitable dielectric constant** (see 5.6).

## 5.8 Stabilisation against oxidation

**Oxidation** is the loss of electrons or hydrogen (or gain of oxygen). In pharmaceuticals it is usually **autoxidation**, a free-radical chain reaction with atmospheric oxygen:

```text
 Initiation:   RH  --(light, heat, metal ions)-->  R•  + H•
 Propagation:  R•  + O2   -->  ROO•
               ROO• + RH  -->  ROOH + R•    (chain continues)
 Termination:  R• + R•  or  ROO• + R•  -->  stable products
               (antioxidants donate H and end the chain)
```

**Drugs easily oxidised:** adrenaline (epinephrine; turns pink to brown), ascorbic acid, phenothiazines, morphine, vitamins A and E, unsaturated fixed oils (rancidity), aldehydes, phenols.

**Methods of preventing oxidation**

1. **Antioxidants**
   - **Reducing agents** (oxidised in preference to the drug): water soluble, such as sodium metabisulfite, sodium bisulfite, sodium sulfite, ascorbic acid, thioglycerol.
   - **Chain-breaking antioxidants** (block the free-radical chain): oil soluble, such as butylated hydroxyanisole (BHA), butylated hydroxytoluene (BHT), propyl gallate, tocopherols.
   - **Synergists and chelating agents** (bind trace metals that catalyse oxidation): disodium edetate, citric acid, tartaric acid.
2. **Removing oxygen:** replace air in the container with nitrogen or carbon dioxide; boil water to remove dissolved oxygen.
3. **pH control:** many oxidations are faster at higher pH (adrenaline is more stable in acidic solution).
4. **Protection from light** (light starts the chain).
5. **Low temperature storage.**
6. **Avoid metal contamination** (from equipment and containers).

## 5.9 Photolytic degradation and its prevention

**Photolysis** is degradation by light, mainly ultraviolet and the shorter visible wavelengths. The drug (or an impurity or excipient) absorbs light and is excited to a reactive state, which may decompose directly or produce free radicals and oxidation.

**Light-sensitive drugs:** nifedipine and other dihydropyridines, riboflavin, sodium nitroprusside, phenothiazines (chlorpromazine), ergometrine, vitamin A, furosemide, hydrocortisone and prednisolone in solution, many dyes.

**Prevention**

| Method | Example |
| --- | --- |
| Amber or coloured glass | Cuts out UV and short visible wavelengths |
| Opaque containers and outer cartons | Tablets in cartons, foil blisters |
| Opaque coatings | Film coat containing titanium dioxide or iron oxide pigments |
| Light-absorbing additives | UV absorbers in the product or container |
| Protection during use | Infusion bags covered with light-proof bags (sodium nitroprusside) |
| Antioxidants | Where photolysis proceeds through free radicals |

Photostability testing (ICH Q1B) exposes the drug and product to a defined amount of light to check whether light-resistant packaging is needed.

## 5.10 Accelerated stability testing and expiration dating

Testing a product at room temperature until it degrades would take years. **Accelerated stability testing** stores the product at **elevated temperatures** (and humidity, light) so that degradation is faster, measures the rate constants, and uses the **Arrhenius equation** to predict the rate, and so the shelf life, at the normal storage temperature.

### Procedure (Arrhenius method)

1. Store samples at several high temperatures, for example 40, 50, 60 and 70 °C.
2. At intervals, assay the remaining drug at each temperature.
3. Find the order of reaction (for example, plot log % remaining against time; a straight line = first order) and the rate constant k at each temperature from the slope.
4. Plot **log k against 1/T** and extrapolate the straight line to the storage temperature (for example 25 °C, i.e. 1/298 K⁻¹).
5. Read k at the storage temperature and calculate t90 = 0.105/k (first order).

```text
 log k ^
       | o  70 °C
       |   o  60 °C
       |     o  50 °C
       |       o  40 °C
       |         .
       |           .   extrapolated
       |             x  k at 25 °C
       +----------------------------> 1/T (K⁻¹)
```

**Free and Blythe method:** instead of k, the time for a fixed percentage of degradation at each temperature is plotted (log t against 1/T) and extrapolated.

### Limitations of accelerated testing

- Valid only if the **mechanism (and order) is the same** at high and low temperature. A reaction with a different pathway at high temperature gives wrong predictions.
- Not suitable for **physical instability**: suspensions and emulsions may break, gels may liquefy, ointments may melt, polymorphic changes may differ at high temperature.
- Not for reactions controlled by diffusion or photochemistry, or for microbial or enzymatic degradation (proteins and enzymes denature at high temperature).
- Moisture loss or gain and evaporation at high temperature may change the system.
- Products that degrade faster at low temperatures (some freeze-related problems) are not covered.
- The result is an estimate; it must be confirmed by **real-time (long-term) stability data**.

### Regulatory storage conditions (ICH and WHO)

| Study | Typical condition | Minimum duration at submission |
| --- | --- | --- |
| Long-term (zone I/II) | 25 °C ± 2 °C / 60% RH ± 5% RH | 12 months |
| Long-term (hot, very humid zone IVb, which includes India) | 30 °C ± 2 °C / 75% RH ± 5% RH | 12 months |
| Intermediate | 30 °C ± 2 °C / 65% RH ± 5% RH | 6 months |
| Accelerated | 40 °C ± 2 °C / 75% RH ± 5% RH | 6 months |

A "significant change" at accelerated conditions (for example, 5% loss of assay from the initial value, or failure to meet specifications) leads to testing at intermediate conditions. Final expiry dates are set from real-time data at the long-term condition of the market, with the label stating storage conditions (for example, "Store below 30 °C, protect from light and moisture").

### Physical stability tests for dosage forms

Besides chemical assay, stability programmes check appearance, colour, odour, pH, viscosity, sedimentation volume and redispersibility (suspensions), creaming and globule size (emulsions), hardness, friability, disintegration and dissolution (tablets), and microbial limits and preservative content (liquids). Freeze–thaw cycling is used to stress emulsions and suspensions.

## Remember

- Zero order: A = A0 − k0t, t½ = A0/2k0, t90 = 0.1A0/k0; suspensions show pseudo-zero order, k0 = k1Cs.
- First order: log A = log A0 − kt/2.303, t½ = 0.693/k, t90 = 0.105/k, k in time⁻¹.
- Second order: 1/(a − x) − 1/a = kt, t½ = 1/ka, k in M⁻¹ time⁻¹ (ethyl acetate + NaOH).
- Order: substitution, graphs (A, log A, 1/(a − x) vs t), half-life method n = 1 + log(t1/t2)/log(a2/a1).
- Arrhenius: log k2/k1 = Ea(T2 − T1)/(2.303RT1T2); plot log k vs 1/T; Q10 about 2–4.
- Dielectric: log k = log k∞ − KZAZB/ε; ionic strength: log k = log k0 + 1.02ZAZB√µ.
- Specific catalysis: H⁺/OH⁻ only; general catalysis: buffer species too (rate rises with buffer concentration at constant pH).
- Hydrolysis: buffers, less water, suspensions, complexation, micelles, cold. Oxidation: antioxidants, nitrogen, chelators, pH, light protection.
- Photolysis: amber glass, opaque packs, TiO2 coating, cartons.
- Accelerated testing: high temperatures → k → log k vs 1/T → extrapolate → t90; confirm with real-time data; accelerated condition 40 °C/75% RH.
