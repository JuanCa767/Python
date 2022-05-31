
#Desarrolle una funcion que de una lista selecciones solo los numeros pares usando filtro
#permite filtrar los datos de una lista


lista_numeros =[10,20,12,25,34,30,40,50,60,340,545]

funcion_pares = lambda n: n %2==0
print(list(filter(funcion_pares,lista_numeros)))


#Desarrollar una funcion filter que de una lista seleccione los nombres que empiezan por J
nombres = ['andrés','juan','juliana','cristian','jaime']
#convertirlo en tupla
nombres_x_j = tuple(filter(lambda n:n[0].lower()=='j',nombres))
#convertirlo las inicales J en mayuscula
nombres_x_j = list(map(lambda n: n.capitalize(),nombres_x_j))

print (nombres_x_j)

'''
apartir de lista nombres retorne una lista con las iniciales de los nombres
Ejemplo
nombres = ['andrés','juan','juliana','cristian','jaime']
nombres =['a','j','j','c','j']
'''
#MAP me sirve para convertir los datos 
respuesta=list(map(lambda n :n[0],nombres))
print (respuesta)