# Unit 4: Nucleic acid metabolism and genetic information transfer

This unit has two parts. The first covers how purine and pyrimidine nucleotides are made and how purines are broken down to uric acid, with hyperuricaemia and gout. The second covers the "central dogma": how the mammalian genome is organised, the structure of DNA and RNA, and how information flows from DNA to DNA (replication), DNA to RNA (transcription) and RNA to protein (translation), with the drugs that block each step.

```text
Central dogma:   DNA ──replication──► DNA
                  │
             transcription
                  ▼
                 RNA ──translation──► Protein
(Reverse transcription RNA → DNA occurs in retroviruses such as HIV.)
```

## 4.1 Biosynthesis of purine nucleotides

Purines can be made in two ways: **de novo** (from small molecules) and by **salvage** (reuse of free bases).

### De novo synthesis

**Site**: cytosol, mainly liver. The purine ring is **built step by step on the ribose-phosphate** (unlike pyrimidines).

**Sources of the atoms of the purine ring**

| Atom | Source |
| --- | --- |
| N1 | Aspartate |
| C2, C8 | N10-formyl tetrahydrofolate (folic acid) |
| N3, N9 | Amide nitrogen of glutamine |
| C4, C5, N7 | Glycine |
| C6 | CO2 |

**Main steps**

```text
Ribose-5-phosphate (from HMP shunt)
  │ PRPP synthetase (ATP → AMP)
PRPP (5-phosphoribosyl-1-pyrophosphate)
  │ Glutamine PRPP amidotransferase  [committed, rate-limiting step;
  │      inhibited by AMP, GMP, IMP — feedback]
5-Phosphoribosylamine
  │ + glycine, formyl-THF, glutamine, CO2, aspartate, formyl-THF
  │   (about 9 more steps; several use ATP)
Inosine monophosphate (IMP) — the first purine nucleotide (base = hypoxanthine)
  ├─► AMP:  IMP + aspartate + GTP → adenylosuccinate → AMP + fumarate
  └─► GMP:  IMP + NAD+ → XMP (IMP dehydrogenase); XMP + glutamine + ATP → GMP
```

AMP formation needs GTP and GMP formation needs ATP, which keeps the two balanced.

### Salvage pathway

Free bases released by breakdown are reattached to PRPP — much cheaper than de novo synthesis, and the main source of purines in brain and red cells.

- Hypoxanthine + PRPP → IMP; guanine + PRPP → GMP (**hypoxanthine–guanine phosphoribosyltransferase, HGPRT**).
- Adenine + PRPP → AMP (**adenine phosphoribosyltransferase, APRT**).

**Lesch–Nyhan syndrome**: X-linked complete lack of HGPRT → PRPP builds up and de novo synthesis rises → severe hyperuricaemia, gout, mental retardation and **self-mutilation** (biting of lips and fingers).

### Drugs acting on purine synthesis

- **Methotrexate** — inhibits dihydrofolate reductase, so folate one-carbon units are not available.
- **6-Mercaptopurine** and **azathioprine** — purine analogues.
- **Mycophenolate** — inhibits IMP dehydrogenase, so GMP falls in lymphocytes (immunosuppression).

## 4.2 Biosynthesis of pyrimidine nucleotides

The pyrimidine ring is **made first and then attached to PRPP**.

**Sources of ring atoms**: N1, C4, C5, C6 from **aspartate**; C2 from **CO2 (bicarbonate)**; N3 from **glutamine**.

```text
Glutamine + CO2 + 2 ATP
  │ Carbamoyl phosphate synthetase II (cytosol; rate-limiting in humans;
  │     inhibited by UTP, activated by PRPP)
Carbamoyl phosphate
  │ + aspartate: Aspartate transcarbamoylase
Carbamoyl aspartate
  │ Dihydroorotase (ring closes)
Dihydroorotate
  │ Dihydroorotate dehydrogenase (inner mitochondrial membrane; inhibited by leflunomide)
Orotate
  │ + PRPP: Orotate phosphoribosyltransferase
Orotidine monophosphate (OMP)
  │ OMP decarboxylase
UMP ──► UDP ──► UTP ──► CTP (CTP synthetase, glutamine adds NH2)
```

