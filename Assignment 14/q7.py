l1=["abcd",2,3,"Aryan",4.5,"abc",6.0,5.0]
l2=[]
print(l1)
"""
for e in l1:
    if(type(e)==int):
        l2.append(e)
l1=l2
print(l1)

"""
#method 2 without using new list 
i=0
n=len(l1)
while i<n:
    if(type(l1[i])!=int):
       # l1.remove(l1[i])
        del(l1[i])
        n-=1
    else :
        i+=1

print(l1)