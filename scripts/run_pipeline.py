"""
run_pipeline.py
----------------
Orchestrates the full Sales Regression Project pipeline:
1. Data ingestion
2. ETL / Transformation
3. Analytics / Visualization
4. Machine Learning (Regression)
"""

import subprocess
import sys

def run_script(script_path):
    """Run a Python script and stop pipeline if it fails."""
    print(f"\n=== Running {script_path} ===\n")
    try:
        subprocess.check_call([sys.executable, script_path])
        print(f"\n=== {script_path} completed successfully ===\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        sys.exit(1)

# List all scripts in order
scripts = [
    "scripts/01_data_ingestion.py",
    "scripts/02_etl_transformation.py",
    "scripts/03_analytics_visualization.py",
    "scripts/04_ml_model.py"
]

# Run each script
for script in scripts:
    run_script(script)

print("\n=== Full Sales Regression Pipeline Completed Successfully ===")