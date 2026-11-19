# Unit 1: Absorption and distribution of drugs, protein binding

Biopharmaceutics links the dosage form to what happens in the body. A tablet can contain the right amount of drug and still fail if the drug does not dissolve, does not cross the gut wall, or is held back in the blood. This unit covers how drugs are absorbed from the gut and other sites, how they spread into tissues, and how binding to plasma and tissue proteins changes their action.

## 1.1 Introduction to biopharmaceutics

**Biopharmaceutics** is the study of how the physicochemical properties of a drug, the dosage form and the route of administration affect the rate and extent of drug absorption, and so the response.

**Pharmacokinetics** is the study of the time course of drug absorption, distribution, metabolism and excretion (ADME) — "what the body does to the drug".

**Pharmacodynamics** is the study of the drug's effect and its mechanism — "what the drug does to the body".

**Clinical pharmacokinetics** applies pharmacokinetic principles to safe and effective treatment of an individual patient.

The steps a drug passes through after an oral dose are often written as **LADME**:

```text
Liberation    → drug released from the dosage form (disintegration, dissolution)
Absorption    → drug crosses membranes into the systemic blood
Distribution  → drug moves from blood into tissues and back
Metabolism    → drug is chemically changed, mostly in the liver
Excretion     → drug or metabolite leaves the body (urine, bile, air …)
(Metabolism + excretion = elimination; distribution + elimination = disposition)
```

**Why biopharmaceutics matters**

- Two products with the same drug and dose may give different blood levels (different bioavailability).
- Excipients, particle size, crystal form and manufacturing process can all change the rate of release.
- It guides the choice of route, dosage form and dosing schedule.

## 1.2 The cell membrane and the gastrointestinal tract

The cell membrane is a **lipid bilayer** (phospholipids with cholesterol) in which proteins float — the fluid mosaic model. It is lipophilic, so lipid-soluble, un-ionised molecules cross easily. Small aqueous pores (about 4–7 Å) let very small water-soluble molecules through. Tight junctions join neighbouring cells.

**Parts of the GIT and their relevance to absorption**

| Region | pH (approx.) | Key features for absorption |
| --- | --- | --- |
| Mouth | 6.2–7.2 | Thin, well-supplied mucosa under the tongue; sublingual drugs avoid first-pass metabolism |
| Stomach | 1–3 (fasting) | Small area, thick mucus, short stay; some weak acids absorbed |
| Duodenum | 5–6 | Main site for many drugs; bile enters here |
| Jejunum and ileum | 6–7.5 | Very large area (villi and microvilli, about 200 m²), rich blood flow; main absorption site |
| Colon | 5.5–7 | Small area, slow transit; target for colon-specific delivery |
| Rectum | about 7 | Partly avoids the liver (lower rectal veins drain to the systemic blood) |

The small intestine is the main site of absorption for nearly all oral drugs — even weak acids — because its surface area and blood flow far outweigh the pH advantage of the stomach.

## 1.3 Mechanisms of drug absorption

```text
                      Mechanisms of absorption
        ┌──────────────────┬───────────────┬─────────────────────┐
  Passive diffusion   Carrier-mediated   Pore (convective)   Vesicular / other
  (most drugs)        transport          transport           transport
                      ├ facilitated                          ├ pinocytosis
                      │ diffusion                            ├ phagocytosis
                      └ active transport                     ├ receptor-mediated
                        (primary, secondary)                   endocytosis
                                                             └ ion-pair transport
```

### Passive diffusion (non-ionic diffusion)

The drug moves **down its concentration gradient**, needs no energy and no carrier, and cannot be saturated. More than 90% of drugs are absorbed this way. It follows **Fick's first law**:

dQ/dt = D × A × Km/w × (CGIT − C)

where dQ/dt = rate of diffusion, D = diffusion coefficient, A = surface area, Km/w = membrane/water partition coefficient, w (or h) = membrane thickness, CGIT − C = concentration difference across the membrane.

