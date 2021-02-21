Name = input("Enter a name :\t")
Degree_Name = input("Enter the degree name :\t")
Credits_obtained = int(input("Enter the Credit taken so far :\t"))
Credits_total = int(input("Enter the total number of credits required  :\t"))
Credits_remaining = int(Credits_total) - int(Credits_obtained)
if Credits_remaining > 0:
    print("\n\tSummary :")
    print("\tName : %s\n\tName of the degree : %s\n\tCredits taken so far : %d\n\tTotal number of Credits required :%d\n\tNumber of credits needed to graduate: %d\n\t"%(Name,Degree_Name,Credits_obtained,Credits_total,Credits_remaining))
else:
    print("Credits obtained cannot be greater than total credits")


