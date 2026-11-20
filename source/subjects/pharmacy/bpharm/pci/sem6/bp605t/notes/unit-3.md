# Unit 3: Monoclonal Antibodies, Vaccines and Diagnostics

Antibodies are the most important class of biopharmaceutical by sales value, and immunodiagnostic assays underpin almost all modern clinical laboratory testing. This unit covers the technology behind both.

## 3.1 Antibody structure

An IgG antibody molecule is a Y-shaped glycoprotein of about 150 kDa composed of two identical heavy chains (H, ~50 kDa each) and two identical light chains (L, ~25 kDa each), held together by disulphide bonds.

```text
           Antigen-binding site
                 ↓       ↓
         Fab    [VH|VL]  [VH|VL]  Fab
                  |          |
         Fc      [CH2|CH2]           Complement / receptor binding
                  |
                [CH3|CH3]
```

**Variable regions (V regions, VH and VL):** The N-terminal domains that differ in sequence between antibodies and are responsible for antigen recognition. Within the variable regions, three segments called **complementarity-determining regions (CDRs)** make direct contact with antigen; the CDRs are also called hypervariable loops. The surrounding framework regions hold the CDRs in the correct conformation.

**Constant regions (C regions, CH and CL):** Determine antibody class (IgG, IgA, IgM, IgE, IgD) and effector functions. The Fc region of IgG binds to Fc receptors on immune cells and initiates complement fixation.