Because blood carries the drug away quickly (C stays near zero — **sink condition**), the rate becomes proportional to CGIT, i.e. **first-order**. Lipophilic, small, un-ionised molecules diffuse fastest.

**pH-partition hypothesis.** Only the un-ionised form of a weak acid or base is lipid-soluble enough to cross the membrane by passive diffusion. Absorption therefore depends on the drug's **pKa**, the **pH** at the absorption site and the **lipid solubility** of the un-ionised form. The fraction un-ionised comes from the Henderson–Hasselbalch equation:

- Weak acid: pH − pKa = log [ionised / un-ionised]
- Weak base: pKa − pH = log [ionised / un-ionised]

**Worked example (example numbers).** A weak acid has pKa 3.5.

- Stomach, pH 1.5: un-ionised fraction = 1 / (1 + 10^(1.5 − 3.5)) = 0.990 → **99.0% un-ionised**.
- Plasma, pH 7.4: un-ionised fraction = 1 / (1 + 10^(7.4 − 3.5)) → **only about 0.013% un-ionised**.
- At equilibrium the un-ionised concentration is the same on both sides, so the total concentration in plasma is about 7,900 times that in gastric fluid (ion trapping).

A weak base with pKa 9 is almost entirely ionised in the stomach (about 0.000003% un-ionised) and still only about 0.3% un-ionised at pH 6.5, yet it is absorbed in the intestine thanks to the huge surface area.

**Limitations of the pH-partition hypothesis**

1. Ignores the very large surface area of the intestine (most acids are still absorbed there).
2. The pH at the membrane surface (micro-climate pH, about 5.3) differs from the bulk lumen pH.
3. Some ionised drugs are absorbed (quaternary compounds partly, by ion-pair formation or pores).
4. Ignores residence time — the drug stays in the intestine much longer than in the stomach.
5. Ignores unstirred water layer, carrier transport and convective (pore) flow.

### Carrier-mediated transport

A membrane protein (carrier) binds the drug, carries it across and releases it. Features: **structural specificity**, **saturation** at high concentration (rate follows Michaelis–Menten kinetics, not first-order), and **competition** between similar molecules.

| Feature | Facilitated diffusion | Active transport |
| --- | --- | --- |
| Direction | Down the gradient | Can go against the gradient |
| Energy (ATP) | Not needed | Needed (primary: ATP direct; secondary: ion gradient, e.g. Na+ or H+ co-transport) |
| Carrier | Yes, saturable | Yes, saturable |
| Inhibited by metabolic poisons | No | Yes |
| Examples | Vitamin B12 (with intrinsic factor), glucose into red cells | Levodopa and methyldopa (amino-acid carriers), 5-fluorouracil, iron, vitamins B1 and B2; peptide carrier (PEPT1) for some cephalosporins and ACE inhibitors |

**Efflux transporters** such as P-glycoprotein (P-gp) pump some drugs back into the gut lumen and reduce their absorption (an active process working the other way).

### Pore transport (convective transport)

Very small water-soluble molecules (molecular weight below about 100–200) pass through water-filled channels, carried with water flow. Examples: urea, water, low-molecular-weight sugars.

### Ion-pair transport

A highly ionised drug forms a neutral complex with an oppositely charged ion in the lumen (for example with mucin or bile salts). The neutral pair is lipophilic enough to diffuse. Quaternary ammonium compounds and some sulfonic acids are absorbed in part this way.

### Vesicular transport (endocytosis)

The membrane folds around the material and pinches off as a vesicle.

- **Pinocytosis** ("cell drinking") — engulfs fluid or dissolved macromolecules: fat-soluble vitamins, some proteins, oral polio vaccine.
- **Phagocytosis** ("cell eating") — engulfs particles.
- **Receptor-mediated endocytosis** — molecules bind a receptor first (for example vitamin B12–intrinsic factor complex).
- **Transcytosis** — vesicle crosses the whole cell and empties on the other side.

