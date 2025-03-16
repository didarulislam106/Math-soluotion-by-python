# Defining all possible outcomes when two dice are thrown
outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]

# Total number of outcomes
total_outcomes = len(outcomes)

# Calculate probabilities
# (a) Sum = 1
sum_1 = sum(1 for (i, j) in outcomes if i + j == 1)
prob_a = sum_1 / total_outcomes

# (b) Sum = 5
sum_5 = sum(1 for (i, j) in outcomes if i + j == 5)
prob_b = sum_5 / total_outcomes

# (c) Sum = 11
sum_11 = sum(1 for (i, j) in outcomes if i + j == 11)
prob_c = sum_11 / total_outcomes

# (d) Sum > 7
sum_gt_7 = sum(1 for (i, j) in outcomes if i + j > 7)
prob_d = sum_gt_7 / total_outcomes

# Print results
print(f"(a) Probability of sum = 1: {prob_a}")
print(f"(b) Probability of sum = 5: {prob_b:.3f}")
print(f"(c) Probability of sum = 11: {prob_c:.3f}")
print(f"(d) Probability of sum > 7: {prob_d:.3f}")