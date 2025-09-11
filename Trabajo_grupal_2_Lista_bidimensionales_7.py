""" Ejercicio 7: Diagonal de una Matriz Cuadrada
Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada. """

matriz_cuadrada = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(matriz_cuadrada)
for i in range(len(matriz_cuadrada)):
    for j in range(len(matriz_cuadrada[i])):
        if i==j:
            print(matriz_cuadrada[i][j])