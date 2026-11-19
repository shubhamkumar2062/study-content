# Last-night revision sheet

If you have only an hour, learn these five with their diagrams: **stages of drug discovery + bioisosterism**, **Hansch and Free–Wilson analysis**, **molecular docking (types + scoring + validation)**, **pharmacophore and drug-likeness filters**, and **MM vs QM with energy minimisation**. They cover nearly every 10-mark question.

**Equations to write without thinking**

| Equation | Use |
| --- | --- |
| log(1/C) = −k1(log P)² + k2 log P + k3σ + k4Es + k5 | Hansch (parabolic) |
| log P₀ = k2 ÷ (2k1) | Optimum lipophilicity |
| π_X = log P(R–X) − log P(R–H) | Substituent lipophilicity |
| σ_X = log K_X − log K_H; log(k_X/k_H) = ρσ | Hammett constant and equation (ρ = 1.00 for benzoic acid) |
| Es = log(k_X/k_CH3), acid-catalysed hydrolysis | Taft steric constant (CH3 = 0) |
| BA = μ + Σ aᵢXᵢ | Free–Wilson |
| MR = [(n²−1)/(n²+2)](MW/d) | Molar refractivity |
| Tc = c/(a + b − c) | Tanimoto similarity |
| N2/N1 = exp(−ΔE/RT) | Conformer populations |
| ΔG° = −2.303RT log K | Affinity and free energy |

**Numbers that appear as one-mark questions**

| Item | Value |
| --- | --- |
| Lipinski's rule of five | MW ≤ 500, log P ≤ 5, HBD ≤ 5, HBA ≤ 10 (fails if two are broken) |
| Veber | rotatable bonds ≤ 10, PSA ≤ 140 Å² |
| Rule of three (fragments) | MW < 300, log P ≤ 3, HBD ≤ 3, HBA ≤ 3 |
| Successful re-docking | RMSD ≤ 2 Å from the crystal pose |
| Acceptable QSAR model | r² > 0.8, q² > 0.5, 5 compounds per descriptor |
| Homology modelling template | ideally > 30 % sequence identity |
| Ethane rotational barrier | about 3 kcal/mol (12 kJ/mol) |
| CoMFA grid spacing | about 2 Å |
| Tanimoto "similar" | about 0.85 and above |
| RT at 25 °C | about 0.59 kcal/mol |

**Unit 1 in one minute.** Target identification → validation → hit → lead → optimisation → preclinical → Phase I/II/III → approval → Phase IV. Lead = confirmed, modifiable activity. Six routes to a lead: traditional medicine, random screening (HTS), non-random screening, serendipity, drug metabolism, clinical observation. Isostere = same number and arrangement of valence electrons; bioisostere = similar properties and similar biological action. Classical: monovalent (H/F, OH/NH2), divalent (O/S/NH/CH2), trivalent (CH=/N=), tetravalent, ring equivalents (benzene/thiophene/pyridine). Non-classical: tetrazole for COOH, sulphonamide for carbonyl, cyclic for non-cyclic. Case studies: uracil → 5-fluorouracil; H2 antagonist ring changes (imidazole → furan → thiazole); COOH → tetrazole in losartan.

**Unit 2 in one minute.** Activity is always log(1/C). SAR qualitative, QSAR quantitative and needs a congeneric series. Parameters: lipophilic (log P, π), electronic (σ, σ*, pKa, HOMO/LUMO), steric (Es, MR, STERIMOL L and B1–B5), topological (connectivity indices). log P by shake-flask or HPLC; calculated by fragment methods (Rekker, Hansch–Leo). Hansch = linear free energy related, additive contributions; parabolic form gives an optimum log P. Free–Wilson = additive group contributions, cannot extrapolate to a new substituent. Report n, r², s, F, q². 3D-QSAR: CoMFA (steric + electrostatic, Lennard-Jones and Coulomb, cut-offs, PLS, green/yellow and blue/red contours) and CoMSIA (five Gaussian similarity fields: steric, electrostatic, hydrophobic, H-bond donor and acceptor; smoother maps, no cut-offs). Alignment is the weak point.

