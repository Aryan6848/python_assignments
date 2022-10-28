n1=int(input("Enter the number "))
n2=int(input("Enter the number "))
n=min(n1,n2)
while n<=max(n1,n2):
    i=2
    while(i<=n**(1/2)):
        if(n%i==0):
            break
        i+=1
    else:
        print(n,"is prime")
    n+=1
