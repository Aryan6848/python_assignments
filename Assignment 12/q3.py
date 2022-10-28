
n=2

while (n<=100):
    i=2
    while(i<=n**(1/2)):
        if(n%i==0):
            break
        i+=1
    else:
        print(n)
    n+=1

