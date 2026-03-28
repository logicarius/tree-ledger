# VIVA QUESTIONS AND ANSWERS  
## Project: TreeLedger – Urban Tree Census Data Analysis

---

## 1. What is the TreeLedger project about?

TreeLedger is a data analysis project designed to process, clean, analyze, and visualize urban tree census data. The project demonstrates a structured Python-based data pipeline that converts raw municipal tree data into meaningful insights about tree distribution, species composition, and physical characteristics.

---

## 2. Why did you choose this project?

I chose this project because urban tree data is a real-world environmental dataset with practical relevance. It allowed me to apply data science concepts such as data cleaning, exploratory analysis, and visualization on a realistic dataset rather than a toy example.

---

## 3. What datasets were used in this project?

Two datasets were used:
1. A small sample CSV dataset for prototype testing and pipeline validation.  
2. A real municipal urban tree census dataset containing over 9,600 records and 25 attributes.

---

## 4. Why did you use a sample dataset first?

The sample dataset was used to test and validate the data pipeline in a controlled environment. Once the pipeline worked correctly, it was extended to handle the real municipal dataset. This approach reduces errors and ensures reproducibility.

---

## 5. Explain the folder structure of your project.

The project follows an industry-style structure:
- `data/raw` stores original datasets  
- `data/processed` stores cleaned datasets  
- `src` contains reusable Python scripts  
- `notebooks` is used for exploratory analysis  
- `outputs/plots` stores generated visualizations  

This separation improves clarity, maintainability, and scalability.

---

## 6. What is the purpose of `data_cleaning.py`?

`data_cleaning.py` contains a reusable function that standardizes column names, cleans text fields, ensures numeric consistency, removes unnecessary columns, and saves the cleaned data. It allows the same cleaning logic to be applied to different datasets.

---

## 7. Why did you dynamically detect text and numeric columns?

Real-world datasets often have different schemas, so hardcoding column names is unreliable. Dynamically detecting text and numeric columns makes the cleaning function flexible and robust across datasets.

---

## 8. What is exploratory data analysis (EDA)?

Exploratory Data Analysis is the process of understanding a dataset’s structure, quality, and patterns using summary statistics and visualizations before applying further analysis or modeling.

---

## 9. What steps were involved in data inspection?

The data inspection included:
- Checking column names and data types  
- Examining dataset size using `.shape()`  
- Identifying missing values  
- Analyzing summary statistics using `.describe()`

---

## 10. Why is data cleaning important?

Data cleaning ensures consistency, correctness, and reliability. Without proper cleaning, analysis results can be misleading due to incorrect data types, inconsistent naming, or missing values.

---

## 11. What analysis did you perform on the cleaned data?

The analysis included:
- Tree count per ward  
- Identification of the most common tree species  
- Analysis of tree size distribution using height, girth, and canopy diameter  

---

## 12. What does the median tree height indicate?

The median tree height of approximately 6 meters indicates that most urban trees are mid-sized. Median is preferred over mean because it is less affected by extreme values.

---

## 13. What are percentiles (25%, 50%, 75%)?

Percentiles divide the dataset into parts:
- 25%: one-quarter of values lie below this  
- 50%: the median  
- 75%: three-quarters of values lie below this  

They describe the distribution of data rather than just the average.

---

## 14. What visualizations did you generate?

The project generated:
- Bar plots for tree count per ward  
- Bar plots for top tree species  
- Histogram for tree height distribution  

All plots were saved as image files.

---

## 15. Why did you save plots instead of only displaying them?

Saving plots makes the analysis reproducible and allows results to be reused in reports, presentations, or dashboards without rerunning the notebook.

---

## 16. Why did you separate `analysis.py` and `analysis_real.py`?

`analysis.py` was used for prototype testing on the sample dataset, while `analysis_real.py` contains the final analysis logic for the real municipal urban tree census dataset. This separation maintains clarity between testing and production-level analysis.

---

## 17. What challenges did you face during the project?

Key challenges included handling schema differences between datasets, resolving module import issues, and ensuring that code changes were reflected correctly after kernel restarts.

---

## 18. How did you ensure reproducibility?

Reproducibility was ensured by using modular scripts, saving cleaned datasets and plots, maintaining a consistent folder structure, and documenting all steps clearly.

---

## 19. What are the limitations of your project?

The project is limited to descriptive analysis and does not include predictive modeling, time-series analysis, or geospatial visualization.

---

## 20. What is the future scope of this project?

Future enhancements include:
- Geospatial analysis using GIS data  
- Time-series analysis of tree growth  
- Machine learning models for tree health prediction  
- Integration with air quality or climate datasets  

---
