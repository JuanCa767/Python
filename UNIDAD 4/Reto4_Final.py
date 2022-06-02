from functools import reduce

datos= [ [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],]

def ordenes(rutinaContable):

    nFactura = list(map(lambda lista: [lista[0]] + list(map(lambda j: j[1]*j[2], lista[1:])), rutinaContable))
    nFactura = list(map(lambda lista: [lista[0]]+ [reduce(lambda v1,v2 : round(v1+v2,2), lista[1:])], nFactura))
    vlrMinimo= 600000
    nFactura = list(map(lambda nFactura: nFactura if nFactura[1] >= vlrMinimo else (nFactura[0], nFactura[1] + 25000), nFactura))
    print('---------------------- Inicio registro diario -----------------------------------------')
    for n in range(len(nFactura)):
        print(f'La Factura {nFactura[n][0]} tiene un total en pesos de {nFactura[n][1]}')
    print('------------------------ Fin registro diario -----------------------------------------')
   

print(ordenes(datos))
