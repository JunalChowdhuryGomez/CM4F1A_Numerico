import numpy as np

A = np.array([
    [6, 5, -5],
    [2, 6, -2],
    [2, 5, -1]
])

x = np.array([1, 2, 3], dtype=float)

def normalize_inf(v):
    return v / np.linalg.norm(v, ord=np.inf)

num_iter = 200

for i in range(num_iter):
    x = np.dot(A, x)
    x = normalize_inf(x)

rho_A_approx = np.linalg.norm(np.dot(A, x), ord=np.inf)

print("Vector aproximado después de 200 iteraciones:", x)
print("Estimación del radio espectral p(A) =", rho_A_approx)