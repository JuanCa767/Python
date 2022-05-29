

abuelo = [
    [[100, 50, 90], [150, 40, 200], [200, 250, 290]],
    [[40, 60, 100], [110, 140, 250], [20, 280, 260]]
]

'''
Iterar la lista 'abuelo' y mostrar los datos con la siguiente estructura: 
------------Padre 1--------
    ------Hijo 1--------
        *100
        *50
        *90
    -----Hijo 2--------
        *150
        *40
        *200
'''
#Solución de Andrea
for padre in abuelo:
    print (padre)
    for hijo in padre:
        print (hijo)
        for elemento in hijo:
            print (elemento)



print('-----------------------------------------------')


padre = [
    [100, 50, 90], 
    [150, 40, 200],
    [40, 60, 100], 
    [110, 140, 250]
]

'''
1) Iterar la lista padre y mostrar la sumatoria TOTAL de todos los elementos
de las listas hijos
'''

for hijo in padre:
    suma = 0
    #Iterar lista hijo
    for e in hijo:
        suma +=e
        print(f"La sumatoria por hijo:  ",suma)


