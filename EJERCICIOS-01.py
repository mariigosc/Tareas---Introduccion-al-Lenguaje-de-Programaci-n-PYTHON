# EJERCICIOS-01 #

print("------------------- EJERCICIOS-01 -------------------")
print()
import math

print("----------------------------------------------------")
# 1. Calcular el volumen de una esfera cuyo radio es de 5 cm: #

print("1. Calcular el volumen de una esfera cuyo radio es de 5 cm:")
print()

# Datos
r = 5                           # r = radio en cm

# Formula matemática:
v = (4/3) * math.pi * r**3      # v = volumen en cm

print(v)

print()
print("     El volumen de una esfera cuyo radio es de 5 cm es =", v)
print()
print("----------------------------------------------------")

# 2. Calcular el volumen de un cilindro cuya altura es de 50 cm y radio es de 5cm: #

print("2. Calcular el volumen de un cilindro cuya altura es de 50 cm y radio es de 5cm:")
print()

# Datos
r = 5                           # r = radio en cm
h = 50                          # h = altura en cm

# Formula matemática:
v = math.pi * r**2 * 50      # v = volumen en cm

print(v)

print()
print("     El volumen de un cilindro cuya altura es de 50 cm y radio es de 5cm =", v)
print()
print("----------------------------------------------------")

# 3. Covertir el número 777 a número binario: #

print("3. Covertir el número 777 a número binario:")
print()

num = 777

                                            # Aplicamos la primera división entre 2:
                                            # - El operador '//' calcula la división entera (descarta los decimales: 777 // 2 = 388).
                                            # - El operador '%' (módulo) obtiene el residuo (777 % 2 = 1).
                                            # Este primer residuo corresponde al dígito menos significativo (extremo derecho del binario).
cociente = num//2
residuo = num % 2

                                            # Convertimos el residuo numérico a tipo texto (string) con str().
                                            # Esto nos permitirá concatenar caracteres en lugar de sumarlos numéricamente.
bin = str(residuo)

                                            # El algoritmo se repite mientras el cociente sea mayor que cero.
while cociente > 0:
  print(cociente)
  coci = cociente//2
  residuo = cociente % 2
  bin = bin + str(residuo)
                                            # Actualizamos el cociente con el nuevo valor calculado para la siguiente iteración.
                                            # Cuando llegue a 0, la condición del while se volverá falsa y el ciclo terminará.
  cociente = coci

print()
print("     El 777 en número binario: =", bin)
print()
print("----------------------------------------------------")

# 4. Convertir el número binario 1011001 a número entero. #

print("4. Convertir el número binario 1011001 a número entero:")
print()

bin='1011001'

#bin = '101' # 2

len = len(bin)

suma = 0
for i in range(len):
  c = bin[-1-i]
  suma = suma + float(c) * 2**i

print(suma)
print("     El número binario 1011001 a número entero =", suma)
print()
print("----------------------------------------------------")

# 5. Calcular la distancia entre los puntos p1(1,2) y p2(5,7): #

print("5. Calcular la distancia entre los puntos p1(1,2) y p2(5,7):")
print()

# Datos
    # p1 (1,2) y p2 (5,7)
x1 = 1
x2 = 2
y1 = 5
y2 = 7

# Formula matemática:
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)      # d = distancia

print(d)

print()
print("     La distancia entre los puntos p1(1,2) y p2(5,7) =", d)
print()
print("----------------------------------------------------")

# 6. Convertir 60 grados Fahrenheit a grados Celsius: #

print("6. 60 grados Fahrenheit a grados Celsius:")
print()

# Datos
f = 60              # f = grados Fahrenheit

# Formula matemática:
C = (f - 32) * 5/9

print(C)

print()
print("     60 grados Fahrenheit en Celsius =", C)
print()
print("----------------------------------------------------")

# 7. Convertir 60 grados Celsius a grados Fahrenheit: #

print("7. Convertir 60 grados Celsius a grados Fahrenheit:")
print()

# Datos
c = 60              # c = grados Celsius

# Formula matemática:
F = (c * 9/5) + 32

print(F)

print()
print("     Celsius a grados Fahrenheit =", F)
print()
print("----------------------------------------------------")

# 8. Encontrar el área de un triangulo cuyos vertices son p1(2,2), p2(3,4) y p3(1, 5): #

print("8. Encontrar el área de un triangulo cuyos vertices son p1(2,2), p2(3,4) y p3(1, 5):")
print()

# Datos
# p1(2,2), p2(3,4) y p3(1, 5)

# Punto 1: p1(2, 2)
x1 = 2
y1 = 2

# Punto 2: p2(3, 4)
x2 = 3
y2 = 4

# Punto 3: p3(1, 5)
x3 = 1
y3 = 5

term1 = x1*(y2-y3)
term2 = x2*(y3-y1)
term3 = x3*(y1-y2)

# Formula matemática:
a = (1/2)*abs(term1+term2+term3)          # a = area

print(a)

print()
print("     El área de un triangulo cuyos vertices son p1(2,2), p2(3,4) y p3(1, 5) =", a)
print()
print("----------------------------------------------------")

# 9. Responder si un número es par o impar. Utilice el codigo: #
# nombre = input("¿Cómo te llamas? ")
# print(f"Hola, {nombre}")

print("- ¿Cómo te llamas? ")
nombre = input("- " )
print()

print(f"- Hola, {nombre}")

print(f" {nombre}, introduce un número entero:")
numero = int(input("- " ))          # Se lee y convierte a entero en el renglón de abajo
print()

# Evaluar el condicional (if / else) con (%)
        # - El operador '%' calcula el residuo de la división entera entre 2.
        # - Si el residuo es exactamente 0 (numero % 2 == 0), el número es divisible entre 2 -> PAR.
        # - De lo contrario (residuo diferente de 0), el número es -> IMPAR.

if numero % 2 == 0:
    print(f"- {nombre}, el número {numero} es par")
    print()
else:
    print(f"- {nombre}, el número {numero} es impar")
    print()