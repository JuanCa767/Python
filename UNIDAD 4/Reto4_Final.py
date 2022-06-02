from functools import reduce

datos= [ [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],]

def ordenes(rutinaContable):

    nFactura = list(map(lambda lista: [lista[0]] + list(map(lambda j: j[1]*j[2], lista[1:])), rutinaContable))
    nFactura = list(map(lambda lista: [lista[0]]+ [reduce(lambda v1,v2 : round(v1+v2,2), lista[1:])], nFactura))
    vlrMinimo= 600000
    nFactura = list(map(lambda nFactura: nFactura if nFactura[1] >= vlrMinimo else (nFactura[0], nFactura[1] + 25000), nFactura))
    print('------------------------ Inicio Registro diario ---------------------------------')
    for n in range(len(nFactura)):
        print(f'La factura {nFactura[n][0]} tiene un total en pesos de {nFactura[n][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')
   

print(ordenes([ 
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
]))
