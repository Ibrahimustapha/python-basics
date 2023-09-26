import random

def choose_a_word():
    word_list = ["Network","Zebra","Hitman","Jungle","Yellow","Xylophone","Greenland","Destiny","Liquid","Origin","Trampoline","Favorite","Application","Macaroni"]
    return random.choice(word_list)
def hang_man():
    word = choose_a_word()
    guessed_letters = []
    attempts = 10

    print("Welcome to Hangman")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word +=letter
            else:
                display_word += "_"

print(f"Word: {hang_man()}")