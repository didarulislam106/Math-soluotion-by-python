# 3. A car factory collected data; when a car had its first repair done

# Defining the cumulative data
cumulative_data = {
    "0-10,000": 50,
    "10,001-20,000": 143,
    "20,001-30,000": 436,
    "30,001-40,000": 827,
    "40,001-50,000": 1010,
    "50,001+": 1050
}

# Total number of cars
total_cars = cumulative_data["50,001+"]

# Calculate probabilities

# (a) At most 20,000 km
prob_a = cumulative_data["10,001-20,000"] / total_cars

# (b) Between 20,001 km and 30,000 km
prob_b = (cumulative_data["20,001-30,000"] - cumulative_data["10,001-20,000"]) / total_cars

# (c) Between 30,001 km and 40,000 km
prob_c = (cumulative_data["30,001-40,000"] - cumulative_data["20,001-30,000"]) / total_cars

# (d) Over 40,000 km
prob_d = (total_cars - cumulative_data["30,001-40,000"]) / total_cars

# (e) Sum of probabilities
sum_prob = prob_a + prob_b + prob_c + prob_d

# (f) Probability of repair in 30,001-40,000 km given no repair in 0-30,000 km
cars_no_repair_0_30k = total_cars - cumulative_data["20,001-30,000"]
cars_repair_30k_40k = cumulative_data["30,001-40,000"] - cumulative_data["20,001-30,000"]
prob_f = cars_repair_30k_40k / cars_no_repair_0_30k

# Print results
print(f"(a) Probability of repair at most 20,000 km: {prob_a:.2f}")
print(f"(b) Probability of repair between 20,001 km and 30,000 km: {prob_b:.2f}")
print(f"(c) Probability of repair between 30,001 km and 40,000 km: {prob_c:.2f}")
print(f"(d) Probability of repair over 40,000 km: {prob_d:.2f}")
print(f"(e) Sum of probabilities (a)-(d): {sum_prob:.2f}")
print(f"(f) Probability of repair in 30,001-40,000 km given no repair in 0-30,000 km: {prob_f:.2f}")