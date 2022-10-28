thislist=["Java","SQL","C","ReactJs","Javascript","Python"]
#method1 by using sort function 
"""
thislist.sort()
print(thislist)

"""
#method2 by using > operator 

i=0
while(i<len(thislist)-1):
    j=i+1
    while j<len(thislist):
        if(thislist[i]>thislist[j]):
            temp=thislist[j]
            thislist[j]=thislist[i]
            thislist[i]=temp
        j+=1
    i+=1

print(thislist)


# write fun

#even the > operator we have used in the list is abstraction because > operator first check unicode of firstelement of the 
# string and if both the unicode of the firat element of the list is same then it goes to next element ,similarly the process go one 
# for the first different element ,if found greater then return true .

