# Unit 5: Cell signalling, receptors and protein kinases

This unit covers cell signals, the receptors that receive them, an overview of the main signalling pathways, what happens when pathways go wrong, and how protein kinases work. It is the most pharmacological unit: most drugs act on receptors or signalling proteins.

## 5.1 Cell signals: introduction

**Cell signalling** is the way cells communicate: a cell releases a signal, a target cell detects it with a **receptor**, and the receptor sets off a chain of events inside the cell (**signal transduction**) that ends in a **response** — change in metabolism, gene expression, movement, secretion, division or death.

### General steps

```text
 Signal (first messenger) → Receptor → Transducers / second messengers
     → Effector proteins (enzymes, channels, transcription factors) → Cell response
     → Termination (signal removed, receptor turned off)
```

### Types of signalling by distance

| Type | How the signal travels | Example |
| --- | --- | --- |
| Endocrine | Hormone in blood to distant cells | Insulin, adrenaline, thyroxine |
| Paracrine | Diffuses to nearby cells | Growth factors, histamine, nitric oxide |
| Autocrine | Acts on the cell that released it | Interleukin-2 on T cells; some cancer growth factors |
| Synaptic (neuronal) | Neurotransmitter across a synapse | Acetylcholine, noradrenaline |
| Contact-dependent (juxtacrine) | Membrane-bound signal touches receptor on neighbour | Notch–Delta signalling; immune cell recognition |
| Gap junctions | Small molecules pass directly between cytoplasms | Spread of Ca2+ and cAMP in heart muscle |

### Types of signal molecules

- **Hydrophilic** (peptides, catecholamines, acetylcholine) cannot cross the membrane, so they bind **cell-surface receptors**.
- **Lipophilic** (steroid hormones, thyroid hormones, vitamin D, retinoic acid) cross the membrane and bind **intracellular receptors**.
- **Gases** (nitric oxide) diffuse in and act directly on enzymes (soluble guanylyl cyclase).

### Key features of signalling

1. **Specificity** — a signal acts only on cells that have its receptor.
2. **Amplification** — one hormone molecule can lead to millions of product molecules through enzyme cascades.
3. **Integration** — a cell combines many signals at once.
4. **Desensitisation (adaptation)** — continued signal reduces the response.
5. **Termination** — signals are switched off by removing the signal, GTP hydrolysis, phosphatases and phosphodiesterases.

**Second messengers** are small molecules made inside the cell after receptor activation: **cAMP, cGMP, Ca2+, inositol trisphosphate (IP3), diacylglycerol (DAG)** and phosphatidylinositol trisphosphate (PIP3).

## 5.2 Receptors for cell signals

A **receptor** is a protein that binds a specific signal (ligand) and changes the activity of the cell. Drugs that bind and activate receptors are **agonists**; drugs that bind without activating and block agonists are **antagonists**.

| Receptor family | Structure | Transduction | Time to respond | Examples |
| --- | --- | --- | --- | --- |
| Ligand-gated ion channels (ionotropic) | Several subunits form a pore | Channel opens; ions flow | Milliseconds | Nicotinic acetylcholine, GABA-A, glutamate (NMDA, AMPA), 5-HT3 |
| G protein-coupled receptors (GPCRs) | Single chain crossing the membrane seven times | Activate a G protein → enzymes or channels | Seconds | β-adrenergic, muscarinic, opioid, histamine, dopamine, angiotensin |
| Enzyme-linked receptors | One transmembrane segment; enzyme domain inside or associated | Receptor kinase activity, phosphorylation cascades | Minutes to hours | Insulin and growth factor receptors (tyrosine kinases), TGF-β (serine/threonine kinase), cytokine receptors (JAK), ANP receptor (guanylyl cyclase) |
| Intracellular (nuclear) receptors | Ligand-binding, DNA-binding (zinc fingers) and activation domains | Hormone–receptor complex binds DNA and changes transcription | Hours to days | Glucocorticoid, oestrogen, androgen, thyroid hormone, vitamin D, retinoid receptors, PPARs |

### G protein-coupled receptors

GPCRs form the largest receptor family and are the targets of a large share of marketed drugs.

```text
         outside
   N— ╭╮ ╭╮ ╭╮ ╭╮   seven helices cross the membrane
 ═════│││││││││││═════
      ╰╯ ╰╯ ╰╯ ╰—C   inside: binds the G protein (αβγ)
```

**The G protein cycle:**

