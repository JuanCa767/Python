#Pyton puede trabajar con funciones dentro de otra funcion

def imprime_cosas():
    print("Hola Mundo ")
    print("Entendiendo funciones ")

imprime_cosas()

def repetir_funciones():
    imprime_cosas()
    imprime_cosas()

repetir_funciones()

#Ejemplo
#Vamos a crear una funcion que permita ingresar dos numeros y sumarlos

def mensaje():
    print("Ingrese por favor un valor")
    
def sumaDosNumeros():
    mensaje()
    num1= float(input())
    mensaje()
    num2= float(input())
    mensaje()
    return print("La suma de: ", num1, " + ", num2, " es igual a: ", num1+num2)

sumaDosNumeros()