"""
03_analytics_visualization.py
-----------------------------
Perform EDA and generate plots
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load processed data
processed_path = "data/processed/Superstore_Sales_processed.csv"
df = pd.read_csv(processed_path)

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

# ----------------- Sales Distribution -----------------
plt.figure(figsize=(8,6))
sns.histplot(df["Sales"], bins=50, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("images/sales_distribution.png")
plt.close()

# ----------------- Profit vs Sales -----------------
plt.figure(figsize=(8,6))
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Profit vs Sales")
plt.savefig("images/profit_vs_sales.png")
plt.close()

# ----------------- Correlation Heatmap -----------------
plt.figure(figsize=(10,8))
numeric_cols = ["Sales", "Quantity", "Discount", "Profit", "Profit_Margin"]
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("images/correlation_heatmap.png")
plt.close()

print("EDA plots saved to 'images/' folder")
