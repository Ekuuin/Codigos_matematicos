import numpy as np
import matplotlib.pyplot as plt

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
    tol = 1e-4 
    err = 1000
    while err > tol:
        x1 = x0 - df(x0)/d2f(x0) #Metodo de Newton
        err = np.abs(x1-x0)     #Calcula los maximos y minimos de la funcion
        x0 = x1
    return x0



x0 = np.array([-0.5, 0.5, 2, 1.2])      #Creamos un array con los valores de x0 para el método de Newton Rapson y su primera derivada
x2 = np.array([-1, 1, 0])               #Creamos un array con los valores de x2 para el método de Newton Rapson y su segunda derivada
x = np.arange(-1.5 , 2.0, 0.01)
xo = np.array([])
xm = np.array([])


for i in x0:
    xo = np.append(xo,[NewtonRap(i)])       #En estos ciclos, realizamos la función de NewtonRap mientras iteramos los valores de x0 y x2
for j in x2:                                    # para el segundo método.
    xm = np.append(xm,[NewtonRap2(j)])

print(xo)
print(xm)

plt.grid()
plt.figure(1)
plt.plot(x, f(x))
plt.plot(xo, xo*0, 'ro')
plt.plot(xm, f(xm), 'bo')
plt.show()
