# 7. Let’s throw two dice. With what probability the sum is 10, 11 or 12?

from itertools import product

# Defining all possible outcomes when two dice are thrown
outcomes = list(product(range(1, 7), repeat=2))

# Total number of outcomes
total_outcomes = len(outcomes)

# Count favorable outcomes (sum = 10, 11, or 12)
favorable_outcomes = sum(1 for (i, j) in outcomes if i + j in {10, 11, 12})

# Calculate probability
probability = favorable_outcomes / total_outcomes

# Print result
print(f"Probability that the sum is 10, 11, or 12: {probability}")