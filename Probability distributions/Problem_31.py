import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 3           # number of spins
p = 1/8         # probability of joker in a single spin

# Distribution (PMF)
x_vals = range(n + 1)
pmf_vals = binom.pmf(x_vals, n, p)

# Expected Value
expected_value = binom.mean(n, p)

# Output
print("Probability Distribution (PMF):")
for x, p_x in zip(x_vals, pmf_vals):
    print(f"P(X = {x}) = {p_x:.4f}")

print(f"\nExpected Value E[X] = {expected_value:.4f}")

# Plotting the distribution
plt.bar(x_vals, pmf_vals, color='skyblue', edgecolor='black')
plt.title('Binomial Distribution: Number of Jokers in 3 Spins')
plt.xlabel('Number of Jokers (X)')
plt.ylabel('Probability')
plt.xticks(x_vals)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
