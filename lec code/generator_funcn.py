from re import A


def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

it=fib()
fib_list=[]
print("enter y to generate the number")
while True:
    ans= input()
    if(ans=='y'):
        fib_list.append(next(it))
    else :
        break
    print("do you want to generate another number [y/n]")


print(fib_list)