# Unit 1: Targeted drug delivery — concepts, biological events, tumour targeting and brain-specific delivery

A conventional dosage form distributes the drug all over the body. Only a small fraction reaches the diseased tissue; the rest produces side effects and is wasted. Paul Ehrlich's "magic bullet" idea — a carrier that takes the drug only where it is needed — is the starting point of this subject. At postgraduate level the question is no longer *what* targeting is, but *which biological barriers* stand between an injected carrier and the target cell, and *how* carrier design answers each one.

## 1.1 Definitions and the ideal system

**Targeted (site-specific) drug delivery** is the delivery of a drug selectively to a pre-selected organ, tissue, cell population or intracellular compartment, at a rate and in an amount that gives the wanted effect there, while keeping exposure of other sites as low as possible.

A targeted system has three functional parts:

```text
  [ DRUG ] ── loaded into ── [ CARRIER ] ── decorated with ── [ HOMING DEVICE ]
   cytotoxic,                 liposome,                        antibody, Fab,
   peptide,                   nanoparticle,                    folate, transferrin,
   nucleic acid               micelle, dendrimer,              sugar, peptide (RGD),
                              erythrocyte, microsphere          aptamer
```

**Attributes of an ideal targeted system (frequently asked as a 5-mark question)**

1. Biochemically inert (no pharmacological activity of its own), non-toxic, non-immunogenic.
2. Physically and chemically stable in vivo and on storage.
3. Restricts drug distribution to the target cells or tissue, with a high *targeting index*.
4. Controlled and predictable rate of drug release at the target.
5. Drug released in active form, able to reach its receptor or intracellular site.
6. Minimal drug leakage during transit.
7. Carrier biodegradable or readily eliminated; degradation products harmless.
8. Simple, reproducible, economical and scalable preparation.

**Advantages**: higher concentration at the site, lower total dose, better therapeutic index, protection of labile drugs, fewer and less severe adverse effects, less frequent dosing, and treatment of sites otherwise inaccessible (brain, intracellular pathogens).
**Limitations**: rapid clearance by the mononuclear phagocyte system, low loading of many carriers, physical instability (aggregation, fusion, leakage), immunogenicity of protein ligands, difficult sterilisation and scale-up, high cost, and complex regulatory requirements (each batch must be characterised for size, charge, loading and release).

## 1.2 Levels (orders) of targeting

| Order | Target reached | Example |
| --- | --- | --- |
| Zero / organ level | Capillary bed of an organ after regional administration | Intra-arterial infusion to the liver; intra-articular injection |
| First order | A particular organ or tissue compartment | Liposomes taken up by liver and spleen; nanocarriers accumulating in a tumour |
| Second order | A particular cell type within that organ | Kupffer cells but not hepatocytes; tumour cells but not stroma |
| Third order | An intracellular organelle or compartment | Lysosome, cytosol, mitochondrion, nucleus (needed for gene delivery) |

A useful quantitative measure is the **therapeutic availability** or **targeting index** — the ratio of AUC at the target after the targeted formulation to the AUC at the target after the free drug — together with the **drug targeting efficiency** (fraction of the dose reaching the target) and the **selectivity index** (target AUC divided by non-target AUC).

## 1.3 Biological events and processes involved in drug targeting

This is the heart of Unit 1. A carrier injected intravenously meets a fixed sequence of events; each one is both an obstacle and an opportunity.

### a. Opsonisation and protein corona formation

Within seconds of entering blood, plasma proteins adsorb on the carrier surface and form a **protein corona** (albumin, apolipoproteins, fibrinogen, complement components, immunoglobulins). Specific adsorption of **opsonins** — IgG, complement C3b, fibronectin — marks the particle for phagocytosis. The identity of the corona, not the bare surface, is what cells actually "see".

Factors favouring opsonisation: large size (above about 200 nm), hydrophobic surface, high positive or negative zeta potential, rough surface.
Factors reducing it: hydrophilic steric coating, near-neutral charge, small size.

### b. Uptake by the mononuclear phagocyte system (MPS / RES)

Opsonised carriers are removed by macrophages of the liver (Kupffer cells, the largest sink), spleen (marginal zone and red pulp), bone marrow and lung. Liver uptake is high because the sinusoidal endothelium is **fenestrated** (about 100 nm gaps) and blood flow is slow. The spleen also filters by size through inter-endothelial slits of about 200–250 nm, so particles larger than this are retained mechanically.

