""" Author:
Student ID : 500187737
Student Name : Anand Veerarahavan
"""
#Break statements
dig = 10
while dig > 0:
    print ('The current value is:', dig)
    dig = dig -1

    if dig == 5:
        break
print ("Completed!")

#Continue statements
dig = 11
while dig > 0:
    dig -= 1
    if dig == 7:

        continue
    print ('The current value is:', dig)
print ("Completed!")
