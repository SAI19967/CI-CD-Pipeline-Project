# Architecture Document

## Objective

Build a CI/CD-enabled data pipeline that automatically validates, tests, packages and prepares a retail data processing project for deployment.

## Architecture Flow

```text
Raw Retail CSV
     |
     v
Python Data Pipeline
     |
     |-- Data Cleaning
     |-- Data Validation
     |-- Aggregation
     |
     v
Processed Sales Summary
     |
     v
GitHub Actions CI/CD
     |
     |-- Dependency Installation
     |-- Code Quality Checks
     |-- Unit Tests
     |-- Data Quality Tests
     |-- Docker Build
     |
     v
Deployment Ready Artifact
```

## Main Components

### Source Data
The raw source is a retail sales CSV file containing order, customer, category, sales, profit, discount, region and city information.

### Data Pipeline
The Python pipeline reads raw data, standardizes numeric fields, validates business rules and creates category-level sales summaries.

### Data Quality Layer
Data quality checks validate required columns, null values, negative sales values and discount ranges.

### CI/CD Automation
GitHub Actions runs automated checks every time code is pushed or a pull request is created.

### Docker Packaging
Docker creates a consistent runtime environment for local or cloud deployment.

## Cloud Extension Ideas

This project can be extended to Azure by adding:

- Azure Data Lake Gen2 for file storage
- Azure Container Registry for Docker images
- Azure Data Factory for pipeline orchestration
- Azure Databricks for scalable transformations
- Azure DevOps or GitHub Actions for release pipelines
- Power BI for reporting
