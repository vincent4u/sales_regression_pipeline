"""
ETL Transformation Module
-------------------------
Clean and transform Superstore Sales data
"""

import pandas as pd
import os

RAW_PATH = "data/raw/Superstore_Sales.csv"
PROCESSED_PATH = "data/processed/Superstore_Sales_processed.csv"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw Superstore sales data."""
    df = df.copy()
    df = df.drop_duplicates()
    df = df.fillna({
        "Postal Code": 0,
        "Customer ID": "Unknown",
        "Sales": 0,
        "Quantity": 0,
        "Discount": 0,
        "Profit": 0
    })
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Sales"] = df["Sales"].astype(float)
    df["Profit"] = df["Profit"].astype(float)
    df["Quantity"] = df["Quantity"].astype(int)
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create derived features for modeling."""
    df = df.copy()
    df["Profit_Margin"] = df["Profit"] / df["Sales"].replace(0, 1)
    df["Order_Year"] = df["Order Date"].dt.year
    df["Order_Month"] = df["Order Date"].dt.month
    return df


def run_etl():
    """Run full ETL pipeline."""
    df = pd.read_csv(RAW_PATH)
    df = clean_data(df)
    df = engineer_features(df)
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Processed data saved to {PROCESSED_PATH}")


if __name__ == "__main__":
    run_etl()
