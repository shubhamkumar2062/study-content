# Unit 1: Benzene and its derivatives

Benzene (C6H6) is a flat ring of six carbons whose six π electrons are shared by the whole ring. That sharing makes it unusually stable, so it prefers **substitution** (keep the ring) over **addition** (break the ring).

## 1.1 Structure of benzene

**Kekulé structure (1865).** A six-membered ring with alternating single and double bonds. Kekulé said the double bonds keep switching between two positions.

**Why Kekulé alone fails:**

- Benzene does not decolourise bromine water or cold KMnO4, unlike real alkenes.
- Only **one** ortho-disubstituted product exists (one 1,2-dibromobenzene). Fixed double bonds would give two.
- All six C–C bonds are the **same length, 1.39 Å**. That sits between a C–C single (1.54 Å) and a C=C double bond (1.34 Å).
- Benzene is about **36 kcal/mol (150 kJ/mol)** more stable than expected (resonance energy).

**Resonance energy from heats of hydrogenation**

| Compound | Heat of hydrogenation |
| --- | --- |
| Cyclohexene (1 C=C) | 28.6 kcal/mol |
| "Cyclohexatriene" expected (3 × 28.6) | 85.8 kcal/mol |
| Benzene actually measured | 49.8 kcal/mol |
| Difference = resonance energy | 36 kcal/mol |

**Resonance (modern) picture.** Benzene is a **resonance hybrid** of the two Kekulé structures. The real molecule is neither; it is an average, drawn as a hexagon with a circle inside.

```text
Draw in the exam:

   Kekulé I   <-->   Kekulé II     =     Hybrid
    ___               ___                 ___
   //  \             /  \\               / o \     (circle = 6 shared π electrons)
  ||    ||          |    |               |     |
   \\__//            \\__//              \___/
```

**Orbital picture (draw this for 5 marks).**

1. Each carbon is **sp2 hybridised**: bond angle 120°, so the ring is a flat regular hexagon.
2. sp2 orbitals form six C–C σ bonds and six C–H σ bonds.
3. Each carbon keeps one unhybridised **p orbital** standing perpendicular to the ring.
4. The six p orbitals overlap sideways all round the ring.
5. Result: two doughnut-shaped **π electron clouds**, one above and one below the plane, holding six delocalised electrons.

```text
        ~~~~~~~~~~~~~~      <- π cloud above the ring
     C---C---C---C---C---C  (flat hexagon of σ bonds, side view)
        ~~~~~~~~~~~~~~      <- π cloud below the ring
```

*Real-life link:* this cloud of shared electrons is why benzene rings appear in so many drugs (paracetamol, aspirin, diazepam): the ring is stable in the body and gives a flat surface that fits receptor pockets.

## 1.2 Aromaticity and Hückel's rule

A compound is **aromatic** when it meets all four conditions:

1. **Cyclic** — atoms joined in a ring.
2. **Planar** — the ring is flat.
3. **Fully conjugated** — every ring atom has a p orbital in the π system.
4. **Hückel's rule** — it has **(4n + 2) π electrons**, where n = 0, 1, 2, 3 … (2, 6, 10, 14 … electrons).

If conditions 1–3 hold but there are **4n π electrons** (4, 8 …), the compound is **antiaromatic** (very unstable). If the ring is not flat or not fully conjugated, it is **non-aromatic**.

| Compound | π electrons | n | Verdict |
| --- | --- | --- | --- |
| Benzene | 6 | 1 | Aromatic |
| Naphthalene | 10 | 2 | Aromatic |
| Anthracene, phenanthrene | 14 | 3 | Aromatic |
| Pyridine, pyrrole, furan, thiophene | 6 | 1 | Aromatic (heterocycles) |
| Cyclopentadienyl anion | 6 | 1 | Aromatic |
| Tropylium (cycloheptatrienyl) cation | 6 | 1 | Aromatic |
| Cyclopropenyl cation | 2 | 0 | Aromatic |
| Cyclobutadiene | 4 | — | Antiaromatic |
| Cyclooctatetraene | 8 | — | Non-aromatic (tub-shaped, not planar) |

