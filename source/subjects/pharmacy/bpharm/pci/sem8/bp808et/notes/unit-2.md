# Unit 2: DNA, RNA and the flow of genetic information

This unit covers DNA and the flow of molecular information, how DNA works (replication, repair and mutation), DNA and RNA, the types of RNA, and transcription and translation.

## 2.1 DNA and the flow of molecular information

Genetic information flows in one main direction, called the **central dogma**:

```text
          replication
            (DNA → DNA)
              ↺
            DNA  ──transcription──→  RNA  ──translation──→  Protein
              ↖                      |
               └── reverse transcription (retroviruses, telomerase)
                   RNA replication (some RNA viruses): RNA → RNA
```

- **Replication** copies DNA before cell division so each daughter cell gets a full set of genes.
- **Transcription** copies one gene of DNA into RNA.
- **Translation** reads the base sequence of messenger RNA in groups of three (codons) and joins amino acids into a protein.

A **gene** is a segment of DNA that codes for a functional product — a protein or a functional RNA. The full DNA of an organism is its **genome**. The human genome has about 3 × 10^9 base pairs per haploid set and roughly 20,000 protein-coding genes; only about 1–2% of it codes for protein.

### Evidence that DNA is the genetic material

1. **Griffith (1928):** heat-killed virulent (S) pneumococci turned live harmless (R) bacteria into virulent ones — something was transferred.
2. **Avery, MacLeod and McCarty (1944):** the transforming activity was destroyed by DNase but not by protease or RNase, so it was DNA.
3. **Hershey and Chase (1952):** bacteriophages labelled with ³²P (DNA) and ³⁵S (protein) — only the ³²P entered the bacteria and appeared in new phages.

## 2.2 Structure of DNA

### Nucleotides

A nucleotide = **nitrogenous base + pentose sugar + phosphate**. Without the phosphate it is a nucleoside.

| Part | In DNA | In RNA |
| --- | --- | --- |
| Sugar | 2′-deoxyribose | Ribose (has 2′-OH) |
| Purines (two rings) | Adenine (A), Guanine (G) | Adenine, Guanine |
| Pyrimidines (one ring) | Cytosine (C), Thymine (T) | Cytosine, Uracil (U) |

Nucleotides are joined by **3′→5′ phosphodiester bonds**, giving a strand with a free 5′-phosphate end and a free 3′-OH end. Sequences are written 5′ → 3′.

### The Watson–Crick double helix (B-DNA)

1. Two polynucleotide strands wind round a common axis in a **right-handed** helix.
2. The strands are **antiparallel** — one runs 5′→3′, the other 3′→5′.
3. The sugar–phosphate backbone is outside; bases stack inside.
4. **Complementary base pairing:** A pairs with T by **2 hydrogen bonds**; G pairs with C by **3 hydrogen bonds**. So G–C rich DNA is more stable (higher melting temperature).
5. Diameter about 2 nm; one turn about 3.4 nm with about 10 base pairs per turn; base pairs 0.34 nm apart.
6. The helix has a **major groove** and a **minor groove**, where proteins and many drugs bind.
7. **Chargaff's rules** follow: A = T, G = C, and purines = pyrimidines.

```text
   5'  A — T  3'
       G ≡ C          — two H-bonds (A=T), three H-bonds (G≡C)
       T — A
       C ≡ G
   3'  A — T  5'
   (antiparallel strands)
```

| Form | Helix | Base pairs per turn | Notes |
| --- | --- | --- | --- |
| B-DNA | Right-handed | About 10 | Normal form in cells |
| A-DNA | Right-handed, wider | About 11 | Dehydrated DNA, DNA–RNA hybrids |
| Z-DNA | Left-handed, zig-zag backbone | About 12 | G–C alternating sequences |

**Denaturation and renaturation.** Heat or high pH separates the strands (melting); absorbance at 260 nm rises (**hyperchromic effect**). The temperature at which half the DNA is melted is the **Tm**. On slow cooling the strands re-pair (annealing) — the basis of PCR and probes.

### Packing of DNA in eukaryotes

DNA (about 2 m per human cell) must fit into a nucleus a few µm wide.

