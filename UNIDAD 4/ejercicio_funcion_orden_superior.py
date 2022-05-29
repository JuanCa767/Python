
from math import sqrt


'''
1) Desarrolle un función que retorne una lista con las iniciales de 
    cada string a partir de una lista de strings. 
    Para esto utilice el concepto de funciones de orden superior y
    funciones anónimas
'''

nombres = ['Juliana', 'Pedro', 'María', 'Juan Carlos', 'Andrés', 'Alejandra']
'''
['J, 'P',...]
'''

def lista_nombre(obtener_inicial, nombres)->list:
    respuesta = []
    for n in nombres:
        x = obtener_inicial(n)
        respuesta.append(x)
    return respuesta

#obtener la inicial
def obtener_inicial(cadena):
    return cadena[0]

lista_iniciales = lista_nombre(obtener_inicial,nombres)
print(lista_iniciales)



