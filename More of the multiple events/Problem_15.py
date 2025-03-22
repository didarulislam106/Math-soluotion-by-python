# Which probability is better: getting an odd number or at most 4 while throwing a dice?

# Probability of getting an odd number
prob_odd = 3 / 6

# Probability of getting at most 4
prob_at_most_4 = 4 / 6

# Results
print(f"Probability of getting an odd number: {prob_odd:.4f}")
print(f"Probability of getting at most 4: {prob_at_most_4:.4f}")

# Compare the probabilities
if prob_odd > prob_at_most_4:
    print("Getting an odd number has a better probability.")
elif prob_odd < prob_at_most_4:
    print("Getting at most 4 has a better probability.")
else:
    print("Both probabilities are equal.")