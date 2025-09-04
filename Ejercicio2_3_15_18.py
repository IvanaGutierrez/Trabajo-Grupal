""" 2- Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué
ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique. """
""" # Pedimos una nota entre 0 y 10
nota = int(input("Ingrese una nota (0 a 10): "))

# Mientras la nota no esté en el rango correcto...
while nota < 0 or nota > 10:
    print("Error: la nota debe estar entre 0 y 10.")
    nota = int(input("Ingrese una nota válida (0 a 10): "))

# Cuando sale del bucle, ya es válida
print("La nota ingresada es válida:", nota) """
""" 3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
14. Plantee el algoritmo planteando métodos para su resolución. """
""" #Solicitamos un numero de tres digitos
numero_tres_digitos = int(input("Ingrese un numero de 3 digitos: "))
#validamos que sea de 3 digitos
while numero_tres_digitos < 100 or numero_tres_digitos >999:
    print("Error no es un numero de 3 digitos")
    numero_tres_digitos = int(input("Ingrese un numero de 3 digitos: "))
suma = 0 #acumulador
while numero_tres_digitos > 0:
    digito = numero_tres_digitos % 10   # extrae el último dígito
    suma += digito         # suma el dígito
    numero_tres_digitos //= 10          # quita el último dígito    
print("La suma de los dígitos es:", suma) """
""" 15- Indique que sucede si realizo la siguiente declaración de variable:
x = None print(x)
Explique y ejemplifique el uso de None """

#¿Qué es None en Python?

#None es un objeto especial en Python que representa la ausencia de valor o que algo no está definido.

#Es del tipo NoneType.

#No significa 0, ni False, ni una cadena vacía "". Es un valor propio y distinto.

#Usos comunes de None:

#Inicializar variables antes de asignarles un valor real:

resultado = None
if 10 > 5:
    resultado = "Mayor"
print(resultado)   # → Mayor

#Valores por defecto en funciones:
def saludar(nombre=None):
    if nombre is None:
        print("Hola, invitado")
    else:
        print(f"Hola, {nombre}")
saludar()        # → Hola, invitado
saludar("Ivana") # → Hola, Ivana

# Para indicar que una función no devuelve nada:

def sumar(a, b):
    print(a + b)

resultado = sumar(2, 3)  # imprime 5
print(resultado)         # imprime None, porque la función no devuelve nada

# En resumen: None = "sin valor asignado". Es muy útil cuando queremos marcar que una variable aún no tiene un dato válido o que una función no retorna nada.