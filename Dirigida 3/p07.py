#Ejercicio 7
import numpy as np

def gauus_jordan(A):
    A = A.astype(float)
    m, n = A.shape
    print("Matriz original:")
    print(A)
    print("\nProceso de eliminacion de Gauss-Jordan:\n")
    for i in range(min(m, n)):
        pivot_row = i
        for k in range(i+1, m):
            if abs(A[k, i]) > abs(A[pivot_row, i]):
                pivot_row = k
        
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
        
        for j in range(i+1, m):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
    
    for i in range(min(m, n)-1, -1, -1):
        for j in range(i):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
    
    print("Matriz escalonada reducida:")
    print(A)
    print()

A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

gauus_jordan(A.copy())