**Fab fragment** = antigen-binding fragment (one VH, one VL, one CH1, one CL); **Fc fragment** = crystallisable fragment (the remaining two CH2 and CH3 domains). Papain cleaves IgG into two Fab and one Fc; pepsin cleaves into one F(ab')₂ and small Fc fragments.

## 3.2 Hybridoma technology

Hybridoma technology, developed by **Georges Köhler and César Milstein** in 1975 (Nobel Prize 1984), allows the production of large quantities of a single, highly specific antibody — a monoclonal antibody (mAb).

**Key problem before hybridoma technology:** B cells that produce a specific antibody cannot be cultured indefinitely; myeloma cells are immortal but do not produce a specific antibody. The solution was to fuse the two.

**Step-by-step hybridoma procedure:**

```text
Step 1: IMMUNISATION
  Inject antigen into a mouse → immune response develops →
  B cells in the spleen become activated

Step 2: SPLEEN CELL ISOLATION
  Sacrifice the mouse 3–5 days after the last booster
  → isolate spleen cells (mixture of B cells making the desired antibody
    plus many other B cells)

Step 3: FUSION
  Mix spleen cells with myeloma cells (use non-antibody-secreting,
  HAT-sensitive myeloma line, e.g. SP2/0 or NS0) in the presence of
  polyethylene glycol (PEG) → cell membranes fuse to form hybridomas
  (hybrid cells containing both nuclei)

Step 4: HAT SELECTION
  Culture in HAT medium (Hypoxanthine, Aminopterin, Thymidine)
  Aminopterin blocks the main pathway of nucleotide synthesis
  Unfused myeloma cells: cannot use the salvage pathway (blocked by
    the myeloma mutation), die
  Unfused B cells: die naturally within 1–2 weeks (B cells have limited
    lifespan in culture)
  Hybridomas: use the salvage pathway supplied by the B-cell nucleus
    (HGPRT from the spleen cell) and survive

Step 5: CLONING
  Dilute into 96-well plates so each well contains approximately
  one cell → growing clones are single-cell-derived hybridomas

Step 6: SCREENING
  Test supernatants by ELISA for antibody that binds the antigen
  → identify positive clones → re-clone to ensure monoclonality

Step 7: PRODUCTION
  Expand positive clones → grow in bioreactors or as ascites in mice
  → harvest and purify antibody by Protein A/G affinity chromatography
```

The resulting antibodies are **entirely murine (mouse-derived)**. Human patients make an immune response to mouse antibodies (**HAMA — human anti-mouse antibody response**), which limits repeated dosing.

## 3.3 Engineering antibodies to reduce immunogenicity

| Generation | Description | Example |
| --- | --- | --- |
| Murine mAb (-omab) | Entirely mouse sequence | Muromonab-CD3 (OKT3) |
| Chimeric mAb (-ximab) | Mouse V regions + human C regions (~65% human) | Rituximab, cetuximab, infliximab |
| Humanised mAb (-zumab) | Mouse CDRs grafted onto human framework (~95% human) | Trastuzumab, bevacizumab, alemtuzumab |
| Fully human mAb (-umab) | Entirely human; from phage display or transgenic mice | Adalimumab, denosumab, ustekinumab |

**CDR grafting:** Only the three CDR loops from the mouse antibody (which determine specificity) are transferred onto a human antibody framework, retaining specificity while greatly reducing immunogenicity.

**Phage display:** Human antibody variable region gene libraries are displayed on the surface of bacteriophage; phage binding the antigen are selected and the antibody gene isolated. This generates fully human antibodies without immunisation.

## 3.4 Therapeutic monoclonal antibodies

| Drug | Target | Indication | Key toxicity/note |
| --- | --- | --- | --- |
| Rituximab (Mabthera) | CD20 on B cells | Non-Hodgkin lymphoma, CLL, rheumatoid arthritis | Progressive multifocal leucoencephalopathy (PML) |
| Trastuzumab (Herceptin) | HER2/neu receptor | HER2-positive breast and gastric cancer | Cardiotoxicity (LVEF monitoring required) |
| Bevacizumab (Avastin) | VEGF (anti-angiogenic) | Colorectal, lung, ovarian cancer | Hypertension, impaired wound healing, thromboembolism |
| Adalimumab (Humira) | TNF-alpha | Rheumatoid arthritis, Crohn's, psoriasis | Reactivation of TB and hepatitis B; infections |
| Cetuximab (Erbitux) | EGFR | Colorectal and head/neck cancer | Acneiform skin rash (marker of response) |
| Pembrolizumab (Keytruda) | PD-1 (checkpoint inhibitor) | Multiple solid tumours | Immune-related adverse effects |

**Naming convention for mAbs:**
- Target infix: -li- (immunological), -tu- (tumour), -ci- (cardiovascular), -ba- (bacterial)
- Source suffix: -o- (mouse), -xi- (chimeric), -zu- (humanised), -u- (human)
- Plus the class suffix -mab

## 3.5 Bispecific antibodies and antibody-drug conjugates

**Bispecific antibodies** can simultaneously bind two different antigens. For example, blinatumomab (BiTE — bispecific T-cell engager) binds both CD3 on T cells and CD19 on B-cell leukaemia cells, bringing them together to trigger killing. Used in acute lymphoblastic leukaemia.

**Antibody-drug conjugates (ADCs):** A monoclonal antibody is chemically linked to a cytotoxic payload (a small molecule too toxic to give systemically) through a cleavable or non-cleavable linker. The antibody guides the payload to the tumour cell; receptor-mediated endocytosis internalises the complex; the linker is cleaved inside the cell, releasing the drug. Examples: ado-trastuzumab emtansine (T-DM1) for HER2-positive breast cancer; brentuximab vedotin (anti-CD30, with MMAE) for Hodgkin lymphoma.

## 3.6 Recombinant vaccines

**Hepatitis B vaccine** was the first approved recombinant subunit vaccine (1986). The gene for the hepatitis B surface antigen (HBsAg) is expressed in *Saccharomyces cerevisiae*. The expressed protein self-assembles into 22-nm virus-like particles (VLPs) that are immunogenic but non-infectious. This eliminated the need for plasma-derived antigen and the associated risk of blood-borne pathogen contamination. The vaccine is part of routine childhood immunisation worldwide.

**HPV vaccine (Gardasil, Cervarix):** VLPs assembled from the L1 capsid protein of HPV types 16 and 18 (and types 6 and 11 for Gardasil). Expressed in yeast (Gardasil) or baculovirus/insect cells (Cervarix). Protects against cervical cancer precursors.

**DNA vaccines:** A plasmid carrying the antigen gene under a mammalian promoter is injected directly into muscle. Host cells express the antigen, triggering humoral and cellular immune responses. Advantages: stable at room temperature, cheap to produce. Disadvantages: lower immunogenicity in humans than in rodents; regulatory pathway complex. Approved for veterinary use; several DNA vaccines for COVID-19 and other diseases under development.

**Viral vector vaccines:** An attenuated, replication-deficient virus (commonly adenovirus or modified vaccinia Ankara) carries the antigen gene. The vector infects host cells, which express the antigen. Used for Ebola (VSV-based rVSV-ZEBOV), COVID-19 (ChAdOx1 nCoV-19/AstraZeneca, Ad26.COV2.S/Johnson & Johnson). The adenovirus backbone cannot replicate in human cells (deletions in E1 gene), so there is no disease risk from the vector itself.

**Malaria vaccine (RTS,S/Mosquirix):** Partial protection; contains a portion of the circumsporozoite protein of *Plasmodium falciparum* fused to HBsAg; expressed in yeast; forms VLPs.

## 3.7 ELISA

The **enzyme-linked immunosorbent assay (ELISA)** is the most widely used immunoassay format.

**Sandwich ELISA (most common for detecting antigens):**

```text
Step 1: Coat microtitre plate wells with capture antibody
Step 2: Block non-specific binding with BSA or skim milk
Step 3: Add sample containing antigen → antigen binds to capture antibody
Step 4: Add detection antibody (enzyme-conjugated, usually HRP or AP,
        specific for a different epitope on the same antigen)
Step 5: Add enzyme substrate → colour develops in proportion to antigen
Step 6: Stop reaction with acid → read absorbance at 450 nm
```

**Indirect ELISA:** used to detect antibodies; the antigen is coated on the plate; the patient's sample is added; a secondary anti-human antibody conjugated to enzyme is then used to detect bound antibody. Used in HIV serology (ELISA screening followed by Western blot confirmation).

**Competitive ELISA:** used to detect small molecules (haptens) that have only one epitope. A fixed amount of labelled antigen competes with the unlabelled sample antigen for the antibody. More antigen in the sample → less labelled antigen binds → less signal. Inversely proportional.

**Applications of ELISA:** pregnancy tests (hCG), HIV and hepatitis serology, blood bank testing, therapeutic drug monitoring, detection of food allergens, troponin in myocardial infarction.

## 3.8 Other immunoassay formats

**Radioimmunoassay (RIA):** The original immunoassay (Berson and Yalow, Nobel Prize 1977). Uses radiolabelled antigen (usually ¹²⁵I). Very sensitive but requires a radioactive waste licence; largely replaced by ELISA and chemiluminescent assays in clinical labs.

**Chemiluminescence immunoassay (CLIA):** Similar to ELISA but uses a chemiluminescent label (acridinium ester or luminol) instead of a coloured enzyme product. Very high sensitivity; used in automated analysers for thyroid hormones, cardiac markers (troponin, BNP), hormones (LH, FSH, hCG), vitamin D, and drug levels.

**Lateral flow immunoassay (rapid diagnostic tests):** A nitrocellulose strip with coloured latex or gold nanoparticle-labelled antibody in the conjugate pad. Sample wicks along the strip; labelled antibody-antigen complexes are captured at the test line; excess labelled antibody is captured at the control line. No equipment needed; results in 15–30 minutes. Used for pregnancy tests, influenza A/B, COVID-19 antigen, malaria, dengue.

## Remember

1. CDRs (complementarity-determining regions) on the variable domain are the antigen-binding loops; there are three CDRs on each of VH and VL.
2. Hybridoma technology = immunise mouse → fuse spleen cells with HGPRT-negative myeloma cells → HAT selection → clone → screen by ELISA. HAT selects only hybridomas.
3. Chimeric mAb (-ximab) = mouse V regions + human C regions. Humanised mAb (-zumab) = mouse CDRs + human framework. Fully human (-umab) = all human.
4. Rituximab targets CD20 (B-cell lymphoma); trastuzumab targets HER2 (breast cancer); bevacizumab targets VEGF; adalimumab targets TNF-alpha.
5. Hepatitis B surface antigen vaccine (produced in yeast) was the first approved recombinant subunit vaccine (1986); HPV VLP vaccines are produced in yeast or baculovirus.
6. Sandwich ELISA detects antigen using two antibodies recognising different epitopes; indirect ELISA detects antibody in patient serum.
7. Lateral flow tests use gold or latex nanoparticle labels; require no instrumentation; widely used as rapid diagnostic tests.
8. ADCs (antibody-drug conjugates) combine the targeting of an antibody with the killing power of a cytotoxic drug, reducing systemic toxicity.
