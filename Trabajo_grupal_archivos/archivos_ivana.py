def main():
    notas = [
        "Juan;Pérez;53365;8\n",
        "María;López;55654;10\n",
        "Pablo;Gómez;58999;6\n"
    ]
    with open("alumnos.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(notas)
    leer_mostrar(notas)
    #Creando diccionario alumnos
    alumnos = {}              # crear diccionario vacío
    print("Mostrando el diccionario: ")
    leer_mostrar(alumnos)      # PASARLO para que la función lo llene

    # ahora alumnos ya está cargado; podés imprimirlo
    for legajo, datos in alumnos.items():
        
        print(f"Legajo: {legajo} | Nombre: {datos['nombre']} | Nota: {datos['nota']}")
    



def leer_mostrar(alumnos):
    with open("alumnos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(";")
            nombre, apellido, legajo, nota_promedio = partes
            print(f"Nombre: {nombre} | Apellido: {apellido} | Legajo: {legajo} | Nota promedio: {nota_promedio}")

   
main()