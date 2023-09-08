profile = {'name':"Micheal", 'age':"17", 'class':"SS3"}
for i in profile:
    print(i)
print("############################################")
for i in profile.keys():
    print(i)
print("############################################")
for i in profile.values():
    print(i)
print("############################################")
for i in profile.items():
    print(i)
print("############################################")
for keys,values in profile.items():
    print(keys,values)
print("############################################")
for key,values in profile.items():
    print(keys,"==",values)
count = 4
while count <= 10:
    print(count)
    count+=1

for i in range(0,10):
    print(i)
name =["Mustapha","Mazeedah","Samuel","Kehinde"]
counter = 0
while counter < len(name):
    if name[counter] == "Mazeedah":
        counter +=1
        continue
    print(name[counter])
    counter +=1
print("The codes are doing the same thing ##################")
name_to_skip="Mazeedah"
index = 0
while index < len(name):
    current_name= name[index]
    if current_name == name_to_skip:
        index +=1
        continue

    print (current_name)

    index +=1