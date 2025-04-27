import numpy as np
import math
from scipy.stats import norm

# Given data
data = [
    97.0, 101.5, 102.1, 103.9, 93.4, 103.3, 104.1, 98.6, 97.3,
    96.2, 107.7, 104.8, 98.5, 99.2, 93.8, 100.3, 103.7, 96.4
]

# Given population standard deviation
sigma = 25

# Sample size
n = len(data)

# Sample mean
mean = np.mean(data)

# Confidence levels
confidence_levels = [0.95, 0.99, 0.999]

# Calculate confidence intervals
for confidence in confidence_levels:
    z = norm.ppf(1 - (1 - confidence) / 2)
    margin_of_error = z * (sigma / math.sqrt(n))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    print(f"{confidence*100:.1f}% confidence interval: {lower_bound:.1f} ≤ µ ≤ {upper_bound:.1f}")
