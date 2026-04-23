# African Climate Trend Analysis Challenge – Week 0

## Overview

This repository contains the setup and initial configuration for the Week 0 Climate Challenge. The goal is to establish a reproducible development environment, version control workflow, and basic CI pipeline before working with data.

## Environment Setup

Follow the steps below to reproduce the development environment.

### 1. Clone the Repository

```bash
git clone https://github.com/RahemetGisho/climate-challenge-week0.git
cd climate-challenge-week0
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Setup

```bash
python --version
pip list
```

## Project Structure

```
├── .vscode/                 # Editor configuration
├── .github/
│   └── workflows/          # CI workflows
├── .gitignore              # Ignored files and folders
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── src/                    # Source code
├── notebooks/              # Jupyter notebooks
├── tests/                  # Test files
└── scripts/                # Utility scripts
```

## Continuous Integration (CI)

A GitHub Actions workflow is configured to run on every push to the `main` branch. The pipeline installs project dependencies to ensure the environment is correctly set up.

## Notes

- The `data/` directory and all `.csv` files are excluded from version control.
- The virtual environment (`venv/`) is not tracked.
- Ensure the virtual environment is activated before installing dependencies or running code.
