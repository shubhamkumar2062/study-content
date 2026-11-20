# Last-night revision sheet

Focus your final hour on five answers: **the matched-dose bioassay method (calculations + diagram)**, **Schultz-Dale technique and sensitisation for anaphylaxis**, **hot-plate vs tail-flick for analgesic screening**, **LD₅₀ and therapeutic index calculations**, and **the three classic autacoid bioassays (histamine, 5-HT, acetylcholine) with their standard preparations**. These cover the core 10-mark questions.

---

## Definitions in one line

| Term | Meaning |
| --- | --- |
| Bioassay | Estimation of potency or activity of a substance using a living organism or its parts |
| Standardisation | Matching the potency of a preparation to that of a standard |
| Sensitivity | Smallest dose that produces a detectable response |
| Specificity | Ability to detect one substance in a mixture |
| Precision | Reproducibility of repeated estimates |
| ED₅₀ | Dose producing the desired effect in 50% of animals |
| LD₅₀ | Dose lethal to 50% of animals |
| Therapeutic index | LD₅₀ ÷ ED₅₀ (wider = safer) |
| Graded response | Response varies continuously with dose |
| Quantal response | All-or-none; each animal either responds or does not |
| Peristaltic wave | Coordinate contraction-relaxation wave used in guinea-pig ileum |
| Sensitisation | Pre-exposure to antigen causing IgE-mediated mast cell priming |
| In-vivo model | Experiment in a living whole animal |
| In-vitro model | Experiment in isolated organ, cell or tissue |

---

## Standard bioassay preparations — at a glance

| Autacoid | Preparation | Contraction or relaxation? | Species |
| --- | --- | --- | --- |
| Histamine | Guinea-pig ileum (Mg-free Tyrode) | Contraction | Guinea pig |
| Histamine (alternate) | Rat uterus | Contraction | Rat |
| 5-HT (serotonin) | Rat fundal strip | Contraction | Rat |
| 5-HT (alternate) | Rabbit ear artery | Contraction (5-HT₂) | Rabbit |
| Acetylcholine | Frog rectus abdominis | Contraction | Frog |
| Acetylcholine (alternate) | Leech dorsal muscle | Contraction | Leech |
| Bradykinin | Rat uterus (oestrogen-primed) | Contraction | Rat |
| Angiotensin II | Rat aortic strip | Contraction | Rat |

---

## Bioassay methods — when to use each

| Method | Use when | Key calculation |
| --- | --- | --- |
| Three-point (3+3) | Routine potency estimate; most common exam answer | 2 test doses + 2 std doses; use log-dose scale |
| Four-point (2+2) | High precision needed | 2 std + 2 test on same preparation |
| Multiple-point | Research settings; more doses | Dose-response curve, interpolation |
| Bracket dilution | Approximate estimate quickly | Straddle the standard response |

---

## Matched-dose (2+2) bioassay steps

```text
1. Mount preparation; allow to equilibrate (30 min).
2. Prepare dose-response curve for the standard (S1, S2 — two doses, e.g. 1 and 2 µg/mL).
3. Confirm linearity and parallelism.
4. Apply test doses (T1, T2) to bracket the standard responses.
5. Interpolate on the log-dose axis: M = log(T) − log(S) for matched responses.
6. Potency ratio = antilog(M); multiply by concentration of standard.
7. Report with confidence limits.
```

---

## Schultz-Dale technique (anaphylaxis bioassay)

```text
Sensitisation phase (10–14 days before):
  Guinea pig ← inject antigen (ovalbumin) IP or SC.
  IgE forms, sensitises mast cells in smooth muscle.

Assay day:
  Isolate guinea-pig ileum; mount in organ bath (Tyrode at 37°C, O₂).
  Add antigen (ovalbumin) → antigen + IgE on mast cells → degranulation
  → Histamine + other mediators released locally
  → Brisk, immediate contraction of the ileum.
```

**Measurement**: height of contraction = index of anaphylaxis. Antihistamines inhibit the response. Used to test antiallergic drugs.

---

