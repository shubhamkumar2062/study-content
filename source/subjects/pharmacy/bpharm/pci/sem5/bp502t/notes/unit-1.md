# Unit 1: Preformulation studies

Before a company decides how to turn a new drug into a tablet, syrup or injection, it studies the drug powder itself: how it looks under the microscope, how it flows, how well it dissolves, and how it breaks down. This early laboratory work is called **preformulation**. Its findings decide the dosage form, the excipients, the manufacturing method and the storage conditions.

## 1.1 Introduction, goals and objectives

**Preformulation** is the study of the physical and chemical properties of a drug substance, alone and with excipients, carried out before formulation work begins, so that a stable, effective and manufacturable dosage form can be designed.

**Goals**

1. Build a full physicochemical profile of the new drug (identity, purity, form, solubility, stability).
2. Find out which properties could cause trouble in manufacture or in the body (poor flow, poor solubility, instability, polymorphism).
3. Choose the most suitable salt and crystal form.
4. Guide the choice of dosage form, excipients and process.
5. Give early data for the regulatory dossier and for setting specifications.

**Objectives in practice**

| Question asked | Property studied | Decision it guides |
| --- | --- | --- |
| Will it dissolve in the gut? | Solubility, pKa, dissolution rate | Salt form, particle size, need for solubiliser |
| Will it be absorbed? | Partition coefficient (log P), BCS class | Route, enhancers, dosage form type |
| Will the powder run through machines? | Particle size, shape, flow, density | Direct compression or granulation |
| Will it stay stable? | Hydrolysis, oxidation, light, moisture | Packaging, antioxidants, pH, process |
| Does it change form? | Polymorphism, hydrates, amorphous content | Which form to develop and control |
| Does it react with excipients? | Drug–excipient compatibility | Excipient selection |

**Typical order of a preformulation programme**

```text
Drug substance received
   → identity, purity, appearance, colour, odour, taste
   → physical form (crystal/amorphous, polymorphs) by microscopy, XRD, DSC
   → particle size, shape, surface area, density, flow
   → solubility vs pH, pKa, log P, dissolution rate
   → solid-state and solution stability (heat, moisture, light, pH, oxygen)
   → compatibility with excipients
   → report → formulation development
```

## 1.2 Physical properties

### a. Physical form: crystalline and amorphous

- **Crystalline solids** have molecules arranged in a regular, repeating three-dimensional lattice. They show a sharp melting point, give sharp X-ray diffraction peaks and are usually more stable.
- **Amorphous solids** have no long-range order (like glass). They have no sharp melting point, show a glass transition, dissolve faster and give higher apparent solubility, but they absorb more moisture and may slowly crystallise during storage.

| Feature | Crystalline | Amorphous |
| --- | --- | --- |
| Arrangement | Ordered lattice | Random |
| Melting | Sharp melting point | Softens over a range (glass transition) |
| Solubility, dissolution | Lower | Higher |
| Stability | Better | Poorer; may crystallise |
| Example | Most drug powders | Amorphous novobiocin (active), crystalline form poorly absorbed |

**Crystal habit** is the outer shape of a crystal (needle, plate, prism, cube). Two crystals with the same internal lattice can have different habits depending on the solvent and cooling rate. Habit affects flow, packing, compression and syringeability of suspensions: needles flow badly and plates cap easily on compression.

### b. Particle size and shape

Particle size affects dissolution rate (smaller particles have more surface area, as in the Noyes–Whitney equation), content uniformity of low-dose drugs, flow, compression, sedimentation in suspensions and texture of ointments. Griseofulvin, digoxin and spironolactone are absorbed better when micronised.

**Methods of particle size analysis**

| Method | Size range (approx.) | Gives |
| --- | --- | --- |
| Optical microscopy | about 1–100 µm | Number distribution, shape |
| Sieving | about 50 µm and above | Weight distribution |
| Sedimentation (Andreasen pipette) | about 1–200 µm | Stokes' diameter |
| Coulter counter (electrical sensing zone) | about 1–200 µm | Volume distribution |
| Laser diffraction | sub-micron to millimetre | Volume distribution, quick |

**Shape** is described as spherical, angular, flaky, needle-like or irregular, and expressed by shape factors such as sphericity. Spherical particles flow best.

### c. Flow properties

