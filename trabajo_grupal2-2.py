n = int(input("¿Cuántos números tendrá la lista? "))
numeros = []

for i in range(n):
    valor = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(valor)

mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print("El número mayor es:", mayor)
print("El número menor es:", menor)