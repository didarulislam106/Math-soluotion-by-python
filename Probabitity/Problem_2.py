# 2. Students estimated the length of a given segment. Their errors were [cm]

# Defining the list of errors
errors = [
    2, 3, 0, 5, 6, 1, 2, 4, 3, 1, 3, 2,
    1, 0, 1, 1, 0, 2, 1, 1, 0, 5, 0, 2,
    5, 3, 1, 1, 2, 0, 4, 3, 0, 0, 2, 1,
    0, 3, 5, 4, 2, 0, 5, 3, 1, 6, 2, 4,
    1, 1, 4, 7, 2, 0, 2, 1, 0, 4, 4, 3
]

# Counting the number of errors ≤ 1 cm
at_most_1_cm = sum(1 for error in errors if error <= 1)

# Total number of students
total_students = len(errors)

# Calculating the probability
probability = at_most_1_cm / total_students

# Print the result
print(f"Probability of at most 1 cm error: {probability:.3f}")