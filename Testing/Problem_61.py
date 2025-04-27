import scipy.stats as stats
import numpy as np

# Given values
mu_0 = 60.0
mu_1 = 57.0
sigma = 3
n = 20
x_bar = 58.05
alpha = 0.05

# Calculate z-test statistic
z = (x_bar - mu_0) / (sigma / np.sqrt(n))

# Calculate p-value for two-tailed test
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print(f"z-statistic: {z:.4f}")
print(f"p-value: {p_value:.4f}")

# Decision
if p_value < alpha:
    print("Reject H0: mu0 = 60.0")
else:
    print("Fail to reject H0: mu0 = 60.0")

# Additional information: sample mean is closer to mu1 = 57.0
print("Since sample mean is closer to mu1 = 57.0, we accept mu1.")
