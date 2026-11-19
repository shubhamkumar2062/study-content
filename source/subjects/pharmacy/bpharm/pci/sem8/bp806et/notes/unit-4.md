# Unit 4: Stability testing, chromatographic standardisation, dossiers and Drugs and Cosmetics Act provisions

This unit is the practical end of herbal quality control. It asks four questions: will the product keep its quality until the expiry date (stability testing)? How do we prove that every batch has the same chemical profile (chromatography)? What papers must be filed to get permission to sell a new herbal drug at home or abroad (new drug application and export registration)? And what does Indian law demand of the manufacturer (GMP and the Drugs and Cosmetics Act)?

## 4.1 Stability testing of herbal medicines

**Stability** is the ability of a product to keep its identity, strength, quality and purity — physical, chemical, microbiological, therapeutic and toxicological properties — within specified limits throughout its shelf life, in the pack in which it is sold.

**Shelf life** is the period during which the product, stored as directed on the label, stays within its specification. **Stability testing** provides the evidence for the shelf life and the storage instructions.

### Why herbal stability is difficult

| Difficulty | Reason |
| --- | --- |
| Many constituents | The active constituents may be unknown; a single assay cannot show that the whole product is unchanged |
| Constituents interact | Enzymes, tannins, sugars and oils react with each other and with excipients |
| Volatile and labile compounds | Essential oils evaporate; glycosides hydrolyse; polyphenols and carotenoids oxidise; some compounds are light-sensitive |
| Hygroscopic powders | Extracts and churnas absorb moisture, cake and grow mould |
| Microbial load | Natural materials carry spores that can grow on storage |
| Natural variation | Batches differ before storage even begins |

### Approach for herbal products

Because one assay is not enough, herbal stability is judged by a combination of:

1. **Marker or active-constituent content** (HPLC/HPTLC assay) within limits.
2. **Chromatographic fingerprint** — the pattern of peaks or bands should remain comparable to the initial one, with no major new or lost peaks.
3. **Physical properties** — appearance, colour, odour, taste, moisture, pH, viscosity, sedimentation, hardness, disintegration.
4. **Microbial quality** — counts stay within limits; preservative efficacy where relevant.
5. **Dosage-form specific tests** — alcohol content of asavas and arishtas, peroxide or acid value of oils and ghritas, sugar content of syrups and avalehas.

### Climatic zones (WHO stability guidance)

| Zone | Climate | Long-term testing condition |
| --- | --- | --- |
| I | Temperate | 21 °C / 45% RH |
| II | Subtropical, Mediterranean | 25 °C / 60% RH |
| III | Hot and dry | 30 °C / 35% RH |
| IVa | Hot and humid | 30 °C / 65% RH |
| IVb | Hot and very humid | 30 °C / 75% RH |

India is placed in **zone IVb**, so products for the Indian market are tested long-term at **30 °C / 75% RH**.

### Stability protocol (based on ICH Q1A(R2) and WHO guidance)

```text
Select batches (normally 3, at least pilot scale, same process as production)
        |
Pack in the container-closure intended for marketing
        |
Store under: long-term | accelerated (40 °C / 75% RH) | intermediate if needed
        |
Pull samples: long-term 0, 3, 6, 9, 12, 18, 24 months, then yearly
              accelerated 0, 3, 6 months
        |
Test: appearance, moisture, marker assay, fingerprint, microbial, others
        |
Evaluate trends -> assign shelf life and storage statement
```

- **Significant change** during accelerated testing (for example failure of the assay, appearance or another specification) leads to intermediate testing and a more cautious shelf life.
- **Photostability** testing (ICH Q1B) is added for light-sensitive products; results decide whether an opaque or amber pack is needed.
- **In-use stability** is tested for multi-dose liquids that are opened repeatedly.
- **Ongoing (follow-up) stability** — at least one production batch a year is kept on stability to confirm the shelf life.

