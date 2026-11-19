# Unit 5: Reactions of synthetic importance

This unit covers the named reactions that are used again and again in making drugs: four reductions (metal hydride, Clemmensen, Wolff–Kishner, Birch), two oxidations (Oppenauer, Dakin), two rearrangements (Beckmann, Schmidt) and one condensation (Claisen–Schmidt). For each one the examiner expects: **definition (reactant → product), reagents and conditions, mechanism, examples, and applications or limitations**. Learn them in that order.

## 5.1 Overview

| Reaction | Converts | Key reagent |
| --- | --- | --- |
| Metal hydride reduction | C=O compounds → alcohols (LiAlH4 also: acids/esters → alcohols, amides/nitriles → amines) | LiAlH4 or NaBH4 |
| Clemmensen reduction | C=O → CH2 (acid conditions) | Zn–Hg + conc. HCl |
| Wolff–Kishner reduction | C=O → CH2 (basic conditions) | NH2NH2, KOH, heat |
| Birch reduction | Benzene ring → 1,4-cyclohexadiene | Na or Li in liquid NH3 + alcohol |
| Oppenauer oxidation | Secondary alcohol → ketone | Al(O-t-Bu)3 or Al(O-i-Pr)3 + acetone |
| Dakin reaction | o- or p-Hydroxy aryl aldehyde/ketone → dihydric phenol | Alkaline H2O2 |
| Beckmann rearrangement | Ketoxime → N-substituted amide | Acid: conc. H2SO4, PCl5, PPA |
| Schmidt reaction / rearrangement | Acid → amine (one C less); ketone → amide | HN3 + conc. H2SO4 |
| Claisen–Schmidt condensation | Aromatic aldehyde + ketone/aldehyde → α,β-unsaturated carbonyl | Dilute NaOH |

## 5.2 Metal hydride reduction (LiAlH4 and NaBH4)

**Principle.** Complex metal hydrides act as a source of **hydride ion (H⁻)**. Hydride, a nucleophile, attacks the electron-poor carbon of a polar multiple bond (C=O, C≡N). The metal–oxygen product is then hydrolysed during work-up to release the alcohol (or amine).

**Mechanism (ketone with NaBH4):**

```text
            δ+  δ−
  R2C = O   +   H–BH3⁻   ──►   R2CH–O⁻ (borate ester)   ──H2O / H+──►   R2CH–OH
            hydride adds to carbon, oxygen bonds to boron
  Each BH4⁻ (or AlH4⁻) can deliver all four hydrogens,
  so 1 mol of reagent can reduce up to 4 mol of ketone.
```

### Lithium aluminium hydride (LiAlH4)

- Very powerful, unselective reducing agent.
- Reacts violently with water and alcohols (liberating H2), so it is used in **dry ether or dry THF**, followed by careful aqueous or acid work-up.
- Reduces almost all polar groups:

| Starting group | Product |
| --- | --- |
| Aldehyde | Primary alcohol |
| Ketone | Secondary alcohol |
| Carboxylic acid | Primary alcohol |
| Ester | Two alcohols (RCOOR' → RCH2OH + R'OH) |
| Acid chloride, anhydride | Primary alcohol |
| Amide | Amine (RCONH2 → RCH2NH2) |
| Nitrile | Primary amine (RCN → RCH2NH2) |
| Epoxide | Alcohol (hydride attacks the less hindered carbon) |
| Alkyl halide | Alkane |
| Nitro (aliphatic) | Amine |

- Usually does **not** reduce an isolated C=C double bond.

### Sodium borohydride (NaBH4)

- **Mild, selective** reducing agent.
- Stable in water, methanol and ethanol, so it can be used in these solvents; safer to handle.
- Reduces **aldehydes and ketones** (and acid chlorides) to alcohols.
- Normally **does not reduce** carboxylic acids, esters, amides, nitriles, nitro groups or isolated C=C.
- So it can reduce a ketone in a molecule that also contains an ester: ethyl acetoacetate → ethyl 3-hydroxybutanoate.

