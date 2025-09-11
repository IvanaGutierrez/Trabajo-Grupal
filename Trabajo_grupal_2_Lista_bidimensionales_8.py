""" Ejercicio 8: Matriz Identidad
Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad es una matriz
 cuadrada donde los elementos de la diagonal principal son 1 y el resto son 0. """
#importando libreria Numpy
import numpy as np
#declarando la variable n que nos va a dar la dimension de la matriz
n=3
#generando la matriz con ceros
matriz_identidad = np.zeros((n,n))
#recorriendo la fila de la matriz
for i in range(len(matriz_identidad)):
#recorriendo la columna dentro de la fila
    for j in range(len(matriz_identidad[i])):
#aqui estamos en la diagonal principal
        if j == (len(matriz_identidad[i])-1) - i:
#aqui rellenamos la diagonal            
            matriz_identidad[i][j] = 1
#imprimimos la matriz          
print(matriz_identidad)  

