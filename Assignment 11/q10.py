n=int(input("Enter the number "))
sum=0
k=1
while n!=0 :
    r=n%8
    sum=sum+r*k
    n=n//8
    k=k*10

print(sum)


