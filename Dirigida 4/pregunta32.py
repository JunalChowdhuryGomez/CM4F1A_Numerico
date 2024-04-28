import numpy as np
A = np.array([[4, -1, -1, 0],
              [-1, 4, 0, -1],
              [-1, 0, 4, -1],
              [0, -1, -1, 4]], dtype=np.double)

b = np.zeros(4) 
def chebyshev_acceleration(A, b, n_iterations, l_min, l_max):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    x_old = np.copy(x)
    D_inv = np.diag(1 / np.diag(A))  # Inversa de la matriz diagonal D de A
    
    d = (l_max + l_min) / 2
    c = (l_max - l_min) / 2
    
    # Inicializar tau y la iteración inicial
    tau = 1 / d
    rho_prev = 1
    
    for k in range(1, n_iterations + 1):
        rho = 1 / (2 * d - rho_prev)
        x[:] = x_old + rho * (x - x_old)
        x_old[:] = x
        
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = x_old[i] + tau * (b[i] - s1 - s2) * D_inv[i, i]
        
        rho_prev = rho
        print(f"Iteración {k}: {x}")
    return x

# Estimar valores propios mínimo y máximo
l_max = 6  # Asumiendo un cálculo previo o conocimiento del problema
l_min = 2  # Asumiendo un cálculo previo o conocimiento del problema

# Llamada al método de Jacobi con aceleración de Chebyshev
chebyshev_acceleration(A, b, 10, l_min, l_max)

