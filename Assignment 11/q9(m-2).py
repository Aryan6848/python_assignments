
n=int(input("enter the number" ))
sum=0
k=1
while n!=0 :
    r=n%2
    sum=sum+r*k
    n=n//2
    k=k*10

print(sum)
