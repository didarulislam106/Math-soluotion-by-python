import numpy as np
import math
from scipy.stats import norm

# Given data
weights = (
    [1.90] * 8 +
    [1.95] * 10 +
    [1.98] * 12 +
    [2.05] * 4
)

# Sample size
n = len(weights)

# Sample mean
mean = np.mean(weights)

# Sample standard deviation
std_dev = np.std(weights, ddof=1)  # ddof=1 for sample std deviation

# Confidence level
confidence_level = 0.95
z = norm.ppf(1 - (1 - confidence_level) / 2)

# Radius of confidence interval
R = z * (std_dev / math.sqrt(n))

# Lower bound
lower_bound = mean - R

# Check how much under 2.0 kg
underweight = (2.0 - lower_bound) * 1000  # in grams

print(f"At least {underweight:.0f}g underweight")
