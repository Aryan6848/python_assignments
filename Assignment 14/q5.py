n=int(input("Enter the number of number you want to enter "))
i=1
l1=[]
while i<=n:
    l1.append(int(input()))
    i+=1
print("The minumum value is ",min(l1))