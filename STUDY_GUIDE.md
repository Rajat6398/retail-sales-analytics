# Study Guide: Understand Before You Claim This Project

## Day 1 — Run and inspect
1. Install Python and VS Code.
2. Open this folder in VS Code.
3. Run `pip install -r requirements.txt`.
4. Run `python src/run_analysis.py`.
5. Open `data/sales_raw.csv`, `data/sales_clean.csv`, and each report in Excel.

## Day 2 — Explain the code
Be able to explain:
- What is a CSV file?
- Why do we use Pandas?
- What does `dropna()` do?
- Why remove quantity <= 0 and unit_price <= 0?
- What is a primary key / unique order ID?
- What does `GROUP BY` do?
- Difference between `COUNT(*)` and `COUNT(DISTINCT ...)`.
- How is net sales calculated?
- Why store data in SQLite?

## Practice changes
1. Add a SQL query for revenue by sales channel and month.
2. Find the top 5 cities by number of orders.
3. Change the cleaning rule to remove rows with missing city instead of using "Unknown"; compare row counts.
4. Add a `payment_method` column to the synthetic dataset and analyze it.

## Resume wording (use only after you run and understand it)
Retail Sales Analysis | Python, Pandas, SQL, SQLite
- Built a data-cleaning and analytics pipeline for 500 synthetic retail orders.
- Validated and transformed transaction records, calculated net sales, and loaded cleaned data into SQLite.
- Wrote SQL aggregations for monthly revenue, product/category performance, city trends and customer repeat purchases.
