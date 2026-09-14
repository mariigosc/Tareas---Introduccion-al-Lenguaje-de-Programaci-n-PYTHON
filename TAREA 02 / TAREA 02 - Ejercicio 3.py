# ==============================================================================
# TAREA 02
# ==============================================================================

import math                                                 # Para funciones matemáticas y constantes


print("------------------- TAREA 02 -------------------")
print()

# ==============================================================================
# 3. Serie de Fibonacci hasta que el último número no sea mayor que 1000.
#    Inicia con 0 y 1; cada número subsecuente es la suma de los dos anteriores.
# ==============================================================================
print("3. Serie de Fibonacci (términos menores o iguales a 1000):")
print()

# Comenzamos con los dos términos base
a = 0
b = 1

fibonacci = [a, b]

# Usamos una estructura while para generar la serie mientras no supere 1000
while True:
    siguiente = a + b
    if siguiente > 1000:
        break
    fibonacci.append(siguiente)
    a = b
    b = siguiente

print(fibonacci)
print()
print("     Secuencia generada:", fibonacci)
print("     Último término no mayor a 1000 =", fibonacci[-1])
print()
print("----------------------------------------------------")
