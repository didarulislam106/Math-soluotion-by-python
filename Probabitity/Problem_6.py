# 6. Let’s make a two digit number by choosing its digits randomly from 1, 2, 3, 4, and 5. The same digit can appear twice.
# With what probability the number is divisible by 2 or 5? 

from itertools import product

# Defining the digits
digits = [1, 2, 3, 4, 5]

# Generate all possible two-digit numbers
two_digit_numbers = list(product(digits, repeat=2))

# Total number of possible two-digit numbers
total_numbers = len(two_digit_numbers)

# Count numbers divisible by 2 or 5
divisible_by_2_or_5 = sum(1 for num in two_digit_numbers if (num[1] % 2 == 0) or (num[1] % 5 == 0))

# Calculate probability
probability = divisible_by_2_or_5 / total_numbers

# Print result
print(f"Probability that the number is divisible by 2 or 5: {probability}")