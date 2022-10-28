l1=[1,1,2,3,"aryan",4,2,"aryan",2,1,1,5,6]
i=0
l2=[]
n=len(l1)
while i<n:
    if l1[i] not in l2:
        l2.append(l1[i])
    i+=1
print(l2)

j=0
while j<len(l2):
    i=0
    print(l2[j],"->",end=" ")
    while i<n:
        if(l1[i]==l2[j]):
            print(i,end=" ")
        i+=1
    print()
    j+=1   
    