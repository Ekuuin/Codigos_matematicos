import matplotlib.pyplot as plt
import numpy as np

"""f2 = lambda x: x**5 - 3*x*x + 1.6

def f(x):
    return x**5 - 3*x*x + 1.6

x = np.arange(-1 , 1.5 , 0.1)

plt.grid()
plt.figure(1)
plt.plot(x, f2(x))
plt.show()
"""

'''
f = lambda x : x**5 - 3*x*x +1.6
df = lambda x : 5*x**4 - 6*x + 1e-4
d2f = lambda x : 20*x**3 - 6 + 1e-8

def NewtonRap(x0):
    tol = 1e-4; err = 1000
    while err > tol:
        x1 = x0 - f(x0)/df(x0) #Metodo de Newton Primera Derivada
        err = np.abs(x1-x0) # Calcula las raices de la funcion
        x0 = x1
    return x0

def NewtonRap2(x0):
    tol = 1e-4; err = 1000
    while err > tol:
        x1 = x0 - df(x0)/d2f(x0) #Metodo de Newton
        err = np.abs(x1-x0)     #Calcula los maximos y minimos de la funcion
        x0 = x1
    return x0

x0 = NewtonRap(0)
x1 = NewtonRap(1)
x2 = NewtonRap(2)

x3 = NewtonRap2(-1)
x4 = NewtonRap2(1)

x = np.arange(-1 , 1.5, 0.01)
xo = np.array([x0,x1,x2])
xm = np.array([x3,x4])

print(x0,x1,x2)
print(x3,x4)



plt.grid()
plt.figure(1)
plt.plot(x, f(x))
plt.plot(xo, xo*0, 'ro')
plt.plot(xm, f(xm), 'bo')
plt.show()
'''

Dx = 1e-6
f = lambda x : x**2 + np.log(2*x + 7)*np.cos(3*x) + 0.1
df = lambda x : (f(x + Dx) - f(x - Dx)) / (2*Dx)
d2f = lambda x : (f(x + 2*Dx) - 2*f(x) + f(x - 2*Dx)) / (2*Dx)**2

def NewtonRap(x0):
    tol = 1e-4; err = 1000
    while err > tol:
        x1 = x0 - f(x0)/df(x0) #Metodo de Newton Primera Derivada
        err = np.abs(x1-x0) # Calcula las raices de la funcion
        x0 = x1
    return x0

def NewtonRap2(x0):
    tol = 1e-4; err = 1000
    while err > tol:
        x1 = x0 - df(x0)/d2f(x0) #Metodo de Newton
        err = np.abs(x1-x0)     #Calcula los maximos y minimos de la funcion
        x0 = x1
    return x0

x0 = NewtonRap(-0.5)
x1 = NewtonRap(0.5)
x2 = NewtonRap(2)
x3 = NewtonRap(1.2)

x4 = NewtonRap2(-1)
x5 = NewtonRap2(1)
x6 = NewtonRap2(0)

x = np.arange(-1.5 , 2.0, 0.01)
xo = np.array([x0,x1,x2,x3])
xm = np.array([x4,x5,x6])

print(x0 ,x1 ,x2 ,x3)
print(x4 ,x5 ,x6)



plt.grid()
plt.figure(1)
plt.plot(x, f(x))
plt.plot(xo, xo*0, 'ro')
plt.plot(xm, f(xm), 'bo')
plt.show()
