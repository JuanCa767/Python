#-----------------------------------------------------------------------
numeros = [10,20,30,40,50,60,70,80,90]

numeros_al_cuadrado = [n**2 for n in numeros]
print(numeros_al_cuadrado)
#-----------------------lo mismo que anterior----------------------------
lista  =[]
for n in numeros:
    lista.append(n**2)

print(lista)
#-----------------------------------------------------------------------

funcion = lambda lista: [n/2 for n in lista]

print(funcion(numeros_al_cuadrado))

#---------------------------------------------------------------------------

numeros=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
numeros_pares = [n for n in numeros if n%2==0]
print(numeros_pares)

numeros_impares=[n for n in numeros if n%2!=0]
print(numeros_impares)

#----------------------------------------------------------------------------
