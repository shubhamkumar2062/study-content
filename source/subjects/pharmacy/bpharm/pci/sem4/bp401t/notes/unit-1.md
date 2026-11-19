# Unit 1: Stereoisomerism — optical isomerism

Two compounds can have the same molecular formula and the same sequence of bonded atoms and still be different, because their atoms are arranged differently in space. These are **stereoisomers**. Many drugs are chiral, and the two mirror-image forms of a drug can differ in potency, side effects and even in the disease they treat. This unit covers optical isomerism: what optical activity is, how chirality arises, how configurations are named, how chiral molecules react, and how a racemic mixture is separated or avoided by asymmetric synthesis.

## 1.1 Isomerism at a glance

```text
                         ISOMERS (same molecular formula)
                    ┌──────────────┴──────────────┐
           Structural isomers                Stereoisomers
     (different bonding sequence)       (same bonding, different 3-D arrangement)
     chain, position, functional,     ┌──────────────┴──────────────┐
     metamerism, tautomerism      Configurational              Conformational
                                  (bond must break to          (interconvert by rotation
                                   interconvert)                about single bonds)
                            ┌──────────┴──────────┐
                     Optical isomers       Geometrical isomers
                  (enantiomers and           (cis/trans, E/Z) — Unit 2
                   diastereomers)
```

## 1.2 Optical activity

**Plane-polarised light** is light whose vibrations are confined to one plane. It is produced by passing ordinary light through a Nicol prism (calcite) or a polaroid sheet.

**Optical activity** is the property of a substance of rotating the plane of plane-polarised light. It is measured in a **polarimeter**:

```text
 light ──► polariser ──► sample tube ──► analyser ──► eye / detector
 source    (fixed Nicol)   (solution,      (rotated until
 (sodium D line, 589 nm)    length l dm)    light is matched)
```

- **Dextrorotatory**: rotates the plane clockwise (to the right) as seen by the observer; shown as (+) or *d*.
- **Laevorotatory**: rotates anticlockwise (to the left); shown as (−) or *l*.

The observed rotation α depends on the compound, concentration, tube length, temperature, wavelength and solvent. To compare compounds we use **specific rotation**:

```text
          α
[α]  =  ───────        α = observed rotation (degrees)
        l × c          l = tube length in decimetres (dm)
                       c = concentration in g per mL
```

It is written with temperature and wavelength, for example [α] at 25 °C, D line. The pharmacopoeia uses specific rotation as an identity and purity test for many drugs and sugars.

**Worked example.** A solution containing 2 g of a sugar in 50 mL, in a 2 dm tube, shows α = +5.3°. c = 2/50 = 0.04 g/mL, so [α] = 5.3 / (2 × 0.04) = +66.25°.

## 1.3 Chirality and the stereocentre

A molecule is **chiral** if it is not superimposable on its mirror image (like a left and right hand). A chiral molecule is optically active. A molecule that is superimposable on its mirror image is **achiral** and optically inactive.

The commonest cause of chirality is a **stereocentre (chiral centre, asymmetric carbon)**: a carbon atom bonded to four different groups, often marked C*.

Examples of chiral molecules with one stereocentre: lactic acid CH3–C*H(OH)–COOH, glyceraldehyde HOCH2–C*H(OH)–CHO, 2-butanol, alanine.

Note: a stereocentre is the usual cause, but not the only one. Some molecules without a stereocentre are chiral (suitably substituted biphenyls and allenes, Unit 2), and some molecules with stereocentres are achiral (meso compounds).

## 1.4 Elements of symmetry

The true test of chirality is symmetry. A molecule is achiral if it has a plane of symmetry, a centre of symmetry or an alternating axis of symmetry.

| Element | Meaning | Example |
| --- | --- | --- |
| Plane of symmetry (σ) | An imaginary plane that cuts the molecule into two halves that are mirror images of each other | meso-tartaric acid; any CH2X2 molecule |
| Centre of symmetry (i) | A point such that a line drawn from any atom through it meets an identical atom at the same distance on the other side | one stereoisomer of 2,4-dimethylcyclobutane-1,3-dicarboxylic acid |
| Alternating axis of symmetry (Sn) | Rotation by 360°/n followed by reflection in a plane perpendicular to that axis gives the same molecule | some substituted cyclobutanes (S4 axis) |
| Simple axis (Cn) | Rotation by 360°/n gives the same molecule | Does **not** remove chirality; a chiral molecule may have a Cn axis |

Rule to remember: **no σ, no i, no Sn → chiral → optically active.**

## 1.5 Enantiomers, diastereomers and meso compounds

**Enantiomers** are stereoisomers that are non-superimposable mirror images.

