# Sales Data Analysis Dashboard
## Internship Mini Project – Data Analysis

### 1. Project Overview

This project focuses on analyzing an e-commerce sales dataset to understand sales performance, customer orders, product demand, regional performance, and sales trends.

The analysis follows the complete data analysis workflow:

**Data → Cleaning → Analysis → Visualization → Dashboard → Business Insights**

---

## 2. Objectives

The main objectives of this project are:

- Understand the sales dataset and its structure.
- Clean and preprocess the dataset.
- Handle missing and invalid values.
- Analyze total sales and total orders.
- Analyze monthly sales trends.
- Identify top-selling products.
- Analyze regional sales performance.
- Create meaningful visualizations.
- Develop a sales analysis dashboard.
- Generate meaningful business insights.

---

## 3. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Jupyter Notebook
- Visual Studio Code
- Git & GitHub

---

## 4. Dataset

The dataset contains e-commerce order information including:

- Order ID
- Date
- Status
- Fulfilment
- Sales Channel
- SKU
- Category
- Quantity
- Amount
- Shipping State
- Promotion information
- Other order-related attributes

The original dataset was stored separately from the cleaned dataset.

---

## 5. Data Cleaning

The following preprocessing steps were performed:

- Inspected the dataset structure and columns.
- Checked data types.
- Identified missing values.
- Converted `Qty` and `Amount` to appropriate numeric types.
- Removed the unnecessary `index` column.
- Investigated records having zero sales amount.
- Removed zero-amount records from the sales analysis dataset.
- Created a cleaned dataset for further analysis.

After cleaning, the analysis dataset contained **118,806 records and 22 columns**.

---

## 6. Key Performance Indicators

### Total Revenue

The total revenue from valid sales was approximately:

**₹7.86 crore**

### Total Orders

The cleaned dataset contained approximately:

**110,661 unique orders**

### Average Revenue per Order

The average revenue per unique order was approximately:

**₹710**

---

## 7. Sales Analysis

### Revenue by Category

The highest-revenue categories were:

1. Set – approximately ₹3.92 crore
2. Kurta – approximately ₹2.13 crore
3. Western Dress – approximately ₹1.12 crore
4. Top – approximately ₹0.53 crore

Set was the largest contributor to overall revenue.

---

## 8. Regional Performance

Maharashtra generated the highest revenue at approximately:

**₹1.33 crore**

Other high-performing states included:

- Karnataka – approximately ₹1.05 crore
- Telangana – approximately ₹0.69 crore
- Uttar Pradesh – approximately ₹0.68 crore
- Tamil Nadu – approximately ₹0.65 crore

---

## 9. Monthly Sales Trend

The analysis covered March to June 2022.

April 2022 was the strongest sales month, generating approximately:

**₹2.88 crore**

Revenue decreased gradually during May and June after reaching the April peak.

---

## 10. Top-Selling Products

The top-selling SKU was:

**JNE3797-KR-L – 646 units**

Other high-performing SKUs included:

- JNE3797-KR-M – 546 units
- JNE3797-KR-S – 495 units
- JNE3405-KR-L – 471 units
- J0230-SKD-M – 453 units

Multiple variants of the JNE3797 product family appeared among the top-selling products.

---

## 11. Fulfilment Analysis

Amazon fulfilment accounted for:

**82,094 orders**

and generated approximately:

**₹5.43 crore**

Merchant fulfilment accounted for:

**36,712 orders**

and generated approximately:

**₹2.43 crore**

Therefore, Amazon fulfilment was the dominant fulfilment method in the dataset.

---

## 12. Order Status Analysis

The most common order status was:

**Shipped – 76,062 orders**

followed by:

**Shipped - Delivered to Buyer – 28,038 orders**

Cancelled orders accounted for:

**10,761 orders**

---

## 13. Dashboard

A Sales Data Analysis Dashboard was created using Python and Plotly.

The dashboard includes:

- Total Sales
- Total Orders
- Monthly Sales Trend
- Revenue by Category
- Regional Sales
- Top 10 Best-Selling Products

The dashboard provides a visual overview of the major sales performance indicators.

---

## 14. Business Insights

### Insight 1 – Strong Overall Sales Performance

The dataset generated approximately ₹7.86 crore in revenue from around 110,661 unique orders.

### Insight 2 – Set is the Leading Revenue Category

Set generated the highest revenue at approximately ₹3.92 crore, followed by kurta at approximately ₹2.13 crore.

### Insight 3 – Maharashtra is the Top-Performing Region

Maharashtra generated the highest regional revenue at approximately ₹1.33 crore.

### Insight 4 – April was the Strongest Sales Month

Revenue peaked in April 2022 at approximately ₹2.88 crore before declining in May and June.

### Insight 5 – Shipped Orders Dominate

The majority of orders were in the Shipped status, with 76,062 orders.

### Insight 6 – Amazon Fulfilment Dominates Revenue

Amazon fulfilment generated approximately ₹5.43 crore, significantly more than Merchant fulfilment.

### Insight 7 – JNE3797 Product Family Shows Strong Demand

JNE3797-KR-L was the best-selling SKU with 646 units, while multiple JNE3797 variants appeared in the top-selling list.

---

## 15. Conclusion

This project demonstrates the complete data analysis workflow, from data cleaning and preprocessing to exploratory analysis, visualization, dashboard development, and business insight generation.

The analysis identifies major revenue categories, high-performing regions, sales trends, fulfilment performance, and top-selling products. The resulting dashboard provides a concise visual representation of the key findings and can support data-driven sales decisions.

---

## 16. Project Files

The final project contains:

- Original Dataset
- Cleaned Dataset
- Data Understanding Notebook
- Data Cleaning Notebook
- EDA Notebook
- Sales Dashboard
- Business Insights
- Project Report
- Final Presentation