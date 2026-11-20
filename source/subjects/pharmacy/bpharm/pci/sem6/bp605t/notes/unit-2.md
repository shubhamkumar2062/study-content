# Unit 2: Expression Systems and Recombinant Proteins

Once a gene has been cloned, it must be expressed in a system capable of producing the encoded protein in sufficient quantity and quality for therapeutic use. This unit covers the biology of prokaryotic and eukaryotic expression systems, then describes the major recombinant therapeutic proteins on the market.

## 2.1 Prokaryotic expression systems

**Escherichia coli** is the most widely used expression host because it grows rapidly, is genetically well understood, can be cultured cheaply at large scale, and produces high yields of recombinant protein.

**Key components of a bacterial expression vector:**

| Component | Function |
| --- | --- |
| Strong inducible promoter (e.g. T7, lac, tac) | Controls transcription; induction allows accumulation of protein without slowing early growth |
| Ribosome binding site (Shine-Dalgarno sequence) | Essential for translation initiation in prokaryotes |
| His-tag or other affinity tag | Facilitates downstream purification |
| Terminator | Efficient mRNA termination |

**IPTG induction:** The *lac* promoter system is induced by isopropyl-β-D-thiogalactopyranoside (IPTG), a non-metabolisable lactose analogue that displaces the lac repressor and turns on transcription.

**Inclusion bodies:** When *E. coli* expresses large amounts of a foreign protein, the protein often accumulates as insoluble aggregates called **inclusion bodies**. This is both a problem and an advantage: inclusion bodies protect the protein from protease degradation and allow easy isolation by centrifugation, but the protein must be denatured and **refolded** to recover biological activity.

**Refolding process:** inclusion bodies dissolved in 6–8 M urea or 6 M guanidinium hydrochloride → slow removal of denaturant by dilution or dialysis → protein refolds → oxidative refolding with controlled thiol-disulphide exchange to form correct disulphide bonds.

**Advantages of *E. coli*:** fast growth (doubling time ~20 min), inexpensive media, high yields (up to 30% of total cell protein), well-characterised genetics, no cold chain needed during fermentation.

**Limitations:** Cannot glycosylate proteins; incorrect disulphide bond formation is common; endotoxin contamination of the final product requires rigorous removal; some eukaryotic proteins fold poorly in the prokaryotic cytoplasm.

## 2.2 Eukaryotic expression systems

### 2.2.1 Yeast

**Saccharomyces cerevisiae** was the first yeast used for pharmaceutical expression (recombinant hepatitis B vaccine, recombinant insulin). It can carry out some post-translational modifications and is GRAS (generally recognised as safe).

**Pichia pastoris** is now preferred for many proteins because it grows to very high cell densities on methanol (the AOX1 promoter is induced by methanol), secretes protein into the medium (simplifying purification), and glycosylates proteins (though the glycoforms differ from human patterns — high mannose).

Advantages over *E. coli*: glycosylation, correct disulphide bonds, secretion; disadvantages: glycans are not identical to human glycans; slower growth than bacteria.

### 2.2.2 Baculovirus / insect cell system

Recombinant baculovirus infects *Spodoptera frugiperda* (Sf9 or Sf21) or *Trichoplusia ni* (High Five) insect cells. The polyhedrin promoter, which is very strong in insect cells, is replaced with the gene of interest. The system supports glycosylation and complex protein assembly.

Uses: production of virus-like particles for vaccines, multiprotein complexes for structural studies, and some diagnostics. Scale-up is more difficult than bacterial systems.

### 2.2.3 Mammalian cell expression

**Chinese Hamster Ovary (CHO) cells** and **Human Embryonic Kidney 293 (HEK293) cells** are the dominant systems for biopharmaceuticals that require human-compatible post-translational modifications.

**Advantages of mammalian cells:**
- Correct glycosylation (closest to human patterns)
- Correct folding and disulphide bond formation
- Secretion of the product into the medium
- Best suited for therapeutic proteins where glycan identity affects half-life, immunogenicity or activity (e.g. EPO, monoclonal antibodies)

**Disadvantages:** slow growth, expensive culture media, risk of viral contamination, requires extensive viral clearance validation, lower yield per litre than bacterial cultures.

**Stable cell lines** are made by integrating the expression construct into the host chromosome so the gene is inherited by all daughter cells. Selection with dihydrofolate reductase (dhfr) and methotrexate amplification is a classical method for increasing gene copy number in CHO cells.

