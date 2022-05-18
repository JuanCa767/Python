#esto es un arreglo
numeros=[25,26,24,23]

maximo = max(numeros)
print(f'El maxiomo numero es: ',maximo)

minimo= min(numeros)
print("El valor minimo es: ",minimo)

suma = sum(numeros)
print("La sumatoria es: ",suma,"\n")

def imprime_cosas():
    print("Hola Mundo \n")
    print("Mi primera funcion \n")
    
imprime_cosas()

def repite_cosas():
    print("\n")
    imprime_cosas()
    imprime_cosas()
    
repite_cosas()