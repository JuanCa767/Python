
from math import sqrt


def funcion_orden_superior(sumar):
    print(sumar(60,40))

def sumar(n1,n2):
    return n1+n2
#Se crea una variable de referencia
referencia_sumar = sumar
otra_referencia = referencia_sumar
ultima_referencia = otra_referencia
#print(referencia_sumar(40,50))
#funcion_orden_superios(sumar)
#funcion_orden_superior(referencia_sumar)

#-------------------------------------------------------------------------------------

def mapear_datos(funcion, lista_numeros: list)->list:
    respuesta = []
    for num in lista_numeros:
        x = funcion(num)
        respuesta.append(x)
    return respuesta

#Fabrica de funciones sobre un mismo número
#Retorna una función que recibe un solo parámetro de tipo numérico
def fabricar_operacion(operador):
    respuesta = lambda n: f'No existe la operación para n con operación {operador}'
    #Evaluar el operador
    if operador == '**2':
        respuesta = lambda n: n**2
    elif operador == 'sqrt':
        #Raíz cuadrada
        respuesta = lambda n: sqrt(n)
    elif operador == '/2':
        respuesta = lambda n: n/2
    return respuesta

numeros = [4,20,30,40,50,60,70,80]
operacion = fabricar_operacion('/2')
respuesta = mapear_datos(operacion, numeros) 
print(respuesta)
