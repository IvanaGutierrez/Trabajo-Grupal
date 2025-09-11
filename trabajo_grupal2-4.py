filas = int(input("Ingresa cantidad de filas: "))
columnas = int(input("Ingresa cantidad de columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

rotada = []
for i in range(columnas):
    fila_rotada = []
    for j in range(filas):
        fila_rotada.append(0)
    rotada.append(fila_rotada)

for i in range(filas):
    for j in range(columnas):
        rotada[j][filas - 1 - i] = matriz[i][j]

print("\nMatriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz rotada 90°:")
for fila in rotada:
    print(fila)
