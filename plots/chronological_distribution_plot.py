import matplotlib.pyplot as plt
import matplotlib as mpl

def chronological_distribution_plot(painters_vases):
    # Sort by Start date ascending (earliest first)
    painters_vases = painters_vases.sort_values(by="Start", ascending=True)

    # Normalize vase counts for color intensity
    painters_vases["Vase_Normalized"] = painters_vases["Vase_Count"] / painters_vases["Vase_Count"].max()

    fig, ax = plt.subplots(figsize=(12, 10))  # create figure and axes

    cmap = plt.cm.Blues
    norm = mpl.colors.Normalize(vmin=painters_vases["Vase_Count"].min(), vmax=painters_vases["Vase_Count"].max())

    bars = ax.barh(
        painters_vases['Painter'],
        painters_vases['End'] - painters_vases['Start'],
        left=painters_vases['Start'],
        color=cmap(painters_vases['Vase_Normalized'])
    )

    # Annotate vase count next to bars
    for bar, count in zip(bars, painters_vases['Vase_Count']):
        ax.text(bar.get_x() + bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,
                f"{int(count)}", va='center')

    ax.set_xlim(-610, -440)  # Keep tight range around your data

    ax.axvline(0, color='black', linestyle='--')
    ax.set_xlabel("Year (BC)")
    ax.set_title("Active Periods of Vase Painters Over Time with Vase Counts")

    # Create ScalarMappable for colorbar
    sm = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # needed for older matplotlib versions

    # Add colorbar with label, attach to our axes
    cbar = fig.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)  # smaller and closer colorbar
    cbar.set_label('Number of vases', fontsize=10)
    cbar.ax.tick_params(labelsize=8)


    plt.tight_layout()
    plt.show()