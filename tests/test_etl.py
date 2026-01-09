import pandas as pd
import numpy as np
from scripts import etl_transformation as etl


def test_processed_data_has_no_missing_values():
    """Processed dataset should not contain missing values."""
    df = pd.DataFrame({
        "Order Date": ["2023-01-01", "2023-01-02"],
        "Ship Date": ["2023-01-03", "2023-01-04"],
        "Sales": [100, 200],
        "Quantity": [1, 2],
        "Discount": [0.0, 0.1],
        "Profit": [20, 50],
        "Postal Code": [12345, 54321],
        "Customer ID": ["C001", "C002"]
    })

    processed_df = etl.clean_data(df)
    assert processed_df.isnull().sum().sum() == 0


def test_profit_margin_calculation():
    """Profit margin should be calculated correctly."""
    df = pd.DataFrame({
        "Order Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Ship Date": ["2023-01-02", "2023-01-03", "2023-01-04"],
        "Sales": [100, 200, 0],
        "Profit": [20, 50, 0],
        "Quantity": [1, 2, 3],
        "Discount": [0.0, 0.1, 0.2],
        "Postal Code": [12345, 54321, 11111],
        "Customer ID": ["C001", "C002", "C003"]
    })

    # Step 1: Clean data first
    processed_df = etl.clean_data(df)

    # Step 2: Engineer features
    processed_df = etl.engineer_features(processed_df)

    expected = [0.2, 0.25, 0.0]
    actual = processed_df["Profit_Margin"].values

    import numpy as np
    assert np.allclose(actual, expected)

