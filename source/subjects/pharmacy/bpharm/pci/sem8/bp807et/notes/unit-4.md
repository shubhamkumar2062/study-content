# Unit 4: Informatics and methods in drug design

Every method in the earlier units needs data — protein sequences and structures, molecular structures, measured activities, measured ADME properties. Informatics is the organised storage, retrieval and analysis of that data. Two branches matter for drug design: **bioinformatics** (biological molecules — DNA, RNA, proteins) and **chemoinformatics** (small molecules and their properties).

## 4.1 Introduction to bioinformatics

**Bioinformatics** is the use of computer methods to store, retrieve, analyse and interpret biological data, mainly nucleic acid and protein sequences, structures and functions.

**Why a drug designer needs it**

| Task | Bioinformatics tool |
| --- | --- |
| Find and choose a target | Genome and proteome databases, disease–gene links |
| Check how similar the target is to other human proteins | Sequence alignment — predicts selectivity problems and side effects |
| Get the 3D structure | Structure databases; if none exists, build a homology model |
| Find the binding site | Structural comparison with related proteins, cavity detection |
| Understand pathways | Pathway and interaction databases |
| Personalised medicine | Polymorphism data (for example variation in drug-metabolising enzymes) |

**Core ideas**

- **Sequence alignment** — writing two or more sequences one under the other to show matching residues. *Pairwise* alignment compares two sequences; *multiple* alignment compares several and shows conserved regions. **BLAST** is the standard fast search tool: it compares a query sequence with a whole database and reports similar sequences with scores and E-values (a low E-value means the match is unlikely to be chance). **Clustal** type programs do multiple alignment.
- **Homology (comparative) modelling** — building the 3D structure of a protein from the known structure of a related protein. Steps: find a template with high sequence identity (ideally above 30 %), align target and template, copy the conserved backbone, build loops and side chains, energy minimise, then validate (Ramachandran plot, stereochemistry checks). Used when no experimental structure exists — very common for G-protein coupled receptors and for many bacterial and parasite enzymes.
- **Structural genomics and proteomics** — large-scale determination of structures and of the protein complement of a cell.
- **Phylogenetic analysis** — evolutionary trees; useful to see whether a parasite enzyme has a close human relative (if not, a selective drug is more likely).

### Important biological databases

| Database | Holds |
| --- | --- |
| GenBank (NCBI), EMBL-ENA, DDBJ | Nucleotide sequences; the three exchange data daily |
| UniProt (Swiss-Prot reviewed + TrEMBL unreviewed) | Protein sequences with curated annotation |
| Protein Data Bank (PDB, run by the wwPDB with RCSB, PDBe and PDBj) | Experimentally determined 3D structures of proteins and nucleic acids (X-ray, NMR, cryo-EM) |
| Cambridge Structural Database (CSD) | Small-molecule crystal structures — bond lengths, angles, preferred conformations |
| Pfam, InterPro | Protein families and domains |
| SCOP, CATH | Structural classification of proteins |
| KEGG, Reactome | Metabolic and signalling pathways |
| BRENDA | Enzyme data — substrates, inhibitors, kinetics |
| PubMed / MEDLINE | Biomedical literature |
| Ensembl, UCSC Genome Browser | Genome annotation |

A PDB entry is identified by a four-character code and contains the atomic coordinates, the resolution, the R-factor, the bound ligands (HETATM records) and the crystallographic water. Resolution matters: below about 2.0 Å the structure is detailed enough for careful docking; above 3.0 Å side-chain positions are uncertain.

## 4.2 Introduction to chemoinformatics

**Chemoinformatics (cheminformatics)** is the application of computer methods to chemical problems: representing, storing, searching and analysing chemical structures and their biological and physical data.

### Representing a molecule in a computer

| Representation | What it is | Example / note |
| --- | --- | --- |
| Connection table | List of atoms and the bonds between them | The basis of MOL and SDF files |
| **SMILES** | A single line of text for a structure | Ethanol CCO; benzene c1ccccc1; aspirin CC(=O)Oc1ccccc1C(=O)O |
| **SMARTS** | A pattern language for substructure searching | Used to write filters for unwanted groups |
| **InChI / InChIKey** | A standard, non-proprietary identifier; the InChIKey is a fixed-length hashed version | Good for looking a compound up across databases |
| MOL / SDF | Single and multiple structure files with coordinates and data fields | The usual exchange format for libraries |
| MOL2, PDB | Formats carrying 3D coordinates, atom types and charges | Used by docking programs |
| Fingerprints | A string of bits recording which fragments are present | MACCS keys (fixed set of substructures), path-based and circular (ECFP) fingerprints |

