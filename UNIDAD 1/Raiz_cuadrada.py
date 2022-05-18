#Cree una funcion que permita hallar la raiz cuadrada

def raizCuadrada():
    print("Programa para calcular la raíz cuadrada de un numero \n")
    valor= float(input("Ingrese un numero para calcular la raiz cuadrada: "))
    raiz = valor **0.5
    return print("La raiz cuadrada de: ", valor, " es ", raiz)

raizCuadrada()

