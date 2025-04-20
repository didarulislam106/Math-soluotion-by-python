from scipy.stats import norm

# Parameters
mu = 80     # mean weight in kg
sigma = 4   # standard deviation

# (a) P(77 ≤ X ≤ 80)
p_a = norm.cdf(80, mu, sigma) - norm.cdf(77, mu, sigma)

# (b) P(X > 80)
p_b = 1 - norm.cdf(80, mu, sigma)

print(f"(a) P(77 ≤ X ≤ 80) = {p_a:.2f}")
print(f"(b) P(X > 80) = {p_b:.2f}")
