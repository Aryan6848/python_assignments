""" month=int(input("enter the month number"))
match month:
    case 1:
        print(31)
    case 2:
        print(28 or 29)
    case 3:
        print(31)
    case 4:
        print(30)
    case 5:
        print(31)
    case 6:
        print(30)
    case 7:
        print(31)
    case 8:
        print(31)
    case 9:
        print(30)
    case 10:
        print(31)
    case 11:
        print(30)
    case 12:
        print(31)
    case _ :
        print("no match")
"""

#second method
month =int(input("Enter the month number"))
if month in (1,3,5,7,8,10,12):
    print(" 31 days")
elif month == 2:
    print("28 days and 29 ")
elif month in (4,6,9,11) :
    print(" 30 days ")
else :
    print("Invalid choice")
    
