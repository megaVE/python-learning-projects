import random
import hangman_art, hangman_words

lives = 6
attempts = []
chosen_word = random.choice(hangman_words.word_list)

display = []
for _ in chosen_word:
    display += "_"

print(hangman_art.logo)
print(hangman_art.stages[lives])

while lives and "_" in display:
    print(f"\n{display}\n")
    print(f"Already tried: [{', '.join(attempts)}]\n")
    guess = input("Guess a letter: ").lower()
    print("")

    if guess in attempts:
        print("You have already tried this letter before!")
    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess
        print("Correct!")
    else:
        attempts += guess
        lives -= 1
        print(hangman_art.stages[lives])
        print("Wrong Guess!")

# Feedback

print(f'\nThe word was "{chosen_word}".')
if(lives):
    print("You Win!")
else:
    print("You Lost!")