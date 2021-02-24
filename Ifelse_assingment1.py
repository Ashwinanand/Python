""" Author:
Student ID : 500187737
Student Name : Anand Veerarahavan
"""
# IF - ELSE - ELIF and nested ELIF
"""Used in scenarios where all the possible outcomes can be predicted or predetermined and also the action has to be perfomed based on the conditions satisfied"""
# Create a login based on age :
""" Conditions:
User must be greater than 17 years
User must not have negative age values
User cannot have age as 0"""

age = int(input("Enter the age: "))
if age < 0:
    print("Age cannot be negative")

elif age == 0:
    print("Invalid age")

elif age > 17:
    if age < 100:
        print("Authorized to login")
    else:
        print("Age cannot exceed 100")
elif age <= 17:
    print("Age criteria does not match, come back when you are 17 or older")
