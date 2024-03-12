# This programme reads in a string and strips any leading or trailing spaces.
# It also converts all letters to lowercases.
# Finally it outputs the lengths of the original string and the normalised one

# Author: Grace Mary Smyth

rawstring = input("Please enter a string: ")
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len(rawstring)
lengthofnormalised = len(normalisedstring)

print(f"That string normalised is: {normalisedstring}")
print(f"We reduced the input string from {lengthofrawstring} to {lengthofnormalised} characters")
