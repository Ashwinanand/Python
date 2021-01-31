import random
print()
print("Random Number: ",random.random())
t1 = (1, 3, 5, 7, 9)
l1 = [101, 207, 308, 403, 502]
print()
print("From the tuple {1,3,5,7,9}: ",random.choice(t1))
print()
print("From the list {101,207,308,403,502}: ",random.choice(l1))
print()
print("Random uniform example (range {1-8} ) :",random.uniform(1, 8))
print()
print("Random integer example :",random.randint(3, 8))
print()

