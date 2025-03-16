from itertools import product
from fractions import Fraction

# Let’s throw a coin three times. With what probability

# Defining all possible outcomes when a coin is tossed three times
outcomes = list(product("HT", repeat=3))

# Total number of outcomes
total_outcomes = len(outcomes)

# Calculate probabilities
# (a) 4 heads
prob_a = Fraction(0, total_outcomes)  # Impossible to get 4 heads in 3 tosses

# (b) 3 heads
count_3_heads = sum(1 for outcome in outcomes if outcome.count("H") == 3)
prob_b = Fraction(count_3_heads, total_outcomes)

# (c) 2 heads
count_2_heads = sum(1 for outcome in outcomes if outcome.count("H") == 2)
prob_c = Fraction(count_2_heads, total_outcomes)

# (d) 1 head
count_1_head = sum(1 for outcome in outcomes if outcome.count("H") == 1)
prob_d = Fraction(count_1_head, total_outcomes)

# (e) 0 heads
count_0_heads = sum(1 for outcome in outcomes if outcome.count("H") == 0)
prob_e = Fraction(count_0_heads, total_outcomes)

# Print results
print(f"(a) Probability of 4 heads: {prob_a}")
print(f"(b) Probability of 3 heads: {prob_b}")
print(f"(c) Probability of 2 heads: {prob_c}")
print(f"(d) Probability of 1 head: {prob_d}")
print(f"(e) Probability of 0 heads: {prob_e}")