# Unit 1: Introduction to medicinal chemistry, physicochemical properties and drug metabolism

Medicinal chemistry is the branch of pharmacy that studies drugs as **chemical structures**: how a molecule is built, what its physical properties are, how it reaches the receptor, what it does there, and how the body takes it apart again. This unit gives the vocabulary used in the rest of the subject, so read it first and come back to it whenever a later unit says "because of the partition coefficient" or "this is a bioisostere".

## 1.1 History and development of medicinal chemistry

Early medicine used whole plants and minerals. Chemistry entered when workers began isolating the single substance responsible for the effect.

| Period | What happened | Why it mattered |
| --- | --- | --- |
| Up to 1800 | Crude drugs: opium, cinchona bark, belladonna, ephedra | Activity known, chemistry unknown; dose varied with the batch |
| 1805–1830 | Morphine isolated from opium, then quinine, strychnine, atropine, caffeine | Proof that one pure compound carries the activity: the start of the alkaloid era |
| 1850–1900 | Synthetic organic chemistry grows: chloroform and ether as anaesthetics, acetylsalicylic acid, phenacetin, antipyrine, barbital (1903) | Drugs could now be made, not only harvested |
| Early 1900s | Ehrlich's work on selective staining and arsenicals; the idea of a "magic bullet" and of receptors | Birth of the receptor concept and of planned chemotherapy |
| 1930s–1940s | Prontosil leads to sulphonamides; penicillin developed for use | The first true antibacterials; metabolism to an active form recognised |
| 1950s–1970s | Antihistamines, phenothiazines, benzodiazepines, beta blockers, H2 blockers | Systematic structure modification; SAR becomes a working method |
| 1980s onward | Receptor cloning, enzyme crystal structures, computer-aided design, combinatorial chemistry, biotechnology products | Rational design replaces much of the trial-and-error screening |

**Terms used in this subject**

- **Drug**: a chemical substance that produces a biological response, used for diagnosis, prevention, treatment or cure.
- **Lead compound**: a molecule with useful but imperfect activity, used as the starting point for modification.
- **Structure–activity relationship (SAR)**: how a change in structure changes the biological effect.
- **Pharmacophore**: the arrangement of groups and distances a molecule must have to fit its receptor.
- **Prodrug**: an inactive derivative converted in the body to the active drug (for example enalapril to enalaprilat).

## 1.2 Physicochemical properties in relation to biological action

A drug must dissolve in the gut fluid, cross lipid membranes, travel in blood and still bind its target. These demands pull in opposite directions, and the properties below describe the compromise.

### Ionization

Most drugs are weak acids or weak bases. The fraction ionized is given by the Henderson–Hasselbalch equation:

- Weak acid: pH = pKa + log([A⁻]/[HA])
- Weak base: pH = pKa + log([B]/[BH⁺])

```text
Stomach pH 1–3        Intestine pH 6–8        Plasma pH 7.4
Weak acid (aspirin)   mostly unionized →      more ionized →        ionized, trapped in plasma
Weak base (atropine)  mostly ionized  →       less ionized →        partly unionized
```

- Only the **unionized** form crosses lipid membranes easily; the **ionized** form usually binds the receptor in drugs that act at an anionic site (for example the quaternary nitrogen of acetylcholine).
- Weak acids are therefore absorbed partly from the stomach, weak bases mainly from the intestine.
- **Ion trapping**: a weak acid that crosses into plasma (pH 7.4) ionizes and cannot easily return; this is used in aspirin poisoning, where urine alkalinization speeds excretion.
- Quaternary ammonium drugs (neostigmine, ipratropium) are permanently charged: poor oral absorption, no entry into the brain, but useful when only a peripheral effect is wanted.

### Solubility

A drug must have both water solubility (to dissolve and travel) and lipid solubility (to cross membranes). Adding polar groups (–OH, –COOH, –NH2, –SO3H) raises water solubility; adding alkyl, halogen or aromatic rings raises lipid solubility. Salt formation (hydrochlorides of bases, sodium salts of acids) is the usual way to make an injectable solution.

### Partition coefficient

**P = concentration in n-octanol / concentration in water**, usually quoted as log P.

- Activity in most series rises with log P, reaches a maximum and then falls (a parabola). The best log P for central activity is around 2; very lipophilic drugs are trapped in fat and bound to protein.
- Hansch used log P with electronic (σ) and steric (Es) constants to correlate structure with activity quantitatively.
- Examples: thiopental is far more lipid-soluble than pentobarbital and enters the brain within seconds; the quaternary neostigmine has a negative log P and stays outside the brain.

