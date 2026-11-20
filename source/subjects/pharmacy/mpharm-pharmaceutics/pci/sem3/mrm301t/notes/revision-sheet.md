# Last-night revision sheet

## Unit 1: General research methodology

- **Research** = systematic, objective, replicable search for knowledge. Basic vs applied; quantitative vs qualitative; descriptive, analytical, experimental; retrospective vs prospective.
- **Process:** problem → literature → objectives (SMART) → hypothesis (H0/H1) → design → sample size → protocol → ethics approval → pilot → data → analysis → report.
- **PICO:** Population, Intervention, Comparison, Outcome.
- **Literature:** primary, secondary, tertiary sources; PubMed (MeSH), Scopus, Web of Science, Cochrane, CTRI; Boolean AND narrows, OR widens, NOT excludes; systematic review → PRISMA; meta-analysis → forest plot.
- **Designs:** cross-sectional (prevalence); case–control (cases first, look back, **odds ratio**, rare disease); cohort (exposure first, follow forward, **relative risk**); RCT (gold standard).
- RR = EER/CER; RRR = 1 − RR; ARR = CER − EER; **NNT = 1/ARR rounded up** (CER 0.20, EER 0.12 → RR 0.60, ARR 0.08, NNT 13).
- **Random error** ↓ with larger n; **bias** only removed by design.
- Biases: selection, allocation, performance, detection, attrition, recall, publication, confounding. Remedies: randomization + concealment, blinding, ITT, registration, matching/stratification.
- **Randomization:** simple, block, stratified, cluster, minimization. Concealment protects before allocation; blinding after.
- **Controls:** placebo, active, no-treatment, dose–response, historical, add-on.
- **Crossover (AB/BA):** own control, fewer subjects; needs stable disease and washout (≈ 5 half-lives in BE studies); problems: carryover, period effect, dropouts.
- **Blinding:** open, single, double, triple, PROBE; double-dummy for different dosage forms; emergency unblinding kept.

## Unit 2: Biostatistics

- n (two means, per group) = 2(zα/2 + zβ)²σ²/Δ²; σ 10, Δ 5, α 0.05, power 80% → **63**; with 10% dropout 63/0.9 = **70**.
- n (two proportions) = (zα/2 + zβ)²[p1q1 + p2q2]/(p1 − p2)²; 40% vs 25% → **150**.
- n ↑ with smaller α, higher power, larger σ, smaller Δ, more dropouts; ↓ with paired designs.
- **Type I** (α) = reject true H0 (false positive); **Type II** (β) = miss real effect; **power = 1 − β** (80–90%).
- **P value** = chance of data this extreme if H0 true. Not P(H0 true). Report exact P + effect + 95% CI. Bonferroni α/k for multiple tests.
- **df:** one-sample/paired n − 1; unpaired n1 + n2 − 2; r n − 2; ANOVA k − 1, N − k; χ² (r − 1)(c − 1).
- One-sample t = (x̄ − µ)/(s/√n). Unpaired t = (x̄1 − x̄2)/√[sp²(1/n1 + 1/n2)] (example **4.92**, df 14, CI 3.1–7.9). Paired t = d̄/(sd/√n) (example **7.21**, df 7).
- **ANOVA:** CF = G²/N; SST = Σx² − CF; SSB = ΣT²/n − CF; F = MSB/MSW (example **13.40** vs 3.89); LSD = t√(2MSW/n) = 3.98; post-hoc Tukey, Dunnett, Bonferroni.
- **r** = Sxy/√(SxxSyy) (example **−0.991**); t = r√[(n − 2)/(1 − r²)]; regression ŷ = a + bx, b = Sxy/Sxx (ŷ = 142.25 − 1.018x).
- **Non-parametric:** Wilcoxon signed rank (paired; T = 0 ≤ 3); Mann–Whitney U = n1n2 + n1(n1 + 1)/2 − R1 (U = 3 ≤ 5); Kruskal–Wallis H = 12/N(N + 1) × ΣR²/n − 3(N + 1) (H = 8.0 > 5.99); Friedman (7.0); Spearman ρ = 1 − 6Σd²/n(n² − 1) (0.83).
- **χ²** = Σ(O − E)²/E; E = row × column/N; E ≥ 5 else Fisher's exact; Yates for small 2 × 2; McNemar for paired (example **8.0** > 3.84).

