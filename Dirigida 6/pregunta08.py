import numpy as np

def f(x, B):
    return x + np.exp(-B * x**2) * np.cos(x)

def df(x, B):
    return 1 - np.exp(-B * x**2) * np.sin(x) - 2 * B * x * np.exp(-B * x**2) * np.cos(x)

def newton_method(x0, B, tol=1e-6, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        fx = f(x, B)
        dfx = df(x, B)
        if dfx == 0:
            raise ValueError("La derivada es cero. No se puede continuar.")
        #print(f"x = {x}, f(x) = {fx}, df(x) = {dfx } ")
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("El metodo de Newton no convergio.")

# Valores de B y puntos iniciales
Bs = [1, 5, 10, 25, 50]
x0s = [0, 1, 2, 10]

# Calcular y mostrar resultados
for B in Bs:
    for x0 in x0s:
        try:
            root = newton_method(x0, B)
            print(f"Para B = {B}, x0 = {x0}, la raiz es: {root:.6f}")
        except ValueError as e:
            print(f"Para B = {B}, x0 = {x0}, hubo un error: {e}")