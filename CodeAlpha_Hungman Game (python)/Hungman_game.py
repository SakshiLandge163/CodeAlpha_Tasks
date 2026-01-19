import random

words = ["python", "apple", "chair", "train", "house"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to the Hangman Game")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only a single letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_wrong - wrong_guesses)

else:
    print("\nYou lost! The word was:", word)
