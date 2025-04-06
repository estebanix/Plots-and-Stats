import scipy.stats as stats

def make_SW_test(groups):
    p_values = []
    
    for group in groups:
        shapiro_stat, p_value = stats.shapiro(group)
        p_values.append(p_value)

    return p_values
