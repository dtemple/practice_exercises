# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

num = random.randint(1,9)

print("Welcome to the guessing game. Type 'exit' anytime to quit. \n")

def endgame(outcome, num_guesses):
    if outcome == 0:
        print("Thanks for playing. You took " + str(num_guesses) + " guesses. \n")
    else:
        print("Congrats, you got it! You took " + str(num_guesses) + " guesses. \n")

def check_guess(guess,num_guesses,num):
    while guess != num:
        if guess < num:
            guess = input("Too low. Guess again! ")
            num_guesses += 1
            if guess == "exit":
                outcome = 0
                endgame(outcome, num_guesses)
            guess = int(guess)
        else:
            guess = input("Too high. Guess again! ")
            num_guesses += 1
            if guess == "exit":
                outcome = 0
                endgame(outcome, num_guesses)
            guess = int(guess)
    endgame(1,num_guesses)


guess = input("I'm thinking of a number between 1 - 9. Can you guess it?\n")
if guess == "exit":
    outcome = 0
    num_guesses = "no"
    endgame(outcome, num_guesses)
else:
    guess = int(guess)
    num_guesses = 1
    check_guess(guess,num_guesses,num)