## 1.4 Factors influencing drug absorption through the GIT

### A. Physicochemical properties of the drug

| Factor | How it affects absorption |
| --- | --- |
| Drug solubility and dissolution rate | Dissolution is often the slowest (rate-limiting) step for poorly water-soluble drugs (Class II of the BCS) |
| Particle size and surface area | Smaller particles → larger surface → faster dissolution (micronisation of griseofulvin, spironolactone, digoxin) |
| Polymorphism and amorphism | Metastable polymorph and amorphous form dissolve faster than the stable crystal (chloramphenicol palmitate form B better than form A) |
| Solvates and hydrates | Anhydrous form usually dissolves faster than hydrate (anhydrous ampicillin vs trihydrate) |
| Salt form | Sodium/potassium salts of weak acids and hydrochlorides of weak bases dissolve faster |
| pKa and lipophilicity | Decide the un-ionised fraction and membrane permeability; good absorption needs a balance (log P roughly 1–3) |
| Drug stability in GIT | Acid-labile drugs (benzylpenicillin, erythromycin) degrade in the stomach; enteric coating or prodrugs help |
| Complexation | Tetracycline + Ca2+, Mg2+, Al3+, Fe2+ form non-absorbable chelates |
| Adsorption | Charcoal, kaolin and antacids can adsorb drugs and reduce absorption |

**Dissolution — Noyes–Whitney equation**

dC/dt = D × A × (Cs − Cb) / h

D = diffusion coefficient, A = surface area of the dissolving solid, h = thickness of the diffusion (stagnant) layer, Cs = saturation solubility at the surface, Cb = concentration in the bulk. Anything that raises D, A or Cs, or lowers h (stirring, gut motility), speeds dissolution.

### B. Dosage form (pharmaceutical) factors

- **Type of dosage form** — usual order of speed: solution > suspension > capsule > tablet > coated tablet > controlled-release product.
- **Disintegration and dissolution time** of tablets.
- **Excipients:** diluents (hydrophilic ones aid wetting), binders (too much slows disintegration), disintegrants, lubricants (hydrophobic magnesium stearate slows wetting), surfactants (aid wetting and solubilisation), colourants and complexing agents.
- **Manufacturing variables:** compression force, granulation method, drying, coating thickness.
- **Product age and storage:** hardening of tablets and changes in crystal form on storage.

### C. Patient-related (physiological) factors

| Factor | Effect |
| --- | --- |
| Gastric emptying rate | Most drugs are absorbed in the small intestine, so fast emptying gives faster onset. Slowed by fatty meals, cold food, lying on left side, anticholinergics, opioids, diabetes; speeded by fasting, warm liquids, metoclopramide |
| Intestinal transit time | Usually 3–4 h; longer contact helps poorly soluble drugs and drugs absorbed only in one region (riboflavin) |
| GI pH | Changes ionisation, solubility and stability |
| Food | Delays emptying; may increase absorption of lipophilic drugs (griseofulvin with fatty food) or reduce it (tetracycline with milk) |
| Blood flow to the GIT | Keeps sink conditions; reduced in shock and heart failure |
| Disease states | Achlorhydria, malabsorption, Crohn's disease, liver cirrhosis (less first pass) |
| Presystemic (first-pass) metabolism | Gut wall enzymes (CYP3A4), gut bacteria and the liver remove drug before it reaches the systemic blood — glyceryl trinitrate, propranolol, lidocaine |
| Age | Infants: higher gastric pH, irregular emptying; elderly: lower acid, slower motility |

## 1.5 Absorption of drugs from non per oral extravascular routes

Extravascular routes put the drug outside the blood vessels, so an absorption step is needed (unlike IV injection).

