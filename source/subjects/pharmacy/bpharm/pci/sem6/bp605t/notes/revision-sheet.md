# Last-night revision sheet

If you have only an hour, master these six: **gene cloning steps**, **PCR cycle**, **hybridoma technology**, **penicillin fermentation**, **mAb downstream processing**, and **biosimilar vs originator**. Then read the recombinant proteins table and the comparison tables once each.

## Key terms to know cold

| Term | One-line definition |
| --- | --- |
| Restriction endonuclease | Bacterial enzyme that cuts dsDNA at a specific palindromic sequence |
| DNA ligase (T4) | Seals nicks in dsDNA using ATP; joins sticky or blunt ends in cloning |
| Vector | DNA molecule (plasmid, phage, BAC, YAC) that carries a foreign gene into a host and allows replication |
| Competent cells | Bacteria made able to take up foreign DNA (CaCl₂ treatment or electroporation) |
| Sticky ends | Single-stranded overhangs produced by most Type II restriction enzymes; allow annealing with complementary ends |
| IPTG | Isopropyl-β-D-thiogalactopyranoside; non-metabolisable inducer of *lac* promoter in *E. coli* |
| Inclusion bodies | Insoluble aggregates of recombinant protein in *E. coli*; require solubilisation and refolding |
| Hybridoma | Cell formed by fusing a B lymphocyte with a myeloma cell; immortal and antibody-secreting |
| HAT medium | Hypoxanthine, aminopterin, thymidine; selects only hybridomas (unfused myeloma cells die) |
| CDR | Complementarity-determining region; the antigen-contact loops within the variable domain |
| Biosimilar | Biologic approved on the basis of demonstrated similarity to an approved reference product |
| Lyophilisation | Freeze-drying; freezing followed by sublimation of ice under vacuum |
| LAL test | Limulus amebocyte lysate test; detects bacterial endotoxin |
| Protein A | *S. aureus* protein that binds Fc of IgG; used as the first capture step in mAb purification |
| Fed-batch | Fermentation mode in which nutrients are added during the run; extends productive phase |

## Comparison tables

### *E. coli* vs eukaryotic expression systems

| Feature | *E. coli* | Yeast (*Pichia*) | CHO cells |
| --- | --- | --- | --- |
| Growth rate | Very fast (20 min doubling) | Fast | Slow (24 h doubling) |
| Cost | Very low | Low | High |
| Glycosylation | None | High mannose; not human | Human-compatible |
| Disulphide bonds | Often mismatched | Usually correct | Correct |
| Secretion | Poor (mostly intracellular) | Good | Good |
| Endotoxin | Yes (LPS) | No | No |
| Examples | Insulin, GH, IFN-β1b | Hepatitis B vaccine, insulin | EPO, Factor VIII, mAbs, tPA |

### Batch vs fed-batch vs continuous fermentation

| Feature | Batch | Fed-batch | Continuous |
| --- | --- | --- | --- |
| Nutrients | Added at start only | Added during run | Added and removed continuously |
| Volume | Constant | Increases | Constant |
| Duration | Fixed (hours–days) | Extended | Indefinite (weeks–months) |
| Contamination risk | Lower | Lower | Higher |
| Main use | Beer, wine, vaccines | Penicillin, recombinant proteins | Wastewater, some amino acids |

### Biosimilar vs originator biologic

| Feature | Originator biologic | Biosimilar |
| --- | --- | --- |
| First approval | Full clinical trial package | Comparability data + abbreviated clinical |
| Approval pathway | BLA (FDA), MAA (EMA), NDA (CDSCO) | Abbreviated BLA (FDA 351(k)), CHMP guideline |
| Manufacturing | Original cell line and process | Different cell line; must demonstrate comparability |
| Identical to reference? | Is the reference | Highly similar, not identical |
| Naming | INN alone | INN + suffix (US); same INN (EU) |
| Cost | High | Lower (20–80% reduction) |

### Chromatography types used in biopharmaceutical purification

| Type | Basis of separation | Ligand/stationary phase | Use |
| --- | --- | --- | --- |
| Affinity | Specific interaction (Protein A–Fc) | Protein A, substrate analogues, His-tag Ni resin | Highest specificity; first capture step |
| Ion exchange | Charge | DEAE (anion), CM/SP (cation) | Most impurity removal |
| Size exclusion | Molecular size | Sephadex, Superose | Aggregate removal, polishing, analytical |
| Hydrophobic interaction | Hydrophobicity | Butyl-, phenyl-Sepharose | Used at high salt (after ammonium sulphate) |

## Text diagrams

### Hybridoma technology flowchart

