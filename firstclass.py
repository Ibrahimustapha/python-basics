number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
number3 = int(input("Enter your third number: "))
number4 = int(input("Enter your fourth number: "))
operation = input("Enter operation: ")
if operation == '+':
    answer = (number1 + number2 + number3 + number4)
    print(f'your answer is {answer}')
elif operation == '-':
    answer = (number1 - number2 - number3 - number4)
    print(f'your answer is {answer}')
elif operation == '*':
    answer = (number1 * number2 * number3 * number4)
    print(f'your answer is {answer}')
elif operation == '/':
    answer = (number1 / number2 / number3 / number4)
    print(f'your answer is {answer}')
elif operation == '**':
    answer = (number1 ** number2 ** number3 ** number4)
    print(f'your answer is {answer}')
elif operation == '%':
    answer = (number1 % number2 % number3 % number4)
    print(f'your answer is {answer}')
else:
    print("SYNTAX ERROR")