**Memory trick:** "**C-P-C-H**" = Cyclic, Planar, Conjugated, Hückel.

## 1.3 Electrophilic aromatic substitution (EAS) — general mechanism

An **electrophile** (E+, "electron lover") replaces one H of the ring. The π cloud is rich in electrons, so it attracts electrophiles.

1. **Generate the electrophile.** A reagent plus a catalyst (acid or Lewis acid) makes E+.
2. **Attack (slow, rate-determining).** The π electrons attack E+. A positively charged, non-aromatic intermediate forms, called the **arenium ion / sigma (σ) complex / Wheland intermediate**. Its + charge is spread over three carbons by resonance (ortho and para to the new group).
3. **Lose H+ (fast).** A base removes H+ from the carbon carrying E. Aromaticity is restored.

```text
FLOWCHART — every EAS answer follows this

 Reagent + catalyst ──► E+ (electrophile)
                              │
                              ▼
 Benzene π cloud attacks E+ ──► σ-complex (arenium ion, 3 resonance forms)  [slow]
                              │
                              ▼
 Base removes H+ ──► substituted benzene (aromatic again)  [fast]
```

**Energy diagram (describe in words):** energy rises to transition state 1 → dips into the σ-complex (an intermediate valley) → rises a little to transition state 2 → falls to products. The first hump is higher, so step 2 is rate-determining.

## 1.4 The four key reactions

**(a) Nitration** — conc. HNO3 + conc. H2SO4 ("nitrating mixture"), 50–55 °C.

```text
Electrophile:  HNO3 + 2 H2SO4  →  NO2+ (nitronium ion) + H3O+ + 2 HSO4−
Overall:       C6H6 + HNO3  —(H2SO4, 50 °C)→  C6H5NO2 (nitrobenzene) + H2O
```

H2SO4 is the stronger acid; it protonates HNO3, which then loses water to give NO2+. Keep the temperature below about 60 °C or dinitrobenzene forms. *Use:* nitrobenzene → aniline → sulpha drugs, paracetamol.

**(b) Sulfonation** — fuming H2SO4 (oleum, H2SO4 + SO3) or hot conc. H2SO4.

```text
Electrophile:  2 H2SO4  ⇌  SO3 + H3O+ + HSO4−     (SO3 is neutral but electron-poor at S)
Overall:       C6H6 + H2SO4 (SO3)  ⇌  C6H5SO3H (benzenesulfonic acid) + H2O
```

Sulfonation is **reversible**: heating with dilute acid or steam removes –SO3H (desulfonation). Chemists use this to block a position temporarily. *Use:* sulfonic acids → sulfonamide drugs, detergents.

**(c) Halogenation** — Cl2/FeCl3 (or AlCl3) or Br2/FeBr3, in the dark.

```text
Electrophile:  Cl2 + FeCl3  →  Cl+ ··· FeCl4−   (Lewis acid polarises Cl–Cl)
Overall:       C6H6 + Cl2  —(FeCl3)→  C6H5Cl (chlorobenzene) + HCl
```

Iodine is too unreactive; iodination needs an oxidising agent (HNO3) to make I+. In **sunlight without catalyst**, Cl2 **adds** instead, giving BHC (see 1.6). This contrast is a favourite MCQ.

**(d) Friedel–Crafts reactions** — Lewis acid AlCl3, anhydrous.

*Alkylation:*

```text
Electrophile:  R–Cl + AlCl3  →  R+ + AlCl4−
Example:       C6H6 + CH3Cl  —(AlCl3)→  C6H5CH3 (toluene) + HCl
```

*Acylation:*

```text
Electrophile:  R–COCl + AlCl3  →  R–C≡O+ (acylium ion, resonance-stabilised) + AlCl4−
Example:       C6H6 + CH3COCl  —(AlCl3)→  C6H5COCH3 (acetophenone) + HCl
```

**Limitations of Friedel–Crafts alkylation (very high probability):**

