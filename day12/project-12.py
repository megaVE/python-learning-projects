#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

answer = random.randint(1,100)
attempts = 10

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")

if dificulty == 'hard':
    attempts = 5

while attempts:
    print(f"Your have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}")
        break

    attempts -= 1
    
    if attempts:
        print("Guess again")
print("You've run out of guesses, you lose.")