### Searching

- **Exact search** — the same compound (best done through InChIKey or a canonical SMILES).
- **Substructure search** — all compounds containing a given fragment; uses graph matching, speeded up by screening with fingerprints first.
- **Similarity search** — compounds "like" a query. Similarity between two fingerprints is usually the **Tanimoto coefficient**: Tc = c ÷ (a + b − c), where a is the number of bits set in molecule A, b in molecule B and c the number set in both. Tc runs from 0 to 1; above about 0.85 with a good fingerprint, two molecules are usually considered similar. The **similar property principle** says structurally similar molecules usually have similar properties — the basis of ligand-based screening, but it fails at "activity cliffs", where a tiny change destroys activity.
- **Pharmacophore and 3D shape search** — described in Unit 3.

### Other chemoinformatics jobs

- Library design (diverse libraries, focused libraries, combinatorial enumeration).
- Calculation of descriptors and properties (log P, PSA, pKa, solubility).
- Duplicate removal, salt stripping, tautomer and protonation standardisation — the unglamorous but essential cleaning of data.
- Clustering and diversity analysis, so that the compounds bought represent the whole chemical space.
- Data mining of screening results and electronic laboratory notebooks.

## 4.3 ADME databases and predictive tools

ADME (absorption, distribution, metabolism, excretion) and toxicity data decide whether an active molecule can ever become a medicine. Databases collect measured values; predictive tools estimate them from structure.

**Properties stored or predicted**

| Step | Typical parameters |
| --- | --- |
| Absorption | Aqueous solubility, log P and log D, PSA, Caco-2 or MDCK permeability, human intestinal absorption, P-glycoprotein substrate/inhibitor |
| Distribution | Plasma protein binding, volume of distribution, blood–brain barrier penetration |
| Metabolism | Cytochrome P450 isoform (CYP1A2, 2C9, 2C19, 2D6, 3A4) substrate and inhibitor status, metabolic sites, half-life |
| Excretion | Renal clearance, total clearance |
| Toxicity | hERG inhibition (QT prolongation risk), Ames mutagenicity, hepatotoxicity, skin sensitisation, acute toxicity class |

**Resources commonly named in textbooks**

| Resource | Content |
| --- | --- |
| admetSAR | Collected ADMET data with prediction models |
| SwissADME | Free web calculation of physicochemical properties, drug-likeness, pharmacokinetic behaviour |
| pkCSM | Predicts ADMET endpoints from graph-based signatures |
| DrugBank | Drug entries combining chemistry, pharmacology, targets, metabolism and interactions |
| Metrabase, drug metabolism databases | Transporter and metabolism data |
| PharmGKB | Pharmacogenomic data — how genetic variation changes drug response |
| PubChem (BioAssay section) | Screening results, including toxicity assays |

**How these are used:** apply them as filters right after drug-likeness screening, and again on the final docking hits; a potent compound predicted to block hERG, to be a strong CYP3A4 inhibitor or to be mutagenic is deprioritised before any chemistry is done. Remember that these are *predictions* with limited accuracy, especially for metabolism; they guide experiments, they do not replace them.

## 4.4 Chemical, biochemical and pharmaceutical databases

