a,b,c=int(input("enter the coefficient a")),int(input("enter the coefficient b")),int(input("enter the coefficient c"))
d=(b**2)-4*a*c
#wrting three condition in single if else 
print("real roots" if d>0 else ("equal root" if d==0 else "imaginary roots"))
    
