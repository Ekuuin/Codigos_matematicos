import matplotlib.pyplot as plt
import numpy as np

""" f = lambda x , y : (y + 1) * (x + 1) * np.cos(x**2 + 2*x)   #Función lambda donde tenemos la ecuación que evaluaremos.

def rk(x,y,h,xf):
    xarr = np.array([]) #Creamos un par de arreglos vacíos donde guardaremos los valores correspondientes en cada iteración.
    yarr = np.array([])
    for i in np.arange(x, xf+h, h): #Ciclo for que va desde x: valor inicial de X, xf+h: el valor final de X + el aumento h para realizar las iteraciones correctas.
        print('x[',i,'] = ',x,'   y[',i,'] = ', y) #Imprime los valores de X y Y en cada iteración.
        k1 = f(x , y)
        k2 = f(x + h/2 , y + k1 * h/2)
        k3 = f(x + h/2 , y + k2 * h/2)  #Calculo de los valores K usando la función lambda.
        k4 = f(x + h , y + k3 * h)
        print('k1 = ',k1,'  k2 = ',k2,'  k3 = ',k3,'  k4 = ',k4)  #Imprime los valores de K.
        xarr = np.append(xarr,x)            #Agrega los valores de X y Y al final de su respectivo arreglo.
        yarr = np.append(yarr,y)
        y += ((k1 + 2*k2 + 2*k3 + k4) / 6) * h  #Sustitución del valor de Y para la siguiente iteración.
        x += h  #Aumento de x en h
    return np.array([xarr, yarr])   #Regresa un arreglo creado a partir del arreglo xarr y yarr, divididos para uso individual.

t = rk(0, 4, 0.01, 2) #Llamado de la función rk usando x: valor inicial x - y: valor inicial y - h: aumento - xf: valor final x

plt.grid()
plt.figure(1)
plt.plot(t[0], t[1])
plt.show() """

V = np.array([[1,2,3]])
M = np.array([[1,2,3], [4,-5,6], [7,8,9]])
VT = np.transpose(V)
MI = np.linalg.inv(M)
A = np.matmul(M,MI)
B = np.matmul(M,VT)
C = np.matmul(V,M)
print(V)
print(VT)
print(MI)
print(f'Identidad: \n{A}')
print(B)
print(C)