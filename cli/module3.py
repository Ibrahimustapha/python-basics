##Firstname = "Destiny"
##Last_name = "Ngozi"
#Middle_name = "Samuel"#########
#e#_mail = "desty_ngo_samuel##@gmail.com"
#d#ef email_generator (Firs#tname, Last_name):
  ##  email = f"{Firstname}.{Last_name}@gmail.com".lower()
#  ##  return email#########
#def num_repeat(num):
#    for i in num:
#        if num.count(i) > 1:#
#            print(f"The item that got repeated is {i} and it was repeated {num.count(i)} times",)
#            break
def name_startswith(names):
    for i in names:
        if i.startswith("M"):
            print(i)
            break

from math import pi
def areaofacircle(r):
    area = (pi + r)**2
    return area