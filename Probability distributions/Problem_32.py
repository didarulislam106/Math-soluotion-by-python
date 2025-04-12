from scipy.stats import binom
import matplotlib.pyplot as plt

# Parameters
n = 2           # number of throws
p = 0.70        # probability of scoring

# Distribution (PMF)
x_vals = range(n + 1)
pmf_vals = binom.pmf(x_vals, n, p)

# Expected Value
expected_value = binom.mean(n, p)

# Output the distribution
print("Probability Distribution (PMF):")
for x, prob in zip(x_vals, pmf_vals):
    print(f"P(X = {x}) = {prob:.4f}")

print(f"\nExpected Value E[X] = {expected_value:.4f}")