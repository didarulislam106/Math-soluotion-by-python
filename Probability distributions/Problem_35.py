from scipy.stats import binom
import math

# Parameters
n = 2
p = 0.8

# Expected value (mean)
mu = n * p

# Variance and standard deviation
variance = n * p * (1 - p)
sigma = math.sqrt(variance)

# Probability mass function (PMF)
x_vals = range(n + 1)
pmf_vals = binom.pmf(x_vals, n, p)

# Output results
print("Probability Distribution (PMF):")
for x, prob in zip(x_vals, pmf_vals):
    print(f"P(X = {x}) = {prob:.4f}")

print(f"\nExpected Value (µ) = {mu}")
print(f"Standard Error (σ) = {sigma}")
