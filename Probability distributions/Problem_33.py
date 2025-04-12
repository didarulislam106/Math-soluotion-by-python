from sympy import symbols, Eq, solve, Rational

# Define variables
n, p = symbols('n p', positive=True)

# Given values
mu = 2
variance = Rational(4, 3)  # variance = 4/3 as a rational number

# Equations based on binomial distribution
eq1 = Eq(n * p, mu)                          # Equation for mean
eq2 = Eq(n * p * (1 - p), variance)          # Equation for variance

# Solve the system of equations
solution = solve((eq1, eq2), (n, p))

# Display solution
for sol in solution:
    n_val, p_val = sol
    print(f"n = {n_val}, p = {p_val}")