1. In the resting state the α subunit holds **GDP** and is bound to βγ.
2. The ligand-bound receptor acts as an exchange factor: Gα releases GDP and binds **GTP**.
3. Gα-GTP separates from βγ; both can regulate effectors.
4. Gα has built-in **GTPase** activity; it hydrolyses GTP to GDP and rejoins βγ — the signal switches off (helped by RGS proteins).

| G protein | Effector | Second messenger | Example receptors |
| --- | --- | --- | --- |
| Gs | Stimulates adenylyl cyclase | cAMP ↑ | β1, β2-adrenergic, H2, D1, glucagon, V2 |
| Gi | Inhibits adenylyl cyclase; βγ opens K+ channels | cAMP ↓ | α2-adrenergic, M2, opioid, D2 |
| Gq | Activates phospholipase C-β | IP3 and DAG ↑, Ca2+ ↑ | α1-adrenergic, M1, M3, H1, AT1 |

### Intracellular receptors

The steroid hormone diffuses into the cell and binds its receptor (in the cytoplasm for glucocorticoids, where the receptor is held by heat-shock proteins; in the nucleus for thyroid hormone). The complex binds **hormone response elements (HREs)** in DNA, recruits co-activators and changes the transcription of target genes. Effects need new protein synthesis, so they start slowly and last long — this explains why corticosteroids take hours to act.

## 5.3 Signalling pathways: overview

### 1. cAMP–protein kinase A pathway

```text
 Hormone → GPCR → Gs → adenylyl cyclase: ATP → cAMP
   cAMP binds regulatory (R) subunits of PKA (R2C2)
   → releases 2 active catalytic (C) subunits
   → phosphorylate target enzymes (glycogen phosphorylase kinase ↑, glycogen synthase ↓)
   → C subunits enter nucleus → phosphorylate CREB → gene transcription
 Off switch: phosphodiesterase (PDE) breaks cAMP → 5′-AMP
```

Example: adrenaline on liver raises blood glucose by glycogen breakdown; on the heart it raises rate and force (β1). Methylxanthines (theophylline, caffeine) inhibit PDE and raise cAMP.

### 2. Phosphoinositide–calcium pathway

```text
 Ligand → GPCR → Gq → phospholipase C-β
   PIP2 → IP3 + DAG
   IP3 → binds IP3 receptor on ER → Ca2+ released into cytosol
   DAG + Ca2+ → activate protein kinase C (PKC)
   Ca2+ → calmodulin → Ca2+/calmodulin-dependent kinases, myosin light-chain kinase
```

Responses: smooth muscle contraction, secretion, platelet activation. Lithium blocks inositol recycling, which damps this pathway.

### 3. Nitric oxide–cGMP pathway

Acetylcholine acts on endothelium → Ca2+ ↑ → nitric oxide synthase makes **NO** → NO diffuses into smooth muscle → activates **soluble guanylyl cyclase** → **cGMP** ↑ → protein kinase G → relaxation (vasodilation). Nitrates (glyceryl trinitrate) release NO; **sildenafil** inhibits **PDE5**, which breaks down cGMP.

### 4. Receptor tyrosine kinase (RTK)–Ras–MAP kinase pathway

```text
 Growth factor (EGF, PDGF) → binds RTK → two receptors pair (dimerise)
   → each phosphorylates the other on tyrosines (autophosphorylation)
   → phosphotyrosines bind adaptor Grb2 (SH2 domain) → SOS (exchange factor)
   → Ras-GDP → Ras-GTP (active)
   → Raf (MAPKKK) → MEK (MAPKK) → ERK (MAPK)
   → ERK enters nucleus → activates transcription factors → cell division genes
 Off: Ras hydrolyses its GTP (GTPase, helped by GAP proteins)
```

This is a **kinase cascade** — each kinase activates the next, giving great amplification.

### 5. PI3-kinase–Akt pathway (insulin pathway)

Insulin binds its receptor tyrosine kinase → insulin receptor substrate (IRS) is phosphorylated → **PI3-kinase** converts PIP2 to **PIP3** → **Akt (protein kinase B)** is activated → GLUT4 moves to the membrane (glucose uptake), glycogen synthesis rises, cell survival and growth (via mTOR) increase. **PTEN**, a phosphatase, reverses PIP3 formation and acts as a tumour suppressor.

### 6. JAK–STAT pathway

