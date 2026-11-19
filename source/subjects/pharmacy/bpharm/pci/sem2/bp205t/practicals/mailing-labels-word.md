# Mailing labels with the label wizard in MS Word

**Aim:** To create mailing labels using the label wizard (Mail Merge) and generate labels in MS Word.

> Menu names are for a recent version of Microsoft Office. In MS Access the same job can be done with **Create → Labels** (Label Wizard).

## Principle

**Mail merge** joins a **main document** (the label layout) with a **data source** (a list of names and addresses in Excel, Access or a Word table). Each record of the data source fills one label, so hundreds of labels are made at once without retyping. **Merge fields** such as «Name» and «Address» mark where data go. In a pharmacy this is used for letters to doctors, address labels for suppliers or patients, and medicine reminder slips.

## Requirements

Computer with MS Word and MS Excel (or Access), label sheets (e.g. A4 sheet with 14 or 21 labels) or plain paper, printer.

## Procedure

1. **Prepare the data source.** In Excel, type column headings in row 1: Title, FirstName, LastName, Address, City, PIN. Enter 8–10 records (doctors or suppliers). Save as `Addresses.xlsx` and close it.
2. Open a new Word document → **Mailings → Start Mail Merge → Labels**.
3. In **Label Options**, choose the printer type, label vendor and product number matching the sheet (or **New Label** to enter the label height, width and number across and down). Click OK; Word shows a grid of blank labels.
4. **Mailings → Select Recipients → Use an Existing List** → choose `Addresses.xlsx` → select the sheet → OK.
5. Optionally **Edit Recipient List** to sort by city or untick records not needed.
6. Click in the first label. Use **Insert Merge Field** (or **Address Block**) to place «Title» «FirstName» «LastName», then press Enter, «Address», Enter, «City» – «PIN». Format the text (font size, bold name).
7. Click **Update Labels** so all labels copy the layout of the first one.
8. Click **Preview Results** to see real names; use the arrows to check each record.
9. **Finish & Merge → Edit Individual Documents → All** to create a new document with all labels; save it as `Labels_Merged.docx`.
10. Print on the label sheet (do a test print on plain paper first and hold it over the label sheet to check alignment).

## Observations

| Item | Detail |
| --- | --- |
| Data source | Addresses.xlsx, ___ records |
| Label size / product | ___ (labels across × down) |
| Merge fields used | Title, FirstName, LastName, Address, City, PIN |
| Labels produced | ___ labels on ___ sheet(s) |

## Result

___ mailing labels were produced from the address list by mail merge using the label wizard in MS Word.

## Precautions

1. Use clear column headings with no blank rows in the data source.
2. Choose the correct label product or measure the label size exactly.
3. Preview before printing; test-print on plain paper.
4. Close the Excel file before connecting it to Word.

## Viva questions

1. **What is mail merge?** Combining a main document with a data source to produce many personalised documents or labels.
2. **What are merge fields?** Placeholders in the main document that are replaced by data from each record.
3. **Name possible data sources.** Excel sheet, Access table or query, Word table, Outlook contacts.
4. **Why use Update Labels?** To copy the layout of the first label to all other labels.
5. **Where is the Label Wizard in Access?** Create → Labels, after selecting a table or query.
6. **One pharmacy use of labels?** Address labels for doctors or suppliers, or patient medicine labels.
