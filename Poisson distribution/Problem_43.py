from scipy.stats import poisson

# λ = 2 cars per minute
lam = 2

# P(X >= 4) = 1 - P(X <= 3)
p_4_or_more = 1 - poisson.cdf(3, lam)

print(f"P(X >= 4) = {p_4_or_more:.2f}")
