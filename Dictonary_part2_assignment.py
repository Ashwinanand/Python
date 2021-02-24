""" Author:
Student ID : 500187737
Student Name : Anand Veerarahavan
"""
"""About Dictionaries : Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates."""

# Creating a new dictionary

dictionary1={}
dictionary2 = {'name': 'Anand' ,'age':25 , 'sex':'male', 'id': 500187737 , 'coursename': 'AI and DS', 'experience(years)': 1.5}
print("New dictionary ", dictionary2)

#Length of the dictionary
print('Length of the dictionary ', len(dictionary2))

#String Representation of the dictionary
print('String representation ', str(dictionary2))

#Data type of the dictionary
print('Data type of dictonary ', type(dictionary2))

#Getting keys of the dictionary
print('Getting a specific key value(Name) ', dictionary2.get('name'))

#Getting all items of the dictionary
print('Getting all the items in the dictionary ', dictionary2.items())

#Getting a list of keys from the dictionary
print('Getting a list of keys from the dictionary ', dictionary2.keys())

#Update the empty dictionary with values from another dictionary
dictionary1.update(dictionary2)

#Updated dictionary
print('Updated dictionary 1 : ', dictionary1)

#Returning a list of values
print('Returning list of values from dictionary ', dictionary1.values())

#Sorting in dictionary
dictionary3 = {'a':'3', 'b':'89', 'c':'5', 'd':'0'}

sortedDict = sorted(dictionary3.items())

print("Sorting the dictionary matching the items")

for k,v in sortedDict:

    print("The key : ", k,"- The corresponding value : ", v)

print("Thus the dictionary is sorted : ", sortedDict)

# Serching keys in a dictionary

dictionary4 = {'Anand':25 ,'Mark':70, 'Luke':34, 'Graham': 45}
print("Names and age's dictionary :",dictionary4)
search_parameter = int(input('Search by age - Enter an age: '))
bvalue = True

for name, age in dictionary4.items():

    if age == search_parameter:

         print(name)
         bvalue = False

if bvalue == True:
    print("Key not found for the given age")
else:
    print("Key found for the entered age")