Cytokines (interferons, interleukins, erythropoietin, growth hormone) bind receptors without their own kinase activity. Associated **Janus kinases (JAKs)** phosphorylate the receptor and the **STAT** proteins; STATs pair up, move to the nucleus and switch on genes. JAK inhibitors (tofacitinib, ruxolitinib) block this.

### 7. Other important pathways

| Pathway | Key steps | Role |
| --- | --- | --- |
| TGF-β–SMAD | Receptor serine/threonine kinase phosphorylates SMADs → nucleus | Growth inhibition, fibrosis |
| Wnt–β-catenin | Wnt stops β-catenin destruction → β-catenin enters nucleus | Development, stem cells; mutated in colon cancer (APC) |
| Notch | Contact-dependent; receptor cut, its fragment goes to nucleus | Cell fate decisions |
| Hedgehog | Relieves inhibition of Smoothened | Development; basal cell carcinoma |
| NF-κB | IκB destroyed → NF-κB enters nucleus | Inflammation, immunity; target of glucocorticoids |

### Switching signals off

- Removal of ligand (enzymes, reuptake).
- GTP hydrolysis by G proteins and Ras.
- Phosphodiesterases destroy cAMP and cGMP.
- **Protein phosphatases** remove phosphates.
- **Desensitisation:** G protein-coupled receptor kinases (GRKs) phosphorylate the active receptor; **β-arrestin** binds and uncouples it from the G protein and promotes its **internalisation** (endocytosis). Long-term exposure reduces receptor numbers (**down-regulation**) — the basis of tolerance, e.g. to β2-agonists. Long-term blockade increases them (**up-regulation**).

## 5.4 Misregulation of signalling pathways

When a pathway is stuck "on" or "off", disease results.

| Misregulation | Mechanism | Disease | Drug approach |
| --- | --- | --- | --- |
| Ras mutation | Ras cannot hydrolyse GTP — permanently active | Many cancers (pancreas, colon, lung) | Newer drugs target specific mutant forms |
| BCR-ABL fusion (Philadelphia chromosome, t(9;22)) | Constantly active tyrosine kinase | Chronic myeloid leukaemia | Imatinib |
| HER2 (ErbB2) over-expression | Excess RTK signalling | Some breast cancers | Trastuzumab (antibody), lapatinib |
| EGFR activating mutations | Constant RTK signal | Non-small cell lung cancer | Gefitinib, erlotinib |
| BRAF V600E mutation | Constantly active Raf | Melanoma | Vemurafenib, dabrafenib |
| Loss of PTEN | PI3K–Akt pathway stays on | Several cancers | PI3K and mTOR inhibitors |
| JAK2 V617F mutation | Constant JAK–STAT signalling | Polycythaemia vera, myelofibrosis | Ruxolitinib |
| Cholera toxin | ADP-ribosylates Gsα → cannot hydrolyse GTP → cAMP stays high in gut cells → Cl− and water loss | Severe watery diarrhoea | Oral rehydration |
| Pertussis toxin | ADP-ribosylates Giα → cannot be activated → loss of inhibition | Whooping cough | Vaccination |
| Insulin receptor and post-receptor defects | Reduced response to insulin (insulin resistance) | Type 2 diabetes mellitus | Metformin, glitazones (PPARγ agonists) |
| Antibodies against receptors | Block or stimulate | Myasthenia gravis (block nicotinic receptor); Graves' disease (stimulate TSH receptor) | Anticholinesterases; antithyroid drugs |
| V2 receptor mutation | No response to ADH | Nephrogenic diabetes insipidus | Thiazides (paradoxical effect) |
| Constant NF-κB activation | Excess inflammatory genes | Rheumatoid arthritis, inflammatory bowel disease | Glucocorticoids, TNF-α blockers |

General lesson: **gain-of-function** changes in growth pathways (oncogenes) and **loss-of-function** of their brakes (tumour suppressors) cause cancer; toxins and autoantibodies can hijack normal receptors.

## 5.5 Protein kinases: functioning

A **protein kinase** is an enzyme that transfers the **terminal (γ) phosphate of ATP** to the hydroxyl group of a **serine, threonine or tyrosine** residue on a target protein:

Protein–OH + ATP → Protein–O–PO3²⁻ + ADP

The added phosphate (two negative charges) changes the protein's shape, activity, location or partners — it acts as an on/off switch. **Protein phosphatases** remove it, so the switch is reversible. Humans have about 500 protein kinase genes (the "kinome").

### Classification

