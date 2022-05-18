'''
Desarrolle un programa que lea dos numeros positivos y determine si el ultimo digito
de un numero es igual al ultimo digito del otro
'''
#variables
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

if num1 <0:
    num1=num1*(-1)

ud1= num1-num1/10*10

if num2 <0:
    num2 = num2*(-1)
    
ud2= num2-num2/10*10

if ud1 == ud2:
    print("El útlimo digito de un numero es igual al último digito del otro")
else:
    print("El último digito de un numero NO es igual al último digito del otro")