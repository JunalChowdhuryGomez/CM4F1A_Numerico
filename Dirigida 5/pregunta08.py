import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt 

# Datos proporcionados
c = np.array([0.5, 0.8, 1.5, 2.5, 4])
k = np.array([1.1, 2.4, 5.3, 7.6, 8.9])

# Definir la funcion de ajuste
def func(c, a, b):
    return (a * c**2) / (b + c**2)

# Usar curve_fit para encontrar los valores optimos de a y b
params, covariance = curve_fit(func, c, k, p0=[1, 1])
a, b = params
print("Para el ajuste: (a * c^2) / (b + c^2)")
print("a: ",a)
print("b: ",b)
# Generar valores de c para la curva ajustada
c_fit = np.linspace(min(c), max(c), 100)
k_fit = func(c_fit, a, b)

# Graficar datos originales y curva ajustada
plt.scatter(c, k, label='Datos originales', color='red')
plt.plot(c_fit, k_fit, label='Curva ajustada', color='blue')
plt.xlabel('c')
plt.ylabel('k')
plt.legend()
plt.title('Ajuste de la funcion $k = \\frac{ac^2}{b + c^2}$')
plt.grid(True)
plt.show()
