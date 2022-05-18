estudiante_1 = {
    'nombre': 'Andrés',
    'edad': 20,
    'notas': {
        'nota_1': 3.5,
        'nota_2': 4.2,
        'nota_3': 4.8
    }
}
estudiante_2 = {
    'nombre': 'Alejandra',
    'edad': 24,
    'notas': {
        'nota_1': 3.2,
        'nota_2': 4.5,
        'nota_3': 4.4
    }
}
estudiante_3 = {
    'nombre': 'Sebastian',
    'edad': 24,
    'notas': {
        'nota_1': 4.2,
        'nota_2': 2.5,
        'nota_3': 3.4
    }
}

notas_estudiantes = {
    '1234': estudiante_1,
    '9876': estudiante_2,
    '1144': estudiante_3
}

'''
Desarrollar una función que reciba como parametro el diccionario 
notas_estudiantes. 
La funcion debe retornar un diccionario que contega el promedio de notas
de cada estudiante.
'''
#definimos la función
def calcular_promedio_notas(notas_est:dict):
    #primero creamos el diccionario que va almacenar 
    #las el promedio de notas
    dict_promedio_estudiante = dict() #Esto es un diccionario vacio

    #Recorrer el diccionario padre
    for estudiante in notas_est.values():
        #imprimimos el nombre del estudiante
        #print(estudiante['nombre'])       
        nombre = estudiante['nombre']
        #obtener el diccionario de notas del estudiante
        notas = estudiante['notas']
        #variable don de se almacenan las notas de cada estudiante
        promedio = 0
        #recorer el diccionario hijo de cada estudiante (notas)
        #for anidado
        for n in notas.values():
            #sumar las notas
            promedio += n
            #Imprimir notas
            #print(n)
        #obtener el tamaño del diccionario de notas
        cant_notas = len(notas)
        #print("Cantidad de notas -> ", cant_notas) 
        promedio /= cant_notas
        #redondear las a dos cifras : round(numero_a_redondear, cantidad_de_decimales)
        #print("pormedio: ", round (promedio,1))
        #añadir promedio del estudiante al diccionario dict_promedio_estudiante
        #dict_promedio_estudiante[nombre] = estudiante['id_estudiante']
        dict_promedio_estudiante[nombre] = round(promedio,1)
    return dict_promedio_estudiante

print(calcular_promedio_notas(notas_estudiantes))