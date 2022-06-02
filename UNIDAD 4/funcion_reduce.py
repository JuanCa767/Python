#
from functools import reduce
#lista
numeros = [1,2,3,4]

funcion_sumar = lambda acumulador, elemento: acumulador + elemento

suma_num= reduce(funcion_sumar, numeros)
#print(suma_num)

def sumar(lista:list):
    acumulador = 0
    for n in lista:
        acumulador +=n

#------------------------------------------------------------------------
#Desarrolle una funcion donde presente la lista de nombres separados por coma

nombres = ['andrés','juan','juliana','cristian','jaime']
#explicacion
concatenar = lambda ac, e: ac+', '+e
respuesta1=reduce(concatenar, nombres)
#print(respuesta1)
#desarrollado por mi
respuesta= reduce(lambda ac, e: ac + ", " + e, nombres)
#print(respuesta)


#--------------------------------------------------------------------------------------------
'''
A partir de la lista de nombres imprima todos los nombres 
que empiezan por 'J' separados por coma. 
NOTA: Para el resultados final los nombres deben empezar en mayúscula
'''
nombres= ['andrés','juan','juliana','cristian','jaime', 'manuel', 'patricia']

nombres = list(filter(lambda n:n[0].lower()=='a',nombres))
nombres =list(map(lambda n: n.capitalize(),nombres))
concatenar = lambda ac, e: ac+', '+e
respuesta= reduce(lambda ac, e: ac + ", " + e, nombres)

#print(nueva_lista)
print(respuesta)



