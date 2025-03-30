from math import comb

total_outcomes = 3 ** 13
favorable_outcomes = comb(13, 12) * 2  # 13 ways to choose 12 correct, 2 wrong options for the 13th
probability = favorable_outcomes / total_outcomes

print(f"Probability of guessing 12 matches correctly: {probability:.7f}")