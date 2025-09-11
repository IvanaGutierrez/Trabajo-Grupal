numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))
pares = sum(1 for n in numeros if n % 2 == 0)
impares = len(numeros) - pares
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
