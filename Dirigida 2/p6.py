import numpy as np
import matplotlib.pyplot as plt

def matriz_vandermonde_norma_inf(x, n):
    m = len(x)
    matriz_vander = np.vander(x, n, increasing=True)
    return np.linalg.norm(matriz_vander, ord=np.inf)

def norma_teorica(n):
    return (np.power(2,n)) / (np.e * (n - 1) * np.log(n))

# Numero de puntos
n_valores = np.arange(2, 31)

# Calcular las normas y valores teooricos
valores_norma = []
valores_teoricos = []
for n in n_valores:
    m = 2*n - 1
    x = np.linspace(-1, 1, m)
    norm = matriz_vandermonde_norma_inf(x, n)
    valores_norma.append(norm)
    teorico = norma_teorica(n)
    valores_teoricos.append(teorico)

# Graficar
plt.figure(figsize=(10, 6))
plt.semilogy(n_valores, valores_norma, label='Norma Infinita de A')
plt.semilogy(n_valores, valores_teoricos, label='(2^n) / (e * (n - 1) * log(n))', linestyle='--')
plt.title('Norma Infinita de la Matriz de Vandermonde vs. Expresion Teorica')
plt.xlabel('Valor de n')
plt.ylabel('Norma Infinita')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()