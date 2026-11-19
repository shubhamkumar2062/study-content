# Unit 4: Genetics, genomics and the cell cycle

This unit covers the science of genetics, transgenics and genomic analysis, cell cycle analysis, mitosis and meiosis, and the activities and checkpoints that control the cycle. Programmed cell death (apoptosis), which is closely tied to checkpoint control, is also covered here.

## 4.1 The science of genetics

**Genetics** is the study of heredity — how traits pass from parents to offspring — and of variation between individuals.

### Basic terms

| Term | Meaning |
| --- | --- |
| Gene | Unit of heredity; a DNA segment coding a protein or functional RNA |
| Locus | Position of a gene on a chromosome |
| Allele | Alternative form of a gene (e.g. tall T and dwarf t) |
| Genotype | Allele make-up (TT, Tt, tt) |
| Phenotype | Observable trait (tall or dwarf) |
| Homozygous | Two identical alleles (TT or tt) |
| Heterozygous | Two different alleles (Tt) |
| Dominant / recessive | Dominant allele shows in the heterozygote; recessive shows only when homozygous |
| Diploid (2n) / haploid (n) | Two sets / one set of chromosomes; humans 2n = 46, gametes n = 23 |
| Karyotype | Number and appearance of the chromosomes of a cell |

### Mendel's laws

Gregor Mendel (1866) crossed garden pea plants.

1. **Law of dominance:** in a cross of two pure forms, only the dominant trait appears in the F1.
2. **Law of segregation:** the two alleles of a gene separate during gamete formation, so each gamete carries one. Monohybrid cross Tt × Tt gives a phenotype ratio **3 : 1** and genotype ratio **1 : 2 : 1**.
3. **Law of independent assortment:** alleles of different genes (on different chromosomes) sort independently. Dihybrid cross gives **9 : 3 : 3 : 1**.

```text
   Monohybrid cross  Tt × Tt
            T        t
     T     TT       Tt
     t     Tt       tt        → 3 tall : 1 dwarf
```

**Chromosome theory of inheritance** (Sutton and Boveri): genes lie on chromosomes, and chromosome behaviour in meiosis explains Mendel's laws. **Linkage** (Morgan, in fruit flies): genes close together on one chromosome tend to be inherited together and break the law of independent assortment; **crossing over** in meiosis separates them, and its frequency is used to map genes.

**Deviations from Mendelian ratios:** incomplete dominance (pink snapdragons, 1:2:1), co-dominance (AB blood group), multiple alleles (ABO), polygenic traits (height, skin colour), epistasis.

### Patterns of human inheritance

| Pattern | Features | Examples |
| --- | --- | --- |
| Autosomal dominant | Affected in every generation; 50% risk to child of affected parent | Huntington's disease, familial hypercholesterolaemia |
| Autosomal recessive | Parents are usually unaffected carriers; 25% risk to each child | Sickle cell anaemia, thalassaemia, cystic fibrosis, phenylketonuria |
| X-linked recessive | Mostly males affected; carrier mothers | Haemophilia A and B, G6PD deficiency, Duchenne muscular dystrophy, colour blindness |
| Mitochondrial | Passed only through the mother | Some myopathies and optic neuropathies |

**Chromosomal disorders:** Down syndrome (trisomy 21), Turner syndrome (45,X), Klinefelter syndrome (47,XXY). They arise mostly from **non-disjunction** — chromosomes failing to separate in meiosis.

### Genetics and drug response (pharmacogenetics)

| Gene variant | Effect on drug response |
| --- | --- |
| Slow acetylators (NAT2) | Isoniazid builds up — more peripheral neuropathy |
| G6PD deficiency | Haemolysis with primaquine, dapsone, some sulphonamides |
| CYP2D6 poor metabolisers | Codeine gives little pain relief (poor conversion to morphine) |
| TPMT deficiency | Severe bone-marrow toxicity with azathioprine and mercaptopurine |
| HLA-B*5701 | Hypersensitivity to abacavir |

