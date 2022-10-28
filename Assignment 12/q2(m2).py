n=int(input("enter the number "))
i=5
if(n==1):
    print("number is not prime ")
    exit()
if(n%2==0 or n%3==0):
        print(" number is not prime ")
        exit()
while i<=n**(1/2) :
    
    if(n%i==0 and n%(i+2)==0):
        print("number is not prime ")
        break
    i+=6

else :
    print("number is prime")                                