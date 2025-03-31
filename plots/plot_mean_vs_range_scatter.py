import matplotlib.pyplot as plt
import seaborn as sns

def plot_mean_vs_range_scatter(df, variable_1, variable_2, grouping_variable):
    # Calculate means and ranges for the specified variables
    mean_per_group_1 = df.groupby(grouping_variable)[variable_1].mean()
    mean_per_group_2 = df.groupby(grouping_variable)[variable_2].mean()
    range_per_site_1 = df.groupby(grouping_variable)[variable_1].agg(["min", "max"])
    range_per_site_2 = df.groupby(grouping_variable)[variable_2].agg(["min", "max"])


    # Calculate error ranges
    error_1 = [mean_per_group_1 - range_per_site_1['min'], range_per_site_1['max'] - mean_per_group_1]
    error_2 = [mean_per_group_2 - range_per_site_2['min'], range_per_site_2['max'] - mean_per_group_2]

    # Generate a unique color for each site
    sites = mean_per_group_1.index
    colors = sns.color_palette("hsv", len(sites))

    # Create the scatter plot with unique colors for each site
    plt.figure(figsize=(12, 8))
    for site, color in zip(sites, colors):
        plt.scatter(mean_per_group_1[site], mean_per_group_2[site], label=site, color=color, s=100)
        plt.errorbar(mean_per_group_1[site], mean_per_group_2[site],
                     xerr=[[error_1[0][site]], [error_1[1][site]]],
                     yerr=[[error_2[0][site]], [error_2[1][site]]],
                     fmt='o', ecolor=color, capsize=5, linestyle='none')  # Use the same color as the point

    # Add labels, title, and legend
    plt.xlabel(f"Mean {variable_1}")
    plt.ylabel(f"Mean {variable_2}")
    plt.title(f"Scatter Plot of Mean {variable_1} vs Mean {variable_2} with Range")
    plt.legend(title="SITE", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()
