# Data: Number of heads observed in each throw
data = [0, 2, 3, 2, 4, 3, 4, 3, 3, 4, 1, 4, 3, 4, 5, 3, 4, 4, 4, 4, 3, 2, 1, 4, 2, 3, 4, 2, 
        5, 3, 4, 2, 4, 2, 1, 2, 4, 3, 2, 2, 1, 5, 2, 3, 1, 5, 3, 3, 3, 1, 3, 4, 2, 3, 4, 1, 
        3, 5, 5, 3, 2, 5, 3, 2, 3, 4, 2, 3, 3, 3, 2, 3, 4, 5, 5, 0, 5, 2, 3, 3, 4, 3, 0, 4, 
        1, 2, 4]

# Count occurrences of each number of heads
counts = {i: data.count(i) for i in range(6)}

# Total number of throws
total_throws = len(data)

# Calculate probabilities for each outcome (0, 1, 2, 3, 4, 5 heads)
probabilities = {k: counts[k] / total_throws for k in counts}

# Print the distribution (probabilities)
for heads, prob in probabilities.items():
    print(f"P({heads} heads) = {prob:.3f}")