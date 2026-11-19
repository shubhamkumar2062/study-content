# Unit 1: Drug discovery, lead discovery and analog based drug design

Making a new medicine is a long, costly and uncertain project. Out of many thousands of compounds that chemists make or buy, only a handful ever reach a patient. Computer aided drug design (CADD) exists to cut down this waste: it helps a team choose which molecules are worth making and testing. Before you can use the computational tools in later units, you need the map of the whole journey — where a **lead** comes from, how it is improved, and what "analog based drug design" means.

## 1.1 Stages of drug discovery and development

```text
Target identification  ->  Target validation  ->  Hit/lead discovery
        -> Lead optimisation -> Preclinical studies -> IND application
        -> Clinical trials Phase I -> II -> III -> Marketing approval
        -> Phase IV (post-marketing surveillance)
```

| Stage | What is done | Typical output |
| --- | --- | --- |
| Target identification | Find the enzyme, receptor, ion channel, transporter or nucleic acid whose change causes or controls the disease | A named biological target |
| Target validation | Prove that acting on the target really changes the disease (knockout animals, antisense, tool compounds, clinical genetics) | A "druggable", validated target |
| Assay development | Build a reliable in-vitro test (enzyme inhibition, binding, cell assay) | Screening assay |
| Hit identification | Screen libraries (HTS), natural products, virtual screening, fragment screening | Hits: compounds with measurable activity |
| Lead identification | Confirm hits, check they are real and reproducible, build simple SAR | One or a few lead series |
| Lead optimisation | Improve potency, selectivity, solubility, metabolic stability and safety by making analogs | Preclinical candidate |
| Preclinical | Pharmacology, pharmacokinetics, toxicology in animals, formulation, stability | Data package for the regulator |
| Clinical trials | Phase I safety in healthy volunteers, Phase II efficacy in patients, Phase III large comparative trials | Evidence for approval |
| Regulatory review | Dossier submitted to CDSCO (India), USFDA, EMA | Marketing authorisation |
| Phase IV | Post-marketing surveillance, pharmacovigilance | Long-term safety information |

Useful definitions to quote in the exam:

- **Target** — the macromolecule in the body with which a drug interacts to produce its effect.
- **Hit** — a compound that shows the wanted activity in a screening assay, usually weak.
- **Lead** — a compound with confirmed, reproducible activity, a known structure, acceptable early properties, and clear scope for chemical modification. It is not yet a drug.
- **Drug candidate** — the optimised molecule chosen to go into preclinical and clinical development.
- **Pharmacophore** — the arrangement in space of the structural features needed for activity.

Why the early stages matter so much: a molecule rejected at the design stage costs almost nothing, while one rejected in Phase III costs a fortune. CADD shifts the decision-making to the cheap end of the pipeline, and also reduces the number of animals used.

## 1.2 Rational approaches to lead discovery

**(a) Leads from traditional medicine (ethnopharmacology).** Plants used for centuries in Ayurveda, Siddha, Unani and folk practice are screened for the active principle, which then becomes a lead. Classic examples: reserpine from *Rauwolfia serpentina* (used for hypertension), artemisinin from *Artemisia annua* for malaria, quinine from cinchona bark, morphine from opium, digitalis glycosides from foxglove, and vinca alkaloids from *Catharanthus roseus*. Advantage: human use already suggests both activity and some safety. Limitation: isolating and identifying the true active constituent is slow, and yields are often poor.

**(b) Random screening (blind screening).** Every available compound — synthetic, microbial broth, plant extract — is tested in an assay without any prior reason to expect activity. This was the route to many antibiotics, for example streptomycin from soil actinomycetes. Modern high throughput screening (HTS) is random screening done by robots on hundreds of thousands of wells per day, with miniaturised plates and automated readout. Advantage: no assumptions, so genuinely new chemotypes appear. Limitation: very expensive, large hit lists full of false positives (aggregators, assay interferers).

**(c) Non-random (targeted or directed) screening.** Only compounds that have some structural or mechanistic reason to work are screened — analogs of a known active, compounds from a focused library built around a pharmacophore, or molecules from a related therapeutic class. The hit rate is far higher than with random screening, but the chemical novelty is lower.

**(d) Serendipitous discovery.** An unexpected observation is followed up intelligently. Examples: penicillin, when mould contamination cleared a bacterial plate; the hypoglycaemic effect noticed during sulphonamide use, which led to the sulphonylureas; the mood-lifting effect seen with an antitubercular agent, which pointed to the MAO inhibitors; minoxidil's hair growth and sildenafil's effect observed during cardiovascular trials. Serendipity "favours the prepared mind" — the observation has to be recognised as important.

**(e) Lead discovery based on drug metabolism.** A metabolite may be more active, longer acting or safer than the parent. Then the metabolite itself is developed. Examples of this logic: the conversion of an inactive precursor to an active species (prodrug thinking in reverse), oxazepam and desmethyldiazepam as active metabolites of benzodiazepines, fexofenadine as the active metabolite of terfenadine with a better cardiac safety profile, and acetaminophen (paracetamol) as a metabolite of acetanilide and phenacetin. Metabolism studies also warn of **toxic** metabolites, letting the chemist block the vulnerable position.

**(f) Lead discovery based on clinical observation.** A drug given for one indication shows a useful side effect, which becomes the new indication. Examples: aspirin's antiplatelet action, the use of an antiepileptic for neuropathic pain, the discovery of diuretic and antidiabetic actions from sulphonamide therapy, and the anti-angina nitrates. This is also the basis of **drug repurposing**, where an approved drug is re-tested for a new disease — attractive because its safety and pharmacokinetics are already known.

## 1.3 Analog based drug design

