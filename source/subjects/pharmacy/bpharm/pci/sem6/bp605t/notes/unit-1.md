# Unit 1: Recombinant DNA Technology

Recombinant DNA (rDNA) technology is the set of laboratory techniques used to cut, join, copy and express DNA from different sources. The underlying logic is simple: a gene from any organism can be inserted into a host cell and that host can then produce the gene's protein product at scale. Every biopharmaceutical on the market — from recombinant insulin to monoclonal antibodies — depends on the tools described in this unit.

## 1.1 DNA structure review

DNA is a double helix of two antiparallel polynucleotide strands held together by hydrogen bonds between complementary bases: adenine pairs with thymine (two hydrogen bonds) and guanine pairs with cytosine (three hydrogen bonds). The backbone is built from deoxyribose sugar and phosphate groups linked by 3'–5' phosphodiester bonds. The sequence of bases in the coding strand carries the genetic information. RNA is similar but uses ribose, uracil in place of thymine, and is usually single-stranded.

The human genome contains about 3 × 10⁹ base pairs encoding around 25,000 genes. Most DNA in eukaryotic cells is non-coding. Prokaryotes have smaller, circular genomes and no introns.

## 1.2 Restriction endonucleases

Restriction endonucleases (restriction enzymes) are bacterial enzymes that recognise specific short DNA sequences (restriction sites) and cut both strands. They are the molecular scissors of rDNA work.

**Classification:**

| Type | Properties | Use in rDNA |
| --- | --- | --- |
| Type I | Recognise and methylate at one site, cut at a distant random site; require ATP and S-adenosylmethionine | Not used (cut unpredictably) |
| Type II | Recognise a specific palindromic sequence of 4–8 bp and cut at or near that site; require only Mg²⁺ | The workhorse enzyme of all rDNA work |
| Type III | Recognise asymmetric sequences, cut a fixed distance away; require ATP | Not used for routine cloning |

**Type II restriction enzymes in detail.** The recognition sequence is typically a 4–8 bp palindrome — it reads the same on both strands in the 5'→3' direction. For example, EcoRI recognises 5'-GAATTC-3' and cuts between G and A on each strand, producing four-nucleotide single-stranded overhangs called **sticky ends (cohesive ends)**. HindIII and BamHI are other examples. Some enzymes, such as SmaI, cut in the middle of their recognition sequence and produce **blunt ends**.

Sticky ends are essential for cloning because a gene fragment cut with one enzyme can anneal with a vector cut with the same enzyme before ligation.

**Naming convention:** EcoRI = *E. coli* restriction and modification, type I (the first enzyme discovered from that organism).

## 1.3 DNA ligase

DNA ligase seals single-stranded nicks in double-stranded DNA by forming a phosphodiester bond. In rDNA work, **T4 DNA ligase** (from bacteriophage T4) is used to join the sticky ends of an insert and a vector after they have annealed. The reaction requires ATP as an energy source. Without ligase, the annealed ends would fall apart; with it, a covalent recombinant molecule is formed.

## 1.4 Vectors

A vector is a DNA molecule used to carry a foreign gene into a host cell and allow it to replicate and be expressed.

**Features a good cloning vector must have:**

1. An **origin of replication** so it replicates inside the host.
2. **Selectable markers** (usually antibiotic resistance genes) so cells carrying the vector can be selected.
3. A **multiple cloning site (polylinker)** — a short stretch containing many restriction enzyme sites where the insert is placed.
4. Small size, so it is easy to manipulate and enters cells efficiently.

**Types of vectors:**

| Vector | Size of insert | Host | Key features |
| --- | --- | --- | --- |
| Plasmid | Up to 10 kb | Bacteria, yeast | Circular dsDNA; self-replicating; most common for small genes |
| Bacteriophage lambda (λ) | 10–20 kb | *E. coli* | Head-and-tail phage; replaced non-essential genes with insert; high efficiency |
| Cosmid | 35–45 kb | *E. coli* | Plasmid containing the λ cos site; packaged into phage heads for delivery |
| Bacterial artificial chromosome (BAC) | 100–300 kb | *E. coli* | Based on the F plasmid; used for genomic libraries |
| Yeast artificial chromosome (YAC) | Up to 1,000 kb | *S. cerevisiae* | Contains yeast centromere, telomeres and ARS; can hold very large inserts for genome projects |

**Expression vectors** are specialised plasmids that include a strong promoter, ribosome binding site and transcription terminator so that the inserted gene is not just carried but actively expressed as protein.

## 1.5 Steps in gene cloning

Gene cloning means making many identical copies of a gene inside a living cell. The standard steps are:

```text
Step 1: ISOLATION OF DNA
  Lyse cells → extract total DNA → isolate the gene of interest
  (or synthesise it chemically if the protein sequence is known)

Step 2: RESTRICTION DIGESTION
  Cut the DNA and the vector with the SAME restriction enzyme
  → both have complementary sticky ends

Step 3: LIGATION
  Mix insert + vector + T4 DNA ligase + ATP
  → recombinant plasmid formed

Step 4: TRANSFORMATION
  Introduce the recombinant plasmid into competent host cells
  (competent = treated with CaCl₂ or electroporation to make them able to take up DNA)

Step 5: SELECTION
  Plate on agar containing the selection antibiotic → only transformed
  cells grow → blue-white selection (lacZ disruption) or PCR identifies
  clones containing the insert
```

**Blue-white selection** uses the lacZ gene in the multiple cloning site. Insertion of a foreign gene disrupts lacZ, so colonies with an insert remain white in the presence of IPTG and X-gal, while vector-only colonies turn blue. White colonies are picked and confirmed by restriction mapping or PCR.

## 1.6 Polymerase chain reaction (PCR)

