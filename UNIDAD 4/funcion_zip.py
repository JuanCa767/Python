from functools import reduce

#a partir de dos iterables, me devuelve una lista de tuplas
#ejemplo de zip
nombres = ['Raul','Pedro','Sofia']
apellidos =['Lopez','Perez','Gonzalez']

nombre_apellido =list( zip(nombres,apellidos))
#print(nombre_apellido)


#ejemplo2
#listas
lista_1=[10,20,30,40,50,60,70,80,90]
lista_2=[90,80,70,60,50,40,30,20,10]
#enviarlos a una lista de tuplas
lista_tupla= list( zip(lista_1,lista_2))
#print(lista_tupla)

sumar  = list(map(lambda tupla : tupla[0]+tupla[1], lista_tupla))
respuesta = reduce(lambda ac,e : ac+e,sumar)
print(respuesta)
