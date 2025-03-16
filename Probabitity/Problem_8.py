# 8. Grade 5 was obtained as follows. In the mathematics exam 15% of students, in the physics exam 12% of students and in
# both 7% of students. With what probability a random student gets grade 5 in at least one of these exams?

# Defining the probabilities
P_M = 0.15  # Probability of grade 5 in mathematics
P_P = 0.12  # Probability of grade 5 in physics
P_M_and_P = 0.07  # Probability of grade 5 in both mathematics and physics

# Apply the inclusion-exclusion principle
P_M_or_P = P_M + P_P - P_M_and_P

# Print the result
print(f"Probability of grade 5 in at least one exam: {P_M_or_P:.2f}")