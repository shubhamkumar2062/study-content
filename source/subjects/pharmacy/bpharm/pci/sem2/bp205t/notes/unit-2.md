# Unit 2: Web technologies and databases

Most drug information today is looked up on web pages and stored in databases. This unit explains how the web works (HTML, XML, CSS, programming languages, web servers and server products) and then how databases store and find data (database concepts, MySQL, MS Access and pharmacy drug databases).

## 2.1 The Internet and the World Wide Web

- **Internet** — a worldwide network of computer networks that exchange data using the TCP/IP set of rules (protocols).
- **World Wide Web (WWW)** — a service on the Internet made of linked documents (web pages) viewed in a **web browser** (Chrome, Firefox, Edge, Safari). It was proposed by Tim Berners-Lee at CERN in 1989.
- **Web page** — one document written in HTML; a **website** is a group of related pages under one domain.
- **URL** (uniform resource locator) — the address of a resource, e.g. `https://www.example.org/drugs/index.html` = protocol + domain name + path.
- **HTTP** (hypertext transfer protocol) — the rule for requesting and sending web pages. **HTTPS** is the secure, encrypted version, needed wherever patient data or passwords are sent.
- **Client–server model** — the browser (client) sends a request; the web server returns the page.

```text
  BROWSER (client)                         WEB SERVER
  user types URL  ── HTTP request ──►  finds the file or runs a program
                                        (may query a database server)
  shows the page  ◄── HTTP response ──  sends HTML, CSS, images, scripts
```

## 2.2 HTML (HyperText Markup Language)

**HTML** is the language used to create the structure and content of web pages. It is a **markup language**, not a programming language: it uses **tags** to mark parts of a document (heading, paragraph, list, table, link, image). The browser reads the tags and displays the page.

**Features**

- Tags are written in angle brackets: `<p>` opens and `</p>` closes. A tag plus its content is an **element**.
- Some tags are empty (no closing tag): `<br>`, `<img>`, `<hr>`.
- Tags can have **attributes** that give extra information: `<a href="page2.html">`, `<img src="tablet.jpg" alt="Tablet">`.
- HTML tags are predefined (fixed) and not case-sensitive. The current version is **HTML5**.
- Files are saved with the extension `.html` or `.htm` and opened in a browser.

**Basic structure of an HTML document**

```text
<!DOCTYPE html>
<html>
  <head>
    <title>Drug Information</title>
  </head>
  <body>
    <h1>Paracetamol</h1>
    <p>Class: <b>Analgesic and antipyretic</b></p>
    <ul>
      <li>Dosage form: tablet</li>
      <li>Store below 25 °C</li>
    </ul>
    <a href="https://www.example.org">More information</a>
  </body>
</html>
```

**Common tags**

| Tag | Use |
| --- | --- |
| `<html>`, `<head>`, `<title>`, `<body>` | Document structure; title appears on the browser tab |
| `<h1>` to `<h6>` | Headings, largest to smallest |
| `<p>`, `<br>`, `<hr>` | Paragraph, line break, horizontal line |
| `<b>`, `<i>`, `<u>` | Bold, italic, underline |
| `<ul>`, `<ol>`, `<li>` | Unordered (bullet) list, ordered (numbered) list, list item |
| `<table>`, `<tr>`, `<th>`, `<td>` | Table, row, header cell, data cell |
| `<a href="">` | Hyperlink |
| `<img src="" alt="">` | Image |
| `<form>`, `<input>`, `<select>`, `<button>` | Forms for entering data |
| `<div>`, `<span>` | Containers used for layout and styling |

## 2.3 XML (eXtensible Markup Language)

**XML** is a markup language designed to **store and carry data** in a form that both people and computers can read. In XML the writer **makes up the tags** to describe the data, so it is "extensible".

```text
<?xml version="1.0" encoding="UTF-8"?>
<drugs>
  <drug id="D001">
    <name>Amoxicillin</name>
    <class>Penicillin antibiotic</class>
    <form>Capsule</form>
    <strength unit="mg">500</strength>
  </drug>
</drugs>
```

**Rules of XML (a "well-formed" document)**

