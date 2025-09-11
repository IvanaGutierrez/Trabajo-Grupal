""" Ejercicio 6: Multiplicar una Matriz por un Escalar
Escribe un programa que multiplique cada elemento de una
lista bidimensional por un valor escalar dado por el usuario. """
import numpy as np
matriz_numpy = np.array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
])
print(matriz_numpy)
valor_escalar = float(input("Ingrese el valor por el cual desea mutiplicar la matriz"))

# Multiplicar la matriz por el escalar
matriz_resultante =  np.zeros_like(matriz_numpy)

for i in range(len(matriz_numpy)):
    for j in range(len(matriz_numpy[i])):

     matriz_resultante[i][j] = valor_escalar * matriz_numpy[i][j]

print(matriz_resultante)
