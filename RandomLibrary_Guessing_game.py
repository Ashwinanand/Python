import random
up = 20
down =1
tobeguessed = random.randint(down , up)
print(tobeguessed)
guess = 0
while guess!=tobeguessed:
    guess = int(input("Enter the val"))
    if guess>0:
        if guess > tobeguessed:
            print("Larger")
        elif guess < tobeguessed:
            print("Small")
    else:
        print("Sorry you gave up!")
        break

else:
    print("Congrats")
print("break statement")
