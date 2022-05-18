#funcion con argumentos
def suma(a,b):
    return a+b
print("\n")
print("Es funcion suma recibe los datos por parametro ")
print("la suma es: ",suma(5,10),"\n")

#funcin con argumentos y parametros
def suma(a,b):
    return a+b

a = 1200
b=50
print(suma(a,b))

#otra manera de hacerlo
def otra_suma1(num1, num2):
    print(num1+ num2)
    print("\n")

resul = otra_suma1(5, 7)

print (resul)


#otra
def otra_suma(num1,num2):
    print(num1 + num2)
    print("\n")
    return num1 + num2

otra_suma(5, 6)
