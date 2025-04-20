from scipy.stats import norm

# Parameters
mu = 5
sigma = 0.2

# (a) Find k such that P(X ≤ k) = 0.95
k_a = norm.ppf(0.95, mu, sigma)

# (b) Find k such that P(X > k) = 0.01 ⇒ P(X ≤ k) = 0.99
k_b = norm.ppf(0.99, mu, sigma)

print(f"(a) k for P(X ≤ k) = 0.95 → k = {k_a:.3f}")
print(f"(b) k for P(X > k) = 0.01 → k = {k_b:.3f}")