The first three enzymes form one multifunctional protein (**CAD**), and the last two form **UMP synthase**.

**Thymidine nucleotides (for DNA only)**

```text
Ribonucleotide (NDP) ──ribonucleotide reductase──► deoxyribonucleotide (dNDP)
        (inhibited by hydroxyurea)
dUMP ──thymidylate synthase (N5,N10-methylene THF)──► dTMP
        (inhibited by 5-fluorouracil)
Dihydrofolate ──dihydrofolate reductase──► tetrahydrofolate (recycled)
        (inhibited by methotrexate; bacterial enzyme by trimethoprim)
```

**Orotic aciduria**: deficiency of UMP synthase → orotic acid in urine, megaloblastic anaemia not cured by B12 or folate, growth failure; treated with uridine.

| Feature | Purine synthesis | Pyrimidine synthesis |
| --- | --- | --- |
| Ring built on | Ribose-5-P (PRPP first) | Free ring first, then PRPP added |
| First nucleotide | IMP | UMP (via OMP) |
| Rate-limiting enzyme | PRPP amidotransferase | Carbamoyl phosphate synthetase II |
| Carbamoyl phosphate | Not used | Used (cytosolic CPS-II) |
| Site | Cytosol | Cytosol + one mitochondrial step |

## 4.3 Catabolism of purine nucleotides

In humans purines are broken down to **uric acid**, which is excreted in urine (most other mammals oxidise it further to allantoin by uricase, which humans lack).

```text
AMP ──AMP deaminase──► IMP                 GMP
 │ nucleotidase                              │ nucleotidase
Adenosine                                   Guanosine
 │ adenosine deaminase (ADA)                 │ purine nucleoside phosphorylase
Inosine                                     Guanine
 │ purine nucleoside phosphorylase           │ guanase (guanine deaminase)
Hypoxanthine ──xanthine oxidase──► Xanthine ◄┘
                                     │ xanthine oxidase
                                  Uric acid  (excreted in urine)
```

**Adenosine deaminase deficiency** damages lymphocytes and causes **severe combined immunodeficiency (SCID)**; it was one of the first diseases treated by gene therapy.

Pyrimidines are broken down to soluble products (β-alanine and β-aminoisobutyrate, CO2 and NH3), so they do not cause a disease like gout.

## 4.4 Hyperuricaemia and gout

Serum uric acid is normally about **3–7 mg/dl** in men and a little lower in women (ranges vary by laboratory). **Hyperuricaemia** is a level above about 7 mg/dl (men) or 6 mg/dl (women). At body pH uric acid is present mostly as **monosodium urate**, which is poorly soluble; above the saturation level it can form crystals.

### Causes of hyperuricaemia

| Over-production | Under-excretion (more common) |
| --- | --- |
| Primary: enzyme defects (HGPRT deficiency — Lesch–Nyhan; PRPP synthetase over-activity; von Gierke disease) | Kidney failure |
| Secondary: high cell turnover — leukaemia, lymphoma, psoriasis; **cancer chemotherapy** (tumour lysis); high-purine diet (meat, sea food), alcohol, fructose | Drugs: thiazide and loop diuretics, low-dose aspirin, pyrazinamide, ethambutol, ciclosporin |
| | Lactic acidosis and ketoacidosis (organic acids compete for excretion), lead poisoning |

### Gout

**Definition.** A disease caused by deposition of **monosodium urate crystals** in joints and tissues, usually with long-standing hyperuricaemia.

**Features**

1. **Acute gouty arthritis**: sudden, very painful, red, swollen joint, often the big toe (**podagra**), frequently starting at night; crystals are taken up by neutrophils, which set off inflammation.
2. **Tophi**: chalky urate deposits in ear cartilage, around joints and tendons (chronic gout).
3. **Kidney**: uric acid stones and urate nephropathy.
4. Linked to obesity, hypertension, diabetes and the metabolic syndrome.

