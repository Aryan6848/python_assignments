n=int (input("Enter the no. of numbers you want to enter "))
l1=[]
i=1
while i<=n:
    l1.append(int(input()))
    i+=1
print("the max number is ",max(l1))