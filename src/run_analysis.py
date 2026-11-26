from pathlib import Path
import sqlite3
import pandas as pd
from clean_data import clean_sales_data

ROOT = Path(__file__).resolve().parents[1]
DB_FILE = ROOT / "retail_sales.db"
SQL_DIR = ROOT / "sql"
REPORT_DIR = ROOT / "reports"

def load_to_sqlite(df: pd.DataFrame) -> None:
    with sqlite3.connect(DB_FILE) as conn:
        df.to_sql("orders", conn, if_exists="replace", index=False)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_orders_category ON orders(category)")
        conn.commit()

def export_query(conn, filename: str, query: str) -> None:
    result = pd.read_sql_query(query, conn)
    result.to_csv(REPORT_DIR / filename, index=False)
    print(f"Exported {filename} ({len(result)} rows)")

def run():
    REPORT_DIR.mkdir(exist_ok=True)
    df = clean_sales_data()
    load_to_sqlite(df)

    with sqlite3.connect(DB_FILE) as conn:
        for sql_file in sorted(SQL_DIR.glob("*.sql")):
            query = sql_file.read_text(encoding="utf-8")
            export_query(conn, sql_file.stem + ".csv", query)

    print("\\nPipeline completed.")
    print(f"Clean transactions: {len(df)}")
    print(f"Database: {DB_FILE}")
    print(f"Reports: {REPORT_DIR}")

if __name__ == "__main__":
    run()
