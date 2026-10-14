import numpy as np

def calcular_skewness(datos):
    x = np.array(datos)
    n = len(x) # longitud de vector
    x_barra = np.mean(x) # media de x
    
    # Numerador: raíz cuadrada de 'n' multiplicada por la sumatoria de (x_i - x_barra)^3
    numerador = np.sqrt(n) * np.sum((x - x_barra)**3)
    
    # Denominador: sumatoria de (x_i - x_barra)^2 elevada a la 3/2
    denominador = (np.sum((x - x_barra)**2))**(3/2)
    
    skewness = numerador / denominador
    return skewness

def calcular_kurtosis(datos):
    """
    Medida para evaluar qué tan parecido es la distribución de los datos 
    con la distribución norma
    """
    x = np.array(datos)
    n = len(x) # longitud de vector
    x_barra = np.mean(x) # media de x
    
    # Numerador: 'n' multiplicada por la sumatoria de (x_i - x_barra)^4
    numerador = n * np.sum((x - x_barra)**4)
    
    # Denominador: sumatoria de (x_i - x_barra)^2 elevada al cuadrado
    denominador = (np.sum((x - x_barra)**2))**2
    
    # Se divide el numerador entre el denominador y se le resta 3
    kurtosis = (numerador / denominador) - 3
    return kurtosis

# ==========================================
# PRUEBA DE LAS FUNCIONES
# ==========================================
# Utilizamos el vector de prueba que aparece en la pantalla
x = (3, 2, 3, 4, 5, 6, 7)

resultado_skewness = calcular_skewness(x)
resultado_kurtosis = calcular_kurtosis(x)

print(f"Datos: {x}")
print(f"Skewness (Asimetría): {resultado_skewness:.4f}")
print(f"Kurtosis (Curtosis): {resultado_kurtosis:.4f}")

```
