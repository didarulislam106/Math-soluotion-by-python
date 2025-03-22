# With what probability two picked playing cards are two aces?

from math import comb

# Total number of cards in a deck
total_cards = 52

# Number of aces in a deck
num_aces = 4

# Number of ways to choose 2 aces
ways_to_choose_2_aces = comb(num_aces, 2)

# Number of ways to choose any 2 cards
ways_to_choose_2_cards = comb(total_cards, 2)

# Probability of drawing 2 aces
probability = ways_to_choose_2_aces / ways_to_choose_2_cards

# Result
print(f"Probability of drawing 2 aces: {probability:.6f} (or {1}/{int(1/probability)})")