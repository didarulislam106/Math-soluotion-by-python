import numpy as np
from scipy import stats

# Differences between two voltage meters
differences = np.array([0.4, -0.6, 0.2, 0.0, 1.0, 1.4, 0.4, 1.6])

# Null hypothesis mean difference
mu_0 = 0

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(differences, mu_0)

print(f"t-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.4f}")

# Decision based on p-value and significance level alpha = 0.05
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis (H0). Calibration differs.")
else:
    print("Fail to reject the null hypothesis (H0). Calibration does not differ.")