### Comparison

| Point | LiAlH4 | NaBH4 |
| --- | --- | --- |
| Reducing power | Strong | Mild |
| Solvent | Dry ether, THF only | Water, methanol, ethanol |
| With water | Reacts violently | Stable (slowly decomposes in acid) |
| Aldehydes, ketones | Reduced | Reduced |
| Acids, esters, amides, nitriles | Reduced | Not reduced (normally) |
| Selectivity | Low | High |
| Safety | Fire hazard | Relatively safe |

**Applications**: reduction of carbonyl intermediates in steroid and drug synthesis; LiAlH4 converts amides to amines (making secondary and tertiary amine drugs); NaBH4 is used for selective reductions, for example of a ketone in the presence of an ester, and to reduce sugars to sugar alcohols in the laboratory. Attack usually occurs from the less hindered face of a cyclic ketone, giving useful stereoselectivity.

## 5.3 Clemmensen reduction

**Reaction.** The C=O group of an aldehyde or ketone is reduced to a CH2 group by heating with **zinc amalgam (Zn–Hg) and concentrated hydrochloric acid**.

```text
  R–CO–R'   ──Zn(Hg), conc. HCl, reflux──►   R–CH2–R'

  C6H5–CO–CH3        → C6H5–CH2–CH3        (acetophenone → ethylbenzene)
  C6H5–CO–CH2CH3     → C6H5–CH2CH2CH3      (propiophenone → n-propylbenzene)
```

**Mechanism.** Not fully settled. The reaction occurs on the zinc surface: electrons pass from zinc to the protonated carbonyl, giving zinc-bound intermediates (organozinc/zinc carbenoid species), which are protonated stepwise until the CH2 compound is released. The corresponding alcohol is **not** an intermediate — alcohols are not reduced to alkanes under these conditions.

**Applications**

- Preparing **straight-chain alkylbenzenes**: Friedel–Crafts **acylation** followed by Clemmensen reduction avoids the carbocation rearrangement and polysubstitution of direct Friedel–Crafts alkylation (n-propylbenzene cannot be made cleanly by direct alkylation with n-propyl chloride, which gives mainly isopropylbenzene).
- Reducing aryl ketones, keto acids (with acids stable to HCl).

**Limitations**

- Not suitable for compounds that are sensitive to strong acid (acetals, some alcohols that dehydrate, acid-sensitive heterocycles such as furan and pyrrole).
- Poor for high molecular weight, poorly soluble ketones.
- α,β-Unsaturated ketones may also have the C=C reduced; some compounds rearrange.
- For acid-sensitive compounds, use the Wolff–Kishner reduction instead.

## 5.4 Wolff–Kishner reduction

**Reaction.** An aldehyde or ketone is converted into its **hydrazone**, which is heated with a strong base (KOH or sodium ethoxide) at about 180–200 °C; nitrogen gas is lost and the C=O becomes CH2.

```text
  R2C=O + H2N–NH2 ──(−H2O)──► R2C=N–NH2 (hydrazone) ──KOH, heat──► R2CH2 + N2↑

  Huang-Minlon modification (one pot, used today):
  ketone + hydrazine hydrate + KOH in diethylene glycol (bp about 245 °C);
  water and excess hydrazine are distilled off so the mixture reaches about 200 °C;
  gives high yields in a few hours at normal pressure (the original method used
  sodium ethoxide in a sealed tube).
```

**Mechanism**

```text
1. Hydrazone formation:    R2C=O + NH2NH2 → R2C=N–NH2 + H2O
2. Base removes an N–H proton:          R2C=N–NH⁻  ↔  R2C⁻–N=NH
3. Carbon is protonated by solvent:     R2CH–N=NH  (diimide-type intermediate)
4. Base removes the second N–H proton:  R2CH–N=N⁻
5. N2 is lost (driving force: very stable N2 gas) → carbanion R2CH⁻
6. Carbanion takes a proton from solvent → R2CH2
```

