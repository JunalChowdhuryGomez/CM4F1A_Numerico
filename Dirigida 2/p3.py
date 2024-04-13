import numpy as np
import matplotlib.pyplot as plt

def perturb_poly(w_roots, variance):
    perturbed_coeffs = [np.random.normal(1, np.sqrt(variance)) * coeff for coeff in w_roots]
    return np.poly1d(perturbed_coeffs)

def plot_roots(w_roots, perturbed_roots):
    x = [root.real for root in w_roots]
    y = [root.imag for root in w_roots]
    plt.scatter(x, y, label='Raices exactas')
    x_perturbed = [root.real for root in perturbed_roots]
    y_perturbed = [root.imag for root in perturbed_roots]
    plt.scatter(x_perturbed, y_perturbed, label='Raices perturbadas')
    plt.xlabel('Real')
    plt.ylabel('Imaginaria')
    plt.title('Raices exactas vs. Raices perturbadas')
    plt.legend()
    plt.show()
num_roots = 20
mu, sigma = 0, np.exp(-10)
w_roots = np.arange(1, num_roots + 1)
W = np.poly1d(w_roots)
perturbed_poly = perturb_poly(w_roots, sigma)
perturbed_roots = perturbed_poly.roots
plot_roots(w_roots, perturbed_roots)