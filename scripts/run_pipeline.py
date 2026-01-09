"""
run_pipeline.py
----------------
Orchestrates the full Sales Regression Pipeline:

1. Data ingestion
2. ETL / Transformation
3. Analytics / Visualization
4. Machine Learning (Regression)
"""

import subprocess
import sys

def run_script(script_path):
    """
    Runs a Python script using the current Python interpreter.
    Stops the pipeline if the script fails.
    """
    print(f"\n=== Running {script_path} ===\n")
    try:
        # subprocess.check_call raises CalledProcessError if script fails
        subprocess.check_call([sys.executable, script_path])
        print(f"\n=== {script_path} completed successfully ===\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        sys.exit(1)  # Stop pipeline on error

# List of scripts in order
scripts = [
    "scripts/01_data_ingestion.py",       # Download & save dataset
    "scripts/02_etl_transformation.py",  # Clean & transform data
    "scripts/03_analytics_visualization.py",  # EDA plots
    "scripts/04_ml_model.py"             # Train & save regression model
]

# Run each script sequentially
for script in scripts:
    run_script(script)

print("\n=== Full Sales Regression Pipeline Completed Successfully ===")