### 2.2.4 Plant and transgenic animal systems

**Plant expression (Pharming in plants):** Foreign genes are introduced into plants (tobacco, maize, potato) via *Agrobacterium tumefaciens* or biolistics. Proteins accumulate in seeds or leaves and are eaten or extracted. Advantages: low cost, easy scale-up, no mammalian pathogens. Disadvantages: plant glycans may be immunogenic; regulatory pathway is unclear.

**Transgenic animals:** The gene is inserted into the germline of an animal (goat, sheep, cow) under the control of a mammary-specific promoter (e.g. from the beta-casein gene), so the recombinant protein is secreted into milk. Antithrombin and AT-III are examples produced in transgenic goats. Concerns include animal welfare, transgene transmission to the environment, and difficult purification from milk.

## 2.3 Recombinant human insulin

**Historical background:** Before 1982, insulin was extracted from pig or cow pancreas. Animal insulin differed slightly in amino acid sequence, causing immunological reactions in some patients. Recombinant human insulin was the first approved recombinant therapeutic protein (Humulin, 1982, Genentech/Eli Lilly).

**Structure:** Human insulin has 51 amino acids in two chains: chain A (21 amino acids) and chain B (30 amino acids), linked by two interchain disulphide bonds (A7–B7 and A20–B19); chain A also has an intrachain disulphide bond (A6–A11).

**Production in *E. coli* (two routes):**

Route 1 — Separate chain synthesis: chain A and chain B are expressed as separate fusion proteins, cleaved from the fusion partner, mixed and oxidatively combined to form the correct disulphide bonds.

Route 2 — Proinsulin route: a synthetic proinsulin gene (with introns removed) is expressed in *E. coli* as a fusion protein, the C-peptide is cleaved in vitro using trypsin and carboxypeptidase B, and the resulting insulin is purified. This is the preferred industrial method.

**Production in yeast:** Proinsulin is expressed in *Saccharomyces cerevisiae* or *Pichia pastoris* and secreted into the medium; the C-peptide is then enzymatically removed. Yeast production gives fewer endotoxin concerns.

**Comparison with animal insulin:**
- Human insulin differs from pig insulin in one amino acid (B30: threonine in human, alanine in pig) and from bovine insulin in three amino acids.
- Recombinant human insulin is less immunogenic, eliminates the need for large-scale slaughterhouse supply, and can be produced consistently.

## 2.4 Recombinant growth hormone (Somatropin)

Human growth hormone (hGH) is a 191-amino acid protein secreted by the anterior pituitary. Before 1985, hGH for clinical use was extracted from cadaver pituitary glands, causing transmission of Creutzfeldt-Jakob disease (CJD) in some patients; it was withdrawn in 1985.

Somatropin (recombinant hGH) is expressed in *E. coli*. The original *E. coli* product had an extra N-terminal methionine (met-hGH), which was later removed by designing the construct to initiate with the correct human sequence. Modern products are identical to the natural hormone.

Uses: growth hormone deficiency in children and adults, Turner syndrome, Prader-Willi syndrome, short stature in children with chronic renal failure.

## 2.5 Recombinant erythropoietin (EPO)

Erythropoietin is a 165-amino acid glycoprotein produced by the kidney that stimulates red blood cell production. It is heavily glycosylated (40% of its mass is carbohydrate), and glycosylation is essential for its in vivo half-life and activity — this is why *E. coli* cannot be used.

**Production:** EPO is expressed in CHO cells, purified by multiple chromatography steps, and formulated as an injection.

**Uses:** Anaemia of chronic kidney disease, chemotherapy-induced anaemia, anaemia in HIV infection treated with zidovudine, preparation for autologous blood donation.

**Darbepoetin alfa** is a hyperglycosylated analogue (two extra N-glycosylation sites) with a longer half-life allowing less frequent dosing.

**Misuse:** EPO is abused by endurance athletes to raise haematocrit (blood doping). Its misuse causes polycythaemia, hypertension and thromboembolism.

## 2.6 Recombinant coagulation factors

**Factor VIII** is a large glycoprotein (2,332 amino acids) that acts as a cofactor in the coagulation cascade. Its deficiency causes haemophilia A, the most common severe bleeding disorder. Before recombinant technology, Factor VIII was pooled from thousands of donor plasma units; HIV and hepatitis C were transmitted this way on a wide scale in the 1980s.

