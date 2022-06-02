from functools import reduce

lista= [
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]]
 


def ordenes(rutinaContable): 
    nombreLista=[]
    #nombreTupla=[]
    newFactura = list(map(lambda rutinaContable: [nombreLista[0]] + list(map(lambda tupla: nombreLista[1]*nombreLista[2], nombreLista[1:])), rutinaContable))
    newFactura = list(map(lambda rutinaContable: [nombreLista[0]] + [reduce(lambda v1,v2: round(v1 + v2,2), nombreLista[1:])], newFactura))
    minimaCompra = 600000
    newFactura = list(map(lambda newFactura: nombreLista if lista[1] >= minimaCompra else (nombreLista[0], nombreLista[1] + 25000), newFactura))
    print('------------------------ Inicio Registro diario ---------------------------------')
    #Ciclo para imprimir el total de cada compra
    nombreFactura =''
    for lista in range(len(nombreFactura)):
        print(f'La factura {nombreFactura[lista][0]} tiene un total en pesos de {nombreFactura[lista][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')


print(ordenes())