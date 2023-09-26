import random
def Mental_maths():
    number_to_guess = random.randint(1,100)
    attempt = 0

    print("Welcome to Mental Maths")
    print("There's a lost number from 1 to 100, please can you help us find it?")

    while True:
        user_guess = int(input("Enter the winning number: "))
        attempt +=1

        if user_guess < number_to_guess:
            print("Too low! Try again")
        elif user_guess > number_to_guess:
            print("Too high! Try again")
        else:
            print(f"Congrats!Got it on your {attempt} attempt.Good job")
            break
print(Mental_maths())