**Accelerated testing** uses the idea that reaction rates rise with temperature (Arrhenius relation, k = A e^(−Ea/RT)), so degradation seen at 40 °C helps predict behaviour at normal storage. For complex herbal mixtures this prediction is less reliable, so long-term real-time data remain essential.

**Indian rule for ASU medicines**: **Rule 161-B** of the Drugs and Cosmetics Rules prescribes the shelf life (date of expiry) of ASU medicines by type of dosage form; a manufacturer who wants a different period must support it with stability data.

## 4.2 Chromatographic techniques in standardisation of herbal products

**Chromatography** separates the constituents of a mixture by their different distribution between a **stationary phase** and a **mobile phase**. In herbal standardisation it is used for:

1. **Identity** — the fingerprint of the sample matches that of an authentic reference material.
2. **Detection of adulteration and substitution** — extra or missing bands/peaks.
3. **Assay of markers** — quantitative determination of one or more constituents.
4. **Batch consistency** — comparison of fingerprints from batch to batch.
5. **Stability** — change in fingerprint or marker content on storage.
6. **Contaminants** — pesticide residues, residual solvents, aflatoxins.

### Chromatographic fingerprint

A **fingerprint** is a chromatographic pattern of the extractable constituents of a herbal material or product that is characteristic of it. WHO accepts fingerprints as a means of identity and quality assessment when the actives are not fully known. A fingerprint is judged by the **number, position (Rf or retention time), colour and relative intensity** of bands or peaks, not by one compound alone.

### Techniques compared

| Technique | Principle in brief | Uses in herbal QC | Examples |
| --- | --- | --- | --- |
| **Thin-layer chromatography (TLC)** | Adsorption on silica gel layer; Rf = distance moved by the spot ÷ distance moved by the solvent front | Identity, quick screening, limit tests | Identity of senna, liquorice, ashwagandha |
| **High-performance TLC (HPTLC)** | Fine-particle layers, automated sample application, controlled development, derivatisation, densitometric scanning | Fingerprints, assay of markers, many samples in parallel | Withaferin A in ashwagandha, bacosides in brahmi, andrographolide |
| **High-performance liquid chromatography (HPLC)** | Partition between a packed column (often reversed-phase C18) and a pumped liquid; UV/PDA, fluorescence or MS detection | Accurate assay of markers; HPLC fingerprints; aflatoxins | Sennosides, curcuminoids, glycyrrhizin, piperine, silymarin |
| **Gas chromatography (GC)** | Partition between a gas mobile phase and a liquid stationary phase in a heated column; FID, ECD or MS detection | Essential oils, fatty acids, pesticide residues, residual solvents | Eugenol in clove oil, menthol in mint oil |
| **Column chromatography** | Open column of silica or alumina, gravity elution | Isolating marker compounds to use as reference standards | Isolation of andrographolide |
| **Hyphenated techniques** | GC–MS, LC–MS, HPTLC–MS | Identification of unknown peaks, trace contaminants, adulterants | Detecting synthetic drugs added to "herbal" products |

### HPTLC in detail

```text
Sample and standard preparation (extract of fixed strength)
        |
Application as bands on HPTLC silica gel 60 F254 plate (automatic applicator)
        |
Development in a saturated twin-trough chamber (fixed distance)
        |
Drying -> visualisation at 254 nm / 366 nm and after derivatisation
          (anisaldehyde-sulphuric acid, Dragendorff, natural product reagent)
        |
Densitometric scanning -> peak areas and Rf values
        |
Comparison with reference fingerprint; quantification from calibration curve
```

**Advantages of HPTLC for herbals**: many samples and standards on one plate under identical conditions; small solvent use; low cost per sample; visual image plus densitometric data; crude extracts can be applied with simple clean-up; whole fingerprint can be stored as an image for comparison.

### HPLC fingerprints and assay

