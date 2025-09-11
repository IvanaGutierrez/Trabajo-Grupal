""" Ejercicio 9: Matriz Identidad Inversa
Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz identidad inversa es una matriz 
cuadrada donde los elementos de la diagonal inversa principal son 1 y el resto son 0. """
#importando libreria Numpy
import numpy as np
#declarando la variable n que nos va a dar la dimension de la matriz
n=3
#generando la matriz con ceros
matriz_identidad_inversa = np.zeros((n,n))
#recorriendo la fila de la matriz
for i in range(len(matriz_identidad_inversa)):
#recorriendo la columna dentro de la fila
    for j in range(len(matriz_identidad_inversa[i])):
#aqui estamos en la diagonal principal
       if j == (len(matriz_identidad_inversa[i])-1) - i:
#aqui rellenamos la diagonal inversa           
            matriz_identidad_inversa[i][j] = 1
#imprimimos la matriz          
print(matriz_identidad_inversa)  
es_simetrica = np.array_equal(matriz_identidad_inversa, matriz_identidad_inversa.T)
print(es_simetrica)  # True