import math
import matplotlib.pyplot as plt
def f(x):
    return (math.log(1-x))/x
def P_3(x):
    # El polinomio de Taylor de grado 3 para la funcion ln(1 − x) es:
    # P_3(x) = -x + x^2 - x^3
    return (-1)*x + math.pow(x,2) - math.pow(x,3)
print("El polinomio de Taylor de grado 3 para la funcion ln(1 − x) es:\n P_3(x) = -x + x^2 - x^3\n")
print(f"a) El valor adecuado a f(0), evaluamos (x=0)\nf(0) = P_3(0) = {P_3(0)}")
# intervalo [-10^15, 10^15]
a = math.pow(10,-15)
b = -1*math.pow(10,-15)
paso = (a-b)/200
i = b
r = []
while(i<a):
  r.append(i)
  i = i + paso
plt.plot(r, [f(i) for i in r], label='f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de f(x) en el intervalo [-10^15, 10^15]')
plt.legend()
plt.show()
print(f"b) El valor asignado a f(x) cuando x->0 es 0, ya que sus limites de laterales f(0) tienden a 0")
# c) Grafique ln(1 − x) en el intervalo [−5×10^−16,5×10^−16]
# intervalo [-5*10^16, 5*10^16]
a = 5 * math.pow(10,-16)
b = -5 * math.pow(10,-16)
paso = (a-b)/250
i = b
r = []
while(i<a):
  r.append(i)
  i = i + paso
plt.plot(r, [math.log(1-i) for i in r], label=' y = ln(1 − x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de  ln(1 − x) en el intervalo [-5*10^16, 5*10^16]')
plt.legend()
plt.show()
print(f"c) La forma de la grafica es escalonda descendiente\n Las oscilaciones se hacen mas frecuentes con x>0")
print(f"d) 1. El intervalo ([-10^{15}, 10^{15}]) no es simetrico alrededor de (x = 0).\nEsto se debe a que el dominio de la funcion ln(1 - x) esta restringido a (x < 1).\nLa funcion ln(1 - x) no esta definida para valores de (x) mayores o iguales a 1.\nPor lo tanto, el intervalo no es simetrico porque no incluye valores positivos de (x)")
print(f"d) 2. La funcion (f(x)) tiene oscilaciones cuando (x > 0) debido a la presencia de la funcion logaritmica ln(1 - x).\nCerca de (x = 0), ln(1 - x) se comporta de manera suave y monotona.\nSin embargo, a medida que (x) se aleja de 0 hacia valores positivos, la funcion ln(1 - x) se vuelve mas sensible a pequenas variaciones en (x).\nEsto resulta en oscilaciones mas pronunciadas en (f(x)) cuando (x > 0)")