1. There must be exactly one **root element** that contains all others (`<drugs>` above).
2. Every opening tag must have a closing tag.
3. Tags are **case-sensitive** (`<Name>` and `<name>` differ).
4. Elements must be properly nested (close the inner element first).
5. Attribute values must be in quotes.

The structure of an XML document can be fixed with a **DTD** or an **XML Schema (XSD)**; a document that follows it is called **valid**.

**Uses:** exchanging data between different software (for example sending drug data from a database to a website), configuration files, the structured product information files used in regulatory submissions, and exporting Access tables (practical 12).

**HTML vs XML**

| HTML | XML |
| --- | --- |
| Displays data (how it looks) | Stores and carries data (what it is) |
| Tags are predefined | Tags are defined by the user |
| Not case-sensitive | Case-sensitive |
| Browsers tolerate some missing closing tags | Every tag must be closed; strict rules |
| Used for web pages | Used for data exchange and storage |

## 2.4 CSS (Cascading Style Sheets)

**CSS** controls the **presentation** of HTML pages: colours, fonts, sizes, spacing, borders and layout. HTML gives structure; CSS gives style. Keeping style separate means one style sheet can format a whole website, and changing one file changes every page.

**Syntax:** `selector { property: value; }`

```text
h1   { color: navy; font-size: 24px; }
p    { font-family: Arial; line-height: 1.5; }
.warning { color: red; font-weight: bold; }     (a class, used as class="warning")
#header  { background-color: #e0f0ff; }          (an id, used as id="header")
```

**Three ways to add CSS**

| Type | Where | Example |
| --- | --- | --- |
| Inline | In the tag's `style` attribute | `<p style="color:red">` |
| Internal (embedded) | In a `<style>` block inside `<head>` | `<style> p {color:red;} </style>` |
| External | In a separate `.css` file linked to every page | `<link rel="stylesheet" href="style.css">` |

"Cascading" means that when several rules apply to one element, a fixed order of priority decides which one wins (inline beats internal, which beats external, and more specific selectors beat general ones).

## 2.5 Programming languages

A **program** is a set of instructions for a computer; a **programming language** is the set of words and rules used to write it.

| Generation | Type | Features | Examples |
| --- | --- | --- | --- |
| 1st | Machine language | Binary code; runs directly; machine-dependent; hard to write | 10110000 01100001 |
| 2nd | Assembly language | Short codes (mnemonics) like ADD, MOV; needs an **assembler** | Assembly for a given processor |
| 3rd | High-level languages | English-like, machine-independent; need a compiler or interpreter | C, C++, Java, Python, FORTRAN, COBOL |
| 4th | Very high-level / query languages | Say *what* is wanted, not how | SQL, report generators |
| 5th | Logic / constraint languages | Used in expert systems | Prolog |

**Language translators**

- **Assembler** — assembly language to machine code.
- **Compiler** — translates the whole high-level program at once into machine code, then it runs (C, C++).
- **Interpreter** — translates and runs one line at a time (Python, JavaScript); easier to test, usually slower.

**Languages of the web**

- **Client-side** (run in the browser): HTML, CSS, **JavaScript** (makes pages interactive — checking a form before it is sent, showing a drop-down).
- **Server-side** (run on the web server): PHP, Python, Java, C# (ASP.NET), Node.js (JavaScript on the server). They read databases and build pages on request.
- **SQL** talks to the database.

## 2.6 Web servers and server products

