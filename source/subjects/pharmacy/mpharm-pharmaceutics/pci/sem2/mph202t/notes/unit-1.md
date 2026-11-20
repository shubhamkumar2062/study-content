# Unit 1: Drug absorption from the gastrointestinal tract

This unit explains how an oral drug moves from the dosage form into the blood: the structure of the gut, the routes across the epithelium, the pH-partition hypothesis and its limits, dissolution theory, the effect of each dosage form, and the modern "transport model" that links permeability, solubility and charge state. It ends with the experimental methods used to measure solubility and permeability.

All numbers in worked examples are example numbers for hypothetical drugs, chosen to make the arithmetic clear.

## 1.1 The gastrointestinal tract as an absorbing organ

```text
 Dosage form
     │  disintegration / deaggregation
     ▼
 Drug particles in GI fluid ──dissolution──► Drug in solution
                                                 │  permeation across epithelium
                                                 ▼
                                       Portal blood → liver (first pass) → systemic blood
```

| Region | Typical pH (fasted) | Transit | Main features |
| --- | --- | --- | --- |
| Stomach | 1–3 (rises to 3–5 after a meal) | 0.5–2 h, depends on meal | Small surface, mixing and grinding; little absorption of most drugs |
| Duodenum | about 5–6.5 | minutes | Bile and pancreatic juice enter; rapid pH rise |
| Jejunum | about 6–7 | together with ileum about 3–4 h | Largest absorbing surface (folds, villi, microvilli), many transporters |
| Ileum | about 7–7.5 | | Bile salt reabsorption, Peyer's patches (M-cells) |
| Colon | about 5.5–7 | 10–30 h or more | Long residence, bacteria, less fluid; site for colon-targeted and some extended-release absorption |

**Why the small intestine absorbs most drugs:** the folds of Kerckring, villi and microvilli multiply the surface greatly; blood flow is high; residence time is several hours; and the epithelium carries many uptake transporters. The stomach mainly decides *when* the drug reaches the intestine.

**Gastric emptying.** In the fasted state the stomach follows the migrating motor complex (MMC), a cycle of about 1.5–2 h: phase I (quiet), phase II (irregular contractions) and phase III (strong "housekeeper" waves that sweep undissolved material, including non-disintegrating tablets, into the intestine). A meal stops the MMC and the stomach empties slowly in the fed pattern. Fat, high calorie load, acidity, cold or very hot liquids and some drugs (anticholinergics, opioids) slow emptying; metoclopramide speeds it. Because most drugs are absorbed in the intestine, slower emptying usually delays tmax and may lower Cmax.

