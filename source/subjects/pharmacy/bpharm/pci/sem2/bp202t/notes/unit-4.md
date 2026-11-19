# Unit 4: Carbonyl compounds (aldehydes and ketones)

Aldehydes and ketones share the **carbonyl group, >C=O**. Its polar double bond makes the carbon an electron-poor target for nucleophiles, and it makes the neighbouring α-hydrogens slightly acidic. Almost every named reaction in this unit is built from those two facts. Expect at least one 10-mark mechanism (aldol, Cannizzaro, benzoin or Perkin) every year.

## 4.1 The carbonyl group

```text
        R                 • Carbonyl C is sp2: planar, bond angles about 120°
          \   δ+   δ−     • σ bond + π bond between C and O
            C ═══ O       • O is more electronegative → C=O is polar (δ+ on C, δ− on O)
          /               • Resonance:  >C=O  ⟷  >C⁺–O⁻
        R' (or H)         • Nucleophiles attack C; electrophiles (H⁺) attack O
```

- **Aldehyde:** carbonyl carbon carries at least one H: R–CHO (formaldehyde HCHO, acetaldehyde CH3CHO, benzaldehyde C6H5CHO).
- **Ketone:** carbonyl carbon carries two carbon groups: R–CO–R' (acetone CH3COCH3, acetophenone C6H5COCH3).

**Nomenclature:** aldehydes end in **-al** (methanal, ethanal, 3-methylbutanal; the CHO carbon is C1); ketones end in **-one** (propanone, butan-2-one, pentan-3-one). Common names: formaldehyde, acetaldehyde, propionaldehyde, butyraldehyde; dimethyl ketone (acetone), ethyl methyl ketone.

### Electromeric effect

The **electromeric effect (E)** is the **temporary and complete transfer** of a shared π-electron pair to one of the bonded atoms, **at the demand of an attacking reagent**. It occurs only in multiple bonds (C=C, C=O, C≡N) and disappears as soon as the reagent is removed.

```text
   −E effect (C=O, nucleophile attacking carbon):
        >C=O   + Nu⁻   ──▶   >C⁺–O⁻ (momentarily)  ──▶  Nu–C–O⁻
        π pair moves AWAY from the atom the reagent attacks (towards O)

   +E effect (C=C, electrophile attacking):
        CH2=CH2 + H⁺  ──▶  H–CH2–C⁺H2
        π pair moves TOWARDS the atom the reagent attacks
```

| Inductive effect | Electromeric effect |
| --- | --- |
| Permanent | Temporary, needs a reagent |
| Partial shift of σ electrons | Complete shift of π electrons |
| Found in σ bonds | Found only in multiple bonds |
| Fades along the chain | Acts only between the two atoms of the multiple bond |

When inductive and electromeric effects oppose each other, the electromeric effect usually wins because it is called up by the reagent at the moment of reaction.

### Preparation of aldehydes and ketones (two methods each)

| Product | Method | Reaction |
| --- | --- | --- |
| Aldehyde | Oxidation of 1° alcohol | CH3CH2OH + [O] (K2Cr2O7 / H2SO4) → CH3CHO + H2O; distil the aldehyde out at once so it is not oxidised to acid |
| Aldehyde | Rosenmund reduction | R–COCl + H2 ──Pd / BaSO4 (poisoned)──▶ R–CHO + HCl |
| Aldehyde or ketone | Dehydrogenation over copper (about 300 °C) | 1° alcohol → aldehyde; 2° alcohol → ketone (+ H2) |
| Ketone | Oxidation of 2° alcohol | (CH3)2CHOH + [O] → CH3COCH3 + H2O |
| Ketone | Dry distillation of calcium salts | (CH3COO)2Ca ──heat──▶ CH3COCH3 + CaCO3 (with calcium formate, aldehydes form) |
| Ketone | Hydration of alkynes | CH3C≡CH + H2O ──HgSO4, dil. H2SO4──▶ CH3COCH3 (via the enol) |
| Both | Ozonolysis of alkenes | Unit 2 |

## 4.2 Nucleophilic addition

Because the carbonyl carbon is electron-poor, the typical reaction is **addition of a nucleophile to C and of H (or an electrophile) to O**.

**Base-catalysed mechanism (example: HCN with a little base → cyanohydrin):**