## 4.2 Transgenics and genomic analysis

### Recombinant DNA technology — the tools

| Tool | Role | Example |
| --- | --- | --- |
| Restriction endonucleases | "Molecular scissors"; cut DNA at specific palindromic sites, giving sticky or blunt ends | EcoRI cuts G^AATTC; SmaI gives blunt ends |
| DNA ligase | "Molecular glue"; joins fragments | T4 DNA ligase |
| Vectors | Carry foreign DNA into a host and copy it | Plasmids (pBR322, pUC), bacteriophage λ, cosmids, BACs, YACs, viral vectors for animal cells |
| Hosts | Cells that copy and express the DNA | *E. coli*, yeast, CHO cells |
| Reverse transcriptase | Makes complementary DNA (cDNA) from mRNA — no introns, so it can be expressed in bacteria | Used to clone the human insulin gene |
| Thermostable DNA polymerase | For PCR | Taq polymerase |

A good plasmid vector has an **origin of replication**, a **selectable marker** (antibiotic-resistance gene) and a **multiple cloning site**.

### Steps of gene cloning

```text
 1. Isolate the gene (or make cDNA)        → 2. Cut gene and vector with the same restriction enzyme
 3. Join with DNA ligase (recombinant DNA) → 4. Put into host cells (transformation, e.g. CaCl2 / heat shock, electroporation)
 5. Select cells that took up the vector (antibiotic resistance; blue–white screening:
    an insert disrupts lacZα → white colonies)
 6. Grow the clone → 7. Express and purify the protein
```

### Methods of genomic analysis

- **Polymerase chain reaction (PCR):** copies a chosen DNA stretch millions of times in cycles of **denaturation (about 94–95 °C)**, **primer annealing (about 50–65 °C)** and **extension (72 °C)** by Taq polymerase. Each cycle roughly doubles the target. **RT-PCR** starts from RNA; **real-time (quantitative) PCR** measures the amount as it forms.
- **Gel electrophoresis:** DNA (negatively charged) moves through agarose towards the positive electrode; small fragments move faster. Stained with ethidium bromide or safer dyes.
- **Blotting:** Southern blot detects DNA, Northern blot RNA, Western blot protein (with antibodies).
- **DNA sequencing:** Sanger's chain-termination method uses dideoxynucleotides (no 3′-OH) that stop chain growth at each base; next-generation sequencing reads millions of fragments in parallel.
- **Genomics:** study of whole genomes — sequencing, gene mapping, comparing genomes. **Transcriptomics** (all RNAs, by microarrays or RNA-seq) and **proteomics** (all proteins, by 2D gel electrophoresis and mass spectrometry) follow.
- **DNA fingerprinting:** variable repeat regions differ between people; used in forensics and paternity testing.
- **Gene editing:** CRISPR–Cas9 uses a guide RNA to bring the Cas9 nuclease to an exact site, where it cuts both strands; repair makes a knockout or inserts a new sequence.

### Transgenics

A **transgenic organism** carries a foreign gene (transgene) in all its cells, passed to its offspring.

**Methods of making transgenic animals:**

1. **Microinjection** of DNA into the male pronucleus of a fertilised egg (first transgenic mice).
2. **Embryonic stem cell method** — modify ES cells, place them in an early embryo; used to make **knockout mice** (a gene switched off).
3. **Retroviral vectors.**
4. Nuclear transfer (cloning) from a modified cell.

**Methods for plants:** *Agrobacterium tumefaciens* Ti plasmid, gene gun (biolistics).

**Applications**

