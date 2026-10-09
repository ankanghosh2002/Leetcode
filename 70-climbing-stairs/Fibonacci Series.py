#Fibonacci Series Function
#09.10.26


def fib(n):
    a=0
    b=1
    l=[]
    for i in range(n):
        l.append(a)
        a,b=b,a+b 
    return l

print(fib(3))