```text
Immunise mouse with antigen
          ↓
Collect spleen cells (3–5 days after last boost)
          ↓
Fuse with HGPRT-negative myeloma cells using PEG
          ↓
Culture in HAT medium
  ├── Unfused myeloma cells DIE (blocked main pathway, no salvage)
  ├── Unfused B cells DIE (limited lifespan)
  └── Hybridomas SURVIVE (use salvage pathway from B-cell nucleus)
          ↓
Dilute into 96-well plates (1 cell/well) → clonal expansion
          ↓
Screen supernatants by ELISA for specific antibody
          ↓
Re-clone positive wells → confirm monoclonality
          ↓
Scale up → bioreactor or mouse ascites → Protein A purification
          ↓
MONOCLONAL ANTIBODY
```

### Penicillin production summary

```text
P. chrysogenum spore stock
          ↓
Shake flask → seed fermenter
          ↓
Production fermenter (fed-batch, 25–26°C, pH 6.0–6.5)
Medium: corn steep liquor + lactose + phenylacetic acid (Pen G precursor)
          ↓
Ferment 6–8 days (penicillin accumulates in idiophase)
          ↓
Mycelium removed by filtration
Broth acidified (pH 2–3) → extract into organic solvent
Re-extract into aqueous buffer (pH 7) → charcoal treatment → crystallise
          ↓
Potassium penicillin G crystal
```

## Recombinant therapeutic proteins reference table

| Product | Gene/protein | Host system | Key indication |
| --- | --- | --- | --- |
| Insulin (Humulin, Novolog) | Proinsulin | *E. coli* or yeast | Type 1 and type 2 diabetes |
| Somatropin (Genotropin) | hGH (191 aa) | *E. coli* | GH deficiency, Turner syndrome |
| Erythropoietin (Epoetin alfa) | EPO (165 aa glycoprotein) | CHO cells | Anaemia of CKD, chemotherapy |
| Darbepoetin alfa (Aranesp) | Hyperglycosylated EPO analogue | CHO cells | Less frequent dosing (longer half-life) |
| Factor VIII (Advate) | Coagulation factor VIII | CHO/BHK cells | Haemophilia A |
| Factor IX (Benefix) | Coagulation factor IX | CHO cells | Haemophilia B |
| Alteplase (Activase) | tPA (527 aa) | CHO cells | MI, ischaemic stroke, PE |
| IFN-α2b (Intron-A) | Interferon-alpha | *E. coli* | Hepatitis B/C, hairy cell leukaemia |
| IFN-β1a (Avonex) | Interferon-beta | CHO cells | Multiple sclerosis |
| IFN-β1b (Betaseron) | Interferon-beta (Cys17→Ser) | *E. coli* | Multiple sclerosis |
| Filgrastim (Neupogen) | G-CSF | *E. coli* | Chemotherapy-induced neutropenia |
| Rituximab (Mabthera) | Anti-CD20 chimeric mAb | CHO cells | B-cell lymphoma, RA |
| Trastuzumab (Herceptin) | Anti-HER2 humanised mAb | CHO cells | HER2+ breast cancer |
| Adalimumab (Humira) | Anti-TNF-α fully human mAb | CHO cells | RA, Crohn's, psoriasis |
| Hepatitis B vaccine | HBsAg | *S. cerevisiae* | HBV prevention |

## Scoring tips

1. **Draw the bioreactor.** Two boxes with components labelled (sparger, impeller, baffles, probes, jacket) is worth 3–4 marks in a 10-mark fermentation question.
2. **Write the PCR cycle as three named steps with their temperatures.** Denaturation 95°C, annealing 55–65°C, extension 72°C. Add: Taq polymerase from *Thermus aquaticus*; Mullis 1983 Nobel Prize 1993.
3. **For hybridoma, explain HAT selection clearly.** State what aminopterin does (blocks de novo purine/pyrimidine synthesis) and why the myeloma cells die (they cannot use the salvage pathway due to their HGPRT mutation).
4. **For biosimilar questions, use the word "comparability."** Regulators ask for a comparability exercise; the drug is highly similar, not identical, because living cells cannot produce identical molecules.
5. **State units and limits for quality control.** Endotoxin limit: 5 EU/kg per dose (IV products). Residual host cell DNA: < 10 ng per dose (WHO). These numbers earn marks in a 10-mark QC or DSP question.
6. **Know the virus clearance steps.** Low pH (inactivates enveloped viruses), solvent/detergent (enveloped), viral nanofiltration 20 nm (enveloped and some non-enveloped). Two orthogonal steps required; ICH Q5A is the guiding document.