| Field | Example |
| --- | --- |
| Disease models | Knockout and transgenic mice for cancer, diabetes and Alzheimer's research; testing new drugs |
| Pharming (drugs from animals) | Human antithrombin produced in the milk of transgenic goats |
| Recombinant medicines | Insulin and growth hormone from *E. coli*; hepatitis B vaccine from yeast; erythropoietin and monoclonal antibodies from mammalian cells |
| Agriculture | Bt cotton (insect resistance, grown widely in India), Golden Rice (provitamin A) |
| Gene therapy | Correct a faulty gene with a viral vector or edited cells |
| Toxicology | Mutation-test transgenic animals |

**Concerns:** biosafety, ecological effects, animal welfare and ethics. In India, genetically engineered organisms are regulated under the Environment (Protection) Act rules, with approval of field release by the Genetic Engineering Appraisal Committee.

## 4.3 The cell cycle and its analysis

The **cell cycle** is the ordered series of events by which a cell grows, copies its DNA and divides into two.

| Phase | Events | Typical share of a 24-hour human cycle |
| --- | --- | --- |
| G1 (gap 1) | Cell grows, makes RNA and proteins; checks size and signals | About 11 h (most variable) |
| S (synthesis) | DNA replicated; centrosome duplicated | About 8 h |
| G2 (gap 2) | Makes mitosis proteins; checks DNA | About 4 h |
| M (mitosis + cytokinesis) | Chromosomes separated; cell divides | About 1 h |
| G0 | Resting, non-dividing state | Neurons, mature muscle cells stay here; liver cells can re-enter |

G1, S and G2 together are **interphase**.

### Methods of cell cycle analysis

1. **Flow cytometry with a DNA dye** (propidium iodide): G1 cells have 2n DNA, G2/M cells 4n, S-phase cells in between. A histogram shows the fraction in each phase; a "sub-G1" peak indicates apoptotic cells with fragmented DNA.

```text
  cell count
     |  G1
     |  ||
     |  ||            G2/M
     |  ||   S         ||
     |  ||_______......||____
     +-----------------------> DNA content
        2n               4n
```

2. **Labelling S-phase cells** with ³H-thymidine or **BrdU** (a thymidine analogue detected by antibody).
3. **Mitotic index** — the percentage of cells in mitosis under the microscope.
4. **Synchronisation** — blocking cells at one stage (thymidine block at G1/S; nocodazole or colchicine in mitosis) and then releasing them.
5. **Detection of cyclins and phosphorylated proteins** by Western blot.
6. Time-lapse microscopy of live cells.

## 4.4 Mitosis and meiosis

### Mitosis (equational division)

1. **Prophase:** chromatin condenses into visible chromosomes, each with two **sister chromatids** joined at the centromere; nucleolus disappears; spindle starts forming.
2. **Prometaphase:** nuclear envelope breaks down; spindle microtubules attach to **kinetochores**.
3. **Metaphase:** chromosomes line up at the **metaphase (equatorial) plate**.
4. **Anaphase:** cohesin is cut; sister chromatids separate and move to opposite poles.
5. **Telophase:** nuclear envelopes re-form; chromosomes uncoil; nucleoli return.
6. **Cytokinesis:** a contractile actin–myosin ring pinches animal cells into two (cleavage furrow); plant cells form a cell plate.

Result: two genetically identical diploid cells.

### Meiosis (reduction division)

**Meiosis I** separates homologous chromosomes:

- **Prophase I** (long) — leptotene (threads appear), zygotene (homologues pair, **synapsis**, synaptonemal complex), pachytene (**crossing over** between non-sister chromatids), diplotene (chiasmata visible), diakinesis (further condensation).
- **Metaphase I** — homologous pairs (bivalents) line up; random orientation gives independent assortment.
- **Anaphase I** — homologues go to opposite poles (sister chromatids stay together).
- **Telophase I** — two haploid cells.

**Meiosis II** separates sister chromatids, like mitosis, with no DNA replication before it. Result: four haploid, genetically different cells.

