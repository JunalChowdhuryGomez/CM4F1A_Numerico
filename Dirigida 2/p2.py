import numpy as np
import matplotlib.pyplot as plt

w_roots = np.arange(1, 21)
W = np.poly(w_roots)
perturb = np.zeros_like(W)
perturb[1] = 1e-7
W_perturb = W + perturb
perturbed_roots = np.roots(W_perturb)
w_roots = np.sort(w_roots)
perturbed_roots = np.sort(perturbed_roots)
x_pert = [i.real for i in perturbed_roots]
y_pert = [i.imag for i in perturbed_roots]
plt.scatter(x_pert, y_pert)
x = [i.real for i in w_roots]
y = [i.imag for i in w_roots]
plt.scatter(x, y)
plt.ylabel('Imaginario')
plt.xlabel('Real')
plt.title('Comparacion entre raices originales y perturbadas')
plt.legend(['Perturbadas', 'Originales'])
plt.show()