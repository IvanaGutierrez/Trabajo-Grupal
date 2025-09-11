numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
