# Unit 4: Targeted drug delivery

Most drugs spread through the whole body after absorption, although they are needed only in one organ or one type of cell. Anticancer drugs are the clearest example: they kill healthy dividing cells as well as tumour cells. **Targeted drug delivery** aims to carry the drug mainly to the place where it is needed. The idea goes back to Paul Ehrlich's "magic bullet": a drug that finds its target and spares everything else.

## 4.1 Concept and definition

**Targeted (site-specific) drug delivery** is the selective delivery of a drug to a particular organ, tissue, cell or intracellular site, in the right amount, while keeping it away from other sites.

A targeted system usually has three parts:

```text
   [ drug ] ── carried by ── [ carrier ] ── guided by ── [ targeting ligand ]
                              liposome,                   antibody, peptide,
                              nanoparticle,               folate, sugar,
                              polymer, cell               transferrin
```

**Ideal targeted system**

1. Reaches the target selectively and stays there.
2. Protects the drug on the way and releases it at the target at a suitable rate.
3. Non-toxic, non-immunogenic, biocompatible and biodegradable.
4. Physically and chemically stable in the body and on storage.
5. Easy to prepare, reproducible and affordable.

## 4.2 Levels of targeting

| Level | Target | Example |
| --- | --- | --- |
| First order | An organ or tissue (capillary bed of a region) | Drug carrier given into the artery of the liver |
| Second order | A particular cell type within the organ | Tumour cells but not normal cells; liver Kupffer cells |
| Third order | An intracellular site in the target cell | Delivery to lysosomes or the nucleus after endocytosis |

## 4.3 Approaches to targeting

### a. Passive targeting

Uses the natural behaviour of the body toward particles, without any special ligand.

1. **Uptake by the reticuloendothelial system (RES) / mononuclear phagocyte system.** Particles above about 100 nm, and particles coated with plasma proteins (opsonised), are taken up by macrophages in the liver and spleen. This is useful for treating infections in macrophages (for example leishmaniasis and fungal infections).
2. **Enhanced permeability and retention (EPR) effect.** Tumour blood vessels are leaky, with large gaps between endothelial cells, and tumours have poor lymphatic drainage. Nanocarriers (roughly 10–200 nm) leak into tumour tissue and stay there, so the drug concentrates in the tumour. Long-circulating ("stealth") carriers coated with polyethylene glycol make use of this effect.

### b. Active targeting

The carrier surface is decorated with a ligand that binds a receptor or antigen found mainly on the target cells.

| Ligand | Target |
| --- | --- |
| Monoclonal antibodies or fragments | Tumour antigens (HER2, CD20, EGFR) |
| Folic acid | Folate receptors over-expressed on many cancer cells |
| Transferrin | Transferrin receptors (tumours, blood–brain barrier) |
| Galactose / asialoglycoproteins | Asialoglycoprotein receptors on liver hepatocytes |
| Mannose | Mannose receptors on macrophages |
| Peptides (RGD) | Integrins on tumour blood vessels |

### c. Physical targeting

An external stimulus releases or concentrates the drug at the site: heat (thermosensitive liposomes), pH-sensitive carriers that release in acidic tumour tissue or endosomes, magnetic microspheres guided by an external magnet, ultrasound and light.

### d. Inverse targeting

The RES is first blocked (for example with a large dose of blank carrier particles), so that a following drug-loaded carrier avoids the liver and spleen and reaches other organs.

### e. Dual and double targeting

- **Dual targeting**: the carrier itself has an effect that adds to the drug's effect (for example an antiviral carrier with an antiviral drug).
- **Double targeting**: spatial targeting (to a site) combined with temporal control (release at a set time).

### f. Other classifications

- **Carrier-based**: liposomes, niosomes, nanoparticles, microspheres, polymer–drug conjugates, resealed erythrocytes, dendrimers.
- **Prodrug approach**: an inactive form activated by enzymes at the site (for example drugs targeted to the colon by bacterial enzymes).
- **Ligand-mediated** and **antibody-mediated** targeting.

## 4.4 Advantages and disadvantages of targeted delivery

**Advantages**

