
---

## 🧠 Data Cleaning & Transformation (Python)
Cloud Cost Optimization Dashboard - ETL Pipeline
Author: Ganesh Dhore
Description:
    1. Reads AWS Cost & Usage Report (CUR) data from CSV.
    2. Cleans and standardizes fields.
    3. Aggregates cost and usage by Service, Region, and Date.
    4. Detects top cost drivers and potential savings opportunities.
    5. Outputs a clean dataset for loading into Snowflake or Power BI.
"""

import pandas as pd

# ----------------------------
# STEP 1. LOAD RAW DATA
# ----------------------------
input_path = "data/sample_cur.csv"
df = pd.read_csv(input_path)

print("✅ Data Loaded:", df.shape)
print(df.head())

# ----------------------------
# STEP 2. CLEAN DATA
# ----------------------------
# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Remove invalid or missing records
df = df.dropna(subset=["servicename", "region", "cost"])

# Ensure numeric types
df["cost"] = pd.to_numeric(df["cost"], errors="coerce").fillna(0)
df["usagequantity"] = pd.to_numeric(df["usagequantity"], errors="coerce").fillna(0)

# Convert date
df["usagedate"] = pd.to_datetime(df["usagedate"], errors="coerce")

# ----------------------------
# STEP 3. AGGREGATE DATA
# ----------------------------
# Aggregate total cost & usage by service, region, and date
agg = (
    df.groupby(["usagedate", "servicename", "region"])
      .agg(total_cost=("cost", "sum"), total_usage=("usagequantity", "sum"))
      .reset_index()
)

# ----------------------------
# STEP 4. ANALYZE TRENDS
# ----------------------------
# Top services by cost (for insight generation)
top_services = (
    agg.groupby("servicename")["total_cost"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n💰 Top 5 Services by Cost:\n", top_services)

# ----------------------------
# STEP 5. DETECT ANOMALIES
# ----------------------------
# Detect high-cost spikes (3x average threshold)
mean_cost = agg["total_cost"].mean()
spike_threshold = 3 * mean_cost
anomalies = agg[agg["total_cost"] > spike_threshold]

print(f"\n⚠️ Found {len(anomalies)} potential cost spikes (>{spike_threshold:.2f})")

# ----------------------------
# STEP 6. OUTPUT CLEAN DATA
# ----------------------------
output_path = "data/cleaned_cost_data.csv"
agg.to_csv(output_path, index=False)

print(f"\n✅ ETL complete! Clean data saved to: {output_path}")
