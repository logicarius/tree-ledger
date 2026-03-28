"""
Module for analyzing cleaned tree datasets and generating visualizations.
Supports both sample and real municipal datasets via the mode parameter.
"""
import pandas as pd
import matplotlib.pyplot as plt


def identify_low_density_areas(df):
    """
    Identifies wards with below-average tree density.
    These wards are potential priority zones for plantation planning.

    Parameters:
        df (pandas.DataFrame): Cleaned tree dataset with 'ward_name' column

    Returns:
        pandas.Series: Wards with tree counts below the average
    """
    #Count trees per ward
    ward_counts = df["ward_name"].value_counts()

    #Calculate average tree count across all wards
    threshold = ward_counts.mean()

    #Return only wards below average
    return ward_counts[ward_counts < threshold]


def analyze_tree_data(input_path, output_dir, mode="real"):
    """
    Analyzes tree data and generates visualizations.
    Use mode="sample" for prototype testing, mode="real" for municipal dataset.

    Parameters:
        input_path (str): Path to cleaned CSV file
        output_dir (str): Directory to save output plots
        mode (str): "sample" or "real"

    Returns:
        dict: Key analysis results
    """
    #Load cleaned data
    df = pd.read_csv(input_path)

    if mode == "sample":
        #Basic analysis on sample dataset
        trees_per_location = df.groupby("location")["tree_id"].count()

        #Plot
        plt.figure()
        trees_per_location.plot(kind="bar")
        plt.title("Number of Trees per Location")
        plt.xlabel("Location")
        plt.ylabel("Number of Trees")
        plt.tight_layout()

        #Save plot
        plt.savefig(f"{output_dir}/trees_per_location.png")
        plt.close()

        return {"trees_per_location": trees_per_location}

    #--- Real municipal dataset analysis ---

    #1. Tree count per ward
    trees_per_ward = df["ward_name"].value_counts()

    plt.figure(figsize=(10, 5))
    trees_per_ward.head(10).plot(kind="bar")
    plt.title("Top 10 Wards by Tree Count")
    plt.xlabel("Ward Name")
    plt.ylabel("Number of Trees")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/trees_per_ward.png")
    plt.close()

    #2. Most common tree species
    top_species = df["common_name"].value_counts().head(10)

    plt.figure(figsize=(10, 5))
    top_species.plot(kind="bar")
    plt.title("Top 10 Tree Species in Urban Area")
    plt.xlabel("Tree Species")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_species.png")
    plt.close()

    #3. Tree height distribution
    plt.figure(figsize=(8, 5))
    df["height_m"].plot(kind="hist", bins=30)
    plt.title("Distribution of Tree Heights")
    plt.xlabel("Height (meters)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/height_distribution.png")
    plt.close()

    #4. Identify low density wards
    low_density_wards = identify_low_density_areas(df)

    #Return all results
    return {
        "trees_per_ward": trees_per_ward,
        "top_species": top_species,
        "height_summary": df["height_m"].describe(),
        "low_density_wards": low_density_wards,
    }
