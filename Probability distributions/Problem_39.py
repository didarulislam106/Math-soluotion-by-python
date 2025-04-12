# Possible outcomes and corresponding wins
outcomes = [40, 20, 20, -100]
probability = 1 / 4  # Each outcome has equal probability

# Calculate expected value (mean of wins)
mu = sum(outcome * probability for outcome in outcomes)

print(f"Expected value of the win = {mu}€")