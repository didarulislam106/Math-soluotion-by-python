# 10 people shake each others hands. How many handshakes are performed?
from math import comb

n = 10
handshakes = comb(n, 2)
print(f"Number of handshakes: {handshakes}")


# 8 teams play pairwise. How many matches are played?
from math import comb

n = 8
matches = comb(n, 2)
print(f"Number of matches: {matches}")