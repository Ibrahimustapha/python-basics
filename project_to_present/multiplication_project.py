Table = int(input("Enter the multiplication table: "))
term = int(input("What term do you want to stop: "))
for i in range(1,term+1):
    print(Table,"*",i,"=", Table*i )