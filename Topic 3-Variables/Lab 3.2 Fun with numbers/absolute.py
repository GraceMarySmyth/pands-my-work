# Give the absolute value of a number

# Author: Grace Mary Smyth

# In the question, number is ambiguous but the output implies that we should be dealing with floats
# Casting the input into a float
number = float(input("Enter a number: "))
absolutevalue = abs(number)
print("The absolute value of {}is {}".format(number, absolutevalue))
