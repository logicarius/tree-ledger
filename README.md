# TreeLedger 🌳

TreeLedger is a beginner-friendly environmental data analysis project built using Python.  
It focuses on organizing, cleaning, and analyzing tree and environmental datasets in a structured and reproducible way.

This repository is designed as a learning-oriented prototype that follows real-world project practices.

---

## Objectives

- Learn how to structure a real data analysis project
- Practice data handling with Pandas and NumPy
- Analyze tree and environmental datasets step by step
- Generate meaningful statistics and visualizations
- Build clean, readable, and reusable code

---

## Tech Stack

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

---

## Project Structure

treeledger/
│
├── data/
│   ├── raw/
│   │   └── trees_sample.csv
│   └── processed/
│       └── trees_cleaned.csv
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── data_cleaning.py
│   └── analysis.py
│
├── outputs/
│   └── plots/
│       └── trees_per_location.png
│
├── README.md
├── PROBLEM_STATEMENT.md
└── requirements.txt

---

## How to Use TreeLedger

1. Install dependencies

pip install -r requirements.txt

2. Clean raw data

from data_cleaning import clean_tree_data

clean_tree_data(
    "data/raw/trees_sample.csv",
    "data/processed/trees_cleaned.csv"
)

3. Run analysis

from analysis import analyze_tree_data

analyze_tree_data(
    "data/processed/trees_cleaned.csv",
    "outputs/plots/trees_per_location.png"
)

The generated plot will be saved in the outputs/plots directory.

---

## Current Status

Project completed with:
- Data ingestion
- Data cleaning
- Analysis
- Visualization
- Structured documentation

## Code Organization

- `analysis.py`  
  Used for prototype testing and validation on the sample dataset.

- `analysis_real.py`  
  Contains the final analysis logic applied to the real municipal urban tree census dataset.
