# 📊 Sales Data Analysis Dashboard

An end-to-end **E-Commerce Sales Data Analysis project** built with Python, Pandas, Matplotlib, and Plotly as part of a Data Analysis Internship.

The project follows the complete data analytics workflow:

**Data → Cleaning → Analysis → Visualization → Dashboard → Business Insights**

---

## 📌 Project Overview

The objective of this project is to analyze an e-commerce sales dataset and identify meaningful patterns in:

- Sales performance
- Product categories
- Top-selling products
- Regional performance
- Monthly sales trends
- Order status
- Fulfilment performance

The final outcome is an interactive **Sales Analysis Dashboard** along with documented analysis and business insights.

---

## 🎯 Objectives

- Understand and inspect the dataset
- Identify and handle data quality issues
- Clean and preprocess the data
- Calculate important sales KPIs
- Analyze sales by category and region
- Identify top-selling products
- Analyze monthly sales trends
- Create meaningful visualizations
- Build an interactive sales dashboard
- Generate actionable business insights

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Plotly | Interactive dashboard visualizations |
| Jupyter Notebook | Analysis and documentation |
| Git & GitHub | Version control and project management |

---

## 📁 Project Structure

```text
sales-data-analysis/
│
├── data/
│   ├── raw/
│   │   └── amazon_dataset.csv
│   │
│   └── processed/
│       └── amazon_cleaned.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda.ipynb
│
├── dashboard/
│   ├── sales_dashboard.py
│   └── sales_dashboard.html
│
├── reports/
│   └── Sales_Data_Analysis_Report.md
│
├── presentation/
│   └── Sales_Data_Analysis_Final_Presentation.pptx
│
├── .gitignore
└── README.md



# Data Analysis Workflow
1. Data Understanding

The dataset was initially inspected using Pandas to understand:

Dataset dimensions
Column names
Data types
Missing values
Statistical characteristics
Unique values

Key Pandas methods used:
df.head()
df.shape
df.columns
df.info()
df.describe()
df.isnull().sum()
df.nunique()


2. Data Cleaning

The following cleaning and preprocessing steps were performed:

Identified missing values
Investigated missing-value patterns
Checked for duplicate records
Converted numerical columns to appropriate data types
Converted the Date column to datetime format
Removed unnecessary columns
Investigated zero-amount transactions
Created a cleaned dataset for analysis

Zero-amount records were investigated rather than blindly deleted. They were retained in the cleaned dataset but excluded from revenue-focused analysis.



3. Exploratory Data Analysis

The analysis focused on the key requirements of the project:

Total sales
Total orders
Average order value
Revenue by category
Regional sales performance
Monthly sales trends
Order status distribution
Fulfilment performance
Top-selling products




📈 Key Performance Indicators
KPI	Result
Total Revenue	₹7.86 Crore
Unique Orders	110,661
Average Revenue per Order	₹710.04
Valid Sales Records	118,806


🏆 Key Findings
1. Top Revenue Category

Set generated the highest revenue at approximately ₹3.92 crore, followed by Kurta at approximately ₹2.13 crore.

2. Top Performing Region

Maharashtra generated the highest regional revenue at approximately ₹1.33 crore, followed by Karnataka at approximately ₹1.05 crore.

3. Monthly Sales Trend

April 2022 was the strongest month in the available dataset, generating approximately ₹2.88 crore in revenue.

4. Order Status

The majority of orders were in the Shipped status, with approximately 76,062 orders, followed by Shipped - Delivered to Buyer with approximately 28,038 orders.

5. Fulfilment Performance

Amazon fulfilment generated approximately ₹5.43 crore from 82,094 orders, compared with approximately ₹2.43 crore from Merchant fulfilment.

6. Top-Selling Product

The best-selling SKU was:

JNE3797-KR-L — 646 units sold

Other variants of the JNE3797 product family also appeared among the top-selling products.

7. Category Demand

Set and Kurta were the two strongest categories by quantity sold, with approximately 44,201 and 44,098 units respectively.



📊 Dashboard

The project includes an interactive HTML dashboard built using Plotly.

Dashboard includes:
💰 Total Sales
🛒 Total Orders
📈 Monthly Sales Trend
🏆 Top-Selling Products
📦 Revenue by Category
📍 Regional Sales

The dashboard is available at:
    dashboard/sales_dashboard.html
    It can be opened directly in a web browser.


📓 Analysis Notebooks
01_data_understanding.ipynb

Initial exploration and understanding of the dataset.

02_data_cleaning.ipynb

Data quality investigation, missing-value handling, preprocessing and cleaning.

03_eda.ipynb

Exploratory data analysis, KPIs, visualizations and business insights.


📄 Project Report

A detailed project report is available in:
    reports/Sales_Data_Analysis_Report.md

The report covers:

Project objectives
Dataset
Data cleaning
Analysis
Visualizations
Dashboard
Business insights
Conclusion









############

🚀 How to Run the Project
1. Clone the repository
git clone https://github.com/prathamg1123/sales-data-analysis.git
2. Navigate to the project
cd sales-data-analysis
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
Windows
.venv\Scripts\activate
5. Install required packages
pip install pandas numpy matplotlib plotly jupyter
6. Run the notebooks
Open Jupyter:
jupyter notebook
Then execute the notebooks in order:

01_data_understanding.ipynb
        ↓
02_data_cleaning.ipynb
        ↓
03_eda.ipynb

7. Generate the dashboard
Navigate to the dashboard directory:
cd dashboard
Run:
python sales_dashboard.py
This generates:
sales_dashboard.html
Open the HTML file in a web browser to view the dashboard.