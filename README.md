# TreeLedger

TreeLedger cleans and analyses an urban tree census. It takes a raw municipal
dataset, tidies it into a consistent form, and runs basic analysis on how trees are distributed across the city.

I built this solo while learning data cleaning and analysis with Pandas.

## What it does

The code sits in two files in `src/`:

- `data_cleaning.py` cleans the raw CSV: it standardises column names, trims
  text fields, forces numeric columns to be numeric, and drops columns that are not needed.

- `analysis.py` runs the analysis: tree count per ward, the most common species, the height distribution, and a function that lists wards with a below-average tree count.

## Dataset

A municipal urban tree census with 9,623 trees and 25 attributes per tree (e.g. height, girth, canopy diameter, ward, botanical name, and common name). It covers 71 wards and 155 species.

## What the analysis produces

- Tree count per ward, and the top 10 wards by count.
- The most common species across the dataset.
- The height distribution. The median height is 6 m, with a range of 2 m to 24 m.
- A list of wards that sit below the average tree count.

## How to use

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Clean the raw data:
   ```python
   from src.data_cleaning import clean_tree_data
   clean_tree_data(
       "data/raw/urban_tree_census.csv",
       "data/processed/urban_tree_census_cleaned.csv",
   )
   ```
3. Run the analysis:
   ```python
   from src.analysis import analyze_tree_data
   results = analyze_tree_data(
       "data/processed/urban_tree_census_cleaned.csv",
       "outputs/plots",
       mode="real",
   )
   ```
4. List the below-average wards:
   ```python
   from src.analysis import identify_low_density_areas
   import pandas as pd
   df = pd.read_csv("data/processed/urban_tree_census_cleaned.csv")
   print(identify_low_density_areas(df))
   ```
   Plots are saved in `outputs/plots/`.

## Tech stack

Python 3, Pandas, NumPy, Matplotlib, Jupyter.

## Files

```
treeledger/
  data/
    raw/         original datasets
    processed/   cleaned datasets
  notebooks/
    exploration.ipynb
  src/
    data_cleaning.py
    analysis.py
  outputs/plots/  generated plots
  requirements.txt
```
