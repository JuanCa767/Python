'''
UTILIZAR LIST COMPREHENSION Y LAMBDA
1) Desarrolle una función que reciba como parámetro una lista de números,
    retorne una lista con los números pares elevados al cuadrado
2) Desarrolle una función que reciba como parámetro una lista de nombres,
    Retorne una lista con las iniciales
3) Desarrolle una función que reciba como parámetro una lista de nombres,
    Retorne una lista con los nombres que empiecen por 'J' y coloque 
    su nombre en mayúscula
'''
#punto 1
numeros=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]

numeros_pares= lambda lista:[n**2 for n in lista if n%2==0]

print(numeros_pares(numeros))

#punto 2
nombres=['juan','pedro','camilo','dayana','maria']

iniciales = lambda lista: [n[0] for n in lista]
print(iniciales(nombres))

#punto 3

nombres=['juan','Jaime','Pedro','camilo','dayana','maria']

iniciales_J = lambda lista: [n.upper() for n in lista if n[0].lower()=='j' ]
print(iniciales_J(nombres))