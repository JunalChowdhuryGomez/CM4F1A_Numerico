import numpy as np
import matplotlib.pyplot as plt

def generar_matriz_triang_sup(m):
    mu = 0
    sigma = 1 / np.sqrt(m)
    A = np.random.normal(mu, sigma, (m, m))
    A = np.triu(A)
    return A

def calcular_norma_2(A):
    norm_2 = np.linalg.norm(A, ord=2)
    return norm_2

def calcular_radio_espectral(A):
    valores_propios = np.linalg.eigvals(A)
    radio_espectral = np.max(np.abs(valores_propios))
    return radio_espectral

cantidad_matrices = 10
valores_m = [np.power(2,i+2) for i in range(1,cantidad_matrices+1)]

valores_norma_2 = []
valores_radio_espectral = []

for m in valores_m:
    A = generar_matriz_triang_sup(m)
    norma_2 = calcular_norma_2(A)
    radio_espectral = calcular_radio_espectral(A)
    valores_norma_2.append(norma_2)
    valores_radio_espectral.append(radio_espectral)

# Graficar norma 2 y radio espectral
plt.plot(valores_m, valores_norma_2, label='Norma 2 de A')
plt.plot(valores_m, valores_radio_espectral, label='Radio Espectral p(A)')
plt.xlabel('Tamanio de la matriz m')
plt.ylabel('Valor')
plt.title('Norma 2 vs Radio Espectral para Matriz triangular supperior')
plt.legend()
plt.grid(True)
plt.show()