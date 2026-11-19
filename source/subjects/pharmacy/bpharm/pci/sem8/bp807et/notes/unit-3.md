# Unit 3: Molecular modelling and virtual screening techniques

High throughput screening tests real compounds in real plates. **Virtual screening** tests them inside a computer first, so only the promising ones are bought or synthesised. This unit covers the filters (drug-likeness), the two main search strategies (pharmacophore based and docking based), and the way a molecule can be built from nothing inside the binding site (de novo design).

## 3.1 Virtual screening: the idea

**Virtual screening (VS)** is the computational search of a large compound library for molecules most likely to bind a given target, so that a small, enriched subset goes forward for biological testing.

```text
Library (10^5 - 10^7 compounds)
        |  filters: unwanted groups, drug-likeness, duplicates
        v
Filtered library
        |
        +---- ligand-based VS (similarity, pharmacophore, QSAR)  ... when no protein structure
        |
        +---- structure-based VS (docking)                        ... when the 3D structure is known
        v
Ranked hit list (10^2 - 10^3)
        |  visual inspection, chemical sense, diversity, availability
        v
Purchase / synthesise and test (10 - 100 compounds)
```

| | Ligand-based VS | Structure-based VS |
| --- | --- | --- |
| Needs | One or more known active ligands | 3D structure of the target (X-ray, NMR, cryo-EM or a homology model) |
| Methods | 2D similarity, fingerprints, pharmacophore search, shape matching, QSAR | Molecular docking and scoring |
| Speed | Very fast | Slower (seconds to minutes per molecule) |
| Finds new scaffolds? | Yes, through "scaffold hopping" | Yes |
| Main weakness | Biased towards the known actives | Scoring functions are approximate; protein flexibility and water are hard |

Advantages of VS over HTS: much cheaper, uses no compound and no reagent, can screen compounds that have not yet been made, and gives a structural hypothesis for why a hit works. Weaknesses: false positives and false negatives, dependence on the quality of the structure, and the fact that a computed score is not a measured affinity.

## 3.2 Drug-likeness screening

Before any expensive calculation, obviously unsuitable molecules are removed. **Drug-likeness** is the extent to which a molecule's properties resemble those of known oral drugs.

**Lipinski's rule of five** (a molecule is likely to have poor oral absorption or permeation if two or more of these are broken):

| Property | Limit |
| --- | --- |
| Molecular weight | not more than 500 |
| log P (calculated) | not more than 5 |
| Hydrogen bond donors (sum of OH and NH) | not more than 5 |
| Hydrogen bond acceptors (sum of N and O) | not more than 10 |

Exceptions are important to mention: natural products, antibiotics, antifungals, vitamins and substrates of active transporters often break the rules and are still good drugs. The rule is about **passive** oral absorption, not about potency.

**Veber's rules** (oral bioavailability in the rat): rotatable bonds ≤ 10 and polar surface area ≤ 140 Å² (or total hydrogen bonds ≤ 12).

**Other common filters**

| Filter | Content |
| --- | --- |
| Ghose filter | MW 160–480, log P −0.4 to 5.6, molar refractivity 40–130, 20–70 atoms |
| Lead-likeness | Smaller and less lipophilic than drugs (MW ≤ 350, log P ≤ 3), leaving room for optimisation |
| Rule of three (fragments) | MW < 300, log P ≤ 3, HBD ≤ 3, HBA ≤ 3, rotatable bonds ≤ 3 |
| REOS / PAINS filters | Remove reactive, unstable or promiscuous groups (Michael acceptors, quinones, rhodanines, catechols, epoxides, acyl halides) that give false positives |
| Ligand efficiency | LE = ΔG ÷ number of heavy atoms; keeps hits small and efficient |

**ADMET prediction** also belongs here: predicted solubility, Caco-2 or MDCK permeability, blood–brain barrier penetration, plasma protein binding, cytochrome P450 inhibition and substrate status, hERG channel blockade (cardiac risk), Ames mutagenicity and hepatotoxicity alerts. Using these early is called "failing fast and failing cheap"; the principle is that poor pharmacokinetics and toxicity, not lack of potency, cause most late-stage failures.

## 3.3 Pharmacophore mapping and pharmacophore based screening

**Pharmacophore** (IUPAC): the ensemble of steric and electronic features that is necessary to ensure the optimal supramolecular interactions with a specific biological target and to trigger (or block) its biological response. In plain words — the pattern of features, and the distances between them, that a molecule must carry to be active. It is an abstraction, **not** a real molecule and not a functional group list.

**Typical pharmacophoric features**

