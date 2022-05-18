#funciones anidadas, son funciones dentro de otras funciones

def primerFuncion():
    print("\n \"Hola desde la funcion extarna \"\n")
    def segundaFuncion():
        print("\n \"Hola desde la funcion interna \"\n")
        
    segundaFuncion()
primerFuncion()

#Funcion que permita acceder a los datos anidados de otra funcion
def primerNumero(x):
    def segundoNumero(y):
        return x*y
    return segundoNumero

resultado = primerNumero(2)

print(resultado(5))