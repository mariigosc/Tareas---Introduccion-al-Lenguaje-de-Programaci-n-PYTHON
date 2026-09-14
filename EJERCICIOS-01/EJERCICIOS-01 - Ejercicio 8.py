# EJERCICIOS-01 #
# 8. Encontrar el área de un triangulo cuyos vertices son p1(2,2), p2(3,4) y p3(1, 5): #

print("8. Encontrar el área de un triangulo cuyos vertices son p1(2,2), p2(3,4) y p3(1, 5):")
print()

import math

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