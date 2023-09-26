import random

# def choose_word():
#     word_list = ["python", "java", "javascript", "ruby", "popcorn"]
#     return random.choice(word_list)

# def hangman():
#     word = choose_word()
#     guessed_letters = []
#     attempts = 6

#     print("Welcome to Hangman!")
    
#     while attempts > 0:
#         display_word = ""
#         for letter in word:
#             if letter in guessed_letters:
#                 display_word += letter
#             else:
#                 display_word += "_"

#         print(f"Word: {display_word}")
#         print(f"Guessed letters: {', '.join(guessed_letters)}")
#         print(f"Attempts left: {attempts}")

#         guess = input("Guess a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input. Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You already guessed that letter.")
#             continue

#         guessed_letters.append(guess)

#         if guess not in word:
#             attempts -= 1

#         if "_" not in display_word:
            
#             print(f"Congratulations! You guessed the word: {word}")
#             break

#     if attempts == 0:
#         print(f"Sorry, you're out of attempts. The word was: {word}")

# print(hangman())

def choose_a_word():
    word_list = ["Network","Zebra","Hitman","Jungle","Yellow","Xylophone","Greenland","Destiny","Liquid","Origin","Trampoline","Favorite","Application","Macaroni"]
    return random.choice(word_list)
def hangman():
    word = choose_a_word()
    guess_letter = []
    attempts = 10
    
    print("Welcome to Word guesser")
    
    while attempts > 0:
        display_word = ""
        for letter in word:
            if