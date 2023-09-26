import random

# def guess_the_number():
#     number_to_guess = random.randint(1,100)
#     attempts = 0

#     print("Welcome to Guess the number")
#     print("There's a number from 1 t0 100. Can you guess it?")

#     while True:
#         user_guess = int(input("Enter your lucky number"))
#         attempts =+1

#         if user_guess < number_to_guess :
#             print("Too low! Try again.")
#         elif user_guess > number_to_guess :
#             print("Too high! Try again.")
#         else:
#             print(f"Congrats! You got it on your {attempts} attempt")
#             break

# # if __name__ == "__main__":
# print(guess_the_number())


def Number_war():
    number_to_guess = random.randint(1,100)
    attempt = 0

    print("Welcome to Number_warr")
    print("There's a number from 1 t0 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your lucky number"))
        attempt +=1

        if user_guess < number_to_guess :
            print("Too low! Try again.")
        elif user_guess > number_to_guess :
            print("Too high! Try again.")
        else:
            print(f"Congrats! You got it on your {attempt} attempt")
            break

print(Number_war())