n=int(input("Enter the number of number you want to enter "))
i=1
l1=[]
while i<=n:
    l1.append(int(input()))
    i+=1

print(l1)
sum=0
for e in l1:
    sum+=e

print("The sum is ", sum)