| Class | Phosphorylates | Examples |
| --- | --- | --- |
| Serine/threonine kinases | Ser and Thr | PKA, PKC, PKG, Ca2+/calmodulin kinases, Akt, Raf, ERK (MAPK), CDKs |
| Receptor tyrosine kinases | Tyr | Insulin receptor, EGFR, HER2, PDGFR, VEGFR |
| Non-receptor tyrosine kinases | Tyr | Src, Abl, JAK, BTK |
| Dual-specificity kinases | Ser/Thr and Tyr | MEK (MAPK kinase) |

### Structure

The **catalytic (kinase) domain** of about 250–300 amino acids is shared by all kinases:

- A smaller **N-terminal lobe** (mostly β-sheet) with a glycine-rich loop that holds ATP.
- A larger **C-terminal lobe** (mostly α-helix) that binds the substrate protein.
- **ATP binds in the cleft** between the two lobes — this pocket is where most kinase-inhibitor drugs bind.
- An **activation loop** that must usually be phosphorylated for full activity.

```text
        N-lobe (β-sheet)
          ___________
         /  ATP site  \   ← cleft: ATP (and most inhibitor drugs) bind here
         \___________/
        C-lobe (α-helix) — substrate binding, activation loop
```

### How kinases are regulated

| Mechanism | Example |
| --- | --- |
| Second messenger binding | cAMP frees catalytic subunits of PKA; DAG + Ca2+ activate PKC; cGMP activates PKG |
| Binding of a partner protein | Cyclins activate CDKs; Ca2+/calmodulin activates CaM kinases |
| Phosphorylation by another kinase (cascade) | Raf → MEK → ERK |
| Autophosphorylation | Receptor tyrosine kinases after dimerisation |
| Removal of an inhibitory or pseudosubstrate segment | PKC pseudosubstrate leaves the active site when activated |
| Inhibitor proteins | p21, p27 on CDKs |
| Location (scaffold and anchoring proteins) | AKAPs place PKA near its targets |
| Dephosphorylation by phosphatases | PP1, PP2A; calcineurin (target of ciclosporin and tacrolimus) |

### Functions controlled by kinases

Metabolism (glycogen breakdown), gene transcription (CREB, STATs), cell cycle (CDKs), growth and survival (Akt, ERK), muscle contraction (myosin light-chain kinase), memory and synaptic change (CaM kinase II), immune cell activation (BTK, JAK).

### Protein kinase inhibitors as drugs

Most are small molecules that compete with ATP for the cleft; their names usually end in **"-tinib"**.

| Drug | Kinase target | Main use |
| --- | --- | --- |
| Imatinib | BCR-ABL, c-KIT | Chronic myeloid leukaemia, GIST |
| Gefitinib, erlotinib | EGFR | Non-small cell lung cancer |
| Lapatinib | EGFR and HER2 | HER2-positive breast cancer |
| Sorafenib, sunitinib | Several (VEGFR, PDGFR, Raf) | Kidney and liver cancer |
| Vemurafenib | Mutant BRAF | Melanoma |
| Trametinib | MEK | Melanoma (with BRAF inhibitor) |
| Palbociclib | CDK4/6 | Breast cancer |
| Ibrutinib | BTK | Chronic lymphocytic leukaemia |
| Tofacitinib, ruxolitinib | JAK | Rheumatoid arthritis; myelofibrosis |

Resistance often develops through mutations in the ATP pocket (for example the T315I "gatekeeper" mutation in BCR-ABL), which led to newer-generation inhibitors.

## Remember

- Signalling: signal → receptor → transduction (second messengers) → response → termination.
- Endocrine, paracrine, autocrine, synaptic, contact-dependent signalling.
- Four receptor families: ion channels (ms), GPCRs (s), enzyme-linked (min–h), nuclear receptors (h–days).
- Gs ↑ cAMP; Gi ↓ cAMP; Gq → PLC → IP3 (Ca2+) + DAG (PKC).
- PKA = R2C2; cAMP frees C subunits. PDE breaks cAMP; PDE5 inhibitors raise cGMP.
- RTK → Grb2–SOS → Ras → Raf → MEK → ERK; insulin → IRS → PI3K → PIP3 → Akt; cytokines → JAK–STAT.
- Desensitisation: GRK + β-arrestin; down-regulation explains tolerance.
- Cholera toxin keeps Gs on; pertussis toxin keeps Gi off; mutant Ras stays GTP-bound.
- Kinases put ATP's γ-phosphate on Ser, Thr or Tyr; phosphatases remove it; ATP pocket = drug site (imatinib, gefitinib).