```text
   HCN + OH⁻ → CN⁻ + H2O            (generates the strong nucleophile)

          R                          R                         R
           \                          \                         \
   N≡C⁻  +  C=O   ──slow──▶      N≡C–C–O⁻    ──H–CN──▶    N≡C–C–OH   +  CN⁻
           /                          /                         /
          R'                         R'                        R'
   (Nu⁻ attacks C; sp2 → sp3,     tetrahedral alkoxide      cyanohydrin
    π pair moves onto O)
```

**Acid-catalysed mechanism (weak nucleophiles such as H2O, ROH):** H⁺ first protonates the oxygen, making the carbon even more positive (>C=O⁺H ⟷ >C⁺–OH); then the weak nucleophile adds.

**Reactivity order:** HCHO > CH3CHO > other aldehydes > CH3COCH3 > other ketones > aromatic aldehydes/ketones.

1. **Electronic:** alkyl groups push electrons (+I) and lower the δ+ on carbon; ketones have two.
2. **Steric:** two groups crowd the tetrahedral product more than one group and an H.
3. **Aromatic** carbonyls are stabilised by resonance with the ring, so they react more slowly.

**Important nucleophilic additions**

| Reagent | Product | Use |
| --- | --- | --- |
| HCN (base) | Cyanohydrin R2C(OH)CN | Hydrolysed to α-hydroxy acids (lactic acid from acetaldehyde) |
| NaHSO3 (saturated) | Crystalline bisulfite adduct | Purification and separation of aldehydes and methyl ketones (adduct is decomposed by dilute acid or alkali) |
| Grignard reagent, then H3O⁺ | Alcohols (1° from HCHO, 2° from RCHO, 3° from ketones) | Building carbon chains |
| Alcohol (dry HCl) | Hemiacetal, then acetal | Protecting carbonyl groups; sugar ring structures are cyclic hemiacetals |
| NH2–Z (addition, then loss of water) | >C=N–Z | Crystalline derivatives for identification (table below) |
| Reduction (NaBH4, LiAlH4) | Alcohols | Synthesis |

**Addition–elimination (condensation) with ammonia derivatives:** >C=O + H2N–Z → >C=N–Z + H2O

