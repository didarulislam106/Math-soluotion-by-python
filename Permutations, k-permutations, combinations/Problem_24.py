from math import comb

men = comb(7, 3)  # 35 ways to choose 3 men
women = comb(5, 2) # 10 ways to choose 2 women
total_groups = men * women

print(f"Total groups with 3 men and 2 women: {total_groups}")