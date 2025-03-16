# 9. In the pedestrian crossing, the lights are adjusted so that red light is on for 40 s and the green light is on for 20 s. 
# With what probability a pedestrian has to wait max 30 s? 

# Defining the light durations
red_duration = 40  # Red light duration in seconds
green_duration = 20  # Green light duration in seconds
total_cycle = red_duration + green_duration  # Total cycle time in seconds

# Step 2: Define the favorable time interval
favorable_interval = 30  # Pedestrian waits at most 30 seconds

# Step 3: Calculate the probability
probability = favorable_interval / total_cycle

# Step 4: Print the result
print(f"Probability of waiting at most 30 seconds: {probability:.2f}")