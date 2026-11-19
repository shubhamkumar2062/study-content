# Unit 4: Bioinformatics

Modern biology produces huge amounts of data: whole genomes, protein sequences and three-dimensional protein structures. **Bioinformatics** uses computers to store, search and make sense of these data. For pharmacy it matters because drug targets, disease genes and vaccine candidates are now found by searching databases before any experiment is done. This unit covers the introduction, objectives, databases and core concepts of bioinformatics and its impact on vaccine discovery.

## 4.1 Introduction and definition

**Bioinformatics** is the field that applies computer science, mathematics and statistics to biological data, especially DNA, RNA and protein sequences and structures, in order to store them, retrieve them, analyse them and interpret what they mean.

It combines three subjects:

```text
          BIOLOGY
     (genes, proteins,
       cells, disease)
            /\
           /  \
          / BIO-\
         /INFOR- \
        / MATICS  \
       /____________\
 COMPUTER          MATHEMATICS
 SCIENCE           AND STATISTICS
 (databases,       (algorithms, probability,
  programming)      scoring)
```

**Why it grew**

- DNA sequencing became faster and cheaper; the **Human Genome Project** (completed in 2003) produced the sequence of about 3 billion base pairs of human DNA.
- The data are far too large to study by hand.
- The Internet allowed public databases shared by laboratories worldwide.

**Related terms**

| Term | Meaning |
| --- | --- |
| Genome | The complete DNA of an organism |
| Genomics | Study of whole genomes: sequencing, mapping and comparing them |
| Proteome / proteomics | All the proteins made by a cell or organism / their study |
| Transcriptomics | Study of all RNA transcripts (which genes are switched on) |
| Pharmacogenomics | How a person's genes affect their response to drugs |
| Computational biology | Building models and simulations of biological systems (closely overlapping field) |

## 4.2 Objectives of bioinformatics

1. **Organise and store** biological data in databases so that researchers can reach them.
2. **Develop tools and algorithms** to analyse the data (sequence alignment, structure prediction, gene finding).
3. **Analyse and interpret** data to understand biological meaning: gene function, protein structure and evolutionary relationships.
4. **Compare** sequences between species to find related genes and proteins.
5. **Predict** protein structure and function from sequence.
6. **Support drug discovery and vaccine design** by finding targets, antigens and suitable molecules.
7. **Support personalised medicine** by linking genetic differences to disease and drug response.

## 4.3 Concept of bioinformatics

The central idea: biological information flows from DNA to RNA to protein (the **central dogma**), and every step can be read and studied as a sequence of letters.

```text
DNA  (letters A, T, G, C)  ──transcription──►  mRNA (A, U, G, C)
                                                   │ translation
                                                   ▼
                                    Protein (20 amino acids, one-letter codes)
                                                   │ folding
                                                   ▼
                                    3D structure  →  function  →  drug target
```

**Main activities**

1. **Sequence analysis**
   - **Sequence alignment** — lining up two or more sequences to find similar regions. **Pairwise alignment** compares two; **multiple sequence alignment** compares many (Clustal Omega, MUSCLE).
   - **Global alignment** compares sequences over their whole length (Needleman–Wunsch method); **local alignment** finds the best matching part (Smith–Waterman method).
   - **Database similarity searching** with **BLAST** (Basic Local Alignment Search Tool) or FASTA finds sequences in a database that resemble a query sequence.
   - **Homology** — similar sequences often come from a common ancestor and have similar functions, so the function of a new gene can be guessed from a known one.
2. **Gene finding and annotation** — locating genes in a raw genome and labelling what they do.
3. **Phylogenetic analysis** — building evolutionary trees from sequences to show how organisms or strains are related (used to trace virus outbreaks).
4. **Structural bioinformatics** — predicting the 3D shape of proteins (homology modelling; machine-learning structure prediction tools), studying binding sites and docking drugs into them.
5. **Functional genomics** — studying gene expression (microarrays, RNA sequencing).
6. **Systems biology** — modelling networks of genes, proteins and metabolic pathways.

**File format example — FASTA** (a common text format for sequences):

```text
>sp|P01308|INS_HUMAN Insulin
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKT...
```

The first line starts with ">" and gives the identifier and description; the following lines give the sequence.

## 4.4 Bioinformatics databases

A **biological database** is an organised, searchable collection of biological data, usually free online.

### Classification

| Type | What it holds | Examples |
| --- | --- | --- |
| **Primary (archival) databases** | Original data submitted directly by researchers (raw sequences, structures) | GenBank, ENA, DDBJ, Protein Data Bank (PDB) |
| **Secondary (derived) databases** | Information derived from primary data after analysis: patterns, motifs, domains, families | PROSITE, Pfam, PRINTS, InterPro |
| **Composite databases** | Combine several primary databases into one search | UniProt (partly), NCBI's linked databases |
| **Specialised databases** | Focus on one organism, disease or data type | OMIM (human genetic disorders), KEGG (pathways), DrugBank (drugs and targets), IEDB (immune epitopes) |
| **Literature databases** | Published articles | PubMed |

### Nucleotide sequence databases

The three main DNA databases exchange data every day as the **International Nucleotide Sequence Database Collaboration (INSDC)**, so a sequence submitted to one appears in all three:

| Database | Run by |
| --- | --- |
| **GenBank** | NCBI (National Center for Biotechnology Information), USA |
| **ENA** (European Nucleotide Archive) | EMBL–EBI (European Bioinformatics Institute), UK |
| **DDBJ** (DNA Data Bank of Japan) | National Institute of Genetics, Japan |

