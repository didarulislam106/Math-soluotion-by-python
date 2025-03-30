from math import factorial

girls_arrangements = factorial(4)
boys_arrangements = factorial(3)
total_queues = girls_arrangements * boys_arrangements

# Calculate the total number of arrangements
print(f"Total possible queues: {total_queues}")