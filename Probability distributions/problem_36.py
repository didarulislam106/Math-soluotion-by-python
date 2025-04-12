from scipy.stats import hypergeom

# Parameters
N = 6  # total number of balls
K = 3  # number of white balls
n = 3  # number of draws

# Expected value (mean) for hypergeometric distribution
mu = hypergeom.mean(N, K, n)

print(f"Expected number of white balls (µ) = {mu}")
