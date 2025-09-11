#Ejercico 1
valorDecimal =  float(input("Ingrese un numero decimal: "))
casteoaString = str(valorDecimal)
casteoaEntero = int(valorDecimal)
casteoaBooleano = bool(valorDecimal)
casteoaComplejo = complex(valorDecimal) 

#De decimal a entero se elimina la parte decimal sin redondear ejemplo (12.99 quedaria 12 entero).
print(f"El resultado de castear el numero decimal a entero es: {casteoaEntero}")

"""El resultado de castear un entero a decimal(float) en este caso de se le agrega un 0 
pero notese que se pierde informacion con respecto al decimal original que fue convertiro a entero."""

#Puedo castearlo sin crear variables tambien.

print(f"El resultado de castear un entero a decimal {(float(casteoaEntero))}")

#El numero decimal se transforma en una cadena de texto.

print(f"El resultado de castear el numero decimal a cadena de texto es: {casteoaString}")


"""Al ser un numero decimal el que ingresa el usuario  cuando el decimal
se transforma en booleano el resultado sera true. En el caso de que sea false
0, none, una cadena vacia " " se consideraria false."""

print(f"El resultado de castear el numero decimal a booleano es: {casteoaBooleano}")

#El numero decimal a numero complejo(complex) 

print(f"El resultado de castear un decimal a complejo es: {casteoaComplejo}")

print("")

#Ejercicio 4

totalFinal = float(input("Introduzca el total a pagar: "))

billetesde200 = billetesde100 = billetesde50 = billetesde20 = billetesde10 = billetesde5 = billetesde2 = billetesde1 = 0
monedas50centavos = monedas25centavos = monedas10centavos = monedas5centavos = 0

billetes = [200, 100, 50, 20, 10, 5, 2, 1]
monedas  = [0.50, 0.25, 0.10, 0.05]


while(totalFinal >= billetes[0]):
    totalFinal -= billetes[0]
    billetesde200 +=1

while(totalFinal >= billetes[1]):
    totalFinal -= billetes[1]
    billetesde100 +=1

while(totalFinal >= billetes[2]):
    totalFinal -= billetes[2]
    billetesde50 +=1

while(totalFinal >= billetes[3]):
    totalFinal -= billetes[3]
    billetesde20 +=1

while(totalFinal >= billetes[4]):
    totalFinal -= billetes[4]
    billetesde10 +=1

while(totalFinal >= billetes[5]):
    totalFinal -= billetes[5]
    billetesde5 +=1
while(totalFinal >= billetes[6]):
    totalFinal -= billetes[6]
    billetesde2 +=1

while(totalFinal >= billetes[7]):
    totalFinal -= billetes[7]
    billetesde1 +=1

while(totalFinal >= monedas[0]):
    totalFinal -= monedas[0]
    monedas50centavos +=1

while(totalFinal >= monedas[1]):
    totalFinal -= monedas[1]
    monedas25centavos +=1

while(totalFinal >= monedas[2]):
    totalFinal -= monedas[2]
    monedas10centavos +=1

while(totalFinal >= monedas[3]):
    totalFinal -= monedas[3]
    monedas5centavos +=1

print("Billetes necesarios:")
if billetesde200 > 0:
    print(f"200: {billetesde200}")
if billetesde100 > 0:
    print(f"100: {billetesde100}")
if billetesde50 > 0:
    print(f"50: {billetesde50}")
if billetesde20 > 0:
    print(f"20: {billetesde20}")
if billetesde10 > 0:
    print(f"10: {billetesde10}")
if billetesde5 > 0:
    print(f"5: {billetesde5}")
if billetesde2 > 0:
    print(f"2: {billetesde2}")
if billetesde1 > 0:
    print(f"1: {billetesde1}")

print("Monedas necesarias:")
if monedas50centavos > 0:
    print(f"0.50: {monedas50centavos}")
if monedas25centavos > 0:
    print(f"0.25: {monedas25centavos}")
if monedas10centavos > 0:
    print(f"0.10: {monedas10centavos}")
if monedas5centavos > 0:
    print(f"0.05: {monedas5centavos}")

print("")

#Ejercicio 14
"""En Java existen los tipos valor (los primitivos como int, float, char) y
los tipos referencia (objetos, arreglos, String, etc.). Los de valor guardan directamente el dato, 
mientras que los de referencia guardan una dirección al objeto en memoria.

En Python todo es un objeto. Aun así, los inmutables (int, float, str, tuple) 
se comportan parecido a los de valor porque no se pueden cambiar, y los mutables (list, dict, set, clases) 
funcionan como referencia porque varias variables pueden apuntar al mismo objeto."""

#Ejercicio 19
class OperacionMatematica:

    #Constructor para inicializar los atributos.
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = None 

    #Si queremos usar las variables del constructor tenemos que pasarle como parametro self a los metodos.
    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: división por cero"
        
    #Este metodo tiene 2 parametros porque operacion necesita saber que operacion realizar.
    def aplicarOperacion(self, operacion):
        self.operacion = operacion
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multiplicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"

class Calculo:

    #En python no existe el metodo main como en java pero lo podemos simular.
    #Lo declaramos estatico porque no necesitamos a self
    
    #@staticmethod indica que el método pertenece a la clase, no a una instancia.
    #Eso significa que podés llamarlo sin crear un objeto de la clase

    @staticmethod

    def main():

        valor1 = float(input("Ingrese el primer número: "))
        valor2 = float(input("Ingrese el segundo número: "))

        #Creamos la instancia con las variables locales que le pedimos al usuario

        op = OperacionMatematica(valor1, valor2)

        print("")

        #Utilizamos el objeto para invocar a los metodos correspondientes y efecturas dichas operaciones.
        print("Suma:", op.aplicarOperacion("+"))
        print("Resta:", op.aplicarOperacion("-"))
        print("Multiplicación:", op.aplicarOperacion("*"))
        print("División:", op.aplicarOperacion("/"))

#Usamos esto para definir el punto de entrada del programa (la clase principal) y de paso invocamos a la clase calculo.
if __name__ == "__main__":
    Calculo.main()
