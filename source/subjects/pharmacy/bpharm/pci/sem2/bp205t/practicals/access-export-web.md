# Exporting tables, queries, forms and reports to web pages

**Aim:** To export tables, queries, forms and reports of an MS Access database to web pages (HTML) and view them in a browser.

## Principle

**Exporting** copies data out of Access into another format. Exporting to an **HTML document** creates a web page containing the data as an HTML table (for tables, queries and forms) or the formatted pages of a report, which any browser can open without Access. This is used to share lists (drug catalogue, stock list) on an intranet or website. The page is a **static** snapshot: later changes in the database do not appear until it is exported again.

## Requirements

Computer with MS Access and a web browser; `Hospital.accdb`, `DrugInfo.accdb` or `Pharmacy.accdb` with tables, queries, forms and reports.

## Procedure

1. Open the database. In the Navigation Pane select the `Drug` (or `Patient`) **table**.
2. **External Data → Export → More → HTML Document**.
3. Choose the destination folder and file name (`Drug.html`). Tick **Export data with formatting and layout** and **Open the destination file after the export operation is complete** → OK.
4. Choose encoding (Default or Unicode UTF-8) → OK. The page opens in the browser as an HTML table.
5. Repeat for a **query** (`qryReorder` → `qryReorder.html`).
6. Repeat for a **form** (`Patient Form`); the form's data are exported as a table.
7. Repeat for a **report** (`Patient Report`); each report page becomes an HTML page with navigation links (First, Previous, Next, Last).
8. Open each file in the browser; right-click → **View page source** to see the HTML tags (`<table>`, `<tr>`, `<td>`).
9. Save the export steps if offered, so the export can be repeated with one click (**External Data → Saved Exports**).

## Observations

| Object exported | Object name | HTML file created | Appearance in browser |
| --- | --- | --- | --- |
| Table | Drug | Drug.html | HTML table of all records |
| Query | qryReorder | qryReorder.html | Table of items below reorder level |
| Form | Patient Form | Patient Form.html | Data as a table |
| Report | Patient Report | Patient Report.html (+ further pages) | Formatted report pages with navigation |

## Result

A table, a query, a form and a report were exported from MS Access as HTML web pages and viewed in a web browser.

## Precautions

1. Export only the fields that are meant to be shared; never publish confidential patient data on public web pages.
2. Re-export after updating data, as exported pages are not live.
3. Keep exported files together in one folder (reports create several linked pages).
4. Use UTF-8 encoding if data contain special characters.

## Viva questions

1. **What does exporting mean?** Copying data or objects from Access into another format or program.
2. **Is an exported HTML page updated automatically?** No, it is a static snapshot.
3. **Which HTML tags hold an exported table?** `<table>`, `<tr>` (row), `<th>` (heading) and `<td>` (cell).
4. **How do you see the HTML code of a page?** Right-click → View page source.
5. **Give one pharmacy use.** Publishing a drug catalogue or price list on the hospital intranet.
