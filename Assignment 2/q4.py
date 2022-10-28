a=5
b=5
print(" variable is a value is ",a, "address is",id(a))
print(" variable is b value is ",b, "address is",id(b))


""" note that two diiferent variables are holding the same value but the address
is same for both the variables .... Actually what happens is that this a,b will be created in namespace
and the objectn will be created in heap and this namespace variables are holding the address of
the dynamically created objects ,since the value s same python will not create two seperate objects for both
it will give the address of same object to both of the variables """
