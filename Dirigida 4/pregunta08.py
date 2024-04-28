import numpy as np

def hallarSVD(A):
  U, S, Vt = np.linalg.svd(A)

  print("Matriz U (vectores singulares izquierdos):")
  print(U)
  print("\nValores singulares:")
  print(S)
  print("\nMatriz V^T (transpuesta de los vectores singulares derechos):")
  print(Vt)
  
def menu():
  print("\na)")
  matrizA = np.array([[1, -1], [0, 1],[1, 0]])
  hallarSVD(matrizA)
  
  print("\nb)")
  matrizB = np.array([[1, 1, 1], [-1, 0, -2],[1, 2, 0]])
  hallarSVD(matrizB)
  
  print("\nc)")
  matrizC = np.array([[3, 2, 2], [2, 3, -2]])
  hallarSVD(matrizC)

menu()