**Diagnosis**: needle-shaped, negatively birefringent crystals in joint fluid under polarised light; serum uric acid (may be normal during an attack).

**Treatment (pharmacy-relevant)**

| Purpose | Drugs |
| --- | --- |
| Acute attack | NSAIDs (e.g. naproxen, indometacin), colchicine, corticosteroids (aspirin is avoided: it alters urate excretion) |
| Lower uric acid (long term) | **Xanthine oxidase inhibitors**: allopurinol (a hypoxanthine analogue; its product oxypurinol binds the enzyme tightly) and febuxostat |
| Increase excretion | **Uricosurics**: probenecid, sulfinpyrazone |
| Break down urate | Rasburicase (recombinant uricase; tumour lysis syndrome) |
| Lifestyle | Plenty of water, less meat, sea food, alcohol and sugary drinks; weight loss |

## 4.5 Organisation of the mammalian genome

**Genome**: the complete DNA of an organism.

- Human haploid genome: about **3 × 10^9 base pairs** on **23 chromosomes** (body cells are diploid: 22 pairs of autosomes + one pair of sex chromosomes).
- Only about **1–2%** codes for proteins (roughly 20,000 protein-coding genes). The rest includes introns, regulatory regions, RNA genes and much repetitive DNA.
- **Mitochondrial DNA**: small circular DNA (about 16.5 kb) with 37 genes; inherited only from the mother.

### Packaging: DNA → chromatin → chromosome

```text
DNA double helix (2 nm)
   │ wraps about 1.7 times (≈146 bp) round a histone octamer (2 each of H2A, H2B, H3, H4)
Nucleosome ("beads on a string", 10 nm fibre); linker DNA between beads, histone H1 binds it
   │ coils further
30 nm chromatin fibre (solenoid)
   │ loops attached to a protein scaffold
Looped domains → condensed chromatin
   │ maximum condensation at metaphase
Chromosome (two sister chromatids joined at the centromere; telomeres at the ends)
```

Histones are rich in the basic amino acids lysine and arginine, whose positive charges bind the negative phosphate backbone of DNA.

- **Euchromatin**: loosely packed, genes active (transcribed).
- **Heterochromatin**: tightly packed, genes mostly silent (e.g. centromeres, inactive X chromosome — Barr body).

### Features of mammalian genes and DNA

1. **Split genes**: coding sequences (**exons**) are interrupted by non-coding **introns**, removed after transcription.
2. **Repetitive DNA**: highly repetitive satellite DNA (centromeres), moderately repetitive interspersed elements (LINEs, SINEs such as Alu sequences), and unique (single-copy) sequences that contain most genes.
3. **Gene families** and **pseudogenes** (non-functional copies).
4. **Regulatory sequences**: promoters, enhancers and silencers.
5. **Telomeres**: repeated TTAGGG sequences at chromosome ends, kept by **telomerase** (active in germ cells and many cancers).

## 4.6 Structure and functions of DNA and RNA

### DNA (Watson–Crick double helix, 1953)

1. Two polynucleotide strands wound round a common axis in a **right-handed double helix**.
2. Strands are **antiparallel** (one runs 5′→3′, the other 3′→5′).
3. Sugar–phosphate backbone on the outside; bases stacked inside.
4. **Complementary base pairing**: A pairs with T by **two** hydrogen bonds; G pairs with C by **three** hydrogen bonds. So GC-rich DNA is more stable (higher melting temperature).
5. B-form dimensions: diameter about 2 nm, about 10 base pairs per turn, 3.4 nm per turn (0.34 nm between base pairs).
6. **Major and minor grooves** where proteins bind.
7. Other forms: A-DNA (right-handed, wider) and Z-DNA (left-handed, zig-zag backbone).

**Functions of DNA**: stores genetic information; template for its own replication and for transcription; site of mutation and genetic variation.

**Denaturation**: heat separates the strands (melting); absorbance at 260 nm rises (**hyperchromic effect**). On cooling the strands pair again (renaturation, annealing — the basis of PCR and hybridisation).

