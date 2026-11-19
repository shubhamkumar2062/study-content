# Unit 5: Introduction to drug design — QSAR, pharmacophore modelling, docking and combinatorial chemistry

The last unit leaves the drug classes behind and asks **how new drugs are found and improved**. It is short (7 hours) but scores well, because the answers are definitions, named parameters and labelled diagrams rather than long lists of drugs. Three blocks: **approaches to drug design**, **QSAR with its physicochemical parameters** (including pharmacophore modelling and docking), and **combinatorial chemistry**.

## 5.1 Drug discovery and the approaches to drug design

**Drug design** means planning a molecule to fit a known biological target, instead of testing compounds at random. The older method, **random screening**, tested everything available; it gave penicillin and many natural products but is slow and wasteful.

### The stages from idea to market

```text
Target identification and validation
        ↓
Lead discovery  (screening, natural products, serendipity, "me-too" design)
        ↓
Lead optimisation  (SAR, QSAR, bioisosterism, prodrugs)
        ↓
Preclinical studies (pharmacology, pharmacokinetics, toxicology)
        ↓
Clinical trials: Phase I (safety, healthy volunteers) → Phase II (efficacy, patients)
        → Phase III (large comparative) → regulatory approval → Phase IV (post-marketing)
```

A **lead compound** is a molecule with some useful activity that becomes the starting point for improvement. Leads come from natural products, from an existing drug's side effect (sulphonamides → diuretics and sulphonylureas), from the structure of the natural substrate or receptor ligand, from screening, and from clinical observation.

### Approaches used in drug design

| Approach | What is done | Example |
| --- | --- | --- |
| **Random (empirical) screening** | Test large numbers of compounds in a biological assay | Early antibiotics |
| **Analogue (molecular modification) design** | Change a known drug systematically: homologation, chain branching, ring changes, isosteric replacement | Semi-synthetic penicillins, fluoroquinolones from nalidixic acid |
| **Bioisosteric replacement** | Replace a group by another with similar size, shape or electronic properties | –OH by –NH2, –H by –F, –S– by –CH2–, carboxyl by tetrazole |
| **Mechanism-based (rational) design** | Design from the enzyme's catalytic mechanism; suicide substrates | Clavulanic acid, eflornithine, captopril |
| **Structure-based (direct) design** | Use the X-ray or NMR structure of the target to design a fitting molecule | HIV protease inhibitors, imatinib |
| **Ligand-based (indirect) design** | No target structure known; use the common features of active molecules — QSAR and pharmacophore modelling | Antihistamine and beta-blocker series |
| **Prodrug approach** | Modify delivery rather than potency (Unit 2) | Chloramphenicol palmitate, enalapril |
| **Combinatorial chemistry with high-throughput screening** | Make and test very many compounds quickly | Modern lead finding |
| **Computer-aided drug design (CADD)** | Molecular modelling, docking, virtual screening, pharmacophore searching | Used alongside all of the above |

**Bioisosterism** deserves its own definition: **isosteres** are groups with the same number of atoms and valence electrons (for example O, NH, CH2, S), while **bioisosteres** are groups that can replace one another in a drug and keep broadly similar biological activity. Classical bioisosteres: –F for –H, –OH for –NH2 or –SH, –COOH for tetrazole or sulphonamide, benzene for thiophene or pyridine.

## 5.2 Physicochemical parameters used in QSAR

### The idea of QSAR

**Quantitative structure–activity relationship (QSAR)** expresses biological activity as a **mathematical equation in measurable molecular properties**. If the equation fits, it predicts which analogue to make next, so fewer compounds have to be synthesised.

Biological activity is used as **log (1/C)**, where C is the concentration producing a standard effect (ED50, IC50, MIC). Taking the logarithm makes the relation linear and the more potent drug gives the larger value.

Three kinds of property are used, as **Hansch** set out: **lipophilic (hydrophobic), electronic and steric**.

### Lipophilic (hydrophobic) parameters

**Partition coefficient P** = concentration in octanol ÷ concentration in water at equilibrium. It measures how a drug divides between a fatty phase and water, which governs absorption and the ability to cross membranes. **log P** is used. A **parabolic relation** is common: activity rises with log P up to an optimum (**log P₀**) and then falls, because very lipophilic molecules are trapped in the first membrane they meet and are poorly soluble in body fluids.

**π (pi), the hydrophobic substituent constant:**

```text
   π(X) = log P (of the substituted compound) − log P (of the parent compound)
```

A **positive π** means the substituent is more lipophilic than hydrogen (alkyl groups, Cl, CF3); a **negative π** means it is more hydrophilic (OH, NH2, COOH). π values are additive, so the log P of a new analogue can be estimated before it is made. **clog P** is the same quantity *calculated* from the structure by software rather than measured.

### Electronic parameters

**Hammett's substituent constant σ (sigma)** measures the electron-withdrawing or electron-donating power of a group on an aromatic ring. It is defined from the ionisation of substituted benzoic acids:

```text
   σ = log K(substituted benzoic acid) − log K(benzoic acid)
```

