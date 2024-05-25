import numpy as np

# Parametros
n = 20
tol = 1e-10
max_iter = 10000

# Matriz tridiagonal A
A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)

# Vector b
b = np.zeros(n)
b[-1] = 1

# Solucion exacta
x_exact = -n / 4 + np.arange(1, n + 1) / 2

# Metodo SOR
def sor(A, b, omega, tol, max_iter):
    n = len(b)
    x = np.zeros(n)
    for k in range(max_iter):
        x_old = np.copy(x)
        for i in range(n):
            sigma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sigma)
        if np.linalg.norm(x - x_old) < tol:
            return x, k + 1
    return x, max_iter

# Metodo de gradiente conjugado
def gradiente_conjugado(A, b, tol, max_iter):
    x = np.zeros(len(b))
    r = b - A.dot(x)
    p = r.copy()
    rsold = np.dot(r, r)
    for k in range(max_iter):
        Ap = A.dot(p)
        alpha = rsold / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r, r)
        if np.sqrt(rsnew) < tol:
            return x, k + 1
        p = r + (rsnew / rsold) * p
        rsold = rsnew
    return x, max_iter

# Ejecutar metodos
omega = 1.5
x_sor, iter_sor = sor(A, b, omega, tol, max_iter)
x_cg, iter_cg = gradiente_conjugado(A, b, tol, max_iter)

# Comparacion de iteraciones
print(f"SOR iteraciones: {iter_sor}")
print(f"Gradiente conjugado iteraciones: {iter_cg}")