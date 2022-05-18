#----------Funciones que retornan un tipo de dato-----------


def sumar(num1, num2):
    resultado=num1 + num2
    return resultado 
 
resp = sumar(10,5)
print (resp)
print (sumar(2,12))

'''
        USAMOS EL TIPADO DINAMICO:

Que es le tipado Dinamico?
Es una funcion que tiene Python que le permite asignar otro valor a una variable 
dentro del codigo a medida que va avanzando dentro del codigo.
Ejemplo: Tenemos la funcion sumar del ejemplo anterior
con la variable sumatoria asinamos al funcion sumar con otros valores utiliando la funcion sumar y otros datos.
que quedan almacenados en esa variable.
Y creamos otra variable sumatoria2 a la que le asignamos el valor de val varialbe sumatoria  + otro valor y quedan 
asignados en la variable sumatoria2
'''

sumatoria = sumar(20,50)
sumatoria2 = sumatoria +10

#otra funcion
def saludar(nombre_usuario):
    return "Hola "+nombre_usuario+", nos alegra que nos visites"

print(saludar('Juan'))