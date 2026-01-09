"""
02_etl_transformation.py
-------------------------
Clean and transform Superstore Sales data
"""

import pandas as pd
import os

# Paths
raw_path = "data/raw/Superstore_Sales.csv"
processed_path = "data/processed/Superstore_Sales_processed.csv"

# Load raw data
df = pd.read_csv(raw_path)

# ----------------- Data Cleaning -----------------
# Drop duplicates
df = df.drop_duplicates()

# Handle missing values (simple approach)
df = df.fillna({
    "Postal Code": 0,
    "Customer ID": "Unknown",
    "Sales": 0,
    "Quantity": 0,
    "Discount": 0,
    "Profit": 0
})

# Convert data types
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Sales"] = df["Sales"].astype(float)
df["Profit"] = df["Profit"].astype(float)
df["Quantity"] = df["Quantity"].astype(int)

# ----------------- Feature Engineering -----------------
# Example: calculate profit margin
df["Profit_Margin"] = df["Profit"] / df["Sales"].replace(0, 1)

# Example: extract year and month
df["Order_Year"] = df["Order Date"].dt.year
df["Order_Month"] = df["Order Date"].dt.month

# Ensure processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Save processed data
df.to_csv(processed_path, index=False)
print(f"Processed data saved to {processed_path}")
