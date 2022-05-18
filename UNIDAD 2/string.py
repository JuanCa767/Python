#leer los datos de un string

fruta="fresa"
letra=fruta[1]
#print(letra)
#tamaño de la cadena
fruta= "bananba"
letra= fruta[2]
#print(letra)
longitud=len(fruta)
ultimo=fruta[longitud-1]
#print(ultimo)
tamano= len(fruta)
#print(tamano)

#rebanadas de string
s="Monty Python"
print(s[0:5])
print(s[6:12])

s="Juan Carlos"
#print(s[0:4])
#print(s[5:12])
tamano= len(s)
#print(tamano)

fruta= "banana"
print(fruta[:3])
print(fruta[3:])
print(fruta[3:3]) #las cadenas son inmutables, quiere decir que no se puede cambiar su contenido
tamano= len(fruta)
#print(tamano)

#Eejemplo de inmutabilidad
saludo="Hola como estas?"
nSaludo='J'+saludo[1]
#print(nSaludo)
tamano= len(saludo)
#print(tamano)
utlimo_caracter= saludo[tamano-1]
#print(utlimo_caracter)

#operado in en cadenas
var1="a"
var2 = "banana"
#print(var1 in var2)

var1="ola"
var2 = "banana"
#print(var1 in var2)

#comparacion de string
palabra="banana"
if palabra == "banana":
   print("Esta bien, hay comparacion ")
