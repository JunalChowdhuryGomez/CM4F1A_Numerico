#Ejercicio 14
#a)
import scipy.io as sio
data = sio.loadmat('hw4data')
y = data['y']

#b)
import numpy as np
n = len(y)
x = np.arange(1, n + 1)  # Valores de x: 1, 2, ..., n
A = np.column_stack((x**2, x, np.ones(n)))  # Columnas  x^2, x, y 1
#print(A)
# Ahora tenemos el sistema Ax = y

#c)
# Calcular A^T y A y A^T y
A_transpose_A = np.dot(A.T, A)
A_transpose_y = np.dot(A.T, y)
# Resolver el sistema A^T A x = A^T y usando eliminacion gaussiana
x = np.linalg.solve(A_transpose_A, A_transpose_y)
print(x)

#d)
import matplotlib.pyplot as plt
# Generar puntos para graficar la parabola ajustada
x_vals = np.linspace(1, n, 100)
y_vals = x[0] * x_vals**2 + x[1] * x_vals + x[2]
# Graficar los datos y la parabola ajustada
plt.plot(x_vals, y_vals, label='Ajuste cuadratico')
plt.scatter(np.arange(1, n + 1), y, color='red', label='Datos') 
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste cuadratico a los datos')
plt.grid(True)
plt.show()