| Feature | Mitosis | Meiosis |
| --- | --- | --- |
| Occurs in | Somatic cells | Germ cells (testis, ovary) |
| Divisions | One | Two |
| Daughter cells | Two | Four |
| Chromosome number | Kept (2n → 2n) | Halved (2n → n) |
| Pairing of homologues | No | Yes (synapsis) |
| Crossing over | Normally none | Yes, in prophase I |
| Genetic make-up of products | Identical to parent | Different from parent and each other |
| Purpose | Growth, repair, replacement | Gamete formation, variation |

## 4.5 Cellular activities and checkpoints

### The control system: cyclins and CDKs

**Cyclin-dependent kinases (CDKs)** are protein kinases that drive the cycle. They are active only when bound to a **cyclin**, whose level rises and falls in each cycle (made, then destroyed by the ubiquitin–proteasome system).

| CDK–cyclin pair | Stage driven |
| --- | --- |
| CDK4/6 – cyclin D | Progress through G1 (responds to growth factors) |
| CDK2 – cyclin E | G1 → S transition |
| CDK2 – cyclin A | S phase |
| CDK1 – cyclin B (maturation/mitosis-promoting factor, MPF) | G2 → M; entry into mitosis |

**Brakes:** CDK inhibitor proteins — p21 and p27 (Cip/Kip family) and p16 (INK4 family, blocks CDK4/6).

**The Rb–E2F switch:** in G1 the retinoblastoma protein (Rb) holds the transcription factor E2F inactive. CDK4/6–cyclin D and CDK2–cyclin E phosphorylate Rb; E2F is freed and turns on S-phase genes. Past this **restriction point** the cell is committed to divide even if growth signals are removed.

### Checkpoints

| Checkpoint | Checks | Main molecules | If a problem is found |
| --- | --- | --- | --- |
| G1/S (restriction point) | Cell size, nutrients, growth signals, DNA damage | Rb, E2F, p53, p21 | Arrest in G1 for repair, or G0, or apoptosis |
| Intra-S | Damage during replication; stalled forks | ATR, Chk1 | Slows replication |
| G2/M | Is DNA fully and correctly replicated? | ATM/ATR, Chk1/Chk2, CDK1–cyclin B | Delay mitosis until repaired |
| Spindle assembly (metaphase–anaphase) | Are all kinetochores attached to the spindle? | Mad2, anaphase-promoting complex (APC/C), securin, separase, cohesin | Anaphase held back; prevents wrong chromosome numbers |

**p53, "guardian of the genome":** DNA damage activates the kinases ATM and ATR, which stabilise p53. p53 is a transcription factor: it switches on **p21** (stopping the cycle for repair), DNA-repair genes, and, if damage is too great, pro-apoptotic genes (Bax, Puma, Noxa). p53 is mutated in about half of human cancers.

**Cancer and the cell cycle:** cancer arises when **proto-oncogenes** (normal growth genes, such as Ras and Myc) become overactive **oncogenes**, and **tumour-suppressor genes** (p53, Rb) lose function, so checkpoints fail.

**Drugs acting on the cycle**

| Drug group | Phase |
| --- | --- |
| Antimetabolites (methotrexate, 5-fluorouracil, cytarabine) | S phase |
| Vinca alkaloids (vincristine) and taxanes (paclitaxel) | M phase — disrupt microtubules of the spindle |
| Bleomycin | G2 phase |
| Etoposide (topoisomerase II inhibitor) | S and G2 |
| CDK4/6 inhibitors (palbociclib) | Hold cells in G1 (breast cancer) |
| Alkylating agents, cisplatin | Act in all phases (cell-cycle non-specific) |

## 4.6 Apoptosis (programmed cell death)

**Apoptosis** is an orderly, energy-dependent "cell suicide" in which the cell dismantles itself without spilling its contents, so there is no inflammation.

