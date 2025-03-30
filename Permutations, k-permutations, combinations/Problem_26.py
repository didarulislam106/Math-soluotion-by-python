# Let’s consider a deck of playing cards.
# (a) How many permutations does the deck have?
from math import factorial

permutations = factorial(52)
print(f"Number of permutations: {permutations:.1e}")  

# (b) With what probability 5 cards drawn contain 4 aces?
from math import comb

total_hands = comb(52, 5)
favorable = comb(4, 4) * comb(48, 1)
probability = favorable / total_hands

print(f"Probability of 4 aces in 5 cards: {probability:.6f}")

# (c) With what probability 5 cards drawn contain 3 clubs and 2 spades?
from math import comb

total_hands = comb(52, 5)
favorable = comb(13, 3) * comb(13, 2)
probability = favorable / total_hands

print(f"Probability of 3 clubs and 2 spades: {probability:.5f}")