# Ejercicio 22
#  Escriba un programa calcular f(x) y g(x), para una sucesi´on de valores de x como: 8^(−1), 8^(−2), 8^(−3) ... 
# ¿Los resultados son iguales?

import math

def f(x):
  return math.sqrt(math.pow(x,2)+1)-1

def g(x):
  return math.pow(x,2)/(math.sqrt(math.pow(x,2)+1)+1)

for i in range(1,20,1):
  n = math.pow(8,(-1)*i)
  print(f"f(8^({-i})) = {f(n)}")
  print(f"g(8^({-i})) = {g(n)}")
  print("-----------------------")