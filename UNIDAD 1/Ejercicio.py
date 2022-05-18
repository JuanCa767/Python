'''
1 Desarrollar una funcion que reciba como parametro el nombre y la edad del usuario.
Que muestre ne pantalla el nombre del usuario e indique si es mayor de edad o menor de edad
Ejemplo: Pedro es mayor de edad
'''
#1
def mayorDeEdad(nombre1:str, edad:int):
    if edad >= 18:
        print(nombre1, " Es mayor de edad")
    else:
        print(nombre1, " Es menor de edad")

mayorDeEdad("Camilo",145)