| Route | How absorption happens | Advantages | Limitations |
| --- | --- | --- | --- |
| Buccal / sublingual | Passive diffusion through thin, vascular oral mucosa into the jugular vein | Rapid onset, avoids first pass and gastric acid | Only potent, lipophilic, small-dose drugs; taste |
| Rectal | Passive diffusion; lower and middle rectal veins bypass the liver | Useful in vomiting, unconscious patients, children | Erratic absorption, patient dislike |
| Topical / transdermal | Diffusion through the stratum corneum (rate-limiting) by transcellular, intercellular or appendageal paths | Long, steady delivery, avoids first pass | Only potent lipophilic drugs of low molecular weight; skin irritation |
| Intramuscular | Diffusion into capillaries and lymph; depends on blood flow (deltoid > vastus lateralis > gluteal) | Suitable for depot forms | Pain, local damage; oily or suspension forms absorb slowly |
| Subcutaneous | Diffusion into capillaries, slower than IM because blood flow is lower | Self-injection (insulin), depots | Small volumes only |
| Pulmonary (inhalation) | Very large alveolar area, thin membrane, rich blood flow | Fast local and systemic action; avoids first pass | Particle size critical (about 1–5 µm reach the deep lung) |
| Intranasal | Highly vascular mucosa | Rapid; some peptides; avoids first pass | Mucociliary clearance; small volume |
| Ocular | Corneal diffusion | Local action | Tear drainage removes most of the dose; systemic absorption via nasolacrimal duct |
| Vaginal | Mucosal diffusion | Local and some systemic action | Changes with menstrual cycle |

## 1.6 Distribution of drugs

**Distribution** is the reversible transfer of a drug between the blood and extravascular fluids and tissues. Body water is about 60% of body weight (about 42 L in a 70 kg adult): plasma about 3 L, interstitial fluid about 11 L, intracellular fluid about 28 L.

**Factors that decide distribution**

1. Tissue permeability of the drug (physicochemical nature, membrane type).
2. Blood flow (perfusion rate) of the tissue.
3. Binding to plasma proteins and tissue components.
4. Physiological barriers and special tissues.
5. Disease states, age, obesity, pregnancy.

### Tissue permeability of drugs

- **Perfusion rate-limited distribution** — highly lipophilic drugs cross membranes so easily that the blood flow decides how fast the tissue fills. Well-perfused organs (lungs, kidneys, liver, heart, brain) equilibrate first; skin, muscle, fat later. Example: thiopental reaches the brain within seconds and then **redistributes** to muscle and fat, ending its action.
- **Permeability rate-limited distribution** — polar or ionised drugs cross slowly; the membrane decides the rate (brain, CSF).

**Physicochemical drug properties:** molecular size (below about 500–600 Da cross capillaries easily), degree of ionisation at pH 7.4, lipid/water partition coefficient.

**Special barriers**

- **Blood–brain barrier (BBB):** capillary cells have tight junctions and are wrapped by glial cells, with efflux pumps. Only lipophilic un-ionised drugs enter well. Ways to get a drug in: lipophilic prodrug, carrier transport (levodopa via amino-acid carrier), osmotic opening, intranasal route.
- **Placental barrier:** lipophilic drugs below about 1,000 Da cross; this matters for fetal safety.
- **Blood–testis barrier** and the eye's blood–aqueous barrier.

### Apparent volume of distribution (Vd)

Vd is the hypothetical volume of fluid into which the total amount of drug in the body would have to be spread to give the same concentration as in plasma:

Vd = Amount of drug in body / Plasma drug concentration = X / C

It is "apparent" because it need not match a real body space. Example (example numbers): 100 mg in the body, plasma concentration 2 mg/L → Vd = 50 L.

| Vd (70 kg adult) | Meaning | Example drugs |
| --- | --- | --- |
| About 3–5 L | Stays in plasma, highly bound to plasma protein or large molecule | Heparin, warfarin (small Vd) |
| About 14–20 L | Extracellular fluid | Aminoglycosides |
| About 40 L | Total body water | Ethanol, antipyrine |
| Greater than body water (hundreds of litres) | Strongly bound to tissues | Digoxin, chloroquine, amiodarone |

