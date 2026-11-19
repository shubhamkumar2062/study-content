# Unit 1: New drug discovery and development

A new medicine reaches patients only after a long chain of work: finding a disease target, finding a molecule that acts on it, testing that molecule in the laboratory and in animals, testing it in people, and finally convincing a regulator that it is safe, effective and of good quality. This unit follows that chain and then looks at the other side of the market: **generic** medicines, which copy an innovator product after its patents and exclusivities end.

Regulatory science is the study of the rules, standards and evidence that regulators use to make these decisions. Everything in this subject (IND, NDA, ANDA, CTD, clinical trial rules) is built on the stages described here.

## 1.1 Drug discovery and drug development: the difference

| Drug discovery | Drug development |
| --- | --- |
| Finds a new molecule that may become a medicine | Turns that molecule into an approved product |
| Target identification, hit finding, lead optimisation | Pre-clinical studies, clinical trials, manufacturing, regulatory filing |
| Mostly chemistry, biology and computer methods | Pharmacology, toxicology, pharmaceutics, clinical research, regulatory affairs |
| Ends with a **candidate drug** | Ends with **marketing approval** and continues after it |

Overall picture:

```text
DISCOVERY                        DEVELOPMENT                              MARKET
Target → Hit → Lead → Candidate → Pre-clinical → IND/CTA → Phase I → II → III
                                                → NDA/MAA → Approval → Phase IV
```

The whole process commonly takes 10–15 years. Out of thousands of molecules screened, only a handful reach clinical trials, and most of those fail (often in Phase II because the drug does not work well enough, or because of safety). This high failure rate is why new drugs are expensive and why patents and data exclusivity exist.

## 1.2 Stages of drug discovery

### a. Target identification

A **target** is the biological molecule the drug will act on: a receptor, enzyme, ion channel, transporter or nucleic acid. Targets are found from knowledge of disease biology, genomics and proteomics (genes or proteins that differ in disease), and from studying how existing drugs work.

### b. Target validation

The team shows that changing the target really changes the disease. Methods include gene knock-out or knock-down animals, antisense or siRNA, antibodies that block the target, and the use of known tool compounds. A well-validated target reduces the chance of failure later.

### c. Assay development and hit identification

An **assay** is a test that measures activity on the target (for example enzyme inhibition or receptor binding). Hits are molecules that show activity in the assay.

Sources of hits:

1. **High-throughput screening (HTS):** automated testing of large compound libraries.
2. **Natural products:** plant, microbial and marine sources (for example many antibiotics and anticancer drugs).
3. **Rational (structure-based) design:** using the 3-D structure of the target from X-ray crystallography or NMR.
4. **Computer-aided drug design:** virtual screening, docking, QSAR.
5. **Fragment-based screening:** small fragments that bind weakly are grown into potent molecules.
6. **Modifying known drugs** ("me-too" or follow-on molecules) and repurposing old drugs for new uses.
7. **Biotechnology:** monoclonal antibodies, recombinant proteins, nucleic acid drugs.

### d. Hit to lead

Hits are confirmed, ranked and tested for selectivity. A **lead** is a hit series with good potency, selectivity and a reasonable starting profile.

### e. Lead optimisation

Medicinal chemists change the structure to improve:

