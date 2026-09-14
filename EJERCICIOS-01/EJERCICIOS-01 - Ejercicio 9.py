# EJERCICIOS-01 #

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