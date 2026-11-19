# Drug information storage and retrieval using MS Access

**Aim:** To store drug information in an MS Access database and retrieve it using sorting, filtering, queries and a search form.

## Principle

A **drug information database** stores facts about medicines in structured fields so that they can be found quickly. Retrieval is done by **Find**, **Sort**, **Filter** and **queries**. A **parameter query** asks the user for a value (such as a drug name) each time it runs, so one query answers many questions. Wildcards (`*`) with **Like** allow partial-name searches.

## Requirements

Computer with MS Access; reference books or a reliable drug database to collect correct information on 15–20 drugs.

## Procedure

1. Create a database `DrugInfo.accdb` and a table `Drug` in Design View:

| Field | Data type |
| --- | --- |
| DrugID | AutoNumber (primary key) |
| GenericName | Short Text |
| BrandName | Short Text |
| Category | Short Text (lookup: Antibiotic, Antidiabetic, Antihypertensive, Analgesic, …) |
| DosageForm | Short Text |
| Strength | Short Text |
| Indications | Long Text |
| AdultDose | Short Text |
| SideEffects | Long Text |
| Contraindications | Long Text |
| Interactions | Long Text |
| Storage | Short Text |
| Schedule | Short Text (e.g. H, H1, OTC) |

2. Enter information for 15–20 drugs from reliable references.
3. **Simple retrieval:** open the table; use **Find** (Ctrl + F) for a brand name; **sort** by GenericName; **Filter by Selection** on Category = Antibiotic.
4. **Select query:** Query Design → `Drug` → GenericName, Category, AdultDose; criteria under Category: `"Antidiabetic"` → Run → save as `qryAntidiabetic`.
5. **Parameter query:** criteria under GenericName: `Like "*" & [Enter drug name or part of it] & "*"` → Run → type "metf" → Metformin record appears. Save as `qrySearchDrug`.
6. **Search in side effects:** criteria under SideEffects: `Like "*" & [Enter side effect] & "*"` to list all drugs causing, e.g., "dizziness".
7. Create a form on `qrySearchDrug` (Form Wizard, Columnar) so a user can search and view complete information.
8. Note the number of records returned for each search.

## Observations

| Retrieval method | Criterion | Records found |
| --- | --- | --- |
| Find | Brand name "___" | 1 |
| Filter | Category = Antibiotic | ___ |
| Select query | Category = Antidiabetic | ___ |
| Parameter query | Name contains "___" | ___ |
| Side-effect search | "___" | ___ |

## Result

A drug information database of ___ drugs was created in MS Access, and information was retrieved by find, filter, select and parameter queries.

## Precautions

1. Enter information only from reliable, current references; record the source.
2. Use consistent spelling of generic names (one standard name).
3. Use Long Text for descriptive fields; keep categories in a lookup list for uniform entries.
4. Review and update the data periodically.

## Viva questions

1. **What is a parameter query?** A query that asks for a value each time it runs and uses it as the criterion.
2. **What does `Like "*metf*"` find?** Any value containing "metf" anywhere.
3. **Filter vs query?** A filter temporarily limits the records shown; a query is saved and can be reused, joined and calculated.
4. **Why use a lookup field for Category?** To give a fixed list of choices and avoid spelling variations.
5. **Name two advantages of an electronic drug information database.** Fast searching by many fields; easy updating and sharing.
