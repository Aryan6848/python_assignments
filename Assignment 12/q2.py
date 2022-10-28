n=int(input("enter the number "))
i=2
while i<=n**(1/2) :
    if n%i==0 :
        print("number is not prime")
        break
    i+=1
else :
    print("Number is prime")