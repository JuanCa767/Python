#Crear una lista con numeros pares del 1 al 1000
#Crear una lista con numeros impares del 1 al 1000

listaPares = list()
listaImpares = list()

for x in range(1,1001):
    if x%2==0:
        listaPares.append(x)
    else:
        listaImpares.append(x)

print(listaPares,'\n')
print(listaImpares)
