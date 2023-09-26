numd = int(input( "Enter your number: "))
numg = int(input( "Enter your other number: " ))
opr = input("Enter operator: ")
if opr == '+':
    ans = (numd + numg)
    print(f'your ans is {ans}') 
elif opr =='-':
    ans = (numd - numg)
    print(f'your ans is {ans}') 
elif opr =='*':
    ans = (numd * numg)
    print(f'your ans is {ans}')
elif opr == '/':
    ans = (numd / numg)
    print(f'your ans is {ans}')
elif opr == '**':
    ans = (numd ** numg)
    print(f'your ans is {ans}')
elif opr == '%':
    ans = (numd % numg)
    print(f'your ans is {ans}')
else:
    print("SYNTAX ERROR")