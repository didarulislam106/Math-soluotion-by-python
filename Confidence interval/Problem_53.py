import math
from scipy.stats import norm

# Given values
mu = 74.81
sigma = 4
n = 200
confidence_level = 0.95

# Find Z value for 95% confidence
z = norm.ppf(1 - (1 - confidence_level) / 2)

# Calculate radius R
R = z * (sigma / math.sqrt(n))

# Confidence interval
lower_bound = mu - R
upper_bound = mu + R

print(f"Confidence Interval: {lower_bound:.2f} ≤ µ ≤ {upper_bound:.2f}")