- potency and selectivity (structure–activity relationship, SAR);
- drug-likeness: solubility, permeability (Lipinski's rule of five is a common guide for oral drugs);
- ADME: absorption, metabolic stability, half-life;
- early safety: hERG channel binding, genotoxicity alerts, CYP inhibition.

### f. Candidate selection

One molecule (sometimes with a back-up) is chosen as the **development candidate**. It then enters formal pre-clinical development.

## 1.3 Drug development process

Drug development has three overlapping streams that must all be complete at the time of filing:

| Stream | Main work | Regulatory output |
| --- | --- | --- |
| Non-clinical (pre-clinical) | Pharmacology, pharmacokinetics, toxicology in vitro and in animals | Module 4 of the CTD |
| Clinical | Phase I–III trials in humans | Module 5 of the CTD |
| Chemistry, manufacturing and controls (CMC) | API synthesis, formulation, specifications, stability, scale-up | Module 3 of the CTD |

## 1.4 Pre-clinical studies

Pre-clinical studies show that it is reasonably safe to give the drug to humans and help choose the first human dose. Studies that support safety must follow **Good Laboratory Practice (GLP)**.

### a. Pharmacology

- **Primary pharmacodynamics:** effect on the target and in disease models.
- **Secondary pharmacodynamics:** effects on other targets.
- **Safety pharmacology:** effects on vital organ systems. The "core battery" covers the cardiovascular system (including QT prolongation and the hERG assay), the central nervous system and the respiratory system (ICH S7A, S7B).

### b. Pharmacokinetics and drug metabolism

- Absorption, distribution, metabolism and excretion in animal species.
- Metabolites and the enzymes involved; enzyme induction or inhibition.
- Plasma protein binding and tissue distribution.
- **Toxicokinetics:** drug exposure measured during toxicity studies, to link toxicity with exposure.

### c. Toxicology

| Study | What it tells |
| --- | --- |
| Single-dose (acute) toxicity | Effects after one dose; helps choose doses for longer studies |
| Repeated-dose toxicity | Target organs and the no-observed-adverse-effect level (NOAEL); duration linked to the length of the planned trials |
| Genotoxicity | Gene mutation (Ames test) and chromosome damage (chromosomal aberration, micronucleus tests) |
| Carcinogenicity | For drugs used for long periods |
| Reproductive and developmental toxicity | Fertility, embryo–fetal development, pre- and post-natal development |
| Local tolerance | Irritation at the site of application or injection |
| Special studies | Immunotoxicity, phototoxicity, dependence potential where relevant |

The ICH M3(R2) guideline links which non-clinical studies are needed before each clinical phase. In India the required non-clinical data are listed in the **New Drugs and Clinical Trials (NDCT) Rules, 2019**.

### d. Choosing the first human dose

The NOAEL from the most sensitive animal species is converted to a human equivalent dose (by body-surface-area scaling) and a safety factor is applied, giving the maximum recommended starting dose for the first Phase I study. Students need to know the principle, not the numbers.

## 1.5 Non-clinical activities

The syllabus lists "non-clinical activities" separately. These are all the activities that are not studies in humans but are still needed for approval:

1. **Chemistry and API development:** route of synthesis, impurities, polymorphs, salt selection, scale-up of the API.
2. **Pre-formulation:** solubility, pKa, partition coefficient, stability, compatibility with excipients.
3. **Formulation development:** dosage form for clinical trials, then the commercial formula.
4. **Analytical development:** methods for assay, impurities, dissolution; method validation (ICH Q2).
5. **Stability studies:** to set shelf life and storage conditions (ICH Q1A).
6. **Manufacture of clinical supplies** under GMP, with labelling and blinding.
7. **Packaging development.**
8. **Regulatory planning, intellectual property (patents) and project management.**

## 1.6 Clinical studies

Clinical studies are research in humans, done only after regulator and ethics committee approval and with informed consent (details in Unit 4).

| Phase | Subjects | Main question |
| --- | --- | --- |
| Phase 0 (exploratory) | Very few volunteers, micro-doses | Does the drug reach the target? Early PK |
| Phase I (human pharmacology) | Healthy volunteers (patients for toxic drugs such as anticancer agents); small numbers | Safety, tolerability, PK, dose range |
| Phase II (therapeutic exploratory) | Patients with the disease; usually up to a few hundred | Does it work? Which dose? Short-term safety |
| Phase III (therapeutic confirmatory) | Larger numbers of patients, often many centres and countries | Confirms efficacy and safety against placebo or standard treatment |
| Phase IV (post-marketing) | Patients after approval | Rare adverse reactions, long-term safety, new uses, special groups |

Main points:

- Phase III data are the main evidence for approval.
- Bioavailability and bioequivalence studies are clinical pharmacology studies that support formulation changes and generics.
- After approval, safety monitoring continues through pharmacovigilance and periodic safety reports.

## 1.7 Innovator and generic products

**Innovator (originator, brand) product:** the first product of a new active ingredient to be approved, after the company itself carried out the full non-clinical and clinical studies. It is usually protected by patents and by regulatory exclusivity.

**Generic product:** a product that contains the same active ingredient as the innovator (reference) product, in the same dosage form, strength and route, with the same intended use, and is shown to be **bioequivalent** to it. It can be marketed once patents and exclusivities of the reference product no longer block it.

| Point | Innovator | Generic |
| --- | --- | --- |
| Data submitted | Full quality, non-clinical and clinical data | Quality data + bioequivalence; relies on the innovator's proven safety and efficacy |
| US route | NDA under section 505(b)(1) | ANDA under section 505(j) |
| Development time | Long (often more than a decade) | Short (a few years) |
| Cost | Very high | Much lower |
| Price to patient | High while protected | Usually much lower |
| Brand name | Trade name | Generic name or a branded generic name |
| Protection | Patents, data and market exclusivity | Possible exclusivity for the first challenger in the USA |

## 1.8 Concept of generics

### a. Key terms

| Term | Meaning |
| --- | --- |
| Reference listed drug (RLD) | The approved drug product a generic applicant copies and compares with (US term) |
| Pharmaceutical equivalents | Same active ingredient, same dosage form, same strength and route; may differ in excipients, shape, colour |
| Pharmaceutical alternatives | Same active moiety but a different salt, ester or dosage form |
| Bioequivalence | No significant difference in the rate and extent of absorption of the active ingredient when given at the same molar dose under similar conditions |
| Therapeutic equivalence | Pharmaceutical equivalents that are bioequivalent and can be expected to have the same clinical effect and safety; listed in the US Orange Book (Unit 5) |
| Branded generic | A generic sold under a company brand name (very common in India) |
| Biosimilar | A biological product highly similar to an approved reference biological, with no clinically meaningful differences; needs more data than a small-molecule generic |

### b. Why generics matter

1. Lower cost and wider access to medicines.
2. Competition reduces prices of the innovator brand too.
3. Large savings for governments and insurance schemes.
4. India is one of the largest suppliers of generic medicines in the world, so generic development and overseas registration (Unit 3) are a major part of the Indian industry.

### c. The Hatch–Waxman Act (USA, 1984)

Formally the Drug Price Competition and Patent Term Restoration Act. It created the modern generic system:

- the **ANDA** route: generics show bioequivalence instead of repeating clinical trials;
- **patent term restoration** for innovators, to give back some time lost during regulatory review;
- the listing of patents in the Orange Book and **patent certifications** by generic applicants (Paragraph I–IV, Unit 2);
- **180-day exclusivity** for the first generic applicant who successfully challenges a patent (Paragraph IV).

## 1.9 Generic drug product development

```text
Select product (market, patent and exclusivity status, technical difficulty)
  → Study the reference product (characterisation, "reverse engineering")
  → Source API (with DMF) and excipients
  → Pre-formulation and formulation development
  → Comparative dissolution with the reference product
  → Pilot bioequivalence study (optional) → scale-up
  → Exhibit / submission batch under GMP
  → Pivotal bioequivalence study
  → Stability studies → ANDA / dossier → approval → launch
```

### Steps in more detail

1. **Product selection:** market size, patent expiry and exclusivity, number of competitors, technical difficulty, availability of API.
2. **Characterisation of the reference product:** assay, impurities, dissolution in several media, physical tests (weight, hardness, size), excipient list from the label; for some products the aim is the same type and amount of excipients as the reference (often called Q1/Q2 sameness), which some regulators require for certain dosage forms.
3. **API sourcing:** qualified supplier with a Drug Master File; same polymorphic form and particle size range as needed for equivalent performance.
4. **Formulation and process development:** often using quality by design and design of experiments; the product must avoid infringing formulation patents still in force.
5. **Comparative dissolution:** test and reference profiles compared; the similarity factor f2 between 50 and 100 indicates similar profiles.
6. **Scale-up and exhibit batch:** made on production-type equipment under GMP; its size must meet the regulator's minimum batch-size rules (check the current guidance of the target market).
7. **Bioequivalence study:** usually randomised, two-way crossover in healthy volunteers; Cmax and AUC compared; the 90% confidence interval of the test/reference ratio should fall within 80.00–125.00% for most drugs.
8. **Biowaiver:** for some products (for example certain highly soluble drugs under the Biopharmaceutics Classification System, or additional strengths of a product), the regulator may accept in vitro data instead of an in vivo BE study, under defined conditions.
9. **Stability and dossier:** stability data as per ICH or zone-specific conditions; dossier in CTD format.
10. **Life cycle:** post-approval changes, pharmacovigilance, annual reports.

### Challenges in generic development

- Patents on the molecule, polymorph, formulation or method of use.
- Highly variable drugs, narrow therapeutic index drugs and complex products (inhalers, topicals, long-acting injections) that need special BE approaches.
- Differences in excipients that change dissolution or stability.
- Meeting the different requirements of many importing countries.

## Remember

- Discovery: target → validation → hit → lead → optimisation → candidate. Development: pre-clinical → IND/CTA → Phase I–III → NDA/MAA → approval → Phase IV.
- Pre-clinical: pharmacology (with safety pharmacology core battery), ADME + toxicokinetics, toxicology (acute, repeated dose, genotoxicity, carcinogenicity, reproductive, local tolerance), under GLP.
- Non-clinical activities = CMC, pre-formulation, formulation, analytical, stability, clinical supplies, packaging, IP and regulatory planning.
- Phases: 0 micro-dose; I safety and PK; II efficacy and dose; III confirmation; IV post-marketing.
- Innovator = full data, NDA 505(b)(1); generic = same API, dosage form, strength, route + bioequivalence, ANDA 505(j).
- Hatch–Waxman Act 1984: ANDA, patent term restoration, Paragraph IV, 180-day exclusivity.
- Generic development: reference characterisation → API with DMF → formulation → f2 50–100 → exhibit batch → BE (90% CI 80.00–125.00%) → stability → dossier.
