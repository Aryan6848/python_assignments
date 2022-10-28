n1=int(input("Enter the number1 "))
n2=int(input("Enter the the number2 "))
i=2
while(i<=min(n1,n2)):
    if n1%i==0 and n2%i==0:
        print("the numbers are not coprime")
        break
    i+=1
else:
    print("the numbers are coprime")

