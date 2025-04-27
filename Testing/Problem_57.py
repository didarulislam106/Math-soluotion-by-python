import math
from scipy.stats import norm

# Given values
n = 16
sample_mean = 4482
sigma = 115

# Hypotheses means
mu_0 = 4500
mu_1 = 4400

# Standard error
se = sigma / math.sqrt(n)

# Test statistics
z_mu0 = (sample_mean - mu_0) / se
z_mu1 = (sample_mean - mu_1) / se

# Critical Z values
z_critical_5 = norm.ppf(1 - 0.05/2)  # 5% significance (two-tailed)
z_critical_1 = norm.ppf(1 - 0.01/2)  # 1% significance (two-tailed)

# Print results
print(f"Z for mu0=4500: {z_mu0:.3f}")
print(f"Z for mu1=4400: {z_mu1:.3f}")
print(f"Critical Z at 5%: ±{z_critical_5:.3f}")
print(f"Critical Z at 1%: ±{z_critical_1:.3f}")

# Decision for mu0
if -z_critical_5 < z_mu0 < z_critical_5:
    print("mu0=4500 accepted at 5% level.")
else:
    print("mu0=4500 rejected at 5% level.")

if -z_critical_1 < z_mu0 < z_critical_1:
    print("mu0=4500 accepted at 1% level.")
else:
    print("mu0=4500 rejected at 1% level.")

# Decision for mu1
if -z_critical_5 < z_mu1 < z_critical_5:
    print("mu1=4400 accepted at 5% level.")
else:
    print("mu1=4400 rejected at 5% level.")

if -z_critical_1 < z_mu1 < z_critical_1:
    print("mu1=4400 accepted at 1% level.")
else:
    print("mu1=4400 rejected at 1% level.")