- **σ positive** → electron-withdrawing (NO2, CN, halogens, COOH).
- **σ negative** → electron-donating (CH3, OCH3, NH2, OH).
- Separate values exist for **meta (σm) and para (σp)** positions; ortho substituents are excluded because steric effects interfere.
- The **Hammett equation** is log (k/k₀) = ρσ, where ρ (rho) measures how sensitive the reaction, or the biological response, is to electronic change.

Electronic properties matter because they decide **ionisation, hydrogen bonding and the strength of the drug–receptor interaction**. Other electronic descriptors used are the **dipole moment, pKa, and Hückel or quantum-chemical charges**.

### Steric parameters

- **Taft's steric parameter Es** — measured from the rate of acid hydrolysis of substituted esters. A **more negative Es means a bulkier group** (Es of CH3 is taken as 0).
- **Molar refractivity (MR)** — calculated from the refractive index, molecular weight and density; it measures the **volume plus polarisability** of a group, and is useful when bulk helps rather than hinders binding.
- **Verloop's STERIMOL parameters (L, B1–B5)** — describe the length and widths of a substituent in different directions, so they handle shape better than a single number.
- **Molecular weight, molar volume** and surface area are also used.

### Hansch analysis

Hansch combined the three kinds of parameter into one linear free-energy relationship:

```text
   log (1/C) = −k1(log P)² + k2(log P) + k3σ + k4Es + k5
```

- The **(log P)² term** gives the parabola, so the equation can locate the optimum lipophilicity, log P₀.
- Fitting is done by **multiple linear regression**; the quality is judged by **n** (number of compounds), **r or r²** (correlation), **s** (standard deviation) and **F** (significance). A useful rule of thumb is at least **five compounds per parameter**, or the equation will fit noise.
- **Free–Wilson analysis** is the alternative: it treats the contribution of each substituent at each position as an additive constant, with no physicochemical measurement at all. A **mixed approach** uses both.

**3D-QSAR** methods such as **CoMFA (comparative molecular field analysis)** go further: the molecules are aligned, the steric and electrostatic fields around them are calculated on a grid, and the fields are correlated with activity, producing a contour map showing where bulk or charge helps or hinders.

**Limitations of QSAR:** it works only within a closely related series, needs reliable biological data measured the same way, cannot predict toxicity or metabolism well, and a good correlation does not prove a mechanism.

## 5.3 Pharmacophore modelling and docking

### Pharmacophore

A **pharmacophore** is the **arrangement in space of the molecular features that a molecule must have to be recognised by its target** — not a real molecule, but an abstract pattern. Typical features: a hydrogen bond **donor**, a hydrogen bond **acceptor**, a **positive ionisable** centre, a **negative ionisable** centre, a **hydrophobic** group and an **aromatic ring**, each with its position and the distances between them.

```text
   Pharmacophore of a classical H1 antihistamine (as an illustration)

      aromatic ring  ●        ● aromatic ring
                      ╲      ╱
                       ╲    ╱       distances and angles fixed
                        ●──●
                           │   ~0.5 nm
                      ⊕ protonated tertiary amine (positive ionisable)
```

How a pharmacophore model is built when the target structure is unknown (**ligand-based**): collect active molecules, generate their low-energy **conformers**, **align** them on common features, find the features shared by the actives and absent from the inactives, and test the model by its ability to separate known actives from decoys. If the target structure is known (**structure-based**), the features are read from the interactions seen in the binding site.

Uses: **virtual screening** of large databases (a pharmacophore query retrieves molecules with the right pattern), **scaffold hopping** (finding a new chemical skeleton that presents the same features), and guiding analogue design.

### Molecular docking

**Docking** predicts **how and how well a small molecule (the ligand) fits into the binding site of a macromolecule (usually a protein)**. It needs a three-dimensional structure of the target, from **X-ray crystallography, NMR, cryo-electron microscopy** or **homology modelling**.

Docking has two parts:

1. **The search algorithm**, which generates possible positions, orientations and conformations (poses) of the ligand in the site. Early programs kept the ligand rigid; modern ones allow ligand flexibility and, increasingly, some protein flexibility.
2. **The scoring function**, which estimates how good each pose is. Scores may be **force-field based** (van der Waals and electrostatic energies), **empirical** (a weighted sum of hydrogen bonds, ionic contacts, buried hydrophobic surface and rotatable bonds) or **knowledge-based** (statistics of contacts seen in known structures).

```text
   Protein structure (X-ray / homology model)
            + prepared ligand (3D, correct ionisation, charges)
                     ↓  search algorithm → many poses
                     ↓  scoring function → ranked poses
            best pose + predicted binding energy
                     ↓
      virtual screening, lead optimisation, SAR explanation
```

Two models of fit are worth naming in an answer: **Fischer's lock-and-key** (rigid complementarity) and **Koshland's induced fit** (the site adjusts as the ligand binds) — docking programs are moving from the first towards the second.

**Uses:** virtual screening of libraries, choosing which analogues to make, explaining an observed SAR, and studying selectivity and resistance (for example why a mutated enzyme no longer binds a drug). **Limitations:** scoring functions are approximate, so ranking is less reliable than pose prediction; water molecules and protein flexibility are hard to treat; a docking result is a hypothesis that still needs synthesis and testing.

