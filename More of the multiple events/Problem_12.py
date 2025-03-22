# 12. Let’s throw a dice four times. With what probability
# (a) 2 number “2”
# (b) 4 odd numbers 
# (c) at least one “6” 
#  are obtained? 

import random

# Number of simulations
num_simulations = 1000000

# Counters for successful outcomes
count_a = 0  # Exactly 2 number "2"
count_b = 0  # All 4 odd numbers
count_c = 0  # At least one "6"

# Simulate throwing the dice 4 times
for _ in range(num_simulations):
    throws = [random.randint(1, 6) for _ in range(4)]
    
    # (a) Exactly 2 number "2"
    if throws.count(2) == 2:
        count_a += 1
    
    # (b) All 4 odd numbers
    if all(x % 2 == 1 for x in throws):
        count_b += 1
    
    # (c) At least one "6"
    if 6 in throws:
        count_c += 1

# Calculate empirical probabilities
prob_a_sim = count_a / num_simulations
prob_b_sim = count_b / num_simulations
prob_c_sim = count_c / num_simulations

# Print the results
print(f"(a) Empirical probability of exactly 2 number '2': {prob_a_sim:.4f}")
print(f"(b) Empirical probability of all 4 odd numbers: {prob_b_sim:.4f}")
print(f"(c) Empirical probability of at least one '6': {prob_c_sim:.4f}")