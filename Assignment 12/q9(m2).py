#LCM of two numbers using HCF 

a=int(input("Enter the first number"))
b=int(input("Enter the second number "))

def HCF(a,b):
    if(b==0):
        return a
    else :
        return HCF (b,a%b)

LCM=(a*b)//HCF(a,b)
print("LCM of these numbers is ",LCM)