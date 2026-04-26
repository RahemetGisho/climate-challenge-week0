# African Climate Trend Analysis Challenge – Week 0

## Challenge Overview

This project is part of the 10 Academy AI Mastery Week 0 Challenge, focused on analyzing historical climate data across African countries to extract meaningful insights for COP32 climate discussions.

_The objective is to:_

- Set up a professional data science development environment
- Perform data profiling, cleaning, and exploratory data analysis (EDA)
- Generate insights on climate trends such as temperature, precipitation, and humidity

## Business Context

_The analysis supports climate policy preparation for COP32, where data-driven insights are required to:_

- Identify climate trends and anomalies
- Understand environmental patterns across African regions
- Support evidence-based climate decision-making

## Environment Setup

### 1. Clone the repository

- git clone https://github.com/RahemetGisho/climate-challenge-week0.git

- cd climate-challenge-week0

### 2. Create virtual environment

- python -m venv .venv

### 3. Activate environment

**Windows:** .venv\Scripts\activate

**Mac/Linux:** source .venv/bin/activate

### 4. Install dependencies

- pip install -r requirements.txt

## CI/CD Integration

_A GitHub Actions workflow is configured to:_

- Run on every push to main
- Install project dependencies using:
- pip install -r requirements.txt

This ensures reproducibility and environment consistency.

## Git Workflow

_The project follows a branch-based workflow:_

- main → stable version
- setup-task → environment setup & CI
- eda-kenya → Kenya EDA
- eda-ethiopia → Ethiopia EDA
- eda-sudan → Sudan EDA
- eda-tanzania → Tanzania EDA
- eda-nigeria → Nigeria EDA

_All changes were made using Conventional Commits, such as:_

- init: add gitignore
- chore: setup virtual environment
- ci: add github actions workflow

# Task 2: Exploratory Data Analysis (EDA)

EDA was performed separately for each country using dedicated notebooks.

### Data Preparation

- Loaded dataset using pandas
- Converted YEAR + DOY → datetime
- Extracted Month for seasonal analysis
- Added Country column

### Data Cleaning

- Replaced -999 with NaN (NASA sentinel values)
- Removed duplicate rows
- Handled missing values using:
- Forward-fill for time-series consistency
- Dropping rows with excessive missing data

### Outlier Detection

- Used Z-score method
- Flagged values where |Z| > 3
- Documented decision to retain/remove based on impact

## Analysis Performed

### Time Series Analysis

- Monthly average temperature trends (2015–2026)
- Monthly precipitation patterns
- Identification of seasonal peaks

### Correlation Analysis

- Heatmap of numerical features
- Key relationships:
- Temperature vs Humidity
- Temperature range vs Wind speed

### Distribution Analysis

- Histogram of precipitation
- Bubble chart:
  X: Temperature

Y: Humidity

Size: Precipitation

### Data Handling Policy

- Raw and cleaned datasets are stored in data/ (ignored via .gitignore)
- No CSV files are committed to GitHub

**Key Insights (Example)**

- Strong correlation between temperature variables
- Negative relationship between temperature and humidity
- Rainfall closely linked with atmospheric moisture
- Seasonal patterns clearly visible across months

**How to Run the Analysis**

- Activate environment
- Open Jupyter Notebook:

- jupyter notebook
  Navigate to:
- notebooks/<country>\_eda.ipynb

## References

- NASA POWER Climate Data
- 10 Academy Week 0 Challenge Documents
- Pandas & Seaborn Documentation

## Status

- Task 1: Environment Setup & CI
- Task 2: Data Profiling, Cleaning & EDA
- Task 3: Cross-country comparison (pending)

## Author

**Rahemet Hussen**

**Software Engineering Student At ASTU**
