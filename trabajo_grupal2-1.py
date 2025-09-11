numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

suma = 0
for n in numeros:
    suma = suma + n

print("La suma de los elementos es:", suma)
