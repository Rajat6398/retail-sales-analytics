from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "sales_raw.csv"
CLEAN_FILE = ROOT / "data" / "sales_clean.csv"

def clean_sales_data() -> pd.DataFrame:
    df = pd.read_csv(RAW_FILE)

    # Standardize text fields and parse dates.
    text_cols = ["customer_id", "product_id", "product_name", "category", "city", "sales_channel"]
    for col in text_cols:
        df[col] = df[col].astype("string").str.strip()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    numeric_cols = ["quantity", "unit_price", "discount_pct"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows that cannot represent a valid sale.
    df = df.dropna(subset=["order_id", "order_date", "customer_id", "product_id",
                           "product_name", "category", "quantity", "unit_price", "discount_pct"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]
    df = df[df["discount_pct"].between(0, 1)]
    df = df.drop_duplicates(subset=["order_id"])

    # Fill missing city values with an explicit category instead of guessing.
    df["city"] = df["city"].fillna("").replace("", "Unknown")

    df["gross_sales"] = df["quantity"] * df["unit_price"]
    df["net_sales"] = (df["gross_sales"] * (1 - df["discount_pct"])).round(2)
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)
    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

    df.to_csv(CLEAN_FILE, index=False)
    return df

if __name__ == "__main__":
    cleaned = clean_sales_data()
    print(f"Cleaned rows: {len(cleaned)}")
    print(f"Saved: {CLEAN_FILE}")
