# messing with plotting 
# Author: Grace Mary Smyth

# a program that makes a list, called salaries, that has 10 random number (20000 -80000)

import numpy as np 
import matplotlib.pyplot as plt

# it is a good idea to have your absolute values set into variables at the begining of your programme
minsalary = 20000
maxsalary = 80000
numberofentries = 10

np.random.seed(1) # ensures the random numbers are the same each time (easire to debug!)
salaries = np.random.randint(minsalary, maxsalary, numberofentries)
ages = np.random.randint(low=21, high=65, size =numberofentries) # preferable to have absolute values at the top

'''
print(salaries)
'''
plt.scatter(ages, salaries) # this will be random
# plt.show()

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints* xpoints  # multiply each number by itself

plt.plot(xpoints, ypoints, color='r', label = "x squared")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
# plt.show()
plt.savefig('prettier-plot.png')