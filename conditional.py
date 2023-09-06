# name = "Micheal"
# school = "King's College, Lagos"
# real_name = input('Enter your name')
# if real_name == "Micheal" or real_name =="Mustapha":
#     print(school)
# else:
#     print("You're not a student of this school")

# import random

# name = input('what is your name: ')
# question = int(input('How many questions qustions do you want to set? '))
# score = 0
# for i in range(1, question+1):
#     first_number = random.randint(1,10)
#     second_number = random.randint(5,10)
#     answer = first_number*second_number
#     print('what is', first_number, '*', second_number)
#     guess = int(input('Enter your anwser'))
#     if guess == answer:
#         print('You are right')
#         score+=1
#     else:
#         print('You are wrong')
# print('You scored', score, 'of', question)
# Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
# Credits = int(input('Enter your number of credits taken: '))
# if Credits <= 23:
#     print('The student is a freshman')
# elif Credits >=24 and Credits <=53:
#     print('The student is a sophomore')
# elif Credits >=54 and Credits <=83:
#     print('The student is a juniour')
# elif Credits >=84:
#     print('The student is a Senior')
# else:
#     print('nothing')
# # write a program that counts the number of vowels(a,e,i,o,u) in a given string
# names = input('Enter your name')
# vowels = ('a','e','i','o','u')
# if names
# Ask the user to enter a temperature in Celsius. The program should print a message based
# on the temperature:
# • If the temperature is less than -273.15, print that the temperature is invalid because it is
# below absolute zero.[]
# • If it is exactly -273.15, print that the temperature is absolute 0.[]
# • If the temperature is between -273.15 and 0, print that the temperature is below freezing.[]
# • If it is 0, print that the temperature is at the freezing point.[]
# • If it is between 0 and 100, print that the temperature is in the normal range.[]
# • If it is 100, print that the temperature is at the boiling point.
# • If it is above 100, print that the temperature is above the boiling point
temperature = float(input('Enter your temperature in  celsius: '))
if temperature < -273.15:
    print('the temperature is invalid because it is below absolute zero.')
elif temperature == -273.15:
    print('that the temperature is absolute 0')
elif temperature > -273.15 and temperature < 0:
    print('the temperature is below freezing')
elif temperature == 0:
    print('the temperature is at the freezing point')
elif temperature > 0 and temperature < 100:
    print('the temperature is in the normal range')
elif temperature == 100:
    print('the temperature is at the boiling point.')
elif temperature > 100:
    print('the temperature is above the boiling point.')
else:
    print('Not a number')
