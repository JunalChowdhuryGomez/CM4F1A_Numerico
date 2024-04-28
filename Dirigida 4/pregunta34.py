import numpy as np
def jacobi(A, b, x=None, max_iterations=100, tolerance=1e-10):
    n = len(b)
    if x is None:
        x = np.zeros_like(b, dtype=np.double)
    x_new = np.zeros_like(x, dtype=np.double)

    for it in range(max_iterations):
        for i in range(n):
            s = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - s) / A[i, i]

        # Convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            print(f"Jacobi converge  en la iteracion {it+1}")
            return x_new
        x[:] = x_new
        print(f"Iteracion Jacobi  {it+1}: {x}")
    return x

def gauss_seidel(A, b, x=None, max_iterations=100, tolerance=1e-10):
    n = len(b)
    if x is None:
        x = np.zeros_like(b, dtype=np.double)

    for it in range(max_iterations):
        x_old = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - s1 - s2) / A[i, i]

        # Convergencia
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            print(f"Gauss-Seidel converge en la iteracion {it+1}")
            return x
        print(f"Iteracion Gauss-Seidel {it+1}: {x}")
    return x

A = np.array([
    [10, 1, 2, 3, 4],
    [1, 9, -1, 2, -3],
    [2, -1, 7, 3, -5],
    [3, 2, 3, 12, -1],
    [4, -3, -5, -1, 15]
    ], dtype=np.double)
b = np.array([12, -27, 14, -17, 12], dtype=np.double)
print("Resolviendo por el metodo de  Jacobi:")
x_jacobi = jacobi(A, b)
print("\nResolviendo por el metodo de Gauss-Seidel:")
x_gauss_seidel = gauss_seidel(A, b)