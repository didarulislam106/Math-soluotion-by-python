# In total 32 students sit in a class. In how many different ways they can sit?

import math

# Calculate 32 factorial
num_students = 32
arrangements = math.factorial(num_students)

# Print in scientific notation
print(f"Number of seating arrangements: {arrangements:.2e}")