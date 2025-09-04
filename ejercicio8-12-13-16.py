#8
texto = input("Ingresa una cadena: ")
resultado = texto.replace("a", "e").replace("A", "E")
print("Resultado:", resultado)

#12
cadena = "hipopotamo"
cuarta = cadena[3]   # índices empiezan en 0
quinta = cadena[4]
print("La cuarta letra es:", cuarta)
print("La quinta letra es:", quinta)

#13
cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

if cadena2 in cadena1:
    print("La segunda cadena SÍ está dentro de la primera.")
else:
    print("La segunda cadena NO está dentro de la primera.")

#16
def contiene_numeros(cadena):
    return any(ch.isdigit() for ch in cadena)

print(contiene_numeros("Hola123")) 
print(contiene_numeros("Hola"))    