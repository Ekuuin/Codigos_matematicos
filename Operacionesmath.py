import math


#Función de elevar al cuadrado
def sqr(x):
    return(x*x)

#Potencia al cubo
def cubo(x):
    return(x*x*x)

#Raíz Cúbica
def rcub(x):
    if(x<0):
        return -(-x)**(1/3)
    return x**(1/3)

#

y = sqr(5-7)
print("y=", y)

z = rcub(0)
print("z=", z)

print("z =", z , "......" , cubo(z))

#Definir mi propio factorial
def fact(n):
    f = 1
    for k in range(2,n+1):
        f *= k
    return f

print("F = ", fact(5))

#Funcion exponencial
def exp(x):
    f = 1
    s = 1
    for k in range (1,20):
        f *= (x/k)
        s += f
    return s

print("Exp = ", exp(5))

#Funcion seno
def seno(x):
    f = x
    s = x
    for k in range(3, 20, 2):
        f *= -(sqr(x)/(k*(k-1)))
        s += f
    return s

print("Seno = ", seno(.25))

#Funcion coseno
def coseno(x):
    f = 1
    s = 1
    for k in range(2, 20, 2):
        f *= -(sqr(x)/(k*(k-1)))
        s += f
    return s

print("Coseno = ", coseno(.25))

#Definicion SQRT
def sqrt(n):
    x1 = 1
    err = 10
    while err > 1e-8:
        x2 = (x1+n/x1)/2
        err = abs(x2-x1)
        x1 = x2
    return x1

print("Raiz = ", sqrt(1.25))