
"""
Prototype analysis module used for testing on sample data.

Module for analyzing cleaned tree datasets and generating visualizations.

"""

import pandas as pd
import matplotlib.pyplot as plt

def analyze_tree_data(input_path, output_plot_path):

    """
    Analyzes tree data and saves a bar plot of trees per location.

    Parameters:
        input_path (str): Path to cleaned CSV file
        output_plot_path (str): Path to save plot image

    Returns:
        pandas.Series: Tree count per location
    """

    #Load cleaned data
    df = pd.read_csv(input_path)

    #Basic analysis
    trees_per_location = df.groupby("location")["tree_id"].count()

    #Plot 
    plt.figure()
    trees_per_location.plot(kind="bar")
    plt.title("Number of Trees per Location")
    plt.xlabel("Location")
    plt.ylabel("Number of Trees")
    plt.tight_layout()

    #Save plot
    plt.savefig(output_plot_path)
    plt.close()

    return trees_per_location


