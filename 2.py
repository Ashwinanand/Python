#Author : Anand Veerarahavan
#Student ID : 500187737

#Function with argument
def my_function(fname):
  print(fname + " Name ")

my_function("Email")
my_function("Anand")
my_function("Veerarahavan")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Name", "Anand", "Veerarahavan")

# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")

evenOdd(2)
evenOdd(3)


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

