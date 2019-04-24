# imports random module
from random import *

guess_left = 5
secret_num = randint(1,100)

print("*** Guess the Number ***")
print("Welcome to the guess the number game.")
print("You have", guess_left, "chances to guess the number between 0 and 100")

# loop a max of 5 times for player to guess
for i in range(guess_left, 0, -1):
    # get input from the user
    guess_num = int(input("Enter a number between 0 and 100: "))

    if guess_num > secret_num and i != 1:
        print("Too high, guess again\n")
    elif guess_num < secret_num and i != 1:
        print("Too low, guess again\n")
    else:
        if guess_num == secret_num:
            print("Congratulations")
            break

else:
    print("\nSorry, you guessed incorrectly, the right number is", secret_num)

