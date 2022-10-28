year =int(input("Enter the year "))
print(("leap year" if(year%400==0) else "not a leap year" )if year%100==0 else (" Leap Year" if year%4==0 else "Not a Leap Year"))
