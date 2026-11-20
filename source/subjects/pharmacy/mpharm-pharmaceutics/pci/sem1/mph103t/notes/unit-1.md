# Unit 1: Preformulation, stability, pharmaceutical dispersions and parenterals

This unit covers syllabus item 1(a): preformulation concepts, drug–excipient interactions and the methods used to detect them, kinetics of stability and stability testing, theories of dispersion, emulsions, suspensions and SMEDDS, and small and large volume parenterals. At B.Pharm level you learnt *what* preformulation measures; at M.Pharm level the examiner expects *why* each test matters, the mechanism behind each failure, the equations, and the regulatory framework (ICH Q1A(R2), Q1B, Q8–Q10).

## 1.1 Preformulation concepts

**Preformulation** is the investigation of the physical, chemical and biopharmaceutical properties of a drug substance, alone and in combination with excipients, done before formulation development so that a stable, bioavailable and manufacturable dosage form can be designed with the least trial and error.

In modern development it is the first block of **Quality by Design (QbD)**: preformulation data identify the drug's **critical material attributes** (particle size, polymorph, salt form, hygroscopicity, impurity profile) that will later be linked to the **critical quality attributes** of the product.

### Stages and decisions

```text
New drug substance (small quantity, often < 1 g at first)
   │
   ├─ Identity and purity: HPLC, impurity profile, residual solvents
   ├─ Solid state: crystal form, polymorph screen, amorphous content, hydrates
   ├─ Solution properties: pKa, intrinsic solubility, pH–solubility profile, log P / log D
   ├─ Solid and solution stability: pH–rate profile, forced degradation
   ├─ Powder properties: particle size, shape, density, flow, compressibility
   ├─ Biopharmaceutics: permeability (Caco-2), BCS class, dissolution rate
   └─ Compatibility with candidate excipients
   ↓
Decisions: salt / polymorph to develop, dosage form, process (DC vs wet granulation),
excipient short-list, pack, storage conditions, analytical methods
```

### Key parameters and their meaning

