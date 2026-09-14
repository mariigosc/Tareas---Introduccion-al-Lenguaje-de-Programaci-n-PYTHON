# EJERCICIOS-01 #
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