**Applications and comparison with Clemmensen**

| Point | Clemmensen | Wolff–Kishner |
| --- | --- | --- |
| Medium | Strongly acidic (conc. HCl) | Strongly basic (KOH), high temperature |
| Reagents | Zn–Hg, HCl | NH2NH2, KOH, ethylene/diethylene glycol |
| Suitable for | Acid-stable, base-sensitive compounds | Base-stable, acid-sensitive compounds (furans, pyrroles, acetals) |
| Not suitable for | Acid-sensitive groups | Base-sensitive groups (esters hydrolyse, halides eliminate); very hindered ketones form hydrazones slowly |
| By-products | — | N2 gas, water |

Both reduce C=O fully to CH2; together they cover nearly every substrate. Wolff–Kishner is also used for keto groups in steroids and on heterocyclic rings.

## 5.5 Birch reduction

**Reaction.** An aromatic ring is reduced to a **non-conjugated 1,4-cyclohexadiene** by an alkali metal (sodium, lithium or potassium) dissolved in **liquid ammonia**, in the presence of an alcohol (ethanol or tert-butanol) as proton source.

```text
  benzene  ──Na, liquid NH3 (−33 °C), EtOH──►  cyclohexa-1,4-diene
  (the ring is NOT fully reduced; the two remaining C=C are opposite each other)
```

**Mechanism (stepwise electron and proton addition):**

```text
1. Na → Na+ + e⁻(solvated)           blue solution of solvated electrons in NH3
2. Ring + e⁻  → radical anion
3. Radical anion + ROH → cyclohexadienyl radical + RO⁻   (protonation)
4. Radical + e⁻ → cyclohexadienyl anion
5. Anion + ROH → 1,4-cyclohexadiene + RO⁻
   (protonation at the centre of the anion gives the 1,4-diene, not the
    conjugated 1,3-diene)
```

**Effect of substituents (regioselectivity)**

| Substituent | Type | Where it ends up | Example |
| --- | --- | --- | --- |
| –OCH3, –CH3, –NR2 | Electron-donating | On a **double-bond** carbon | Anisole → 1-methoxycyclohexa-1,4-diene |
| –COOH, –CONH2, –COR | Electron-withdrawing | On an **sp3** (saturated) carbon | Benzoic acid → cyclohexa-2,5-diene-1-carboxylic acid |

The methoxy-diene from anisole is an enol ether; mild acid hydrolysis gives **cyclohex-3-enone**, and stronger acid gives the conjugated **cyclohex-2-enone**. This is an excellent way of turning a phenol ether into a cyclic enone.

**Applications**

- Synthesis of **19-nor steroids** (oral contraceptive progestins such as norethisterone): the aromatic A-ring of estradiol 3-methyl ether is Birch reduced and hydrolysed to the 19-nor-Δ4-3-ketone.
- Preparation of cyclohexenones and dihydro aromatic compounds.
- Related dissolving-metal reductions: alkynes → **trans**-alkenes (Na/NH3).

**Precautions**: liquid ammonia is very cold and its vapour irritant; alkali metals react violently with water. Reaction is run in a fume hood with dry apparatus.

## 5.6 Oppenauer oxidation

**Reaction.** A **secondary alcohol** is oxidised to a **ketone** by heating with **aluminium tert-butoxide** (or aluminium isopropoxide) in the presence of a large excess of a hydride acceptor, usually **acetone** (or cyclohexanone), in benzene or toluene. It is the reverse of the **Meerwein–Ponndorf–Verley (MPV) reduction**.

```text
  R2CH–OH  +  (CH3)2C=O   ⇌   R2C=O  +  (CH3)2CH–OH
  sec-alcohol   acetone        ketone    isopropanol
                (excess drives equilibrium to the right)
```

**Mechanism**

