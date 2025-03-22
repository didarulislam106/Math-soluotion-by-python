# In a lottery, there are 4 tickets. The tickets have the numbers 1, 2, 3 and 4. One ticket is picked, put back to the box, and
# another ticked is picked. With what probability at least one “1” is obtained? 

 # Total number of tickets
total_tickets = 4

# Number of unfavorable outcomes (neither draw is a "1")
unfavorable_outcomes = 3 * 3  # 3 choices for the first draw and 3 for the second

# Total number of outcomes
total_outcomes = total_tickets * total_tickets

# Probability of at least one "1"
probability = 1 - (unfavorable_outcomes / total_outcomes)

# Result
print(f"Probability of at least one '1': {probability:.4f}")