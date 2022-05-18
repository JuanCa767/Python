#Esto es un diccionario, se denota con llaves y cada clave, luego de tener su valor lleva coma.
miDiccionario={
    'estudiante':"Juan Calle",
    'edad':20,
    'activo': True,
    'promedio_nota':4.5   
}

#Como acceder a  los valores dentro de un Diccionario
estudiante = miDiccionario['estudiante']
print (estudiante)

x  = miDiccionario['edad']
print(x)

#-------------------------------------------------------
estudiante_1= {
    'nombre': "Andrés",
    'edad': 20,
    'notas': {
        'nota_1': 3.5,
        'nota_2':4.2,
        'nota_3':4.8        
    }
}
estudiante_2= {
    'nombre': "Alejandra",
    'edad': 24,
    'notas': {
        'nota_1': 3.2,
        'nota_2':4.4,
        'nota_3':4.4        
    }
}
notas_estudiante={
    '12345678': estudiante_1,
    '98765432': estudiante_2
}
print( notas_estudiante['12345678'])

#Ejercicio: Crear un diccionario de un supermercado que tiene varias sedes
supermercado = {
    'belen':{
        'aseo': 12000000,
        'frutas': 24000000
    },
    'estadio':{
        'aseo': 10000000,
        'frutas': 8000000       
    }
}

'''
** Calcular el promeido de cada sede
** Calcular el total de ventas de todas las sedes
'''
#** Calcular el promeido de cada sede
#Promedio ventas sede Belen

sede_belen = supermercado['belen']
ventas_belen = sede_belen['aseo']
ventas_belen += sede_belen['frutas']
promedio_ventas_belen = ventas_belen/2

sede_estadio = supermercado['estadio']
ventas_estadio = sede_estadio['aseo'] 
ventas_estadio += sede_estadio['frutas']
promedio_ventas_estadio = ventas_estadio/2

total_ventas = ventas_belen + ventas_estadio

mensaje_ventas = 'PROMEDIO DE VENTAS:\n'
mensaje_ventas += f'Sede belén: ${promedio_ventas_belen}\n'
mensaje_ventas += f'Sede estadio: ${promedio_ventas_estadio}\n'
mensaje_ventas += 'TOTAL VENTAS:\n'
mensaje_ventas += f'{total_ventas}'

print(mensaje_ventas)

print("-----------------------------------------------------------")

#Declarar un diccionario vacío
diccionario = dict()
#diccionario = {}

#Añadir elementos a un diccionario
#diccionario['estudiante_1'] = "Franklin"
diccionario['estudiante_1'] = {
    'nombre': 'Franklin', 
    'apellido': 'Castaño', 
    'activo': True
    }

print(diccionario)

diccionario['estudiante_2'] = {
    'nombre': 'Erika',
    'apellido': 'Delgado',
    'activo': False
}
print(diccionario)
#Para mostrar un datos especifico de un diccionario
print('Estudiante 2:\n', diccionario['estudiante_2'])
#para modificar los valores de un diccionario
diccionario['estudiante_2']['activo'] = True
print('Estudiante 2:\n', diccionario['estudiante_2'])


