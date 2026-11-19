# Exporting tables, queries, forms and reports to XML

**Aim:** To export tables, queries, forms and reports of an MS Access database to XML and study the files produced.

## Principle

**XML (eXtensible Markup Language)** stores data with user-defined tags, so it can be read by other programs, websites and systems regardless of the software that created it. Access can export:

- **Data (XML)** — the records, with field names as tags;
- **Schema (XSD)** — the structure: fields, data types and keys;
- **Presentation (XSL)** — a style sheet, for forms and reports, that formats the data for display.

The exported files can be imported into another database (External Data → Import → XML File), used in web applications, or exchanged between hospital and laboratory systems.

## Requirements

Computer with MS Access, a browser or text editor (Notepad); a database with the `Drug` table, a query, a form and a report.

## Procedure

1. Select the `Drug` **table** → **External Data → Export → XML File**.
2. Choose folder and name (`Drug.xml`) → OK.
3. In the Export XML box tick **Data (XML)** and **Schema of the data (XSD)** → (More Options to include related tables if needed) → OK.
4. Open `Drug.xml` in a browser or Notepad. Note the structure, for example:

```text
<?xml version="1.0" encoding="UTF-8"?>
<dataroot>
  <Drug>
    <DrugID>1</DrugID>
    <GenericName>Metformin</GenericName>
    <Category>Antidiabetic</Category>
  </Drug>
  ...
</dataroot>
```

5. Open `Drug.xsd` and note the definitions of each field and its data type.
6. Repeat for a **query** (`qryReorder`).
7. Repeat for a **form** and a **report**, this time also ticking **Presentation of your data (XSL)**; note that an `.xsl` file (and for reports an `.htm` file that uses it) is created.
8. To check, create a new blank database and **External Data → New Data Source → From File → XML File** → import `Drug.xml` with structure and data → the table is recreated.

## Observations

| Object | Name | Files created | Root element / record element |
| --- | --- | --- | --- |
| Table | Drug | Drug.xml, Drug.xsd | dataroot / Drug |
| Query | qryReorder | qryReorder.xml, .xsd | dataroot / qryReorder |
| Form | Patient Form | .xml, .xsd, .xsl | ___ |
| Report | Patient Report | .xml, .xsd, .xsl, .htm | ___ |

## Result

A table, a query, a form and a report were exported from MS Access to XML with schema (and presentation) files, and the XML was re-imported successfully into a new database.

## Precautions

1. Tick the schema option if the data are to be imported again with correct data types.
2. Keep the .xml, .xsd and .xsl files of one object together.
3. Avoid spaces and special characters in object and field names, as they become XML tag names.
4. Do not share patient data files outside authorised systems.

## Viva questions

1. **What is XML?** eXtensible Markup Language — a text format for storing and exchanging data with user-defined tags.
2. **What is an XSD file?** An XML Schema that defines the structure and data types of the XML data.
3. **What is an XSL file?** A style sheet that formats XML data for display.
4. **What is the root element in an Access XML export?** `dataroot`.
5. **XML vs HTML export?** HTML is for viewing; XML keeps the data structure for exchange and re-import.
6. **Why is XML useful in pharmacy?** It lets different systems (hospital, laboratory, regulatory) exchange data in a common format.
