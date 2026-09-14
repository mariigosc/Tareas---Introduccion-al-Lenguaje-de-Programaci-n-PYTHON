# ==============================================================================
# Procesamiento de Texto: Extracción de Títulos de Artículos Científicos
# Base de datos: abstract-neuroaesth-set.txt
# ==============================================================================

import os

print("------------------- ARTÍCULOS DE NEUROESTÉTICA -------------------")
print()

                                                                            # Nombre del archivo que contiene los abstracts
nombre_archivo = "abstract-neuroaesth-set.txt"

                                                                            # Obtenemos la ruta absoluta exacta de la carpeta donde reside este script
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, nombre_archivo)

                                                                            # 1. Lectura del archivo de texto usando la ruta completa
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

                                                                            # Lista para almacenar los títulos encontrados
titulos = []

                                                                            # 2. Búsqueda y extracción de títulos
for i in range(len(lineas)):
    linea_actual = lineas[i].strip()

                                                                                # Identificamos el inicio de un artículo (ej. "1.", "2.", "15.")
    partes = linea_actual.split(" ")
    if len(partes) > 0 and partes[0].replace(".", "").isdigit() and partes[0].endswith("."):
        
                                                                                    # En el formato de PubMed, el título está 2 renglones más abajo
        if i + 2 < len(lineas):
            posible_titulo = lineas[i + 2].strip()
            
                                                                                        # Si el título abarca un segundo renglón antes de los autores
            if i + 3 < len(lineas) and lineas[i + 3].strip() != "":
                posible_titulo = posible_titulo + " " + lineas[i + 3].strip()
            
            titulos.append(posible_titulo)

                                                                            # 3. Mostrar los resultados en pantalla
print(f"Total de artículos encontrados: {len(titulos)}")
print("------------------------------------------------------------------")
print()

numero = 1
for titulo in titulos:
    print(f"{numero}. {titulo}")
    numero = numero + 1

print()
print("------------------------------------------------------------------")