**Unit 3 in one minute.** Virtual screening funnel: library → filters → ligand-based or structure-based → ranked hits → test. Drug-likeness: Lipinski, Veber, Ghose, lead-likeness, PAINS/REOS filters, ligand efficiency. Pharmacophore features: HBD, HBA, hydrophobic, aromatic ring, positive and negative ionisable, plus exclusion volumes; mapping is ligand based (align actives, find common features) or structure based (from the complex). Docking = search algorithm + scoring function; pose = position + orientation + conformation. Rigid (lock and key) → flexible ligand (standard) → both flexible (induced fit); manual docking by hand on graphics. Search: incremental construction, Monte Carlo, genetic algorithm, simulated annealing. Scoring: force-field, empirical, knowledge-based, consensus. Validate by re-docking (RMSD ≤ 2 Å), cross-docking and enrichment. De novo design: linking and growing strategies inside the site; main problem is synthetic accessibility. FBDD screens fragments by NMR, SPR or X-ray.

**Unit 4 in one minute.** Bioinformatics = biological macromolecules (BLAST with its E-value, Clustal, homology modelling validated by a Ramachandran plot). Chemoinformatics = small molecules (SMILES, SMARTS, InChI/InChIKey, SDF/MOL2, fingerprints MACCS and ECFP, Tanimoto similarity, substructure search). Databases: PDB and CSD (structures), UniProt and GenBank (sequences), PubChem and ChemSpider (compounds), ChEMBL and BindingDB (measured activities), ZINC (purchasable, 3D-ready), DrugBank (drugs with targets and metabolism), KEGG and Reactome (pathways), BRENDA (enzymes), CAS/SciFinder and Reaxys (literature and reactions), CTRI and ClinicalTrials.gov (trials). ADMET tools: admetSAR, SwissADME, pkCSM; endpoints include solubility, Caco-2 permeability, BBB, P-gp, CYP inhibition, hERG, Ames. Curation and standardisation of data come before any model.

**Unit 5 in one minute.** MM = classical balls and springs, no electrons, fast, cannot break bonds. Force field = bond stretch + angle bend + torsion + out-of-plane + van der Waals (Lennard-Jones 12-6) + electrostatic (Coulomb); MM2/MM3, AMBER, CHARMM, OPLS, GROMOS, MMFF94. QM = ab initio (HF, basis sets STO-3G, 6-31G*), semi-empirical (CNDO, INDO, MINDO, MNDO, AM1, PM3), DFT (B3LYP), QM/MM; gives charges, HOMO/LUMO, MEP maps. Minimisation: steepest descent (first derivative, robust, slow at the end), conjugate gradient (first derivative, no zig-zag), Newton–Raphson (second derivative/Hessian, fast near the minimum, expensive); all downhill only → nearest local minimum. Conformational analysis: 3N − 6 degrees of freedom, 3ⁿ combinations for n rotatable bonds, PES with minima and barriers, ethane staggered/eclipsed, butane anti > gauche > syn, cyclohexane chair. Global search: systematic grid, Monte Carlo (Metropolis), simulated annealing, molecular dynamics, genetic algorithm, distance geometry, low-mode search. The bioactive conformation need not be the global minimum.

**Ten likely one-liners**

1. Expand QSAR, SAR, CADD, CoMFA, CoMSIA, ADMET, PDB, SMILES, InChI, HTS, FBDD.
2. Who gave the partition coefficient–activity idea? Meyer and Overton. The σ constant? Hammett. Es? Taft. The LFER model? Hansch and Fujita. The additive model? Free and Wilson.
3. Reference substituent for σ = hydrogen; for Es = methyl.
4. ρ of benzoic acid ionisation = 1.00.
5. Solvent pair for log P = n-octanol and water.
6. Cut-off for "two or more violations" = Lipinski's rule of five.
7. Statistic for leave-one-out cross-validation = q².
8. A pharmacophore is not a functional group or a molecule — it is a pattern of features with distances.
9. Lock and key = rigid docking; induced fit = flexible protein docking.
10. The three classical bioisostere groups asked most: OH/NH2 (monovalent), O/S/NH/CH2 (divalent), benzene/thiophene/pyridine (ring equivalents).
