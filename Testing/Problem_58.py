import numpy as np
from scipy.stats import norm

# Given values
sigma = 60
mu_0 = 120

# Sample data
data = [115, 125, 102, 129, 121, 119, 120, 120, 126, 120,
        124, 118, 116, 132, 114, 108, 127, 131, 130, 181]

n = len(data)
sample_mean = np.mean(data)

# Standard error
se = sigma / np.sqrt(n)

# Test statistic
z = (sample_mean - mu_0) / se

# Critical Z-values
z_critical_10 = norm.ppf(1 - 0.10/2)  # 10% significance (two-tailed)
z_critical_5 = norm.ppf(1 - 0.05/2)   # 5% significance
z_critical_1 = norm.ppf(1 - 0.01/2)   # 1% significance

# Print results
print(f"Sample mean: {sample_mean:.2f}")
print(f"Z value: {z:.3f}")
print(f"Critical Z at 10%: ±{z_critical_10:.3f}")
print(f"Critical Z at 5%: ±{z_critical_5:.3f}")
print(f"Critical Z at 1%: ±{z_critical_1:.3f}")

# Decision
for alpha, z_crit in [("10%", z_critical_10), ("5%", z_critical_5), ("1%", z_critical_1)]:
    if -z_crit < z < z_crit:
        print(f"Hypothesis µ₀=120 accepted at {alpha} significance level.")
    else:
        print(f"Hypothesis µ₀=120 rejected at {alpha} significance level.")