| Feature | Usual symbol / colour | Examples in a molecule |
| --- | --- | --- |
| Hydrogen bond donor (HBD) | Violet / D | –OH, –NH, –NH2 |
| Hydrogen bond acceptor (HBA) | Green / A | C=O, ring N, ether O |
| Hydrophobic (H) | Cyan / yellow | Alkyl chain, phenyl, halogen |
| Aromatic ring / ring aromatic (RA) | Orange | Benzene, pyridine |
| Positive ionisable (PI) | Red | Protonated amine, guanidine |
| Negative ionisable (NI) | Blue | –COO−, tetrazole, phosphate |
| Exclusion volume | Grey sphere | Space occupied by the protein — ligand atoms are forbidden here |

```text
A simple three-point pharmacophore

        HBA
         |  5.2 A
         |
   PI ---+--------- HYD
      7.8 A      6.4 A

A molecule matches if it can place a hydrogen bond acceptor, a positive
ionisable centre and a hydrophobic group at these mutual distances
(within a tolerance, usually about 1 - 1.5 A) in one low-energy conformation.
```

### Pharmacophore mapping (model generation)

**Ligand based** (no protein structure):

1. Collect a set of active molecules, ideally chemically diverse but acting at the same site, with measured activity.
2. Generate many low-energy conformers of each.
3. Superimpose (align) the molecules and look for features common to all.
4. Build the hypothesis: features plus distances plus tolerances.
5. Score and rank the hypotheses, usually by how well they separate actives from inactives.
6. Validate: test against a set of known actives mixed with decoys; measure enrichment.

**Structure based** (protein structure or a ligand–protein complex available): identify the interactions the bound ligand makes in the crystal structure (hydrogen bonds, salt bridge, hydrophobic contacts) and convert them into features; add exclusion volumes from the protein atoms. A pharmacophore built from the empty site alone is called a site-point or apo pharmacophore.

**Pharmacophore based screening:** the hypothesis becomes a 3D query. Every library compound is tested — can it present these features at these distances in some accessible conformation (conformers worked out on the fly or stored in a multi-conformer database)? Matching molecules are kept and ranked by fit value.

**Uses:** fast screening of millions of compounds; **scaffold hopping** (finding a chemically different core that presents the same features, useful for patents and for improving properties); building focused libraries; and as a filter before docking.

**Limitations:** depends on correct alignment and on the set of conformers used; may miss actives whose features sit slightly outside the tolerance; gives no estimate of affinity by itself.

## 3.4 Molecular docking

**Docking** predicts the preferred position, orientation and conformation (together called the **pose**) of a ligand inside the binding site of a macromolecule, and estimates the strength of the interaction with a **scoring function**.

Two parts of every docking program:

1. **Search algorithm** — explores the possible poses (translations, rotations, and for a flexible ligand, the torsions).
2. **Scoring function** — gives each pose a number meant to reflect binding affinity.

### Preparing for docking

```text
Protein                          Ligand
-------                          ------
Get structure (PDB) or build     Draw / retrieve structure
a homology model                 Generate 3D coordinates
Remove water (keep conserved     Add hydrogens, set the correct
waters if they bridge)           protonation and tautomer
Add hydrogens, assign charges    Assign charges, set stereochemistry
Fix missing residues/loops       Energy minimise
Choose and define the grid box
around the active site
```

### Types of docking

| Type | Protein | Ligand | Comment |
| --- | --- | --- | --- |
| **Rigid docking** (rigid body) | Rigid | Rigid | The oldest approach; the lock-and-key model. Only six degrees of freedom (3 translations + 3 rotations). Very fast, used for shape matching of large databases, and for protein–protein docking. Misses any pose that needs the ligand to change shape. |
| **Flexible ligand docking** | Rigid | Flexible | The standard method today. The induced-fit problem is only partly addressed, but it is a good compromise between accuracy and speed. |
| **Flexible docking (both flexible)** | Flexible (side chains, sometimes loops) | Flexible | Closest to reality (induced fit), but very demanding. Handled by soft potentials, rotamer libraries for side chains, induced-fit protocols, or by docking into several structures (ensemble docking). |
| **Manual docking** | — | — | The user places the ligand in the site by hand with interactive graphics, guided by chemical knowledge and real-time energy feedback, then minimises. Useful for a single well-understood complex and for teaching; not practical for screening and subject to personal bias. |

**How ligand flexibility is handled**

| Approach | Method |
| --- | --- |
| Systematic | Incremental construction: anchor a rigid fragment, then grow the rest bond by bond; or a systematic torsion search |
| Stochastic / random | Monte Carlo, simulated annealing, genetic algorithms (population of poses, crossover and mutation, fitness = score), tabu search |
| Ensemble | Pre-generate many conformers and dock each one rigidly |
| Simulation | Molecular dynamics and energy minimisation inside the site |