| Parameter | Method | Why it matters |
| --- | --- | --- |
| pKa | Potentiometric or UV titration, solubility–pH method | Predicts ionisation, solubility and absorption along the gut (pH-partition) |
| Intrinsic solubility (S0) and pH–solubility | Shake-flask, HPLC assay | S = S0[1 + 10^(pH − pKa)] for a weak acid; decides salt need |
| log P / log D | Shake-flask octanol–water, HPLC retention | Membrane permeability; log D at pH 7.4 is more useful for ionisable drugs |
| Intrinsic dissolution rate | Fixed-area compressed disc (Wood's apparatus) | Rate per cm² independent of particle size; values below about 0.1 mg/cm²/min often mean dissolution-limited absorption |
| Polymorphs, hydrates, amorphous form | DSC, TGA, PXRD, hot-stage microscopy, FTIR/Raman, solid-state NMR | Solubility and stability differ; risk of form change during milling, granulation or storage |
| Hygroscopicity | Dynamic vapour sorption (DVS) | Choice of process, excipients and pack |
| Particle size and shape | Laser diffraction, microscopy | Content uniformity, dissolution, flow |
| Flow and compressibility | Carr's index, Hausner ratio, angle of repose, Heckel analysis | Direct compression versus granulation (see Unit 5–6) |

**BCS (Biopharmaceutics Classification System):** Class I high solubility–high permeability, II low solubility–high permeability, III high solubility–low permeability, IV low–low. "High solubility" means the highest single therapeutic dose dissolves in 250 ml or less of aqueous media over pH 1.2–6.8 at 37 °C (ICH M9). Class II drugs gain most from formulation tools such as salt formation, particle size reduction, solid dispersions and lipid systems such as SMEDDS.

## 1.2 Drug–excipient interactions

An excipient is not inert: it can change the chemical stability, physical form or release of the drug. Interactions are of two kinds.

**Physical interactions** — no new chemical bond, but performance changes:

- Adsorption of the drug on a high-surface excipient (drug on talc, colloidal silica or activated charcoal), lowering dissolution.
- Complexation (tetracycline with calcium or magnesium salts; drugs with cyclodextrins, which may be wanted).
- Change of polymorph or loss of crystallinity during processing with an excipient.
- Eutectic formation, lowering melting point and causing sticking.
- Lubricant film: over-mixed magnesium stearate coats granules and slows dissolution and lowers hardness.

**Chemical interactions** — a new chemical species forms:

| Interaction | Mechanism | Example |
| --- | --- | --- |
| Maillard reaction | Reducing sugar carbonyl + primary or secondary amine → glycosylamine → brown Amadori products | Lactose with amine drugs (for example fluoxetine and amlodipine) |
| Base-catalysed hydrolysis | Alkaline lubricant raises micro-environmental pH | Magnesium stearate with aspirin |
| Oxidation by peroxide impurities | Hydroperoxides in povidone, crospovidone, polysorbates, PEG | Oxidation of drugs with sulphide or amine groups |
| Transesterification / esterification | Ester exchange with PEG or with citric/tartaric acid | Drugs with ester or hydroxyl groups |
| Acid–base reaction | Acidic drug with basic excipient (or reverse) | Salt disproportionation in tablets |
| Reaction with aldehyde impurities | Formaldehyde or furfural traces | Gelatin cross-linking in capsules, slowing dissolution |

**The micro-environmental pH** idea is important: in a solid dosage form the "pH" that matters is that of the thin water layer adsorbed on particles, set mainly by the excipients. That is why a drug stable in a buffered solution may still degrade in a tablet.

### Methods to detect interactions

1. **Differential scanning calorimetry (DSC):** 1:1 physical mixtures of drug and excipient are heated and compared with the pure components. Disappearance or shift of the drug melting peak, new peaks, or changes in enthalpy suggest interaction. Fast, needs milligrams, but a change in DSC may be only a physical (dissolution of drug in a molten excipient) event, so it is a *screen*, not proof.
2. **Isothermal stress testing (IST):** binary mixtures (often with about 5–20% added water) are stored at elevated temperature (for example 40–60 °C) for 1–4 weeks and assayed by HPLC for loss of drug and new degradants. More reliable than DSC because it measures real chemical change.
3. **FTIR / Raman:** shifts or loss of characteristic bands (carbonyl, amine, hydroxyl) indicate bonding or salt formation.
4. **Powder X-ray diffraction (PXRD):** detects change of crystal form or loss of crystallinity.
5. **HPLC / LC–MS:** identifies and quantifies degradants, gives kinetic data.
6. **Thermogravimetry (TGA), hot-stage microscopy, solid-state NMR, isothermal microcalorimetry:** microcalorimetry detects very slow reactions at near-ambient temperature from heat flow.
7. **Statistical (factorial) compatibility screens:** instead of one-by-one binary mixtures, a fractional factorial design of prototype mixtures shows which excipient causes the change (see Unit 2).

## 1.3 Kinetics of stability

### Orders of reaction

| Order | Rate law | Integrated form | Half-life | Shelf life (t90) |
| --- | --- | --- | --- | --- |
| Zero | −dC/dt = k0 | C = C0 − k0t | t½ = C0/(2k0) | t90 = 0.1C0/k0 |
| First | −dC/dt = k1C | ln C = ln C0 − k1t | t½ = 0.693/k1 | t90 = 0.105/k1 |
| Second (equal concentrations) | −dC/dt = k2C² | 1/C = 1/C0 + k2t | t½ = 1/(k2C0) | t90 = 0.11/(k2C0) |

**Apparent (pseudo) zero order:** in a suspension only the dissolved drug degrades, and the solution stays saturated because solid keeps dissolving, so the rate k0 = k1 × Cs is constant until the solid is used up.

**Pseudo-first order:** hydrolysis is truly second order (drug + water) but water is in such excess that its concentration does not change, so the rate looks first order.

### Factors affecting degradation rate

- **pH:** specific acid catalysis (H+), specific base catalysis (OH−) and general acid–base catalysis by buffer species. The observed rate kobs = k0 + kH[H+] + kOH[OH−] + buffer terms. Plotting log kobs against pH gives a **pH–rate profile** (V-shaped, U-shaped, sigmoid or bell-shaped) whose minimum gives the pH of maximum stability for the product.
- **Temperature:** Arrhenius equation (below).
- **Ionic strength:** primary salt effect (Brønsted–Bjerrum): log k = log k0 + 1.02 zAzB√μ in water at 25 °C; ions of like charge react faster at higher ionic strength.
- **Dielectric constant of solvent:** reactions between ions of opposite charge are slowed by raising the dielectric constant.
- **Moisture, oxygen, light, metal ions** (catalysing oxidation) and the excipients described above.

### Arrhenius equation and accelerated prediction

k = A·e^(−Ea/RT), or ln k = ln A − Ea/(RT).

A plot of ln k against 1/T (T in kelvin) is a straight line with slope −Ea/R. Extrapolating to the storage temperature gives k there and hence the predicted shelf life.

**Worked example.** First-order rate constants for a drug in solution were 0.0042 day⁻¹ at 50 °C, 0.0105 day⁻¹ at 60 °C and 0.0250 day⁻¹ at 70 °C. Predict t90 at 25 °C.

| T (°C) | T (K) | 1/T (K⁻¹) | k (day⁻¹) | ln k |
| --- | --- | --- | --- | --- |
| 50 | 323.15 | 0.003095 | 0.0042 | −5.473 |
| 60 | 333.15 | 0.003002 | 0.0105 | −4.556 |
| 70 | 343.15 | 0.002914 | 0.0250 | −3.689 |

Least-squares slope = −9,890 K, so Ea = 9,890 × 8.314 = **about 82 kJ/mol**. Intercept ln A = 25.13. At 298.15 K: ln k = 25.13 − 9,890/298.15 = −8.04, so k25 = **3.2 × 10⁻⁴ day⁻¹** and t90 = 0.105/k25 = **about 326 days (just under 11 months)**. The prediction must be confirmed by real-time data, because the mechanism may change with temperature.

**Limitations of accelerated prediction:** valid only if the degradation mechanism and order do not change across the temperature range; not valid for physical changes (melting of a suppository base, protein denaturation, emulsion cracking, polymorph conversion), for evaporative loss, or where moisture content changes with temperature in a solid. Diffusion-controlled solid-state reactions often do not obey Arrhenius behaviour.

**Q10 method** (quick estimate without full data): Q10 = k(T+10)/kT, often taken as 2, 3 or 4. Shelf life at a lower temperature ≈ shelf life at the higher temperature × Q10^(ΔT/10).

## 1.4 Stability testing (ICH Q1A(R2) and related guidelines)

**Stability** is the capacity of a drug product to remain within its specifications of identity, strength, quality and purity throughout its shelf life in the proposed container. Stability testing provides evidence of how quality varies with time under temperature, humidity and light, and fixes the re-test period of the drug substance and the shelf life and storage conditions of the product.

### Types of stability study

- **Stress (forced degradation) testing** on the drug substance: heat, humidity, acid and base hydrolysis, oxidation (for example hydrogen peroxide) and light. Purpose: find degradation pathways and prove that the assay method is **stability-indicating**.
- **Accelerated testing**, **intermediate testing** and **long-term (real-time) testing** on at least three primary batches (pilot scale or larger) in the proposed pack.
- **Photostability testing (ICH Q1B):** overall illumination not less than 1.2 million lux hours and integrated near-UV energy not less than 200 watt-hours/m².
- **In-use stability** (multi-dose products after opening), **ongoing (commitment) stability** on production batches, and stability for post-approval changes.
- **Bracketing and matrixing (ICH Q1D):** reduced designs that test extremes of strength/fill (bracketing) or a planned subset of samples at each time point (matrixing).

### Storage conditions for the general case (ICH Q1A(R2))

| Study | Condition | Minimum period at submission |
| --- | --- | --- |
| Long term | 25 °C ± 2 °C / 60% RH ± 5% RH **or** 30 °C ± 2 °C / 65% RH ± 5% RH | 12 months |
| Intermediate | 30 °C ± 2 °C / 65% RH ± 5% RH | 6 months |
| Accelerated | 40 °C ± 2 °C / 75% RH ± 5% RH | 6 months |

Intermediate testing is needed only when long term is 25 °C/60% RH and a "significant change" occurs at accelerated conditions. Products for refrigerator storage use 5 °C ± 3 °C long term and 25 °C/60% RH accelerated.

**Climatic zones:** I temperate, II subtropical/Mediterranean, III hot–dry, IVa hot–humid, IVb hot–very humid. India is generally treated as **zone IVb**, for which WHO guidance gives long-term conditions of 30 °C ± 2 °C / 75% RH ± 5% RH. This is why Indian packs often carry "Store below 30 °C".

**Testing frequency (long term):** every 3 months in the first year, every 6 months in the second year and annually after that; accelerated at least 0, 3 and 6 months.

**"Significant change"** for a product includes: 5% change in assay from initial value; any degradant exceeding its acceptance criterion; failure of appearance, physical attributes or functionality tests; failure of pH; failure of dissolution for 12 units.

**Parameters tested:** assay, degradation products, dissolution, appearance, hardness/friability (tablets), moisture, pH, viscosity and redispersibility (liquids), microbial limits, preservative content and preservative efficacy, sterility and particulate matter for injections, container–closure integrity.

**Shelf-life assignment:** the time at which the one-sided 95% confidence limit of the mean degradation curve meets the specification limit (ICH Q1E statistical evaluation). Limited extrapolation beyond real-time data is allowed only when supported by accelerated data.

## 1.5 Theories of dispersion

A **dispersion** is a system in which one phase (dispersed phase) is distributed as particles or droplets through another (continuous phase or dispersion medium). Suspensions (solid in liquid, particles usually above about 1 µm) and emulsions (liquid in liquid) are **coarse dispersions**; they are thermodynamically unstable because they have a large interfacial area and therefore a high interfacial free energy: ΔG = γ·ΔA.

### Theories of emulsification

1. **Surface (interfacial) tension theory:** emulsifiers lower the interfacial tension γ, so less work (γΔA) is needed to create the droplet surface, and coalescence has a smaller driving force.
2. **Oriented wedge theory:** emulsifier molecules orient at the interface with their hydrophilic end in water and lipophilic end in oil; the bulkier, more soluble end lies in the continuous phase, curving the film. Monovalent soaps (sodium oleate) favour o/w; divalent soaps (calcium oleate, two hydrocarbon chains) favour w/o.
3. **Interfacial film theory:** the emulsifier forms a barrier film around each droplet. Types of film:
   - **Monomolecular film** — surfactants (Tweens, Spans, sodium lauryl sulphate); a mixture of a water-soluble and an oil-soluble surfactant packs more tightly (complex film).
   - **Multimolecular film** — hydrophilic colloids (acacia, gelatin) form a thick, viscous film that resists coalescence mechanically.
   - **Solid particle film** — finely divided solids (bentonite, aluminium hydroxide) wetted by both phases collect at the interface (Pickering emulsions); the phase that wets the solid better becomes the continuous phase.
4. **Electrical double layer and DLVO theory:** charged droplets or particles repel; stability results from the balance of van der Waals attraction and electrostatic repulsion.

### DLVO theory (Derjaguin–Landau–Verwey–Overbeek)

Total potential energy of interaction VT = VA + VR, where VA (attraction) falls off with distance and VR (repulsion) depends on the surface potential and the thickness of the double layer (1/κ, which shrinks as electrolyte is added).

```text
Potential energy
  ↑            ___  primary maximum (energy barrier)
  |           /   \
  |          /     \______________
  |---------/------------\____/------→ distance between particles
  |        |              secondary minimum (loose, reversible flocs)
  |        |
  ↓   primary minimum (close contact: irreversible aggregation / caking)
```

- A high primary maximum keeps particles apart (deflocculated).
- Particles caught in the **secondary minimum** form loose flocs that redisperse easily — the basis of **controlled flocculation**.
- Electrolyte compresses the double layer, lowers the barrier and favours flocculation (Schulze–Hardy rule: flocculating power rises steeply with counter-ion valency).
- **Steric stabilisation** by adsorbed polymers or non-ionic surfactants adds a non-electrostatic repulsion, useful in high-ionic-strength products.

### Zeta potential

The potential at the shear plane between the fixed (Stern) layer and the mobile diffuse layer, measured from electrophoretic mobility. High magnitude (often quoted as beyond about ±30 mV) means a deflocculated, electrostatically stable system; lowering it to a small value with electrolytes produces controlled flocculation.

## 1.6 Suspensions: preparation and stability

**Stokes' law:** v = d²(ρs − ρo)g / 18η

**Worked example:** particles of 10 µm diameter (d = 10⁻³ cm), density 1.3 g/cm³, in water (1.0 g/cm³, η = 0.01 poise): v = (10⁻³)² × 0.3 × 981 / (18 × 0.01) = 1.6 × 10⁻³ cm/s ≈ 5.9 cm per hour. Raising the vehicle viscosity to 5 cP (0.05 poise) cuts this to about 1.2 cm per hour. Halving particle size cuts velocity four-fold.

### Flocculated versus deflocculated suspensions

| Property | Deflocculated | Flocculated |
| --- | --- | --- |
| Particles | Separate | Loose aggregates (flocs) |
| Sedimentation rate | Slow | Fast |
| Sediment | Closely packed, may form a cake | Loose, large volume, easily redispersed |
| Supernatant | Cloudy | Clear |
| Appearance | Elegant for longer | Less elegant |

**Approach used in practice:** controlled flocculation with electrolytes, surfactants or polymers, then a **structured vehicle** (suspending agents such as methylcellulose, sodium CMC, xanthan gum, bentonite, carbomer — pseudoplastic or thixotropic) to slow settling of the flocs.

**Evaluation parameters:**

- Sedimentation volume F = Vu/V0 (ultimate sediment volume ÷ original suspension volume). Example: 45 ml sediment in a 50 ml suspension gives F = 0.9.
- Degree of flocculation β = F/F∞, where F∞ is the sedimentation volume of the deflocculated system.
- Redispersibility (number of inversions), rheology, zeta potential, particle size growth (Ostwald ripening, crystal growth, polymorphic change), drug content uniformity on shaking.

**Preparation:** wetting of hydrophobic powder with a wetting agent or glycerin (levigation), dispersion of suspending agent, mixing, homogenisation or colloid milling, controlled flocculation, final volume. Large-scale: precipitation methods (solvent change, pH change, double decomposition) can also produce fine particles.

## 1.7 Emulsions: preparation and stability

**Choice of emulsifier — HLB system.** HLB 3–6 favours w/o, 8–18 favours o/w. Each oil has a "required HLB" for an o/w emulsion. A blend of two surfactants gives HLB = f × HLB_A + (1 − f) × HLB_B.

**Worked example:** required HLB 12 using Tween 80 (HLB 15.0) and Span 80 (HLB 4.3): f(Tween) = (12 − 4.3)/(15.0 − 4.3) = 0.72, so about **72% Tween 80 and 28% Span 80** by weight of the emulsifier blend.

**Preparation methods:** dry gum (continental, 4:2:1 oil:water:gum for fixed oils), wet gum (English), bottle method (volatile oils), in-situ soap method, and at industrial scale phase inversion and high-pressure homogenisation or microfluidisation.

**Instabilities:**

| Instability | Reversible? | Cause and control |
| --- | --- | --- |
| Creaming / sedimentation | Yes | Density difference, large droplets; reduce droplet size, raise viscosity, match densities |
| Flocculation | Usually yes | Weak attraction; control zeta potential |
| Coalescence → cracking (breaking) | No | Film rupture; adequate emulsifier, avoid incompatible additives, temperature extremes, microbial attack |
| Ostwald ripening | No | Small droplets dissolve into large ones (higher solubility of small droplets); add a poorly water-soluble oil |
| Phase inversion | — | o/w changes to w/o on changing phase volume ratio (above about 74% internal phase), temperature (PIT for non-ionic surfactants) or adding a divalent ion |

**Evaluation:** droplet size distribution (microscopy, laser diffraction), zeta potential, viscosity, phase separation after centrifugation, freeze–thaw cycling, conductivity (to identify o/w), dilution and dye tests.

## 1.8 Self-micro-emulsifying drug delivery systems (SMEDDS)

**SMEDDS** are isotropic mixtures of oil, surfactant (usually non-ionic with HLB above about 12) and co-surfactant or co-solvent, containing the dissolved drug, which form a fine oil-in-water micro-emulsion spontaneously on gentle agitation in aqueous media such as gastrointestinal fluid. Droplets are typically below about 100 nm for SMEDDS; coarser systems (roughly 100–300 nm) are called SEDDS, and nano-sized ones are often called SNEDDS.

**Why they improve absorption of BCS class II drugs:** the drug stays in solution; huge interfacial area for partition; lipid digestion products form mixed micelles with bile; lymphatic transport of highly lipophilic drugs can bypass first-pass metabolism; some surfactants inhibit P-glycoprotein efflux.

**Components:**

| Component | Examples | Role |
| --- | --- | --- |
| Oil | Medium-chain triglycerides, mono- and diglycerides, oleic acid, vegetable oils | Solubilises the lipophilic drug; promotes lymphatic transport (long-chain) |
| Surfactant | Polysorbate 80, polyoxyl 35 or 40 castor oil, caprylocaproyl macrogolglycerides | Lowers interfacial tension, enables spontaneous emulsification |
| Co-surfactant / co-solvent | Transcutol (diethylene glycol monoethyl ether), propylene glycol, PEG 400, ethanol | Increases interfacial fluidity and drug load |

**Pouton's lipid formulation classification:** Type I oils only (need digestion); Type II oils + water-insoluble surfactants (SEDDS); Type IIIA/IIIB oils + water-soluble surfactants ± co-solvents (SMEDDS; IIIB has less oil); Type IV surfactants and co-solvents without oil (risk of drug precipitation on dilution).

**Development:** solubility of drug in each excipient → construct **pseudo-ternary phase diagrams** (oil vs surfactant:co-surfactant mixture vs water, titration method) to find the micro-emulsion region → select ratios → load drug → optimise by DoE (Unit 2).

**Evaluation:** self-emulsification time and grade, droplet size and polydispersity (dynamic light scattering), zeta potential, robustness to dilution (50–1000 times, different media), cloud point, thermodynamic stability (heating–cooling cycles, centrifugation, freeze–thaw), drug precipitation on dilution, in-vitro dissolution and lipolysis testing, transmittance.

**Solid SMEDDS:** liquid SMEDDS adsorbed on porous carriers (colloidal silica, magnesium aluminometasilicate), spray-dried, or filled in hard or soft gelatin capsules; improves handling and stability.

**Limitations:** chemical instability of drug in lipid, high surfactant content (GI irritation), capsule shell interaction, precipitation on dilution (overcome by supersaturable SMEDDS with polymeric precipitation inhibitors such as HPMC).

## 1.9 Large and small volume parenterals

**Parenteral preparations** are sterile preparations intended for administration by injection, infusion or implantation into the body. By USP convention, a **small-volume parenteral (SVP)** has 100 ml or less per container and a **large-volume parenteral (LVP)** is a single-dose infusion of more than 100 ml (pharmacopoeias word this slightly differently).

### Physiological considerations

- **Route:** intravenous (no absorption phase, any volume as infusion but no oily or suspended particles), intramuscular, subcutaneous (limited volume, suspensions and oils possible), intradermal, intrathecal and intra-ocular (no preservative, strict isotonicity).
- **Tonicity and osmolarity:** plasma osmolality is about 285–295 mOsm/kg. 0.9% NaCl gives about 308 mOsm/L (9 g/L ÷ 58.44 × 2); 5% glucose about 278 mOsm/L. Hypotonic solutions given IV can cause haemolysis; hypertonic solutions are given slowly into large veins (parenteral nutrition through a central line).
- **pH:** blood pH 7.35–7.45 with good buffer capacity, so small volumes away from 7.4 are tolerated; LVPs should be close to physiological pH and lightly buffered. Pain, phlebitis and tissue damage increase at extreme pH.
- **Pyrogens/endotoxins, particulate matter** (emboli, granulomas), **sterility**, **volume and rate** of infusion.

### Formulation considerations

| Component | Examples and remarks |
| --- | --- |
| Vehicle | Water for Injections (WFI); non-aqueous: fixed oils (sesame, cotton-seed), ethyl oleate, benzyl benzoate (IM only); water-miscible co-solvents: ethanol, propylene glycol, PEG 300/400, glycerin |
| Solubilisers | Polysorbate 80, polyoxyl castor oil, cyclodextrins (hydroxypropyl-β-, sulfobutylether-β-) |
| Buffers | Phosphate, citrate, acetate |
| Antioxidants | Sodium metabisulphite, sodium bisulphite, ascorbic acid; nitrogen flushing of headspace |
| Chelating agents | Disodium edetate |
| Preservatives | Benzyl alcohol, chlorocresol, phenol, parabens — for multi-dose SVPs only; **not** in LVPs or in intrathecal, intracisternal and intra-ocular products |
| Tonicity adjusters | Sodium chloride, dextrose, mannitol |
| Bulking agents and cryoprotectants (freeze-dried) | Mannitol, sucrose, trehalose, glycine |

LVPs: simple solutions (electrolytes, dextrose, amino acids, lipid emulsions for parenteral nutrition), no preservative, single dose, usually terminally sterilised in flexible bags or glass bottles.

### Manufacturing

```text
Water for Injections (distillation or equivalent) → compounding in clean area (grade C/D)
→ filtration (0.22 µm sterilising grade filter, integrity tested: bubble point / pressure hold)
→ filling and sealing in grade A zone with grade B background (aseptic) or grade C for
  products to be terminally sterilised → terminal sterilisation (moist heat, typically
  121 °C for at least 15 min equivalent; F0 used to express lethality)
→ leak test → visual inspection → labelling and packing → QC release
```

- **Clean rooms:** graded A to D (Schedule M / EU GMP Annex 1), with HEPA-filtered air, pressure differentials, airlocks and environmental monitoring of viable and non-viable particles.
- **Terminal sterilisation** is preferred whenever the product can withstand it; it gives a sterility assurance level (SAL) of 10⁻⁶. **Aseptic processing** is used for heat-labile products and is validated by media fills (process simulation).
- **Freeze-drying (lyophilisation)** for unstable drugs: freezing below the collapse/eutectic temperature, primary drying (sublimation under vacuum), secondary drying (desorption).
- **Containers:** Type I borosilicate glass for most injections; Type II (treated soda-lime) for some neutral/acidic aqueous products; Type III for non-aqueous; plastics (PVC, polyolefin bags) for LVPs; rubber closures tested for extractables.

### Evaluation (quality control)

- **Sterility test** (membrane filtration or direct inoculation; fluid thioglycollate medium at 30–35 °C and soya-bean casein digest medium at 20–25 °C for 14 days).
- **Bacterial endotoxins test** (LAL: gel-clot, turbidimetric, chromogenic) or the rabbit pyrogen test.
- **Particulate matter:** light obscuration — LVP not more than 25 particles/ml ≥ 10 µm and 3 particles/ml ≥ 25 µm; SVP not more than 6,000 per container ≥ 10 µm and 600 per container ≥ 25 µm.
- **Visible particles and clarity** (inspection against black and white backgrounds), **leaker test** (dye bath with methylene blue under vacuum for ampoules; container closure integrity for vials), **extractable volume**, **pH**, **osmolality**, assay and impurities, **uniformity of content** for powders.

## Remember

- Preformulation feeds QbD: critical material attributes found here are linked to product CQAs later.
- Drug–excipient screens: DSC is a fast screen; isothermal stress testing with HPLC confirms; know Maillard reaction (lactose + amine) and magnesium stearate–aspirin.
- First-order t90 = 0.105/k; Arrhenius slope = −Ea/R; worked example gave Ea ≈ 82 kJ/mol and t90 ≈ 326 days at 25 °C.
- ICH Q1A(R2): long term 25/60 or 30/65 (12 months), intermediate 30/65, accelerated 40/75 (6 months); India is zone IVb (30 °C/75% RH); Q1B photostability 1.2 million lux h and 200 W·h/m².
- DLVO: VT = VA + VR; secondary minimum = loose flocs (controlled flocculation); zeta potential governs.
- F = Vu/V0; β = F/F∞; Stokes velocity ∝ d².
- SMEDDS: oil + surfactant (HLB > 12) + co-surfactant; droplets < 100 nm; Pouton types I–IV; pseudo-ternary phase diagrams.
- SVP ≤ 100 ml, LVP > 100 ml (USP); LVPs have no preservative; 0.9% NaCl ≈ 308 mOsm/L.
