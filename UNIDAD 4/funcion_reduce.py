#
from functools import reduce

lista_numeros=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]

numeros = [1,2,3,4]


funcion_sumar = lambda acumulador, elemento: acumulador + elemento

suma_num= reduce(funcion_sumar, numeros)
print(suma_num)

def sumar(lista:list):
    acumulador = 0
    for n in lista:
        acumulador +=n

#------------------------------------------------------------------------
#desarrolle una funcion donde presente la lista de nombres separados por coma

nombres = ['andrés','juan','juliana','cristian','jaime']
#explicacion
concatenar = lambda ac, e: ac+', '+e
respuesta1=reduce(concatenar, nombres)
print(respuesta1)
#desarrollado por mi
respuesta= reduce(lambda ac, e: ac + ", " + e, nombres)
print(respuesta)


#--------------------------------------------------------------------------------------------
'''
A partir de la lista de nombres imprima todos los nombres 
que empiezan por 'J' separados por coma. 
NOTA: Para el resultados final los nombres deben empezar en mayúscula
'''
nombres= ['andrés','juan','juliana','cristian','jaime']

nombres = list(filter(lambda n:n[0].lower()=='j',nombres))
nombres =list(map(lambda n: n.capitalize(),nombres))
concatenar = lambda ac, e: ac+', '+e
respuesta= reduce(lambda ac, e: ac + ", " + e, nombres)

#print(nueva_lista)
print(respuesta)


'''
A partir de la lista de nombres imprima todos los nombres 
que empiezan por 'J' separados por coma. 
NOTA: Para el resultados final los nombres deben empezar en mayúscula
Algoritmo:
1) Filtrar la lista
2) Convertir iniciales a mayúsculas
3) Reducir la lista a String

nombres = ['andrés','Juan','juliana','cristian','jaime']

nombres =list(filter(lambda n: n[0].lower()=="j", nombres))
nombres = list(map(lambda n: n.capitalize(), nombres))
concatenar = lambda ac, e: ac+", " + e
respuesta = reduce(concatenar,nombres)
#print(respuesta)
'''