```text
1. The alcohol exchanges with an alkoxide on aluminium → R2CH–O–Al(OR)2
2. Acetone coordinates to the same aluminium (Lewis acid)
3. Six-membered cyclic transition state:
          H
   R2C ···· C(CH3)2          the hydride on the carbinol carbon moves
    |        |               directly to the carbonyl carbon of acetone
    O ─ Al ─ O
4. Products: ketone R2C=O released; acetone becomes isopropoxide on Al
```

**Advantages**

- Very **mild and selective**: only the alcohol is oxidised; C=C double bonds, aldehyde-sensitive groups and other oxidisable groups (sulphides, amines) are untouched.
- **No over-oxidation** to acids.

**Applications — especially in steroid chemistry**

- Cholesterol → cholest-4-en-3-one (the C-3 alcohol is oxidised and the 5,6-double bond moves into conjugation with the new ketone).
- **Pregnenolone → progesterone**.
- Similar conversions in making testosterone and other 3-keto-Δ4 steroid hormones.

**Limitations**: works best with secondary alcohols; primary alcohols give aldehydes that undergo aldol condensation in the basic medium; the reaction is reversible, so a large excess of acetone is needed.

## 5.7 Dakin reaction (Dakin oxidation)

**Reaction.** An aromatic aldehyde (or ketone) carrying an **–OH (or –NH2) group in the ortho or para position** is oxidised by **alkaline hydrogen peroxide** to a phenol: the –CHO group is replaced by –OH, and formate is released.

```text
  salicylaldehyde (o-hydroxybenzaldehyde)  ──H2O2, NaOH──►  catechol + HCOO⁻
  p-hydroxybenzaldehyde                    ──H2O2, NaOH──►  hydroquinone + HCOO⁻
  o-hydroxyacetophenone                    ──H2O2, NaOH──►  catechol + CH3COO⁻
```

**Mechanism** (similar to the Baeyer–Villiger oxidation):

```text
1. HO–O⁻ (hydroperoxide anion, from H2O2 + NaOH) adds to the carbonyl carbon
   → tetrahedral intermediate  Ar–CH(O⁻)–O–OH
2. The aryl group migrates from carbon to the neighbouring oxygen while
   OH⁻ leaves (the O–O bond breaks). The o/p –OH (as –O⁻) pushes electrons
   into the ring and makes the aryl group a good migrating group.
   → aryl formate ester  Ar–O–CHO
3. The ester is hydrolysed by the alkali → phenoxide (→ phenol) + formate
```

**Why the o- or p-OH is needed**: without an electron-donating group, aryl migration is slow and the aldehyde is simply oxidised to the carboxylic acid instead.

**Applications**

- Preparation of **catechol** and **hydroquinone** and substituted dihydric phenols (useful in making catechol-type drugs and antioxidants).
- Converting aryl aldehydes and ketones to phenols in natural-product synthesis.

## 5.8 Beckmann rearrangement

**Reaction.** A **ketoxime** rearranges to an **N-substituted amide** under acidic conditions: **conc. H2SO4, PCl5, polyphosphoric acid, SOCl2, or Beckmann's mixture** (acetic acid + acetic anhydride + dry HCl). The group **anti** (trans) to the –OH migrates from carbon to nitrogen — the reaction is **stereospecific**.

```text
          R               OH   (R is anti to OH)
            \           /
             C ═ N              ──acid──►     R'–CO–NH–R
            /                                 N-substituted amide
          R'

  acetophenone oxime (phenyl anti to OH) → acetanilide (CH3CONHC6H5)
  benzophenone oxime                     → benzanilide (C6H5CONHC6H5)
  cyclohexanone oxime                    → ε-caprolactam (7-membered lactam)
```

**Mechanism**

```text
1. The acid protonates (or PCl5 converts) the oxime –OH into a good leaving group (–OH2⁺).
2. Water leaves and, AT THE SAME TIME, the group anti to it moves from C to N
   (concerted: migration and departure happen together, so only the anti group migrates)
   → nitrilium ion  R'–C≡N⁺–R
3. Water attacks the carbon of the nitrilium ion → imidic acid R'–C(OH)=N–R (after loss of H+)
4. Tautomerisation (imidic acid → amide)      → R'–CO–NH–R
```

