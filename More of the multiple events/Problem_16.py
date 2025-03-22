# A plane was over booked. With 5 persons in the airport, random 2 are selected to the plane. Adam, Bella, Cecilia, Daniel
# and Emma are in the queue. With what probability
# (a) With what probability Adam and Emma can board?
# (b) With what probability one man and one woman can board?
# (c) With what probability no man can board? 

from math import comb

# Total number of ways to choose 2 people out of 5
total_ways = comb(5, 2)

# (a) Probability that Adam and Emma board
prob_a = 1 / total_ways

# (b) Probability that one man and one woman board
num_men = 2  # Adam, Daniel
num_women = 3  # Bella, Cecilia, Emma
ways_one_man_one_woman = comb(num_men, 1) * comb(num_women, 1)
prob_b = ways_one_man_one_woman / total_ways

# (c) Probability that no man boards
ways_two_women = comb(num_women, 2)
prob_c = ways_two_women / total_ways

# Results
print(f"(a) Probability that Adam and Emma board: {prob_a:.1f}")
print(f"(b) Probability that one man and one woman board: {prob_b:.1f}")
print(f"(c) Probability that no man boards: {prob_c:.1f}")