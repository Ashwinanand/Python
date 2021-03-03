#Author : Anand Veerarahavan
#Student ID : 500187737

def calculate(a1,a2):

    print("Addition value ", a1+a2)

    if a1>a2:
        print("Subtraction Value", a1-a2)
    else:
        print("Subtractinon Value",a2-a1)

    print("Multiplication value", a1*a2)
    print("Division value", a1 / a2)

def main():

    print("Hello, welcome to main function!")
    print("Performing calculations on the data")
    calculate(5,4)

main()

