# Importamos los módulos necesarios para cálculos y graficación
import numpy as np
import matplotlib.pyplot as plt
import random

# ==============================================================================
# DATOS DEL PROBLEMA
# ==============================================================================
# Definimos la lista de edades proporcionada en el ejercicio y la convertimos 
# en un arreglo de numpy para facilitar los cálculos matemáticos.
datos = [48, 35, 46, 44, 43, 42, 39, 44, 49, 49, 44, 39, 38, 49, 49, 53, 56, 57, 51, 61, 53, 66, 
         71, 75, 72, 65, 67, 38, 37, 46, 44, 44, 48, 49, 30, 45, 47, 45, 48, 47, 47, 44, 48, 43, 
         45, 40, 48, 49, 38, 44, 43, 47, 46, 57, 52, 54, 56, 53, 64, 53, 58, 54, 59, 56, 62, 50, 
         64, 53, 61, 53, 62, 57, 52, 54, 61, 59, 57, 52, 54, 53, 62, 52, 62, 57, 59, 59, 56, 57, 
         53, 59, 61, 55, 61, 56, 52, 54, 51, 50, 50, 55, 63, 50, 59, 54, 60, 50, 56, 68, 66, 71, 
         82, 68, 78, 66, 70, 66, 78, 69, 71, 69, 78, 66, 68, 71, 69, 77, 76, 71, 43, 47, 48, 37, 
         40, 42, 38, 49, 43, 46, 34, 46, 46, 48, 47, 43, 52, 53, 61, 60, 53, 53, 50, 53, 54, 61, 
         61, 61, 64, 53, 53, 54, 61, 60, 51, 50, 53, 64, 64, 53, 60, 54, 55, 58, 62, 62, 54, 53, 
         61, 54, 51, 62, 57, 50, 64, 63, 65, 71, 71, 73, 66]

poblacion = np.array(datos)

# ==============================================================================
# PARTE 1: ESTADÍSTICA DESCRIPTIVA DE LA POBLACIÓN
# ==============================================================================
print("--- 1. ESTADÍSTICAS DE LA POBLACIÓN ---")

media = np.mean(poblacion)
mediana = np.median(poblacion)
# Usamos ddof=0 porque el ejercicio indica que debemos considerar los datos como UNA POBLACIÓN entera
desviacion_estandar = np.std(poblacion, ddof=0)
varianza = np.var(poblacion, ddof=0)

# Para el Rango Intercuartil (IQR) calculamos el Cuartil 3 (75%) y Cuartil 1 (25%)
q3, q1 = np.percentile(poblacion, [75, 25])
rango_intercuartil = q3 - q1

minimo = np.min(poblacion)
maximo = np.max(poblacion)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Rango Intercuartil (IQR): {rango_intercuartil}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}\n")

# ==============================================================================
# PARTE 2: HISTOGRAMA DE LA POBLACIÓN
# ==============================================================================
# Creamos una figura para mostrar el primer histograma
plt.figure(figsize=(8, 5))
plt.hist(poblacion, bins=15, color='skyblue', edgecolor='black')
plt.title("Histograma de Edades de la Población")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
# Descomenta la siguiente línea si deseas ver la gráfica al instante, o déjala 
# así para ver todas juntas al final.
# plt.show() 

# ==============================================================================
# PARTE 3: OBTENCIÓN DE MUESTRAS
# ==============================================================================
print("--- 2. EXTRACCIÓN DE 20 MUESTRAS Y CÁLCULO DE MEDIAS ---")

muestras = []        # Lista para guardar las 20 muestras (cada una de 10 datos)
medias_enteras = []  # Lista para guardar las medias de cada muestra

# Usamos un ciclo FOR para repetir el proceso 20 veces
for i in range(20):
    # random.sample toma 'n' elementos al azar sin reemplazo de la lista
    muestra_actual = random.sample(datos, 10)
    muestras.append(muestra_actual)
    
    # Calculamos la media de esta muestra y la convertimos a un número entero
    # como lo pide la instrucción.
    media_entera = int(np.mean(muestra_actual))
    medias_enteras.append(media_entera)

print(f"Las medias enteras de las 20 muestras son: {medias_enteras}")

# ==============================================================================
# PARTE 4: HISTOGRAMA DE LAS MEDIAS Y BOXPLOT
# ==============================================================================
# Creamos una figura con dos "sub-gráficos" (1 fila, 2 columnas) para ver ambos a la vez
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 1. Histograma de las medias de las 20 muestras
ax1.hist(medias_enteras, color='lightgreen', edgecolor='black', bins=8)
ax1.set_title("Histograma de las Medias de las Muestras")
ax1.set_xlabel("Media (Entero)")
ax1.set_ylabel("Frecuencia")

# 2. Boxplot de las 20 muestras
# Al pasar la lista de listas 'muestras', matplotlib genera una caja por cada muestra
ax2.boxplot(muestras)
ax2.set_title("Boxplot de las 20 Muestras (Tamaño 10)")
ax2.set_xlabel("Número de Muestra")
ax2.set_ylabel("Edades")

# Ajustar el diseño para que no se empalmen y mostrar todas las gráficas creadas
plt.tight_layout()
plt.show()