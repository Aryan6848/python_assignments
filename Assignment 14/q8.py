l1=[1,1,"aryan","aryan", 2,3,2,3,"aryan",1,4,4]
l2=[]
i=0
n=len(l1)
while i<=n-1:
    if  l1[i] not in l2:
        l2.append(l1[i])
    i+=1;
print(l2)


for e in l2:
    print(e,l1.count(e))