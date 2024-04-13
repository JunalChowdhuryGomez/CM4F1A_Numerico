# 14

#  Evalue la funcion y1(x) para x ≈ 0 usando doble precision. 
#  Grafique la funcion en el intervalo [−10^−15, 10^−15]. Repita el experimento usando y2(x)


import math
import matplotlib.pyplot as plt

def y1(x):
  return (math.log10(x+1))/x

def y2(x):
  if(1+x == 1):
    return 1
  else:
    return (math.log10(x+1))/((x+1)-1)
  
a = math.pow(10,-15)
b = -1*math.pow(10,-15)
paso = (a-b)/100
i = b
r = []

while(i<a):
  r.append(i)
  i = i + paso
print(r)
plt.plot(r, [y1(i) for i in r], label='y1(x)')
plt.plot(r, [y2(i) for i in r], label='y2(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y1(x) y y2(x)')
plt.legend()
plt.show()
