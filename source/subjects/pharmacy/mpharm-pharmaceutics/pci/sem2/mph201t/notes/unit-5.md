# Unit 5: Nucleic acid based therapeutic delivery systems

Conventional drugs act on a protein that already exists. **Nucleic acid therapeutics** act one step earlier — on the gene or on the messenger RNA that makes the protein. From a pharmaceutics point of view the molecule itself is only half the problem; the real difficulty is that nucleic acids are large, highly negatively charged, hydrophilic and quickly broken down by nucleases, so they cannot cross a cell membrane on their own. This unit is therefore about **carriers, principles and applications**.

## 5.1 Gene therapy — introduction

**Gene therapy** is the treatment of disease by introducing genetic material into a patient's cells, so as to replace a faulty gene, add a missing function, silence a harmful gene or correct a sequence.

**Strategies**

| Strategy | What is done |
| --- | --- |
| Gene augmentation / replacement | A working copy of a gene is added where the patient's copy does not work (recessive, loss-of-function disorders) |
| Gene silencing / inhibition | Expression of a harmful or over-active gene is switched off (antisense, siRNA, ribozymes) |
| Gene correction / editing | The faulty sequence itself is repaired in place |
| Suicide-gene and prodrug therapy | A gene for an enzyme is delivered that converts a harmless prodrug into a cytotoxic agent inside tumour cells |
| Immunomodulation | Genes for cytokines or antigens are delivered to make the immune system act on the tumour or pathogen; also genetically engineered immune cells |

**Germline versus somatic.** **Somatic** gene therapy alters only the patient's own body cells, so the change is not passed to children; this is the only form that is permitted and practised. **Germline** modification would be heritable and is not permitted. In India, gene therapy research is governed by the national guidelines issued by the Indian Council of Medical Research and the Department of Biotechnology, with institutional ethics-committee and regulatory approval required; the national guidelines explicitly rule out germline modification.

### Ex-vivo and in-vivo gene therapy

```text
EX VIVO                                  IN VIVO
 ┌──────────────────────┐                 ┌──────────────────────┐
 │ Cells taken from the │                 │ Vector carrying the  │
 │ patient (bone marrow,│                 │ gene is given        │
 │ T cells, fibroblasts)│                 │ directly to the      │
 └──────────┬───────────┘                 │ patient — systemic,  │
            ↓                             │ local or organ-      │
 Cultured and the gene is                 │ directed injection   │
 transferred in the laboratory            └──────────┬───────────┘
            ↓                                        ↓
 Modified cells selected,                  Vector must find the
 expanded and tested                       target cells itself
            ↓                                        ↓
 Re-infused into the same patient           Gene is expressed in vivo
```

| Point | Ex vivo | In vivo |
| --- | --- | --- |
| Where transfer happens | In the laboratory | Inside the body |
| Control over the process | High — cells can be selected, tested and expanded; safety checks before return | Low |
| Suitable cell types | Only cells that can be removed and cultured (haematopoietic stem cells, lymphocytes, hepatocytes, fibroblasts, skin) | Any tissue in principle |
| Immune reaction to the vector | Mostly avoided | A major problem |
| Targeting | Not needed — the right cells are treated directly | The main pharmaceutical challenge |
| Cost and complexity | Very high; individualised, needs a cell-processing facility | Lower; closer to a conventional medicine |
| Example type | Modified haematopoietic stem cells for inherited disorders; engineered T cells for blood cancers | Vector injected into eye, muscle, liver or tumour |

An intermediate form, **in-situ** gene therapy, is injection of the vector directly into the target tissue, for example into a tumour.

## 5.2 Potential target diseases

### a. Inherited (monogenic) disorders

The ideal candidate is a disease caused by a single, well-understood gene, where a modest level of expression is enough, where the target cells can be reached, and where the current treatment is poor.

| Disease group | Examples |
| --- | --- |
| Immunodeficiencies | Severe combined immunodeficiency due to adenosine deaminase deficiency or to X-linked common γ-chain defects — the first conditions treated by gene therapy, by the ex-vivo route |
| Blood disorders | β-thalassaemia, sickle cell disease, haemophilia A and B (liver-directed factor VIII or IX genes) |
| Muscle and nerve | Duchenne muscular dystrophy, spinal muscular atrophy |
| Eye | Inherited retinal dystrophy caused by a defect in the RPE65 gene — a small, immune-privileged, easily injected target |
| Metabolic / storage | Lysosomal storage disorders, familial hypercholesterolaemia, urea-cycle defects |
| Lung | Cystic fibrosis (the CFTR gene) — attempted by the nasal and inhaled routes; limited by thick mucus and immune responses |

