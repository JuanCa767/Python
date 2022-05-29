'''
2) Desarrolle una función que reciba como parámetro una lista de string,
    retorne una lista de tuplas donde cada tupla representa a cada string
    de la lista inicial.
nombres = ['Andrés', 'María']
retornar:
    [ ('A', 'n', 'd', 'r', 'e', 's'), (...) ]
'''
ejercicio_2 = "2) Desarrolle una función que reciba como parámetro una lista de string,\n"
ejercicio_2 += "retorne una lista de tuplas donde cada tupla representa a cada string\n"
ejercicio_2 += "de la lista inicial.\n"
ejercicio_2 += "nombres = ['Andrés', 'María']\n"
ejercicio_2 += "retornar: [ ('A', 'n', 'd', 'r', 'e', 's'), (...) ]\n"
print(ejercicio_2)



nombres = ['Andrés', 'María']
n1 = nombres[0]
""" print(n1)
tupla_n1 = tuple(n1)
print(tupla_n1)
lista_tupla = [tupla_n1]
print(lista_tupla)

n2 = nombres[1]
n2 = tuple(n2)
lista_tupla.append(n2)
print(lista_tupla) """

def iterar_lista(convertir, lista: list):
    respuesta = []
    for n in lista:
        tupla = convertir(n)
        respuesta.append(tupla)
    return respuesta

convertir_a_tupla = lambda cadena: tuple(cadena)
respuesta = iterar_lista(convertir_a_tupla, nombres)
print(respuesta)

