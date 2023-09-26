import random

def choose_a_word():
    Word = ["Fashion","Aunty","Chewing","Macaronni","Fanta","Sewage","Water","Dishes"]
    return random.choice(Word)
def choose_word():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman")

    while attempts >0:
        display_word = ""
        for letter in ord:
            if letter in guessed_letters:
                display_word +=letter
            else:
                display_word += "_"

    print(f"Word: {display_word}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in language:
        attempts -= 1

    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: {language}")
        break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was: {language}")

print(choose_word())