- Usually reversed-phase C18 with a gradient of water (often acidified) and acetonitrile or methanol.
- **Photodiode array (PDA) detection** records UV spectra of each peak, which helps confirm peak identity and purity.
- For fingerprints, a **reference chromatogram** is set from authentic batches; test batches are compared by the presence of characteristic peaks and their ratios.

### Validation of chromatographic methods (ICH Q2)

| Parameter | What it shows |
| --- | --- |
| Specificity | The method measures the marker without interference from other constituents |
| Linearity and range | Response proportional to concentration over the working range |
| Accuracy | Closeness to the true value (recovery studies) |
| Precision | Repeatability, intermediate precision and reproducibility |
| Detection limit (LOD) | Smallest amount detectable |
| Quantitation limit (LOQ) | Smallest amount measurable with acceptable precision and accuracy |
| Robustness | Unaffected by small deliberate changes (mobile phase ratio, temperature) |

## 4.3 Documents for new drug application and export registration

### Categories of herbal products in India

| Category | Basis of approval | Regulator |
| --- | --- | --- |
| **Classical ASU medicines** | Made exactly as described in the authoritative books listed in the First Schedule of the Drugs and Cosmetics Act; reference to the text is the main evidence | State licensing authority (AYUSH) |
| **Patent or proprietary ASU medicines** | Ingredients from authoritative books, but a new combination or form; evidence of safety and effectiveness needed | State licensing authority, as per Rule 158-B |
| **Phytopharmaceutical drugs** | A purified and standardised fraction of an extract of a medicinal plant, with defined minimum four bioactive or phytochemical compounds assessed qualitatively and quantitatively; treated like a new drug with non-clinical and clinical data | Central Drugs Standard Control Organisation (CDSCO), under the New Drugs and Clinical Trials Rules, 2019 |

### Contents of a herbal new drug dossier

```text
1. Administrative     - application form, fees, manufacturing licence, GMP certificate
2. Identity of plant  - botanical name, family, part used, voucher specimen,
                        geographical source, GACP, authentication certificate
3. Quality (CMC)      - method of extraction (solvent, DER), fractionation,
                        specifications of herb, extract and product,
                        marker assay and fingerprint, validated methods,
                        contaminant tests (heavy metals, pesticides, microbes,
                        aflatoxins, residual solvents), CoA of batches,
                        stability data and proposed shelf life, packaging
4. Non-clinical       - pharmacology, safety pharmacology,
                        acute and repeated-dose toxicity, special toxicity
5. Clinical           - traditional-use evidence, published literature,
                        clinical trial protocols and reports (as required)
6. Labelling          - label, package insert, claims
```

For regulated markets the same information is arranged in **CTD format** (Modules 1–5).

### Export registration

To export herbal products the manufacturer collects:

1. **Manufacturing licence** and product permission.
2. **GMP certificate** — WHO-GMP certification for many importing countries.
3. **Certificate of Pharmaceutical Product (COPP)** under the WHO certification scheme, or a **free sale certificate** showing the product is legally sold in India.
4. **Product dossier** in the format of the importing country — composition, method of manufacture, specifications, certificates of analysis of recent batches, stability data, labels.
5. **Test reports** for heavy metals, pesticide residues, microbial load and aflatoxins. India has made heavy-metal testing compulsory for ASU medicines being exported.
6. **Botanical/phytosanitary certificates** for crude herbs; permission under the **Biological Diversity Act, 2002** where bioresources are used commercially; **CITES** permits for listed species. Export of certain wild-collected plants is restricted by the export policy.
7. Registration with the export promotion council (**Pharmexcil**) and the importer's regulator.

Importing countries classify herbal products differently — for example traditional herbal medicinal products in the EU (Unit 3), dietary supplements or botanical drugs in the USA, natural health products in Canada — and the dossier must match the class chosen.

## 4.4 GMP requirements and Drugs and Cosmetics Act provisions

### The law

