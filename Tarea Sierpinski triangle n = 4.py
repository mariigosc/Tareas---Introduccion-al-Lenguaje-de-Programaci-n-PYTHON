import turtle

# Configuración básica para n = 4

turtle.speed(4)                 # Velocidad moderada para observar el trazo
                                # speed rendimiento del código al ejecutarse y a la rapidez con la que se pueden desarrollar programas con este lenguaje
turtle.penup()                  # para levantar el lápiz virtual en los gráficos
turtle.goto(-200, 150)          # Ajuste de posición inicial
turtle.pendown()                # sirve para bajar el lápiz del cursor en el módulo gráfico turtle, lo que permite que la tortuga dibuje una línea en la pantalla mientras se mueve

linea = 'F-G-G'
n = 4
angulo = 120
longitud_paso = 20              # Trazo medio

# string
for iteracion in range(n):
    nueva_linea = ""
    for caracter in linea:
        if caracter == 'F':
            nueva_linea = nueva_linea + "F-G+F+G-F"
        elif caracter == 'G':
            nueva_linea = nueva_linea + "GG"
        else:
            nueva_linea = nueva_linea + caracter
    linea = nueva_linea

# Dibujo del fractal
for instruccion in linea:
    if instruccion == 'F' or instruccion == 'G':
        turtle.forward(longitud_paso)
    elif instruccion == '+':
        turtle.left(angulo)
    elif instruccion == '-':
        turtle.right(angulo)




turtle.mainloop()           # Evita que la ventana se cierre al terminar