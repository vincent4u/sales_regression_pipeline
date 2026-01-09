"""
run_pipeline.py
----------------
Orchestrates the Sales Regression Project pipeline.

Pipeline steps:
1. Data ingestion (skipped in CI)
2. ETL / Transformation
3. Analytics / Visualization
4. Machine Learning (Regression)
"""

import subprocess
import sys
import os


def run_script(script_path):
    """Run a Python script and stop pipeline if it fails."""
    print(f"\n=== Running {script_path} ===\n")
    try:
        subprocess.check_call([sys.executable, script_path])
        print(f"\n=== {script_path} completed successfully ===\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        sys.exit(1)


# Detect CI environment
IS_CI = os.getenv("CI", "false").lower() == "true"

# Define pipeline steps
scripts = []

if not IS_CI:
    print("Running FULL pipeline (including data ingestion)")
    scripts.append("scripts/01_data_ingestion.py")
else:
    print("Running CI pipeline (skipping data ingestion)")

scripts.extend([
    "scripts/02_etl_transformation.py",
    "scripts/03_analytics_visualization.py",
    "scripts/04_ml_model.py",
])

# Run pipeline
for script in scripts:
    run_script(script)

print("\n=== Sales Regression Pipeline Completed Successfully ===")
