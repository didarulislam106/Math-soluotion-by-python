from math import comb

n = 10  # Number of trials (rolls)
k = 3   # Desired successes ("6"s)
p = 1/6 # Probability of rolling a "6"

probability = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print(f"Probability of exactly 3 '6's in 10 rolls: {probability:.3f}")