**Relation to binding:** Vd = Vp + Vt × (fu / fut), where Vp and Vt are plasma and tissue water volumes and fu and fut are the unbound fractions in plasma and tissue. Plasma binding lowers Vd; tissue binding raises it.

**Significance:** used to calculate loading doses (Dose = C × Vd), to judge where a drug goes, and to understand why dialysis removes drugs with small Vd better.

## 1.7 Binding of drugs

Binding is usually **reversible** (hydrogen bonds, ionic bonds, van der Waals and hydrophobic forces). Irreversible (covalent) binding is rare and mostly linked to toxicity (reactive paracetamol metabolite binding to liver proteins).

**Only the free (unbound) drug** can cross membranes, act on receptors, be metabolised and be filtered by the kidney. The bound form is a reservoir.

### Plasma protein binding

| Protein | Concentration | Binds mainly | Examples |
| --- | --- | --- | --- |
| Human serum albumin (HSA) | About 3.5–5 g/100 ml (most abundant) | Weak acids and neutral drugs (also some bases) | Warfarin, phenylbutazone, sulfonamides, salicylates, NSAIDs, phenytoin |
| α1-acid glycoprotein (orosomucoid) | Much lower; rises in inflammation, trauma, cancer | Basic drugs | Lidocaine, propranolol, imipramine, quinidine |
| Lipoproteins | Variable | Lipophilic drugs (some bases) | Cyclosporine, some lipophilic drugs |
| Globulins (α, β, γ) | — | Hormones and some vitamins | Transcortin (corticosteroids), thyroxine-binding globulin, transferrin (iron) |
| Red blood cells | — | Some drugs enter or bind to haemoglobin/membrane | Phenytoin, pentobarbital, chlorpromazine |

**Binding sites on albumin:** site I (warfarin site), site II (diazepam/benzodiazepine site), site III (digitoxin site), site IV (tamoxifen site).

### Tissue binding

Drugs can bind to tissue proteins, fats, nucleic acids and bone. Tissue binding raises Vd and often lengthens half-life.

| Tissue | Example |
| --- | --- |
| Liver | Paracetamol reactive metabolite (irreversible), chloroquine |
| Lungs | Basic amines such as imipramine |
| Kidney | Metallothionein binds heavy metals (cadmium, lead) |
| Skin, hair, nails | Griseofulvin (keratin), arsenic |
| Eye | Chloroquine and phenothiazines bind melanin in the retina |
| Bone and teeth | Tetracyclines (chelate calcium; tooth discoloration), lead |
| Fat | Thiopental, DDT, other lipophilic compounds |
| Nucleic acids | Chloroquine, quinacrine |

## 1.8 Factors affecting protein–drug binding

**1. Drug-related factors**

- Physicochemical nature: lipophilic drugs bind more; acids bind albumin, bases bind α1-acid glycoprotein.
- Drug concentration: at high concentration binding sites saturate, so the free fraction rises.
- Affinity of the drug for the protein.

**2. Protein-related factors**

- Physicochemical nature of the protein and number of binding sites.
- Protein concentration: hypoalbuminaemia (liver disease, nephrotic syndrome, burns, malnutrition, old age) increases the free fraction of acidic drugs.

**3. Drug interactions**

- **Displacement:** two drugs compete for one site. Warfarin displaced by phenylbutazone → more free warfarin → bleeding risk. Sulfonamides displace bilirubin in newborns → kernicterus.
- Allosteric changes in the protein.

**4. Patient-related factors**

- Age (neonates have less albumin and bilirubin competes; elderly have less albumin).
- Pregnancy, obesity, inter-subject (genetic) variation.
- Disease: renal failure (uraemic substances and low albumin reduce binding of acids), hepatic failure, inflammation (raises α1-acid glycoprotein → more binding of bases).

## 1.9 Kinetics of protein binding

