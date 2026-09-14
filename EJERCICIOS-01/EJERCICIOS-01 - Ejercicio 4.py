# EJERCICIOS-01 #
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