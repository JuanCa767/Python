#Listas compuestas
hijo_1 =['sebastian','Alejandra']
hijo_2 = ['Juan', 'Camilo']
hijo_3 = ['Ana', 'maria']

padre = [hijo_1, hijo_2, hijo_3]

#print (padre)

print ("-----------------------------------------------")
#print(padre[0])
#print(hijo_1)
#print(padre[1])
#print(hijo_2)

nombre_1 = padre[0][0]
#print(nombre_1)
nombre_2 = padre[0][1]
#print(nombre_2)
nombre_3 = padre[1][0]
#print(nombre_3)
nombre_4 = padre[1][1]
#print(nombre_4)

print ("-----------------------------------------------\n")

'''#Recorrer una lista compuesta, debemos recorrer primero la lista padre
for x in padre:
    #print(x)
    #iterar los hijos
    for i in x:
        #print(i)

#print ("-----------------------------------------------\n")'''
#ejercicio
for x in padre:
    for i in x:
        print(i)




