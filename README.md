# Sales Regression Data Pipeline

**Project Overview:**  
This project demonstrates a **full end-to-end data lifecycle** for a retail sales dataset. It covers **data ingestion, ETL/transformation, analytics, visualization, machine learning (regression), and CI/CD orchestration** — all implemented in Python. The dataset used is the **Superstore Sales dataset**, publicly available and suitable for regression modeling.

---

## **Project Workflow**

Below is a diagram illustrating the full workflow of the project:

![Full Data Lifecycle](images/full_data_lifecycle_diagram.png)

**Workflow Steps:**
sales_regression_pipeline/
│
├── data/
│ ├── raw/ # Raw dataset downloaded from Kaggle
│ └── processed/ # Cleaned and transformed dataset
│
├── scripts/
│ ├── 01_data_ingestion.py
│ ├── 02_etl_transformation.py
│ ├── 03_analytics_visualization.py
│ ├── 04_ml_model.py
│ └── run_pipeline.py # Runs the full pipeline in order
│
├── images/ # Generated plots (EDA)
├── models/ # Trained regression model (.pkl)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

1. **Data Ingestion:**  
   - Load sales data from CSV (or public dataset API)  
   - Store raw data in `data/raw/`  

2. **ETL / Transformation:**  
   - Clean missing or invalid values  
   - Feature engineering: create `Discounted_Sales`, `Revenue_per_Item`, etc.  
   - Store processed data in `data/processed/`  

3. **Analytics / Visualization:**  
   - Explore data distributions, correlations  
   - Generate visualizations such as sales distribution and correlation heatmaps  

4. **Machine Learning:**  
   - Predict `Sales` using features like `Quantity`, `Discount`, `Profit`  
   - Linear regression model implemented in `scripts/04_ml_model.py`  
   - Evaluate model using MSE and R² metrics  
   - Save trained model to `models/`  

5. **CI/CD Automation:**  
   - GitHub Actions workflow executes all scripts automatically on push  
   - Ensures reproducibility and workflow integrity  

6. **Version Control:**  
   - All code, scripts, notebooks, processed data, and models are tracked via Git/GitHub  

---

## **Project Setup**

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/sales_regression_project.git
cd sales_regression_project


---

## **Setup Instructions**

### ** Install Python Dependencies**

```bash
python -m pip install -r requirements.txt


### ** Run the Full Pipeline**
python scripts/run_pipeline.py

