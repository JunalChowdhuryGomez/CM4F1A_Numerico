import numpy as np
A = np.array([[10, -3, 6],
              [1, -8, -2],
              [-2, 4, 9]])
b = np.array([25, -9, -50])
x = np.zeros_like(b)
# numero de iteraciones
n_iter = 10
# Metodo de Gauss-Jacobi
print("Metodo de Gauss-Jacobi:")
for _ in range(n_iter):
    x_new = np.zeros_like(x)
    for i in range(A.shape[0]):
        s = sum(A[i, j] * x[j] for j in range(A.shape[1]) if i != j)
        x_new[i] = (b[i] - s) / A[i, i]
    x = x_new
    print(f"Iteracion {_+1}: {x}")

# Metodo de Gauss-Seidel
print("\nMetodo de Gauss-Seidel:")
for _ in range(n_iter):
    x_new = np.copy(x)
    for i in range(A.shape[0]):
        s1 = sum(A[i, j] * x_new[j] for j in range(i))
        s2 = sum(A[i, j] * x[j] for j in range(i + 1, A.shape[1]))
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    x = x_new
    print(f"Iteracion {_+1}: {x}")