The migrating group keeps its configuration if it is chiral.

**Applications**

1. **Determining the configuration of ketoximes**: identifying the amide shows which group was anti to the OH (Unit 2).
2. **Industrial ε-caprolactam** from cyclohexanone oxime → polymerised to **nylon-6**.
3. **Paracetamol synthesis** — the oxime of 4-hydroxyacetophenone undergoes Beckmann rearrangement to give N-(4-hydroxyphenyl)acetamide (paracetamol).
4. Making amides and, after hydrolysis, amines and acids; identifying ketones.
5. Ring expansion of cyclic ketones to lactams (seven-membered azepinones, linking to Unit 4).

**Aldoximes** under these conditions usually lose water to give **nitriles** rather than amides.

## 5.9 Schmidt reaction (Schmidt rearrangement)

**Reaction.** Carbonyl compounds react with **hydrazoic acid (HN3)** in the presence of **conc. H2SO4**; nitrogen is lost and a group migrates from carbon to nitrogen.

| Substrate | Product |
| --- | --- |
| Carboxylic acid R–COOH | Primary amine R–NH2 (one carbon fewer) + CO2 + N2 |
| Ketone R–CO–R' | Amide R–CO–NH–R' (as in Beckmann) |
| Aldehyde R–CHO | Nitrile R–CN (and some formamide) |

```text
  C6H5COOH + HN3 ──conc. H2SO4──► C6H5NH2 + CO2 + N2     (benzoic acid → aniline)
  cyclohexanone + HN3 ──H2SO4──► ε-caprolactam + N2
```

**Mechanism (carboxylic acid)**

```text
1. In conc. H2SO4 the acid forms an acylium ion R–C≡O⁺ (loss of water)
2. HN3 adds → protonated acyl azide R–CO–NH–N≡N⁺
3. N2 leaves and R migrates from C to N at the same time → protonated isocyanate R–N=C=O
4. Water adds → carbamic acid R–NH–COOH → loses CO2 → R–NH2 (as its salt)
```

The migrating group keeps its configuration.

**Comparison with related rearrangements** (all give an isocyanate intermediate and an amine with one carbon fewer):

| Reaction | Starting material | Reagent |
| --- | --- | --- |
| Hofmann | Primary amide | Br2 + NaOH |
| Curtius | Acyl azide (from acid chloride + NaN3), heat | Heat |
| Lossen | Hydroxamic acid derivative | Base |
| **Schmidt** | **Carboxylic acid directly** | **HN3 + conc. H2SO4** |

**Advantages**: one-step conversion of an acid to an amine; useful for hindered acids. **Limitations and precautions**: HN3 is highly toxic and explosive, so it is usually made in the flask from **sodium azide and sulphuric acid**, in small amounts, behind a safety screen; strongly acidic conditions exclude acid-sensitive compounds.

## 5.10 Claisen–Schmidt condensation

**Reaction.** A crossed aldol condensation between an **aromatic aldehyde (no α-hydrogen)** and an **aliphatic aldehyde or ketone that has α-hydrogens**, in the presence of **dilute aqueous or alcoholic NaOH**. The β-hydroxy carbonyl product loses water readily to give an **α,β-unsaturated carbonyl compound**, conjugated with the aromatic ring.

```text
  C6H5CHO + CH3CHO        ──dil. NaOH──►  C6H5CH=CH–CHO   + H2O   cinnamaldehyde
  C6H5CHO + CH3COCH3      ──dil. NaOH──►  C6H5CH=CH–CO–CH3 + H2O  benzalacetone
  2 C6H5CHO + CH3COCH3    ──dil. NaOH──►  C6H5CH=CH–CO–CH=CH–C6H5 dibenzalacetone
  C6H5CHO + C6H5COCH3     ──dil. NaOH──►  C6H5CH=CH–CO–C6H5       chalcone
```