### Drug-likeness: Lipinski's rule of five

A compound is more likely to be **orally active** if it breaks **none or at most one** of these (all numbers are multiples of five, hence the name):

| Property | Limit |
| --- | --- |
| Molecular weight | not more than 500 |
| log P | not more than 5 |
| Hydrogen bond donors (OH + NH) | not more than 5 |
| Hydrogen bond acceptors (N + O) | not more than 10 |

Veber's additional criteria add **rotatable bonds ≤ 10** and **polar surface area ≤ 140 Å²**. Natural products and actively transported drugs are well-known exceptions. This screen is used in the BP607P practical on drug-likeness.

## 5.4 Combinatorial chemistry

### Concept

**Combinatorial chemistry** is the systematic preparation of a **large number of related compounds (a library)** at the same time by combining sets of building blocks in every possible arrangement, instead of making one compound at a time. Three building blocks of 10 variants each give 10 × 10 × 10 = **1,000 compounds** from 30 starting materials. The library is then tested by **high-throughput screening**.

### Solid-phase synthesis

Developed by **Merrifield** for peptides, this is the backbone of combinatorial chemistry.

```text
   Resin bead ─ linker ─ building block 1
        │ couple block 2, wash
   Resin ─ linker ─ B1 ─ B2
        │ couple block 3, wash
   Resin ─ linker ─ B1 ─ B2 ─ B3
        │ cleave from the linker
   Free product in solution
```

The growing molecule stays attached to an **insoluble polymer bead** (commonly polystyrene cross-linked with divinylbenzene) through a **linker**. After each step the excess reagents and by-products are simply **washed away**, so no chromatography is needed between steps, reactions can be driven to completion with large excesses of reagent, and the whole process is easy to automate.

**Advantages:** fast, automated, easy purification, large excesses possible.
**Disadvantages:** reactions must tolerate the solid support, monitoring the reaction on the bead is harder, the loading per bead is small, and the linker must be cleavable without harming the product.

### Split-and-mix (split-and-pool) method

This is the trick that makes very large libraries possible, with **one compound per bead**:

1. Divide the beads into three portions and couple a different building block to each portion.
2. **Mix all the beads together thoroughly.**
3. **Split them again** into three portions and couple the next set of blocks.
4. Repeat. After *n* steps with *x* blocks each, the library holds **xⁿ** compounds, and every bead carries only one of them.

The problem it creates is **identification** — knowing which compound is on an active bead. Solutions include **tagging** (a chemical or radiofrequency tag added alongside the molecule), **positional encoding** (keeping track of which well a compound came from) and analysis of the single bead by mass spectrometry.

### Parallel (solution-phase) synthesis

Here each compound is made **separately but at the same time**, for example in the 96 wells of a microtitre plate, one known compound per well.

| | Solid phase | Solution phase (parallel) |
| --- | --- | --- |
| Purification | Wash the resin | Normal work-up, often with scavenger resins |
| Library size | Very large (split-and-mix) | Smaller, usually tens to hundreds |
| Identity of each compound | May need tagging | Known from the well position |
| Reaction types | Limited to resin-compatible chemistry | Any solution chemistry |
| Quantity of each compound | Small | Larger, easier to characterise |

**Mixed approach:** a solution-phase reaction with **polymer-supported reagents or scavengers** combines easy purification with free solution chemistry.

### Applications and limits

Combinatorial chemistry is used to **find new leads**, to **optimise a lead** by making focused libraries around it, and in **materials and catalyst discovery**. Modern libraries are smaller but better designed — chosen for **diversity** and for **drug-likeness** (Lipinski's rules) — because the early very large, undesigned libraries gave disappointingly few real leads. The practical consequence for a student is this: combinatorial chemistry increases the *number* of molecules; QSAR, pharmacophore modelling and docking increase the *quality* of the choice. Modern discovery uses them together.

## Remember

- Lead compound, analogue design, bioisosterism, mechanism-based, structure-based and ligand-based design — know one example of each.
- QSAR expresses log (1/C) in terms of lipophilic, electronic and steric parameters.
- π (hydrophobic, from log P), σ (Hammett, electronic, positive = electron-withdrawing), Es (Taft, steric, more negative = bulkier), MR (volume + polarisability), STERIMOL (L, B1–B5).
- Hansch equation is parabolic in log P and gives an optimum log P₀; Free–Wilson is additive; CoMFA is 3D-QSAR.
- A pharmacophore is a 3D arrangement of features (donor, acceptor, ionisable, hydrophobic, aromatic), not a molecule.
- Docking = search algorithm (poses) + scoring function (ranking); needs a 3D target structure; lock-and-key versus induced fit.
- Lipinski's rule of five: MW ≤ 500, log P ≤ 5, donors ≤ 5, acceptors ≤ 10.
- Combinatorial chemistry: solid-phase (Merrifield resin, linker, wash), split-and-mix gives xⁿ compounds with one per bead, parallel synthesis gives one known compound per well.
