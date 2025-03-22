# 13. In a factory, there is a box of 100 circuit boards. Three of the boards are broken. Random two boards are chosen. 
# With what probability at least one of the boards is intact?

import random

# Number of simulations
num_simulations = 1000000

# Count of successful outcomes (at least one intact board)
success_count = 0

# Simulate choosing 2 boards
for _ in range(num_simulations):
    box = ['broken'] * 3 + ['intact'] * 97  # 3 broken boards and 97 intact boards
    random.shuffle(box)
    drawn_boards = box[:2]
    if 'intact' in drawn_boards:  # At least one intact board
        success_count += 1

# Calculate empirical probability
empirical_probability = success_count / num_simulations

# Result
print(f"Empirical probability of at least one intact board: {empirical_probability:.6f}")