```text
DNA double helix (2 nm)
   → wrapped about 1.7 turns (≈147 bp) round a histone octamer
     (2 each of H2A, H2B, H3, H4) = NUCLEOSOME  ("beads on a string", 10 nm fibre)
   → H1 histone binds linker DNA; fibre coils (≈30 nm fibre)
   → loops on a protein scaffold
   → condensed metaphase chromosome
```

**Euchromatin** is loosely packed and actively transcribed; **heterochromatin** is tightly packed and largely silent. Histone acetylation loosens chromatin and switches genes on; DNA methylation at CpG sites usually switches them off (epigenetic control).

## 2.3 DNA functioning: replication

**Replication is semiconservative** (Meselson and Stahl, 1958): each daughter molecule has one old (parental) strand and one new strand. They grew *E. coli* in heavy nitrogen (¹⁵N), moved it to ¹⁴N, and separated DNA by density: after one generation all DNA was hybrid; after two, half hybrid and half light.

### Enzymes and proteins of replication (E. coli)

| Protein | Function |
| --- | --- |
| DnaA | Binds the origin (oriC) and starts unwinding |
| Helicase (DnaB) | Unwinds the double helix using ATP |
| Single-strand binding proteins (SSB) | Keep separated strands apart |
| DNA gyrase (topoisomerase II) | Removes supercoils ahead of the fork — target of fluoroquinolones |
| Primase (DnaG) | Makes short RNA primers (DNA polymerase cannot start a new chain) |
| DNA polymerase III | Main replicating enzyme; adds nucleotides 5′→3′; 3′→5′ exonuclease proofreading |
| DNA polymerase I | Removes RNA primers (5′→3′ exonuclease) and fills the gaps |
| DNA ligase | Seals nicks by forming the last phosphodiester bond |
| Sliding clamp | Holds polymerase on DNA for long stretches (processivity) |

### Steps

1. **Initiation:** proteins bind the origin; helicase opens a **replication bubble** with two **replication forks** moving in opposite directions (bidirectional).
2. **Priming:** primase lays down RNA primers.
3. **Elongation:** DNA polymerase adds deoxynucleotides only to a 3′-OH, so the new strand always grows 5′→3′.
   - **Leading strand** — made continuously towards the fork.
   - **Lagging strand** — made discontinuously away from the fork as **Okazaki fragments** (about 1000–2000 nucleotides in bacteria, 100–200 in eukaryotes), each with its own primer.
4. **Primer removal and gap filling** by DNA polymerase I.
5. **Ligation** of fragments by DNA ligase.
6. **Termination** where forks meet (ter sites in *E. coli*).

```text
          3' ─────────────────────────────── 5'  parental
              leading strand  ─────────────→  (continuous)
   fork  <  helicase
              lagging strand  ←── ←── ←──     (Okazaki fragments)
          5' ─────────────────────────────── 3'  parental
```

### Replication in eukaryotes — differences

- **Many origins** on each chromosome (DNA is long; forks move slower).
- Polymerase **α** (with primase) starts chains; **δ** makes mainly the lagging strand; **ε** the leading strand. Mitochondrial DNA uses polymerase γ.
- Nucleosomes are taken apart and re-formed behind the fork.
- **Telomeres**: the ends of linear chromosomes cannot be fully copied (end-replication problem). **Telomerase**, a reverse transcriptase carrying its own RNA template, adds TTAGGG repeats. It is active in germ cells, stem cells and most cancer cells.
- Replication occurs only once per cycle, in the S phase.

**Fidelity:** base pairing, polymerase proofreading and mismatch repair together give an error rate of about one in 10^9–10^10 bases per replication.

## 2.4 DNA damage, mutation and repair

A **mutation** is a permanent change in DNA sequence.

| Type | Change | Effect |
| --- | --- | --- |
| Transition | Purine ↔ purine or pyrimidine ↔ pyrimidine | Point substitution |
| Transversion | Purine ↔ pyrimidine | Point substitution |
| Silent | New codon codes the same amino acid | No change in protein |
| Missense | New codon codes a different amino acid | Altered protein (sickle cell: Glu → Val in β-globin) |
| Nonsense | Codon becomes a stop codon | Short, usually non-functional protein |
| Frameshift | Insertion or deletion not a multiple of three | Reading frame changes downstream |

