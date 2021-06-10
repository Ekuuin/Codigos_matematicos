import numpy as np

def Fibonacci(n):
    if n < 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

rango = np.arange(0 , 35)
valores = np.array(rango)

for k in rango:
    valores[k] = Fibonacci(k)
    print(Fibonacci(k))

    if k > 0:
        print('Golden Ratio = ', valores[k] / valores[k-1])