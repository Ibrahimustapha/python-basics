def email_generator (first_name, middle_name):
    email = f"{first_name}.{middle_name}@yahoo.com".lower()
    return email
print(email_generator("Munachi","Micheal"))
def num_repeat(num):
    for i in num:
        if num.count(i) > 1:
            print(f"The item that got repeated is {i} and it was repeated {num.count(i)} times",)
            break

def name_startswith(names):
    for i in names:
        if i.startswith("M"):
            print(i)
            break

from math import pi
def areaofacircle(r):
    area = (pi + r)**2
    return area