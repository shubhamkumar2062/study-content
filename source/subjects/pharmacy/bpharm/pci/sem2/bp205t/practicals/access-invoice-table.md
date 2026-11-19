# Invoice table in MS Access

**Aim:** To create an invoice table using MS Access and calculate invoice amounts.

## Principle

An **invoice** (bill) records a sale or purchase: invoice number, date, customer, items, quantity, rate, discount, tax and total. In a relational database the invoice is split into related tables so that each fact is stored once: a `Customer` table, a `Product` (drug) table, an `Invoice` table (one row per bill) and an `InvoiceItem` table (one row per item on a bill). **Relationships** link them through primary and foreign keys, and a **query** calculates amounts. **Referential integrity** stops an invoice line pointing to a drug that does not exist.

## Requirements

Computer with MS Access; a new database `Pharmacy.accdb`.

## Procedure

1. Create the database `Pharmacy.accdb`.
2. Create the tables in Design View:

| Table | Fields (data type) | Primary key |
| --- | --- | --- |
| Customer | CustomerID (AutoNumber), CustomerName (Short Text), Phone (Short Text) | CustomerID |
| Product | ProductID (Short Text), ProductName (Short Text), BatchNo (Short Text), ExpiryDate (Date/Time), Rate (Currency), GSTRate (Number, e.g. 0.12) | ProductID |
| Invoice | InvoiceNo (AutoNumber), InvoiceDate (Date/Time, default Date()), CustomerID (Number) | InvoiceNo |
| InvoiceItem | ItemID (AutoNumber), InvoiceNo (Number), ProductID (Short Text), Quantity (Number), Discount (Number, %) | ItemID |

3. **Database Tools → Relationships**: add all four tables. Drag Customer.CustomerID to Invoice.CustomerID, Invoice.InvoiceNo to InvoiceItem.InvoiceNo, Product.ProductID to InvoiceItem.ProductID. Tick **Enforce Referential Integrity** for each (one-to-many). Save.
4. Enter 5 customers, 8 products and 3 invoices with 2–4 items each.
5. Create a query (**Create → Query Design**) with InvoiceItem and Product; add InvoiceNo, ProductName, Quantity, Rate, Discount, GSTRate and calculated fields:
   - `Amount: [Quantity]*[Rate]`
   - `AfterDiscount: [Amount]*(1-[Discount]/100)`
   - `GST: [AfterDiscount]*[GSTRate]`
   - `LineTotal: [AfterDiscount]+[GST]`
6. Run the query and save it as `qryInvoiceLines`.
7. Create a **Totals** query on `qryInvoiceLines` grouped by InvoiceNo with `Sum` of LineTotal to get each invoice total.
8. Optionally make a report from these queries to print the invoice.

## Observations / calculations

**Formula:** Line total = Quantity × Rate × (1 − Discount/100) × (1 + GST rate)

**Worked example (one line):** 10 strips × ₹30 = ₹300; discount 5% → ₹285; GST 12% = ₹34.20; line total = **₹319.20**.

| InvoiceNo | Product | Qty | Rate (₹) | Disc % | GST % | Line total (₹) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | |
| 1 | | | | | | |
| 2 | | | | | | |

Invoice totals: Invoice 1 = ₹___, Invoice 2 = ₹___, Invoice 3 = ₹___.

## Result

Related tables for invoicing were created in MS Access, and invoice line totals and invoice totals were calculated by queries.

## Precautions

1. Use Currency data type for money and store rates, not totals, in tables (totals are calculated).
2. Enforce referential integrity so invoice lines always point to valid invoices and products.
3. Enter GST and discount in the agreed form (fraction or percentage) consistently.
4. Check expiry date before billing.

## Viva questions

1. **Why are invoices stored in two tables (Invoice and InvoiceItem)?** One invoice has many items; splitting avoids repeating invoice details on every line.
2. **What is referential integrity?** A rule that a foreign key value must match an existing primary key in the related table.
3. **What is a calculated field?** A field in a query computed from other fields, e.g. Amount: [Quantity]*[Rate].
4. **Which data type is used for money?** Currency.
5. **What is a totals query?** A query that groups records and calculates Sum, Count, Average, etc.
6. **What type of relationship is Invoice to InvoiceItem?** One-to-many.
