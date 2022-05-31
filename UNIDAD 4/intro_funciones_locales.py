#funciuones locales, son funciones dentro de otra funcion
#que se crean para utiliar un mismo proceso dentro de un codigo.
#Se emplea cuando se utilizan funciones muy complejas y tiene mucha dofificacion.
#se crea una funcion pequeña qu puede ser llamada dentro del funcion padre.
from unittest import result


def calcular_promedios(lista: list):

    def suma(lista):
        acumulador = 0
        for n in lista:
            acumulador += n
        return acumulador
    #print('Suma-> ', suma(lista))
    promedio = suma(lista)/len(lista)
    return promedio

#print( calcular_promedios([10,20,30,40,50]) )

#-----------------------------------------------------------------------------------

#def sumar_numeros():
    #def sumar(n1,n2):
        #return n1+n2

    #print(sumar(10,20))

#sumar_numeros()


#---------------------------------------------------------------------
#ejemplo 1
def suma(n1=0, n2=0):
    return n1 + n2

def operacion(funcion, n1=0, n2=0):
    return funcion(n1,n2)

funcion_suma = suma
resultado = operacion(funcion_suma, 10,30)
#print(resultado)

#FUNCIONES ANONIMAS O LAMBDA
#----------------------------------FUNCION LAMBDA----------------------------------------------------

def sumar_numeros():
    sumar =lambda n1,n2 :n1+n2  

    #print(sumar(20,30))

#sumar_numeros()

