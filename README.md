# Retail Sales Analytics Dashboard

An end-to-end Retail Sales Analytics project built using **Python, Pandas, SQL, SQLite, and Streamlit**. This project transforms raw retail transaction data into meaningful business insights through data cleaning, SQL analysis, automated reporting, and an interactive dashboard.

## Project Overview

The project analyzes 500 synthetic retail orders from 2025 to understand sales performance, customer behavior, product performance, and revenue trends.

## Key Features

- Data cleaning and preprocessing using Pandas.
- Data quality checks for missing values and invalid records.
- SQLite database creation and management.
- Business analysis using SQL queries.
- Automated CSV report generation.
- Interactive Streamlit dashboard.
- Dynamic filters for date range, city, and sales channel.
- KPI tracking and sales performance analysis.

## Dashboard KPIs

| Metric | Value |
|---|---:|
| Total Revenue | ₹11,283,446.67 |
| Total Orders | 497 |
| Total Customers | 116 |
| Units Sold | 1,214 |
| Average Order Value | ₹22,703.11 |

## Dashboard Filters

- Date Range
- City
- Sales Channel (Online / Retail Store)

## Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Streamlit
- Git and GitHub

## Project Structure

```text
Retail_Sales_Analysis/
│
├── data/
├── reports/
├── sql/
├── src/
├── app.py
├── retail_sales.db
├── requirements.txt
├── README.md
└── STUDY_GUIDE.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rajat6398/retail-sales-analytics.git
cd retail-sales-analytics
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment (Windows)

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the data analysis pipeline

```bash
python src/run_analysis.py
```

### 6. Launch the interactive dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## SQL Analysis

The project includes analysis of:

- Monthly revenue trends
- Category-wise sales performance
- City-wise revenue
- Top-performing products
- Sales channel performance
- Repeat customers

Revenue is calculated using:

`quantity * unit_price * (1 - discount_pct)`

## Business Insights

The dashboard helps understand:

- Overall revenue and order performance.
- Which cities generate more revenue.
- Which product categories perform better.
- Online versus retail store sales.
- Monthly sales trends.

## Interview Explanation

"I developed an end-to-end retail sales analytics project using Python, Pandas, SQLite, SQL, and Streamlit. I cleaned and transformed raw transaction data, performed SQL-based business analysis, generated automated reports, and developed an interactive dashboard with dynamic filters and KPI metrics to analyze retail sales performance."

## Important Note

This project uses synthetic retail transaction data for educational and portfolio purposes. It does not contain real customer information.

## Author

**Rajat Gupta**

GitHub: [Rajat6398](https://github.com/Rajat6398)

Project Repository: [Retail Sales Analytics](https://github.com/Rajat6398/retail-sales-analytics)