# TreeLedger 🌳

TreeLedger is a data analysis pipeline for processing and analyzing urban tree census data.

The project demonstrates how raw municipal datasets can be cleaned, structured, and analyzed to extract insights about urban tree distribution, species composition, and environmental patterns.

---

## Results

- Identified top 10 wards with highest tree density
- Detected uneven distribution across wards — several fall below average tree density, indicating potential priority zones for plantation planning
- Found median tree height ~6m, reflecting a predominance of mid-sized urban trees
- Tree girth and canopy diameter show wide variation, reflecting mixed age groups and species diversity

---

## Tech Stack

- Python 3
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Project Structure

```
treeledger/
│
├── data/
│   ├── raw/                        # Original datasets
│   └── processed/                  # Cleaned datasets
│
├── notebooks/
│   └── exploration.ipynb           # Exploratory analysis
│
├── src/
│   ├── data_cleaning.py            # Reusable cleaning pipeline
│   └── analysis.py                 # Analysis and visualization module
│
├── outputs/
│   └── plots/                      # Generated visualizations
│
├── README.md
├── PROBLEM_STATEMENT.md
└── requirements.txt
```

---

## How to Use

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Clean raw data**
```python
from src.data_cleaning import clean_tree_data

clean_tree_data(
    "data/raw/urban_tree_census.csv",
    "data/processed/urban_tree_census_cleaned.csv"
)
```

**3. Run analysis**
```python
from src.analysis import analyze_tree_data

results = analyze_tree_data(
    "data/processed/urban_tree_census_cleaned.csv",
    "outputs/plots",
    mode="real"   # use mode="sample" for the sample dataset
)
```

**4. Identify low-density wards**
```python
from src.analysis import identify_low_density_areas
import pandas as pd

df = pd.read_csv("data/processed/urban_tree_census_cleaned.csv")
priority_wards = identify_low_density_areas(df)
print(priority_wards)
```

Generated plots are saved in `outputs/plots/`.

---

## Key Insight

Several wards fall below average tree density, indicating potential priority zones for plantation planning. The `identify_low_density_areas()` function surfaces these wards directly from the cleaned dataset.

---

## Dataset

Municipal urban tree census — 9,623 records, 25 attributes including tree measurements (height, girth, canopy diameter), location (ward, road), and species information.