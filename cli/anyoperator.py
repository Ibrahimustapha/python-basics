numd = int(input( "Enter your number: "))
numg = int(input( "Enter your other number: " ))
opr = input("Enter operator: ")
if opr == '+':
    ans = (numd + numg)/numd + 12 **2
    print(f'your ans is {ans}') 
elif opr =='-':
    ans = (numd - numg)/numd/ + 12 **2
    print(f'your ans is {ans}') 
elif opr =='*':
    ans = (numd * numg)/numd + 12 **2
    print(f'your ans is {ans}')
elif opr == '/':
    ans = (numd / numg)/numd + 12 **2
    print(f'your ans is {ans}')
elif opr == '**':
    ans = (numd ** numg)/numd + 12 **2
    print(f'your ans is {ans}')
elif opr == '%':
    ans = (numd % numg)/numd + 12 **2
    print(f'your ans is {ans}')
elif opr == '<':
    ans = f"{numd} is less than {numg}"
    print(f'your ans is {ans}')
else:
    print("SYNTAX ERROR")