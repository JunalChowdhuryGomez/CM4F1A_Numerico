import numpy as np

def crear_matriz_hilbert(n):
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (1 + i + j)
    return H

def vector_b(H):
    b = np.sum(H, axis=1) / 3
    return b

n = 5  # Tamanio de la matriz
H = crear_matriz_hilbert(n)
b = vector_b(H)

def jacobi(A, b, n_iterations=25):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    for it in range(n_iterations):
        x_new = np.zeros_like(x, dtype=np.double)
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        x = x_new
        print(f"Jacobi Iter {it+1}: {x}")
    return x

def gauss_seidel(A, b, n_iterations=25):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    for it in range(n_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x_new[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        x = x_new
        print(f"Gauss-Seidel Iter {it+1}: {x}")
    return x

print("Metodo de jacobi:")
x_jacobi = jacobi(H, b)

print("\nMetodo Gauss-Seidel:")
x_gauss_seidel = gauss_seidel(H, b)
