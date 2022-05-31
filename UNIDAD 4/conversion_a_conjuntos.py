'''
-----------------------------------------------
Conversión de contenedores:
    Conjunto de cadenas de caracteres ✔️
    Ordenar los elementos de un conjunto dentro de una lista ✔️
'''
#conversion de cadena a conjunto
mensaje = 'Hola mundo, somos el grupo 42 de MISION TIC - UTP 2022'
conjunto_mensaje = set(mensaje)
print(conjunto_mensaje)
#------------------------------------------------------------------------
#Conversion de lsita a conjunto
lista_numeros = [10,20,30,40,50,60,10,10,10,20,20,50]
conjunto_numeros = set(lista_numeros)
print(conjunto_numeros)
#--------------------------------------------------------------------------
print('--------DE CONJUNTOS A LISTAS------')
conjunto = {30,40,50,60,10,20}
print(conjunto)
lista = list(conjunto)
#-----------------------------------------------------
#Ordenar los elementos
lista.sort()#permite ordenar la lista
print(lista)
#-------------------------------------------------------
print('-------OBTENER ELEMENTOS EN COMÚN ENTRE DOS LISTAS-------')
lista_placas_1 = ['ABC222', 'QRT442', 'QSF543', 'QRS123']
lista_placas_2 = ['DBC222', 'QRT442', 'RSF543', 'QRS123']
#print('Lista placas 1:\n', lista_placas_1)
#print('Lista placas 2:\n', lista_placas_2)
conjunto_placas_1 = set(lista_placas_1)
conjunto_placas_2 = set(lista_placas_2)
#Interseccion que permite tener el comun entre las listas
placas_en_comun = conjunto_placas_1.intersection(conjunto_placas_2)
print(placas_en_comun)
#convertir a tupla
lista_placas_en_comun = tuple(placas_en_comun)
print(lista_placas_en_comun)
#----------------------------------------------------------------------
#convertir cadena de caracteres a conjuntos
print('-------CADENA DE CARACTERES A CONJUNTOS-------')
mensaje = 'Hola mundo desde Misión Tic - UTP 2022'
conjunto = set(mensaje)
print(conjunto)
#---------------------------------------------------------------------
#convertir cadena de caracteres a conjuntos
print('-------DICCIONARIOS A CONJUNTOS-------')
dict_persona = {
    'nombre': 'María',
    'apellido': 'Quintana',
    'edad': 25,
    'telefono': '123456789'
}
conjunto_persona = set(dict_persona.keys()) #conjunto de llaves del diccionario
print(conjunto_persona)
conjunto_persona = set(dict_persona.values())#conjunto de valores del diccionario
print(conjunto_persona)

