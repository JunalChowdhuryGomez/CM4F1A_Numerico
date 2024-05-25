import numpy as np

def gram_schmidt(A):
    """Gram-Schmidt"""
    (m, n) = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R

def gram_schmidt_modificado(A):
    """Gram-Schmidt Modificado"""
    (m, n) = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    V = A.copy()
    for i in range(n):
        R[i, i] = np.linalg.norm(V[:, i])
        Q[:, i] = V[:, i] / R[i, i]
        for j in range(i + 1, n):
            R[i, j] = np.dot(Q[:, i], V[:, j])
            V[:, j] = V[:, j] - R[i, j] * Q[:, i]
    return Q, R

# Test 1: Matrizz Random  20x10
A1 = np.random.uniform(0, 1, (20, 10))
Q1_Sin_Modificar, R1_Sin_Modificar = gram_schmidt(A1)
Q1_Modificado, R1_Modificado = gram_schmidt_modificado(A1)

# Test 2: Matriz con la ffuncion dada
A2 = np.array([[(2*i - 2*j) / 19 for j in range(1, 11)] for i in range(1, 21)])
Q2_Sin_Modificar, R2_Sin_Modificar = gram_schmidt(A2)
Q2_Modificado, R2_Modificado = gram_schmidt_modificado(A2)

# Funcion que compara resultados con mmatriz identidad
def comparar_con_identidad(Q):
    identidad_aproximada = np.dot(Q.T, Q)
    identidad = np.eye(Q.shape[1])
    return np.linalg.norm(identidad_aproximada - identidad)

# Comparacion
error_sin_modificar_1 = comparar_con_identidad(Q1_Sin_Modificar)
error_modificado_1 = comparar_con_identidad(Q1_Modificado)
error_sin_modificar_2 = comparar_con_identidad(Q2_Sin_Modificar)
error_modificado_2 = comparar_con_identidad(Q2_Modificado)
print(f"Error para Gram-Schmidt Sin modificar con una matriz random: {error_sin_modificar_1}")
print(f"Error para Gram-Schmidt Modificado con una matriz random: {error_modificado_1}")
print(f"Error para Gram-Schmidt Sin modificar con una funcion matriz: {error_sin_modificar_2}")
print(f"Error para Gram-Schmidt Modificado con una funcion matriz: {error_modificado_2}")