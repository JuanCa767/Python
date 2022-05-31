#conjunto vacio
conjunto_vacio = set()
#conjutno lleno, sintaxis
conjunto_de_elementos = {10,20,30,40,50,60}
#print(conjunto_de_elementos)

#ejemplos
conjunto_a = {10,20,30,40,50,60}
conjunto_b = {5,10,15,20,25,35,40,60,65}

#imprimimos los conjuntos
print('Conjunto A:\n',conjunto_a)
print('Conjunto B:\n',conjunto_b)

print('---------INTERSECCIÓN------')
interseccion = conjunto_a.intersection(conjunto_b)
print(interseccion)
print('Estado del conjunto A:\n', conjunto_a)

print('------INTERSECTION UPDATE-------')
conjunto_a.intersection_update(conjunto_b)
print('Estado del conjunto A:\n', conjunto_a)

print('---------DIFFERENCE------')
difference = conjunto_a - conjunto_b#conjunto_a.difference(conjunto_b)
print('Diferencia:\n',difference)
print('Estado de Conjunto A:\n', conjunto_a)

print('---------LOS CONJUNTOS NO TIENEN DUPLICIDAD DE DATOS-------')
nombres = {'Juan', 'Pedro', 'Eliana', 'Pedro', 'Juan', 'Eliana', 'Andrea'}
print("Inicializando un conjunto: \n{'Juan', 'Pedro', 'Eliana', 'Pedro', 'Juan', 'Eliana', 'Andrea'}")
print('Estado del conjunto nombres:\n', nombres)


'''
Conjunto de cadenas de caracteres
-----------------------------------------------
Conversión de contenedores
Ordenar los elementos de un conjunto dentro de una lista
'''
print('\n--------------- CONJUNTO DE CARACTERES CON CONJUNTOS -----------------------')
mensaje = 'Hola mundo, somos el grupo 42 de mision tic UTP'
conjunto_mensaje = set(mensaje)
print(mensaje)
print(conjunto_mensaje)

lista_numeros = [10, 20,30,40,50,60,10,10,10,20,20,50]
conjunto_numeros=set(lista_numeros)
print(conjunto_numeros)

print('-------- CONJUNTO DE LISTAS-----------------')
conjunto = {30,40,50,60,10,20}
print(conjunto)

lista = list(conjunto)
lista.sort()
print(lista)

print('-------OBTENER ELEMENTOS EN COMÚN ENTRE DOS LISTAS-------')
lista_placas_1 = ['ABC222', 'QRT442', 'QSF543', 'QRS123']
lista_placas_2 = ['DBC222', 'QRT442', 'RSF543', 'QRS123']
print('Lista placas 1:\n', lista_placas_1)
print('Lista placas 2:\n', lista_placas_2)

conjunto_placas_1 = set(lista_placas_1)
conjunto_placas_2 = set(lista_placas_2)
placas_en_comun = conjunto_placas_1.intersection(conjunto_placas_2)
print(placas_en_comun)
lista_placas_en_comun = tuple(placas_en_comun)
print(lista_placas_en_comun)