For a protein P with n identical, independent binding sites and a drug D:

P + D ⇌ PD     Ka = [PD] / ([P][D])

Define r = moles of drug bound per mole of protein = [PD] / [PT]. Then

r = n Ka [D] / (1 + Ka [D])     (Langmuir-type equation)

where [D] is the free drug concentration and Ka is the association constant.

**Linear plots used to find n and Ka**

| Plot | Equation | Axes | Slope | Intercept |
| --- | --- | --- | --- | --- |
| Direct plot | r vs [D] | — | Hyperbola reaching n | — |
| Klotz (double reciprocal / Lineweaver–Burk type) | 1/r = 1/(n Ka [D]) + 1/n | 1/r vs 1/[D] | 1/(n Ka) | y-intercept 1/n |
| Scatchard | r/[D] = n Ka − r Ka | r/[D] vs r | −Ka | y-intercept n Ka; x-intercept n |

**Worked example (example numbers).** A protein has n = 2 sites with Ka = 1 × 10^5 M⁻¹. At free drug concentrations of 1, 5, 10, 20 and 50 µM, r = 0.18, 0.67, 1.00, 1.33 and 1.67. Plotting r/[D] against r gives a straight line falling with slope −1 × 10^5 (= −Ka) and meeting the x-axis at r = 2 (= n). A curved Scatchard plot suggests more than one class of binding sites.

```text
 r/[D]
   │\
nKa│ \           Scatchard plot
   │  \          slope = −Ka
   │   \
   │    \
   └─────\──── r
          n
```

**Methods to measure binding:** equilibrium dialysis (most common reference method), ultrafiltration, ultracentrifugation, gel filtration, and spectroscopic methods.

## 1.10 Clinical significance of protein binding

1. **Absorption:** binding in plasma keeps the free concentration low, maintaining the sink and the concentration gradient.
2. **Distribution:** highly plasma-bound drugs stay mainly in the blood (small Vd); they cross the BBB and placenta less.
3. **Drug action:** only free drug acts. A highly bound drug (more than about 90%) may have a delayed onset but longer action.
4. **Metabolism and excretion:** bound drug is not filtered at the glomerulus and is protected from many enzymes, so elimination is slower and half-life longer (tetracyclines, digitoxin). For drugs with high extraction ratio, active secretion can strip drug from protein.
5. **Displacement interactions:** most important for drugs that are highly bound (above about 95%), have a small Vd and a narrow therapeutic index (warfarin, phenytoin, tolbutamide). Example: 99% bound → 98% bound doubles the free fraction (0.01 → 0.02). Usually the effect is short-lived because the extra free drug is distributed and eliminated.
6. **Diagnosis:** binding of contrast agents to proteins helps imaging; serum albumin levels guide dose adjustment.
7. **Drug design and long action:** strong binding can prolong action (some sulfonamides).
8. **Disease:** low albumin in liver/kidney disease, or high α1-acid glycoprotein after surgery or myocardial infarction, changes the free fraction and the response.

## Remember

- Biopharmaceutics = drug + dosage form + route → rate and extent of absorption.
- Passive diffusion follows Fick's law, is first-order and non-saturable; carrier transport is specific, saturable and shows competition.
- pH-partition hypothesis: un-ionised, lipophilic form is absorbed; but the small intestine absorbs most drugs because of its area and transit time.
- Noyes–Whitney: dC/dt = D A (Cs − Cb)/h — smaller particles, better solubility and wetting speed dissolution.
- Vd = amount in body / plasma concentration; plasma binding lowers it, tissue binding raises it.
- Albumin binds acids (site I warfarin, site II diazepam); α1-acid glycoprotein binds bases.
- Scatchard: r/[D] = nKa − rKa (slope −Ka, x-intercept n); Klotz: 1/r vs 1/[D].
- Only free drug acts, is metabolised and filtered; displacement matters for highly bound, low-Vd, narrow-margin drugs.
