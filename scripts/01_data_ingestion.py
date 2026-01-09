"""
01_data_ingestion.py
--------------------
Download Superstore dataset from Kaggle and convert Excel to CSV
"""

import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Create raw folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# ------------------ Kaggle Download ------------------
dataset = "juhi1994/superstore"
api = KaggleApi()
api.authenticate()
api.dataset_download_files(dataset, path="data/raw", unzip=True)

# ------------------ Find the Excel file ------------------
raw_files = [f for f in os.listdir("data/raw") if f.endswith(".xls") or f.endswith(".xlsx")]
if not raw_files:
    raise FileNotFoundError("No Excel file found in data/raw after Kaggle download")

excel_path = os.path.join("data/raw", "US Superstore data.xls")  # explicitly use the correct file
print(f"Found Excel file: {excel_path}")

# ------------------ Convert Excel to CSV ------------------
df = pd.read_excel(excel_path)

csv_path = "data/raw/Superstore_Sales.csv"
df.to_csv(csv_path, index=False)

print(f"Excel file converted and saved as CSV: {csv_path}")
print(df.head())
