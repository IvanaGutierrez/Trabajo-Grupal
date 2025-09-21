

def main():
    golosinas = [
        ["Codigo producto", "Golosina", "Stock"],
        [1, "KitKat", 20],
        [2, "Chicles", 50],
        [3, "Caramelos de Menta", 50],
        [4, "Huevo Kinder", 10],
        [5, "Cheetos", 10],
        [6, "Twix", 10],
        [7, "M&M'S", 10],
        [8, "Papas Lays", 2],
        [9, "Milkybar", 10],
        [10, "Alfajor Tofi", 15],
        [11, "Lata Coca", 20],
        [12, "Chitos", 10]
    ]
    
    empleados = {
        1100: "José Alonso",
        1200: "Federico Pacheco",
        1300: "Nelson Pereira",
        1400: "Osvaldo Tejada",
        1500: "Gastón García"
    }
    
    golosinas_pedidas = [
        ["Código golosina", "Denominación golosina", "Cantidad total pedida"]
    ]
    claves_tecnico = ('admin', 'CCCDDD', 2020)


    while True:  # Bucle principal del menú
        opcion = input("Elige una opción (A)(B)(C)(D)(S para salir): ").upper()

        if opcion == "A":
            legajo = int(input("Ingresa tu legajo: "))
            if validar_legajo(empleados, legajo):#verifica que el nro de legajo se encuentre en la lista
                seguir = True
                while seguir:
                    seguir = pedir_golosinas(golosinas, golosinas_pedidas)#si es empleadom puede pedir golosina
            else:
                print("Usted no es un empleado de la empresa.")#si ingresa un legajo que no corresponde a un empleado
                
        elif opcion == "B":
            mostrar_golosinas(golosinas)#llamando funcion mostrar lista de golosinas
        elif opcion == "C":
            if validar_tecnico(claves_tecnico):
                recargar_golosina(golosinas)
        elif opcion == "D":
            apagar_maquina(golosinas_pedidas)
            break
        elif opcion == "S":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def validar_legajo(empleados, legajo):
    return legajo in empleados#buscando legajo en diccionario empleados

def mostrar_golosinas(golosinas):
    for fila in golosinas:#recorriendo fila de golosinas
        print(fila) #mostrando lista de golosinas

def pedir_golosinas(golosinas, golosinas_pedidas): 
    codigo = input("Ingrese el código de la golosina que quiere (o 'salir'): ")
    
    if codigo.lower() == "salir": #convierte a minuscula
        return False#retorna falso para salir del ciclo
    
    if not codigo.isdigit():   # Verifica si NO son solo números
        print("Ingrese un número válido o 'salir'.")
        return True
    
    codigo = int(codigo)  # Ahora es seguro convertirlo
   

    for i in range(1, len(golosinas)):
        if golosinas[i][0] == codigo:
            if golosinas[i][2] > 0: #comprobando que haya stock
                golosinas[i][2] -= 1 #descontando la golosina extraida
                print(f"Se entregó {golosinas[i][1]}, stock restante: {golosinas[i][2]}")#mostrando que golosina se enttrego y ctas quedan
                registrar_golosinas_pedidas(codigo, golosinas[i][1], golosinas_pedidas)#registrando golosina pedida
            else:
                print(f"Lo sentimos, la golosina {golosinas[i][1]} no está disponible.") #sino hay stock le muestra 
                #este mensaje con el nombre de laa golosina
            return True

    print("Código no encontrado.")
    return True

def registrar_golosinas_pedidas(codigo, nombre, golosinas_pedidas):
    for fila in golosinas_pedidas[1:]:#recorriendo desde la fila 1
        if fila[0] == codigo: #verificando el codigo de la golosina en la fila 0
            fila[2] += 1 #agregando a la lista de golosinas pedidas
            return
    golosinas_pedidas.append([codigo, nombre, 1]) #

   
def validar_tecnico(claves_tecnico):
    print("Ingrese las 3 claves del técnico en orden:")
    intento1 = input("Clave 1: ") #1er elemto de la tupla
    intento2 = input("Clave 2: ") #2do elemento de la tupla
    intento3 = input("Clave 3: ") #3er elemto de la tupla

    if (intento1, intento2, int(intento3)) == claves_tecnico:#si coinciden las 3 aprueba el acceso a recargar golosinas
        return True
    else:
        print("No tiene permiso para ejecutar la función de recarga")
        return False
    
def recargar_golosina(golosinas):
    codigo = int(input("Ingrese el código de la golosina a recargar: "))
    
    for fila in golosinas[1:]:#recorre lista golosinas desde la fila 1
        if fila[0] == codigo:
            cantidad = int(input(f"Ingrese la cantidad a recargar de {fila[1]}: ")) #pide cantidad a recargar mostrando el nombre de golosina
            if cantidad > 0: #verifica que sea mayor a 0
                fila[2] += cantidad #suma al stock la cantidad recargada
                print(f"Se recargaron {cantidad} unidades de {fila[1]}. Stock actual: {fila[2]}")#muestra el estado acual del 
                #stock de la golosina recargada
            else:
                print("Cantidad inválida, debe ser mayor a 0.")
            return  # terminamos la recarga
    print("Código de golosina no encontrado.")

def apagar_maquina(golosinas_pedidas):
    print("\nResumen de golosinas pedidas:")
    
    total = 0
    # Mostramos encabezado
    for fila in golosinas_pedidas:
        print(fila)
    
    # Sumamos cantidades 
    for fila in golosinas_pedidas[1:]:
        total += fila[2]

    print(f"\nTotal de golosinas pedidas: {total}")
    print("Apagando máquina...")
        
main()

