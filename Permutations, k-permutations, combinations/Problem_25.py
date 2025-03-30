#  A password consists of 5 different symbols. There are 115 symbols available.
# (a) How many different passwords exist, when the order matters and each symbol can be used only once? Solution
# 1.8 · 1010
from math import perm

n = 115
k = 5
passwords = perm(n, k)
print(f"Number of possible passwords: {passwords:.1e}")

# (b) If you try to guess the password and each guess takes 10 s, how long it would take to make all the guesses?
total_time_seconds = passwords * 10
seconds_per_year = 60 * 60 * 24 * 365
years = total_time_seconds / seconds_per_year

print(f"Time to guess all passwords: {years:.0f} years")