A **web server** is a computer, and the software on it, that stores websites and sends pages to browsers in reply to HTTP requests. It runs all the time, has a fixed address and is connected to the Internet (or to a hospital's internal network, an **intranet**).

**Common web server software**

| Product | Notes |
| --- | --- |
| Apache HTTP Server | Free, open-source; long one of the most used servers; often run with Linux, MySQL and PHP (the "LAMP" stack) |
| Nginx | Free, open-source; fast; often used in front of other servers |
| Microsoft IIS (Internet Information Services) | Comes with Windows Server; runs ASP.NET sites |
| Apache Tomcat | Runs Java web applications |

**Server products** are server programs that provide other services on a network:

- **Database servers** — MySQL, Microsoft SQL Server, Oracle Database, PostgreSQL.
- **Application servers** — run the business logic of large programs (hospital information system, ERP).
- **Mail servers** — send and store e-mail (Microsoft Exchange).
- **File and print servers**, **proxy servers** (filter and speed up web access), **DNS servers** (turn domain names into IP addresses).
- **Cloud services** — servers rented over the Internet instead of bought (hosting, storage, databases).

## 2.7 Introduction to databases

- **Database** — an organised collection of related data stored so it can be easily found, added to and changed. Example: a pharmacy's records of drugs, suppliers, patients and sales.
- **DBMS (database management system)** — software that creates and manages databases and controls who can use them. Examples: MySQL, Oracle, Microsoft SQL Server, MS Access.

**Why a database is better than separate files (advantages of a DBMS)**

1. Less **redundancy** (data stored once, not in many registers).
2. **Consistency** — one change updates everywhere.
3. **Data sharing** among many users at once.
4. **Security** — passwords and user rights.
5. **Integrity** — rules stop wrong entries (quantity cannot be negative).
6. Fast **searching and reports** through queries.
7. **Backup and recovery**.

**Database models**

| Model | Structure | Example |
| --- | --- | --- |
| Hierarchical | Tree (one parent, many children) | Early IBM IMS |
| Network | Records linked many-to-many | Older mainframe systems |
| Relational (RDBMS) | Tables with rows and columns, linked by keys | MySQL, Oracle, SQL Server, Access |
| Object-oriented | Data stored as objects | Used for complex data such as images |

**Relational database terms**

| Term | Meaning | Example |
| --- | --- | --- |
| Table (relation) | Data about one subject in rows and columns | `Drug` table |
| Record (row, tuple) | All data about one item | One drug |
| Field (column, attribute) | One kind of data | `DrugName`, `Strength` |
| Data type | Kind of value in a field | Text, number, date, yes/no |
| Primary key | Field that uniquely identifies each record; cannot be blank or repeated | `DrugID` |
| Foreign key | Field in one table that refers to the primary key of another | `SupplierID` in the `Drug` table |
| Relationship | Link between tables | One supplier → many drugs (one-to-many) |

Relationships may be **one-to-one** (patient ↔ medical record number), **one-to-many** (one doctor writes many prescriptions) or **many-to-many** (many patients take many drugs, handled through a linking table such as `Prescription`).

**Normalisation** is splitting data into well-designed tables so each fact is stored once, avoiding repetition and update errors.

```text
SUPPLIER table                      DRUG table
+-------------+-----------+         +--------+------------+----------+-------------+
| SupplierID  | Name      |         | DrugID | DrugName   | Strength | SupplierID  |
|   (PK)      |           |         |  (PK)  |            |          |   (FK)      |
+-------------+-----------+         +--------+------------+----------+-------------+
| S1          | ABC Pharma|  1 ──► M | D1     | Metformin  | 500 mg   | S1          |
|             |           |         | D2     | Amlodipine | 5 mg     | S1          |
+-------------+-----------+         +--------+------------+----------+-------------+
One supplier (S1) supplies many drugs: a one-to-many relationship through SupplierID.
```

## 2.8 SQL (Structured Query Language)

**SQL** is the standard language for working with relational databases.

| Group | Commands | Purpose |
| --- | --- | --- |
| DDL (data definition) | CREATE, ALTER, DROP | Make or change the structure of tables |
| DML (data manipulation) | INSERT, UPDATE, DELETE, SELECT | Add, change, remove and read data |
| DCL (data control) | GRANT, REVOKE | Give or take away permissions |

```text
CREATE TABLE Drug (
   DrugID    INT PRIMARY KEY,
   DrugName  VARCHAR(50),
   Category  VARCHAR(30),
   Stock     INT
);
INSERT INTO Drug VALUES (1, 'Metformin', 'Antidiabetic', 200);
SELECT DrugName, Stock FROM Drug WHERE Stock < 50 ORDER BY DrugName;
UPDATE Drug SET Stock = 180 WHERE DrugID = 1;
DELETE FROM Drug WHERE DrugID = 1;
```

## 2.9 MySQL

**MySQL** is an open-source relational database management system that uses SQL. It is now owned by Oracle Corporation and is free under its community licence.

- Works on the **client–server** model: the MySQL server holds the data; many clients connect at once.
- Runs on Windows, Linux and macOS; fast and reliable for large numbers of records.
- Supports user accounts and permissions, indexes, transactions and backups.
- Widely used behind websites, often with PHP and Apache (LAMP), and through tools such as MySQL Workbench or phpMyAdmin.
- **Pharmacy uses:** online pharmacy websites, hospital and pharmacy management software, drug information portals, storing clinical or laboratory data for many users.

## 2.10 MS Access

**Microsoft Access** is a desktop relational DBMS that is part of Microsoft Office. It suits small offices, pharmacies and student projects. Databases are saved as one file (`.accdb`; older versions `.mdb`).

**Objects of an Access database**

| Object | Use |
| --- | --- |
| Table | Stores the data in rows and columns |
| Query | Asks a question of the data: select, sort, filter, calculate, update or delete records |
| Form | A screen for entering, viewing and editing records one at a time |
| Report | Formatted output for printing (with groups, totals, headings) |
| Macro | A saved series of actions to automate a task |
| Module | Program code written in VBA (Visual Basic for Applications) |

**Common data types in Access:** Short Text, Long Text, Number, Date/Time, Currency, AutoNumber, Yes/No, Attachment, Hyperlink, Lookup.

**Views:** Datasheet view (enter data like a spreadsheet) and Design view (set fields, data types and the primary key). Tools such as the **Table, Form, Report and Label wizards** make objects step by step.

**MySQL vs MS Access**

| MS Access | MySQL |
| --- | --- |
| Desktop database in one file | Client–server database |
| Few users at once; small data | Many users; large data |
| Built-in forms and reports with a graphical interface | Needs other tools or programs for forms and reports |
| Part of Microsoft Office (paid) | Free community edition, open-source |

## 2.11 Pharmacy drug databases

A **drug database** is an organised, searchable collection of information on medicines: names (generic and brand), composition, dosage forms and strengths, indications, dose, contraindications, side effects, interactions, use in pregnancy and lactation, storage, price and manufacturer.

**Uses in pharmacy**

- Answering drug information queries from doctors, nurses and patients.
- Checking prescriptions for drug interactions, duplications and wrong doses.
- Finding substitutes and brands; stock and price lookup at the counter.
- Patient counselling leaflets and labels.
- Research, teaching and pharmacovigilance.

**Examples**

| Database | Type of information |
| --- | --- |
| National Formulary of India (NFI) | Government reference on drugs used in India |
| CIMS and similar Indian drug indexes | Brands, composition, prices and prescribing data for Indian products |
| DrugBank | Drug and drug-target data, chemistry and pharmacology (free for non-commercial use) |
| PubChem (NCBI) | Chemical structures and properties of compounds |
| Micromedex, Lexicomp | Clinical drug references used in hospitals (subscription) |
| MEDLINE / PubMed | Published medical and pharmacy literature |

**Hospital and pharmacy software** keeps its own drug master database, linked to stock, billing and patient records, so that the same drug data are used for dispensing, labelling and reports.

## Remember

- Internet = network of networks; WWW = linked pages on it; URL = address; HTTP/HTTPS = rules for sending pages.
- HTML = structure with predefined tags; XML = data with user-defined, case-sensitive tags and one root element; CSS = style (inline, internal, external).
- Generations of languages: machine → assembly → high-level → 4GL (SQL) → 5GL; compiler translates all at once, interpreter line by line.
- Web servers: Apache, Nginx, IIS, Tomcat; server products include database, application, mail, proxy and DNS servers.
- Database = organised data; DBMS manages it; relational model uses tables, primary keys and foreign keys.
- SQL: DDL (CREATE), DML (INSERT, SELECT, UPDATE, DELETE), DCL (GRANT).
- MS Access objects: tables, queries, forms, reports, macros, modules.
- Drug databases support drug information, prescription checking, counselling and research.
