N=int (input("Enter the number "))
n=N
k=0.1
sum=0
count1=0
while n!=0 :
    r=n%2
    sum=sum+r*k
    k=k/10
    n=n//2
    count1+=1

print(count1)

print(sum)
num=sum*10
count=0
while num<1 :
    count+=1
    num=num*10

print(count)

sum=sum*(10**count1)


# rev the sum
rev=0
while sum!=0 :
    r=sum%10
    rev=rev*10+r
    sum=sum//10

print(rev)

if N%2==0 :
    print("the binary of the number is ",int(rev*(10**(count))))
else :
    print("the binary of the number is ",rev)