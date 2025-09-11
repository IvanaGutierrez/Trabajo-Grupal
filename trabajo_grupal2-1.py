n = int(input("¿Cuántos números tendrá la lista? "))
numeros = []

for i in range(n):
    valor = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(valor)
suma = 0
for n in numeros:
    suma = suma + n

print("La suma de los elementos es:", suma)