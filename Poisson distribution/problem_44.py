from scipy.stats import poisson

# λ = 1 computer per month
lam = 1

# P(X < 2) = P(X = 0) + P(X = 1)
p_less_than_2 = poisson.cdf(1, lam)

print(f"P(X < 2) = {p_less_than_2:.2f}")
