from random import randint
from sys import exit

print("*****Guess the number between 0-100*****")
number = randint(0,100)  # random number

while True:
    guess = input("Enter your guess>")
    
    if int(guess) > number:
        print("Guess big.")
        continue 
    elif int(guess) < number:
        print("Guess small.")
        continue
    else:
        print("\nRight!")  # add a new line
        break

exit(0)  # exit the program