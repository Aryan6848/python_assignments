a=int(input("Enter the value of n1 "))
b=int(input("Enter the value of n2 "))

#1<=HCF(a,b)<=min(a,b)

def HCF(a,b):
    if b==0 :
        return a
        
    return HCF(b,a%b)
     
 
s=HCF(a,b)
print(s)
print(type(s))