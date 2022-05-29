
a=[(0,'camisas','RC',2,10),
    (1,'Pantalon','RP',5,14),
    (0,'camisa','RS',3,7),
    (1,'medias','RCA',10,100)]


def AutoPartes(ventas:list):
    resultado={}
    for x in range(len(ventas)):
        resultado[x]=[ventas[x]]
    return resultado


def consultaRegistro(ventas,idProducto):
    resulta2={}
    for i in ventas:
        if idProducto==ventas[i][0][0]:
            resulta2[i]=ventas[i]

        resulta3=''
        if len(resulta2)==0:
            resulta3='No hay registro de venta de ese producto'
        else:
            for i in resulta2:
                resulta3 += 'codigo: {}, Descripción: {}, referencia:{}, piezas vendidas: {}, stock: {}\n'.format(ventas[i][0][0],ventas[i][0][1],ventas[i][0][2],ventas[i][0][3], ventas[i][0][4])

    return print(resulta3)



#r = AutoPartes(a)
print(consultaRegistro(AutoPartes(a),0))






#print(r,'\n',r[3][0][1])
'''

#a= 'a,b,c,d,'
#a = [1,2,3,4,'a','b']
#a = (1,2,3,4,5,6)
a ={'nombres': 'juan', 'apellidos': 'castro', 'edad':44}
#para imprimri las llaves del diccionario seria solo: for x in a.keys: print(x)
#Asi como esta abajo se imprimen los valores que tiene cada llave
# .keys(): me devuelve las llaves del diccionario
#.values(): El for me devuelve los valores dentro de las llaves.
#.items(): El for me devuelve los datos en tuplas
print('----------con tuplas ---------------')
for x in a.items():
    #print(x)

print('----------- sin tuplas -------------------')
for i, j in a.items():
    #print(i,j)

'''