**Other physiological factors:** intestinal transit time, blood flow to the gut, luminal enzymes (peptidases degrade peptides), gut-wall metabolism (CYP3A4 in enterocytes), efflux transporters (P-glycoprotein, BCRP), disease (achlorhydria, malabsorption, Crohn's disease), age, and food (bile release improves solubility of lipophilic drugs; binding to food can reduce absorption).

## 1.2 Mechanisms of drug absorption

| Mechanism | Driving force / carrier | Saturable? | Typical substrates |
| --- | --- | --- | --- |
| Passive transcellular diffusion | Concentration gradient of the un-ionised, lipid-soluble form (Fick's law) | No | Most small lipophilic drugs |
| Paracellular diffusion | Through tight junctions between cells | No | Small hydrophilic molecules, some cations |
| Carrier-mediated: facilitated diffusion | Carrier, no energy, down the gradient | Yes | Some sugars, vitamins |
| Carrier-mediated: active transport | Carrier, energy (ATP or ion gradient), can work against a gradient | Yes, shows competition | Amino acid and peptide-like drugs (PEPT1 substrates such as β-lactams and ACE-inhibitor prodrugs), nucleosides |
| Efflux (active, secretory direction) | ABC transporters P-gp, BCRP, MRP2 pump drug back into the lumen | Yes | Many lipophilic drugs; lowers net absorption |
| Endocytosis (pinocytosis, receptor-mediated, phagocytosis) | Membrane vesicles | Yes | Macromolecules, particles, vitamin B12–intrinsic factor complex |
| Ion-pair transport | A charged drug pairs with an endogenous counter-ion and the neutral pair diffuses | — | Quaternary ammonium compounds |
| Lymphatic uptake (M-cells, chylomicrons) | Via lipoproteins and lymph | — | Very lipophilic drugs (log P above about 5) given with fat, particulates |

**Fick's first law for passive diffusion**

dQ/dt = (D × K × A / h) × (CGI − Cplasma) = P × A × ΔC

where D is the diffusion coefficient in the membrane, K the membrane/water partition coefficient, A the area, h the membrane thickness and P (= DK/h) the permeability coefficient. Because blood flow removes absorbed drug rapidly, Cplasma is much smaller than CGI ("sink condition") and absorption follows apparent first-order kinetics: rate = Ka × amount at the absorption site.

**Carrier-mediated transport** follows Michaelis–Menten kinetics: rate = Jmax × C/(Kt + C). At low concentration it is near first order; at high concentration it saturates and becomes zero order, so the fraction of a large dose absorbed falls. It is structure-specific and can be inhibited competitively.

## 1.3 pH-partition theory of drug absorption

**Statement (Brodie, Shore and Schanker):** in the GI tract, only the un-ionised form of a weak acid or weak base, if it is lipid-soluble enough, crosses the membrane by passive diffusion. The fraction un-ionised depends on the pKa of the drug and the pH at the absorption site (Henderson–Hasselbalch):

- Weak acid: % un-ionised = 100 / (1 + 10^(pH − pKa))
- Weak base: % un-ionised = 100 / (1 + 10^(pKa − pH))

At steady state, if only the un-ionised form crosses and its concentration is equal on both sides, the ratio of total drug concentrations across a membrane separating two pH values is:

- Weak acid: Rplasma/GI = [1 + 10^(pHplasma − pKa)] / [1 + 10^(pHGI − pKa)]
- Weak base: RGI/plasma = [1 + 10^(pKa − pHGI)] / [1 + 10^(pKa − pHplasma)]

### Worked example 1 (example numbers)

A weak acid of pKa 4.4 is un-ionised to 99.94% at pH 1.2, 0.40% at pH 6.8 and 0.10% at pH 7.4. A weak base of pKa 9.0 is un-ionised to 0.63% at pH 6.8 and 2.45% at pH 7.4, and is almost completely ionised at pH 1.2.

For a weak acid of pKa 3.5 with gastric pH 1.4 and plasma pH 7.4:

R = (1 + 10^3.9)/(1 + 10^−2.1) = 7944/1.008 ≈ **7,880**

so total drug at equilibrium would be about 7,900 times higher in plasma than in the stomach: the acid is "trapped" in plasma (ion trapping). For a weak base of pKa 8.5 the ratio stomach/plasma is about 9 × 10^5, which is why weak bases given intravenously can accumulate in gastric juice.

### Limitations of the pH-partition hypothesis

1. **Surface area and residence time dominate.** Weak acids are absorbed mainly in the small intestine, where they are highly ionised, because its surface is huge and contact time long. The stomach's favourable pH cannot outweigh its small area.
2. **Microclimate pH.** The layer next to the enterocyte surface is more acidic (about 5.5–6) than the bulk intestinal fluid, which increases the un-ionised fraction of weak acids at the membrane.
3. **Ionised forms do cross.** Paracellular diffusion, ion-pairs and transporters carry charged species; the ionised form has a small but real permeability.
4. **Unstirred (aqueous boundary) layer.** For very lipophilic drugs, diffusion through the water layer next to the membrane, not membrane partitioning, limits the rate.
5. **Ignores dissolution.** A poorly soluble drug may never reach a high enough solution concentration.
6. **Ignores carriers and efflux, gut-wall metabolism, and binding to mucus.**
7. **Lipid solubility (log P or log D) also matters,** not only the un-ionised fraction; a fully un-ionised but very polar molecule is still poorly absorbed.

Despite these, the hypothesis correctly predicts the *direction* of pH effects and explains ion trapping, urinary pH effects on excretion, and the use of buffered or salt forms.

## 1.4 Formulation and physicochemical factors: dissolution

For most solid oral products, **dissolution is the rate-limiting step for poorly soluble drugs**, and **permeation is rate-limiting for soluble but poorly permeable drugs**.

### Dissolution process and models

```text
 Solid surface │ stagnant diffusion layer (thickness h) │ bulk solution
   C = Cs      │ ───────── concentration falls ──────►  │  C (bulk)
```

**Noyes–Whitney equation** (with the Nernst–Brunner film interpretation):

dM/dt = D × A × (Cs − C) / h

- dM/dt: dissolution rate (mass per time)
- D: diffusion coefficient of the drug in the medium
- A: surface area of the dissolving solid
- Cs: saturation solubility at the surface; C: bulk concentration
- h: thickness of the diffusion (stagnant) layer

When C is much smaller than Cs (sink conditions, in practice C below about 10–30% of Cs), rate ≈ D A Cs / h, i.e. constant.

**Other models**

- **Interfacial barrier model:** the slow step is the reaction or detachment at the solid–liquid interface, not diffusion; rate = Ki (Cs − C).
- **Danckwerts surface-renewal model:** turbulent eddies continually replace fluid at the surface; rate = A (Cs − C) √(γD), where γ is the rate of surface renewal.
- **Hixson–Crowell cube-root law** for a powder of equal spheres dissolving with shrinking area: W0^(1/3) − W^(1/3) = κ t.

### Worked example 2 — Noyes–Whitney (example numbers)

D = 5 × 10⁻⁶ cm²/s, A = 50 cm², h = 30 µm (3 × 10⁻³ cm), Cs = 1.0 mg/mL, C = 0.05 mg/mL.

dM/dt = 5 × 10⁻⁶ × 50 × (1.0 − 0.05)/(3 × 10⁻³) = 0.0792 mg/s = **4.75 mg/min**.

Particle size effect: 100 mg of powder (density 1.3 g/cm³) as spheres of diameter d has surface S = 6m/(ρd). At d = 50 µm, S = 92 cm²; at d = 10 µm, S = 462 cm². A five-fold smaller diameter gives a five-fold larger area and, other terms constant, a five-fold faster initial dissolution.

### Worked example 3 — Hixson–Crowell (example numbers)

A powder sample of 100 mg leaves 64 mg undissolved after 10 min. κ = (100^(1/3) − 64^(1/3))/10 = (4.642 − 4.000)/10 = 0.0642 mg^(1/3)/min. Time for complete dissolution = 100^(1/3)/κ ≈ **72 min**.

### Factors affecting the dissolution rate

| Group | Factor | Effect and explanation |
| --- | --- | --- |
| Drug (physicochemical) | Solubility (Cs) | Directly proportional in Noyes–Whitney |
| | Particle size / surface area | Micronisation and nanosizing increase A; very fine hydrophobic powders may aggregate or float, so effective area matters |
| | Polymorphism | Metastable polymorphs have higher free energy and higher solubility; may convert to the stable form on storage |
| | Amorphous state | Higher solubility than crystalline; basis of solid dispersions; risk of recrystallisation |
| | Hydrates and solvates | Anhydrous forms usually dissolve faster than hydrates in water; organic solvates may dissolve faster |
| | Salt form | Salts of weak acids or bases dissolve faster; a sodium salt of a weak acid raises the pH of the diffusion layer, increasing local solubility |
| | Wettability | Contact angle; surfactants improve wetting |
| | Complexation, prodrugs, cocrystals | Change apparent solubility |
| Formulation | Diluents | Hydrophilic diluents (lactose) help wetting; adsorbents can bind drug |
| | Disintegrants | Superdisintegrants (croscarmellose, crospovidone, sodium starch glycolate) increase area quickly |
| | Binders | Excess binder or strong binders slow disintegration |
| | Lubricants | Hydrophobic magnesium stearate coats particles and slows dissolution, worse with long mixing |
| | Surfactants | Improve wetting and solubilise (micelles) |
| | Coatings | Film coats add a lag; enteric coats delay release until intestinal pH |
| Processing | Granulation method | Wet granulation often improves wetting; dry granulation may slow it |
| | Compression force | Higher force lowers porosity and slows disintegration; very high force can fracture particles and increase area |
| | Storage | Ageing, moisture uptake and hardening can slow dissolution |
| Medium / test | Agitation | Faster agitation reduces h |
| | Temperature, viscosity, pH, volume, surface tension | Affect Cs, D and h |

## 1.5 Gastrointestinal absorption: the role of the dosage form

General order of rate of drug availability (fastest to slowest): **solution > suspension > capsule > tablet > coated tablet** (modified-release products are designed to be slow).

### Solutions (elixirs, syrups, solutions)

- No dissolution step, so absorption is usually fastest and most complete.
- Factors: dilution in gastric fluid may **precipitate** a weak acid from its salt solution (fine precipitate usually redissolves quickly); viscosity of syrups slows gastric emptying and diffusion; cosolvents (ethanol, propylene glycol) may precipitate drug on dilution; complexation (with cyclodextrins or other ingredients) can reduce free drug; chemical stability in solution limits use.

### Suspensions

- Dissolution of fine, already wetted particles is rapid.
- Key factors: particle size and size distribution, polymorphic form, wetting agent, viscosity (high viscosity slows dissolution and emptying), crystal growth on storage (Ostwald ripening), drug–excipient complexation and the density of the vehicle.

### Capsules (hard gelatin)

- The shell dissolves quickly in warm acidic fluid; then the powder plug must deaggregate.
- Factors: particle size, hydrophilic versus hydrophobic diluent, lubricant, wetting agent, tightness of packing (dense plugs dissolve slowly), and shell cross-linking on ageing (aldehydes or high humidity make gelatin less soluble; pepsin or pancreatin may be added to the test medium in such cases).
- Soft gelatin capsules with drug dissolved in oil or a self-emulsifying system can give fast, reproducible absorption of lipophilic drugs.

### Tablets

- Must disintegrate into granules and then fine particles before most dissolution occurs. Granules dissolve faster than the intact tablet, and primary particles faster still (Wagner's scheme).

```text
 Tablet ──disintegration──► Granules ──deaggregation──► Fine particles
    │ (slow)                    │ (moderate)                │ (fast)
    └──────────────────── drug in solution ◄──────────────┘
                                │ absorption
                                ▼
                        drug in blood
```

- Factors: compression force, binder and disintegrant type and amount, lubricant, granule size, porosity, coating. Sugar coating and film coating add time; enteric coating moves release to the intestine; changes in coating thickness change lag time.

### Dissolution methods (summary)

Official methods (IP, USP, BP): basket (Apparatus 1), paddle (Apparatus 2), reciprocating cylinder (3), flow-through cell (4), paddle over disc (5), rotating cylinder (6) and reciprocating holder (7). Details, alternatives and acceptance criteria are covered in Unit 2.

### Formulation and processing factors

Choice of salt or polymorph, particle size, excipient compatibility, granulation route, compression and coating determine product performance; they are deliberately controlled in quality by design (Unit 2).

### Correlation of in vivo data with in vitro dissolution data

The aim is a predictive mathematical link between an in vitro property (usually rate or extent of dissolution) and an in vivo response (plasma level, AUC, Cmax or fraction absorbed). Level A (point-to-point), B (mean dissolution time vs mean residence time) and C (single point) correlations, and their regulatory uses (biowaivers, setting dissolution specifications), are described in Unit 2. A correlation is most likely when dissolution is the rate-limiting step (BCS Class II).

## 1.6 The transport model: permeability, solubility and charge state

Modern biopharmaceutics (for example the treatment by Avdeef) combines the pH-partition hypothesis with diffusion through barriers in series.

### Flux and the effective permeability

Flux across the intestinal wall: J = Peff × C (C = dissolved drug concentration at the surface). Drug must cross several resistances in series, like electrical resistors:

1/Peff = 1/PABL + 1/(Pm + Ppara)

- **PABL:** permeability of the aqueous boundary (unstirred) layer; depends on the diffusion coefficient and layer thickness, not on lipophilicity.
- **Pm:** membrane (transcellular) permeability; for a weak acid or base only the neutral species crosses well, so Pm = P0 × fneutral, where P0 is the intrinsic permeability of the neutral form.
- **Ppara:** paracellular permeability through tight junctions.

Consequences:

- At pH values where the drug is mostly neutral, Pm is large and **PABL limits** the flux (log Peff vs pH curve flattens).
- Where the drug is mostly ionised, Pm falls by a factor of 10 for each pH unit away from the pKa until Ppara or the small permeability of the ion sets a floor.
- The apparent pKa seen in permeability–pH curves shifts from the true pKa because of the boundary layer ("pKa flux").

### Solubility × permeability = flux

The maximum flux depends on *both*: Jmax = Peff × Cs. A highly soluble but impermeable drug and a highly permeable but insoluble drug can both have low flux. Charge state works in opposite directions: ionisation raises solubility but lowers membrane permeability. This trade-off underlies the BCS (Unit 5). A simple estimate is the **maximum absorbable dose**:

MAD = S × Ka × SIWV × SITT

(S solubility at pH 6.5, Ka transintestinal absorption rate constant, SIWV small-intestinal water volume about 250 mL, SITT small-intestinal transit time about 270 min.)

**Example (example numbers):** S = 0.05 mg/mL, Ka = 0.03 min⁻¹ → MAD = 0.05 × 0.03 × 250 × 270 = **about 101 mg**. A planned 200 mg dose would be solubility-limited; the dose number D0 = (200/250)/0.05 = 16 (well above 1).

### Properties of the GIT relevant to the model

- **Surface area and villus structure** set the available area.
- **Mucus layer** (glycoproteins) and the unstirred water layer slow diffusion of lipophilic and large molecules; mucus binds some cationic drugs.
- **Bile salts and lipids** form mixed micelles that raise the apparent solubility of lipophilic drugs (food effect, FaSSIF and FeSSIF media).
- **Transit and fluid volume:** fluid is not uniformly spread; pockets of fluid and short residence limit dissolution.

### pH microclimate

The Na⁺/H⁺ exchanger on the apical membrane pumps protons into a thin layer near the surface that is held by mucus. Its pH is about 5.5–6.5 while the bulk lumen may be 6.5–7.5. For weak acids this raises the neutral fraction at the membrane; for weak bases it lowers it. It explains why weak acids are absorbed better from the jejunum than bulk-pH calculations predict.

### Intracellular pH environment

The cytoplasm of enterocytes is about pH 7.0–7.2, and blood is 7.4. A weak acid entering the cell becomes more ionised and is "pulled" through towards the blood side; a weak base may be partly trapped in acidic intracellular compartments (lysosomes, pH about 4.5–5), which increases its tissue retention. The pH gradient across the cell therefore adds a driving force beyond simple concentration.

### Tight-junction complex

```text
  Lumen
  ┌─────────┐ tight junction ┌─────────┐
  │ cell    │╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳│ cell    │   ← claudins, occludin, ZO proteins
  │         │ adherens jn    │         │
  │         │  desmosome     │         │
  └─────────┘                └─────────┘
  Blood / lamina propria
```

- Seals adjacent enterocytes; formed by transmembrane proteins (claudins, occludin, junctional adhesion molecules) linked to the actin cytoskeleton through zonula occludens (ZO) proteins.
- The paracellular route is narrow (pores of a few ångströms) and leakier in the upper small intestine than in the colon.
- It favours small hydrophilic molecules (molecular weight below about 200–300 Da) and, because the pores carry negative charges, **cations pass more easily than anions**.
- Paracellular area is only a tiny fraction of the total surface, so this route is minor for most drugs.
- **Permeation enhancers** (medium-chain fatty acids such as sodium caprate, chitosan, bile salts, EDTA) open tight junctions transiently; they are used in some oral peptide products.

## 1.7 Solubility: experimental methods

| Method | What it measures | Notes |
| --- | --- | --- |
| Shake-flask (equilibrium or thermodynamic) | Concentration of a saturated solution in equilibrium with excess solid at fixed temperature (37 °C for biopharmaceutics) | Gold standard; shake 24–72 h, separate by filtration or centrifugation, assay by HPLC or UV; check pH at the end and the solid form (polymorph or salt conversion) |
| pH–solubility profile | Shake-flask at several pH values across 1.2–6.8 | Needed for BCS solubility class; gives intrinsic solubility S0 and pKa-related curve |
| Kinetic solubility | Concentration at which drug added from a DMSO stock precipitates, detected by nephelometry, turbidity or UV | High-throughput screening in discovery; often overestimates (supersaturation, amorphous precipitate) |
| Potentiometric (acid–base titration, e.g. "CheqSol") | Intrinsic solubility of ionisable drugs from titration curves | Small sample, fast |
| Biorelevant media | Solubility in FaSSIF, FeSSIF, FaSSGF | Shows food and bile effects for lipophilic drugs |
| Phase-solubility (Higuchi–Connors) | Solubility vs complexing-agent concentration | Studies cyclodextrin complexes |

## 1.8 Permeability: in vitro, in situ and in vivo methods

### In vitro

1. **PAMPA (parallel artificial membrane permeability assay):** a filter coated with lipid in an organic solvent separates donor and acceptor wells; measures passive transcellular permeability only. Fast and cheap; no transporters, no paracellular route.
2. **Caco-2 monolayers:** human colon carcinoma cells grown on filters for about 21 days differentiate into enterocyte-like cells with tight junctions, brush border and transporters (P-gp, BCRP, PEPT1). Integrity is checked by trans-epithelial electrical resistance (TEER) and markers (lucifer yellow, mannitol). Apparent permeability:

   Papp = (dQ/dt) / (A × C0)

   Bidirectional studies (apical→basolateral and basolateral→apical) give the **efflux ratio** = Papp(B→A)/Papp(A→B); a ratio of about 2 or more suggests active efflux, confirmed with an inhibitor.
3. **MDCK and MDCK-MDR1 cells:** grow faster (3–5 days), lower background transporter expression; MDR1-transfected cells test P-gp efflux.
4. **Excised tissue:** Ussing chamber (mounted intestinal segment, measures flux and electrical parameters), everted gut sac (drug transfer into the sac), intestinal rings for uptake.

**Example (example numbers):** a Caco-2 insert of area 1.12 cm², donor concentration 100 µg/mL, steady appearance in the receiver 0.12 µg/min.
Papp = (0.12/60 µg/s)/(1.12 cm² × 100 µg/cm³) = **1.8 × 10⁻⁵ cm/s**, which is in the high-permeability range for most laboratories (each laboratory classifies against its own reference drugs).

### In situ

- **Single-pass intestinal perfusion (SPIP) in rats:** a segment of jejunum is cannulated and perfused at a fixed flow Q with drug solution; inlet and outlet concentrations (corrected for water flux with a non-absorbed marker) give

  Peff = −Q × ln(Cout/Cin) / (2πrL)

  where r is the radius and L the length of the segment. Blood supply and innervation are intact.
- **Closed-loop (Doluisio) method:** a tied segment filled with drug solution; samples taken from the loop over time.
- **Intestinal–vascular perfusion:** drug appearance in mesenteric blood is measured directly.

### In vivo

- **Human regional jejunal perfusion (Loc-I-Gut):** a multichannel tube with two balloons isolates a 10 cm segment of jejunum; Peff in humans is measured directly. Human Peff values classify BCS permeability.
- **Mass-balance and absolute bioavailability studies:** fraction absorbed (fa) from urinary recovery of total radioactivity after oral and IV doses, or from absolute bioavailability corrected for first-pass loss. Under ICH M9, fa of 85% or more means high permeability.
- **Pharmacokinetic deconvolution** (Wagner–Nelson, Loo–Riegelman; Unit 3) gives the time course of absorption.

## 1.9 Linking the pieces

```text
 Dose ─► Disintegration ─► Dissolution (Noyes–Whitney: D, A, Cs, h)
                                │
                                ▼
            Dissolved drug at gut surface (pH microclimate, charge state)
                                │  Peff = f(ABL, membrane P0·fneutral, paracellular)
                                ▼
          Enterocyte (CYP3A4, P-gp efflux, pH 7.0–7.2) ─► portal blood ─► liver ─► F
```

Oral bioavailability: **F = fa × FG × FH**, where fa is the fraction absorbed into the gut wall, FG the fraction escaping gut-wall metabolism and FH the fraction escaping hepatic first pass. Biopharmaceutic design works mainly on fa (solubility, dissolution, permeability).

## Remember

- Rate-limiting step: dissolution for poorly soluble drugs, permeation for poorly permeable ones.
- pH-partition: only the un-ionised, lipid-soluble form diffuses; % un-ionised acid = 100/(1 + 10^(pH − pKa)), base = 100/(1 + 10^(pKa − pH)).
- Limits of pH-partition: intestinal surface area, microclimate pH, unstirred layer, carriers and ion pairs, dissolution.
- Noyes–Whitney: dM/dt = DA(Cs − C)/h; sink condition keeps C small; Hixson–Crowell is the cube-root law.
- Dosage form order: solution > suspension > capsule > tablet > coated tablet.
- Transport model: 1/Peff = 1/PABL + 1/(Pm + Ppara); Pm = P0 × fneutral; flux = Peff × Cs.
- Microclimate pH about 5.5–6.5; intracellular pH about 7.0–7.2; tight junctions favour small hydrophilic cations.
- Permeability methods: PAMPA, Caco-2 (efflux ratio ≥ 2), MDCK, Ussing chamber; SPIP Peff = −Q ln(Cout/Cin)/(2πrL); Loc-I-Gut; fa ≥ 85% = high permeability.
- F = fa × FG × FH.
