def AutoPartes(ventas:list):
    resultado = {} 
    for i in range(len(ventas)):
        resultado[i] = [ventas[i]]
    return(resultado)

# print(AutoPartes(ventas))

def consultarRegistro (ventas, idProducto):
    resultado2 = {}
    resultadoFinal = ''
    for i in ventas:
        if idProducto == ventas[i][0][0]:
            resultado2[i] = ventas[i]

    resultadoFinal=''       
    if len(resultado2) == 0:
        resultadoFinal = 'No hay registro del producto'
    else: 
        for i in resultado2:
            resultadoFinal += f'Producto consultado : {resultado2[i][0][0]} Descripción {resultado2[i][0][1]} #Parte {resultado2[i][0][2]} Cantidad vendida {resultado2[i][0][3]} Stock {resultado2[i][0][4]} Comprador {resultado2[i][0][5]} Documento {resultado2[i][0][6]} Fecha Venta {resultado2[i][0][7]}\n'
    return resultadoFinal

print(consultarRegistro(AutoPartes([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'), 
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010))

