# ==============================================================================
# TAREA 02
# ==============================================================================

import math                                                 # Para funciones matemáticas y constantes


print("------------------- TAREA 02 -------------------")
print()

# ==============================================================================
# 2. Función que dado un número natural y un número x en R calcule la serie: x + x^2/2! + x^3/3! + ... + x^100/100!
# ==============================================================================

print("2. Serie exponencial S = sum(x^k / k!) hasta el término n:")
print()

def calcular_factorial(n):
    """
    Calcula n! mediante un ciclo acumulativo.
    El factorial de 0 es 1 por definición matemática.
    """
    if n < 0:
        return "El factorial solo está definido para números naturales (n >= 0)"
    
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def calcular_serie(x, n):
    """
    Calcula la serie de Taylor de e^x utilizando la función factorial.
    """
    suma = 0.0
    for k in range(n + 1):
        # Término k: x^k / k!
        # Para k = 0 -> x^0 / 0! = 1
        # Para k = 1 -> x^1 / 1! = x
        termino = (x ** k) / calcular_factorial(k)
        suma = suma + termino
    return suma

# Datos del ejercicio
x_val = 2.0
n_val = 100  # Límite indicado en la sumatoria

resultado_serie = calcular_serie(x_val, n_val)

print(resultado_serie)
print()
print(f"     El resultado de la serie para x = {x_val} con n = {n_val} es =", resultado_serie)
print(f"     Comprobación con math.exp({x_val}) =", math.exp(x_val))
print()
print("----------------------------------------------------")