1. **Polyalkylation** — the alkyl group activates the ring, so the product reacts again (di-, tri-alkylbenzenes). Use excess benzene to reduce it.
2. **Carbocation rearrangement** — n-propyl chloride gives mostly **isopropylbenzene (cumene)**, because the 1° carbocation shifts to a more stable 2° one.
3. **Fails on deactivated rings** — no reaction with nitrobenzene, benzoic acid, benzaldehyde, etc. (Nitrobenzene is even used as the solvent.)
4. **Fails with –NH2, –NHR, –NR2 rings** — the lone pair on nitrogen binds AlCl3 and the ring becomes deactivated.
5. **Aryl and vinyl halides** (e.g. chlorobenzene as the halide) do not form carbocations, so they cannot alkylate.
6. **Reversible** — alkyl groups can migrate or come off.

**Why acylation is better:** the acylium ion does not rearrange, and the C=O product deactivates the ring, so no poly-acylation. To get a straight-chain alkylbenzene, acylate first, then reduce C=O to CH2 (Clemmensen: Zn-Hg/HCl, or Wolff–Kishner). Acylation needs slightly more than 1 equivalent of AlCl3 because the ketone product holds on to AlCl3.

## 1.5 Effect of substituents on reactivity and orientation

A group already on the ring decides two things: **how fast** the next substitution happens (reactivity) and **where** it goes (orientation).

**Two electronic effects:**

- **Inductive effect (I)** — pull or push of electrons through σ bonds. Electronegative atoms (–NO2, –Cl, –OH) are –I. Alkyl groups are +I.
- **Resonance / mesomeric effect (R or M)** — sharing through π orbitals. A group with a lone pair next to the ring donates (+R: –OH, –NH2, –OCH3, –Cl). A group with a π bond to an electronegative atom withdraws (–R: –NO2, –CHO, –COOH, –CN).

| Class | Groups (strongest first) | Ring becomes | Next group goes to |
| --- | --- | --- | --- |
| Strong activators | –O−, –NH2, –NHR, –NR2, –OH, –OCH3 | Much faster than benzene | Ortho + para |
| Moderate activators | –NHCOCH3, –OCOCH3 | Faster | Ortho + para |
| Weak activators | –CH3 and other alkyls, –C6H5 | Slightly faster | Ortho + para |
| Weak deactivators | –F, –Cl, –Br, –I | Slower | Ortho + para (exception) |
| Strong deactivators | –NO2, –NR3+, –CF3, –CN, –SO3H, –COOH, –COOR, –CHO, –COR | Much slower | Meta |

**Why activators send the group ortho/para (anisole example):** when E+ attacks ortho or para, one resonance form of the σ-complex puts the + charge on the carbon holding –OCH3. The oxygen lone pair then shares into the ring, giving a fourth, extra-stable form (every atom has an octet). Meta attack never gets this extra form.

**Why –NO2 sends the group meta:** ortho or para attack puts + on the carbon next to the already positive nitrogen of –NO2. Two + charges side by side is very unstable. Meta attack avoids this, so meta is the "least bad" route.

**Why halogens are the odd one out:** strong –I (pulls electrons) makes the ring slower, but their lone pairs (+R) still stabilise the ortho/para σ-complex. So: deactivating but ortho/para-directing.

**Methyl group:** +I effect and **hyperconjugation** (C–H σ electrons share into the ring) push electrons in. Toluene nitrates about 25 times faster than benzene and gives o- + p-nitrotoluene.

**Ortho vs para ratio:** para is usually the major product with a bulky group or bulky electrophile (steric hindrance at ortho).

```text
ORIENTATION FLOWCHART

 Does the atom joined to the ring have a lone pair, or is it an alkyl?
   ├─ YES → ortho/para director
   │        ├─ is it a halogen? → deactivating (–I wins on rate)
   │        └─ otherwise       → activating
   └─ NO, it is δ+ or carries + (C=O, N=O, C≡N, NR3+) → meta director, deactivating
```

*Pharmacy example:* making paracetamol, the –OH of phenol directs the nitro group para; reducing it gives p-aminophenol, which is acetylated to paracetamol.

## 1.6 Important derivatives: DDT, saccharin, BHC, chloramine

