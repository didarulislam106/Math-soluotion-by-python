# Total tickets and prize amounts
total_tickets = 1000
prizes = [99, 49, 19, -1]
ticket_counts = [1, 10, 15, 974]

# Calculate the expected value (mean of net wins)
mu = sum((ticket_counts[i] / total_tickets) * prizes[i] for i in range(len(prizes)))

print(f"Expected value of the net win = {mu}€")