**Consequences for design**: MPS uptake is a *problem* when the target is elsewhere, and an *opportunity* when the target is the macrophage itself — leishmaniasis, listeriosis, *Mycobacterium* infections, systemic fungal infections (liposomal amphotericin B) and macrophage-based delivery of antiretrovirals.

### c. Long circulation (stealth) and the steric barrier

Grafting hydrophilic flexible polymer chains — most often **polyethylene glycol (PEG) of 2,000–5,000 Da**, and also poloxamers, polysaccharides and polyglycerols — creates a hydrated cloud that sterically prevents opsonin adsorption. This can extend the circulation half-life of liposomes from minutes to many hours. Points worth stating in an answer:

- Surface PEG density and chain length decide whether the layer is in the "mushroom" or the denser "brush" conformation; the brush gives better protection.
- The **accelerated blood clearance (ABC) phenomenon**: a second dose of PEGylated carrier given a few days after the first is cleared faster because anti-PEG IgM is produced; it is dose- and interval-dependent.
- PEG also hinders uptake by the target cell once the carrier has arrived — the **"PEG dilemma"** — answered by cleavable PEG linkers (pH- or enzyme-sensitive) that shed the coat in the tumour microenvironment.

### d. Extravasation — crossing the endothelium

| Endothelium | Structure | Permeability to carriers |
| --- | --- | --- |
| Continuous (muscle, lung, skin, and with tight junctions in the brain) | No gaps | Essentially closed to nanocarriers |
| Fenestrated (kidney glomerulus, endocrine glands, intestinal villi) | Pores roughly 50–60 nm | Small carriers may pass |
| Discontinuous / sinusoidal (liver, spleen, bone marrow) | Gaps about 100–150 nm, little basement membrane | Open to most nanocarriers |
| Tumour neovasculature | Irregular, wide inter-endothelial gaps, incomplete pericyte cover | Leaky — the basis of EPR |

Carriers can also be carried across intact endothelium by **transcytosis**, either adsorptive (cationic carriers) or receptor-mediated (transferrin, insulin, LDL receptors) — the main route into the brain.

### e. Cellular association, internalisation and intracellular trafficking

Once at the target cell, the carrier may stay on the surface and release drug outside, or be internalised by:

| Pathway | Size limit | Notes |
| --- | --- | --- |
| Phagocytosis | Above about 0.5 µm | Professional phagocytes only |
| Macropinocytosis | Up to about 1 µm | Non-selective fluid uptake |
| Clathrin-mediated endocytosis | About 120 nm | Commonest receptor route; goes to endosome → lysosome |
| Caveolae-mediated endocytosis | About 60–80 nm | Can bypass lysosomes |
| Clathrin- and caveolae-independent routes | About 90 nm | Several mechanisms |

The internalised vesicle matures: early endosome (pH about 6.0–6.5) → late endosome (pH about 5.0–5.5) → lysosome (pH about 4.5–5.0, rich in hydrolases). Two design consequences:

- Acid-labile linkers (hydrazone), pH-sensitive liposomes (DOPE with cholesteryl hemisuccinate) and acid-degradable polymers are used so that release is triggered inside the endosome.
- For drugs that must act in the cytosol (nucleic acids, proteins, some toxins), **endosomal escape** is essential. Mechanisms used: the **proton-sponge effect** of polymers with buffering amines (polyethylenimine, PAMAM dendrimers) causing osmotic swelling and rupture; fusogenic lipids (DOPE); fusogenic peptides (GALA, INF-7); and photochemical internalisation.

### f. Efflux, metabolism and elimination

Even after entry, **P-glycoprotein (MDR1)**, MRPs and BCRP pump many cytotoxic drugs back out — a major cause of multidrug resistance and of failure at the blood–brain barrier. Carriers partly overcome this by delivering the drug inside a vesicle (bypassing the surface pump) or by including an inhibitor such as a poloxamer or d-α-tocopheryl PEG succinate.

Elimination: particles smaller than about 6–8 nm (hydrodynamic diameter) are filtered by the kidney; larger ones are cleared mainly by the liver and spleen; biodegradable polymers are hydrolysed (PLGA → lactic and glycolic acids) and the fragments excreted.

### g. The "size-charge-shape-surface" summary

