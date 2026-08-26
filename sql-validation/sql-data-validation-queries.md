# SQL — Data Validation Queries

**Data source:** W3Schools sample database (`Customers`, `Orders`, `Employees` tables)
**Tool used:** W3Schools Try SQL Editor — https://www.w3schools.com/sql/trysql.asp
**Author:** Dimuth Anjuka
**Date:** 26 Aug 2026

## Purpose

Practice of core SQL used for data validation and QA work: verifying record counts,
filtering, checking referential integrity across related tables, aggregating data, and
identifying missing/NULL values. Every query below was executed against the live sandbox
and the result recorded is the actual result observed, not an assumed one.

> **Note:** Queries 1–3 and 6 are reconstructed here in their standard form to match the
> results reported during testing. If any line differs from what was actually typed at the
> time, flag it before this is committed — accuracy here matters as much as it did for the
> login test cases.

## 1. Basic retrieval and filtering

### Q1 — Total record count
```sql
SELECT * FROM Customers;
```
**Result:** 91 records
**Validation purpose:** Baseline count check — confirms the expected total number of rows exists before any filtering is applied.

### Q2 — Filter by a specific field value
```sql
SELECT * FROM Customers WHERE Country = 'Germany';
```
**Result:** 11 records
**Validation purpose:** Confirms `WHERE` filtering returns only rows matching the specified condition — the kind of check used to verify a filter/search feature returns the correct subset of data.

### Q3 — Sort order
```sql
SELECT * FROM Customers ORDER BY CustomerName ASC;
```
**Result:** Records returned in alphabetical order by `CustomerName`
**Validation purpose:** Confirms `ORDER BY` produces the expected sort — analogous to verifying a UI "sort A–Z" feature returns data in the correct sequence.

## 2. Joins — relational integrity checks

### Q4 — Matching related records across two tables
```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```
**Result:** 196 rows
**Validation purpose:** Confirms every order successfully links to a customer record via `INNER JOIN`, which only returns rows with a match on both sides.

### Q5 — Orphaned-record check
```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Customers.CustomerID IS NULL;
```
**Result:** 0 records
**Validation purpose:** A `LEFT JOIN` keeps every order even without a matching customer, so filtering for `CustomerID IS NULL` surfaces any order pointing at a customer that doesn't exist. 0 records confirms referential integrity — no orphaned orders in this dataset.

### Q6 — Aggregation across a join
```sql
SELECT Customers.CustomerName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerName
ORDER BY NumberOfOrders DESC;
```
**Result:** 91 rows returned (one per customer); top result: **Ernst Handel — 7 orders**
**Validation purpose:** Confirms `GROUP BY` + `COUNT()` correctly aggregates related records per customer, and `ORDER BY ... DESC` surfaces the highest value first — useful for questions like "which account has the most activity."

## 3. NULL / missing-data checks

### Q7 — Completeness check on a stored field
```sql
SELECT * FROM Customers WHERE PostalCode IS NULL;
```
**Result:** 0 records
**Validation purpose:** Confirms no customer record is missing its postal code. A 0-record result here is itself the correct outcome — it demonstrates the data is complete, not that the query failed.

### Q8 — Verifying NULL handling with a guaranteed NULL-producing query
```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderID IS NULL;
```
**Result:** 17 records — `OrderID` column blank (NULL) for every row
**Validation purpose:** Identifies customers with zero orders (a real business/data question), and demonstrates the mechanics of NULL directly: a `LEFT JOIN` fills unmatched columns with NULL, `IS NULL` (not `= NULL`) is required to detect it, and NULL renders as a blank cell rather than a value like `0` or `""`.

## 4. Lessons learned — schema verification

Two queries in this session initially failed because a column name was assumed rather than confirmed against the actual schema:

| Attempted query | Error | Root cause | Resolution |
|---|---|---|---|
| `SELECT ... FROM Employees WHERE ReportsTo IS NULL;` | `Invalid column name 'ReportsTo'` | This sample `Employees` table has no manager/hierarchy column at all (only `EmployeeID, LastName, FirstName, BirthDate, Photo, Notes`) | Ran `SELECT * FROM Employees;` to inspect the real schema before writing further queries against it |
| `SELECT ... FROM Customers WHERE Region IS NULL;` | `Invalid column name 'Region'` | This sample `Customers` table has no `Region` or `CompanyName` column (only `CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country`) | Ran `SELECT * FROM Customers;` to inspect the real schema, then used the LEFT JOIN approach (Q8) to demonstrate NULL instead |

**Takeaway:** Don't assume a column exists based on a similar dataset seen elsewhere (e.g. the standard Northwind schema) — verify the actual schema with `SELECT *` first. This is the same discipline as checking actual API responses or actual UI behavior rather than assuming expected behavior in any other area of testing.
