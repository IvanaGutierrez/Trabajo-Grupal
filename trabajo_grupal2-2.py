numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print("El número mayor es:", mayor)
print("El número menor es:", menor)
