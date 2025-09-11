numeros = input("Ingresa elementos separados por espacio: ").split()

invertida = []
for i in range(len(numeros)-1, -1, -1):
    invertida.append(numeros[i])

print("Lista invertida:", invertida)