Once a lead exists, the chemist makes **analogs** — close structural relatives — to learn which parts of the molecule matter and to improve the profile. The study of how changes in structure change activity is the **structure–activity relationship (SAR)**.

Common analog strategies:

| Strategy | What is changed | Purpose |
| --- | --- | --- |
| Homologation | Lengthening or shortening a chain by –CH2– units | Tune lipophilicity and fit |
| Chain branching | Straight to branched chain | Change potency and metabolism |
| Ring variation | Open a chain into a ring, expand, contract or fuse rings | Lock conformation, improve selectivity |
| Introduction of substituents | –Cl, –F, –CH3, –OCH3, –NO2, –NH2 | Change electronic and steric properties |
| Stereochemistry | Separate enantiomers, use a rigid analog | Improve potency, cut off-target effects |
| Isosteric/bioisosteric replacement | Swap one group for another of similar properties | Keep activity, improve ADME or patent position |
| Prodrug formation | Add a cleavable group | Improve absorption, taste, stability or site delivery |

## 1.4 Bioisosterism

**Isosteres** (Langmuir) are atoms, ions or molecules with the same number of atoms and the same number and arrangement of valence electrons, so they have similar physical properties — for example N2 and CO, or N3− and NCO−.

**Bioisosteres** are groups or molecules that have similar physical or chemical properties and produce **broadly similar biological effects**. Bioisosteric replacement means exchanging one such group for another in a lead to improve potency, selectivity, duration, solubility or safety, or to get around a patent.

### Classification

**1. Classical bioisosteres** (Grimm's hydride displacement law and Erlenmeyer's extension):

| Class | Examples |
| --- | --- |
| Monovalent | –H and –F; –OH and –NH2; –Cl, –Br, –SH, –CF3 (pseudo-halide) |
| Divalent | –O–, –S–, –NH–, –CH2– |
| Trivalent | –CH= and –N= ; –P= and –As= |
| Tetravalent | =C=, =Si=, =N+=, =P+= |
| Ring equivalents | Benzene, thiophene, pyridine, furan, pyrrole |

**2. Non-classical bioisosteres** — the groups do not obey the electron-count rules but still mimic each other's shape, charge distribution or hydrogen bonding:

- Cyclic and non-cyclic replacements: an open chain replaced by a ring that holds the same geometry.
- Acid replacements for –COOH: tetrazole, sulphonamide, hydroxamic acid, acylsulphonamide, phosphonic acid.
- Carbonyl replacements: –C(=O)– by –SO2– or by a sulphoxide.
- Amide replacements: ester, retro-amide, 1,2,4-oxadiazole, olefin.
- Hydrogen replaced by fluorine (similar size, very different electronegativity, blocks metabolism).

### Why bioisosteric replacement is done

1. Increase potency by better fit or better electronics.
2. Improve selectivity between related receptor subtypes.
3. Block a metabolic soft spot (for example put F where hydroxylation occurs).
4. Improve aqueous solubility or membrane permeability.
5. Remove a toxic or unstable group.
6. Produce a patentable new structure.

### Three case studies

**Case study 1 — Fluorine for hydrogen in 5-fluorouracil.** Uracil is the natural pyrimidine. Replacing the hydrogen at position 5 with fluorine gives a molecule the enzyme thymidylate synthase accepts, but the strong C–F bond cannot be broken in the normal way, so the enzyme is blocked. A monovalent classical bioisostere converts a nutrient into an anticancer agent.

**Case study 2 — Ring bioisosterism in the H2 antagonists.** The imidazole ring of histamine was replaced in a stepwise programme: first an imidazole-containing antagonist, then replacement of the ring by furan, and later by a thiazole ring, giving ranitidine and famotidine respectively, together with replacement of the thiourea group by nitroethenediamine and guanidine-type groups. Potency rose and the unwanted effects of the earlier agents fell.

**Case study 3 — Carboxylic acid replaced by tetrazole in the sartans.** The angiotensin II receptor blockers began with carboxylic acid leads that were poorly absorbed. Replacing –COOH with a tetrazole ring (similar pKa and charge, but more lipophilic and metabolically stable) gave orally active drugs such as losartan. This is the standard textbook example of a non-classical acid bioisostere.

(Other acceptable case studies: sulphonamide to sulphonylurea; procaine to lidocaine, where the ester is replaced by the more stable amide; thiophene for benzene in several NSAIDs.)

## 1.5 Where computers enter

- Target validation — bioinformatics, sequence and structure databases (Unit 4).
- Hit finding — virtual screening and docking instead of, or alongside, HTS (Unit 3).
- Lead optimisation — QSAR models guide which analog to make next (Unit 2).
- Property prediction — drug-likeness and ADMET filters remove likely failures early.
- Conformational analysis and energy minimisation give the three-dimensional shapes everything else depends on (Unit 5).

## Remember

1. Order of stages: target identification → validation → hit → lead → optimisation → preclinical → Phase I–III → approval → Phase IV.
2. Hit = weak activity in a screen; lead = confirmed, modifiable, with early SAR; candidate = optimised molecule entering development.
3. Six routes to a lead: traditional medicine, random screening (HTS), non-random screening, serendipity, drug metabolism, clinical observation.
4. Isostere = same number and arrangement of valence electrons; bioisostere = similar properties **and** similar biological action.
5. Classical bioisosteres are grouped as monovalent, divalent, trivalent, tetravalent and ring equivalents; non-classical ones include tetrazole for –COOH and sulphonamide for carbonyl.
6. Keep three case studies ready: 5-fluorouracil (H → F), the H2 antagonist ring changes, and –COOH → tetrazole in losartan.
7. Repurposing an approved drug is fast because safety and pharmacokinetics are already known.
