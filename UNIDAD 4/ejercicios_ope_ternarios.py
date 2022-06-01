'''
Obtener una lista con los nombres que empiecen en 'j'  ponerlos en mayusculas
 de lo contrario almacenar un string como 'null'
 ejemplo 
 nombres=['juan','Jaime','Pedro','camilo','dayana','maria']
 nombres = ['JUAN','JAIME0, 'NULL0...]

Desarrollar una funcion  que reciba como parametro una lsita con numeros, 
retornar una lista con los numeros pares para elevarlos  al cuadrado y 
los numeros imprares elevados al cubo

'''

nombres=['juan','Jaime','Pedro','camilo','dayana','maria']

#punto 1
funcion = lambda lista: [n.upper() if n[0].lower()=='j' else "NULL" for n in lista]
print(funcion(nombres))


#punto 2
numeros=[2,3,4,5,6,7]

funcion = lambda lista:[n**2 if n%2==0 else n**3 for n in lista]
print(funcion(numeros))


#------------USANDO MAP Y FILTER---------------------------
#para pares
funcion = lambda lista:list(map(lambda n:n**2, list(filter(lambda n:n%2==0, lista))))
print(funcion([2,3,4,5,6,7,8]))
#para numeros impares
funcion = lambda lista:list(map(lambda n:n**2, list(filter(lambda n:n%2!=0, lista))))
print(funcion([2,3,4,5,6,7,8]))