| Compound | Chemical name | Made from | Main use |
| --- | --- | --- | --- |
| DDT | p,p'-Dichlorodiphenyltrichloroethane | Chlorobenzene + chloral | Insecticide (malaria mosquitoes) |
| Saccharin | o-Sulfobenzimide (1,2-benzisothiazol-3-one 1,1-dioxide) | Toluene | Artificial sweetener |
| BHC | Benzene hexachloride = 1,2,3,4,5,6-hexachlorocyclohexane | Benzene + Cl2 in UV light | Insecticide; γ-isomer lindane for scabies, lice |
| Chloramine-T | Sodium N-chloro-p-toluenesulfonamide | Toluene | Antiseptic, disinfectant, oxidising reagent |

**DDT**

```text
2 Cl–C6H5 (chlorobenzene) + Cl3C–CHO (chloral)  —(conc. H2SO4)→  (p-ClC6H4)2CH–CCl3 (DDT) + H2O

Structure: two p-chlorophenyl rings on one carbon, which also carries a –CCl3 group.
      Cl–C6H4
             \
              CH–CCl3
             /
      Cl–C6H4
```

The para positions are chosen because Cl is an o/p director and para has less crowding. DDT kills insects by keeping their nerve sodium channels open. It is now **banned or restricted** for farming because it does not break down, builds up in fat (bioaccumulation) and harms birds (thin eggshells). It is still allowed in limited indoor malaria spraying.

**Saccharin (Remsen–Fahlberg synthesis)**

```text
Toluene
  │  ClSO3H (chlorosulfonic acid)
  ▼
o-Toluenesulfonyl chloride  (+ para isomer, separated)
  │  NH3
  ▼
o-Toluenesulfonamide
  │  KMnO4 (oxidises –CH3 to –COOH)
  ▼
o-Sulfamoylbenzoic acid
  │  heat, –H2O (ring closes)
  ▼
Saccharin  (benzene ring fused to a 5-membered ring: C=O, N–H, SO2)
```

Saccharin is about **300–500 times sweeter than sugar** and gives no calories, so it suits diabetic and diet products. It is poorly soluble, so the **sodium salt** is used in tablets and syrups. It has a slight bitter aftertaste.

**BHC (benzene hexachloride, gammexane, lindane)**

```text
C6H6 + 3 Cl2  —(sunlight / UV, no catalyst)→  C6H6Cl6
```

This is a **free-radical addition**, not substitution; the ring loses aromaticity. Several stereoisomers form (α, β, γ, δ …). Only the **γ-isomer (lindane, \~12–15% of the mixture)** is strongly insecticidal. *Uses:* insecticide; 1% lindane lotion for **scabies and head lice**. Its use is now restricted because of nerve toxicity and environmental persistence. The name "benzene hexachloride" is misleading — it is a cyclohexane, not a benzene.

**Chloramine-T**

```text
Toluene —(ClSO3H)→ p-toluenesulfonyl chloride —(NH3)→ p-toluenesulfonamide
        —(NaOCl / NaOH)→  CH3–C6H4–SO2–N(Cl)− Na+   (chloramine-T)
```

In water it slowly releases **hypochlorite (active chlorine)**, which kills microbes. *Uses:* antiseptic for wounds and mouthwashes, disinfecting water, surfaces and instruments, and as an oxidising agent in drug analysis. It is gentler on tissue than bleach. (Dichloramine-T, the N,N-dichloro form, is a related antiseptic.)

## 1.7 Unit 1 mind map

```text
                         BENZENE & DERIVATIVES
   ┌────────────────────────┬────────────────────┬───────────────────────┐
 Structure                 Aromaticity            EAS                    Derivatives
 • Kekulé + flaws          • C-P-C-H              • 3-step mechanism     • DDT
 • resonance, 1.39 Å       • 4n+2 π e−            • nitration            • saccharin
 • sp2 orbital picture     • anti / non-aromatic  • sulfonation (rev.)   • BHC / lindane
 • 36 kcal/mol RE                                 • halogenation         • chloramine-T
                                                  • Friedel–Crafts
                                                  • substituent effects
```
