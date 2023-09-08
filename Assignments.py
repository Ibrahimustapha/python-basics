#list.append(x) # append x to end of list
# list.extend(iterable) # append all elements of iterable to list
# list.insert(i, x) # insert x at index i
# list.remove(x) # remove first occurance of x from list
# list.pop([i]) # pop element at index i (defaults to end of list)
# list.clear() # delete all elements from the list
# list.index(x[, start[, end]]) # return index of element x
# list.count(x) # return number of occurances of x in list
# list.reverse() # reverse elements of list in-place (no return)
# list.sort(key=None, reverse=False) # sort list in-place
# list.copy() # return a shallow copy of the list
#friends = ["Chucks", "Elijah", "Hector", "Miracle", "Samuel"]
#siblings = [1, 2, 4 , 5, 2]
#ages = [15, 13, 14, 13 ,13]
#friends.append("Daniel")
#print(friends)
#friends.extend(ages)
#print(friends)
#friends.insert(2, "siblings")
#print(friends)
#friends.remove("Chucks")
#print(friends)
#friends.pop(8)
#print(friends)
#siblings.clear()
#print(siblings)
#print(ages.index(13))
#print(friends.count("Elijah"))
#friends.reverse()
#print(friends)
#friends.copy()
#ages.sort(key=15, reverse=False)
#print(ID_information)
#Assignment
#Write a python condition that checks if name is Korede and age is 15
#if the condition is true, it must print "You can buy a new phone"
#else :it will print "You have to wait for more years to buy a new phone"
name = "Korede"
age = 14
statment1 = "You can buy a new phone""You can buy a new phone"
statment2 ="You have to wait for more years to buy a new phone"
if(age == 15):
    print(statment1)
else:
    print(statment2)    