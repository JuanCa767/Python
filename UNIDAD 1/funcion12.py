
print("Seleccione una opcion "'\n')
seleccion = int(input(" 1 para suma '\n, 2 para resta'\n', 3 multiplicacion'\n', 4 division "))
num1 = int( input("Ingrese el primer numero "))
num2 = int(input("Ingrese el primer numero "))

#funcion
def operaciones(num1, num2):
    if seleccion == 1:
        suma = num1 + num2
        print(" La suma de los dos numeros es: ",suma)
    if seleccion == 2:
        resta = num1 - num2
        print("La resta es: ", resta)
    if seleccion == 3:     
        multiplicacion= num1*num2
        print("La multiplicacion es: ",multiplicacion)
    if seleccion == 4:
        division= num1/num2
        print("La multiplicacion es: ",division)        
    else:
        print("Esta opcion no esta disponible ")

#llama la funcion
operaciones(num1,num2)