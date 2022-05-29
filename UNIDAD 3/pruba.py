
ventas = [(2001, 'rosca', 'PT29872',2,45,'Luis Moreno',3456,'12/06/2020'),
(2010,'bujia','MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujia','ER6523',9,36,'Pedro Montes',1234,'12/06/2020'),
(3578,'tijera','QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón','EN5698',2,8,'Juan Peña',565,'12/06/2020')]


def AutoPartes(ventas:list):
    dic = {}
    for i in range(len(ventas)):
        dic[i] = {
            'IdProducto': ventas[i][0],
            'dProducto' : ventas[i][1],
            'pnProducto': ventas[i][2],
            'cvProducto': ventas[i][3],
            'sProducto' : ventas[i][4],
            'nComprador': ventas[i][5],
            'cComprador': ventas[i][6],
            'fVenta'    : ventas[i][7]
        }
     
    return dic






print(AutoPartes(ventas))