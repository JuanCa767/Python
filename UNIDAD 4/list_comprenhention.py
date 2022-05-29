#
numeros = [10,20,30,40,50]
#Para elevar al cuadrado
numeros_al_cuadrado = [n**2 for n in numeros]

'''for n in numeros:
    n**2'''
print(numeros_al_cuadrado)

#para dividir por dos
division_numeros=[n/2 for n in numeros]
print(division_numeros)

#operadores ternarios
print('--------------OPERADORES TERNARIOS-----------')
numeros_pares=[n for n in numeros if n%2==0]
print(numeros_pares)

impares_en_cero=[n if n&2==0 else 0 for n in numeros]
print(impares_en_cero)

#---------------------------------------------------------
print('------------------------------------------')

nombres = ['juan', 'maria', 'pedro', 'juliana']
iniciales=[n[0] for n in nombres]
print(iniciales)

mayusculas = [n.upper() for n in nombres]
print(mayusculas)   