1. Higher drug concentration at the site of action; lower dose needed.
2. Fewer side effects on healthy tissues; better therapeutic index.
3. Protection of drug from degradation in the blood.
4. Prolonged action and less frequent dosing.
5. Possible delivery across barriers (blood–brain barrier) and into cells.
6. Useful for toxic drugs such as anticancer agents and amphotericin B.

**Disadvantages**

1. Rapid removal of carriers by the RES (unless surface-modified).
2. Complex preparation; difficult scale-up; high cost.
3. Stability problems (aggregation, drug leakage).
4. Immune reactions to antibodies or carriers.
5. Limited drug loading in many carriers.
6. Need for skilled handling and specialised evaluation.

## 4.5 Liposomes

**Liposomes** are microscopic vesicles made of one or more concentric phospholipid bilayers enclosing an aqueous core. They were first described by Bangham in the 1960s.

```text
          Unilamellar liposome
             o o o o o o o
          o  ─────────────  o      o = polar head
        o   (aqueous core:   o     ─ = hydrocarbon tails
       o    water-soluble     o
        o    drug)           o     lipid-soluble drug sits inside
          o  ─────────────  o      the bilayer
             o o o o o o o
```

Hydrophilic drugs are carried in the aqueous core; lipophilic drugs in the bilayer.

**Components**

| Component | Role | Examples |
| --- | --- | --- |
| Phospholipids | Form the bilayer | Phosphatidylcholine (lecithin), phosphatidylethanolamine, phosphatidylglycerol, hydrogenated soy PC, dipalmitoyl PC |
| Cholesterol | Stiffens the bilayer, reduces leakage, improves stability | Cholesterol |
| Charge-inducing agents | Prevent aggregation by charge repulsion | Stearylamine (+), dicetyl phosphate (−) |
| PEG-lipids | Steric coating, long circulation ("stealth") | PEG-distearoyl phosphatidylethanolamine |
| Antioxidants | Protect unsaturated lipids | α-tocopherol |

**Classification**

| Basis | Types |
| --- | --- |
| Structure / size | Multilamellar vesicles (MLV, about 0.5–5 µm, many bilayers), small unilamellar vesicles (SUV, about 20–100 nm), large unilamellar vesicles (LUV, above about 100 nm), giant unilamellar vesicles (above about 1 µm), multivesicular vesicles |
| Composition and use | Conventional, long-circulating (PEGylated, stealth), immunoliposomes (antibody on surface), cationic liposomes (gene delivery), pH-sensitive and thermosensitive liposomes |

**Methods of preparation**

1. **Thin-film hydration (Bangham method)**: lipids dissolved in chloroform–methanol; solvent evaporated in a rotary evaporator to leave a thin film; film hydrated with aqueous drug solution with shaking → MLVs. Sonication or extrusion through polycarbonate membranes reduces size to SUVs or uniform LUVs.
2. **Sonication** (probe or bath) of MLVs → SUVs.
3. **French pressure cell**: MLVs forced through a small orifice at high pressure → unilamellar vesicles.
4. **Solvent injection**: lipids in ethanol (ethanol injection) or ether (ether injection) injected into an aqueous phase → vesicles form as the solvent dilutes or evaporates.
5. **Reverse-phase evaporation**: water-in-oil emulsion of drug solution in lipid-containing organic solvent; solvent removed to give a gel which collapses into LUVs with high aqueous entrapment.
6. **Detergent removal**: lipids solubilised in detergent micelles; detergent removed by dialysis or gel filtration → vesicles form.
7. **Freeze-thaw** and **dehydration–rehydration** methods to increase entrapment.

**Evaluation**: vesicle size and size distribution (dynamic light scattering), shape and lamellarity (electron microscopy, NMR), zeta potential, entrapment efficiency (separate free drug by dialysis, gel filtration or centrifugation), drug release, phase transition temperature (differential scanning calorimetry), stability (leakage, aggregation, oxidation of lipids).

**Applications**

