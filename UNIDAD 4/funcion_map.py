#Obtener el cuadrado de todos los elemmeentos de la lista

def cuadrado(elemento = 0):
    return elemento*elemento

lista=[1,2,3,4,5,6,7,8,9,10]
resultado = list(map(cuadrado,lista))

print(resultado)


#-----------------------casteando
respuesta = list(map(lambda n : n**2, lista))
print(respuesta)

#convertirlos a string
print(list(map(lambda n : f'{n}',lista)))


'''
Retornar una lista con la inicial de cada nombre en mayúscula
'''
nombres = ['andrés','juan','juliana','cristian','jaime']

respuesta=list(map(lambda n :n[0],nombres))
#respuesta = list(map(lambda n: n.capitalize(), nombres))
print(respuesta)
