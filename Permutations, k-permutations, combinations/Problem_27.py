# For an entrance exam, 20 math questions and 15 physics questions are considered. The questions are chosen in random
# and their order does not matter. With what probability chosen 6 questions
# (a) are all math questions? Solution 0.024
from math import comb

total = comb(35, 6)
favorable = comb(20, 6)
probability = favorable / total

print(f"Probability of all 6 questions being math: {probability:.3f}")

# (b) contain 3 math questions and 3 physics questions? 
from math import comb

total = comb(35, 6)
favorable = comb(20, 3) * comb(15, 3)
probability = favorable / total

print(f"Probability of 3 math and 3 physics questions: {probability:.3f}")