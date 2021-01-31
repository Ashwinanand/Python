print("The Test scores program")
print()
print("Enter 3 test scores")

total_score = 0
total_score += int(input(" Enter test score 1 : "))
total_score += int(input(" Enter test score 2 : "))
total_score += int(input(" Enter test score 3 : "))

average_score = round(total_score / 3)
print()

print("Total Score is :  ", total_score, "\nAverage Score is : ", average_score)
print()
print("Bye")