Good flow is needed for even die filling, uniform tablet weight and uniform capsule fill. Flow depends on particle size (fine powders below about 100 µm are cohesive), shape, moisture and surface roughness.

**Measures of flow**

1. **Angle of repose (θ):** a funnel is fixed at a height and powder is poured to form a cone; tan θ = h/r, where h is the height and r the radius of the heap base.
2. **Bulk density** = mass ÷ bulk (poured) volume; **tapped density** = mass ÷ volume after tapping to constant volume.
3. **Carr's compressibility index** = 100 × (tapped density − bulk density) ÷ tapped density.
4. **Hausner ratio** = tapped density ÷ bulk density.

| Flow character | Angle of repose (°) | Carr's index (%) | Hausner ratio |
| --- | --- | --- | --- |
| Excellent | 25–30 | 10 or less | 1.00–1.11 |
| Good | 31–35 | 11–15 | 1.12–1.18 |
| Fair | 36–40 | 16–20 | 1.19–1.25 |
| Passable | 41–45 | 21–25 | 1.26–1.34 |
| Poor | 46–55 | 26–31 | 1.35–1.45 |
| Very poor | 56–65 | 32–37 | 1.46–1.59 |
| Very, very poor | above 66 | above 38 | above 1.60 |

(Scale as given in the US Pharmacopeia general chapter on powder flow; textbooks use very similar bands.)

**Worked example:** 50 g of powder occupies 100 ml loosely and 80 ml after tapping. Bulk density 0.50 g/ml, tapped density 0.625 g/ml. Carr's index = 100 × (0.625 − 0.50)/0.625 = 20% (fair). Hausner ratio = 1.25 (fair). Flow can be improved by granulation or a glidant such as colloidal silicon dioxide.

### d. Solubility profile (pKa, pH, partition coefficient)

A drug must dissolve before it is absorbed. As a working rule, an aqueous solubility below about 1 mg/ml often signals absorption problems for an oral drug.

**pKa and pH.** Most drugs are weak acids or weak bases, so their solubility changes with pH. The Henderson–Hasselbalch equation gives the ratio of ionised to un-ionised drug:

- Weak acid: pH = pKa + log [ionised]/[un-ionised]
- Weak base: pH = pKa + log [un-ionised]/[ionised]

Total solubility of a weak acid: S = S0 [1 + 10^(pH − pKa)], where S0 is the solubility of the un-ionised form. A weak acid becomes more soluble as pH rises; a weak base as pH falls. pKa is found by potentiometric titration, by UV spectroscopy at different pH values, or from the solubility–pH curve.

**Partition coefficient (P or log P).** P = concentration in octanol ÷ concentration in water for the un-ionised form, at equilibrium. It measures lipophilicity, which governs passage across membranes. Very low log P → poor membrane crossing; very high log P → poor water solubility. The distribution coefficient (log D) includes ionisation at a stated pH. Measured by the shake-flask method (n-octanol and water) or by HPLC.

