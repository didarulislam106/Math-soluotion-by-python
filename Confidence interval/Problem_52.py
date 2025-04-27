import numpy as np
from scipy.stats import norm

# Given data
data = [30.8, 30.0, 29.9, 30.1, 31.7, 34.0]
sigma = 2.5  # known standard deviation
confidence_level = 0.99

# Calculate sample mean and sample size
mean = np.mean(data)
n = len(data)

# Find Z value for 99% confidence
z = norm.ppf(1 - (1 - confidence_level) / 2)

# Calculate radius
radius = z * (sigma / np.sqrt(n))

# Confidence interval
lower_bound = mean - radius
upper_bound = mean + radius

print(f"99% confidence interval: {lower_bound:.2f} ≤ µ ≤ {upper_bound:.2f}")