### RNA

Single-stranded (with folded double-stranded regions), contains **ribose** and **uracil** instead of thymine; does not follow Chargaff's rules.

| Type | Share of cell RNA | Structure | Function |
| --- | --- | --- | --- |
| **mRNA** (messenger) | About 5% | Linear; 5′ **cap** (7-methylguanosine) and 3′ **poly-A tail** in eukaryotes | Carries the code from DNA to the ribosome |
| **tRNA** (transfer) | About 15% | About 75–90 nucleotides; **cloverleaf** with acceptor arm (CCA at 3′ end, carries the amino acid), anticodon arm, D arm and TψC arm | Brings the right amino acid to the ribosome, reads the codon |
| **rRNA** (ribosomal) | About 80% | With proteins forms ribosomes: eukaryotic 80S = 60S (28S, 5.8S, 5S rRNA) + 40S (18S rRNA); prokaryotic 70S = 50S + 30S | Structure of ribosome; 28S (23S in bacteria) rRNA catalyses peptide bond formation (a ribozyme) |
| Small RNAs | Small | snRNA, miRNA, siRNA | Splicing, gene silencing |

| DNA | RNA |
| --- | --- |
| Deoxyribose | Ribose |
| Thymine | Uracil |
| Double-stranded | Usually single-stranded |
| Mainly in nucleus (and mitochondria) | Nucleus and cytoplasm |
| Stable, long-lived | Less stable (mRNA short-lived) |
| Genetic store | Expression of genetic information |

## 4.7 DNA replication (semiconservative model)

**Semiconservative**: each new DNA molecule contains one old (parent) strand and one newly made strand. Proved by **Meselson and Stahl (1958)**: E. coli grown in heavy nitrogen (15N) and moved to normal 14N gave DNA of intermediate density after one generation, then intermediate + light after the second.

```text
Parent (heavy/heavy) → 1st generation: all hybrid (heavy/light)
                     → 2nd generation: half hybrid, half light/light
```

### Steps and enzymes

1. **Initiation** — replication begins at **origins** (one in bacteria; many in eukaryotes), forming **replication forks** that move in both directions (bidirectional).
2. **Unwinding**:
   - **Helicase** separates the strands (uses ATP).
   - **Single-strand binding proteins** keep them apart.
   - **Topoisomerases** relieve the supercoiling ahead of the fork. Bacterial DNA gyrase (topoisomerase II) is blocked by **quinolones** (ciprofloxacin); human topoisomerases by **etoposide** and **camptothecins** (anticancer).
3. **Primer** — **primase** lays down a short **RNA primer**; DNA polymerases cannot start a chain.
4. **Elongation**:
   - **DNA polymerase** adds deoxynucleotides only to the 3′-OH end, so synthesis is always **5′→3′**.
   - Prokaryotes use DNA pol III; eukaryotes use pol δ and ε, with pol α–primase.
   - **Leading strand**: made continuously towards the fork.
   - **Lagging strand**: made discontinuously as **Okazaki fragments**, away from the fork.
5. **Primer removal and gap filling** — DNA pol I in bacteria; RNase H and pol δ in eukaryotes.
6. **Joining** — **DNA ligase** seals the nicks between fragments.
7. **Proofreading** — 3′→5′ exonuclease activity of polymerases removes wrong bases; mismatch repair follows, making replication very accurate.
8. **Termination** — at telomeres, **telomerase** (a reverse transcriptase with its own RNA template) prevents shortening.

```text
5' ─────────────────────────────── 3'   template
        ◄── leading strand (continuous)
                         FORK ◄ helicase
        ── Okazaki ── Okazaki ──►        lagging strand (pieces, joined by ligase)
3' ─────────────────────────────── 5'   template
```

**Drugs**: nucleoside analogues block viral DNA synthesis (aciclovir, zidovudine — a reverse transcriptase inhibitor); cytarabine blocks DNA polymerase in cancer cells.

## 4.8 Transcription (RNA synthesis)