- Same melting point, boiling point, solubility, density and refractive index.
- Same chemical reactions with achiral reagents, at the same rate.
- Rotate plane-polarised light by the same amount in opposite directions.
- Differ in reactions with other chiral substances (enzymes, receptors, chiral reagents), so they often differ in biological activity and taste or smell.

**Diastereomers** are stereoisomers that are **not** mirror images. They arise when a molecule has two or more stereocentres (and cis/trans isomers are also diastereomers).

- Different physical properties (melting point, solubility, specific rotation), so they can be separated by crystallisation, distillation or chromatography.
- Different reaction rates even with achiral reagents.

**Number of stereoisomers.** A compound with n different stereocentres can have at most 2^n stereoisomers. If the molecule can be divided into two identical halves, some forms are meso and the number is smaller.

**Meso compounds** have two or more stereocentres but are achiral, because they have an internal plane of symmetry. One half rotates light one way and the other half cancels it (**internal compensation**). A meso compound cannot be resolved.

**Tartaric acid (HOOC–CHOH–CHOH–COOH), two similar stereocentres:**

```text
   COOH          COOH           COOH
   |             |              |
 H-C-OH       HO-C-H          H-C-OH
   |             |              |
 HO-C-H        H-C-OH         H-C-OH     ← plane of symmetry between C2 and C3
   |             |              |
   COOH          COOH           COOH
 (+)-tartaric  (−)-tartaric    meso-tartaric
   └── enantiomers ──┘          (achiral, diastereomer of both)
```

So tartaric acid has only three stereoisomers (not four): (+), (−) and meso. An equimolar mixture of (+) and (−) is the racemic form (racemic acid), inactive by **external compensation**.

**2,3-Dihydroxybutanal or 2-bromo-3-chlorobutane** (two different stereocentres) has the full four stereoisomers: two pairs of enantiomers; any member of one pair is a diastereomer of either member of the other pair. In a Fischer projection, if similar groups on the two neighbouring stereocentres are on the same side, the isomer is called *erythro*; if on opposite sides, *threo* (names taken from the sugars erythrose and threose).

**Epimers** are diastereomers that differ in configuration at only one of several stereocentres (glucose and mannose differ only at C-2).

## 1.6 Representing configurations

**Fischer projection**: the stereocentre is drawn as the crossing point of two lines. Horizontal bonds point towards the viewer; vertical bonds point away. The main carbon chain is written vertically with the most oxidised carbon at the top.

Rules for handling a Fischer projection:

1. Rotating it by 180° in the plane gives the same molecule.
2. Rotating it by 90° gives the enantiomer.
3. Swapping any two groups once gives the enantiomer; swapping twice gives back the same molecule.

Wedge–dash drawings show bonds in front (solid wedge) and behind (dashed wedge) the plane of the paper.

## 1.7 D/L system of nomenclature

The D/L system gives the **relative configuration**, by comparison with glyceraldehyde.

- In the Fischer projection of glyceraldehyde with CHO at the top and CH2OH at the bottom, the form with –OH on the **right** is **D-glyceraldehyde**; –OH on the **left** is **L-glyceraldehyde**.
- **Sugars**: look at the stereocentre farthest from the carbonyl (the lowest one in the Fischer projection). –OH on the right → D-sugar (D-glucose); on the left → L-sugar.
- **Amino acids**: write COOH at the top and the side chain R at the bottom; –NH2 on the left → L-amino acid. Proteins are made of L-amino acids.

Important: D and L describe configuration, while (+) and (−) describe the measured direction of rotation. They are unrelated. D-glucose is dextrorotatory, but D-fructose is laevorotatory.

Limits of D/L: it needs a reference compound related to glyceraldehyde, and it becomes ambiguous for molecules with several stereocentres or groups unlike those of sugars. The R/S system was introduced to describe any stereocentre without reference to another compound.

## 1.8 Sequence rules (Cahn–Ingold–Prelog) and the R/S system

**R/S** gives the **absolute configuration** of each stereocentre.

**Step 1 — rank the four groups by the sequence (priority) rules.**

1. Higher **atomic number** of the atom directly attached to the stereocentre gets higher priority: I > Br > Cl > S > F > O > N > C > H.
2. For isotopes, higher mass number gets higher priority: D > H.
3. If the first atoms are the same, compare the sets of atoms attached to them, one sphere at a time, at the first point of difference. Example: –CH2OH (O,H,H) ranks above –CH(CH3)2 (C,C,H) because O beats C at the first comparison.
4. Double and triple bonds are counted as duplicated or triplicated atoms. –CHO counts as C bonded to (O,O,H); –COOH counts as (O,O,O); –C≡N counts as (N,N,N).

**Step 2 — orient the molecule** so that the lowest-priority group (4) points away from the viewer.

**Step 3 — trace 1 → 2 → 3.** Clockwise = **R** (rectus, right); anticlockwise = **S** (sinister, left).