1. Cancer therapy: PEGylated liposomal doxorubicin (less cardiotoxicity, uses EPR).
2. Fungal infections: liposomal amphotericin B (less kidney toxicity).
3. Vaccines and adjuvants; gene delivery with cationic liposomes.
4. Topical and cosmetic delivery.
5. Targeting macrophage infections (leishmaniasis) through RES uptake.
6. Ophthalmic and pulmonary delivery.

**Advantages**: biocompatible and biodegradable; carry both water- and fat-soluble drugs; reduce toxicity; protect drug; can be targeted. **Disadvantages**: short shelf life (oxidation and hydrolysis of phospholipids, leakage, fusion), costly lipids, low entrapment of some drugs, rapid RES uptake of conventional liposomes, difficult sterilisation and scale-up.

## 4.6 Niosomes

**Niosomes** are vesicles formed from **non-ionic surfactants** (with cholesterol) in water. Their structure is similar to liposomes: a bilayer enclosing an aqueous core. They were first developed for cosmetics.

**Components**: non-ionic surfactants such as sorbitan esters (Spans), polysorbates (Tweens), polyoxyethylene alkyl ethers (Brij); cholesterol to stabilise the bilayer; a charge inducer (dicetyl phosphate).

**Preparation**: thin-film hydration, ether injection, reverse-phase evaporation, sonication, the "bubble" method, and the proniosome approach (a dry free-flowing powder of surfactant on a carrier such as sorbitol, which forms niosomes on adding water).

| Feature | Liposomes | Niosomes |
| --- | --- | --- |
| Bilayer material | Phospholipids | Non-ionic surfactants |
| Chemical stability | Lower (phospholipids oxidise and hydrolyse) | Higher |
| Cost | High | Lower |
| Storage | Special conditions, often under nitrogen | Easier |
| Purity of raw materials | Natural phospholipids vary | Synthetic surfactants more uniform |
| Use | Approved medicines in several areas | Mainly cosmetics, topical and research use |

**Applications**: topical and transdermal delivery, anticancer and anti-infective delivery under study, ocular delivery, vaccines (as adjuvants), and cosmetics.

## 4.7 Nanoparticles

**Nanoparticles** are solid colloidal particles roughly 10–1000 nm in size (most drug carriers are below about 300 nm), in which drug is dissolved, entrapped, encapsulated or attached.

| Type | Structure |
| --- | --- |
| Nanospheres | Matrix: drug spread through a polymer particle |
| Nanocapsules | Reservoir: oily or aqueous core inside a polymer shell |
| Solid lipid nanoparticles (SLN) | Solid lipid core (glycerides, waxes) stabilised by surfactant |
| Nanostructured lipid carriers (NLC) | Solid lipid mixed with liquid oil; higher loading than SLN |
| Polymeric micelles | Core–shell aggregates of amphiphilic block copolymers |
| Dendrimers | Tree-like, branched synthetic polymers with many surface groups |
| Inorganic | Gold, silica, iron oxide (magnetic) nanoparticles |
| Protein-based | Albumin-bound nanoparticles (paclitaxel albumin-bound) |

**Polymers used**: PLA, PLGA, polycaprolactone, polyalkylcyanoacrylates, chitosan, alginate, gelatin, albumin.

**Methods of preparation**

1. **Emulsion–solvent evaporation**: polymer and drug in organic solvent emulsified in water and solvent evaporated.
2. **Nanoprecipitation (solvent displacement)**: polymer and drug in a water-miscible solvent (acetone) added to water; polymer precipitates as nanoparticles.
3. **Salting-out** and **emulsification–solvent diffusion** methods.
4. **Polymerisation of monomers** (alkylcyanoacrylates) in emulsion.
5. **Ionic gelation**: chitosan cross-linked with tripolyphosphate.
6. **High-pressure homogenisation** (hot or cold) for SLN and NLC.
7. **Supercritical fluid** methods.

**Characterisation**: particle size and polydispersity (dynamic light scattering / photon correlation spectroscopy), zeta potential (surface charge, physical stability), morphology (TEM, SEM, atomic force microscopy), drug loading and entrapment efficiency, in vitro release (dialysis bag), crystallinity (DSC, X-ray diffraction), sterility and stability.

