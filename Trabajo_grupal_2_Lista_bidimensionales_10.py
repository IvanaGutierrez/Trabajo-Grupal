""" Ejercicio 10: Verificar Matriz Simétrica
Una matriz es simétrica si es igual a su transpuesta. 
Escribe un programa que verifique si una matriz es simétrica. """
import numpy as np

matriz_a = np.array([
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
])

# Comparar con su transpuesta
es_simetrica = np.array_equal(matriz_a, matriz_a.T)
print(es_simetrica)  # True