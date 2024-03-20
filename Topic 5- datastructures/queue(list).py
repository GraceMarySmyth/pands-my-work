# Programme that puts 10 random numbers into a queue(list)
# Then outputs all the values in the list
# Then take all the numbers from the queue one at a time, print it and the current numbers in the queue
# Ther command pop[0] takes the first element out of a list

import random
queue = []
rangeto = 100
numberofnumbers = 10

for n in range(0,numberofnumbers):
    queue.append(random.randint(0,rangeto))
    print (f"queue is{queue}")
    

while len(queue) != 0:

    currentnumber = queue.pop(0)
    print("current number is", {currentnumber}, "and the queue is", [queue])

print ("The queue is now empty")
