from scipy.stats import norm

# Parameters
mu = 175    # mean height in cm
sigma = 8   # standard deviation
threshold = 200  # height in cm

# Calculate the probability
p_over_200 = 1 - norm.cdf(threshold, mu, sigma)

print(f"Probability a man is taller than 2 meters: {p_over_200:.6f} ({p_over_200 * 100:.4f}%)")
