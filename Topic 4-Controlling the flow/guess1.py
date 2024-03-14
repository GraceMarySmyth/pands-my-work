# Programme that prompts user to guess a number
# The programme continues until the correct number is guessed.
# Author: Grace Mary Smyth

numbertoguess = 30
guess = int(input("Please guess the number: "))
while guess != numbertoguess:
    print("Wrong")
    guess = int(input("Please guess again: "))

    if guess == numbertoguess: 
        print ("Well done! Yes the number was ", numbertoguess)