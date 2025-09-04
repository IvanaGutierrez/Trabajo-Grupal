#ej5
texto=input("ingrese una cadena")
resultado= " "

for caracter in texto:
    if caracter != " " :
        resultado += caracter
print(resultado)



#ej6
cadena= " la lluvia en Mendoza es Escasa"
contador=0

for caracter in cadena:
    contador+=1
print("numero de caracteres", contador)



#ej7
cadena=input("ingrese una cadena:")
contador=0
vocales=0

for caracter in cadena:
    contador+=1
    if caracter.lower() in "aeiou" :
       vocales+=1
print("cantidad de caracteres:", contador)
print("cantidad de vocales:", vocales)


#ej11
cadena1=input("ingrese una cadena:")
cadena2=input("ingrese otra cadena:")
if cadena1==cadena2 :
    print("las palabras son iguales")
else:
    print("son distintas")
