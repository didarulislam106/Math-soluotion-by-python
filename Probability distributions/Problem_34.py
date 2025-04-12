from scipy.stats import binom
import math

# Parameters
n = 4
p = 1/6

# Expected value (mean)
mu = n * p

# Variance and standard deviation
variance = n * p * (1 - p)
sigma = math.sqrt(variance)

print(f"Expected Value (µ) = {mu}")
print(f"Standard Deviation (σ) = {sigma}")
