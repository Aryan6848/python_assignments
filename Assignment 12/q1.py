n=int (input("Enter the number "))
temp=n
sum=0
while temp!=0:
    r=temp%10
    sum=sum*10+r
    temp=temp//10

print("reverse of the number is ",sum)
