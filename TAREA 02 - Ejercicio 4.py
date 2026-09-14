# ==============================================================================
# TAREA 02
# ==============================================================================

import math                                                 # Para funciones matemáticas y constantes
import turtle                                               # Para gráficos vectoriales y fractales 


print("------------------- TAREA 02 -------------------")
print()

# ==============================================================================
# 4. Graficar el L-Sistema (Fractal de Sierpinski):
#    Variables: F, G
#    Constantes: +, -
#    Inicio: F - G - G
#    Reglas: F -> F - G + F + G - F, G -> GG
#    Ángulo: 120 grados
# ==============================================================================

print("4. Graficando L-Sistema con turtle...")

turtle.clearscreen()
turtle.speed(0)
turtle.penup()
turtle.goto(-250, 200) # Centrado en la ventana de dibujo
turtle.pendown()

cadena = "F-G-G"
n_iteraciones = 4                                  # Nivel de iteración para visualizar la estructura del fractal
angulo = 120
longitud_paso = 8

                                                   # Sustitución simultánea construyendo una nueva cadena carácter por carácter[cite: 3]
for _ in range(n_iteraciones):
    nueva_cadena = ""
    for char in cadena:
        if char == "F":
            nueva_cadena = nueva_cadena + "F-G+F+G-F"
        elif char == "G":
            nueva_cadena = nueva_cadena + "GG"
        else:
            nueva_cadena = nueva_cadena + char
    cadena = nueva_cadena

                                                    # Trazado de las instrucciones generadas
for simbolo in cadena:
    if simbolo == "F" or simbolo == "G":
        turtle.forward(longitud_paso)
    elif simbolo == "+":
        turtle.left(angulo)
    elif simbolo == "-":
        turtle.right(angulo)

print("     Dibujo del L-Sistema finalizado.")
print()
print("----------------------------------------------------")