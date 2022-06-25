from xml.sax.xmlreader import InputSource


class Empleado:
    def __init__(empleado) -> None:
        empleado.nombre= input('Digite el nombre y apellidos : ')
        empleado.sueldo = float(input('Digite el sueldo: '))

    
    def imprimir(empleado):
        print('-------------------------------------------')
        print('Nombres y apellidos: ', empleado.nombre )
        print('Sueldo: ', empleado.sueldo)

    def pagar_impuestos(empleado):
        if empleado.sueldo >3000:
            print(f'El empleado {empleado.nombre} debe pagar impuestos' )
        else:
            print(f'El empleado {empleado.nombre} NO debe pagar impuestos')