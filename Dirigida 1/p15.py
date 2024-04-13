# Ejercicio 15
# Calcule un valor aproximado del epsilon del maquina usando el algoritmo 1
import math
def func():
  s = 1
  for k in range(1,100,1):
    s = 0.5*s
    t = s + 1
    if(t<=1):
      s = 2*s
  return s

z = func()

print(f"Epsilon de maquina (doble precision): {z}")
cantidad_bits = 1 - math.log(z,2)
print("Cantidad de bits: ",cantidad_bits)