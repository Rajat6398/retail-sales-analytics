
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sales_clean.csv"

st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(DATA)

    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )
    df["net_sales"] = pd.to_numeric(
        df["net_sales"], errors="coerce"
    )
    df["quantity"] = pd.to_numeric(
        df["quantity"], errors="coerce"
    )

    df = df.dropna(
        subset=["order_date", "net_sales", "quantity"]
    )

    return df


st.title("📊 Retail Sales Analytics Dashboard")
st.caption("Business Performance | Interactive Sales Analysis")

try:
    df = load_data()

    if df.empty:
        st.warning("No valid sales data found.")
        st.stop()

    # -----------------------------
    # SIDEBAR FILTERS
    # -----------------------------
    st.sidebar.header("Dashboard Filters")

    min_date = df["order_date"].min().date()
    max_date = df["order_date"].max().date()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    cities = ["All"] + sorted(
        df["city"].dropna().unique().tolist()
    )

    selected_city = st.sidebar.selectbox(
        "Select City", cities
    )

    channels = sorted(
        df["sales_channel"].dropna().unique().tolist()
    )

    selected_channels = st.sidebar.multiselect(
        "Select Sales Channel",
        channels,
        default=channels
    )

    # -----------------------------
    # APPLY FILTERS
    # -----------------------------
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = date_range
        end_date = date_range

    filtered = df[
        (df["order_date"].dt.date >= start_date) &
        (df["order_date"].dt.date <= end_date) &
        (df["sales_channel"].isin(selected_channels))
    ].copy()

    if selected_city != "All":
        filtered = filtered[
            filtered["city"] == selected_city
        ]

    if filtered.empty:
        st.warning("No sales records match the selected filters.")
        st.stop()

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    revenue = filtered["net_sales"].sum()
    orders = filtered["order_id"].nunique()
    customers = filtered["customer_id"].nunique()
    units = filtered["quantity"].sum()

    st.subheader("Business Performance Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Revenue", f"₹{revenue:,.2f}")
    c2.metric("Total Orders", f"{orders:,}")
    c3.metric("Customers", f"{customers:,}")
    c4.metric("Units Sold", f"{units:,.0f}")

    st.divider()

    # -----------------------------
    # MONTHLY REVENUE
    # -----------------------------
    st.subheader("Monthly Revenue")

    monthly = (
        filtered.groupby(
            filtered["order_date"].dt.to_period("M")
        )["net_sales"]
        .sum()
        .reset_index()
    )

    monthly["Month"] = monthly["order_date"].astype(str)

    fig1 = px.bar(
        monthly,
        x="Month",
        y="net_sales",
        text_auto=".2s",
        title="Revenue by Month",
        labels={
            "Month": "Month",
            "net_sales": "Revenue (₹)"
        }
    )

    st.plotly_chart(fig1, use_container_width=True)

    # -----------------------------
    # CATEGORY AND CITY
    # -----------------------------
    left, right = st.columns(2)

    with left:
        st.subheader("Category Performance")

        category = (
            filtered.groupby("category")["net_sales"]
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            category,
            names="category",
            values="net_sales",
            hole=0.4,
            title="Revenue by Category"
        )

        st.plotly_chart(fig2, use_container_width=True)

    with right:
        st.subheader("City Performance")

        city = (
            filtered.groupby("city")["net_sales"]
            .sum()
            .reset_index()
            .sort_values("net_sales")
        )

        fig3 = px.bar(
            city,
            x="net_sales",
            y="city",
            orientation="h",
            title="Revenue by City",
            labels={
                "city": "City",
                "net_sales": "Revenue (₹)"
            }
        )

        st.plotly_chart(fig3, use_container_width=True)

    # -----------------------------
    # SALES CHANNEL
    # -----------------------------
    st.subheader("Sales Channel Performance")

    channel = (
        filtered.groupby("sales_channel")["net_sales"]
        .sum()
        .reset_index()
    )

    fig4 = px.pie(
        channel,
        names="sales_channel",
        values="net_sales",
        hole=0.4,
        title="Online vs Retail Store"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # -----------------------------
    # TOP 10 PRODUCTS
    # -----------------------------
    st.subheader("Top 10 Products")

    products = (
        filtered.groupby("product_name")["net_sales"]
        .sum()
        .nlargest(10)
        .reset_index()
        .sort_values("net_sales", ascending=True)
    )

    fig5 = px.bar(
        products,
        x="net_sales",
        y="product_name",
        orientation="h",
        text_auto=".2s",
        title="Top Products by Revenue",
        labels={
            "product_name": "Product",
            "net_sales": "Revenue (₹)"
        }
    )

    st.plotly_chart(fig5, use_container_width=True)

    # -----------------------------
    # DOWNLOAD FILTERED DATA
    # -----------------------------
    st.divider()
    st.subheader("Download Sales Report")

    csv_data = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Sales CSV",
        data=csv_data,
        file_name="filtered_sales_report.csv",
        mime="text/csv"
    )

    # -----------------------------
    # SALES DATA TABLE
    # -----------------------------
    st.subheader("Sales Data")

    st.caption(f"Showing {len(filtered)} filtered records.")

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Built with Python | Pandas | Streamlit | Plotly"
    )

except Exception as e:
    st.error(f"Dashboard error: {e}")
    st.exception(e)
