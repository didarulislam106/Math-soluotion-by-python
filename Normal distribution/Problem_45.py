from scipy.stats import norm

# (a) P(Z ≤ 0.25)
p_a = norm.cdf(0.25)

# (b) P(1.2 ≤ Z ≤ 2.1)
p_b = norm.cdf(2.1) - norm.cdf(1.2)

# (c) P(-1 ≤ Z ≤ 1.5)
p_c = norm.cdf(1.5) - norm.cdf(-1)

print(f"(a) P(Z ≤ 0.25) = {p_a:.4f}")
print(f"(b) P(1.2 ≤ Z ≤ 2.1) = {p_b:.4f}")
print(f"(c) P(-1 ≤ Z ≤ 1.5) = {p_c:.4f}")
