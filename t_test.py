import numpy as np
from scipy import stats

def two_sample_ttest(sample1, sample2, equal_var=True):
    sample1 = np.array(sample1, dtype=float)
    sample2 = np.array(sample2, dtype=float)
    tstat, pvalue = stats.ttest_ind(sample1, sample2, equal_var=equal_var)
    return float(tstat), float(pvalue)

if __name__ == "__main__":
    group_a = [23, 20, 22, 21, 24, 19]
    group_b = [30, 28, 29, 31, 27, 26]
    t, p = two_sample_ttest(group_a, group_b, equal_var=False)
    print("Group A:", group_a)
    print("Group B:", group_b)
    print("t-statistic:", t)
    print("p-value:", p)
    if p < 0.05:
        print("Result: statistically significant difference (alpha=0.05)")
    else:
        print("Result: no statistically significant difference (alpha=0.05)")
