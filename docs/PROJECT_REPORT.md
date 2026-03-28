# PROJECT REPORT  
## TreeLedger: Urban Tree Census Data Analysis

---

## 1. Introduction

Urban trees play a crucial role in maintaining environmental balance, improving air quality, and enhancing the quality of life in cities. Managing and understanding large-scale urban tree data is essential for informed decision-making in urban planning and environmental conservation.

The **TreeLedger** project was developed to design a structured and reproducible data analysis pipeline for tree and environmental datasets. The project demonstrates how raw municipal tree census data can be cleaned, analyzed, and visualized using Python-based data science tools.

The project was first implemented using a small sample dataset to validate the pipeline and was later extended to analyze a real municipal urban tree census dataset containing over **9,600 tree records**.

---

## 2. Objectives

The main objectives of the TreeLedger project are:

- To design a clean and reusable data analysis pipeline  
- To preprocess and clean raw tree census data  
- To analyze urban tree distribution and characteristics  
- To generate meaningful visual insights from real-world data  
- To follow industry-style project structure and documentation practices  

---

## 3. Tools and Technologies Used

The project was implemented using the following tools and technologies:

- **Python 3** – core programming language  
- **Pandas** – data manipulation and analysis  
- **NumPy** – numerical operations  
- **Matplotlib** – data visualization  
- **Jupyter Notebook** – exploratory data analysis  
- **VS Code** – development environment  

---

## 4. Dataset Description

Two datasets were used in this project:

### Sample Dataset  
A small CSV dataset created for testing and validating the data pipeline.

### Real Urban Tree Census Dataset  
A municipal-level dataset containing **9,623 records** and **25 attributes**, including:

- Tree measurements (height, girth, canopy diameter)  
- Location information (ward, road, society)  
- Species information (common name, botanical name)  
- Ecological and administrative attributes  

The real dataset represents actual urban tree census data and required careful inspection and cleaning before analysis.

---

## 5. Methodology

The project followed a structured data analysis workflow:

### 5.1 Data Loading
Raw datasets were loaded into Pandas DataFrames from the `data/raw` directory.

### 5.2 Initial Data Inspection
The structure, data types, size, and missing values were examined using functions such as:

- `.info()`  
- `.columns`  
- `.shape`  
- `.describe()`  

### 5.3 Data Cleaning
A reusable data cleaning function was implemented to:

- Standardize column names  
- Remove unnecessary whitespace  
- Ensure numeric consistency  
- Export cleaned data to `data/processed`  

The same cleaning pipeline was successfully applied to both sample and real datasets.

### 5.4 Data Analysis
Exploratory and statistical analysis was performed on the cleaned dataset to:

- Count trees across different wards  
- Identify the most common tree species  
- Analyze tree size distribution  

### 5.5 Visualization
Visualizations were generated and saved as image files, including:

- Tree count per ward  
- Top tree species  
- Tree height distribution  

---

## 6. Results and Observations

Key findings from the analysis include:

- The dataset contains a diverse range of tree species across multiple wards.  
- Certain wards have significantly higher tree counts than others.  
- The median tree height is approximately **6 meters**, indicating a predominance of mid-sized urban trees.  
- Tree girth and canopy diameter show wide variation, reflecting mixed age groups and species diversity.  

These observations provide valuable insights into urban tree distribution and structure.

---

## 7. Conclusion

The TreeLedger project successfully demonstrated how a structured data pipeline can be applied to real-world environmental datasets. By extending the analysis from a sample dataset to a large municipal tree census, the project highlights the importance of data inspection, cleaning, and reproducible analysis.

The project serves as a strong foundation for future extensions such as geospatial analysis, predictive modeling, or integration with environmental planning systems.

---

## 8. Future Scope

Possible future enhancements include:

- Geospatial visualization using GIS data  
- Time-series analysis of tree growth  
- Machine learning models for tree health prediction  
- Integration with air quality or climate datasets  
