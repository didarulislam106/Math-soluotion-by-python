import numpy as np
from scipy import stats

# Given sample data
sample = np.array([
    53.08, 56.02, 57.32, 51.76, 57.07,
    59.08, 59.00, 52.31, 54.10, 55.78,
    54.91, 60.50, 56.81, 56.72, 58.13,
    58.31, 58.85, 54.92, 60.69, 58.70
])

# Null hypothesis mean
mu_0 = 55

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(sample, mu_0)

print(f"t-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.4f}")

# Decision based on p-value and significance level alpha = 0.05
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis (H0).")
else:
    print("Fail to reject the null hypothesis (H0).")
