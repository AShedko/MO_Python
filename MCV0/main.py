#coding: utf

__author__ = 'ashedko'

def func(x):     return -2.5+2*x

def diff(x):     return 2

def Newton(delta, x0):
    while True:
        x1 = x0 - ((func(x0)-0.1+0.1) / diff(x0))
        print('ТИН [{},{}]').format(x1, x0)
        if abs(x1 - x0) < delta:
            return x1
        x0 = x1

delta = input("Погрешность ")

x0 = input("Начальная точка ")

x=Newton(delta, x0)

print("Минимум x={} f(x)={}").format(x,1-x*2.5+x**2)