# 23. A student answers 8 questions from 10 options.

# (a) How many ways the student can choose?
from math import comb

n = 10
k = 8
ways = comb(n, k)

print(f"Number of ways to choose 8 questions: {ways}")

# (b) How many ways the student can choose, if the first 3 questions are mandatory?
from math import comb

n_remaining = 7
k_remaining = 5
ways_mandatory = comb(n_remaining, k_remaining)

print(f"Number of ways with first 3 mandatory: {ways_mandatory}")