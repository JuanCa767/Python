
#Input para solicitar datos al usuario
#Input retorna un string
#Castear/convertir -> int()
#num_1 = int( input('Ingrese un número >>> ') )
#num_2 = int( input('Ingrese otro número >>> ') )
#suma = num_1 + num_2
#print(f'La suma es {suma}')


opcion = ''

while opcion != 3:
    mensaje_menu = '1) Sumar\n'
    mensaje_menu += '2) Restar\n'
    mensaje_menu += '3) Salir\n'
    mensaje_menu += '>>> '
    #Capturo lo que ingresa el usuario y lo casteo/convierto a entero
    opcion = int(input(mensaje_menu))
    if opcion == 1:
        #Solicitar datos al usuario y convertirlos a flotante (números con decimales)
        num_1 = float( input('Ingrese el primer número >>> ') )
        num_2 = float( input('Ingrese el segundo número >>> ') )
        #Sumar los números
        suma = num_1 + num_2
        print(suma)
    elif opcion == 2:
        #Solicitar datos al usuario y convertirlos a flotante (números con decimales)
        num_1 = float( input('Ingrese el primer número >>> ') )
        num_2 = float( input('Ingrese el segundo número >>> ') )
        resta = num_1 - num_2
        print(resta)
    elif opcion != 3:
        print('opción incorrecta')


'''
Mejore el algoritmo anterior creando una función que solicite los números al usuario 
y retorne un diccionario con los números ingresados
'''
