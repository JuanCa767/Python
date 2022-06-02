from functools import reduce

datos= [
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]]


def ordenes(rutinaContable):
    
    nFactura = list(map(lambda lista: [lista[0]] + list(map(lambda n: n[1]*n[2], lista[1:])), rutinaContable))
    nFactura = list(map(lambda lista: [lista[0]]+ [reduce(lambda v1,v2: round(v1+v2,2), lista[1:])], nFactura))
    vlrMinimo= 600000
    nFactura = list(map(lambda lista: nFactura if lista[1] >= vlrMinimo else (lista[0], lista[1] + 25000), nFactura))
    print('---------------------- Inicio registro diario -----------------------------------------')
    for n in range(len(nFactura)):
        print(f'La Factura {nFactura[n][0]} tiene un total en pesos de {nFactura[n][1]}')
    print('------------------------ Fin registro diario -----------------------------------------')



print(ordenes(datos))