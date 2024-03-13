# Programme that reads a students percentage marks
# Prints our corresponding grade
# This programme should also check that programme is valid ie not less than 0 and greater than 100

# Author: Grace Mary Smyth

percentage = float(input("Enter the percentage: "))
#print (percentage)

#careful with ands and ors
if percentage <0 or percentage > 100:
    # later we will show you error handling
    # this should really throw an error
    print ("Please enter a number between 0 and 100")
elif percentage < 40 :
    print ("Fail")
elif percentage < 50 :
    print ("Pass")
elif percentage < 60 :
    print ("Merit 2")
elif percentage <70 :
    print ("Merit 1")
else: # the only option left is between 70 and 100
    print ("Distinction")
    