### Hydrogen bonding

A hydrogen bond (about 1–7 kcal/mol) forms between an H attached to N or O and a lone pair on another N or O.

- It holds a drug on its receptor (for example the phenolic –OH groups of adrenaline on the beta receptor).
- Too many hydrogen-bonding groups keep the drug in water and block membrane passage. As a rough guide, oral drugs rarely have more than 5 donors and 10 acceptors.
- Intramolecular hydrogen bonding has the opposite effect: it hides polar groups inside the molecule and raises lipid solubility.

### Protein binding

Acidic drugs bind mainly to **albumin**, basic drugs to **α1-acid glycoprotein**. Binding is reversible:

Drug + Protein ⇌ Drug–Protein complex

- Only the **free** fraction is active, filtered by the kidney and able to be metabolised.
- High binding gives a long duration (phenylbutazone, warfarin) and a small apparent volume of distribution.
- Displacement from the binding site raises free drug suddenly: sulphonamides displacing bilirubin in the newborn, or aspirin displacing warfarin.

### Chelation

A **chelate** is a ring formed when a ligand donates two or more pairs of electrons to one metal ion.

| Chelating drug | Metal | Use |
| --- | --- | --- |
| EDTA (calcium disodium) | Lead | Lead poisoning; also a preservative aid |
| Dimercaprol (BAL) | Arsenic, mercury, gold | Heavy-metal antidote |
| Penicillamine | Copper | Wilson's disease |
| Desferrioxamine | Iron | Iron overload |
| Tetracyclines (unwanted) | Ca, Mg, Al, Fe | Chelation with milk or antacids blocks absorption and stains teeth |

Natural chelates include haemoglobin (iron) and chlorophyll (magnesium).

### Bioisosterism

**Bioisosteres** are groups with similar size, shape or electron distribution that can replace one another and keep (or usefully change) the activity.

| Type | Examples |
| --- | --- |
| Classical, monovalent | –H / –F; –OH / –NH2 / –SH; –Cl / –Br / –CF3 |
| Classical, divalent | –O– / –S– / –NH– / –CH2– |
| Classical, trivalent | –N= / –CH= |
| Ring equivalents | Benzene / thiophene / pyridine |
| Non-classical | –COOH replaced by tetrazole, sulphonamide or hydroxamic acid; ester replaced by amide |

Uses: 5-fluorouracil (F for H) acts as an antimetabolite; replacing –O– by –S– in phenothiazines and in sulphonamide analogues changes potency and duration; losartan uses a tetrazole in place of an acid group for better absorption.

### Optical isomerism

When a carbon carries four different groups the molecule exists as two non-superimposable mirror images (enantiomers). The receptor is itself chiral, so the two usually differ:

- Levo-adrenaline is about 10 times more active than the dextro form.
- (S)-ibuprofen is the active COX inhibitor; the (R) form is largely converted to (S) in the body.
- Levodopa is active and is carried by an amino-acid transporter; the D form is not.
- **Easson–Stedman hypothesis**: the more active enantiomer makes three-point contact with the receptor; the other can manage only two.

### Geometrical isomerism

Restricted rotation about a double bond or a ring places groups cis or trans, changing the distance between pharmacophoric groups.

- Diethylstilbestrol: the trans isomer matches the oestrogen receptor; the cis form is much weaker.
- Cis-flupenthixol is the active antipsychotic isomer.
- In the antihistamine triprolidine and in similar drugs, only one geometric form gives good activity.

## 1.3 Drug metabolism

Metabolism (biotransformation) converts lipid-soluble drugs into more water-soluble products that the kidney can excrete. The liver microsomal enzymes, chiefly **cytochrome P450**, do most of the work.

### Phase I reactions (functionalisation)

Phase I introduces or unmasks a polar group (–OH, –NH2, –SH, –COOH). The product may be inactive, still active, or even more active.

