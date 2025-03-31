from joypy import joyplot
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd


def calculate_percentage_portion(df, group_by_var=None, continuous_var=None, thr=None):
    percentages = {}

    if group_by_var:  # Only group if a variable is provided
        groups = df.groupby(group_by_var, observed=False)
        for name, group in groups:
            count_all = len(group)
            count_above_threshold = (group[continuous_var] > thr).sum()

            percent_above_threshold = (count_above_threshold / count_all) * 100 if count_all > 0 else 0.0
            percentages[name] = percent_above_threshold
    else:
        count_all = len(df)
        count_above_threshold = (df[continuous_var] > thr).sum()
        percentages["All"] = (count_above_threshold / count_all) * 100 if count_all > 0 else 0.0

    return percentages  # Ensure the function returns the dictionary


def percentage_portion_distribution_kde(df, target_variable, grouping_variable=None, threshold=None, grouping_order = None):
    plt.figure(figsize=(10, 6))

    # Filter the order to match actual data present in df
    if grouping_order:
        unique_dating_values = [x for x in grouping_order if x in df[grouping_variable].values]
        df[grouping_variable] = pd.Categorical(df[grouping_variable], categories=unique_dating_values, ordered=True)

    joyplot(
        data=df.groupby(grouping_variable, observed=False), 
        by=grouping_variable if grouping_variable else None, 
        column=target_variable, 
        colormap=cm.coolwarm,
        overlap=0.5,
        alpha=0.6,
        figsize=(10, 6)
    )

    # Calculate percentages above the threshold
    percentages = calculate_percentage_portion(df=df, group_by_var=grouping_variable, continuous_var=target_variable, thr=threshold)

    # Create a legend for the percentages
    handles = [plt.Line2D([0], [0], color='black', lw=4, label=f"{code}: {percent:.1f}%") for code, percent in percentages.items()]

    plt.legend(handles=handles, title=f'Percentage of Observations > {threshold}', loc='upper right', prop={'size': 10})
    
    if threshold is not None:
        plt.axvline(x=threshold, color='green', linestyle='--', linewidth=1)

    # Customize labels and display
    plt.title(f"{target_variable} Distribution")
    plt.xlabel(target_variable)
    plt.show()
