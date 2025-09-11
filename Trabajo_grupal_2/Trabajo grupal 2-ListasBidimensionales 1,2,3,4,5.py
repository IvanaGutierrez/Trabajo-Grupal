#Ejercicio 1

def matriz(filas,columnas):

    #Creo la matriz de manera dinamica.
    matrixrellenada = []

    #El contador es para rellenarla de manera ascendente.
    contador = 1

    #El bucle i se encarga de crear una nueva fila cada vez.
    for i in range(filas):
        fila = []

    #El bucle j se encarga de rellenar esa fila con columnas.
        for j in range(columnas):
            fila.append(contador)
            contador +=1
    #Guardo la lista matriz generada del bucle(fila = []) en la matriz que genere por fuera para que no ser pierdan los datos cuando salga del bucle.
        matrixrellenada.append(fila)
    #La retorno para que el metodo la devuelva.
    return matrixrellenada

filas_pedida_al_usuario = int(input("Introduce el numero de filas de su matriz: "))
columnas_pedida_al_usuario = int(input("Introduce el numero de columna de su matriz: "))

#Paso los Argumentos al metodo y los recibe como parametros para poder crear la matriz.
m = matriz(filas_pedida_al_usuario, columnas_pedida_al_usuario)

#Recorro la matriz nueva y la imprimo.
for fila in m:
    print(fila)

print("")

#Ejercicio 2

matriz2 = [
    [1,2,3],
    [4,5,6]
]

#Total acumula la suma elemento es una variable temporal representa cada numero en la matriz 'for filaa in matriz2' sirve para iterar las filas y 'for elemento in filaa' itera las columnas 
total = sum(elemento for filaa in matriz2 for elemento in filaa)

print("Suma de Todos los Elementos:",total)

print("")

#Ejercicio 3

total2 = 0
contador_de_fila = 0

matriz3 = [
    [1,2,3],
    [4,5,6]
]

contador_de_fila = 1

for p in matriz3:          
    total2 = 0             
    for numero in p:        
        total2 += numero   
    print(f"La Suma de la fila {contador_de_fila} es: {total2}")
    contador_de_fila += 1

print("")

#Ejercicio 4

filas = 3
columnas = 3
contador = 1

matriz4 = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(contador)
        contador += 1
    matriz4.append(fila)

print("Matriz normal:\n ",matriz4)

# len(matriz4[0] = numero columna de la matriz original , len(matriz4) = numero de filas de la matriz original.
#matriz4[j][i]  Toma el elemento de la fila j y columna i de la matriz original y lo añade a la nueva fila de la transpuesta.

transpuesta = [[matriz4[j][i] for j in range(len(matriz4))] for i in range(len(matriz4[0]))]

print("Matriz Transpuesta:\n",transpuesta)

print("")

#Ejecicio5

matriz5 = [
    [42, 22, 102],
    [93, 55, 63],
    [250, 10, 13]
]

#Max es una funcion que devuelve el valor mas grande al ser una lista bidimensional debo o usar 2 bucles o Comprehension para poder recorrerla y que la funcion 'Max' determine el elemento mas grande
#Si hicieramos esto max(matriz5) obtendriamos la columna mas grande de la matriz lo cual es incorrecto para este ejercicio.

valormasgrande = max(elementotemp for filaejer5 in matriz5 for elementotemp in filaejer5)

print(valormasgrande)
