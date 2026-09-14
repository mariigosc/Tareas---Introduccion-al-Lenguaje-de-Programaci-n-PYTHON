# ==============================================================================
# TAREA 02
# ==============================================================================

import math                                                 # Para funciones matemáticas y constantes
import numpy as np                                          # Para discretización lineal y funciones trigonométricas
import random                                               # Para generación de números aleatorios


print("------------------- TAREA 02 -------------------")
print()


# ==============================================================================
# 5. Perímetro de un círculo mediante sus ecuaciones paramétricas:
#    x = 2 * sin(theta), y = 2 * cos(theta), theta en [0, 2*pi]
# ==============================================================================
print("5. Perímetro de un círculo mediante aproximación paramétrica:")
print()

def distancia(p1, p2):
    """Distancia euclidiana entre dos puntos (x, y)[cite: 2]"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Discretizamos el intervalo [0, 2*pi] con 1000 puntos usando numpy
teta = np.linspace(0, 2 * np.pi, 1000)

# Punto inicial con theta = teta[0]
x1 = 2 * np.sin(teta[0])
y1 = 2 * np.cos(teta[0])

perimetro = 0.0

# Iteramos sobre el resto de los puntos angulares
for tt in teta[1:]:
    x2 = 2 * np.sin(tt)
    y2 = 2 * np.cos(tt)
    
    perimetro = perimetro + distancia((x1, y1), (x2, y2))
    
    # Actualizamos el punto previo
    x1 = x2
    y1 = y2

print(perimetro)
print()
print("     Perímetro numérico aproximado =", perimetro)
print("     Perímetro analítico (2 * pi * r con r=2) =", 2 * math.pi * 2)
print()
print("----------------------------------------------------")