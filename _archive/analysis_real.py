"""
Final analysis module for the real municipal urban tree census dataset.


Module for analyzing urban tree census data and generating visual insights.

This module performs descriptive analysis on a cleaned urban tree dataset
and saves plots that summarize tree distribution and characteristics.

"""

import pandas as pd
import matplotlib.pyplot as plt


def analyze_real_tree_data(input_path, output_dir):
    """
    Analyzes cleaned urban tree census data and generates visual outputs.

    The analysis includes:
    1. Tree count per ward
    2. Most common tree species
    3. Distribution of tree heights

    Parameters:
        input_path (str): Path to the cleaned CSV file
        output_dir (str): Directory where output plots will be saved

    Returns:
        dict: A dictionary containing key analysis results
    """


    # Load cleaned dataset

    df = pd.read_csv(input_path)


    # 1. Analyze tree distribution across wards----

    # Count number of trees in each ward
    trees_per_ward = df["ward_name"].value_counts()

    # Plot top 10 wards by tree count
    plt.figure(figsize=(10, 5))
    trees_per_ward.head(10).plot(kind="bar")
    plt.title("Top 10 Wards by Tree Count")
    plt.xlabel("Ward Name")
    plt.ylabel("Number of Trees")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/trees_per_ward.png")
    plt.close()


    # 2. Identify most common tree species----

    # Count occurrences of each species
    top_species = df["common_name"].value_counts().head(10)

    # Plot top 10 species
    plt.figure(figsize=(10, 5))
    top_species.plot(kind="bar")
    plt.title("Top 10 Tree Species in Urban Area")
    plt.xlabel("Tree Species")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_species.png")
    plt.close()


    # 3. Analyze height distribution of trees----

    plt.figure(figsize=(8, 5))
    df["height_m"].plot(kind="hist", bins=30)
    plt.title("Distribution of Tree Heights")
    plt.xlabel("Height (meters)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/height_distribution.png")
    plt.close()


    # Return key results for further use or inspection

    return {
        "trees_per_ward": trees_per_ward,
        "top_species": top_species,
        "height_summary": df["height_m"].describe()
    }
