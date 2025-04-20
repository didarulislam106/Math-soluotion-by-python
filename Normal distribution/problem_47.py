from scipy.stats import norm

# Parameters
mu = 3       # mean life in years
sigma = 1.2  # standard deviation
batch_size = 7000

# P(X > 5)
p_more_than_5 = 1 - norm.cdf(5, mu, sigma)

# Expected number of batteries
expected_count = p_more_than_5 * batch_size

print(f"Probability a battery lasts > 5 years: {p_more_than_5:.4f}")
print(f"Expected number of batteries: {expected_count:.0f}")