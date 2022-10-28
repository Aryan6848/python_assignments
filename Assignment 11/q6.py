from re import I


n=int(input(" Enter the value "))
fact=1
i=1
''''while i<=n:
    fact=fact*i 
    i+=1
print('factorial of ',n,'is',fact)
'''

for e in range(2,n+1,1):
    fact=fact*e
print(fact)