| Feature | Apoptosis | Necrosis |
| --- | --- | --- |
| Cause | Physiological signals or limited damage | Severe injury (ischaemia, toxins) |
| Cells involved | Single cells | Groups of cells |
| Cell size | Shrinks | Swells |
| Membrane | Intact; forms blebs and apoptotic bodies | Breaks |
| Nucleus | Chromatin condenses; DNA cut into fragments of about 180–200 bp (ladder on gel) | Random breakdown (smear) |
| Energy | Needs ATP | No |
| Inflammation | None — bodies are eaten by phagocytes | Present |

### Pathways

**Intrinsic (mitochondrial) pathway** — triggered by DNA damage, loss of growth factors, oxidative stress:

1. BH3-only proteins (Bid, Bad, Puma, Noxa) are activated and inhibit anti-apoptotic **Bcl-2** and **Bcl-xL**.
2. **Bax and Bak** open pores in the outer mitochondrial membrane.
3. **Cytochrome c** is released into the cytosol and binds **Apaf-1** → the **apoptosome** → activates **caspase-9**.
4. Caspase-9 activates the executioner **caspases-3 and -7**.

**Extrinsic (death-receptor) pathway:**

1. **Fas ligand**, **TNF-α** or **TRAIL** binds its death receptor on the cell surface.
2. The adaptor **FADD** recruits procaspase-8 (death-inducing signalling complex) → active **caspase-8**.
3. Caspase-8 activates caspase-3 directly, and also cuts **Bid** to tBid, which links to the intrinsic pathway.

```text
 Extrinsic: FasL/TNF → death receptor → FADD → caspase-8 ─┐
                                              (Bid → tBid)  │
 Intrinsic: DNA damage → p53 → Bax/Bak → cytochrome c ──→ Apaf-1 → caspase-9
                                                            │
                                         caspase-3 / 7 (executioners)
                                                            ↓
            DNA fragmentation, protein breakdown, blebbing, apoptotic bodies,
            phosphatidylserine on outer surface → engulfed by macrophages
```

**Caspases** are cysteine proteases that cut after aspartate residues. They are held in check by inhibitor of apoptosis proteins (IAPs).

**Detection of apoptosis:** DNA laddering on agarose gel, TUNEL staining of DNA breaks, **annexin V** binding to exposed phosphatidylserine (flow cytometry), caspase activity assays, sub-G1 peak.

**Significance:** shaping organs in development (removal of web between fingers), deleting self-reactive immune cells, removing damaged or infected cells. Too little apoptosis → cancer, autoimmunity; too much → neurodegenerative diseases, ischaemic damage. Many anticancer drugs kill tumour cells by triggering apoptosis; venetoclax directly blocks Bcl-2 in some leukaemias.

## Remember

- Mendel: dominance, segregation (3:1), independent assortment (9:3:3:1); linkage breaks independent assortment.
- Autosomal recessive: sickle cell, cystic fibrosis, PKU; X-linked recessive: haemophilia, G6PD deficiency, DMD.
- Recombinant DNA: restriction enzyme cuts, ligase joins, plasmid vector, transformation, selection.
- PCR: 94–95 °C denature, 50–65 °C anneal, 72 °C extend with Taq. Southern = DNA, Northern = RNA, Western = protein.
- Transgenic animals by pronuclear microinjection or ES cells; knockout mice; Bt cotton.
- Cell cycle G1 → S → G2 → M; G0 = resting. Flow cytometry: 2n (G1), 4n (G2/M).
- Mitosis: 2 identical diploid cells. Meiosis: 4 different haploid cells; crossing over in pachytene.
- CDK4/6–cyclin D (G1), CDK2–cyclin E (G1/S), CDK1–cyclin B = MPF (G2/M). Rb–E2F switch; p53 → p21.
- Checkpoints: G1/S, intra-S, G2/M, spindle assembly (Mad2, APC/C).
- Apoptosis: intrinsic (cytochrome c, Apaf-1, caspase-9) and extrinsic (Fas/TNF, FADD, caspase-8) → caspase-3; no inflammation.
