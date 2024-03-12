# rounds a number
# Be careful of round
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# So do not use when accuracy is essential
# Author: Grace Mary Smyth

numbertoround = float(input("Enter a float number: "))
roundednumber = round(numbertoround)
print ('{}rounded is {}'.format(numbertoround,roundednumber))