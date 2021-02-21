#Number of minutes (talktime)
noOfMinutes = float(input("The Number of call minutes Used:"))
#Credit already present in account
creditAvailable = float(input("credit available:"))
#Print the number of minutes
print(noOfMinutes)
#check condition for more than 200 minutes
minutesExceeded = noOfMinutes > 200
if minutesExceeded:
#If talktime more than 200 minutes
#Calculate remaining minutes
    remainingMinutes = noOfMinutes - 200
#Calculate cost for 200 minutes
    costFor200Minutes = 200 * 0.25
    costForExceededMinutes = remainingMinutes * 0.35
    totalCost = costFor200Minutes + costForExceededMinutes

else:
#If talktime less than 200 minutes
    totalCost = noOfMinutes * 0.25
#Taxes calculation
taxes = .13 * totalCost
#Output
print("Customer account number: \t\t\t\t 12345")
print()
print("Minutes used:\t\t\t\t\t\t\t", noOfMinutes)
print()
print("Charge for the first 200 minutes@ 0.25:\t", costFor200Minutes if minutesExceeded else totalCost)
print()
print("Charge for the remaining minutes@ 0.35:\t", costForExceededMinutes if minutesExceeded else 0)
print()
print("Taxes:\t\t\t\t\t\t\t\t\t", taxes)
print()
print("Credits:\t\t\t\t\t\t\t\t", creditAvailable)
print()
#Print summary
inf0 = "Amount can be payed from Credit"
print("Total bill without credit deduction:\t", inf0 if totalCost + taxes < 0 else totalCost + taxes)
print()
print("Total bill:\t\t\t\t\t\t\t\t", inf0 if totalCost + taxes - creditAvailable < 0 else totalCost + taxes - creditAvailable)