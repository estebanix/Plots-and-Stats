from scipy.stats import stats
from shapiro_wilk_test import make_SW_test

def perform_parametric_test(groups):
    results = make_SW_test(groups)

    non_normal = [i for i, p in enumerate(results) if p < 0.05]

    if len(non_normal) == 0:
        if len(groups) > 2:
            print("Applying ANOVA test for multiple groups...")
            stat, p_value = stats.f_oneway(*groups)
            print(f"ANOVA F-statistic: {stat}, p-value: {p_value}")
            if p_value < 0.05:
                print("There is a significant difference between the groups.")
            else:
                print("There is no significant difference between the groups.")
        else:
            print("Applying t-test for two groups...")
            stat, p_value = stats.ttest_ind(groups[0], groups[1])
            print(f"t-test statistic: {stat}, p-value: {p_value}")
            if p_value < 0.05:
                print("There is a significant difference between the groups.")
            else:
                print("There is no significant difference between the groups.")
    else:
        print("At least one group is not normally distributed. You should use non-parametric tests like Kruskal-Wallis or Mann-Whitney U.")
