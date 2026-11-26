# 📊 Retail Sales Analytics Dashboard

An end-to-end Retail Sales Analytics project built using **Python, Pandas, SQL, SQLite, Streamlit and Plotly** to analyze retail transactions, identify business trends and visualize sales performance through an interactive dashboard.

## 🚀 Live Dashboard

**[👉 Open Retail Sales Analytics Dashboard](https://retail-sales-analytics-avbac2pe7rjsgsuqfw4uww.streamlit.app/)**

## 📌 Project Overview

This project analyzes 500 synthetic retail transactions from 2025 to generate meaningful business insights.

The project covers the complete data analytics workflow, including data inspection, data cleaning, database management, SQL analysis, report generation and interactive dashboard development.

The main objective is to understand sales performance, customer behavior, product performance and geographical revenue distribution.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| SQLite | Database management |
| SQL | Business data analysis |
| Streamlit | Interactive dashboard development |
| Plotly | Data visualization |
| Git & GitHub | Version control and project hosting |

## 📊 Dashboard Features

### Key Performance Indicators (KPIs)

- Total Revenue
- Total Orders
- Total Customers
- Units Sold
- Average Order Value

### Interactive Filters

- Date Range Filter
- City Filter
- Sales Channel Filter

### Visualizations

- Monthly Revenue Trends
- Category-wise Sales Performance
- City-wise Revenue Analysis
- Top 10 Products
- Sales Channel Performance
- Repeat Customer Analysis

### Additional Features

- Interactive charts
- Dynamic KPI updates
- CSV report download
- User-friendly dashboard interface

## 🔍 Data Analysis

The project focuses on answering important business questions:

1. What is the total revenue generated?
2. How does revenue change month by month?
3. Which product categories perform best?
4. Which cities generate the highest revenue?
5. Which products contribute most to sales?
6. How do Online and Retail Store channels perform?
7. Who are the repeat customers?

## 🧹 Data Cleaning & Preparation

Data cleaning was performed using Python and Pandas.

Key activities include:

- Checking missing values
- Identifying invalid quantities
- Checking invalid unit prices
- Cleaning and preparing transaction records
- Calculating net sales revenue
- Preparing cleaned data for SQL analysis

**Revenue Calculation:**

`Net Revenue = Quantity × Unit Price × (1 - Discount Percentage)`

## 🗄️ Database & SQL Analysis

SQLite was used to store cleaned retail transaction data.

SQL queries were used for:

- Monthly revenue analysis
- Category performance analysis
- City-wise sales analysis
- Top product identification
- Sales channel comparison
- Repeat customer analysis

## 📁 Project Structure

```text
retail-sales-analytics/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── sales_raw.csv
│   └── sales_clean.csv
│
├── src/
│   └── run_analysis.py
│
├── reports/
│
└── README.md
```

## ▶️ How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Rajat6398/retail-sales-analytics.git
```

### 2. Navigate to Project Directory

```bash
cd retail-sales-analytics
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Data Analysis Pipeline

```bash
python src/run_analysis.py
```

### 6. Launch Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning and preprocessing using Pandas
- Working with databases using SQLite
- Writing SQL queries for business analysis
- Building interactive dashboards using Streamlit
- Creating visualizations using Plotly
- Generating analytical CSV reports
- Managing projects using Git and GitHub
- Deploying applications using Streamlit Community Cloud

## 🎯 Interview Explanation

"I developed an end-to-end Retail Sales Analytics project using Python, Pandas, SQL, SQLite and Streamlit. I started by inspecting and cleaning raw retail transaction data, handled data quality issues, calculated net revenue and stored cleaned records in SQLite. I then performed SQL-based business analysis to identify monthly sales trends, category performance, city-wise revenue, top products and repeat customers. Finally, I developed an interactive dashboard using Streamlit and Plotly with dynamic filters, KPI metrics and CSV download functionality."

## ⚠️ Disclaimer

This project uses **500 synthetic retail transactions** created for educational and portfolio purposes. No real customer information or confidential business data is used.

## 👨‍💻 Author

**Rajat Gupta**

GitHub: [Rajat6398](https://github.com/Rajat6398)

Project Repository: [Retail Sales Analytics](https://github.com/Rajat6398/retail-sales-analytics)

Live Application: [Retail Sales Analytics Dashboard](https://retail-sales-analytics-avbac2pe7rjsgsuqfw4uww.streamlit.app/)
