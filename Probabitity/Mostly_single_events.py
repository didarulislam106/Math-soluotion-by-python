# 1. The height distribution of IT students is as follows.

# Defining the height distribution as a list of dictionaries
height_distribution = [
    {"range": (1.51, 1.53), "students": 2},
    {"range": (1.54, 1.56), "students": 2},
    {"range": (1.57, 1.59), "students": 5},
    {"range": (1.60, 1.62), "students": 38},
    {"range": (1.63, 1.65), "students": 62},
    {"range": (1.66, 1.68), "students": 110},
    {"range": (1.69, 1.71), "students": 126},
    {"range": (1.72, 1.74), "students": 130},
    {"range": (1.75, 1.77), "students": 126},
    {"range": (1.78, 1.80), "students": 72},
    {"range": (1.81, 1.83), "students": 42},
    {"range": (1.84, 1.86), "students": 23},
    {"range": (1.87, 1.89), "students": 7},
    {"range": (1.90, 1.92), "students": 1},
]

# Calculating the total number of students
total_students = sum(interval["students"] for interval in height_distribution)
print(f"Total students: {total_students}")

# Defining a function to calculate the probability for a given condition
def calculate_probability(condition):
    # Filter intervals that satisfy the condition
    filtered_students = sum(
        interval["students"] for interval in height_distribution if condition(interval["range"])
    )
    # Calculate probability
    probability = filtered_students / total_students
    return probability

# Defining conditions for each part of the problem

# (a) Height greater than 180 cm (1.80 m)
condition_a = lambda x: x[0] > 1.80

# (b) Height between 163 cm (1.63 m) and 174 cm (1.74 m)
condition_b = lambda x: 1.63 <= x[0] <= 1.74

# (c) Height less than 160 cm (1.60 m)
condition_c = lambda x: x[1] < 1.60

# Calculating probabilities
prob_a = calculate_probability(condition_a)
prob_b = calculate_probability(condition_b)
prob_c = calculate_probability(condition_c)

# Print results
print(f"(a) Probability of height greater than 180 cm: {prob_a:.3f}")
print(f"(b) Probability of height between 163 cm... 174 cm: {prob_b:.3f}")
print(f"(c) Probability of height less than 160 cm: {prob_c:.3f}")