### b. Cancer

Cancer accounts for the majority of gene-therapy trials, because the disease is life-threatening and short-term expression is often enough. Approaches:

1. **Suicide-gene (GDEPT) therapy** — a gene for a foreign enzyme is expressed in tumour cells and a non-toxic prodrug is then given, which that enzyme converts into the active cytotoxic agent; neighbouring cells are also killed through the "bystander effect".
2. **Restoring a tumour-suppressor gene** such as p53, or **silencing an oncogene** with antisense or siRNA.
3. **Immunotherapy** — genes for cytokines or tumour antigens; genetically engineered T cells carrying a chimeric antigen receptor directed at a tumour antigen (an ex-vivo approach used in B-cell malignancies); genetic vaccines.
4. **Oncolytic viruses** engineered to replicate selectively in tumour cells and lyse them.
5. **Anti-angiogenic genes** that cut off the tumour's blood supply, and **genes that increase sensitivity** to radiation or chemotherapy.

Other areas under study: cardiovascular disease (therapeutic angiogenesis), neurodegenerative disease, infectious disease, and genetic vaccines — the last being the principle behind nucleic acid vaccines.

## 5.3 Gene expression systems — vectors

### a. What a gene must carry

A therapeutic gene construct ("expression cassette") contains a **promoter** (constitutive such as CMV, or tissue-specific, or inducible), the **transgene** (usually the complementary DNA), **enhancers**, a **polyadenylation signal**, and, in a plasmid, a bacterial origin of replication and a selection marker. Expression can be made selective by choosing a tissue-specific or tumour-specific promoter — an elegant form of targeting that works even if the carrier itself is not selective.

### b. The ideal vector

High efficiency of transfer; selectivity for the target cell; adequate capacity for the gene; expression at the right level and for the right time; no immunogenicity or toxicity; no risk of insertional mutagenesis; stable, reproducible and able to be manufactured at scale and stored.

### c. Viral vectors (transduction)

Viruses are natural gene-delivery machines; the pathogenic genes are removed and replaced by the therapeutic cassette, and the vector is produced in packaging cell lines.

| Vector | Genome and capacity | Integration and duration | Strengths | Limitations |
| --- | --- | --- | --- | --- |
| **Retrovirus (γ-retrovirus)** | RNA, about 8 kb | Integrates; long-lasting | Efficient, permanent in dividing cells | Infects only **dividing** cells; random integration risks insertional mutagenesis; low titre; inactivated by complement |
| **Lentivirus** (a retrovirus subgroup) | RNA, about 8–9 kb | Integrates; long-lasting | Transduces **non-dividing** cells too; favoured for ex-vivo stem-cell and T-cell work; safer "self-inactivating" designs | Integration risk remains; complex manufacture |
| **Adenovirus** | Double-stranded DNA, about 8 kb (up to about 36 kb for "gutless" forms) | **Episomal**, transient | Very high titres and very efficient in dividing and non-dividing cells; broad tropism | Strong innate and adaptive immune response; short expression; pre-existing immunity is common |
| **Adeno-associated virus (AAV)** | Single-stranded DNA, about **4.7 kb** | Mostly episomal; long expression in non-dividing tissue | Non-pathogenic, low immunogenicity, many serotypes with different tissue tropism (AAV2 eye, AAV8 liver, AAV9 crosses to the nervous system); the leading vector for in-vivo therapy | Very small capacity; pre-existing neutralising antibodies; costly manufacture; high doses needed |
| **Herpes simplex virus** | dsDNA, about 30–150 kb | Episomal; latency in neurons | Huge capacity; natural neurotropism | Cytotoxicity, inflammation |
| **Poxvirus / vaccinia, baculovirus** | Large dsDNA | Transient | Large capacity; strongly immunogenic, so useful for vaccines | Immunogenicity limits repeat dosing |

**General problems of viral vectors**: immune and inflammatory reactions (including severe reactions at high systemic doses), the risk of insertional mutagenesis with integrating vectors, the possibility of recombination into a replication-competent virus, limited capacity, high manufacturing cost and demanding quality control, and a cold chain.

### d. Non-viral vectors (transfection) — the pharmaceutics answer

Safer, cheaper, easier to make and to scale, with no limit on the size of the gene and little immunogenicity — but **much less efficient** and usually giving only transient expression.

