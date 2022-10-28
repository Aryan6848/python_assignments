t=(1,3,4,5,6)
l=len(t)-1
i=0
while l>=i:
    print(t[l],end=" ")
    l-=1
print()


#m2
l=list(t)
print(l[::-1])  # using slicing operator we have reversed the list 
print(tuple(l[::-1]))  # converted list into tuple 
for e in l[::-1]:
    print(e,end=" ")
print()


#m3
s=str(t)  # tuple k bracket ko bhi isne element bna diya string ka 
print(s[0])   # (
for e in s[::-1]:
    print(e,end=" ")