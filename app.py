
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
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    div[data-testid="stMetric"] {
        background-color: rgba(128,128,128,0.08);
        border: 1px solid rgba(128,128,128,0.2);
        padding: 16px;
        border-radius: 10px;
        min-width: 0;
        width: 100%;
    }

    div[data-testid="stMetricValue"] {
        font-size: 1.25rem !important;
        white-space: normal !important;
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
        line-height: 1.4 !important;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 0.9rem !important;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():

    df = pd.read_csv(DATA)

    required_columns = [
        "order_date",
        "net_sales",
        "quantity",
        "order_id",
        "customer_id",
        "city",
        "category",
        "sales_channel",
        "product_name"
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

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
        subset=[
            "order_date",
            "net_sales",
            "quantity",
            "order_id",
            "customer_id"
        ]
    )

    return df


# -----------------------------
# DASHBOARD HEADER
# -----------------------------
st.title("📊 Retail Sales Analytics Dashboard")

st.caption(
    "Business Performance | Interactive Sales Analysis"
)


try:

    df = load_data()

    if df.empty:
        st.warning("No valid sales data found.")
        st.stop()

    # -----------------------------
    # SIDEBAR FILTERS
    # -----------------------------
    st.sidebar.header("Dashboard Filters")

    # Date Filter
    min_date = df["order_date"].min().date()
    max_date = df["order_date"].max().date()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(date_range, (tuple, list)):

        if len(date_range) == 2:
            start_date, end_date = date_range

        elif len(date_range) == 1:
            start_date = end_date = date_range[0]

        else:
            start_date, end_date = min_date, max_date

    else:
        start_date = end_date = date_range

    # City Filter
    cities = ["All"] + sorted(
        df["city"].dropna().unique().tolist()
    )

    selected_city = st.sidebar.selectbox(
        "Select City",
        cities
    )

    # Category Filter
    categories = sorted(
        df["category"].dropna().unique().tolist()
    )

    selected_categories = st.sidebar.multiselect(
        "Select Category",
        categories,
        default=categories
    )

    # Sales Channel Filter
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
    filtered = df[
        (df["order_date"].dt.date >= start_date) &
        (df["order_date"].dt.date <= end_date) &
        (df["sales_channel"].isin(selected_channels)) &
        (df["category"].isin(selected_categories))
    ].copy()

    if selected_city != "All":

        filtered = filtered[
            filtered["city"] == selected_city
        ]

    if filtered.empty:
        st.warning(
            "No sales records match the selected filters."
        )
        st.stop()

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    revenue = filtered["net_sales"].sum()
    orders = filtered["order_id"].nunique()
    customers = filtered["customer_id"].nunique()
    units = filtered["quantity"].sum()

    aov = revenue / orders if orders else 0

    st.subheader("Business Performance Overview")

    # First Row: 3 KPI Cards
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Revenue",
        f"₹{revenue:,.2f}"
    )

    c2.metric(
        "Total Orders",
        f"{orders:,}"
    )

    c3.metric(
        "Customers",
        f"{customers:,}"
    )

    # Second Row: 2 KPI Cards
    c4, c5 = st.columns(2)

    c4.metric(
        "Units Sold",
        f"{units:,.0f}"
    )

    c5.metric(
        "Average Order Value",
        f"₹{aov:,.2f}"
    )

    st.divider()

    # -----------------------------
    # BUSINESS INSIGHTS
    # -----------------------------
    st.subheader("💡 Business Insights")

    city_sales = (
        filtered.groupby("city")["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    category_sales = (
        filtered.groupby("category")["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    product_sales = (
        filtered.groupby("product_name")["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    channel_sales = (
        filtered.groupby("sales_channel")["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    i1, i2 = st.columns(2)

    with i1:

        st.info(
            f"🏙️ **Top City:** {city_sales.index[0]} "
            f"(₹{city_sales.iloc[0]:,.2f})"
        )

        st.info(
            f"📦 **Top Category:** {category_sales.index[0]} "
            f"(₹{category_sales.iloc[0]:,.2f})"
        )

    with i2:

        st.info(
            f"🏆 **Top Product:** {product_sales.index[0]} "
            f"(₹{product_sales.iloc[0]:,.2f})"
        )

        st.info(
            f"🛒 **Top Sales Channel:** {channel_sales.index[0]} "
            f"(₹{channel_sales.iloc[0]:,.2f})"
        )

    st.divider()

    # -----------------------------
    # MONTHLY REVENUE
    # -----------------------------
    st.subheader("📈 Monthly Revenue")

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
        },
        hover_data={
            "net_sales": ":,.2f"
        }
    )

    fig1.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue (₹)",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # -----------------------------
    # CATEGORY AND CITY
    # -----------------------------
    left, right = st.columns(2)

    with left:

        st.subheader("📦 Category Performance")

        category = (
            filtered.groupby("category")["net_sales"]
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            category,
            names="category",
            values="net_sales",
            hole=0.45,
            title="Revenue by Category"
        )

        fig2.update_traces(
            textinfo="percent+label",
            hovertemplate=(
                "%{label}<br>"
                "Revenue: ₹%{value:,.2f}<br>"
                "Share: %{percent}"
                "<extra></extra>"
            )
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    with right:

        st.subheader("🏙️ City Performance")

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
            },
            hover_data={
                "net_sales": ":,.2f"
            }
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    # -----------------------------
    # SALES CHANNEL
    # -----------------------------
    st.subheader("🛒 Sales Channel Performance")

    channel = (
        filtered.groupby("sales_channel")["net_sales"]
        .sum()
        .reset_index()
    )

    fig4 = px.pie(
        channel,
        names="sales_channel",
        values="net_sales",
        hole=0.45,
        title="Online vs Retail Store"
    )

    fig4.update_traces(
        textinfo="percent+label",
        hovertemplate=(
            "%{label}<br>"
            "Revenue: ₹%{value:,.2f}<br>"
            "Share: %{percent}"
            "<extra></extra>"
        )
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # -----------------------------
    # TOP 10 PRODUCTS
    # -----------------------------
    st.subheader("🏆 Top 10 Products")

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
        },
        hover_data={
            "net_sales": ":,.2f"
        }
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    # -----------------------------
    # DOWNLOAD FILTERED DATA
    # -----------------------------
    st.divider()

    st.subheader("📥 Download Sales Report")

    csv_data = filtered.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Filtered Sales CSV",
        data=csv_data,
        file_name="filtered_sales_report.csv",
        mime="text/csv"
    )

    # -----------------------------
    # SALES DATA TABLE
    # -----------------------------
    st.subheader("📋 Sales Data")

    st.caption(
        f"Showing {len(filtered)} filtered records."
    )

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------
    # FOOTER
    # -----------------------------
    st.divider()

    st.caption(
        "Built with Python | Pandas | Streamlit | Plotly"
    )


except Exception as e:

    st.error(f"Dashboard error: {e}")
    st.exception(e)
