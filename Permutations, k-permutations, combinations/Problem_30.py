# English test contains 40 questions. Each question has 4 options. The student is guessing.
# (a) With what probability all answers are correct?
probability_all_correct = (1/4) ** 40
print(f"Probability of all correct: {probability_all_correct:.2e}")

# (b) With what probability exactly 5 answers are correct?
from math import comb

n = 40
k = 5
p = 1/4

probability_5_correct = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print(f"Probability of exactly 5 correct: {probability_5_correct:.5f}")

# (c) With what probability at least 5 answers are correct? 
from math import comb

n = 40
p = 1/4

# Calculate cumulative probability for k=0 to 4
cumulative = sum(comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(5))

probability_at_least_5 = 1 - cumulative
print(f"Probability of at least 5 correct: {probability_at_least_5:.5f}")