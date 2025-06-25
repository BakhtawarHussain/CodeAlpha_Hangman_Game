import random

words = ["python", "tokyo", "euphoria", "moon", "stigma", "lie"]
word = random.choice(words)
guessed_letters = ''
turns = 6

def display_hangman(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    return display_word

while turns > 0:
    current_word = display_hangman(word, guessed_letters)
    print("Word:", current_word)
    print("Guessed letters:", guessed_letters)

    guess = input("Guess a letter: ")

    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
    elif guess in word:
        guessed_letters += guess
        print("Good job!")
    else:
        turns -= 1
        print("Incorrect guess. You have", turns, "turns left.")

    if current_word == word:
        print("You won! The word was:", word)
        break

    if turns == 0:
        print("Game Over! The word was:", word)