### Scoring functions

| Class | Based on | Examples / notes |
| --- | --- | --- |
| Force-field based | Sum of van der Waals, electrostatic and sometimes solvation terms from a molecular mechanics force field | Physically clear, but desolvation and entropy are poorly treated |
| Empirical | Weighted sum of terms (hydrogen bonds, ionic contacts, hydrophobic contact area, rotatable bonds frozen) with weights fitted to measured affinities of known complexes | Fast; depends on the training set |
| Knowledge-based | Statistical potentials from the frequency of atom-pair contacts observed in the PDB | Robust and fast; implicitly includes effects hard to model |
| Consensus | Combine several scoring functions and keep compounds ranked well by most of them | Reduces the chance of a single function's systematic error |

**Validation of a docking protocol**

- **Re-docking:** remove the ligand from a crystal complex and dock it back. Success is usually taken as **RMSD ≤ 2 Å** from the crystal pose.
- **Cross-docking:** dock a ligand into a structure solved with a different ligand.
- **Enrichment:** dock known actives mixed with decoys and check how many actives appear in the top few per cent (enrichment factor, ROC curve).

**Docking based screening** is simply docking applied to a whole library: filter → dock in a fast mode → re-dock the best few per cent in a careful mode → consensus scoring → visual inspection by a chemist → buy and test.

**Limitations of docking:** scoring functions correlate only moderately with measured affinity (good at ranking poses, weak at ranking molecules); protein flexibility and ordered water molecules are simplified; entropy and desolvation are approximate; protonation and tautomer choices change the result. Always treat a docking score as a hypothesis to be tested in the laboratory.

## 3.5 De novo drug design

**De novo design** builds a brand-new ligand inside the binding site atom by atom or fragment by fragment, instead of searching an existing library.

Steps:

1. Analyse the site — shape, hydrophobic pockets, hydrogen bonding groups, charges.
2. Place **hot spots** or probe fragments where favourable interactions are predicted.
3. **Build** the molecule by one of two strategies:
   - **Linking:** place several fragments in their best sub-pockets, then join them with a suitable linker (the fragment-linking approach).
   - **Growing:** start from one anchored fragment and add atoms or groups stepwise, scoring at each step.
   - (Atom-based growth is possible but gives molecules that are hard to synthesise.)
4. Score and rank the structures built.
5. Filter for drug-likeness and, crucially, for **synthetic accessibility**.
6. Make the best designs and test them.

**Advantages:** truly novel structures (so new patent space), good shape complementarity with the site, useful when libraries contain nothing suitable.

**Limitations:** many of the molecules built cannot realistically be synthesised; scoring errors are magnified because nothing is based on a known active; results depend heavily on the quality of the structure used.

**Fragment based drug design (FBDD)** is the experimental cousin: screen very small fragments (rule of three) by biophysical methods such as NMR, surface plasmon resonance, thermal shift or X-ray crystallography; they bind weakly but efficiently, and are then grown, linked or merged into a lead. Ligand efficiency is the guiding number.

## 3.6 Putting the methods together

| Situation | Best approach |
| --- | --- |
| Protein structure unknown, several actives known | Ligand-based: pharmacophore, similarity, QSAR |
| Protein structure known, no ligand known | Structure-based: docking, de novo design |
| Both known | Structure-based pharmacophore, docking validated by re-docking, then QSAR on the hits |
| Need a new scaffold for patent reasons | Pharmacophore based scaffold hopping, or de novo design |
| Library of millions, limited computer time | Filter → pharmacophore screen → dock the survivors |

## Remember

1. Virtual screening ranks compounds in the computer so that only an enriched subset is tested; ligand-based needs known actives, structure-based needs the 3D target.
2. Lipinski: MW ≤ 500, log P ≤ 5, HBD ≤ 5, HBA ≤ 10 — about passive oral absorption, with well-known exceptions. Veber adds rotatable bonds ≤ 10 and PSA ≤ 140 Å².
3. A pharmacophore is a pattern of features (HBD, HBA, hydrophobic, aromatic, positive and negative ionisable) with distances and tolerances, plus exclusion volumes — never a real molecule.
4. Docking = search algorithm + scoring function; output is a pose plus a score.
5. Rigid (lock and key) → flexible ligand (standard) → both flexible (induced fit); manual docking is done by hand on graphics.
6. Scoring functions: force-field, empirical, knowledge-based, consensus.
7. Re-docking success is judged by RMSD ≤ 2 Å against the crystal pose; screening success by enrichment factor.
8. De novo design grows or links fragments inside the site; its main practical problem is synthetic accessibility.
