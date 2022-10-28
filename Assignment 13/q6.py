firstlist=["Java","python","SQL"]
secondlist=["C","Cpp","NoSQL"]

#method1=concatenation
"""
firstlist=firstlist+secondlist
print(firstlist)

"""

#method2 -> using append function

for e in secondlist:
    firstlist.append(e)

print(firstlist)