# Total number of coins
total_coins = 12

# Number of each type of coin
coins_1e = 6
coins_2e = 4
coins_50c = 2

# Probabilities for each coin value
prob_1e = coins_1e / total_coins
prob_2e = coins_2e / total_coins
prob_50c = coins_50c / total_coins

# Print the distribution
print(f"P(1€) = {prob_1e}")
print(f"P(2€) = {prob_2e}")
print(f"P(0.50€) = {prob_50c}")
