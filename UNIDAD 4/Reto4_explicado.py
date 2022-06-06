from functools import reduce

datos = [ 
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
]

def ordenes(rutinaContable):
    nF = list(map(lambda lista: [lista[0]] + list(map(lambda tupla:tupla[1]*tupla[2],lista[1:] )),rutinaContable))
    nF= list(map(lambda lista: [lista[0]] + [reduce(lambda ac, el: round(ac+el,2), lista[1:])], nF))
    VlMinimo = 600000
    nF= list(map(lambda lista: lista if lista[1]>= 600000 else [lista[0],lista[1]+25000],nF))
    print('------------------------ Inicio Registro diario ---------------------------------')
    for n in range(len(nF)):
        print(f'La factura {nF[n][0]} tiene un total en pesos de {nF[n][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')

ordenes(datos)