## Unit 3: Medical research and ethics

- Landmarks: Hippocratic Oath; Percival 1803; **Nuremberg Code 1947** (voluntary consent essential); Geneva 1948; **Helsinki 1964**; Tuskegee (1932–72); **Belmont 1979** (respect for persons, beneficence, justice); ICH-GCP 1996; **ICMR 2017**; **NDCT Rules 2019**.
- **Values:** autonomy, beneficence, non-maleficence, justice (+ dignity, truthfulness).
- **Double effect:** good act; bad effect foreseen not intended; not the means; proportionate (opioids in terminal pain).
- **Euthanasia:** active/passive; voluntary/non-voluntary/involuntary; assisted suicide. India: active illegal; passive allowed (Aruna Shanbaug 2011); living wills (Common Cause 2018).
- **Consent:** disclosure, comprehension, voluntariness, capacity, documentation, withdrawal; child assent; impartial witness; audio-video consent where rules require; re-consent.
- **Confidentiality** with limited exceptions (notifiable disease, court order, serious risk to others).
- **EC (India):** ≥ 7 members — medical scientist, clinician, legal expert, social scientist/ethicist/theologian, lay person; both genders; ≥ half non-affiliated; outside chairperson; registered with CDSCO for trials.
- Conflicts of interest → disclose and recuse; no fee-splitting; vendor gifts restricted (UCPMP 2024); avoid treating own family; sexual relationships with patients forbidden; futile treatment not obligatory, comfort care always.

## Unit 4: CPCSEA guidelines

- PCA Act 1960 (Section 15) → Breeding of and Experiments on Animals (Control and Supervision) Rules 1998 → CPCSEA (renamed **CCSEA**, 2023).
- **3Rs:** Replacement, Reduction, Refinement (Russell and Burch, 1959).
- **IAEC:** biological scientist, 2 scientists of other disciplines, veterinarian (mandatory), scientist in charge of animal house + main nominee, link nominee, outside scientist, socially aware nominee. Form B = protocol; Form D = record of animal use; IAEC approves up to rodents.
- **Quarantine:** ≥ 1 week small, 6 weeks large animals; then stabilisation; separate species.
- **Environment:** 18–29 °C; RH 30–70%; standby HVAC; separate ventilation; timed light cycle; low noise.
- Animal rooms ≈ 50–60% of built area; facility away from habitation, dust, noise, pests.
- **Records:** plans, staff, health, SOPs, breeding/stock, IAEC minutes, Form D, deaths, clinical, training, water analysis.
- **SOP items:** author, title, date, previous issue, distribution, objectives, instruments, reagents, normal values, hazard and risk.
- No eating, drinking, smoking in animal rooms; medical check-ups; vaccination; training for new staff.
- Transport: mode, container, density, food and water, protection from stress.
- Painful procedures under anaesthesia; never paralyse without anaesthesia; euthanasia humane, approved, by trained person, death confirmed.

## Unit 5: Declaration of Helsinki

- WMA; adopted **June 1964, Helsinki**; revisions 1975 Tokyo (independent committee), 1983, 1989, 1996, **2000 Edinburgh** (A introduction, B basic principles, C research with care), 2002 and 2004 clarifications, 2008 Seoul, 2013 Fortaleza, **2024 Helsinki** (current, 37 paragraphs).
- Knowledge never takes precedence over participants' rights; responsibility on researcher, not participant.
- Basic principles: sound science and protocol; prior ethics committee approval, monitoring and approval of amendments; risk–benefit; vulnerable groups; privacy; free informed (written) consent; assent; independent person seeks consent in dependent relationships; registration before first participant; publish negative results.
- With medical care: only if potential value to patients; test against **best proven intervention**; placebo only when no proven treatment, or compelling reason with no serious/irreversible harm; **post-trial provisions**; refusal never affects care; unproven intervention as last resort with consent, then researched.
