# Climate Challenge Week 0

## Project Setup Guide

Follow these steps to reproduce the development environment.

### 1. Clone the Repository

```bash
git clone https://github.com/RahemetGisho/climate-challenge-week0.git
cd climate-challenge-week0
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Installation

```bash
python --version
```

---

## Project Structure

```
├── .vscode/
├── .github/
│   └── workflows/
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
├── tests/
└── scripts/
```

---

## Notes

- The `data/` folder and `.csv` files are ignored and not included in the repository.
- Make sure your virtual environment is activated before running any scripts.
