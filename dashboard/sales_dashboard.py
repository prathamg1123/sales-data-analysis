import pandas as pd
import plotly.express as px
from pathlib import Path

# Load cleaned data

DATA_PATH = Path("../data/processed/amazon_cleaned.csv")

df = pd.read_csv(DATA_PATH)

# Make sure Date is datetime
df["Date"] = pd.to_datetime(df["Date"])


# KPI calculations

total_sales = df["Amount"].sum()
total_orders = df["Order ID"].nunique()


# Category sales

category_sales = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)


# Top products

top_products = (
    df.groupby("SKU")["Qty"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)


# Monthly sales

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Amount"]
    .sum()
    .reset_index()
)

monthly_sales["Date"] = monthly_sales["Date"].astype(str)


# Regional sales

regional_sales = (
    df.groupby("ship-state")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# -----------------------------
# Charts
# -----------------------------

fig_category = px.bar(
    category_sales,
    x="Category",
    y="Amount",
    title="Revenue by Category"
)

fig_monthly = px.line(
    monthly_sales,
    x="Date",
    y="Amount",
    markers=True,
    title="Monthly Sales Trend"
)

fig_region = px.bar(
    regional_sales,
    x="ship-state",
    y="Amount",
    title="Top 10 States by Revenue"
)

fig_products = px.bar(
    top_products,
    x="SKU",
    y="Qty",
    title="Top 10 Best-Selling Products"
)

# -----------------------------
# Dashboard HTML
# -----------------------------

dashboard_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sales Data Analysis Dashboard</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 30px;
        }}

        h1 {{
            text-align: center;
        }}

        .kpis {{
            display: flex;
            gap: 20px;
            justify-content: center;
            margin: 30px 0;
        }}

        .card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            width: 250px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        .card h2 {{
            margin: 0;
            font-size: 28px;
        }}

        .chart {{
            background: white;
            padding: 20px;
            margin: 25px 0;
            border-radius: 10px;
        }}
    </style>
</head>

<body>

<h1>📊 Sales Data Analysis Dashboard</h1>

<div class="kpis">

    <div class="card">
        <h3>Total Sales</h3>
        <h2>₹{total_sales:,.0f}</h2>
    </div>

    <div class="card">
        <h3>Total Orders</h3>
        <h2>{total_orders:,}</h2>
    </div>

</div>

<div class="chart">
    {fig_monthly.to_html(full_html=False, include_plotlyjs="cdn")}
</div>

<div class="chart">
    {fig_category.to_html(full_html=False, include_plotlyjs=False)}
</div>

<div class="chart">
    {fig_region.to_html(full_html=False, include_plotlyjs=False)}
</div>

<div class="chart">
    {fig_products.to_html(full_html=False, include_plotlyjs=False)}
</div>

</body>
</html>
"""

# -----------------------------
# Save dashboard
# -----------------------------

output_path = Path("sales_dashboard.html")

output_path.write_text(
    dashboard_html,
    encoding="utf-8"
)

print(f"Dashboard created successfully: {output_path}")