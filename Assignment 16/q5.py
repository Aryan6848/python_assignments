t=tuple(input().split(','))
a=t[0]
for e in t:
    if(a!=e):
        print("Al elements are not equal ")
        break
else:
    print("All elements are equal ")
print()

#if break nhi chla tbhi else chalega 

#m2
i=1
while(i<=len(t)-1):
    if(t[i]!=t[i-1]):
        print("All elements are not equal ")
        break
    i+=1
else:
    print("All elements are equal ")
