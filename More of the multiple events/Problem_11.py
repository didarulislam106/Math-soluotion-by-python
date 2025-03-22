# 11. In a box, there are 6 red balls and 4 black balls. Let’s pick up two balls without putting them back to the box.
#  With what probability both of the balls are black? Solution 0.13

import random

# Number of simulations
num_simulations = 1000000

# Count of successful outcomes (both balls are black)
success_count = 0

# Simulate drawing 2 balls
for _ in range(num_simulations):
    box = ['red'] * 6 + ['black'] * 4  # 6 red balls and 4 black balls
    random.shuffle(box)
    drawn_balls = box[:2]
    if drawn_balls == ['black', 'black']:  # Both balls are black
        success_count += 1

# Calculate empirical probability
empirical_probability = success_count / num_simulations

# Result
print(f"Empirical probability of drawing 2 black balls: {empirical_probability:.4f}")