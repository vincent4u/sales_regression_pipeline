"""
Run the full Sales Regression Pipeline
--------------------------------------
1. Data ingestion
2. ETL / Transformation
3. Analytics / Visualization
4. Machine Learning
"""

import subprocess
import sys

def run_script(script_path):
    print(f"\n=== Running {script_path} ===\n")
    try:
        subprocess.check_call([sys.executable, script_path])
        print(f"\n=== {script_path} completed successfully ===\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        sys.exit(1)

scripts = [
    "scripts/01_data_ingestion.py",
    "scripts/etl_transformation.py",
    "scripts/03_analytics_visualization.py",
    "scripts/04_ml_model.py"
]

for script in scripts:
    run_script(script)

print("\n=== Full Sales Regression Pipeline Completed Successfully ===")
