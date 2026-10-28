# guess.py: guess the number the wizard is thinking of

import random

secret = random.randint(1, 20)
guesses = 0

print("The wizard is thinking of a number from 1 to 20.")

while True:
    guess = int(input("Your guess: "))
    guesses = guesses + 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Got it in {guesses} guesses! The wizard is impressed.")
        break
