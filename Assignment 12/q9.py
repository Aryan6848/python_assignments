n1=int(input("enter the value of n1 "))
n2=int(input("enter the value of n2 "))

#max(a,b)<=LCM(a,b)<=a*b

i=max(n1,n2)
while(i<=n1*n2):
    if(i%n1==0 and i%n2==0):
        print("LCM of two numbers is",i)
        break
    i+=min(n1,n2)    
    
#why max(n1,n2) suppaose nos are 8 and 6 so max is 8 so i=8,and i%8==0 and i%6==0 -> false so the next no.
#which we will check should be divisible by 8 and  6 also ,if we increment i by 6 then definetly i will be not
#divisible by 8,because in starting i was 8 so to be divisible by 8 i should increase by 8 
                      