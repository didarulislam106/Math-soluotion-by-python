from scipy.stats import poisson

# λ = expected number of malfunctions
lam = 900 * 0.007  # λ = 6.3

# (a) Probability that exactly 7 controllers malfunction
p_7 = poisson.pmf(7, lam)

# (b) Probability that more than 3 controllers malfunction
p_more_than_3 = 1 - poisson.cdf(3, lam)

print(f"(a) P(X = 7) = {p_7:.2f}")            
print(f"(b) P(X > 3) = {p_more_than_3:.2f}") 