| Property | Effect |
| --- | --- |
| Size below about 6 nm | Rapid renal clearance |
| Size about 10–200 nm | Longest circulation, best EPR accumulation |
| Size above about 200–300 nm | Splenic filtration and MPS uptake |
| Strong positive charge | Opsonisation, serum aggregation, non-specific cell binding, but better cell uptake |
| Near-neutral, hydrophilic surface | Long circulation |
| Shape: rods/filaments | Longer circulation than spheres of the same volume; poorer phagocytosis |
| Stiffness | Softer particles circulate longer and are phagocytosed less |

## 1.4 Approaches to targeting

**Passive targeting** uses the natural fate of the carrier and the anatomy of the diseased tissue: MPS uptake for liver, spleen and macrophage diseases; the EPR effect for solid tumours and inflamed tissue; capillary blockade by particles above about 7 µm trapped in lung capillaries; and local administration (intratumoural, intra-arterial, intrathecal, intra-articular, ocular, pulmonary).

**Active targeting** adds a ligand that binds a receptor or antigen over-expressed on the target: monoclonal antibodies and fragments (Fab, scFv), folic acid (folate receptor-α on ovarian, endometrial and lung tumours), transferrin (transferrin receptor on dividing cells and brain endothelium), peptides (RGD for αvβ3 integrin on angiogenic vessels), sugars (galactose for the asialoglycoprotein receptor on hepatocytes, mannose for macrophage and dendritic-cell mannose receptors), hyaluronic acid (CD44) and aptamers.

A key point for essays: **active targeting does not usually increase the total amount reaching the tumour** — the carrier must first extravasate passively. What the ligand changes is *retention and internalisation* by the target cell, which is what matters for drugs acting inside the cell.

**Physical / stimulus-responsive targeting**: thermosensitive liposomes releasing at about 41–43 °C with local hyperthermia; pH-sensitive carriers exploiting the acidic (about pH 6.5–6.9) tumour interstitium and the acidic endosome; redox-sensitive disulfide carriers using the high intracellular glutathione; enzyme-sensitive linkers (matrix metalloproteinases, cathepsin B, azoreductase of colonic bacteria); magnetic microspheres and nanoparticles guided by an external magnet; ultrasound- and light-triggered release.

**Inverse targeting**: the MPS is deliberately saturated or suppressed (a pre-dose of blank carrier or of dextran sulfate) so that the next, drug-loaded carrier escapes the liver and spleen.

