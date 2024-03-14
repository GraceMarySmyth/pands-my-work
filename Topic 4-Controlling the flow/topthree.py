# Programme generates 10 random numbers (0-100)
# Prints them out
# Then prints out the top three

# using a list to storer and manipulate the numbers

import random
# I programming in the general case
howmany    = 10
tophowmany = 3
rangefrom  = 0
rangeto    = 100 

numbers = []

for i in range(0, howmany):
    numbers.append(random.randint(rangefrom,rangeto))
print(f"{howmany} random numbers\t {numbers}")

# Iam keeping the original list, maybe I dont need to
topones = numbers.copy()

topones.sort(reverse = True)
print("The top {tophowmany} are \t\t {topones[0:tophowmany]}")
