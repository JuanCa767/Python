datos = [
    (2001, 'rosca', 'PT29872', 'Luis Molero', '12/06/2020'),
    (2012, 'piñón', 'EN5698', 'Carlos Rendón',  '12/06/2020'),
    (2010, 'bujía', 'MS9512', 'Pedro Montes', '12/06/2020'),
    (2001, 'bujía', 'JHT222', 'Pedro Faria', '12/06/2020'),
    (2012, 'tijera', 'QW8523', 'Jorge Hernandez', '12/06/2020'),
    (2010, 'bujía', 'ER6523', 'Samir Delgado', '12/06/2020'),
    ]

'''
Agrupar los vehiculos por el año.
respuesta = {
    2010: {
        'PT29872':{
            'repuesto': 'rosca',
            'fecha_ingreso': '12/06/2020',
            'propietario': 'Luis Molero'
        },
        'EN5698':{
            'repuesto': 'piñón',
            'fecha_ingreso': '12/06/2020',
            'propietario': 'Carlos Rendón'
        }
    }
}


def agruparPormodelo(lista_carros: list)->dict:
    dic={}
    for i in range(len(lista_carros)):
        dic[i] ={
            'modelo':lista_carros[i][0],
            'repuesto':lista_carros[i][1],
            'fecha ingreso': lista_carros[i][4],
            'placa': lista_carros[i][2],
            'Nombre':lista_carros[i][3]
        }

    return dic

print(agruparPormodelo(lista_carros))
'''
#(2001, 'rosca', 'PT29872', 'Luis Molero', '12/06/2020')

def agruparPorModelo(lista_carros:list):
    #crear diccionario vacio
    dic_carros = dict()
    #iterar los carros
    for carro in lista_carros:
        anio, repuesto, placa, propietario, fecha = carro
        carro = {
            placa : {
                'repuesto': repuesto,
                'fecha_ingreso': fecha,
                'propietario': propietario
            }
        }
        if anio in dic_carros:
            for placa, info in dic_carros[anio].items():
                carro[placa] = info
        dic_carros[anio] = carro
    
    return dic_carros


print(agruparPorModelo(datos))
