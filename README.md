## African Climate Trend Analysis Challenge – Week 0

### Overview

This project is part of the 10 Academy AI Mastery – Week 0 Challenge, focused on analyzing historical climate data from multiple African countries. The goal is to move from raw, noisy datasets to policy-relevant insights that can support Ethiopia’s strategic positioning in COP32 climate negotiations.

The workflow spans environment setup, data cleaning, exploratory analysis, and cross-country comparison, culminating in a climate vulnerability ranking.

### Objectives

- Build a reproducible data science environment
- Perform robust data profiling, cleaning, and EDA
- Analyze climate trends (temperature, rainfall, humidity)
- Compare countries and identify climate risk patterns
- Generate evidence-based insights for COP32

### Business Context

Climate negotiations increasingly rely on data-backed evidence. This project supports:

- Identification of regional climate trends
- Detection of anomalies and extreme events
- Prioritization of climate finance based on vulnerability

### Environment Setup

**Clone Repository**

git clone https://github.com/RahemetGisho/climate-challenge-week0.git

cd climate-challenge-week0

**Create Virtual Environment**

python -m venv .venv

**Activate Environment**

**Windows:**
.venv\Scripts\activate

**Mac/Linux:**
source .venv/bin/activate

**Install Dependencies**

- pip install -r requirements.txt

### CI/CD Integration

A GitHub Actions workflow ensures:

- Automatic execution on every push to main
- Dependency installation validation
- Reproducibility across environments

### Git Workflow

| Branch            | Purpose                |
| ----------------- | ---------------------- |
| main              | Stable version         |
| setup-task        | Environment & CI setup |
| eda-\*            | Country-level analysis |
| compare-countries | Cross-country analysis |
| dashboard-dev     | Streamlit dashboard    |

- All commits follow Conventional Commits
- Clean and professional version control

## Task 2: Exploratory Data Analysis (EDA)

Each country was analyzed independently using dedicated notebooks.

### Data Preparation & Cleaning

The datasets were structured using pandas, with temporal features engineered from YEAR and DOY into proper datetime formats. Missing values, represented by NASA sentinel -999, were replaced with NaN, and duplicates were removed to ensure data integrity.

Outliers were identified using Z-score analysis, with extreme values carefully evaluated to distinguish genuine climate events from anomalies.

### Analysis Highlights

- Time Series: Monthly temperature & rainfall trends (2015–2026)
- Correlation: Strong relationships among temperature variables, inverse link with humidity
- Distribution: Skewed rainfall patterns and seasonal variability

### Data Policy

- All datasets stored in data/
- Excluded via .gitignore
- No raw/cleaned CSVs committed

## Task 3: Cross-Country Comparison & Vulnerability Ranking

This phase synthesizes all country datasets into a unified analytical framework.

### Data Integration

Cleaned datasets from five countries were combined into a single DataFrame, enabling consistent and direct comparison.

### Temperature Trends

Multi-country time series analysis revealed distinct warming patterns, with summary statistics (mean, median, standard deviation) used to quantify differences.

### Precipitation Variability

Boxplots and statistical summaries highlighted differences in rainfall stability, revealing regions with high variability and climate uncertainty.

### Extreme Climate Events

Climate stress was quantified using:

- Extreme Heat Days → T2M_MAX > 35°C
- Dry Spells → PRECTOTCORR < 1 mm

These indicators reveal the intensity and persistence of climate risk.

### Statistical Validation

A one-way ANOVA test confirmed that temperature differences across countries are statistically significant (p < 0.05), proving that each country represents a distinct climate system.

### Vulnerability Ranking

Countries were ranked based on combined climate stress factors:

- Temperature trends
- Rainfall variability
- Extreme event frequency

This produces a multi-dimensional vulnerability assessment.

### COP32 Insights

**Key findings from the analysis:**

- Some countries face extreme heat and drought pressure
- Others exhibit unstable precipitation patterns
- Ethiopia shows a moderate but sensitive climate profile

_Supports targeted, data-driven climate finance decisions_

### Interactive Dashboard

An interactive dashboard was built using Streamlit.

### Features

- Country multi-select filter
- Year range slider
- Variable selector (T2M, PRECTOTCORR, RH2M)
- Interactive visualizations

### Deployment

Hosted on Streamlit Community Cloud for real-time exploration.

### References

NASA POWER Climate Data
10 Academy Challenge Materials
Pandas Documentation
Seaborn Documentation
