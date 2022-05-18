#---------------CONDICIONALES 2----------------

num1= 100
num2 =120
num3 = 50
num4 = 200

if (num1 > num2 and num3 > num4):
    print("Se cumple la condicion del and")
else: 
    print("No se cumple la condicion del and")
    

'''
Uno solo = es asignacion
un doble (==) es comparacion
'''
if (num3 > num2)or(num1 == num4):
  print("Se cumple la condicon del or")
else:
  print("No se cumple la condicon del or")

#Diferente -> o !=
if (num1 > num2 and num4 != num1) or (num3 == num2 and num1 > num3):
    print("Se cumple la condicion #4")  
else:
    print("No se cumple la condicion #4")

#negacion
if not ((num1 > num2 and num4 != num1) or (num3 == num2 and num1 > num3)):
    print("Se cumple la condicion #4")  
else:
    print("No se cumple la condicion #4")