**1. Physical methods**
- **Naked DNA injection** (intramuscular, intradermal) — simple, low efficiency.
- **Electroporation** — short pulses open transient pores; efficient locally.
- **Gene gun (biolistics)** — DNA-coated gold microparticles fired into skin; used for genetic vaccines.
- **Hydrodynamic injection** — rapid injection of a large volume; effective in the liver of small animals, hard to translate.
- **Sonoporation** with microbubbles, **magnetofection**, **laser** and **microinjection**.

**2. Chemical and colloidal carriers**

| Carrier | Principle and examples |
| --- | --- |
| **Cationic lipids (lipoplexes)** | Positively charged lipids such as DOTAP and DOTMA, usually with the helper lipid **DOPE**, bind DNA/RNA electrostatically. Easy to prepare, efficient in vitro; serum-sensitive and somewhat cytotoxic in vivo |
| **Ionisable lipid nanoparticles (LNPs)** | The modern form: the ionisable lipid is **positively charged at the low pH used for mixing**, so it binds the nucleic acid, but is **near-neutral at blood pH**, which greatly lowers toxicity; it becomes charged again in the acidic endosome and drives escape. A typical LNP also contains cholesterol, a helper phospholipid and a PEG-lipid, and is made by rapid **microfluidic mixing** of an ethanolic lipid stream with an acidic aqueous nucleic-acid stream. This is the carrier used for approved siRNA and mRNA products |
| **Cationic polymers (polyplexes)** | Polyethylenimine (branched or linear — the classic "proton sponge"), poly-L-lysine, chitosan (biodegradable, mucoadhesive, good for nasal and oral routes), dendrimers (PAMAM), polyamidoamines, cyclodextrin-containing polymers |
| **Lipid–polymer hybrids, micelles, inorganic carriers** | Calcium phosphate co-precipitates (an old, simple method), gold and silica nanoparticles, carbon nanotubes |
| **Receptor-targeted conjugates** | DNA complexed to a ligand–polycation conjugate (asialoglycoprotein for hepatocytes, transferrin, folate), **GalNAc conjugates** for highly efficient hepatocyte delivery of siRNA through the asialoglycoprotein receptor |

**Formulation parameters to quote**: the **N/P ratio** (moles of protonatable nitrogen of the carrier to moles of phosphate of the nucleic acid) controls complex size, charge and efficiency; particle size and zeta potential; and the **encapsulation efficiency** (commonly measured with the RiboGreen or PicoGreen dye-exclusion assay, with and without a detergent).

**Barriers the complex must still cross**: nuclease attack and serum protein binding → clearance by the MPS → extravasation → binding and endocytosis → **endosomal escape** → release of the nucleic acid from the carrier ("unpackaging") → for DNA only, entry through the nuclear envelope, which is the main reason DNA is far less efficient than mRNA or siRNA in non-dividing cells.

## 5.4 Liposomal gene delivery systems

Liposomes were the first widely used non-viral carriers and remain the basis of the clinically successful systems.

**Types used**

1. **Cationic liposomes / lipoplexes**: preformed cationic vesicles are simply mixed with the nucleic acid; the complex is held together by charge. Structure is usually a multilamellar "sandwich" of nucleic acid between bilayers, not a classical vesicle with an aqueous core. A net positive charge helps binding to the cell surface but also causes serum aggregation, complement activation and rapid lung and liver uptake after intravenous injection.
2. **Ionisable lipid nanoparticles** — as described above; the current standard for systemic use.
3. **Anionic and neutral liposomes** with the nucleic acid condensed first by protamine or a polycation, then encapsulated.
4. **pH-sensitive liposomes** containing DOPE, which changes from a bilayer to an inverted-hexagonal phase at low pH and fuses with the endosomal membrane.
5. **Stabilised plasmid–lipid particles and "stealth" PEGylated lipoplexes**, in which the nucleic acid is encapsulated inside a PEG-coated particle for longer circulation; cleavable PEG is used to allow uptake at the target.
6. **Immunoliposomes and ligand-bearing liposomes** for active targeting; **virosomes** using viral fusion proteins to help entry.

**Role of helper lipids**: DOPE promotes membrane fusion and endosomal escape; cholesterol gives stability in serum; the PEG-lipid controls particle size during manufacture and circulation time afterwards.

**Preparation**: simple mixing of the components for lipoplexes (order, rate and ionic strength of mixing matter greatly for reproducibility); thin-film hydration and extrusion; the ethanol-dilution method; and **microfluidic rapid mixing** for lipid nanoparticles, which gives reproducible, small, highly loaded particles and is the method used industrially.

**Evaluation of a gene delivery system**

