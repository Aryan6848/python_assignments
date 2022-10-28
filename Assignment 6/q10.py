a,b,c=int(input("enter number")),int(input("enter number")),int(input("enter number"))
print((a if b>c else (c if c>a else a ))  if a>b else (b if b>c else c))
