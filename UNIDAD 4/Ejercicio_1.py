#esta es una fabrica de funciones

def crear_opearicon(operacion:str):
    funcion = ''
    if operacion == '+':
        funcion = lambda n1,n2 : n1+n2
    elif operacion == '-':
        funcion = lambda n1,n2 : n1-n2
    elif operacion == '*':
        funcion = lambda n1,n2 : n1*n2
    elif operacion == '/':
        funcion = lambda n1,n2 : n1/n2
    elif operacion == '**':
        funcion = lambda n1,n2 : n1**n2
    else:
        funcion = lambda n1,n2 : ' Ingrese una funcion valida'
    return funcion

'''
#esta funcion es lo mismo que representa el lambda que esta abajo como funcion de orden superior
def orden_superior(funcion):
    resultado= funcion(10,20)
    return f'El resultado es:  {resultado}'''



respuesta = crear_opearicon('+')
#print (respuesta(2,5))
#print(orden_superior(respuesta))

#con esto creamos una funcion de orden superior, con una funcion anonima
#Que referencia a la funcion principal que es la fabrica de funciones.
#esto es equivalente a la funcion que esta en la linea 20
func_orden_superior = lambda funcion_operacion: f'El resultado es {funcion_operacion(10,20)}'
print (func_orden_superior(respuesta))


