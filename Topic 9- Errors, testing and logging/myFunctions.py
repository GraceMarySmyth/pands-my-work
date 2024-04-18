# make a function called Fibonacci in a module called myFunctions
# The Fibonacci function should take in a number and return a list containing a Fibonacci sequence of that many numbers
# A Fibonacci sequence is a series of numbers that starts off with 0 and 1 and each subsequence number is the sum of the previous two.
# write the test cases before we write the function body
# Author: Grace Mary Smyth

import logging
logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    a = 0
    b = 1
    fibonaccisequence = [0]
# We have one in the list already so number -1 times
# This is not the most efficient code
# could of used yield
    for i in range (1, number):
        fibonaccisequence.append(b)
# this is a funky code make a=b and b=a+b
        a, b = b, a + b 
    logging.debug("%d: %s", number, fibonaccisequence)

    if number == 0:
    return[]
    return []

    if number <0:
        raise valueerror("number must be >0")

if __name__ == '__main__':
    # Tests will go here
    print("All good")

return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'

try:
    fibonacci(-1)
except ValueError:
    # we want this exception to be thrown
    # so this is an example where we want to do nothing
    pass
else:
    # if the exception was not thrown we should throw
    # Assertion error
    assert False, 'fibonacci missing ValueError'
    # or
    #raise AssertionError("fibonacci no valueError ")