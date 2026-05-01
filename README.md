# CI/CD Data Pipeline Project using GitHub Actions, Docker and Python

## Project Overview

This project demonstrates a production-style **CI/CD pipeline for a Python-based retail data processing application**. The goal is to show how a data engineering project can be automatically tested, validated, packaged with Docker, and deployed using GitHub Actions.

This is suitable for a **Junior Data Engineer / Azure Data Engineer / Data Analyst Engineer portfolio** because it covers practical skills recruiters look for: automation, testing, version control, Docker, GitHub Actions, data validation, and deployment readiness.

---

## Business Problem

Retail businesses receive daily sales files from different stores. Before analytics teams can build dashboards, the raw files must be validated, cleaned, transformed, and saved in a reliable format.

Manual execution creates issues such as:

- Repeated human errors
- No automated quality checks
- No standard deployment process
- Difficult rollback and maintenance
- Inconsistent output files

This project solves the problem by building a CI/CD-enabled data pipeline.

---

## Solution

The project uses Python to process retail sales data and GitHub Actions to automate the delivery pipeline.

Whenever code is pushed to GitHub, the CI/CD workflow automatically:

1. Checks out the source code
2. Installs dependencies
3. Runs code quality checks
4. Runs unit tests
5. Executes data validation tests
6. Builds a Docker image
7. Confirms the project is deployment-ready

---

## Architecture

```text
Developer Pushes Code
        |
        v
GitHub Repository
        |
        v
GitHub Actions Workflow
        |
        |-- Install Dependencies
        |-- Run Lint Checks
        |-- Run Unit Tests
        |-- Run Data Quality Tests
        |-- Build Docker Image
        |
        v
Deployment Ready Data Pipeline
```

---

## Tech Stack

| Area | Tools |
|---|---|
| Programming | Python |
| Data Processing | Pandas |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Version Control | Git, GitHub |
| Code Quality | Flake8 |
| Documentation | Markdown |

---

## Folder Structure

```text
cicd-data-pipeline-project/
│
├── .github/workflows/
│   └── ci_cd_pipeline.yml
│
├── config/
│   └── pipeline_config.yml
│
├── data/
│   └── sample_retail_sales.csv
│
├── docs/
│   ├── architecture.md
│   ├── recruiter_project_summary.md
│   └── resume_bullet_points.md
│
├── scripts/
│   └── run_pipeline.sh
│
├── src/
│   ├── data_pipeline.py
│   └── data_quality.py
│
├── tests/
│   ├── test_data_pipeline.py
│   └── test_data_quality.py
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Key Features

- Automated CI/CD workflow using GitHub Actions
- Dockerized Python data pipeline
- Unit testing with Pytest
- Data quality checks for nulls, negative sales, and invalid profit values
- Clean GitHub repository structure
- Recruiter-friendly documentation
- Resume-ready bullet points
- Easy to extend to Azure Data Factory, Databricks, or Azure DevOps

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cicd-data-pipeline-project.git
cd cicd-data-pipeline-project
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
python src/data_pipeline.py
```

### 5. Run tests

```bash
pytest tests/
```

---

## Run with Docker

```bash
docker build -t cicd-data-pipeline .
docker run cicd-data-pipeline
```

---

## CI/CD Workflow

The GitHub Actions workflow is stored in:

```text
.github/workflows/ci_cd_pipeline.yml
```

It runs automatically on:

- Push to `main`
- Pull request to `main`

---

## Sample Output

The pipeline reads sample retail sales data, validates it, calculates total sales and profit by category, and saves a processed output file.

Example output columns:

- Category
- Total Sales
- Total Profit
- Order Count
- Average Discount

---

## GitHub Portfolio Description

**Project Title:** CI/CD Data Pipeline using GitHub Actions, Docker and Python

**Short Description:** Built an automated CI/CD pipeline for a retail data processing project using Python, Pytest, Docker and GitHub Actions. The workflow validates data quality, runs automated tests and builds a Docker image for deployment readiness.

---

## Resume Bullet Points

- Built an automated CI/CD pipeline using GitHub Actions to test, validate and package a Python-based retail data processing application.
- Developed data quality checks to identify null values, negative sales, invalid profit records and duplicate order records before processing.
- Containerized the data pipeline using Docker to ensure consistent execution across local and cloud environments.
- Implemented unit testing with Pytest and code quality checks using Flake8 to improve reliability and maintainability.
- Designed a GitHub-ready project structure with documentation, workflow automation and deployment-ready configuration for recruiter portfolio presentation.

---

## Future Enhancements

- Deploy Docker image to Azure Container Registry
- Trigger Azure Data Factory pipeline after successful GitHub Actions run
- Add Databricks notebook deployment
- Store processed output in Azure Data Lake Gen2
- Add Power BI dashboard integration
- Add notification alerts using Microsoft Teams or Slack

---

## Author

**Sai Teja Vasantha**

Portfolio Project: Junior Data Engineer / Azure Data Engineer / CI/CD Data Pipeline