**Dissolution rate.** Intrinsic dissolution is measured from a compressed disc of pure drug of fixed area (Wood's apparatus); a rate above about 1 mg/min/cm² is usually not rate-limiting for absorption, while values far lower suggest dissolution-limited absorption.

**Ways to improve poor solubility:** salt formation, pH adjustment, cosolvents, surfactants, complexation with cyclodextrins, particle size reduction, amorphous form or solid dispersions, prodrugs.

### e. Polymorphism

**Polymorphism** is the ability of a substance to exist in more than one crystalline form with the same chemical composition. Polymorphs differ in melting point, solubility, dissolution rate, density, hardness, and stability.

- **Stable form:** lowest free energy, highest melting point, lowest solubility.
- **Metastable form:** higher energy and solubility; changes to the stable form with time, heat, moisture or grinding.
- **Enantiotropic** polymorphs can change into each other reversibly at a transition temperature; **monotropic** polymorphs change only one way (metastable → stable).
- **Pseudopolymorphs:** solvates and hydrates (solvent built into the lattice). Anhydrous forms usually dissolve faster than hydrates (anhydrous ampicillin vs trihydrate).

**Pharmaceutical examples:** chloramphenicol palmitate (form B is absorbed much better than form A), ritonavir (appearance of a less soluble new form forced reformulation), cocoa butter (polymorphic fat; overheating gives a low-melting unstable form, so suppositories fail to set), and many sulphonamides and barbiturates.

**Methods to detect polymorphs:** X-ray powder diffraction (fingerprint of each lattice), differential scanning calorimetry (melting points and transitions), thermogravimetric analysis (solvent loss), hot-stage microscopy, infrared and Raman spectroscopy, solubility and dissolution studies.

### f. Other physical properties studied

Hygroscopicity (moisture uptake at different humidities), density, compressibility, melting point, colour, odour and taste (taste masking needed for paediatric liquids), and optical activity.

## 1.3 Chemical properties

The main chemical ways in which drugs break down are listed below. Preformulation stress studies expose the drug to heat, moisture, acid, alkali, oxygen and light to find which ones matter.

### a. Hydrolysis

Reaction with water, usually catalysed by H+ or OH− ions. The most common route of degradation.

| Group | Example drugs | Notes |
| --- | --- | --- |
| Esters | Aspirin, procaine, benzocaine, atropine | Aspirin → salicylic acid + acetic acid (vinegar odour of old tablets) |
| Amides | Paracetamol, chloramphenicol, lignocaine | Slower than esters |
| Lactams | Penicillins, cephalosporins | β-lactam ring opens; dry powders reconstituted before use |
| Imides, carbamates | Barbiturates | — |

**Prevention:** keep moisture out (dry granulation or direct compression, desiccant, moisture-proof packs), adjust pH to the point of maximum stability, use non-aqueous or dry forms (powder for reconstitution, lyophilised injections), reduce dielectric constant with cosolvents, complexation, suspensions instead of solutions (only dissolved drug hydrolyses).

### b. Oxidation

Loss of electrons or gain of oxygen; often a free-radical chain reaction started by light, heat or trace metals (auto-oxidation).

Examples: adrenaline and other catecholamines (turn pink then brown), ascorbic acid, vitamin A, morphine, phenothiazines, unsaturated oils (rancidity).

**Prevention:** replace air with nitrogen or carbon dioxide; antioxidants (water-soluble: sodium metabisulphite, sodium bisulphite, ascorbic acid; oil-soluble: butylated hydroxyanisole, butylated hydroxytoluene, tocopherols, propyl gallate); chelating agents such as disodium edetate to bind metal ions; light-resistant amber containers; low temperature; optimum pH.

### c. Reduction

Gain of electrons; less common than oxidation. Some drugs with nitro groups, metal ions (for example, reduction of some metal salts) or quinone structures can be reduced, especially in the presence of reducing excipients or impurities. Prevention follows the same lines: control of impurities, pH and light.

### d. Racemisation

Conversion of an optically active form into an equal mixture of its two enantiomers (racemate), with loss of optical activity and often of potency, because usually one enantiomer is the active one.

Examples: L-hyoscyamine racemises to atropine (DL-hyoscyamine) with half the potency; L-adrenaline racemises in solution, especially at low pH and higher temperature; pilocarpine undergoes epimerisation to isopilocarpine. Controlled by pH and temperature.

### e. Polymerisation

Joining of drug molecules into larger chains or dimers. Examples: concentrated aqueous ampicillin and other aminopenicillins form dimers and polymers (linked to allergic reactions); formaldehyde solution forms paraformaldehyde on standing; glucose solutions heated during sterilisation form 5-hydroxymethylfurfural, which can polymerise and cause yellowing. Controlled by concentration, pH, temperature and short storage after reconstitution.

### f. Other routes

Decarboxylation, photolysis (nifedipine, riboflavin, sodium nitroprusside), isomerisation and hydration/dehydration.

### g. Drug–excipient compatibility

Binary mixtures (often 1:1) of drug and each excipient are stored at raised temperature and humidity and examined by DSC, HPLC and appearance. Classic incompatibilities: amine drugs + lactose (Maillard reaction, browning), aspirin + magnesium stearate (alkaline stearate speeds hydrolysis), tetracycline + calcium salts (chelation, less absorption).

## 1.4 BCS classification of drugs and its significance

The **Biopharmaceutics Classification System (BCS)** groups drugs by aqueous solubility and intestinal permeability, the two factors that mainly control oral absorption.

- **High solubility:** the highest dose strength dissolves in 250 ml or less of aqueous media over the pH range 1 to 6.8 (older guidance used up to pH 7.5).
- **High permeability:** the extent of absorption in humans is 85% or more of the dose (older guidance used 90%).
- **Rapid dissolution:** at least 85% of the label amount dissolves within 30 minutes in standard media.

```text
                     PERMEABILITY
                   high         low
              +------------+------------+
   SOLUBILITY |  Class I   |  Class III |   high solubility
              |  propranolol, metoprolol | atenolol, cimetidine
              +------------+------------+
              |  Class II  |  Class IV  |   low solubility
              | carbamazepine, ketoconazole | furosemide (often placed), hydrochlorothiazide
              +------------+------------+
```

| Class | Problem | Formulation approach |
| --- | --- | --- |
| I | Usually none; absorption fast | Simple conventional tablet or capsule |
| II | Dissolution limits absorption | Micronisation, salts, solid dispersions, surfactants, cyclodextrins, lipid systems |
| III | Permeability limits absorption | Permeation enhancers, prodrugs; dissolution is not critical |
| IV | Both | Hard to develop orally; consider other routes or advanced systems |

(Class placement of a given drug can differ between sources because it depends on the dose used.)

**Significance**

1. Predicts whether absorption will be limited by dissolution or by permeability.
2. Guides the choice of formulation technique early.
3. Allows **biowaivers**: for some Class I (and in certain guidelines Class III) drugs in rapidly dissolving immediate-release products, in-vitro dissolution can replace an in-vivo bioequivalence study.
4. Helps set meaningful dissolution specifications and in vitro–in vivo correlation.

## 1.5 Application of preformulation in developing dosage forms

### Solid oral dosage forms (tablets, capsules)

- Flow and compressibility decide direct compression versus wet or dry granulation.
- Moisture-sensitive or heat-sensitive drugs (aspirin) avoid wet granulation; use dry granulation or direct compression.
- Poor solubility → smaller particle size, soluble salt, surfactant, hydrophilic excipients.
- Polymorph selection and control during milling, granulation and drying.
- Compatibility studies decide diluent, lubricant and disintegrant.
- Light- or moisture-sensitive drugs → coating and suitable packs.

### Liquid oral dosage forms (syrups, suspensions, emulsions)

- Solubility at a palatable pH decides solution or suspension.
- pH–stability profile decides the buffer and pH of the product.
- Hydrolysis-prone drugs (many antibiotics) → dry powder for reconstitution.
- Taste and odour decide flavouring, sweetening or use of an insoluble salt.
- Particle size and density data help in designing suspensions that settle slowly and redisperse easily.
- Preservative choice depends on pH and on partitioning into oil phases.

### Parenteral dosage forms

- Solubility in water at a pH near 7.4 (or a tolerable pH) decides solution, cosolvent system, suspension or emulsion.
- Stability to heat decides terminal sterilisation versus aseptic filtration; unstable drugs are freeze-dried.
- Oxidation-prone drugs need antioxidants, nitrogen flushing and chelating agents.
- pKa and pH data help avoid precipitation on dilution or mixing.
- Compatibility with containers and closures (adsorption, leaching).

### Impact on stability of dosage forms

Preformulation identifies the main degradation route and its rate, so the formulator can control the factors that drive it: pH, moisture, oxygen, light, temperature and excipients. This leads to the right packaging, storage label (for example "store in a cool, dry place, protect from light") and a realistic shelf life, later confirmed by formal stability studies.

## Remember

- Preformulation = physical and chemical study of the drug before formulation; it guides dosage form, excipients, process and packaging.
- Amorphous forms dissolve faster but are less stable; the stable polymorph has the highest melting point and lowest solubility.
- Angle of repose tan θ = h/r; Carr's index = 100(ρtapped − ρbulk)/ρtapped; Hausner ratio = ρtapped/ρbulk. Carr's index up to 15% or Hausner ratio up to 1.18 means good flow.
- Weak acid S = S0[1 + 10^(pH − pKa)]; log P from octanol–water shake flask.
- Hydrolysis (esters, amides, β-lactams) and oxidation (catecholamines, ascorbic acid, oils) are the main chemical routes; also reduction, racemisation (hyoscyamine → atropine) and polymerisation (ampicillin).
- BCS: Class I high/high, II low solubility, III low permeability, IV both low; high solubility = highest dose in 250 ml over pH 1–6.8.
- Classic incompatibilities: aspirin–magnesium stearate, amines–lactose, tetracycline–calcium.
