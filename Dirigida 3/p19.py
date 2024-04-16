#Ejercicio 19
import numpy as np

def invertir_matriz_LU(L, U):
    # Obtenemos las dimensiones de la matriz
    n = len(L)
    # Creamos una matriz identidad del mismo tamano que A
    A_inv = np.eye(n)
    # Resolvemos el sistema de ecuaciones LUx = b para cada columna de la matriz identidad
    for i in range(n):
        # Resolvemos Ly = b
        y = np.linalg.solve(L, A_inv[:, i])

        # Resolvemos Ux = y
        x = np.linalg.solve(U, y)

        # La solucion x es la i-esima columna de la matriz inversa
        A_inv[:, i] = x
    return A_inv

# Matriz A
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

# Factorizacion LU conocida de A
L = np.array([[1, 0, 0], [-0.5, 1, 0], [0, -2/3, 1]])
U = np.array([[2, -1, 0], [0, 1.5, -1], [0, 0, 4/3]])

# Invertir la matriz utilizando su factorizacion LU
A_inv = invertir_matriz_LU(L, U)

print("Inversa de la matriz A:")
print(A_inv)