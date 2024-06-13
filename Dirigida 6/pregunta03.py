import numpy as np

def punto_fijo(x0, y0, max_iter=1000, tol=1e-6):
    x, y = x0, y0
    for i in range(max_iter):
        x_n1 = 10 / (x + y)
        y_n1 = np.sqrt((57 - y) / (3 * x))
        if np.abs(x_n1 - x) < tol and np.abs(y_n1 - y) < tol:
            break
        x, y = x_n1, y_n1
        print(f"Iteration {i + 1}: x = {x:.6f}, y = {y:.6f}")
    return x, y
    
x0 = 2.5
y0 = 3.5
x, y = punto_fijo(x0, y0)
print(f"Solucion encontrada: x = {x}, y = {y}")