**Definition.** Synthesis of RNA on a DNA template by **DNA-dependent RNA polymerase**. Only one strand (the **template**, or antisense strand) is copied; the RNA has the same sequence as the other (**coding**, sense) strand, with U for T. RNA is made 5′→3′. **No primer is needed.**

### RNA polymerases

- **Prokaryotes**: one enzyme; core (α2ββ′ω) + **sigma (σ) factor**, which recognises the promoter.
- **Eukaryotes**: three nuclear enzymes —
  - **RNA pol I** (28S, 18S, 5.8S rRNA);
  - **RNA pol II** (mRNA, most snRNA and miRNA; very sensitive to α-amanitin);
  - **RNA pol III** (tRNA, 5S rRNA).

### Stages

1. **Initiation** — the polymerase binds the **promoter**:
   - prokaryotes: Pribnow box TATAAT at about −10 and a sequence at −35;
   - eukaryotes: **TATA (Hogness) box** at about −25, with general transcription factors (TFIID binds TATA).

   The DNA unwinds locally and the first nucleotides are joined.
2. **Elongation** — the polymerase moves along the template, adding ribonucleotides complementary to it; the DNA rewinds behind it.
3. **Termination** — in bacteria either **rho-independent** (a GC-rich hairpin followed by U's) or **rho-dependent** (rho protein).

### Post-transcriptional processing (eukaryotic mRNA)

1. **5′ capping** with 7-methylguanosine — protects the mRNA and helps ribosome binding.
2. **3′ poly-A tail** (about 200 adenines) — stability and export.
3. **Splicing** — introns removed and exons joined by the **spliceosome** (snRNPs). Alternative splicing lets one gene make several proteins.
4. rRNA and tRNA are also cut and chemically modified.

**Inhibitors of transcription**

| Drug | Action |
| --- | --- |
| **Rifampicin** | Binds the β subunit of bacterial RNA polymerase; blocks initiation (anti-tubercular) |
| **Actinomycin D** (dactinomycin) | Intercalates into DNA; blocks elongation (anticancer) |
| **α-Amanitin** (death-cap mushroom) | Inhibits eukaryotic RNA pol II |

## 4.9 Genetic code

The **genetic code** is the set of rules by which the sequence of bases in mRNA is translated into the amino acid sequence of a protein. Each **codon** is three bases.

**Features**

1. **Triplet** — 4³ = **64** codons: 61 code for amino acids, 3 are **stop codons** (**UAA, UAG, UGA**).
2. **Start codon** — **AUG** (methionine); it also codes for internal methionine.
3. **Degenerate (redundant)** — most amino acids have more than one codon (leucine, serine and arginine have six). Only methionine and tryptophan have one each.
4. **Unambiguous** — one codon codes for one amino acid only.
5. **Non-overlapping** and **commaless** — read continuously, three bases at a time, from a fixed start.
6. **Nearly universal** — same in almost all organisms; exceptions in mitochondria (e.g. UGA = tryptophan).
7. **Wobble** — the third base of the codon pairs less strictly with the first base of the anticodon, so one tRNA can read several codons.

**Mutations**: point mutations (silent, missense — sickle cell anaemia, glutamate → valine in β-globin; nonsense — premature stop) and frameshift mutations (insertion or deletion not a multiple of 3).

## 4.10 Translation (protein synthesis) and its inhibitors

**Site**: ribosomes in the cytoplasm (free or on rough ER). Proteins are made from the **N-terminal to the C-terminal** end, reading mRNA **5′→3′**.

### Steps

**1. Activation of amino acids**

Amino acid + tRNA + ATP → aminoacyl-tRNA + AMP + PPi (**aminoacyl-tRNA synthetase**, one specific enzyme per amino acid). This is the step that ensures the right amino acid is put on the right tRNA (2 high-energy bonds).

**2. Initiation**

- Small ribosomal subunit (40S; 30S in bacteria) binds the mRNA at the cap and scans for **AUG** (in bacteria the Shine–Dalgarno sequence positions it).
- Initiator **Met-tRNAi** (formyl-Met in bacteria) binds AUG in the **P site**, helped by initiation factors (eIFs) and GTP.
- The large subunit joins → **80S initiation complex** (70S in bacteria).

**3. Elongation (repeated for each amino acid)**

```text
(a) Binding:   aminoacyl-tRNA enters the A site (EF-1 / EF-Tu, GTP)
(b) Peptide bond: peptidyl transferase (rRNA of large subunit) moves the growing chain
                  from the P-site tRNA to the A-site amino acid
(c) Translocation: ribosome moves one codon along mRNA (EF-2 / EF-G, GTP);
                   empty tRNA goes to the E site and leaves; peptidyl-tRNA now in P site
```

**4. Termination**

When a stop codon reaches the A site, **release factors** bind, the peptide is released by hydrolysis, and the ribosome dissociates.

**Energy**: about **4 high-energy bonds per peptide bond** (2 from ATP in activation, 1 GTP in binding, 1 GTP in translocation).

**Post-translational modification**: folding (chaperones), removal of signal peptide, disulphide bonds, glycosylation, phosphorylation, hydroxylation of proline and lysine in collagen (vitamin C), carboxylation of clotting factors (vitamin K), proteolytic activation (proinsulin → insulin).

### Inhibitors of protein synthesis

| Inhibitor | Target | Action |
| --- | --- | --- |
| **Streptomycin, gentamicin** (aminoglycosides) | 30S | Misreading of code; block initiation |
| **Tetracyclines** | 30S | Block binding of aminoacyl-tRNA to the A site |
| **Chloramphenicol** | 50S | Inhibits peptidyl transferase |
| **Erythromycin** (macrolides), clindamycin | 50S | Block translocation |
| **Linezolid** | 50S | Prevents formation of the initiation complex |
| **Puromycin** | Bacterial and eukaryotic ribosomes | Looks like aminoacyl-tRNA; causes premature chain release |
| **Cycloheximide** | 60S (eukaryotes) | Inhibits peptidyl transferase |
| **Diphtheria toxin** | eEF-2 (eukaryotes) | ADP-ribosylates eEF-2, stopping translocation |
| **Ricin** | 60S (eukaryotes) | Damages 28S rRNA |

Antibiotics are selective because bacterial ribosomes (70S) differ from human cytoplasmic ribosomes (80S). Mitochondrial ribosomes resemble bacterial ones, which explains some toxicity (e.g. chloramphenicol bone-marrow suppression).

## Remember

- Purine ring: aspartate (N1), formyl-THF (C2, C8), glutamine (N3, N9), glycine (C4, C5, N7), CO2 (C6); built on PRPP; first product IMP; PRPP amidotransferase rate-limiting.
- Pyrimidine ring: aspartate + carbamoyl phosphate (CPS-II, glutamine) made first, then PRPP; first product UMP via orotate.
- Purine breakdown ends in uric acid by xanthine oxidase (allopurinol, febuxostat inhibit); ADA deficiency → SCID; HGPRT deficiency → Lesch–Nyhan.
- Gout = monosodium urate crystals; big toe; tophi; acute attack: NSAIDs/colchicine; long-term: allopurinol, probenecid.
- Genome: about 3 × 10^9 bp; DNA + histone octamer = nucleosome; exons and introns.
- DNA: antiparallel right-handed double helix, A=T (2 H bonds), G≡C (3 H bonds), 10 bp per turn, 3.4 nm pitch.
- Replication: semiconservative (Meselson–Stahl), helicase → primase → polymerase (5′→3′) → ligase; Okazaki fragments on lagging strand; quinolones inhibit gyrase.
- Transcription: RNA pol II makes mRNA; TATA box; cap, tail and splicing; rifampicin blocks bacterial RNA polymerase.
- Code: triplet, 64 codons, AUG start, UAA/UAG/UGA stop, degenerate, unambiguous, nearly universal, wobble.
- Translation inhibitors: aminoglycosides and tetracyclines (30S); chloramphenicol, macrolides, linezolid (50S); diphtheria toxin (eEF-2).
