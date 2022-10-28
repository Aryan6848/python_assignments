n1=int(input("Enter the value of n1 "))
n2=int(input("Enter the value of n2 "))

#1<=HCF(a,b)<=min(a,b)

i=min(n1,n2)
while i>=1 :
    if(n1%i==0 and n2%i==0):
        print("HCF of the two numbers is",i)
        break
    i-=1