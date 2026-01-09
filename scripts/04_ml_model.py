"""
04_ml_model.py
---------------
Train a simple regression model to predict Sales
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Load processed data
processed_path = "data/processed/Superstore_Sales_processed.csv"
df = pd.read_csv(processed_path)

# Features and target
features = ["Quantity", "Discount", "Profit", "Profit_Margin", "Order_Year", "Order_Month"]
target = "Sales"

X = df[features]
y = df[target]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model Evaluation:\nMSE: {mse:.2f}\nR2 Score: {r2:.2f}")

# Save model
os.makedirs("models", exist_ok=True)
model_path = "models/sales_regression_model.pkl"
joblib.dump(model, model_path)
print(f"Trained model saved to {model_path}")
