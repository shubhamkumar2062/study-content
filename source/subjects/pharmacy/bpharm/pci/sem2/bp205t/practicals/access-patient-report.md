# Generating and printing a report from the patient database

**Aim:** To generate a report from the patient database and print it.

## Principle

A **report** is an Access object that presents data from a table or query in a formatted, printable layout, with headings, grouping (for example by diagnosis), sorting, totals and page numbers. Reports are read-only: they display data but do not change it. The **Report Wizard** builds a report step by step; **Design View** and **Layout View** are used to adjust it.

## Requirements

Computer with MS Access and a printer; `Hospital.accdb` with the `Patient` table (at least 10 records).

## Procedure

1. Open `Hospital.accdb` and select the `Patient` table (or a query of it).
2. **Create → Report Wizard** → choose fields: PatientID, PatientName, Gender, DateOfBirth, Diagnosis, AdmissionDate → Next.
3. **Grouping:** add Diagnosis as a grouping level → Next.
4. **Sorting:** sort by PatientName ascending → (Summary Options: Count of records per group if available) → Next.
5. **Layout:** Stepped, orientation Portrait (Landscape if many fields) → Next.
6. Title: `Patient Report` → **Preview the report** → Finish.
7. In **Layout View** or **Design View**, adjust column widths, add the hospital name in the Report Header, and check that the Page Footer shows the date (`=Now()`) and page numbers (`="Page " & [Page] & " of " & [Pages]`).
8. Add a total count in the Report Footer: a text box with `=Count([PatientID])` labelled "Total patients".
9. Save the report. Open **Print Preview**; check margins and page breaks (**Page Setup**).
10. Print (**File → Print** or the Print button in Print Preview). Optionally export as PDF (**External Data → PDF or XPS**).

## Observations

| Report section | Contents |
| --- | --- |
| Report Header | Hospital name, title "Patient Report" |
| Page Header | Column headings |
| Diagnosis Header | Diagnosis name for each group |
| Detail | One line per patient |
| Page Footer | Date and "Page x of y" |
| Report Footer | Total patients = ___ |

## Result

A patient report grouped by diagnosis and sorted by name was prepared from `Hospital.accdb` and printed (___ pages, ___ patients).

## Precautions

1. Choose only the fields needed so the report fits the page.
2. Check Print Preview before printing to save paper.
3. Make sure controls do not overlap the page width, which creates blank pages.
4. Patient reports are confidential; do not leave printouts unattended.

## Viva questions

1. **What is a report?** A formatted, printable presentation of data from a table or query.
2. **Name the sections of a report.** Report header/footer, page header/footer, group header/footer, detail.
3. **Can data be edited in a report?** No, reports only display data.
4. **What is grouping in a report?** Collecting records with the same value (e.g. diagnosis) under one heading, often with subtotals.
5. **How are page numbers added?** With an expression such as `="Page " & [Page] & " of " & [Pages]` in the page footer.
6. **How can a report be shared electronically?** Export it as PDF.
