# Retail Sales Analysis (Python + Pandas + SQLite)

A beginner-friendly portfolio project that cleans retail transaction data, stores it in SQLite,
runs business SQL queries, and exports summary reports.

## Project features
- 500 synthetic retail orders (2025); no real customer data.
- Data-quality checks for missing values, invalid quantity and invalid unit price.
- Cleaning with Pandas.
- SQLite database creation and loading.
- SQL analysis: revenue by month, category, city, sales channel, top products and repeat customers.
- CSV report exports.

## Requirements
- Python 3.10+
- Packages listed in `requirements.txt`

## Run in VS Code / terminal
```bash
# 1. Create and activate a virtual environment (optional but recommended)
python -m venv .venv

# Windows PowerShell:
.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pipeline
python src/run_analysis.py
```

The script creates `retail_sales.db` and writes CSV summaries into `reports/`.

## Database tables
`orders` contains cleaned transactions. Revenue is calculated as:
`quantity * unit_price * (1 - discount_pct)`.

## Suggested interview explanation
"I built a small end-to-end retail analytics workflow. I inspected raw CSV data, handled missing
and invalid records, calculated net sales, loaded the cleaned data into SQLite, and used SQL
aggregations to identify monthly trends, category performance, city performance and top products."

## Important
This is a learning project using synthetic data. Before adding it to a resume, run it yourself,
understand each file, verify the output, and be ready to explain your design decisions.