| Type | Database | Content |
| --- | --- | --- |
| Chemical | **PubChem** (NCBI) | Very large open collection of compound structures, properties and bioassay results |
| Chemical | **ChemSpider** | Open structure search across many sources |
| Chemical | **CAS Registry / SciFinder** | Every compound indexed with a CAS Registry Number; the commercial standard for literature and reaction searching |
| Chemical | **Reaxys** (formerly Beilstein and Gmelin) | Reactions, preparations and measured properties |
| Chemical | **ZINC** | Commercially available compounds, ready-prepared in 3D for virtual screening |
| Chemical | **Cambridge Structural Database** | Small-molecule crystal structures |
| Biochemical / bioactivity | **ChEMBL** | Measured bioactivities (IC50, Ki, EC50) from the medicinal chemistry literature, linked to targets |
| Biochemical / bioactivity | **BindingDB** | Measured binding affinities of ligand–protein pairs |
| Biochemical | **BRENDA**, **KEGG**, **Reactome** | Enzymes, pathways, reactions |
| Biochemical / structure | **PDB**, **PDBbind** | Structures; PDBbind adds measured affinities for complexes |
| Target | **Therapeutic Target Database**, **SuperTarget** | Known and explored drug targets with their drugs |
| Pharmaceutical | **DrugBank** | Approved and investigational drugs: structure, target, mechanism, pharmacokinetics, interactions |
| Pharmaceutical | **USFDA Orange Book**, **Drugs@FDA**, national regulatory databases | Approved products, patents and exclusivity, labelling |
| Pharmaceutical | Pharmacopoeias in electronic form (IP, BP, USP) | Official standards, monographs, tests |
| Clinical | **ClinicalTrials.gov**, **CTRI (Clinical Trials Registry – India)** | Registered clinical trials and their results |
| Safety | **VigiBase / national pharmacovigilance databases** | Reports of suspected adverse drug reactions |
| Natural products | Natural product collections, including Indian ones such as **IMPPAT** for Indian medicinal plant phytochemicals | Structures and sources of natural compounds |
| Literature | **PubMed**, **Google Scholar** | Published papers and abstracts |

**Choosing a database for a task**

```text
Need a 3D protein structure          -> PDB
Need many purchasable molecules in 3D -> ZINC
Need measured IC50 / Ki values        -> ChEMBL, BindingDB
Need drug + target + metabolism facts -> DrugBank
Need any compound's properties quickly-> PubChem, ChemSpider
Need a synthesis route                -> Reaxys, SciFinder
Need pathway context                  -> KEGG, Reactome
Need ADMET estimates                  -> admetSAR, SwissADME, pkCSM
```

### Quality of data

Databases differ in **curation**. Curated resources (Swiss-Prot, ChEMBL, DrugBank) have been checked by people; automatically assembled resources have more errors — wrong stereochemistry, wrong salt forms, duplicate entries, activities recorded in mixed units. Before any QSAR or machine-learning work, data must be standardised: one entry per compound, one unit for activity, salts and solvates stripped, tautomers normalised, suspicious values checked against the original paper. A QSAR model is only as good as the numbers it is fitted to.

## 4.5 Putting informatics into the design cycle

```text
Disease  -> genomics / proteomics          -> target chosen         (bioinformatics)
Target   -> PDB or homology model          -> binding site defined  (bioinformatics)
Site     -> ZINC / in-house library        -> virtual screening     (chemoinformatics)
Hits     -> ChEMBL, BindingDB              -> known SAR checked     (chemoinformatics)
Leads    -> ADMET tools, DrugBank          -> liabilities predicted (ADME databases)
Candidate-> CTRI / ClinicalTrials.gov      -> trial planned
```

## Remember

1. Bioinformatics handles biological macromolecules; chemoinformatics handles small molecules.
2. BLAST = fast sequence similarity search, judged by score and E-value; Clustal-type programs do multiple alignment.
3. Homology modelling needs a template, ideally above 30 % sequence identity, and is validated with a Ramachandran plot.
4. PDB = 3D structures of macromolecules (four-character code, resolution matters); CSD = small-molecule crystal structures.
5. Structure representations: SMILES (line notation), SMARTS (search patterns), InChI/InChIKey (standard identifier), SDF/MOL2/PDB (files with coordinates), fingerprints (MACCS, ECFP).
6. Tanimoto coefficient Tc = c/(a + b − c); the similar property principle underlies similarity searching, and activity cliffs are its exception.
7. ChEMBL and BindingDB hold measured affinities; ZINC holds purchasable compounds ready for docking; DrugBank links drugs, targets and metabolism; PubChem is the large open general resource.
8. Predicted ADMET (solubility, permeability, CYP, hERG, Ames) is a filter, not a measurement — clean, curated data is the foundation of every model.
