# Programme that reads in two numbers and outputs the integer answer and remainder
# Author: Grace Mary Smyth

x = int(input("Enter the first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = x%y    # % gives the remainder

print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))