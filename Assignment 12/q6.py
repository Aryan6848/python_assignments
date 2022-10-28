n=int(input("enter the value of n"))
k=2
while k<=n:
    i=2
    while i<=k**(1/2):
        if((k%i)==0):
            break
        i+=1
    else:
        print(k,"prime")
    k+=1