Causes: replication errors, spontaneous deamination and depurination, UV light (thymine dimers), ionising radiation (strand breaks), chemicals (alkylating agents, intercalators, base analogues).

**DNA repair systems**

| System | Damage fixed | Note |
| --- | --- | --- |
| Direct reversal | Thymine dimers (photolyase in bacteria), alkylated guanine (methyltransferase) | No cutting of the strand |
| Base excision repair | Single damaged bases (uracil, oxidised bases) | Glycosylase removes the base |
| Nucleotide excision repair | Bulky lesions, thymine dimers | Defect causes xeroderma pigmentosum |
| Mismatch repair | Wrong base pairs after replication | Defect causes hereditary colon cancer (Lynch syndrome) |
| Double-strand break repair | Breaks from radiation | Homologous recombination (BRCA1/2) and non-homologous end joining |

Many anticancer drugs work by damaging DNA (alkylating agents, cisplatin, anthracyclines) faster than tumour cells can repair it.

## 2.5 DNA and RNA compared

| Feature | DNA | RNA |
| --- | --- | --- |
| Sugar | Deoxyribose | Ribose |
| Bases | A, G, C, T | A, G, C, U |
| Strands | Usually double-stranded | Usually single-stranded, folds on itself |
| Stability | Stable; no 2′-OH | Less stable; 2′-OH makes it easy to hydrolyse in alkali |
| Location | Nucleus (and mitochondria) | Made in nucleus; works mostly in cytoplasm |
| Function | Long-term store of genetic information | Carries information, decodes it, catalyses and regulates |
| Amount per cell | Constant | Varies with cell activity |
| Copied by | DNA polymerase | RNA polymerase |

## 2.6 Types of RNA

| RNA | Share of cell RNA | Structure | Function |
| --- | --- | --- | --- |
| Ribosomal RNA (rRNA) | About 80% | Large folded molecules with ribosomal proteins | Structure of ribosomes; 23S (bacteria) / 28S (eukaryotes) rRNA forms peptide bonds |
| Transfer RNA (tRNA) | About 15% | Small (about 75–90 nucleotides), cloverleaf in 2D, L-shape in 3D | Carries amino acids; anticodon reads codon |
| Messenger RNA (mRNA) | About 5% | Linear; in eukaryotes has 5′ cap and poly-A tail | Carries the gene's code to ribosomes |
| Small nuclear RNA (snRNA) | Small | Part of spliceosome | Splicing of pre-mRNA |
| Small nucleolar RNA (snoRNA) | Small | — | Chemical modification of rRNA |
| MicroRNA (miRNA) | Small, about 22 nucleotides | Double-stranded precursor processed by Dicer | Silences genes by blocking or destroying target mRNA |
| Small interfering RNA (siRNA) | Small, about 21–23 nucleotides | Double-stranded | RNA interference; basis of siRNA drugs |
| Long non-coding RNA (lncRNA) | Variable | Over 200 nucleotides | Regulates chromatin and transcription |
| Ribozymes | — | Catalytic RNA | Self-splicing introns, peptidyl transferase |

**Ribosome composition**

| Ribosome | Large subunit | Small subunit |
| --- | --- | --- |
| Prokaryotic 70S | 50S: 23S + 5S rRNA + proteins | 30S: 16S rRNA + proteins |
| Eukaryotic 80S | 60S: 28S + 5.8S + 5S rRNA + proteins | 40S: 18S rRNA + proteins |

(S = Svedberg unit of sedimentation; values do not add up because sedimentation depends on shape as well as mass.)

**tRNA cloverleaf**

```text
                 3' end  A
                         C
                         C   ← CCA end: amino acid attaches here
                5' ──┐   |
                     acceptor stem
          D arm  ─┤          ├─  TψC arm
                     |
                  variable loop
                     |
                 anticodon loop
                   ( 3 bases that pair with the mRNA codon )
```

## 2.7 Transcription

