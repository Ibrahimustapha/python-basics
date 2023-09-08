#a function in python is a snippet of code
#used to perform a specific task
#DRY: don't reapet yourself
#Function allows you to reuse the code
#X = 98
#N = 77
#ADD = X + N
#print(ADD)

# def  define
#def add(a, b, c, d , e): #you are declared the function:
#        return a + b + c + d + e 
#print(add(4, 7, 9, 6, 2))
#
#def subtract(d , e): 
 #       return d - e 
#print(subtract(7, 9))

#def multiply(f, g):
#        return f * g 
#print(multiply(23, 13))

#def divide(h, j): 
#        return h - j 
#print(divide(34, 49))

#def exponetial(k, l): 
 #       return k ** l 
#pr#int(exponetial(7, 5))

#def modulus(v, w): 
#        return v % w 
#print(modulus(24, 100))
#The word infront of the  reserved(def) is called the name oof the function
#The word in the bracket of the function decleration is/are
#called the parameter of the function
#name = "zibra"
#age =765432
#if(name == "zibrass"):
#        print("zibra crossing")
#elif(name == "Kenturkey"):
#    print("KFC")
#elif(name == "Balablue"):
  ##      print("Tinubu")
#elif(name == "zibra"):
#       print("bubu zibra baby")
#elif(name == "Iasureyou"):
#       print("BuBu Buhari")
#else:
#        print("not applicable")

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
opr = input('Enter the type of operation: ')
if opr=='+':
    ans = num1 + num2
    print(f'Your final answeris {ans}')
elif opr=='-':
    ans = num1 - num2
    print(f'Your final answeris {ans}')
elif opr=='*':
    ans = num1 * num2
    print(f'Your final answeris {ans}')
elif opr=='/':
    ans = num1 / num2
    print(f'Your final answeris {ans}')
elif opr=='**':
    ans = num1 ** num2
    print(f'Your final answeris {ans}')
elif opr=='%':
    ans = num1 % num2
    print(f'Your final answeris {ans}')
else:
    print("invalid entry")

#numa = int(input('Enter first number: '))
#numb = int(input('Enter second number: '))
#numc = int(input('Enter third number: '))
#opr = input('Enter the type of operation: ')
#if opr=='+':
#    ans = numa + numb + numc
#    print(f'Your final answeris {ans}')
#elif opr=='-':
#    ans = numa - numb - numc
#    print(f'Your final answeris {ans}')
#elif opr=='*':
#    ans = numa * numb * numc
#    print(f'Your final answeris {ans}')
#elif opr=='/':
#    ans = numa / numb / numc 
#    print(f'Your final answeris {ans}')
#elif opr=='**':
#    ans = numa ** numb ** numc
#    print(f'Your final answeris {ans}')
#elif opr=='%':
#    ans = numa % numb % numc
#    print(f'Your final answeris {ans}')
#else:
#    print("invalid entry")
number1 = int(input('Enter first number: '))
number2 = int(input('Enter first number: '))
operation = input('Enter operation: ')
if operation == '+':
    answer = number1 + number2
    print(f'Your final answeris {answer}')
elif operation == '-':
    answer = number1 - number2
    print(f'Your final answeris {answer}')
elif operation == '*':
    answer = number1 * number2
    print(f'Your final answeris {answer}')
elif operation == '/':
    answer = number1 / number2
    print(f'Your final answeris {answer}')
elif operation == '**':
    answer = number1 ** number2
    print(f'Your final answeris {answer}')
elif operation == '%':
    answer = number1 % number2
    print(f'Your final answeris {answer}')
else:
    print("SyntaxError")