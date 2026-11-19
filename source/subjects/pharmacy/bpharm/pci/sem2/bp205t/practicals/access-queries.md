# Creating and working with queries in MS Access

**Aim:** To create and use different types of queries in MS Access on a pharmacy database.

## Principle

A **query** asks a question of the data. It can select certain fields and records, sort them, combine related tables, calculate new values, summarise groups, or change data. Access builds queries in **Query Design** (a grid) and stores them as **SQL**. Types:

| Query type | What it does |
| --- | --- |
| Select | Shows chosen fields and records |
| Parameter | Asks the user for a criterion when run |
| Totals (aggregate) | Groups records and calculates Sum, Count, Avg, Min, Max |
| Calculated field | Creates a new column from an expression |
| Crosstab | Summarises data in a row-and-column grid |
| Action — Make-table | Creates a new table from results |
| Action — Append | Adds results to an existing table |
| Action — Update | Changes values in many records |
| Action — Delete | Removes records that meet a criterion |

## Requirements

Computer with MS Access; `Pharmacy.accdb` (Product, Customer, Invoice, InvoiceItem tables) or `DrugInfo.accdb`. Add fields `Stock` (Number) and `ReorderLevel` (Number) to the Product table if absent.

## Procedure

1. **Select query with criteria:** Query Design → Product → ProductName, Stock, ReorderLevel, ExpiryDate. Criteria under Stock: `<[ReorderLevel]` → Run → list of items to reorder. Save `qryReorder`.
2. **Date criterion:** criteria under ExpiryDate: `Between Date() And Date()+90` → items expiring in 90 days. Save `qryNearExpiry`.
3. **Sorting:** set Sort = Ascending under ProductName.
4. **Multiple criteria:** same row = AND; different rows (Or row) = OR. Example: Category "Antibiotic" OR "Antifungal".
5. **Parameter query:** criteria `[Enter category]` under Category.
6. **Calculated field:** `StockValue: [Stock]*[Rate]`.
7. **Totals query:** click **Totals (Σ)**; Group By Category, Sum of StockValue.
8. **Join query:** add Invoice, InvoiceItem and Product (relationships appear) to list each invoice with product names.
9. **Update query (practise on a copy):** Design → Update; Update To for Rate: `[Rate]*1.05` with criterion Category = "Analgesic" → Run → confirm.
10. **Delete query (on a copy):** delete products with ExpiryDate `<Date()`.
11. For each query open **SQL View** and copy the SQL statement, e.g. `SELECT ProductName, Stock FROM Product WHERE Stock < ReorderLevel ORDER BY ProductName;`

## Observations

| Query | Type | Criterion / expression | Records returned |
| --- | --- | --- | --- |
| qryReorder | Select | Stock < ReorderLevel | ___ |
| qryNearExpiry | Select | Between Date() And Date()+90 | ___ |
| qryCategory | Parameter | [Enter category] | ___ |
| qryStockValue | Totals | Sum of [Stock]*[Rate] by Category | ___ |
| qryRateUpdate | Update | Rate × 1.05 | ___ records updated |

## Result

Select, parameter, calculated, totals, join and action queries were created and run on the pharmacy database, and their SQL was noted.

## Precautions

1. Back up the database before running action (update, delete) queries; they cannot be undone.
2. Put text criteria in quotes and dates in `#…#` when typed directly (e.g. `#31/12/2026#`).
3. Check that the tables in a join query are related correctly, or the result multiplies rows.
4. Name queries clearly (prefix `qry`).

## Viva questions

1. **What is a query?** A request to select, combine, calculate or change data in tables.
2. **Name the action queries.** Make-table, append, update and delete.
3. **How are AND and OR written in the design grid?** AND on the same Criteria row; OR on separate rows.
4. **What is a crosstab query?** A summary shown as a grid with row and column headings.
5. **What language does Access use behind queries?** SQL (Structured Query Language).
6. **What does `Between Date() And Date()+90` mean?** Dates from today up to 90 days ahead.
