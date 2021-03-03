#Author : Anand Veerarahavan
#Student ID : 500187737
def calc_tax(amt, txrate):
    global tax
    tax = amt*txrate
    return tax


def main():
    final = calc_tax(85,5)
    print("Tax amt is :", final)

main()
