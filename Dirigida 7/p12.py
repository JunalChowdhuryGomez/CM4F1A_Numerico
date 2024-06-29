import numpy as np

A = np.array([
    [2, 0, -1],
    [-2, -10, 0],
    [-1, -1, 4]
])

v = np.array([1, 1, 1], dtype=float)

def norma_infinita(v):
    return v / np.linalg.norm(v, ord=np.inf)

# Iteracioon 1
v1 = np.dot(A, v)
v1_normalizado = norma_infinita(v1)

# Iteraccion 2
v2 = np.dot(A, v1_normalizado)
v2_normalizado = norma_infinita(v2)

rho_A_approx = np.linalg.norm(v2, ord=np.inf)

print("Iteracion 1: v1 =", v1)
print("Iteracion 1: v1_normalizado =", v1_normalizado)
print("Iteracion 2: v2 =", v2)
print("Iteracion 2: v2_normalizado =", v2_normalizado)
print("Estimacion del radio espectral p(A) =", rho_A_approx)