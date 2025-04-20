from scipy.stats import norm

# Parameters
mu = 3      # mean resistance in ohms
sigma = 0.1 # standard deviation in ohms

# (a) P(2.9 ≤ X ≤ 3.05)
p_a = norm.cdf(3.05, mu, sigma) - norm.cdf(2.9, mu, sigma)

# (b) P(X > 2.95)
p_b = 1 - norm.cdf(2.95, mu, sigma)

# (c) P(X < 2.83)
p_c = norm.cdf(2.83, mu, sigma)

print(f"(a) P(2.9 ≤ X ≤ 3.05) = {p_a:.4f}")
print(f"(b) P(X > 2.95) = {p_b:.4f}")
print(f"(c) P(X < 2.83) = {p_c:.4f}")
