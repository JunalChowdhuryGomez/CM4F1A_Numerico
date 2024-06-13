import numpy as np

def g1(x, y):
    return (8*x - 4*(x**2) + (y**2) + 1)/8

def g2(x, y):
    return (2*x - (x**2) + 4*y - (y**2) + 3)/4

def punto_fijo(g_funcs, x0, tol, max_iter=1000):
    x = np.array(x0, dtype=float)
    for _ in range(max_iter):
        x_nuevo = np.array([g(x[0], x[1]) for g in g_funcs])
        if np.linalg.norm(x_nuevo - x, ord=np.inf) < tol:
            return x_nuevo
        x = x_nuevo
    print("El metodo no convergio.")
    return None

# Parametros
x0 = [2, 0.5]  # Estimacion inicial
tolerancia = 1e-6

# Definir las funciones g
g_funcs = [g1, g2]

# Encontrar la solucion
solucion = punto_fijo(g_funcs, x0, tolerancia)
print(f"La solucion encontrada es: {solucion}")