Recombinant Factor VIII (e.g. Recombinate, Advate) is expressed in CHO or BHK cells. It eliminated the risk of viral transmission and has become the standard of care in developed countries. Extended half-life products (PEGylated or Fc-fusion Factor VIII) allow less frequent infusions.

**Factor IX** deficiency causes haemophilia B. Recombinant Factor IX (Benefix) is also produced in CHO cells. Gene therapy (adeno-associated virus delivery of the Factor IX gene) is now approved and may cure haemophilia B with a single treatment.

## 2.7 Tissue plasminogen activator (tPA)

Alteplase (rtPA) is a recombinant form of the natural serine protease that activates plasminogen to plasmin, dissolving fibrin clots. It is a 527-amino acid glycoprotein expressed in CHO cells; glycosylation is necessary for its activity and clearance rate.

Uses: acute myocardial infarction (within hours of onset), ischaemic stroke (within 4.5 hours), massive pulmonary embolism.

Tenecteplase (TNKase) and reteplase are engineered variants with longer half-lives or greater fibrin specificity, expressed in *E. coli* (reteplase, unglycosylated) or CHO cells.

## 2.8 Interferons

Interferons are cytokines produced in response to viral infection and other stimuli. Three main types:

**Interferon-alpha (IFN-α):** produced by leucocytes; antiviral and antiproliferative. Recombinant IFN-α2a (Roferon-A) and IFN-α2b (Intron-A) are expressed in *E. coli*. Uses: chronic hepatitis B and C, hairy cell leukaemia, Kaposi sarcoma, some solid tumours. PEGylation extends the half-life (Peg-IFN-α2a, Peg-IFN-α2b), reducing dosing from thrice-weekly to once-weekly.

**Interferon-beta (IFN-β):** produced by fibroblasts; immunomodulatory. Recombinant IFN-β1a (Avonex, produced in CHO cells) and IFN-β1b (Betaseron, produced in *E. coli*, with a serine substitution at position 17 for stability) are used in relapsing-remitting multiple sclerosis.

**Interferon-gamma (IFN-γ):** produced by T cells and NK cells; activates macrophages. IFN-γ1b (Actimmune, produced in *E. coli*) is used for chronic granulomatous disease and severe malignant osteopetrosis.

**Common adverse effects of interferons:** flu-like syndrome (fever, chills, myalgia, headache) — the most frequent; depression and mood disturbances; myelosuppression; raised liver enzymes; injection-site reactions.

## 2.9 Interleukins and colony-stimulating factors

**Interleukin-2 (IL-2, aldesleukin):** expressed in *E. coli*; used in metastatic renal cell carcinoma and melanoma (high-dose IL-2 therapy); causes severe capillary leak syndrome.

**Colony-stimulating factors (CSFs)** stimulate the proliferation and differentiation of blood cell precursors.

| CSF | Producer | Main action | Clinical use |
| --- | --- | --- | --- |
| G-CSF (filgrastim, lenograstim) | *E. coli* | Stimulates neutrophil production and release | Chemotherapy-induced neutropenia, bone marrow transplantation, mobilisation of stem cells |
| GM-CSF (sargramostim) | Yeast | Stimulates neutrophils and macrophages | Bone marrow transplant recovery, chemotherapy-induced myelosuppression |

**Pegfilgrastim** is PEGylated G-CSF with a longer half-life, allowing a single injection per chemotherapy cycle rather than daily filgrastim injections.

## Remember

1. *E. coli* gives high yields, is cheap and fast, but cannot glycosylate proteins and tends to form inclusion bodies; use it for small, non-glycosylated proteins (insulin, GH, IFN-β1b).
2. CHO and HEK293 cells are the gold standard for glycoproteins (EPO, Factor VIII, tPA, monoclonal antibodies) because they produce human-compatible glycans.
3. Recombinant insulin is the first approved recombinant drug (1982); proinsulin route in *E. coli* or yeast is the industrial standard.
4. EPO must be expressed in mammalian cells (CHO) because glycosylation is essential for its in vivo half-life.
5. PEGylation extends the half-life of proteins such as interferons and G-CSF by increasing size and reducing renal filtration.
6. Haemophilia A = Factor VIII deficiency; haemophilia B = Factor IX deficiency; both are now treated with recombinant products from CHO cells.
7. Interferons cause a flu-like syndrome; IFN-α is used in hepatitis; IFN-β in multiple sclerosis; IFN-γ in chronic granulomatous disease.
8. G-CSF (filgrastim) is the main drug used to prevent or treat chemotherapy-induced neutropenia.
