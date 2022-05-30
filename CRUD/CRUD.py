# 1. Menu de opciones
menuOpciones = True

# Diccionario de tareas
tareas ={'01': {'Descripcion': 'Lavando la loza',
                'Tiempo': 5,
                'Estado': 'Pendiente'},
        '02': {'Descripcion': 'Aqui',
                'Tiempo': 16,
                'Estado': 'Pendiente'}}

# Funciones
# Funcion para Agregar Tareas
def adicionarTareas (tareas, identificador, nuevaTarea):
    tareas[identificador] = nuevaTarea
    return tareas

# Funcion para consultarTareas
def consultarTareas (tareas):
    for identificador, tarea in tareas.items():
        print(identificador, '--', end = '')
        for atributo in tarea.values():
            print(atributo,'--', end = '')
    print('')

#Funciones para Actualizar Tareas 
# Funcion para buscar identificador
def consultarIdentificador (identificador, tareas):
    conjuntoIdentificadores = set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False
# Funcion para actualizar Tareas
def actualizarTareas (tareas, identificador):
    nuevaDescripcion = str(input('Agrega una descripcion nueva: '))
    nuevoTiempo = int(input('Agrega el nuevo tiempo: '))
    nuevoEstado = str(input('Agrega e nuevo estado: '))
    # Modificarems esta info en el diccionario
    tareas[identificador]['Descripcion'] = nuevaDescripcion
    tareas[identificador]['Tiempo'] = nuevoTiempo
    tareas[identificador]['Estado'] = nuevoEstado

#Funcion para eliminarTarea
def eliminarTarea (identificador, tareas):
    conjuntoIdentificadores = set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        tareas.pop(identificador)
        print(f'El numero de tarea {identificador} fue eliminado')
    else: 
        print('La tarea no fue encontrada')

while menuOpciones:
    print('-------- Aplicacion CRUD -------\n'
        '1. Crear Tarea\n'
        '2. Consultar Tarea\n'
        '3. Actualizar Tarea\n'
        '4. Eliminar Tarea\n'
        '5. Salir\n')

    opcion = input('Digite la opcion:')
    
    
    if opcion == '1':
        identificador = input('Numero de tu tarea: ')
        descripcion = str(input('Describe tu tarea: '))
        tiempo = int(input('Cuanto vas a tardar: '))
        estado = str(input('Agrega el estado de la tarea: '))
        nuevaTarea = {
            'Descripcion' : descripcion,
            'Tiempo' : tiempo,
            'Estado' : estado
        }
        tareas = adicionarTareas(tareas, identificador, nuevaTarea)
        print(tareas)
        
        
    elif opcion == '2':
        consultarTareas(tareas)
        
    elif opcion == '3':
        identificador = str(input('Ingresa el numero de ID: '))
        if consultarIdentificador (identificador, tareas):
            actualizarTareas(tareas, identificador)
            print(tareas[identificador])
        else:
            print('No se ha encontrado el identificador')
        
    elif opcion == '4':
        identificador = str(input('Ingresa el numero de ID: '))
        eliminarTarea(identificador,tareas)
    elif opcion == '5': 
        print('-------Saliendo del programa------------')
        menuOpciones = False
    else:
        print('Digite un numero del 1 al 5')