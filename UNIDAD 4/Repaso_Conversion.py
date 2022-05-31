
#CONVERSION DE CADENAS
#de cadena en lista
from ntpath import join


cadena = "hola"
lista = list(cadena)
#print(lista)
#de de cadenas a tuplas
cad = "Hola"
cad1= 'adios'
num = 15
tupla1= tuple(cad)
#print(tupla1)
tupGeneral = (tupla1,num,tuple(cad1))
#print(tupGeneral)
#de de cadena a conjunto
saludo= "hhola"
conjunto = set(saludo)
#print(conjunto)


#CONVERSION DE LISTAS
#de listas a cadenas
lista = ['h','o','l','a']
#print(lista)
cadena =''.join(lista)
#print(cadena)
#De lista a tupla
lista1=['h','o','l','a',1,2,3,4,5,65]
#print(lista1)
tupla = tuple(lista1)
#print(tupla)
#De Listas a conjuntos
lista2=['h','o','l','a',1,2,3,4,5,65]
conjunto = set(lista2)
#print(conjunto)

#CONVERSION DE TUPLAS
#De tuplas a  lista
tupla=('hola','mundo',123,123,123)
listaT=list(tupla)
#print (listaT) 
#De tuplas a conjuntos
tupla2=('hola','mundo',123,123,123)
conjunto1=set(tupla2)
#print (conjunto1)

#CONVERSION DE CONJUNTOS
# de conjunto a dacena 
Conj1={'h','o','l','a'}
cadena2=''.join(Conj1)
#print (cadena2)
# De conjunto a tupla
Conj2={'h','o','l','a',12}
tupla3= tuple(Conj2)
#print(cad)
#De conjunto a lista
Conj1={'h','o','l','a'}
lista = list(Conj1)
#print(lista)

#CONVERSION a DICCIONARIOS
#de cadena 
cadena = 'Hola'
diccionario = dict(zip(range(len(cadena)),cadena))
#print(diccionario)
#de lista
lista=['h','o','l','a']
diccionario= dict(zip(range(len(lista)),lista))
#print(diccionario)
#de tupla
tupla=('h','o','l','a')
diccionario=dict(zip(range(len(tupla)),tupla))
#print(diccionario)
#de conjuntos
conjunto3={'h','o','l','a'}
diccionario=dict(zip(range(len(conjunto3)),conjunto3))
#print(diccionario)

#CONVERSION De DICCIONARIOS
#diccionario a cadena
diccionario={0:'h',1:'o',2:'l',3:'a'}
cadenaValores= "" .join(diccionario.values())
print(cadenaValores)
#---------------------------------------------------
# a tuplas
tuplaLlaves=tuple(diccionario.keys())
tuplaValores=tuple(diccionario.values())
tuplaItems=tuple(diccionario.items())
print(tuplaLlaves)
print(tuplaValores)
print(tuplaItems)
#a listas
#---------------------------------------------------
listaLlaves=tuple(diccionario.keys())
listaValores=tuple(diccionario.values())
listaItems=tuple(diccionario.items())
print(listaLlaves)
print(listaValores)
print(listaItems)
#a Conjuntos
#-----------------------------------------------------------
conjuntoLlaves=tuple(diccionario.keys())
conjuntoValores=tuple(diccionario.values())
conjuntoItems=tuple(diccionario.items())
print(conjuntoLlaves)
print(conjuntoValores)
print(conjuntoItems)
