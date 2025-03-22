# Weather forecast announced that the chance of rain on Saturday is 30% and the chance of rain on Sunday is 60%. 
# With what probability, it rains during the weekend?

# Probability of rain on Saturday
prob_saturday = 0.3

# Probability of rain on Sunday
prob_sunday = 0.6

# Probability of no rain on Saturday
prob_no_saturday = 1 - prob_saturday

# Probability of no rain on Sunday
prob_no_sunday = 1 - prob_sunday

# Probability of no rain on both days
prob_no_rain_both_days = prob_no_saturday * prob_no_sunday

# Probability of rain on at least one day
prob_rain_weekend = 1 - prob_no_rain_both_days

# Result
print(f"Probability of rain during the weekend: {prob_rain_weekend:.2f}")