import numpy as np
import math
from scipy.stats import norm

# Given data
weights = [692] * 6 + [701] * 4  # in grams

# Sample size
n = len(weights)

# Sample mean
mean = np.mean(weights)

# Sample standard deviation
std_dev = np.std(weights, ddof=1)  # ddof=1 for sample std deviation

# Confidence level
confidence_level = 0.99
z = norm.ppf(1 - (1 - confidence_level) / 2)

# Radius of confidence interval
R = z * (std_dev / math.sqrt(n))

# Confidence interval
lower_bound = mean - R
upper_bound = mean + R

print(f"{lower_bound:.1f} ≤ µ ≤ {upper_bound:.1f} g")