PCR is an in-vitro method for amplifying a specific DNA sequence exponentially without cloning it into a cell. It was developed by Kary Mullis in 1983 (Nobel Prize 1993).

**Components needed for PCR:**

| Component | Role |
| --- | --- |
| Template DNA | The source of the sequence to be amplified |
| Two oligonucleotide primers | Short single-stranded DNA (20–30 bases) that flank the region of interest, one complementary to each strand |
| Thermostable DNA polymerase | Usually *Taq* polymerase from *Thermus aquaticus*; stable at 95°C |
| dNTPs (dATP, dCTP, dGTP, dTTP) | Building blocks for new DNA strands |
| Buffer with Mg²⁺ | Mg²⁺ is a cofactor for Taq polymerase |

**Three-step cycle (repeated 25–35 times):**

```text
95°C   DENATURATION   — hydrogen bonds broken; double-stranded DNA separates

55–65°C ANNEALING     — primers bind (hybridise) to their complementary sequences
                        on each single-stranded template

72°C   EXTENSION      — Taq polymerase extends from the 3' end of each primer,
                        synthesising a new complementary strand
```

Each cycle doubles the number of copies. After 30 cycles, one copy of the target becomes 2³⁰ = about 10⁹ copies.

**Applications of PCR:**

- **Diagnosis** of infectious diseases (detection of viral or bacterial DNA/RNA — RT-PCR for RNA viruses)
- **Forensics** (DNA fingerprinting from tiny crime-scene samples)
- **Cloning** (PCR amplification of a gene before insertion into a vector)
- **Prenatal diagnosis** (detection of genetic mutations from fetal cells)
- **Quantitative PCR (qPCR)** for gene expression studies
- **Detection of food adulteration or species identification**

## 1.7 DNA sequencing

**Sanger (dideoxy) method:**

Fred Sanger developed this in the 1970s. It is based on selective incorporation of **dideoxynucleotides (ddNTPs)**, which lack the 3'-OH group needed to form the next phosphodiester bond. When a ddNTP is incorporated, chain extension stops.

```text
Template + primer + dNTPs + small amount of ONE ddNTP (e.g. ddATP)
→ DNA polymerase extends from the primer
→ at every position where A should be incorporated, the chain may
  terminate (ddATP) or continue (dATP)
→ a ladder of fragments, each terminating at a different A position
→ run on polyacrylamide gel or capillary electrophoresis
→ read the size ladder → sequence
```

Modern automated Sanger sequencing uses four fluorescently labelled ddNTPs (each colour for one base) and capillary electrophoresis; a laser reads the fluorescence order as fragments pass a detector.

**Next-generation sequencing (NGS):** Modern platforms (Illumina, Nanopore) sequence millions of DNA fragments simultaneously, allowing whole-genome sequencing in days. The concept relevant for the exam is **massively parallel sequencing** — millions of reads generated at once, then assembled bioinformatically.

## 1.8 Gel electrophoresis and blotting

**Gel electrophoresis** separates DNA or protein molecules by size. DNA is negatively charged at neutral pH, so it migrates toward the positive electrode; smaller fragments travel faster through the gel matrix.

| Feature | Agarose gel | Polyacrylamide gel (PAGE) |
| --- | --- | --- |
| Use | DNA and RNA (100 bp – 20 kb) | Small DNA (sequencing), proteins |
| Resolution | Lower | Higher |
| Running buffer | TAE or TBE | Tris-glycine |
| Visualisation | Ethidium bromide under UV | Coomassie or silver stain (protein) |

**Blotting techniques** transfer separated molecules from the gel to a membrane where they are probed with a labelled complementary molecule:

| Technique | Separates | Probe |
| --- | --- | --- |
| Southern blot | DNA | Labelled DNA or RNA probe |
| Northern blot | RNA | Labelled DNA probe |
| Western blot | Protein | Specific antibody |

**Southern blotting steps:** electrophorese DNA → denature in alkali → transfer to nylon membrane → hybridise with labelled probe → wash → detect (autoradiography or chemiluminescence).

## 1.9 Gene expression systems overview

After a gene is cloned, it must be expressed as protein. The three key systems are:

- **Prokaryotic (bacterial)** — fastest and cheapest; described fully in Unit 2.
- **Eukaryotic (yeast, insect, mammalian)** — needed when the protein requires post-translational modifications (glycosylation, correct disulphide bonds); described in Unit 2.
- **Cell-free systems** — in vitro transcription-translation; used for research and toxic proteins.

The choice of expression system depends on the size, complexity, required modifications, and scale of the target protein.

## Remember

1. Type II restriction enzymes recognise palindromic sequences and cut at or near that site; they are the workhorse enzymes of rDNA technology. Type I and III are not used for routine cloning.
2. Sticky ends produced by the same restriction enzyme on both insert and vector allow complementary annealing and ligation by T4 DNA ligase.
3. Vectors must have an origin of replication, selectable markers and a multiple cloning site.
4. YACs hold the largest inserts (up to 1 Mb), BACs up to 300 kb, cosmids 35–45 kb and plasmids up to 10 kb.
5. PCR cycle = denaturation (95°C) → annealing (55–65°C) → extension (72°C); Taq polymerase is used because it is heat-stable.
6. Sanger sequencing uses ddNTPs to terminate chain extension; modern NGS platforms sequence millions of fragments simultaneously.
7. Southern = DNA probe on DNA blot; Northern = RNA blot; Western = antibody probe on protein blot. "SNoW DRoP" is a mnemonic: S = DNA, N = RNA, W = protein.
8. Blue-white selection distinguishes insert-containing colonies (white) from vector-only colonies (blue) using lacZ disruption with X-gal and IPTG.
