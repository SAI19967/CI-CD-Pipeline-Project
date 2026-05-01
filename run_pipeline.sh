#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running tests..."
pytest tests/ -v

echo "Running data pipeline..."
python src/data_pipeline.py

echo "Pipeline completed successfully."
