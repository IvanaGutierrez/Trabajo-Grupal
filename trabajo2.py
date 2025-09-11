#ej5
numero = [2, 3, 4, 5, 6]
valor = int(input("ingrese un valor para multiplicar cada elemento de la lista: "))

resultado = []  

for elemento in numero:       
    multiplicado = elemento * valor
    resultado.append(multiplicado)  

print("lista:", numero)
print("lista multiplicada:", resultado)


#ej6
ingreso = input("ingrese una lista de numeros: ")
lista = [int(num) for num in ingreso.split()]

lista2 = []  

for num in lista:                
    if num not in lista2:        
        lista2.append(num)       

print("lista original:", lista)
print("lista sin duplicados:", lista2)


#ej7
ingreso = input("ingrese una lista de numeros para sacar el promedio: ")
lista = [int(num) for num in ingreso.split()]

suma = 0
contador = 0

for num in lista:      
    suma += num        
    contador += 1      

promedio = suma / contador

print("el promedio de los elementos es:", promedio)



#ej8
ingreso=(input("ingrese una lista de numeros:"))

lista=[int(num) for num in ingreso.split()]
vistos = set()
repetidos = set()

for num in lista:
    if num in vistos:
        repetidos.add(num) 
    else:
        vistos.add(num)

print("Lista original:", lista)
print("Elementos repetidos:", list(repetidos))