## Analgesic screening models — comparison

| Model | Stimulus | Endpoint | Opioids | NSAIDs | Notes |
| --- | --- | --- | --- | --- | --- |
| Hot plate | Thermal (55°C plate) | Latency to lick paw or jump | Yes | Weak | Supraspinal; can be adapted |
| Tail flick (D'Amour & Smith) | Radiant heat beam on tail | Tail withdrawal latency | Yes | Poor | Spinal reflex; objective |
| Acetic acid writhing | Chemical (IP acetic acid) | Number of writhes in 20 min | Yes | Yes (better) | Sensitive to both; screen first |
| Formalin test | Chemical (SC formalin) | Licking time phase 1 (acute) and phase 2 (inflammatory) | Phase 1 | Phase 2 | Separates opioid from anti-inflammatory |
| Randall-Selitto | Pressure on inflamed paw | Threshold force producing withdrawal | Yes | Yes | Useful for anti-inflammatory analgesics |

---

## Anti-inflammatory models — comparison

| Model | Trigger | Paw volume by | Use |
| --- | --- | --- | --- |
| Carrageenan paw oedema | Carrageenan 1% (sub-plantar) | Plethysmometer | Acute; prostaglandin-dependent |
| Adjuvant arthritis (Freund's) | Complete Freund's adjuvant | Plethysmometer + X-ray | Chronic; immune-mediated |
| Cotton pellet granuloma | Implanted pellets | Weight (dry) | Chronic; anti-fibrotic |
| Croton-oil ear oedema | Topical croton oil | Micrometer; ear punch weight | Topical anti-inflammatory |

**All models**: measure drug vs vehicle; express as % inhibition of inflammation.

---

## Toxicity study types

| Type | Duration | Animals | What it determines |
| --- | --- | --- | --- |
| Acute toxicity | Single dose, 14-day observation | Rodents (rat, mouse) | LD₅₀; dose for sub-acute studies; clinical signs of toxicity |
| Sub-acute (28-day) | 28 days daily dosing | Rodents | Organ toxicity; reversibility |
| Sub-chronic (90-day) | 90 days | Rodents + non-rodent | NOAEL; regulatory requirement |
| Chronic | 6–24 months | Rodents + non-rodent | Carcinogenicity, cumulative toxicity |
| Reproductive | Females during gestation | Rat, rabbit | Teratogenicity, foetal toxicity |
| Genetic (Ames test) | — | *Salmonella* bacteria | Mutagenicity |

---

## Important calculations

| Formula | Symbol | Use |
| --- | --- | --- |
| Therapeutic index | TI = LD₅₀ / ED₅₀ | Safety measure; higher = safer |
| Protective index | PI = TD₅₀ / ED₅₀ | For neuropharmacology (TD = toxic dose) |
| Potency ratio (bioassay) | M = log T − log S (matched responses) | How many times more/less potent than standard |
| % inhibition (anti-inflammatory) | (control − treated) ÷ control × 100 | Efficacy of anti-inflammatory |
| Clearance | CL = dose / AUC | Rate of elimination per unit concentration |
| Volume of distribution | Vd = dose / C₀ | Apparent space for drug distribution |
| Half-life | t½ = 0.693 × Vd / CL | Time for concentration to halve |

---

## Exam reminder

- Section A (20 marks): expect one MCQ per model (hot plate / EPM / carrageenan / LD₅₀ / Schultz-Dale). Know the endpoint of each.
- Section B (10 marks each, 2 of 3): matched-dose bioassay method with calculation is a near-certain 10-mark question. Write the formula, the steps, and add a diagram of the organ bath setup.
- Section C (5 marks each, 7 of 9): one-preparation descriptions (Schultz-Dale sensitisation; tail-flick procedure; Ames test; organ bath mounting technique) all score well with a labelled diagram.
- For every in-vivo model: state animal species, route of administration, dose, endpoint measured, and what positive control is used.
- For every in-vitro preparation: state organ, species, bath solution, temperature, gas mixture (O₂/CO₂ or O₂), and contraction direction.
