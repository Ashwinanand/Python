myList =["Python","is","a","programming","language"]
print("This is my first list", myList)
print("Length of the list is :\t", (len(myList)))
print("This is a part of the list \t", myList[2:])
myList2 = ["It", "is", "easy", "to learn"]
myList.append(myList2)
print("The appended list", myList)
mysubList =myList[0:5]
print("This is my sublist \t", mysubList)
extendList=["This", "is", "extension"]
myList.extend(extendList)
print("This is my extended list \t", myList)
print(myList.count("is"))
poppedvalue = myList.pop(3)
print('Popped Value:', poppedvalue)
print("Final List", myList)



