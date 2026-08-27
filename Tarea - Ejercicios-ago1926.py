# Importamos la clase math para pi, e, sqrt y factorial

import math 

print('\n')
print('\n')

print('Ejercicios-ago1926')
print('\n')

# ==========================================
# 1. Calcular las siguientes sumas
# Utilizamos la sentencia 'for' para iterar sobre el rango de 1 a 100

print("EJERCICIO 1")

# a. 1 + 1/2 + 1/3 + 1/4 + ... 1/100
suma_a = 0
for n in range(1, 101):
    suma_a = suma_a + (1 / n)
print(f"1.a: {suma_a}")

# b. 1 + 1/2^2 + 1/3^2 + ... 1/100^2
suma_b = 0
for n in range(1, 101):
    suma_b = suma_b + (1 / (n**2))
print(f"1.b: {suma_b}")

# c. Sumatoria de n/(n+1)
suma_c = 0
for n in range(1, 101):
    suma_c = suma_c + (n / (n + 1))
print(f"1.c: {suma_c}")

# d. Sumatoria de (-1)^n
suma_d = 0
for n in range(1, 101):
    suma_d = suma_d + ((-1)**n)
print(f"1.d: {suma_d}")

# e. Sumatoria de 1/(n(n+1))
suma_e = 0
for n in range(1, 101):
    suma_e = suma_e + (1 / (n * (n + 1)))
print(f"1.e: {suma_e}")

print('\n')

# ==========================================
# 2. Verificar la igualdad de 'e'

print("EJERCICIO 2 ")

suma_e_aprox = 0
# Usamos un número razonable de iteraciones (ej. 50) para simular el infinito
for n in range(50):
    suma_e_aprox = suma_e_aprox + (1 / math.factorial(n)) # Uso del método factorial de math[cite: 3]

print(f"Aproximación de e : {suma_e_aprox}")
print(f"Valor real math.e : {math.e}")

print('\n')

# ==========================================
# 3. Verificar las igualdades de pi

print("EJERCICIO 3")

# a. pi = 4 * sumatoria de (-1)^n / (2n+1)
suma_pi_a = 0
# Iteramos un millón de veces para acercarnos al infinito
for n in range(1000000):
    suma_pi_a = suma_pi_a + (((-1)**n) / ((2 * n) + 1))
pi_a = 4 * suma_pi_a

# b. pi = sqrt(6 * sumatoria de 1/n^2)
suma_pi_b = 0
for n in range(1, 1000000):
    suma_pi_b = suma_pi_b + (1 / (n**2))
pi_b = math.sqrt(6 * suma_pi_b) # Uso de math.sqrt[cite: 3]

print(f"3.a Aproximación de pi : {pi_a}")
print(f"3.b Aproximación de pi : {pi_b}")
print(f"Valor real math.pi     : {math.pi}")

print('\n')

# ==========================================
# 4. Procesamiento de Texto (String's)

print("EJERCICIO 4")

texto_original = """Environmental psychology examines transactions between individuals and their
built and natural environments. This includes investigating behaviors that inhibit
or foster sustainable, climate-healthy, and nature-enhancing choices,
antecedents and correlates of those behaviors, and interventions to promote
proenvironmental behavior. It also includes transactions in which nature
provides restoration or inflicts stress, and transactions that are more mutual,
such as the development of place attachment and identity and the impacts on
and from important physical settings such as home, workplaces, schools, and
public spaces. As people spend more time in virtual environments, online
transactions are coming under increasing research attention. Every aspect of
human existence occurs in one environment or another, and the transactions
with and within them have important consequences both for people and their
natural and built worlds. Environmental psychology matters."""

# a. Reemplace el cambio de linea \n por un espacio en blanco
texto_a = texto_original.replace('\n', ' ') 
# Método replace de la Clase String

print(f'4.a:')
print(texto_a)

print('\n')

# b. Reemplace todos los caracteres no alfabeticos por un espacio
texto_b = ""
for caracter in texto_a:
    # isalpha() evalúa si es una letra
    if caracter.isalpha() or caracter == ' ':
        texto_b = texto_b + caracter
    else:
        texto_b = texto_b + ' '

print(f'4.b:')
print(texto_b)

print('\n')

# c. Convierta caracteres mayúsculas en letras minúsculas
texto_c = texto_b.lower() 
# Método lower de la Clase String

print(f'4.c:')
print(texto_c)

print('\n')

# d. Convierta este string en una lista utilizando el espacio como separador
lista_palabras_a = texto_c.split(' ') # Método split

print(f'4.d:')
print(lista_palabras_a)

print('\n')

# Extra: limpiamos los espacios vacíos que dejó la división de espacios dobles
lista_palabras = []
for palabra in lista_palabras_a:
    if palabra != '': # Operador condicional
        lista_palabras.append(palabra) # Método append de Listas


# e. Utilice la funcion set para encontrar las palabras unicas
palabras_unicas = set(lista_palabras)

print(f'4.e:')
print(lista_palabras)

print('\n')

# f. Para cada una de las palabras unicas encuentre cuantas se repiten

print(f'4.f:')

print(f"Total de palabras únicas: {len(palabras_unicas)}")

print('\n')

print("Frecuencia de repetición de algunas palabras:")

for palabra_unica in palabras_unicas:
    # Usamos el método count() de las listas para contar ocurrencias
    repeticiones = lista_palabras.count(palabra_unica)
    
    # Imprimiremos solo como ejemplo aquellas que se repiten más de 2 veces para no saturar la pantalla
    if repeticiones > 2:
        print(f"'{palabra_unica}': {repeticiones} veces")

print('\n')