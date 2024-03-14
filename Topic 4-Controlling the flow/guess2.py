# programme modified from programme guess1.py
# This programme also states if the number to too low or too high
# Author: Grace Mary Smyth

numbertoguess = 50
guess = int(input("Please guess the number: "))
while guess != numbertoguess:
    if guess <numbertoguess:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was ", numbertoguess)