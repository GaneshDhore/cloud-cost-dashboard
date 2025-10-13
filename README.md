# ☁️ Cloud Cost Optimization Dashboard

## 📌 Overview
This project analyzes and visualizes **AWS cloud cost and usage data** to identify cost-saving opportunities.  
It demonstrates a complete **data pipeline** — from raw data in AWS S3 to actionable insights in Power BI —  
integrating **Python, Snowflake, SQL, and visualization** to deliver automated, reliable financial analytics.

---

## 🎯 Objectives
- Centralize scattered AWS billing data into a structured Snowflake warehouse.  
- Clean, transform, and validate datasets using Python.  
- Build a Power BI dashboard for cost trend analysis and service-level optimization.  
- Automate monthly updates and ensure data consistency for financial reporting.

---

## 🔄 Data Pipeline

AWS S3 (Raw CUR Data)
↓
Python (pandas for cleaning & ETL)
↓
Snowflake (Data Modeling & Storage)
↓
Power BI (Visualization & Reporting)


---

## ⚙️ Tools & Technologies
| Category | Tools Used |
|-----------|-------------|
| **Data Source** | AWS S3 (Cost & Usage Reports - CUR) |
| **ETL / Transformation** | Python, Pandas, NumPy |
| **Data Warehouse** | Snowflake (staging, warehouse, and marts schema) |
| **Visualization** | Power BI |
| **Version Control** | Git & GitHub |
| **Languages** | SQL, Python |

---
🚀 Key Results

Improved dashboard refresh speed by 4× using Snowflake instead of direct S3 connections.

Identified 15–20% potential cost reduction by visualizing unused EC2 & EBS resources.

Automated monthly updates using Python scripts and Power BI scheduled refresh.

🧩 Key Learnings

Importance of separating storage (AWS S3) from analytics (Snowflake).

How to use Python for reproducible ETL workflows.

Experience building reliable pipelines that handle both scale and transparency.

🔗 Future Enhancements

Integrate dbt for transformation automation.

Add Airflow for scheduling ETL tasks.

Extend dashboard to include cost forecasting using time series models in Python.