**Shortcut with a Fischer projection.** If the lowest-priority group is on a vertical bond, read 1 → 2 → 3 directly. If it is on a horizontal bond (pointing at you), read the direction and then reverse it.

**Worked example — D-glyceraldehyde.** Groups: –OH (1), –CHO (2: O,O,H), –CH2OH (3: O,H,H), –H (4). In the D form, H is on a horizontal bond on the left, OH on the right. Going OH → CHO → CH2OH appears anticlockwise; because H is horizontal, reverse it → clockwise → **R**. So D-glyceraldehyde is (R)-glyceraldehyde.

Further examples: L-alanine is (S)-alanine. L-cysteine is (R)-cysteine, because the –CH2SH group outranks –COOH (S has a higher atomic number than O). This shows that D/L and R/S do not translate one-to-one.

**Naming compounds with more than one stereocentre:** give each centre a locant and descriptor, for example (2R,3R)-tartaric acid and (2R,3S)-tartaric acid (meso).

## 1.9 Reactions of chiral molecules

What happens to the configuration depends on whether a bond to the stereocentre is broken.

1. **No bond to the stereocentre is broken → retention of configuration.** The product has the same spatial arrangement, though its sign of rotation and even its R/S label may change because the priorities change. Example: (S)-2-methylbutan-1-ol reacts with HCl at the CH2OH carbon; the stereocentre is untouched, so the chloride keeps the same arrangement.
2. **Bond to the stereocentre broken by an SN2 reaction → inversion (Walden inversion).** The nucleophile attacks from the side opposite the leaving group and the other three groups turn over like an umbrella in the wind. (R)-2-bromobutane with OH− gives (S)-2-butanol.
3. **Bond broken through a planar intermediate (SN1 carbocation, free radical) → racemisation.** The flat intermediate can be attacked from either face, so a nearly 50:50 mixture forms (often with a small excess of inversion in SN1, because the leaving group briefly shields one face).
4. **A new stereocentre created from an achiral starting material with achiral reagents → racemic product.** Free-radical chlorination of butane at C-2 gives (±)-2-chlorobutane; addition of HCN to acetaldehyde gives (±)-lactonitrile.
5. **A second stereocentre created in an already chiral molecule → diastereomers in unequal amounts.** The existing stereocentre makes the two faces unequal. Example: chlorination of (S)-2-chlorobutane at C-3 gives (2S,3S) and meso-(2S,3R)-2,3-dichlorobutane in different amounts.

## 1.10 Racemic modification

A **racemic modification (racemate)** is an equimolar mixture of two enantiomers. It is optically inactive by external compensation and is written (±) or *dl* or *rac*. Laboratory synthesis from achiral materials, without a chiral influence, always gives a racemate.

**Forms of a racemate in the solid state:**

| Form | Description |
| --- | --- |
| Racemic mixture (conglomerate) | Separate crystals of (+) and (−); melting point usually lower than that of the pure enantiomers |
| Racemic compound | Each crystal contains (+) and (−) in equal amounts in a definite lattice; melting point may be higher or lower |
| Pseudoracemate (solid solution) | (+) and (−) mix in any proportion in the crystal; melting point close to the enantiomers |

**Racemisation** is the conversion of one pure enantiomer into the racemate (by heat, acid or base, light). It happens readily when the stereocentre carries an acidic hydrogen next to a carbonyl group (keto–enol tautomerism gives a planar enol). It matters in drug stability: a pure enantiomer can lose potency on storage if it racemises.

**Measures of purity**

```text
Enantiomeric excess (ee) % = ([major] − [minor]) / ([major] + [minor]) × 100
Optical purity %         = observed [α] / [α] of pure enantiomer × 100
```

For a simple mixture the two are equal. A 75:25 mixture has 50% ee.

## 1.11 Resolution of racemic mixtures

**Resolution** is the separation of a racemate into its enantiomers. Enantiomers have identical physical properties, so ordinary distillation or crystallisation cannot separate them. The methods are:

1. **Mechanical separation** — Pasteur (1848) picked out the mirror-image crystals of sodium ammonium tartrate by hand with tweezers under a lens. Possible only when a conglomerate forms well-shaped crystals below a certain temperature; rarely practical.
2. **Biochemical (enzymatic) method** — certain micro-organisms or enzymes use up one enantiomer and leave the other. The mould *Penicillium glaucum* grown on racemic ammonium tartrate consumes the (+) form, leaving the (−) form. Disadvantage: half of the material is lost. Modern **kinetic resolution** uses enzymes such as lipases and esterases that hydrolyse one enantiomer of an ester faster.
3. **Chemical method (via diastereomers)** — the most widely used.
   - React the racemate with a pure enantiomer of a **resolving agent** to form two diastereomers, which differ in solubility.
   - Separate them by fractional crystallisation.
   - Decompose each diastereomer to recover the pure enantiomers and the resolving agent.

