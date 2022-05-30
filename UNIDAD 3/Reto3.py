

'''ventas = [(2001, 'rosca', 'PT29872',2,45,'Luis Moreno',3456,'12/06/2020'),
(2010,'bujia','MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujia','ER6523',9,36,'Pedro Montes',1234,'12/06/2020'),
(3578,'tijera','QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón','EN5698',2,8,'Juan Peña',565,'12/06/2020')]'''



def AutoPartes(ventas:list):
    resultado={}
    for x in range(len(ventas)):
        resultado[x]=[ventas[x]]
    
    return resultado

def consultaRegistro(ventas,idProducto):
    resultado1={}
    for i in ventas:
        if idProducto==ventas[i][0][0]:
            resultado1[i]=ventas[i]

        resultado2=''
        if len(resultado1)==0:
            resultado2='No hay registro de ventas de este producto '
        else:
            for i in resultado1:
                resultado2+='Producto consultado: {} Descripción {} #Parte {} Cantidad vendida {}\n Stock {} Comprador {} Documento {} Fecha Venta {}\n\n'.format(ventas[i][0][0],ventas[i][0][1],ventas[i][0][2],ventas[i][0][3], ventas[i][0][4], ventas[i][0][5],ventas[i][0][6],ventas[i][0][7])
    print(resultado2)

consultaRegistro(AutoPartes([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'), 
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)


#print (AutoPartes(ventas))































 
'''
  
def consultaRegistro(ventas,idProducto):
    newDic = {}#crear un nuevo diccionario
    respuesta=''
    for i in range(len(ventas)) :
        if ventas[i][0][0] == 'IdProducto': ventas[i][0]
            newDic[i] = {
                'Producto consultado': ventas[i][0],
                'Descripcion': ventas[i][1],
                '# Parte': ventas[][],
            }
          
    if len(newDic) == 0:
        respuesta = #Enviar la respuesta cuando no encuentra el producto
    
    for valoresDic in newDic.values(): 
        for idProducto,dProducto...#escribir cada variable como indica el reto# in #iterablevaloresDic:
            respuesta += (f'Devolver respuesta exactamente como aparece en el reto\n')             
            
   print(respuesta)
   


productos =(
    
)
'''