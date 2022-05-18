

from re import X


estudiante_1 = {
    'nombre': 'Andrés',
    'edad': 20,
    'notas': {
        'nota_1': 3.5,
        'nota_2': 4.2,
        'nota_3': 4.8
    }
}

notas_estudiantes = {
    '12345': estudiante_1
}

def calcular_promedio_estudiante(notas_estu:dict):
    #dccionrio vacio
    dict_promedio = dict()
    
    for estudiante in notas_estu.values():
        print('-------EStas son las notas de -------------------')
        #print("nombre del estudiante: ", estudiante['nombre'])
        nombre = estudiante['nombre']
        print ("sus notas son: ")
        #print(estudiante['notas'])
        notas = estudiante['notas']
        promedio = 0
        for x in notas.values():
            promedio += X
        cantidad_notas= len (notas)
        promedio /= cantidad_notas
        dict_promedio[nombre] = round(promedio,1)
        
    
    return dict_promedio
    

print (calcular_promedio_estudiante(notas_estudiantes))