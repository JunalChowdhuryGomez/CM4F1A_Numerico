def f(x):
    return x**8 - 36*x**7 + 546*x**6 - 4536*x**5 + 22449*x**4 - 67284*x**3 + 118124*x**2 - 109584*x + 40320

def biseccion(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("La funcion no cambia de signo en el intervalo dado")
    
    for i in range(max_iter):
        c = (a + b) / 2.0
        print(f"Iteracion {i+1}: a = {a}, f(a) = {f(a)}, b = {b}, f(b) = {f(b)}, c = {c}, f(c) = {f(c)}")
        if abs(f(c)) < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("El metodo de la biseccion no convergio")

# Intervalo dado
a = 5.5
b = 6.5

# Encontrar la raiz usando el metodo de la bisección
try:
    raiz = biseccion(a, b)
    print(f"Una raíz aproximada en el intervalo [{a}, {b}] es: {raiz:.6f}")
except ValueError as e:
    print(e)