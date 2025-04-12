# Possible outcomes (total amounts won in each pair of envelopes)
outcomes = [30, 40, 50, 60, 50, 60, 70, 70, 80, 90]

# Probability of each outcome (since all outcomes are equally likely)
prob = 1 / len(outcomes)

# Expected value
expected_value = sum(outcome * prob for outcome in outcomes)

print(f"Expected value of the total amount won = {expected_value}€")
