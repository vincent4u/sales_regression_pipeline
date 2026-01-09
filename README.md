# Sales Regression Pipeline

[![Sales Regression Pipeline CI](https://github.com/vincent4u/sales_regression_pipeline/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vincent4u/sales_regression_pipeline/actions/workflows/ci.yml)


A comprehensive **end-to-end data analytics and machine learning pipeline** utilizing the **Superstore Sales dataset** from Kaggle. This project illustrates the **entire data lifecycle**, encompassing data ingestion, cleaning, visualization, model training, and evaluation.

## Project Overview

This project includes the following key components:

1. **Data Ingestion**  
   Programmatically download and load the dataset from Kaggle.

2. **ETL / Data Transformation**  
   Clean the data, handle missing values, and perform feature engineering.

3. **Exploratory Data Analysis (EDA)**  
   Generate visualizations to explore sales trends and correlations.

4. **Machine Learning**  
   Train a regression model to predict sales and evaluate its performance.

5. **Pipeline Automation**  
   Orchestrate all steps with a single Python script (`run_pipeline.py`) for reproducibility.

## Folder Structure

```
sales_regression_pipeline/
│
├── data/
│   ├── raw/          # Raw dataset downloaded from Kaggle
│   └── processed/    # Cleaned and transformed dataset
│
├── scripts/
│   ├── 01_data_ingestion.py
│   ├── 02_etl_transformation.py
│   ├── 03_analytics_visualization.py
│   ├── 04_ml_model.py
│   └── run_pipeline.py  # Executes the full pipeline in order
│
├── images/            # Generated plots (EDA)
├── models/            # Trained regression model (.pkl)
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Detailed Steps

1. **Data Ingestion**:  
   - Load sales data from CSV (or public dataset API).  
   - Store raw data in `data/raw/`.

2. **ETL / Transformation**:  
   - Clean missing or invalid values.  
   - Perform feature engineering: create features like `Discounted_Sales`, `Revenue_per_Item`, etc.  
   - Store the processed data in `data/processed/`.

3. **Analytics / Visualization**:  
   - Explore data distributions and correlations.  
   - Generate visualizations, such as sales distribution and correlation heatmaps.

4. **Machine Learning**:  
   - Predict `Sales` using features like `Quantity`, `Discount`, `Profit`.  
   - Implement linear regression in `scripts/04_ml_model.py`.  
   - Evaluate the model using MSE and R² metrics.  
   - Save the trained model to `models/`.

5. **CI/CD Automation**:  
   - Use GitHub Actions to automate the execution of all scripts on push.  
   - Ensures reproducibility and workflow integrity.

6. **Version Control**:  
   - All code, scripts, notebooks, processed data, and models are tracked via Git/GitHub.

## Project Setup

### Clone the Repository

```bash
git clone https://github.com/yourusername/sales_regression_project.git
cd sales_regression_project
```

### Install Python Dependencies

```bash
python -m pip install -r requirements.txt
```

**Key packages:**

- `pandas`, `numpy` – Data manipulation.
- `matplotlib`, `seaborn` – Data visualization.
- `scikit-learn` – Machine learning models.
- `kaggle` – Programmatic Kaggle dataset download.
- `xlrd` – Excel `.xls` support.

### Run the Full Pipeline

```bash
python scripts/run_pipeline.py
```

## Kaggle API Setup

1. Create a Kaggle account: [Kaggle].
2. Generate an API token:
   - Go to Account → API → Create New API Token.
   - This downloads `kaggle.json`.
3. Place `kaggle.json` in:
   ```
   C:\Users\<your_username>\.kaggle\kaggle.json
   ```
   Ensure correct permissions for security:
   ```bash
   icacls "C:\Users\<your_username>\.kaggle\kaggle.json" /inheritance:r /grant:r %username%:R
   ```

## License

This project is for educational and portfolio purposes.
