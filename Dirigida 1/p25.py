# 25
# Disene un programa que imprima los valores de las siguientes funciones f(x), g(x), h(x)
# en 101 puntos igualmente espaciados cubriendo el intervalo [0.99, 1.01]. Analice los resultados.

import math

def f(x):
    # x^8 - 8x^7 + 28x^6 - 56x^5 + 70x^4 - 56x^3 + 28x^2 - 8x + 1
  return math.pow(x,8)-8*math.pow(x,7)+28*math.pow(x,6)-56*math.pow(x,5)+70*math.pow(x,4)-56*math.pow(x,3)+28*math.pow(x,2)-8*x+1

def g(x):
    #  (((((((x − 8)x + 28)x − 56)x + 70)x − 56)x + 28)x − 8)x + 1
  return (((((((x-8)*x+28)*x-56)*x+70)*x-56)*x+28)*x-8)*x+1

def h(x):
    #  (x − 1)^8
  return math.pow((x-1),8)

# intervalo [0.99, 1.01]
b = 0.99
a = 1.01
paso = (a-b)/101

i = b
while(i<a):
  print(f'x= {i}, f(x) = {f(i)}, g(x) = {g(i)}, h(x) = {h(i)}')
  i = i + paso