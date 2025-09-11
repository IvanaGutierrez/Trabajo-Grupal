def rotar_matriz_90(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    # Creamos la matriz rotada con dimensiones invertidas
    rotada = [[0] * filas for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            rotada[j][filas - 1 - i] = matriz[i][j]
    
    return rotada

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

rotada = rotar_matriz_90(matriz)

print("\nMatriz rotada 90°:")
for fila in rotada:
    print(fila)