Transcription is the synthesis of RNA on a DNA template by **RNA polymerase**. Only one strand — the **template (antisense) strand** — is read, in the 3′→5′ direction; RNA grows 5′→3′ and has the same sequence as the **coding (sense) strand**, with U for T. No primer is needed.

### Transcription in prokaryotes

**RNA polymerase:** core enzyme (α2ββ′ω) + **sigma (σ) factor** = holoenzyme. Sigma recognises the promoter. One polymerase makes all classes of RNA.

**Promoter:** two conserved boxes upstream of the start site (+1): the **−35 region (TTGACA)** and the **−10 region or Pribnow box (TATAAT)**.

1. **Initiation:** holoenzyme binds the promoter, unwinds about 13–17 bp to form an open complex and starts the chain.
2. **Elongation:** sigma leaves; the core enzyme moves along, adding ribonucleotides; a transcription bubble travels with it.
3. **Termination:**
   - **Rho-independent (intrinsic):** a G–C rich inverted repeat forms a hairpin in the RNA, followed by a run of U's — the polymerase falls off.
   - **Rho-dependent:** the rho protein (an RNA helicase) chases the polymerase and releases the transcript.

Bacterial mRNA is often **polycistronic** (codes several proteins) and is translated while still being made.

### Transcription in eukaryotes

| RNA polymerase | Products | Note |
| --- | --- | --- |
| RNA polymerase I | 28S, 18S, 5.8S rRNA (in nucleolus) | |
| RNA polymerase II | Pre-mRNA, most snRNAs, miRNAs | Strongly inhibited by α-amanitin (mushroom toxin) |
| RNA polymerase III | tRNA, 5S rRNA, some small RNAs | |

- Promoters contain the **TATA box** (about 25–30 bp upstream), recognised by TATA-binding protein in **TFIID**. **General transcription factors** (TFIIA, B, D, E, F, H) assemble the pre-initiation complex; TFIIH phosphorylates the polymerase tail to release it.
- **Enhancers** and **silencers**, which can be far from the gene, bind activators and repressors that change the rate.

### Processing of eukaryotic pre-mRNA