ASU drugs are controlled under **Chapter IV-A of the Drugs and Cosmetics Act, 1940** and the ASU provisions of the **Drugs and Cosmetics Rules, 1945**.

| Provision | Content |
| --- | --- |
| **Section 3(a)** | Definition of Ayurvedic, Siddha or Unani drug |
| **Section 33C** | **ASU Drugs Technical Advisory Board (ASU DTAB)** — advises governments on technical matters |
| **Section 33D** | **ASU Drugs Consultative Committee (ASU DCC)** — secures uniform administration of the Act across states |
| **Section 33E** | Misbranded ASU drugs |
| **Section 33EE** | Adulterated ASU drugs |
| **Section 33EEA** | Spurious ASU drugs |
| **Section 33EEC** | Prohibition of manufacture and sale of certain ASU drugs (misbranded, adulterated, spurious, or without licence) |
| **Rule 158-B** | Guidelines for licensing ASU drugs — classical, patent/proprietary — and evidence required |
| **Rule 161** | Labelling of ASU medicines |
| **Rule 161-B** | Shelf life / date of expiry of ASU medicines |
| **Schedule E(1)** | Poisonous substances under ASU systems; products containing them carry a caution to be taken under medical supervision |
| **Schedule T** | Good Manufacturing Practices for ASU medicines |

### Licensing

- A manufacturer applies to the **State Licensing Authority** for a licence to manufacture ASU drugs; the licence is granted after inspection of premises, competent technical staff and compliance with Schedule T.
- Each product is approved separately, supported by the textual reference (classical) or by safety and effectiveness data (proprietary).
- Testing is done in the manufacturer's own laboratory or an approved drug testing laboratory, against the official standards (Ayurvedic, Siddha or Unani Pharmacopoeia of India).

### Labelling (Rule 161) — main particulars

- "Ayurvedic medicine", "Siddha medicine" or "Unani medicine" as applicable.
- Name of the medicine; for proprietary medicines, the ingredients with their quantities.
- Batch number, date of manufacture and date of expiry.
- Manufacturing licence number; name and address of the manufacturer.
- "For external use only" where applicable; caution for Schedule E(1) ingredients.

### GMP requirements (summary)

Schedule T (Unit 2) plus WHO-GMP for export units: suitable premises, clean water, waste disposal, separate stores and quarantine, adequate working space, healthy and trained staff in proper clothing, maintained machinery (Part II lists machinery and minimum area per dosage form), master formula and batch records, distribution and complaint records, and a quality control section. Manufacturers who comply receive a **GMP certificate** from the licensing authority.

## Remember

- Herbal stability = marker assay + fingerprint + physical + microbial + dosage-form tests, in the marketed pack.
- Zones: I 21/45, II 25/60, III 30/35, IVa 30/65, IVb 30/75 (India). Accelerated 40 °C/75% RH for 6 months; sample at 0, 3, 6 months.
- Rule 161-B sets shelf life of ASU medicines.
- Fingerprint = characteristic pattern of bands/peaks (number, position, colour, intensity); Rf = spot distance ÷ solvent-front distance.
- HPTLC: many samples on one plate, derivatisation, densitometry; HPLC: accurate marker assay with PDA; GC: oils, pesticides, residual solvents.
- ICH Q2 validation: specificity, linearity, range, accuracy, precision, LOD, LOQ, robustness.
- Phytopharmaceutical = purified standardised fraction with at least four defined bioactive/phytochemical compounds; regulated by CDSCO under NDCT Rules 2019.
- Export papers: licence, GMP/WHO-GMP, COPP or free sale certificate, dossier, contaminant test reports, botanical/biodiversity/CITES clearances.
- Chapter IV-A: 33C ASU DTAB, 33D ASU DCC, 33E misbranded, 33EE adulterated, 33EEA spurious; Rule 158-B licensing; Schedule E(1) poisonous; Schedule T GMP.
