# Write a program that counts how many times it was run
# will have to store data outside of memory, and that is accessible each time the program is run, (persistent data)
# normally use a database for something like this, but we can use a file
# Author: Grace Mary Smyth

FILENAME = "count.txt"
def readnumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
# test it
'''
num = readnumber()
print(num)
'''
# Write a function that takes in a number and overwrites a file with that number (count.txt)
# test it and check that the file has been changed
def writenumber(number):
    with open(FILENAME, "wt") as f:
        #write takes a string so we need to convert it
        f.write(str(number))

# test it
'''
writenumber(3)
'''
# a program that, uses these two functions, to count how many timesthe program has been run

# main
num = readnumber()
num += 1
print(f"we have run this program {num} times")
writenumber(num)