
def simulacion_map(funcion, lista):
    respuesta = []
    for i in lista:
        num = funcion(i)
        respuesta.append(num)
        
    return respuesta

elevar = lambda n: n**2
#elevar al cuadrado todos los numeros de la lista
lista_numeros_1=[10,20,30,40,50,60,70,80]
lista_numeros_2=[20,5,15,40,50,60,70,80]
lista_principal=[lista_numeros_1, lista_numeros_2]

#print(simulacion_map(elevar, lista_numeros_1))
for lista in lista_principal:
    print(simulacion_map(elevar,lista))

