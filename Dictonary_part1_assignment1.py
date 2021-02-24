""" Author:
Student ID : 500187737
Student Name : Anand Veerarahavan
"""
"""About Dictionaries : Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates."""
# Creating a dictonary :

dictionary1 = {'studentName': 'Anand', 'studentID': 500187737 , 'courseName': 'AI and DS'}

# Accessing and printing from a dictionary
print("The student name :", dictionary1['studentName'])

print("The student ID :", dictionary1['studentID'])

print("The course name :", dictionary1['courseName'])

# Deleting items in a dictonary

print("Orginal dictonary", dictionary1)

del dictionary1['courseName']

print("Deleting item in a dictionary", dictionary1)

# Clearing the dictionary

dictionary1.clear()

print("After deleting the dictionary", dictionary1)
