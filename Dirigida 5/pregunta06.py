import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos proporcionados
x = np.array([0.4, 0.8, 1.2, 1.6, 2.0, 2.3])
y = np.array([800, 975, 1500, 1950, 2900, 3600])

# Transformar y usando logaritmo natural
log_y = np.log(y)

# Realizar regresion lineal
slope, intercept, r_value, p_value, std_err = linregress(x, log_y)

# Convertir coeficientes a la forma exponencial
a = np.exp(intercept)
b = slope

print("ln(y) = ln(a) + bx")
print("a: ",a)
print("b: ",b)

# Generar valores de x para la curva ajustada
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * np.exp(b * x_fit)

# Graficar datos originales y curva ajustada
plt.scatter(x, y, label='Datos originales', color='red')
plt.plot(x_fit, y_fit, label='Curva ajustada', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste de la funcion exponencial')
plt.grid(True)
plt.show()