**Mechanism**

```text
1. OH⁻ removes an α-hydrogen from the ketone → enolate ion (resonance-stabilised)
2. The enolate carbon attacks the carbonyl carbon of benzaldehyde
   (benzaldehyde cannot form an enolate itself, so it acts only as the acceptor)
3. The alkoxide takes a proton from water → β-hydroxy ketone (aldol)
4. Base removes the α-H again and OH⁻ is lost (E1cB dehydration)
   → α,β-unsaturated ketone, strongly favoured because the new C=C is
     conjugated with both the C=O and the benzene ring
```

**Why it works well**: the aromatic aldehyde cannot self-condense (no α-H), and it is a more reactive acceptor than the ketone, so mainly one crossed product forms.

**Applications**

- Synthesis of **chalcones**, the precursors of flavonoids; chalcones themselves are studied for anti-inflammatory, antimicrobial and anticancer activity.
- Making **cinnamaldehyde** and its derivatives (flavouring).
- Dibenzalacetone (used in sunscreen research and as a ligand).
- The α,β-unsaturated ketones formed are starting materials for **pyrazolines** (with hydrazine), Michael additions and other heterocycles.

## 5.11 Summary table for quick revision

| Reaction | Reagent | Example to quote |
| --- | --- | --- |
| LiAlH4 | Dry ether | CH3COOC2H5 → C2H5OH (two ethanols); CH3CONH2 → C2H5NH2 |
| NaBH4 | Methanol / water | Acetone → isopropanol; keto group reduced, ester spared |
| Clemmensen | Zn–Hg / conc. HCl | Acetophenone → ethylbenzene |
| Wolff–Kishner | NH2NH2 / KOH / glycol, about 200 °C | Acetophenone → ethylbenzene (acid-free) |
| Birch | Na / liquid NH3 / EtOH | Benzene → 1,4-cyclohexadiene; anisole → 1-methoxy-1,4-diene |
| Oppenauer | Al(O-t-Bu)3 / acetone | Pregnenolone → progesterone |
| Dakin | H2O2 / NaOH | Salicylaldehyde → catechol |
| Beckmann | H2SO4 or PCl5 | Cyclohexanone oxime → caprolactam; acetophenone oxime → acetanilide |
| Schmidt | HN3 / conc. H2SO4 | Benzoic acid → aniline |
| Claisen–Schmidt | Dil. NaOH | Benzaldehyde + acetophenone → chalcone |

## Remember

- LiAlH4: strong, dry ether, reduces acids/esters/amides/nitriles; NaBH4: mild, protic solvents, only aldehydes/ketones (and acid chlorides).
- Clemmensen (Zn–Hg/HCl, acid) and Wolff–Kishner (NH2NH2/KOH, base, Huang-Minlon modification) both give C=O → CH2; choose by acid or base sensitivity. Alcohol is not an intermediate in Clemmensen; N2 loss drives Wolff–Kishner.
- Birch: Na/Li in liquid NH3 + ROH → 1,4-cyclohexadiene; donors stay on the double bond, acceptors on the sp3 carbon; used for 19-nor steroids.
- Oppenauer: Al alkoxide + excess acetone, six-membered transition state, reverse of MPV; selective for secondary alcohols; pregnenolone → progesterone.
- Dakin: alkaline H2O2, needs o-/p-OH; aryl migration (like Baeyer–Villiger) → catechol/hydroquinone.
- Beckmann: anti group migrates (stereospecific) through a nitrilium ion; caprolactam (nylon-6), paracetamol.
- Schmidt: HN3/H2SO4; acid → amine with one C fewer through an isocyanate; HN3 is toxic and explosive (make it from NaN3).
- Claisen–Schmidt: aromatic aldehyde (no α-H) + ketone/aldehyde with α-H, dil. NaOH → α,β-unsaturated carbonyl (chalcone, cinnamaldehyde, benzalacetone).
