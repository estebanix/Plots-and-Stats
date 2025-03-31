import matplotlib.pyplot as plt
import seaborn as sns

def variable_distribution(df, variable, hue_dif=None, ax_value=None):
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    # Subplot 1: Box plot
    sns.boxplot(data=df, x=variable, hue=hue_dif if hue_dif else None, ax=axes[0])
    if ax_value is not None:
        axes[0].axvline(x=ax_value, color='red', linestyle='--', linewidth=1)
    axes[0].set_ylabel("Value Distribution")

    # Subplot 2: KDE plot
    sns.kdeplot(data=df, x=variable, hue=hue_dif if hue_dif else None, fill=True, common_norm=False, ax=axes[1])
    if ax_value is not None:
        axes[1].axvline(x=ax_value, color='red', linestyle='--', linewidth=1)
    axes[1].set_xlabel(variable)
    axes[1].set_ylabel("Density")

    # Adjust the layout to avoid overlap
    plt.tight_layout()
    plt.show()
