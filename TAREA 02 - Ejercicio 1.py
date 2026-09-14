# ==============================================================================
# TAREA 02
# ==============================================================================

import math                                                 # Para funciones matemáticas y constantes
import numpy as np                                          # Para discretización lineal y funciones trigonométricas
import turtle                                               # Para gráficos vectoriales y fractales 
import random                                               # Para generación de números aleatorios

print("------------------- TAREA 02 -------------------")
print()

# ==============================================================================
# 1. Hacer una función en Python para que calcule el factorial de un número natural.
# ==============================================================================

print("----------------------------------------------------")
print("1. Función para calcular el factorial de un número natural:")
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

# Datos de prueba
n_ejemplo = 4
resultado_fact = calcular_factorial(n_ejemplo)

print(resultado_fact)
print()
print(f"     El factorial de {n_ejemplo} ({n_ejemplo}!) es =", resultado_fact)
print()
print("----------------------------------------------------")