import numpy as np

def F(x):
    return np.array([
        x[0]**2 - 2*x[0] - x[1] + 0.5,
        x[0]**2 + 4*x[1]**2 - 4
    ])

def J(x):
    return np.array([
        [2*x[0] - 2, -1],
        [2*x[0], 8*x[1]]
    ])

def metodo_newton_SE(F, J, x0, tol, max_iter=1000):
    x_n = np.array(x0, dtype=float)
    for _ in range(max_iter):
        Fx_n = F(x_n)
        Jx_n = J(x_n)
        print(f"x_n = {x_n}, F(x_n) = {Fx_n}, J(x_n) = {Jx_n}")
        if np.linalg.det(Jx_n) == 0:
            print("La matriz Jacobiana es singular")
            return None
        delta = np.linalg.solve(Jx_n, -Fx_n)
        x_n1 = x_n + delta
        if np.linalg.norm(delta, ord=np.inf) < tol:
            return x_n1
        x_n = x_n1
    print("El metodo no convergio")
    return None

# Parametros
x0 = [2, 0.5]  # Estimacion inicial
tolerancia = 1e-6

# Encontrar la solucion
solucion = metodo_newton_SE(F, J, x0, tolerancia)
print(f"La solucion encontrada es: {solucion}")
