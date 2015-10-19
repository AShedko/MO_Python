__author__ = 'ashedko'
from math import *

def f(x):
    "Function to be optimized"
    return (cos(x**(3*x/2)))
def fib(n):
    "Fibonacci"
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
def luc(n):
    "Lucas"
    return ((1 + sqrt(5))/2)**n + ((1 - sqrt(5))/2)**n

def optFib(n,a,b):
    "Fibonacci method"
    tin=b-a
    for i in range(1,n-1):
        tin=b-a
        x1=a+tin*fib(n-i-1)/fib(n-i+1)
        x2=a+tin*fib(n-i)/fib(n-i+1)
        if (f(x1)<f(x2)):
            b=x2
        else:
            a=x1
    x=a+tin*fib(1)/fib(2)
    xn=x+tin/10
    if f(xn)>f(x):
        return (a+x)/2
    else:
        return (x+b)/2

def optLuc(n,a,b):
    "Fibonacci method"
    tin=b-a
    for i in range(1,n-1):
        tin=abs(b-a)
        x1=a+tin*luc(n-i-1)/luc(n-i+1)
        x2=a+tin*luc(n-i)/luc(n-i+1)
        if (f(x1)<f(x2)):
            b=x2
        else:
            a=x1
       #print(x1,x2,tin)
    x=a+tin*luc(1)/luc(2)
    xn=x+tin/10
    if f(xn)>f(x):
        return a
    else:
        return b


#a = eval(input("Left border:"))
#b = eval(input("Right border:"))
a=0
b=2
n = eval(input("Iterations:"))
for i in range(1,n+1):
    print('{0:3d}: {1:.8f} {2:.8f}'.format(i,optFib(i,a,b),optLuc(i,a,b)))



