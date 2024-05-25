import numpy as np

def gradiente_conjugado(A, b, tol=1e-10, max_iteraciones=1000):
    x = np.zeros_like(b)
    r = b - np.dot(A, x)
    p = r
    rsold = np.dot(r.T, r)
    for iteration in range(max_iteraciones):
        Ap = np.dot(A, p)
        alfa = rsold / np.dot(p.T, Ap)
        x = x + alfa * p
        r = r - alfa * Ap
        rsnew = np.dot(r.T, r)
        if np.sqrt(rsnew) < tol:
            return x, iteration + 1
        p = r + (rsnew / rsold) * p
        rsold = rsnew
    return x, max_iteraciones

# Matriz A y vector B del sistema de ecuaciones
A = np.array([[5, 4, 3], 
              [4, 3, 5], 
              [3, 5, 4]])
B = np.array([60, 50, 46])

# Resolver el sistema usando el metodo de Gradiente Conjugado
X, iterations = gradiente_conjugado(A, B)

for i in range(len(X)):
    print(f'x{i+1} = {X[i]}')