**Advantages**: small size allows passage through capillaries and uptake by cells; EPR targeting of tumours; surface can carry ligands; protection of drug; sustained release; improved solubility and bioavailability of poorly soluble drugs; can be given by many routes.

**Disadvantages**: aggregation; limited drug loading; possible toxicity of some materials; RES uptake; burst release; manufacturing and regulatory complexity.

**Applications**: cancer chemotherapy, delivery across the blood–brain barrier, gene and siRNA delivery, vaccines, ocular and pulmonary delivery, imaging (iron oxide contrast agents) and combined diagnosis–therapy (theranostics).

## 4.8 Monoclonal antibodies

**Antibodies** are Y-shaped immunoglobulin proteins that bind a specific antigen. **Monoclonal antibodies (mAbs)** are identical antibodies produced by a single clone of cells and binding one epitope.

**Hybridoma technique** (Köhler and Milstein, 1975):

```text
Mouse immunised with antigen
   → spleen B cells (make antibody but die in culture)
   + myeloma cells (immortal, make no antibody)
   → fused with polyethylene glycol → hybridoma cells
   → grown in HAT medium (only hybrids survive)
   → screened and cloned (one cell per well)
   → selected clone grown in culture or bioreactor
   → monoclonal antibody harvested and purified
```

**Types by origin (and name endings)**

| Type | Origin | Name ending | Example |
| --- | --- | --- | --- |
| Murine | Fully mouse | -omab | Early diagnostic antibodies |
| Chimeric | Mouse variable region + human constant region | -ximab | Rituximab, infliximab, cetuximab |
| Humanised | Only binding loops from mouse | -zumab | Trastuzumab, bevacizumab |
| Fully human | Human sequences (transgenic mice, phage display) | -umab | Adalimumab |

Mouse proteins trigger human anti-mouse antibody responses, so newer antibodies are humanised or fully human.

**Monoclonal antibodies in drug delivery and targeting**

1. **Naked antibodies**: act by themselves by blocking receptors or recruiting immune cells. Examples: trastuzumab (HER2 breast cancer), rituximab (CD20 on B-cell lymphoma), bevacizumab (VEGF), cetuximab (EGFR).
2. **Antibody–drug conjugates (ADCs)**: a potent cytotoxic drug linked to an antibody, released inside the target cell. Examples: trastuzumab emtansine, brentuximab vedotin.
3. **Radioimmunoconjugates**: antibody carrying a radioactive isotope for imaging or therapy.
4. **Immunoliposomes and antibody-coated nanoparticles**: antibody on the carrier surface guides the whole carrier to the target.
5. **Immunotoxins**: antibody linked to a plant or bacterial toxin.
6. **Diagnostic use**: pregnancy tests, ELISA, imaging of tumours.

**Advantages**: very high specificity; can carry many kinds of payload; long half-life of whole antibodies. **Disadvantages**: large size limits penetration into solid tumours; immunogenicity; antigen may also be present on normal cells; costly production; given only by injection; some patients develop resistance (antigen loss).

## Remember

- Targeting = selective delivery to organ (first order), cell (second order) or intracellular site (third order).
- Passive targeting: RES uptake and the EPR effect of leaky tumour vessels. Active: ligands (antibodies, folate, transferrin, galactose, mannose). Physical: heat, pH, magnet, ultrasound. Inverse: block the RES first.
- Liposomes: phospholipid + cholesterol bilayers; MLV, SUV, LUV; thin-film hydration, sonication, solvent injection, reverse-phase evaporation, detergent removal; stealth PEGylated doxorubicin and liposomal amphotericin B.
- Niosomes: non-ionic surfactant (Span, Tween, Brij) + cholesterol; cheaper and chemically more stable than liposomes; proniosomes.
- Nanoparticles 10–1000 nm: nanospheres, nanocapsules, SLN, NLC, micelles, dendrimers; made by solvent evaporation, nanoprecipitation, ionic gelation, homogenisation; size by DLS, charge by zeta potential.
- mAbs: hybridoma (Köhler and Milstein); -omab murine, -ximab chimeric, -zumab humanised, -umab human; uses as naked antibodies, ADCs, immunoliposomes, radioimmunoconjugates.
