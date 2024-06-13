
import numpy as np
import matplotlib.pyplot as plt

# Definir los rangos para x1 y x2
x1 = np.linspace(-5, 5, 400)
x2 = np.linspace(0, 15, 400)

# Crear una malla para evaluar las funciones
X1, X2 = np.meshgrid(x1, x2)

# Definir las funciones
F1 = -X1*(X1 + 1) + 2*X2 - 18
F2 = (X1 - 1)**2 + (X2 - 6)**2 - 25

# Graficar las curvas
plt.figure(figsize=(10, 8))
plt.contour(X1, X2, F1, levels=[0], colors='r', label='F1: -x1(x1+1) + 2x2 = 18')
plt.contour(X1, X2, F2, levels=[0], colors='b', label='F2: (x1-1)^2 + (x2-6)^2 = 25')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Intersección de las curvas de las ecuaciones')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend(['F1: -x1(x1+1) + 2x2 = 18', 'F2: (x1-1)^2 + (x2-6)^2 = 25'])
plt.show()