**Dual targeting** (the carrier itself has therapeutic activity that adds to the drug's), **double targeting** (spatial + temporal control) and **combination targeting** (two ligands on one carrier, for example transferrin plus a peptide for the brain).

**Cell- and prodrug-based approaches**: resealed erythrocytes, macrophage "Trojan horses", stem cells homing to tumours, and site-activated prodrugs such as antibody-directed enzyme prodrug therapy (ADEPT) and gene-directed enzyme prodrug therapy (GDEPT).

## 1.5 Tumour targeting

### a. Pathophysiology that makes targeting possible

1. **Angiogenesis**: tumours above 1–2 mm recruit new vessels driven by VEGF. These vessels are tortuous, dilated, irregularly branched, with gaps between endothelial cells (reported from about 100 nm to 2 µm depending on tumour type) and an incomplete basement membrane and pericyte coverage.
2. **Defective lymphatic drainage**: macromolecules and particles that leak out are not removed, so they are retained.
3. Together these give the **enhanced permeability and retention (EPR) effect** (Matsumura and Maeda, 1986) — the basis of nearly all nanomedicine in oncology. Macromolecules above about 40 kDa and particles of roughly 10–200 nm accumulate selectively; small molecules diffuse back into blood.
4. **Acidic and hypoxic microenvironment**: the Warburg effect gives extracellular pH about 6.5–7.0, and hypoxia drives HIF-1α, P-glycoprotein expression and resistance to radiotherapy.
5. **Raised interstitial fluid pressure** from leaky vessels and absent lymphatics opposes convective transport into the tumour centre — one of the main reasons EPR often fails in practice.
6. **Dense stroma** (collagen, hyaluronan, cancer-associated fibroblasts) limits penetration beyond a few cell layers from the vessel.

**Limitations of EPR**, which a postgraduate answer must mention: EPR is highly variable between tumour types, between patients and even between regions of the same tumour; it is far more consistent in rodent xenografts than in human disease; large necrotic and poorly perfused areas receive nothing. Strategies to improve it include vascular normalisation with low-dose anti-angiogenic therapy, stromal depletion (hyaluronidase, collagenase), local hyperthermia, and size-shrinking multistage carriers.

### b. Molecular targets on tumour cells

| Target | Over-expressed in | Ligand used |
| --- | --- | --- |
| HER2 | Breast, gastric carcinoma | Trastuzumab, affibody |
| EGFR | Colorectal, head and neck, lung | Cetuximab, panitumumab, GE11 peptide |
| Folate receptor-α | Ovarian, endometrial, lung | Folic acid |
| Transferrin receptor (CD71) | Most proliferating tumours | Transferrin, antibody |
| CD20, CD19, CD22, CD30, CD33 | Haematological malignancies | Rituximab, brentuximab, gemtuzumab |
| αvβ3 integrin | Tumour neovasculature | RGD peptides |
| CD44 | Cancer stem cells, many solid tumours | Hyaluronic acid |
| PSMA | Prostate carcinoma | Small-molecule inhibitors, aptamers |
| VEGF / VEGFR | Tumour vasculature | Bevacizumab, ramucirumab |

### c. Approaches in practice

- **Nanocarrier chemotherapy**: PEGylated liposomal doxorubicin (reduced cardiotoxicity; dose-limiting hand–foot syndrome instead), non-PEGylated liposomal doxorubicin, liposomal daunorubicin, liposomal irinotecan, liposomal cytarabine–daunorubicin fixed ratio, and albumin-bound paclitaxel (uses albumin transport rather than EPR alone).
- **Polymer–drug conjugates** (Ringsdorf model: polymer backbone + solubiliser + cleavable spacer + drug + homing group); HPMA copolymer conjugates were the classic examples studied.
- **Antibody–drug conjugates**: trastuzumab emtansine, brentuximab vedotin, gemtuzumab ozogamicin — potent payload, cleavable or non-cleavable linker, defined drug-to-antibody ratio.
- **Vascular (neovascular) targeting**: RGD- or NGR-decorated carriers destroy the supply rather than the tumour cell; the endothelium is genetically stable, so resistance is less likely.
- **Tumour-activated prodrugs and ADEPT/GDEPT**; hypoxia-activated prodrugs.
- **Magnetic and thermosensitive systems** combined with external hyperthermia.
- **Theranostics**: one carrier for imaging and therapy (iron oxide, radiolabelled carriers).

## 1.6 Brain-specific delivery

### a. The blood–brain barrier (BBB)

The BBB is formed by brain capillary endothelial cells with **continuous tight junctions** (claudin-5, occludin, ZO-1), **no fenestrations**, very few pinocytotic vesicles, a continuous basement membrane, and surrounding pericytes and astrocyte end-feet (the neurovascular unit). It also has a strong **metabolic barrier** (monoamine oxidase, cytochrome P450, peptidases) and **efflux transporters** (P-glycoprotein, BCRP, MRPs) at the luminal membrane. The blood–cerebrospinal fluid barrier at the choroid plexus is a second, separate barrier.

**Rule of thumb for passive entry**: molecular weight below about 400–500 Da, high lipophilicity (log P about 2), fewer than 8–10 hydrogen bonds, low or no ionisation at pH 7.4, and low plasma protein binding. Nearly all large-molecule drugs and more than 98% of small molecules fail these conditions.

### b. Physiological transport routes used for delivery

| Route | Carried normally | Exploited by |
| --- | --- | --- |
| Passive lipid diffusion | Small lipophilic molecules | Lipidisation, prodrugs |
| Carrier-mediated transport | Glucose (GLUT1), large neutral amino acids (LAT1), choline, nucleosides | Levodopa (LAT1), glucose- and amino-acid-conjugated carriers |
| Receptor-mediated transcytosis | Transferrin, insulin, LDL, leptin | Transferrin or anti-transferrin-receptor antibody, insulin-receptor antibody, apolipoprotein E coating, angiopep-2 (LRP1) |
| Adsorptive-mediated transcytosis | Cationic plasma proteins, lectins | Cationic albumin, TAT and other cell-penetrating peptides, cationic liposomes |
| Cell-mediated | Monocytes, macrophages crossing into inflamed brain | "Trojan horse" cell carriers |

### c. Strategies, grouped the way examiners like

**1. Modifying the drug (chemical approaches)**
- Lipidisation and prodrugs: masking polar groups by esterification or amidation raises log P and brain uptake, and the parent drug is regenerated by esterases in the brain.
- Chemical delivery systems (Bodor's dihydropyridine ⇌ pyridinium redox system: the lipophilic dihydro form enters, is oxidised in the brain and the charged form is locked in).
- Peptide modification: cyclisation, halogenation, N-methylation, D-amino acids to resist peptidases.
- Carrier-substrate conjugates designed as substrates of LAT1 or GLUT1.

**2. Modifying the barrier (invasive and semi-invasive)**
- Osmotic opening with intracarotid mannitol; bradykinin analogues acting on B2 receptors; focused ultrasound with microbubbles, which opens tight junctions transiently and is the most actively studied modern method.
- Direct routes: intracerebroventricular and intrathecal infusion, convection-enhanced delivery, implants placed in the resection cavity (carmustine wafers), and intracerebral injection.

**3. Using carriers (the pharmaceutics answer)**
- **Polysorbate 80-coated poly(butyl cyanoacrylate) nanoparticles**: adsorb apolipoprotein E and B, mimic LDL and enter through LDL receptors; the classic proof-of-concept with dalargin and with doxorubicin.
- **Solid lipid nanoparticles and nanostructured lipid carriers**: lipid matrix, good tolerability, possible lymphatic and transcytotic transport.
- **Liposomes and immunoliposomes** bearing transferrin, anti-transferrin-receptor antibody, insulin-receptor antibody or angiopep-2 ("molecular Trojan horses").
- **Polymeric micelles and dendrimers** with surface ligands.
- **Exosomes** and other cell-derived vesicles.
- **P-glycoprotein inhibition** by excipients (poloxamer 188, TPGS) included in the carrier.

**4. Bypassing the barrier — the nose-to-brain route**
Drug deposited on the olfactory and respiratory mucosa can reach the brain along the olfactory and trigeminal nerve pathways (intracellular axonal transport and extracellular perineural transport), avoiding first-pass metabolism and the BBB. Limitations are the small olfactory area in humans (about 3–10 cm² of a roughly 150 cm² nasal cavity), mucociliary clearance (about 15–20 min), enzymatic activity and small volume (about 25–200 µL per nostril). Mucoadhesive gels, in-situ gelling systems, nanoemulsions and chitosan nanoparticles are used to increase residence time. This is taken further in Unit 4.

### d. Evaluating brain targeting

In-vitro BBB models (primary or immortalised brain endothelial cells, co-culture with astrocytes and pericytes, transendothelial electrical resistance, permeability coefficient); in-situ brain perfusion; in-vivo brain uptake index, brain-to-plasma AUC ratio, drug targeting efficiency and **drug targeting index**; microdialysis for free drug in brain interstitial fluid; and imaging (PET, SPECT, fluorescence, MRI with iron oxide labels).

## Remember

- Targeting orders: organ (first) → cell type (second) → intracellular compartment (third).
- The biological sequence to recite: protein corona and opsonisation → MPS capture in liver/spleen → steric stabilisation (PEG, ABC phenomenon, PEG dilemma) → extravasation (continuous, fenestrated, sinusoidal, tumour vessels) → ligand binding → endocytosis (clathrin about 120 nm, caveolae about 60–80 nm) → endosomal acidification → escape or lysosomal degradation → efflux and elimination.
- Size 10–200 nm, neutral hydrophilic surface: longest circulation. Above about 200 nm: spleen and liver. Below about 6–8 nm: kidney.
- EPR = leaky angiogenic vessels + no lymphatic drainage; limited in humans by heterogeneity, high interstitial fluid pressure and dense stroma.
- Tumour targeting: passive (EPR), active (HER2, EGFR, folate, transferrin, RGD, CD44), vascular, stimulus-responsive, prodrug (ADEPT/GDEPT) and theranostic approaches.
- BBB: tight junctions, no fenestrae, efflux pumps, metabolic barrier. Entry needs < 400–500 Da and good lipophilicity, or a transport route: carrier-mediated (LAT1, GLUT1), receptor-mediated (transferrin, insulin, LRP1/angiopep-2, apolipoprotein E after polysorbate 80 coating), adsorptive (cationic, TAT), or bypass by the nose-to-brain route.