```text
 (±)-Acid  +  (−)-Base  ──►  (+)-Acid·(−)-Base   +   (−)-Acid·(−)-Base
 racemate     resolving      └─────── diastereomeric salts ───────┘
              agent                 (different solubility)
                                          │ fractional crystallisation
                                          ▼
                       each salt + dilute HCl → pure (+)-acid and pure (−)-acid
```

   - Resolving agents for racemic **acids**: optically active bases such as brucine, strychnine, quinine, cinchonine and (R)- or (S)-1-phenylethylamine.
   - Resolving agents for racemic **bases**: optically active acids such as (+)-tartaric acid, (−)-malic acid, (+)-camphor-10-sulphonic acid.
   - Racemic **alcohols**: convert to acid esters (for example a half-ester of phthalic acid) and then resolve as acids.
4. **Chromatographic method** — passing the racemate through a column with a **chiral stationary phase** (for example cellulose derivatives, cyclodextrins, or a chiral support); one enantiomer is held more strongly and comes out later. Chiral HPLC is now the standard way of checking enantiomeric purity of drugs.
5. **Preferential crystallisation (seeding)** — a supersaturated solution of a conglomerate is seeded with a crystal of one enantiomer, which then crystallises out first.

## 1.12 Asymmetric synthesis

**Asymmetric synthesis** is a reaction in which an achiral unit of a molecule is converted into a chiral unit so that the two possible stereoisomers are formed in **unequal** amounts. Some chiral influence must be present; otherwise a racemate forms.

**Partial asymmetric synthesis** — the chiral influence is an optically active compound: a chiral starting material, a chiral auxiliary attached temporarily, a chiral reagent, a chiral catalyst or an enzyme.

- Marckwald's classic experiment: the half-ester salt of ethylmethylmalonic acid made with optically active brucine was heated so that it lost CO2; after removal of brucine, 2-methylbutanoic acid was obtained with a small excess of the (−) form.
- McKenzie used an optically active alcohol, (−)-menthol, as an auxiliary: the menthyl ester of a keto acid was reduced (or treated with a Grignard reagent) and then hydrolysed, giving a hydroxy acid with one enantiomer in excess. The chiral menthyl group made one face of the carbonyl more accessible.
- Modern examples: enzymatic reductions with yeast; catalytic asymmetric hydrogenation using rhodium complexes of chiral phosphine ligands (used industrially to make L-dopa for Parkinson's disease).

**Absolute asymmetric synthesis** — no optically active substance is used; the chiral influence is physical, such as **right- or left-circularly polarised light**. When a racemate is photolysed with circularly polarised light, one enantiomer absorbs slightly more and decomposes faster, leaving a small excess of the other. The excess obtained is very small.

## 1.13 Why stereochemistry matters in pharmacy

| Drug | Point to remember |
| --- | --- |
| Thalidomide | Sold as a racemate in the 1950s–60s; serious birth defects. The enantiomers interconvert in the body, so giving one pure form would not have removed the risk |
| Levodopa | Only the L form is used to treat Parkinson's disease |
| Ibuprofen | The (S) form is the active anti-inflammatory; the (R) form is partly converted to (S) in the body |
| Esomeprazole, levocetirizine, escitalopram, levosalbutamol | Single-enantiomer versions of older racemic drugs |
| Adrenaline | The (−) form is far more potent than the (+) form |
| Dextromethorphan | Antitussive; its mirror-image relative levomethorphan is an opioid analgesic — enantiomers can have different actions |

Regulators expect manufacturers to study each enantiomer of a chiral drug and to justify marketing a racemate.

## Remember

- Chiral = not superimposable on its mirror image; test: no plane, centre or alternating axis of symmetry.
- [α] = α/(l × c) with l in dm and c in g/mL; (+) dextro, (−) laevo.
- Enantiomers: identical physical properties except the sign of rotation; diastereomers differ in all physical properties.
- Maximum stereoisomers = 2^n; tartaric acid has only 3 because of the meso form (internal compensation).
- D/L = relative configuration (glyceraldehyde); R/S = absolute configuration by CIP rules; neither tells the sign of rotation.
- CIP: higher atomic number first; multiple bonds duplicated; lowest priority away; clockwise R.
- SN2 → inversion; SN1 / radical → racemisation; no bond to stereocentre broken → retention.
- Racemate: external compensation; resolution mainly through diastereomeric salts (brucine, strychnine, quinine, tartaric acid, camphorsulphonic acid).
- Asymmetric synthesis needs a chiral influence: partial (chiral reagent, auxiliary, catalyst, enzyme) or absolute (circularly polarised light).
