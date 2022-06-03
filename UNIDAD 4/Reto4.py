from functools import reduce

datos = [ 
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
]

#primera manera de hacerlo
def ordenes(rutinaContable):
    print('---------------------- Inicio Registro diario ------------------------')
    for lista in rutinaContable:
        total = 0.0
        for elemento in lista:
            if type(elemento) ==  tuple:
                total = total + elemento[1]* elemento[2]
        if total <=600000:
            total = total + 25000
        print(f'La factura {lista[0]} tiene un total en pesos de {round(total,2):,.2f}')
    print('---------------------- Fin Registro diario ----------------------------')

#ordenes(datos)


#segunda forma de hacerlo
def ordenes(rutinaContable):
    print('---------------------- Inicio Registro diario ------------------------')
    for lista in rutinaContable:
        tuplas = list(filter(lambda x: type(x)==tuple, lista))
        valores = list(map(lambda x: x[1]*x[2], tuplas))
        total = reduce(lambda x,y: x+y, valores)
        if total <600000:
            total = total + 25000
        print(f'La factura {lista[0]} tiene un total en pesos de {total:.2f}')
    print('---------------------- Fin Registro diario ----------------------------')

ordenes(datos)