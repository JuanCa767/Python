#Desarrolle un programa que permita encontrar si un numero ingresado es par o impar.
#Variables
num = 0
num = int(input("Ingrese un nuermo entero: "))

if num < 0:
    print("El numero ingresado debe ser positivo")
else:
    if num/2*2 ==num:
        #num % 2 == 0:
        print("El numero leido es par")
    else:
      print("El numero es Impar")
