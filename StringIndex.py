string, letter = input("Enter").split()
for c in string:
    if letter == c:
        print("Yes", string.index(c))
        break

else: print("no")
