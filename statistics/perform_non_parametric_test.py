from scipy.stats import stats
from shapiro_wilk_test import make_SW_test

def perform_non_parametric_test(groups):
    results = make_SW_test(groups)
    
    non_normal = [i for i, p in enumerate(results) if p < 0.05]

    if len(non_normal) > 0:
        if len(groups) > 2:
            print("Applying Kruskal-Wallis test for multiple groups...")
            stat, p_value = stats.kruskal(*groups)
            print(f"Kruskal-Wallis H-statistic: {stat}, p-value: {p_value}")
            if p_value < 0.05:
                print("There is a significant difference between the groups.")
            else:
                print("There is no significant difference between the groups.")
        else:
            print("Applying Mann-Whitney U test for two groups...")
            stat, p_value = stats.mannwhitneyu(groups[0], groups[1])
            print(f"Mann-Whitney U-statistic: {stat}, p-value: {p_value}")
            if p_value < 0.05:
                print("There is a significant difference between the groups.")
            else:
                print("There is no significant difference between the groups.")
    else:
        print("All groups are normally distributed. You can use parametric tests like ANOVA or t-test.")