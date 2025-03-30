import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_demographic_composition(df, dating_order):
    # Drop missing values in the "dating" column
    df = df.dropna(subset=["dating"])

    # Filter for specific conditions
    df = df[(df["specimen"] == "enamel") & (df["site"] == "ExampleSite")]

    #df["dating"] = df["dating"].str.replace(r"(?<=LT)(\S)", r" \1", regex=True)

    # Mapping for consistent dating labels
    # dating_mapping = {
    #     "LT B": None,
    #     "LT B1a": "LT B1a",
    #     "LT B1-2a": "LT B1",
    #     "LT B1": "LT B1",
    #     "LT B2a": "LT B2a",
    #     "LT B2b": "LT B2b",
    #     "LT B2a-b": "LT B2b",
    #     "LT B2": "LT B2b",
    #     "LT B2b-C1": "LT B2b-C1",
    #     "LT C1": "LT C1"
    # }

    # Apply mapping and drop any remaining NaN values
    #df["dating"] = df["dating"].replace(dating_mapping)
    df = df.dropna(subset=["dating"])

    # Define the desired order for dating categories

    # Filter the order to match actual data present in df
    unique_dating_values = [x for x in dating_order if x in df["dating"].values]

    # Set bar properties
    bar_width = 0.5
    num_categories = len(unique_dating_values)
    bar_positions = np.arange(num_categories)

    # Create figure
    plt.figure(figsize=(12, 6))
    max_height = 0

    # Loop through dating categories and plot stacked bars
    for i, dating_value in enumerate(unique_dating_values):
        dating_data = df[df['dating'] == dating_value]

        male_a_count = len(dating_data[(dating_data['Sex'] == 'Male') & (dating_data['Class'] == 'A')])
        male_b_count = len(dating_data[(dating_data['Sex'] == 'Male') & (dating_data['Class'] == 'B')])
        female_a_count = len(dating_data[(dating_data['Sex'] == 'Female') & (dating_data['Class'] == 'A')])
        female_b_count = len(dating_data[(dating_data['Sex'] == 'Female') & (dating_data['Class'] == 'B')])
        unknown_a_count = len(dating_data[(dating_data['Sex'].isna()) & (dating_data['Class'] == 'A')])
        unknown_b_count = len(dating_data[(dating_data['Sex'].isna()) & (dating_data['Class'] == 'B')])

        total_height = male_a_count + male_b_count + female_a_count + female_b_count + unknown_a_count + unknown_b_count
        max_height = max(max_height, total_height)

        plt.bar(bar_positions[i], male_a_count, width=bar_width, color='#8dd3c7', edgecolor='black', label='Male A' if i == 0 else "")
        plt.bar(bar_positions[i], male_b_count, bottom=male_a_count, width=bar_width, color='#80b1d3', edgecolor='black', label='Male B' if i == 0 else "")
        plt.bar(bar_positions[i], female_a_count, bottom=male_a_count + male_b_count, width=bar_width, color='#fdb462', edgecolor='black', label='Female A' if i == 0 else "")
        plt.bar(bar_positions[i], female_b_count, bottom=male_a_count + male_b_count + female_a_count, width=bar_width, color='#fb8072', edgecolor='black', label='Female B' if i == 0 else "")
        plt.bar(bar_positions[i], unknown_a_count, bottom=male_a_count + male_b_count + female_a_count + female_b_count, width=bar_width, color='#bebada', edgecolor='black', label='Unknown A' if i == 0 else "")
        plt.bar(bar_positions[i], unknown_b_count, bottom=male_a_count + male_b_count + female_a_count + female_b_count + unknown_a_count, width=bar_width, color='#ccebc5', edgecolor='black', label='Unknown B' if i == 0 else "")

    # Adjust plot limits
    plt.xlim(-0.5, num_categories - 0.5)
    plt.ylim(0, max_height * 1.1)

    # Set labels and title
    plt.title('Demographic Composition of Burial Site Nechvalín')
    plt.xlabel('Dating')
    plt.ylabel('Count')

    # Ensure correct order of X-axis labels
    plt.xticks(ticks=bar_positions, labels=unique_dating_values, rotation=45, ha='right')

    # Grid and legend
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()

    # Show plot
    plt.show()
