import numpy as np
def f(x):
    return np.cos(x) + np.sin(50 * x)**2
def df(x):
    return -np.sin(x) + 50 * np.sin(100 * x)
def newton_method(x0, tol=1e-8, max_iter=1000):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        print(f"x = {x}, f(x) = {fx}, df(x) = {dfx } ")
        if dfx == 0:
            raise ValueError("La derivada es cero. No se puede continuar.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("El metodo de Newton no convergio.")
# Aproximacion inicial
x0 = np.pi / 2
# Solucion usando el metodo de Newton
root = newton_method(x0)
print(f"La raiz aproximada es: {root:.6f}")
print(f"Error relativo: {abs(root - np.pi / 2):.6e}")