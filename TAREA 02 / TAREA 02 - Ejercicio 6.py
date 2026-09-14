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
# 6. Dibujar 50 círculos aleatorios en la ventana [-200, 200] x [-200, 200]
#    con radio aleatorio entre 10 y 20 unidades inclusive.
# ==============================================================================
print("6. Dibujando 50 círculos aleatorios con turtle...")

                                                            # Limpiamos el lienzo para el siguiente dibujo
turtle.clearscreen()
turtle.setup(width=600, height=600)
turtle.speed(0)

                                                            # Dibujamos los 50 círculos solicitados
for _ in range(50):
                                                                # Radio aleatorio entre 10 y 20 inclusive
    radio = random.randint(10, 20)
    
                                                                # Coordenadas aleatorias dentro de la ventana de [-200, 200]
    x_azar = random.randint(-200, 200)
    y_azar = random.randint(-200, 200)
    
    turtle.penup()
    turtle.goto(x_azar, y_azar)
    turtle.pendown()
    
                                                                # Función circle solicitada en el enunciado
    turtle.circle(radio)

print("     50 círculos trazados correctamente.")
print()
print("----------------------------------------------------")

                                                            # Mantiene abierta la ventana interactiva de turtle al finalizar
turtle.mainloop()