| Test | Method |
| --- | --- |
| Complex formation and binding | Gel retardation (electrophoretic mobility shift) assay |
| Protection of the nucleic acid | Nuclease (DNase/RNase) protection assay followed by electrophoresis |
| Size, PDI, zeta potential, morphology | DLS, zeta potential, cryo-TEM |
| Encapsulation efficiency | RiboGreen/PicoGreen dye exclusion with and without Triton X-100 |
| Nucleic acid integrity | Agarose gel; for plasmids, the proportion of supercoiled form |
| Transfection efficiency in vitro | Reporter genes (green fluorescent protein, luciferase, β-galactosidase); flow cytometry; quantitative PCR for silencing |
| Cytotoxicity and haemocompatibility | MTT assay, lactate dehydrogenase release, haemolysis |
| Endosomal escape and trafficking | Confocal microscopy with labelled nucleic acid and endosomal markers |
| In vivo | Biodistribution, expression or silencing in target tissue, immune and inflammatory markers, histopathology |

## 5.5 Biodistribution and pharmacokinetics of nucleic acid therapeutics

Classical pharmacokinetics does not describe these agents well: what matters is not plasma concentration but **how much intact nucleic acid reaches the inside of the right cells, and how long the effect lasts**.

**Naked nucleic acid**: an unmodified oligonucleotide is degraded by serum nucleases within minutes and, being small, is filtered and excreted by the kidney — so the plasma half-life is very short and little reaches any tissue other than kidney and liver.

**Chemical stabilisation of oligonucleotides** (an examinable list): **phosphorothioate** backbone (one non-bridging oxygen replaced by sulfur) — far more nuclease-resistant and strongly protein-bound, which prolongs residence but can cause complement and coagulation effects; **2′-O-methyl and 2′-O-methoxyethyl** sugar modifications, **2′-fluoro**, **locked nucleic acid (LNA)**, **morpholino** and **peptide nucleic acid (PNA)** backbones; and the **gapmer** design, in which modified "wings" give stability while a central DNA gap still allows RNase H to act.

**After formulation in a carrier**, the pharmacokinetics become those of the *carrier*: rapid clearance from plasma, with distribution dominated by liver, spleen and, for positively charged complexes given intravenously, the lung capillary bed. Unmodified lipid nanoparticles are taken up mainly by hepatocytes, partly because apolipoprotein E adsorbs on the surface and is recognised by hepatic receptors — which is why the liver is by far the easiest organ to reach and why extra-hepatic delivery is the central research problem.

**Points to make in an answer**

1. Measure both the carrier (labelled lipid or polymer) and the nucleic acid, since they separate in the body.
2. Use the **pharmacodynamic** endpoint as well: protein expressed, or messenger RNA knocked down, and its duration.
3. There is a long lag between plasma clearance and loss of effect — silencing by siRNA in the liver can persist for weeks after the plasma level is undetectable, which allows infrequent dosing.
4. Route changes everything: local administration (eye, airway, tumour, muscle, intrathecal) gives high local levels with little systemic exposure; intravenous administration means liver and spleen; subcutaneous injection of a conjugate suits hepatocyte targets.
5. Elimination is by nuclease degradation to nucleotides that enter normal metabolic pools, by renal excretion of short fragments, and by hepatobiliary clearance of the carrier.
6. Safety assessment is specific: innate immune activation through Toll-like receptors (reduced by chemical modification and by using modified nucleosides in mRNA), complement activation, off-target hybridisation, and, for integrating vectors, insertional mutagenesis.

## 5.6 Antisense molecules and aptamers — "drugs of the future"

### a. Antisense oligonucleotides (ASOs)

A short, single-stranded, chemically modified oligonucleotide (usually about 15–25 bases) designed to be complementary to a chosen messenger RNA. **Mechanisms**:

1. **RNase H-dependent cleavage** — the DNA–RNA hybrid is recognised by RNase H, which cuts the messenger RNA; the main mechanism of gapmers.
2. **Steric block** — the oligonucleotide binds and physically blocks translation or the binding of a protein, without cleavage (used with fully modified chemistries such as morpholino and 2′-O-methoxyethyl).
3. **Splice switching** — the oligonucleotide masks a splice site and changes how the pre-messenger RNA is spliced, for example to skip a faulty exon or to include a needed one. This is the basis of approved treatments for spinal muscular atrophy and for some forms of Duchenne muscular dystrophy.

### b. RNA interference: siRNA and miRNA

