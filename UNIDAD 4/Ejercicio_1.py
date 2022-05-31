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


respuesta = crear_opearicon('+')
#print (respuesta(2,5))

func_orden_superior = lambda funcion_operacion: f'El resultado es {funcion_operacion(10,20)}'
print (func_orden_superior(respuesta))


