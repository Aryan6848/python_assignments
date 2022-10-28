n=int(input("Enter the given number "))
k=n+1
while 1<=n:
    i=2
    while i<=k**(1/2):
        if(k%i==0):
            break
        i+=1
    else :
        print(k,"Prime")
        break
    k+=1