1. **5′ capping:** a 7-methylguanosine cap is added by a 5′–5′ triphosphate bridge. It protects the mRNA and helps the ribosome bind.
2. **Splicing:** non-coding **introns** are removed and coding **exons** joined by the **spliceosome** (snRNPs). Introns usually begin with GU and end with AG. **Alternative splicing** lets one gene make several proteins.
3. **3′ polyadenylation:** the RNA is cut about 10–30 nucleotides after the signal AAUAAA, and a **poly-A tail** (up to about 200 A's) is added. It aids stability and export.

The mature mRNA is exported through nuclear pores.

**Drugs acting on transcription:** rifampicin binds the β subunit of bacterial RNA polymerase (not the human enzyme); actinomycin D intercalates into DNA and blocks RNA chain growth.

## 2.8 The genetic code

| Property | Meaning |
| --- | --- |
| Triplet | Three bases (a codon) code for one amino acid; 4³ = 64 codons |
| Sense and stop codons | 61 code for amino acids; UAA, UAG, UGA are stop codons |
| Start codon | AUG (methionine; N-formylmethionine in bacteria) |
| Degenerate | Most amino acids have more than one codon (leucine, serine, arginine have six; Met and Trp only one) |
| Unambiguous | Each codon means only one amino acid |
| Non-overlapping and comma-less | Read in successive triplets without gaps |
| Nearly universal | Same in almost all organisms; small exceptions in mitochondria (UGA = tryptophan) |
| Wobble | The third codon base can pair loosely with the first anticodon base (Crick's wobble hypothesis), so one tRNA can read several codons |

The code was worked out by Nirenberg and Matthaei, who found that poly-U RNA made polyphenylalanine (UUU = Phe), and by Khorana using synthetic repeating RNAs.

## 2.9 Translation (protein synthesis)

### Step 0: charging of tRNA

Each **aminoacyl-tRNA synthetase** attaches the correct amino acid to its tRNA, using ATP:

amino acid + tRNA + ATP → aminoacyl-tRNA + AMP + PPi

These enzymes also proofread — the accuracy of translation depends on them.

### Ribosome sites

- **A site** (aminoacyl) — receives the incoming charged tRNA.
- **P site** (peptidyl) — holds the tRNA carrying the growing chain.
- **E site** (exit) — releases the empty tRNA.

### Steps in prokaryotes

1. **Initiation:** the 30S subunit binds mRNA where the **Shine–Dalgarno sequence** (purine-rich, about AGGAGG) pairs with 16S rRNA. Initiator **fMet-tRNA** pairs with AUG in the P site with help of **IF1, IF2 (GTP) and IF3**. The 50S subunit joins to form the 70S initiation complex.
2. **Elongation** (repeats for each amino acid):
   - **EF-Tu–GTP** brings the right aminoacyl-tRNA to the A site.
   - **Peptidyl transferase** (activity of 23S rRNA — a ribozyme) moves the chain from the P-site tRNA onto the amino acid in the A site, forming a peptide bond.
   - **EF-G–GTP** moves (translocates) the ribosome one codon along the mRNA; the empty tRNA goes to the E site and leaves.
3. **Termination:** a stop codon enters the A site; **release factors** (RF1 reads UAA/UAG, RF2 reads UAA/UGA, RF3 helps) cause hydrolysis and release of the polypeptide. Subunits separate.

The protein is made from the **N-terminus to the C-terminus** while mRNA is read **5′→3′**. Several ribosomes can read one mRNA at once — a **polysome**.

**Energy:** about four high-energy phosphate bonds per peptide bond (two for charging, one each for EF-Tu and EF-G).

### Differences in eukaryotes

- 80S ribosomes; initiator tRNA carries plain methionine.
- No Shine–Dalgarno sequence: the 40S subunit binds the **5′ cap** (eIF4 complex) and **scans** to the first AUG in a good context (**Kozak sequence**).
- Many initiation factors (eIFs); elongation factors eEF1 and eEF2; a single release factor eRF1 (with eRF3).
- Translation happens in the cytoplasm, separate from transcription in the nucleus.

### Antibiotics and toxins that block translation

| Agent | Target | Action |
| --- | --- | --- |
| Aminoglycosides (streptomycin, gentamicin) | 30S | Misreading of the code; block initiation |
| Tetracyclines | 30S | Block aminoacyl-tRNA binding to the A site |
| Chloramphenicol | 50S | Inhibits peptidyl transferase |
| Macrolides (erythromycin) | 50S | Block the exit tunnel and translocation |
| Linezolid | 50S | Prevents formation of the initiation complex |
| Puromycin | Both types of ribosome | Mimics aminoacyl-tRNA; causes premature release |
| Cycloheximide | Eukaryotic 60S | Blocks translocation (research tool) |
| Diphtheria toxin | Eukaryotic eEF2 | ADP-ribosylates eEF2 and stops elongation |

## Remember

- Central dogma: DNA → RNA → protein; Avery (1944) and Hershey–Chase (1952) proved DNA is the genetic material.
- B-DNA: right-handed, antiparallel, about 10 bp per turn, 3.4 nm pitch, 2 nm wide; A=T (2 H-bonds), G≡C (3 H-bonds).
- Replication: semiconservative, bidirectional, 5′→3′; leading continuous, lagging as Okazaki fragments; primase → pol III → pol I → ligase; gyrase relieves supercoils.
- Telomerase = reverse transcriptase adding TTAGGG; active in cancer cells.
- rRNA about 80%, tRNA 15%, mRNA 5% of cell RNA. 70S = 50S + 30S; 80S = 60S + 40S.
- Prokaryotic promoter: −10 TATAAT and −35 TTGACA; sigma factor recognises it. Eukaryotes: three RNA polymerases; pol II makes mRNA; TATA box.
- mRNA processing: 5′ cap, splicing (GU…AG), poly-A tail.
- Code: 64 codons, AUG start, UAA/UAG/UGA stop, degenerate, nearly universal, wobble.
- Translation: A, P, E sites; EF-Tu brings tRNA, peptidyl transferase (23S rRNA) forms the bond, EF-G translocates; release factors end it.
