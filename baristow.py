import math
import numpy as np
import os

""" #Para Windows
os.system('cls') """

#Para Linux y MacOS
os.system('clear')

print("- - Método de Baristow - -")

grado = int(input("\nIngrese el grado del polinomio: "))

print("\nEl orden es ax^n + bx^m + c, es decir, de mayor a menor")
print("\nIngrese los coeficientes del polinomio, separandolos con un espacio: ")
coeficientes = list(map(float, input().split()))  
a = np.array(coeficientes, dtype = np.float64)

r = float(input("\nIngrese el valor de r0: "))
s = float(input("\nIngrese el valor de s0: "))

Es = float(input("\nIngrese la tolerancia del sistema (Es) en porcentaje: "))

def obtenerB(a, r, s):
    b = []
    b.append(a[0])
    b.append(a[1]+(r*b[-1]))
    for i in a[2:]:
        b.append(i+(r*b[-1])+(s*b[-2]))
    b = np.array(b, dtype = np.float64)
    return b

def obtenerC(b, r, s):
    c = []
    c.append(b[0])
    c.append(b[1]+(r*c[-1]))
    for i in b[2:-1]:
        c.append(i+(r*c[-1])+(s*c[-2]))
    c = np.array(c, dtype = np.float64)
    return c

def delta(b, c):
    A = [[c[-2], c[-3]], [c[-1], c[-2]]]
    A = np.array(A, dtype = np.float64)
    B = [-b[-2], -b[-1]]
    B = np.array(B, dtype = np.float64)
    x = np.linalg.solve(A, B)
    return x

def iteraciones(r, s, a, Es):
    contador = 1
    ER = 100
    ES = 100

    while ER > Es or ES > Es:
        b = obtenerB(a, r, s)
        c = obtenerC(b, r, s)
        deltaRS = delta(b, c)
        r = deltaRS[0] + r 
        s = deltaRS[1] + s
        ER = abs(deltaRS[0] / r) * 100
        ES = abs(deltaRS[1] / s) * 100

        print("\n\nIteración #", contador)
        print("\nEl valor de r es: ", round(r, 4), "por lo que su error es: ", round(ER, 4), "%")
        print("\nEl valor de s es: ", round(s, 4), "por lo que su error es: ", round(ES, 4), "%")

        contador += 1

    den = [1, -r, -s]
    qx, rx = np.polynomial.polynomial.polydiv(a, den)
    print("\n\nEl polinomio final es: ", qx, den)

iteraciones(r, s, a, Es)

""" Ejemplo 1
3
1 1.2 -4 -4.8
0.1
1 """

""" Ejemplo 2 
4
1 1 0.56 -1.44 -2.88
1
1 """

""" Ejemplo 3
5
1 0 0 0 1 1
1
1 """

