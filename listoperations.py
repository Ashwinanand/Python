#Names of people invloved : Charan, Midhun and Anand.
#importing random library
import random
#creating an empty list
appe1=[]
#defining elements of a list
appe1=[1, 2, 3, 4, 5, "apple", "orange", "grape", "Banana", "cherry"]
#printing the defined list
print(appe1)
#popping the list
appe1.pop(1)
appe1.pop(7)
print("After popping")
#printing the popped list
print(appe1)
#Removing the items from the list
appe1.remove("apple")
appe1.remove(3)
#print the list after removing
print("After two removing")
print(appe1)
#inserting the items in the list
appe1.insert(1,"insert1")
print("after inserting")
#print after inserting
print(appe1)
#get the length
print("length of the list is \t",(len(appe1)))
#extending the list
extended=[23,"avacado"]
appe1.extend(extended)
#print the extended list
print(appe1)
#create a sub list
subApp=[1,2,3]
#append the list appe1
appe1.append(subApp)
#print the appended list
print(appe1)
#print the first item of sub list
print(subApp[0])
#print the random item of the original list
print(random.choice(appe1))