| H2N–Z | Product |
| --- | --- |
| Hydroxylamine, NH2OH | Oxime |
| Hydrazine, NH2NH2 | Hydrazone |
| Phenylhydrazine, C6H5NHNH2 | Phenylhydrazone |
| 2,4-Dinitrophenylhydrazine (Brady's reagent) | 2,4-DNP hydrazone (yellow to orange-red precipitate) |
| Semicarbazide, NH2NHCONH2 | Semicarbazone |

These products are crystalline solids with sharp melting points, so they identify unknown carbonyl compounds in the practical.

## 4.3 Aldol condensation

Two molecules of an aldehyde (or ketone) with **α-hydrogen** combine in **dilute alkali** to give a **β-hydroxy aldehyde (aldol)** or β-hydroxy ketone, which loses water on heating to give an **α,β-unsaturated carbonyl compound**.

```text
   2 CH3CHO  ──dil. NaOH, cold──▶  CH3–CH(OH)–CH2–CHO  ──heat (–H2O)──▶  CH3–CH=CH–CHO
                                    3-hydroxybutanal (aldol)                but-2-enal
                                                                            (crotonaldehyde)
Mechanism
Step 1  Enolate formation (OH⁻ removes an acidic α-H):
        HO⁻ + H–CH2–CHO  ⇌  H2O + ⁻CH2–CHO  ⟷  CH2=CH–O⁻   (resonance-stabilised enolate)

Step 2  Nucleophilic addition of the enolate to a second molecule:
        ⁻CH2–CHO + CH3–CHO  ──▶  CH3–CH(O⁻)–CH2–CHO

Step 3  Protonation by water:
        CH3–CH(O⁻)–CH2–CHO + H2O  ──▶  CH3–CH(OH)–CH2–CHO + OH⁻   (base regenerated)

Step 4  Dehydration on heating (E1cB through the enolate):
        CH3–CH(OH)–CH2–CHO  ──▶  CH3–CH=CH–CHO + H2O
```

**Why the α-H is acidic:** the carbanion formed is stabilised by resonance with the carbonyl group (negative charge shared with oxygen).

**Ketones:** 2 CH3COCH3 ──Ba(OH)2──▶ (CH3)2C(OH)CH2COCH3 (diacetone alcohol, 4-hydroxy-4-methylpentan-2-one) ──heat, –H2O──▶ mesityl oxide.

**Compounds without α-H** (HCHO, C6H5CHO, (CH3)3C–CHO) cannot form an enolate and do **not** undergo aldol condensation; with concentrated alkali they give the Cannizzaro reaction instead.

### Crossed aldol condensation

Aldol condensation between **two different carbonyl compounds**. If both have α-H, four products form (two self and two crossed), which is of little use. It is useful when **one partner has no α-H** (so it can only be attacked) and the other has α-H (forms the enolate).

```text
Claisen–Schmidt reaction (aromatic aldehyde + aliphatic aldehyde or ketone):
   C6H5–CHO + CH3–CHO  ──dil. NaOH──▶  C6H5–CH=CH–CHO + H2O
   benzaldehyde (no α-H)               cinnamaldehyde (3-phenylprop-2-enal)

   C6H5–CHO + CH3COCH3 ──dil. NaOH──▶ C6H5–CH=CH–COCH3 (benzalacetone)
   (with two moles of benzaldehyde → dibenzalacetone, prepared in the BP305P practical)
```

Dehydration is easy here because the new C=C is conjugated with the benzene ring.

## 4.4 Cannizzaro reaction

Aldehydes **without α-hydrogen**, heated with **concentrated** NaOH or KOH, undergo **disproportionation**: one molecule is oxidised to the acid salt and the other is reduced to the alcohol.

```text
   2 HCHO + NaOH (conc.) ──▶ HCOONa + CH3OH
   2 C6H5CHO + NaOH (conc.) ──▶ C6H5COONa + C6H5CH2OH
                                 sodium benzoate  benzyl alcohol
Mechanism
Step 1  OH⁻ adds to the carbonyl carbon:
        C6H5–CHO + OH⁻  ──▶  C6H5–CH(OH)–O⁻

Step 2  Hydride transfer (slow, key step): the anion pushes its H, with the bond pair,
        onto the carbonyl carbon of a second aldehyde:
        C6H5–C(H)(OH)–O⁻  +  O=CH–C6H5  ──▶  C6H5–COOH  +  ⁻O–CH2–C6H5

Step 3  Proton exchange:
        C6H5–COOH + ⁻OCH2C6H5  ──▶  C6H5–COO⁻ + C6H5CH2OH
```

**Evidence for hydride transfer:** when the reaction is run in D2O, the benzyl alcohol formed has **no C–D bond**; the hydrogen on its carbon came from the other aldehyde molecule, not from the solvent.

**Intramolecular Cannizzaro:** glyoxal, OHC–CHO, with NaOH gives sodium glycollate, HOCH2COONa.

### Crossed Cannizzaro reaction

Two **different** aldehydes without α-H react together. With **formaldehyde** as one partner, formaldehyde is always oxidised (to formate) and the other aldehyde is reduced to the alcohol, because HCHO is the most reactive towards OH⁻ attack.

```text
   C6H5CHO + HCHO + NaOH ──▶ C6H5CH2OH + HCOONa
   (a good laboratory preparation of benzyl alcohol)

   Pentaerythritol: CH3CHO + 3 HCHO (three aldol additions at the α-carbon)
                    → (HOCH2)3C–CHO, then + HCHO + NaOH (crossed Cannizzaro)
                    → C(CH2OH)4 + HCOONa
   Pentaerythritol is nitrated to pentaerythritol tetranitrate (a vasodilator used in angina).
```

## 4.5 Benzoin condensation

Two molecules of an **aromatic aldehyde** combine in the presence of **cyanide ion** (KCN or NaCN in aqueous ethanol, refluxed) to form an **α-hydroxy ketone** (benzoin).

```text
   2 C6H5–CHO  ──KCN, aq. ethanol, reflux──▶  C6H5–CO–CH(OH)–C6H5   benzoin

Mechanism
Step 1  CN⁻ adds to the carbonyl carbon:
        C6H5–CHO + CN⁻  ──▶  C6H5–CH(O⁻)–CN

Step 2  Proton shift from C to O gives a carbanion, stabilised by both –CN and the ring:
        C6H5–CH(O⁻)–CN  ──▶  C6H5–C⁻(OH)–CN

Step 3  The carbanion attacks a second benzaldehyde:
        C6H5–C⁻(OH)–CN + O=CH–C6H5  ──▶  C6H5–C(OH)(CN)–CH(O⁻)–C6H5

Step 4  Proton transfer and loss of CN⁻ (regenerated catalyst):
        ──▶  C6H5–CO–CH(OH)–C6H5 + CN⁻
```

**Why cyanide is special:** it is a good nucleophile, its –C≡N group stabilises the carbanion in step 2 (so the normally electrophilic aldehyde carbon becomes nucleophilic — "polarity reversal"), and it is a good leaving group in step 4.

**Pharmaceutical link:** benzoin is oxidised (HNO3) to **benzil**, C6H5–CO–CO–C6H5; benzil heated with urea in alkali gives the anticonvulsant **phenytoin**.

## 4.6 Perkin condensation (Perkin reaction)

An **aromatic aldehyde** is heated with the **anhydride of an aliphatic acid** (having α-H) and the **sodium or potassium salt of the same acid** to give an **α,β-unsaturated aromatic acid**.

```text
   C6H5–CHO + (CH3CO)2O  ──CH3COONa, about 180 °C, several hours──▶  C6H5–CH=CH–COOH + CH3COOH
   benzaldehyde  acetic anhydride                                    cinnamic acid

Mechanism (outline)
Step 1  Acetate ion (base) removes an α-H from the anhydride:
        CH3CO–O–COCH3 + CH3COO⁻  ──▶  ⁻CH2CO–O–COCH3 + CH3COOH
Step 2  The carbanion adds to the aldehyde carbonyl (aldol-type addition):
        C6H5–CH(O⁻)–CH2–CO–O–COCH3
Step 3  Acetyl transfer to the alkoxide oxygen, then elimination of acetic acid
        gives the unsaturated anhydride C6H5–CH=CH–CO–O–COCH3
Step 4  Hydrolysis on working up with water:
        C6H5–CH=CH–COOH (cinnamic acid) + CH3COOH
```

**Applications:** cinnamic acid and its derivatives; **coumarin** (a fragrance and the parent of anticoagulants such as warfarin) from salicylaldehyde, acetic anhydride and sodium acetate.

## 4.7 Qualitative tests for aldehydes and ketones

| Test | Reagent | Aldehyde | Ketone |
| --- | --- | --- | --- |
| 2,4-DNP (Brady's) | 2,4-Dinitrophenylhydrazine in acid | Yellow/orange precipitate | Yellow/orange precipitate |
| Tollens' (silver mirror) | Ammoniacal AgNO3, warm | Silver mirror or black precipitate (aldehyde oxidised) | No change |
| Fehling's | Fehling A (CuSO4) + Fehling B (Rochelle salt + NaOH), boil | Red Cu2O precipitate (aliphatic aldehydes; benzaldehyde usually negative) | Negative |
| Benedict's | Alkaline copper citrate, boil | Red/orange precipitate (aliphatic aldehydes, reducing sugars) | Negative |
| Schiff's | Rosaniline decolourised by SO2 | Magenta/pink colour returns | No colour (acetone may give a faint slow colour) |
| Sodium nitroprusside | Na2[Fe(CN)5NO] + NaOH | — | Red/wine colour with methyl ketones (acetone) |
| Iodoform | I2 + NaOH, warm | Only acetaldehyde | Methyl ketones (acetone): yellow CHI3 |
| Sodium bisulfite | Saturated NaHSO3 | Crystalline adduct | Methyl ketones form adducts |

## 4.8 Structure and uses of important carbonyl compounds

| Compound | Structure | Preparation | Uses |
| --- | --- | --- | --- |
| Formaldehyde (methanal) | HCHO; used as **formalin**, about 37–40% solution in water with methanol as stabiliser | Methanol vapour + air over heated silver or copper catalyst (oxidation/dehydrogenation) | Disinfectant and fumigant (rooms, operation theatres); preserving biological specimens; making hexamine and resins (Bakelite, urea–formaldehyde). Polymerises to paraformaldehyde on standing |
| Paraldehyde | Cyclic trimer of acetaldehyde, (CH3CHO)3 (2,4,6-trimethyl-1,3,5-trioxane) | Acetaldehyde + a few drops of conc. H2SO4 at room temperature (depolymerises on warming with dilute acid) | Sedative–hypnotic and anticonvulsant (status epilepticus, rectal or injection); strong smell, partly excreted in breath; attacks many plastics, so glass is used |
| Acetone (propanone) | CH3COCH3, volatile, flammable (bp 56 °C) | Dehydrogenation or oxidation of propan-2-ol; co-product of phenol in the cumene process; dry distillation of calcium acetate | Solvent for resins, fats, gums, nail varnish; extraction solvent; raw material for chloroform, iodoform, chlorobutanol. Excess acetone (ketone bodies) in diabetic urine is detected by Rothera's test (nitroprusside, purple ring) |
| Chloral hydrate | CCl3–CH(OH)2 | Chlorination of ethanol gives chloral (CCl3CHO); chloral + water → chloral hydrate | Sedative–hypnotic; chloral is also a raw material for DDT and, with alkali, gives chloroform |
| Hexamine (methenamine, hexamethylenetetramine) | (CH2)6N4, a cage of 6 CH2 and 4 N | 6 HCHO + 4 NH3 → (CH2)6N4 + 6 H2O | Urinary antiseptic: in acidic urine it slowly releases formaldehyde (given as mandelate or hippurate salts); solid fuel tablets; rubber chemicals |
| Benzaldehyde | C6H5CHO, smell of bitter almonds | Hydrolysis of benzal chloride (from toluene + Cl2 in light); Étard reaction (toluene + CrO2Cl2); obtained from amygdalin of bitter almonds | Flavouring; synthesis of cinnamic acid, benzoin, dyes. Oxidises in air to benzoic acid (store well closed) |
| Vanillin | 4-hydroxy-3-methoxybenzaldehyde | From vanilla pods; synthetically from eugenol (clove oil) → isoeugenol → oxidation; from guaiacol; from lignin | Flavouring agent in syrups, tablets and foods; masks bitter tastes. Gives a phenol colour with FeCl3 and a positive aldehyde test |
| Cinnamaldehyde | C6H5–CH=CH–CHO (3-phenylprop-2-enal) | Main part of cinnamon bark oil; Claisen–Schmidt condensation of benzaldehyde with acetaldehyde | Flavouring, carminative, mild antimicrobial; oxidises in air to cinnamic acid |

### Why chloral hydrate is a stable gem-diol

Most compounds with two –OH on one carbon (gem-diols) lose water at once. Chloral hydrate is stable because (1) the strongly electron-withdrawing –CCl3 group (−I) makes the carbonyl carbon so electron-poor that water adds readily and stays, and (2) intramolecular hydrogen bonding between the –OH hydrogens and the chlorine atoms holds the diol together.

```text
          Cl         OH
           \        /
      Cl –– C –– C – H        CCl3–CH(OH)2
           /        \
          Cl         OH
```

### Hexamine structure

```text
   Four N atoms sit at the corners of a tetrahedron; each pair of N atoms is
   bridged by a CH2 group (6 CH2 bridges). Each N is bonded to three CH2 groups.
   (Cage similar in shape to adamantane.)  Formula (CH2)6N4.
```

## Remember

- Carbonyl C is sp2, δ+; nucleophiles attack C. Reactivity HCHO > CH3CHO > acetone; aromatic slowest.
- Electromeric effect: temporary, complete π shift on demand of reagent; −E for C=O with nucleophiles.
- Aldol: needs α-H, dilute alkali → β-hydroxy carbonyl → α,β-unsaturated on heating.
- Crossed aldol works when one partner lacks α-H (Claisen–Schmidt: benzaldehyde + acetaldehyde → cinnamaldehyde).
- Cannizzaro: no α-H, concentrated alkali, hydride transfer; crossed Cannizzaro with HCHO reduces the other aldehyde.
- Benzoin: 2 ArCHO + CN⁻ → ArCOCH(OH)Ar; benzil → phenytoin.
- Perkin: ArCHO + (RCH2CO)2O + RCH2COONa, heat → ArCH=CRCOOH (cinnamic acid).
- Tollens and Fehling and Schiff: aldehydes; nitroprusside and iodoform: methyl ketones; 2,4-DNP: both.