Double-stranded **small interfering RNA** of about 21–23 base pairs is loaded into the **RNA-induced silencing complex (RISC)**; the passenger strand is discarded and the guide strand directs the complex to a perfectly complementary messenger RNA, which is then cleaved by Argonaute-2. **MicroRNAs** are natural, imperfectly matching regulators that mainly repress translation; **antagomirs** inhibit a microRNA and **miRNA mimics** replace a missing one. Compared with antisense oligonucleotides, siRNA is more potent and catalytic but is double-stranded, larger and essentially always needs a carrier (a lipid nanoparticle) or a conjugate (GalNAc) to get into cells.

### c. Ribozymes, DNAzymes and messenger RNA therapeutics

**Ribozymes** are catalytic RNA molecules (hammerhead, hairpin) that cleave a target RNA; **DNAzymes** are the DNA equivalent. **Therapeutic messenger RNA**, delivered in lipid nanoparticles and containing modified nucleosides to avoid innate immune activation, makes the cell produce a wanted protein for a limited time — the basis of nucleic acid vaccines and of protein-replacement research. Unlike DNA, it need reach only the cytoplasm, not the nucleus.

### d. Aptamers

**Aptamers** are short single-stranded DNA or RNA molecules (or peptides) that fold into a defined three-dimensional shape and bind a target molecule with high affinity and specificity — in effect, "chemical antibodies". They are selected in vitro by **SELEX** (Systematic Evolution of Ligands by EXponential enrichment):

```text
  Large random library (10^13–10^15 sequences)
        ↓  incubate with the target
  Binding sequences retained; non-binders washed away
        ↓  elute the bound sequences
  Amplify by PCR (reverse transcription first for RNA)
        ↓  prepare a new, enriched library
  Repeat 6–15 rounds (with counter-selection against related molecules)
        ↓
  Sequence, truncate and chemically stabilise the best aptamer
```

**Advantages over antibodies**: produced chemically, so no animals or cell culture are needed and batches are reproducible; small (about 6–30 kDa), so they penetrate tissue better; little or no immunogenicity; stable, able to be denatured and refolded; easy to modify, conjugate and reverse with a complementary "antidote" oligonucleotide.
**Limitations**: rapid nuclease degradation and renal clearance unless modified (2′-fluoro, 2′-O-methyl, 3′-capping, PEGylation or conjugation to cholesterol); limited to targets that are accessible in the extracellular space unless carried inside; and a long, costly selection and development process.

**Uses**: as drugs in their own right (the first approved aptamer blocked vascular endothelial growth factor in eye disease); as **targeting ligands** on liposomes, nanoparticles and micelles, which is the use most relevant to this subject; as **aptamer–siRNA chimeras** that both home to a cell-surface receptor and deliver a silencing RNA; and in diagnostics and biosensors (aptasensors).

## Remember

- Somatic gene therapy only; germline modification is not permitted. Ex vivo = cells modified outside the body and returned (controlled, costly); in vivo = vector given to the patient (simpler, but immune response and targeting are the problems).
- Targets: single-gene disorders (immunodeficiencies, haemophilia, thalassaemia, retinal dystrophy, spinal muscular atrophy, cystic fibrosis) and cancer (suicide-gene/GDEPT, tumour suppressors, engineered immune cells, oncolytic viruses).
- Viral vectors: retrovirus (dividing cells only, integrates), lentivirus (non-dividing too), adenovirus (high efficiency, transient, immunogenic), **AAV (about 4.7 kb, low immunogenicity, serotype-specific tropism — the leading in-vivo vector)**, HSV (large capacity, neurotropic).
- Non-viral: physical (electroporation, gene gun, hydrodynamic) and chemical (cationic lipids with DOPE, **ionisable lipid nanoparticles made by microfluidic mixing**, PEI and chitosan polyplexes, dendrimers, GalNAc conjugates). Safer and scalable but less efficient; quote the **N/P ratio**.
- The barrier list for any gene carrier: nucleases and serum → MPS → extravasation → endocytosis → **endosomal escape (proton sponge, DOPE fusion)** → unpackaging → nuclear entry (DNA only).
- Evaluation: gel retardation for binding, nuclease protection for stability, dye exclusion for encapsulation, reporter genes for transfection, MTT for toxicity.
- Pharmacokinetics: naked oligonucleotides last minutes; stabilise with phosphorothioate, 2′-O-methyl/MOE, LNA, morpholino, PNA and gapmer designs; formulated carriers go mainly to liver and spleen; judge by the pharmacodynamic effect and its duration, not plasma levels.
- Antisense works by RNase H cleavage, steric block or splice switching; siRNA works through RISC and Argonaute-2; aptamers are SELEX-selected "chemical antibodies" used both as drugs and as targeting ligands.