| Reaction | Example |
| --- | --- |
| Aromatic hydroxylation | Phenytoin → p-hydroxyphenytoin; propranolol → 4-hydroxypropranolol (active) |
| Aliphatic hydroxylation | Pentobarbital, ibuprofen side chain |
| N-dealkylation | Diazepam → nordazepam; imipramine → desipramine (active) |
| O-dealkylation | Codeine → morphine (active) |
| S-dealkylation and S-oxidation | Chlorpromazine sulphoxide |
| N-oxidation | Trimethylamine, chlorpromazine N-oxide |
| Deamination | Adrenaline and other amines by monoamine oxidase |
| Desulphuration | Thiopental → pentobarbital; parathion → paraoxon (more toxic) |
| Hydrolysis of esters and amides | Aspirin → salicylic acid; procaine by plasma esterase; lidocaine by amidase (slower) |
| Reduction (nitro, azo, carbonyl) | Chloramphenicol nitro group; prontosil → sulphanilamide |

### Phase II reactions (conjugation)

Phase II attaches a large polar endogenous molecule, almost always giving an inactive, readily excreted product.

| Conjugation | Cofactor | Group attacked | Example |
| --- | --- | --- | --- |
| Glucuronidation (commonest) | UDP-glucuronic acid | –OH, –COOH, –NH2, –SH | Morphine, paracetamol, chloramphenicol |
| Sulphation | PAPS | Phenols, alcohols, amines | Paracetamol, steroids (saturable) |
| Glycine / glutamine conjugation | Coenzyme A | Carboxylic acids | Salicylic acid → salicyluric acid; benzoic acid → hippuric acid |
| Glutathione conjugation | Glutathione | Epoxides, quinones | Paracetamol's toxic NAPQI metabolite |
| Acetylation | Acetyl-CoA | Aromatic –NH2, –SO2NH2, hydrazines | Isoniazid, sulphonamides, dapsone |
| Methylation | S-adenosylmethionine | Catechols, amines, thiols | Adrenaline by COMT; noradrenaline; histamine |

Note that acetylation and methylation *reduce* water solubility; acetylated sulphonamides can crystallise in the kidney, which is why older sulphonamides were given with plenty of fluid.

### Factors affecting drug metabolism

1. **Species and strain** differences: results in rats cannot be moved straight to humans.
2. **Age**: newborns have immature glucuronidation (chloramphenicol "grey baby" syndrome); the elderly have reduced liver blood flow and enzyme activity.
3. **Sex and hormones**: some oxidations differ between men and women.
4. **Genetics (pharmacogenetics)**: fast and slow acetylators of isoniazid; CYP2D6 poor metabolisers for debrisoquine and many antidepressants; plasma cholinesterase variants and succinylcholine apnoea.
5. **Enzyme induction**: phenobarbitone, rifampicin, carbamazepine, phenytoin and smoking raise enzyme levels, lowering the effect of other drugs over days to weeks.
6. **Enzyme inhibition**: cimetidine, ketoconazole, erythromycin and grapefruit juice raise the levels of co-administered drugs quickly.
7. **Disease**: liver disease, heart failure (reduced hepatic flow) and thyroid disease alter rates.
8. **Diet, environment and route**: protein content, charcoal-grilled food, insecticides, and the first-pass effect of the oral route.
9. **Dose and saturation**: phenytoin, salicylate and ethanol show saturation (zero-order) kinetics at therapeutic doses.

### Stereochemical aspects of metabolism

- **Substrate stereoselectivity**: enzymes work faster on one enantiomer. S-warfarin is oxidised by CYP2C9, R-warfarin by other routes.
- **Product stereoselectivity**: a prochiral centre may be converted mainly to one enantiomer, as when ketones are reduced to a single alcohol enantiomer.
- **Chiral inversion**: R-ibuprofen is converted in the body to the active S form; the reverse does not happen.
- **First-pass stereoselectivity**: for propranolol the two enantiomers are cleared at different rates, so the ratio in plasma differs from the ratio in the tablet.

## Remember

1. Only the unionized form crosses membranes; the ionized form often binds the receptor.
2. Activity usually peaks at an intermediate log P (around 2 for CNS drugs), not at the highest value.
3. Only free (unbound) drug acts, is filtered and is metabolised.
4. Bioisosteres swap groups of similar size or electronic nature: –COOH for tetrazole, –O– for –S–, H for F.
5. Phase I adds or exposes a polar group; phase II attaches a polar partner. Acetylation and methylation are the two conjugations that do not increase water solubility.
6. Induction (phenobarbitone, rifampicin) is slow to start and slow to wear off; inhibition (cimetidine, ketoconazole) is fast.
7. Chirality matters at every step: levo-adrenaline, S-ibuprofen, levodopa, S-warfarin.
