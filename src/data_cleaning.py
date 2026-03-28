"""
Module for cleaning raw tree and environmental datasets.
"""

import pandas as pd 

def clean_tree_data(input_path, output_path):
    
    """
    Cleans raw tree data and saves a processed CSV file.

    Parameters:
        input_path (str): Path to raw CSV file
        output_path (str): Path to save cleaned CSV file

    Returns:
        pandas.DataFrame: Cleaned dataset
    """

    #Load raw data
    df = pd.read_csv(input_path)

    #Standardize column names
    df.columns = df.columns.str.strip().str.lower()


    #Identify text and numeric columns dynamically
    text_cols = df.select_dtypes(include="object").columns
    numeric_cols = df.select_dtypes(include="number").columns

    #Clean text columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    #Ensure numeric columns are numeric
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    #Drop non-essential columns if present
    drop_cols = ["geom", "remarks", "other_remarks"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns])


    #Save cleaned data
    df.to_csv(output_path, index = False)

    return df