### Protein databases

- **UniProt** — the main protein sequence and function resource. It contains **UniProtKB/Swiss-Prot** (manually reviewed and annotated, high quality) and **UniProtKB/TrEMBL** (automatically annotated, not reviewed).
- **PDB (Protein Data Bank)** — 3D structures of proteins and nucleic acids solved by X-ray crystallography, NMR and cryo-electron microscopy. Each structure has a four-character PDB ID.
- **PROSITE** and **Pfam** — protein families, domains and functional patterns.

### Other useful resources

| Resource | Use |
| --- | --- |
| NCBI Entrez | One search across many NCBI databases (nucleotide, protein, PubMed, gene) |
| KEGG | Metabolic and signalling pathways, diseases, drugs |
| OMIM | Human genes and genetic disorders |
| PubChem | Small molecules and their biological activities |
| DrugBank | Drugs with their targets, mechanisms and interactions |
| BLAST (tool at NCBI) | Finding similar sequences |

**Uses of databases in pharmacy:** finding the sequence and structure of a drug target, checking whether a target exists in humans (to avoid side effects of antimicrobial drugs), finding gene variants that change drug metabolism (pharmacogenomics), and searching for antigens for vaccines.

## 4.5 Applications of bioinformatics (overview)

- **Drug discovery** — target identification and validation, virtual screening, structure-based design.
- **Pharmacogenomics and personalised medicine** — dose or drug chosen by the patient's genes (for example variants of drug-metabolising enzymes).
- **Vaccine discovery** — see 4.6.
- **Diagnosis** — identifying disease-causing mutations and pathogens by their sequences.
- **Microbiology** — tracking resistance genes and outbreak strains.
- **Agriculture and biotechnology** — improved crops, enzyme engineering.
- **Evolution studies** — comparing genomes across species.

## 4.6 Impact of bioinformatics in vaccine discovery

A **vaccine** contains an antigen (or the genetic code for it) that trains the immune system to recognise a pathogen. The classical way of making vaccines (grow the organism, then kill or weaken it, or purify its parts) is slow and fails for organisms that cannot be grown easily or that vary a lot. Bioinformatics has changed vaccine discovery in several ways.

### 1. Reverse vaccinology

Instead of starting in the laboratory, scientists **start from the pathogen's genome** on the computer:

```text
Sequence the pathogen genome
        ↓
Predict all the proteins (open reading frames)
        ↓
Select likely antigens by computer:
  - surface-exposed or secreted proteins (signal peptides, membrane anchors)
  - present in many strains (conserved)
  - not similar to human proteins (to avoid autoimmunity)
        ↓
Make the selected proteins and test them in animals
        ↓
Best candidates go to vaccine development
```

Reverse vaccinology was first used successfully for **Neisseria meningitidis serogroup B** (meningococcus B), whose surface sugar could not be used as an antigen; computer screening of its genome found protein antigens that were later used in a licensed vaccine.

### 2. Epitope prediction (immunoinformatics)

An **epitope** is the small part of an antigen recognised by an antibody (B-cell epitope) or by a T cell (T-cell epitope, presented on HLA/MHC molecules). Programs predict which peptides are likely to be epitopes, and which HLA types will present them, so that **epitope-based** or **multi-epitope vaccines** can be designed. The **Immune Epitope Database (IEDB)** stores known epitopes and prediction tools.

### 3. Comparing strains and tracking variation

Alignment and phylogenetic trees show which parts of a pathogen stay the same across strains (good vaccine targets) and which keep changing. This is used every year to choose **influenza** strains for the seasonal vaccine and to watch new variants of viruses.

### 4. Faster vaccines for new diseases

When a new virus appears, its genome can be sequenced and shared in public databases within days. During the COVID-19 pandemic the SARS-CoV-2 sequence was shared publicly early in 2020, and developers used it directly to design **mRNA** and viral-vector vaccines encoding the spike protein, without needing to grow the virus first.

### 5. Structure-based vaccine design

3D structures (PDB) and modelling help engineer antigens that keep the shape the immune system should recognise (for example stabilising a viral protein in its pre-fusion form).

### 6. Safety and other uses

- Checking candidate antigens for similarity to human proteins and for allergen-like sequences.
- Predicting population coverage of epitopes across HLA types.
- Analysing immune responses in trials and monitoring vaccine effectiveness against new strains.

**Benefits of bioinformatics in vaccine discovery:** faster discovery (years reduced), lower cost, ability to target organisms that cannot be cultured, wider strain coverage and more rational, safer design. **Limitation:** every computer prediction must still be confirmed in the laboratory, in animals and in clinical trials.

## Remember

- Bioinformatics = biology + computer science + mathematics/statistics applied to sequence and structure data.
- Objectives: store, develop tools, analyse, compare, predict structure/function, aid drug and vaccine discovery.
- Central dogma: DNA → RNA → protein → structure → function.
- Alignment: pairwise vs multiple; global (Needleman–Wunsch) vs local (Smith–Waterman); BLAST searches databases.
- Primary databases: GenBank (NCBI), ENA (EMBL–EBI), DDBJ (Japan) — INSDC; PDB for structures. Secondary: PROSITE, Pfam. UniProt: Swiss-Prot (reviewed) + TrEMBL (unreviewed).
- Vaccine discovery: reverse vaccinology (meningococcus B), epitope prediction (IEDB), strain comparison (influenza), rapid genome sharing (COVID-19 mRNA vaccines), structure-based antigen design.
