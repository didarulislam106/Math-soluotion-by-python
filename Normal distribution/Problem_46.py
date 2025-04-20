from scipy.stats import norm

# Parameters
mu = 8
sigma = 1.7

# Calculate P(7 ≤ X ≤ 12.2)
p = norm.cdf(12.2, mu, sigma) - norm.cdf(7, mu, sigma)

print(f"P(7 ≤ X ≤ 12.2) = {p:.4f}")
