'''
estudiantes ={
    'nombre':"",
    'apellido':"",
    'notas':"",
}
'''

#funcion registrar estudiantes
def registrar_estudiante(estudiantes:dict):
    print('---------------------REGISTRAR ESTUDIANTE --------------------')
    #Obtener la cedula del estudiante
    cedula = input('Ingrese la cedula del estudiante: ')
    #Añadir los datos al diccionario 'estudiantes'
    estudiantes[cedula]={
        'nombre': input('Nombre: '),
        'apellido': input('apellido: '),
        'notas': []   
    }
    print('\n Usuario registrado con exito \n')
#-------------------------------------------------------------------------------------------------------------
#Funcion para registar las notas del estudiante
def registrar_notas(estudiantes: dict):
    print('-------------REGISTRAR NOTAS:--------------\n')
    #Obtener la cédula del estudiante
    cedula = input('Ingrese la cédula del estudiante: ')
    #Validar si la cédula está como clave en el diccionario
    if cedula in estudiantes:
        nombre = estudiantes[cedula]['nombre']
        apellido = estudiantes[cedula]['apellido']
        print(f'Estudiante: {nombre} {apellido}')
        notas = []
        opc = ''
        contador = 1
        while opc != 'N':
            nota = float( input(f'Ingrese nota {contador}: ') )
            #Agregar la nota a la lista 'notas'
            notas.append(nota)
            #Solicitar dato al usuario y ponerlo en mayúscula
            opc = input('¿Desea ingresar mas notas? S/N ').upper()
            contador += 1
        estudiantes[cedula]['notas'] = notas

    else:
        print('\nLa cédula ingresada no se encuentra en la base de datos\n')
   
#-------------------------------------------------------------------------------------------------------------
#Funcion que permite actualizar estudiante
def actualizar_estudiante(estudiantes: dict):
    print('-------------ACTUALIZAR ESTUDIANTE:--------------\n')
    #Solicitar cedula del estudiante
    cedula = input('Ingrese la cédula del estudiante: ')
    #Validar si el estudiante existe en el diccionario
    if cedula in estudiantes:
        nombre = input('Ingrese nuevo nombre: ')
        apellido = input('Ingrese nuevo apellido: ')
        #Actualizar info en el diccionario
        estudiantes[cedula]['nombre'] = nombre
        estudiantes[cedula]['apellido'] = apellido
    else:
        print('\nLa cédula ingresada no se encuentra en la base de datos\n')
#------------------------------------------------------------------------------------------------------------
#Funcion para actualizar notas
def actualizar_notas(estudiantes:dict):
    print('-------------ACTUALIZAR NOTAS:--------------\n')
    #solicitar cedula
    cedula = input('Ingrese la cedula del estudiante: ')
    #Validar si el estudiante existe
    if cedula  in estudiantes:
        #validar si el estudiante tiene notas
        if 'notas' in estudiantes[cedula]:
            notas:list = estudiantes[cedula]['notas']
            print('nota\tid_nota')
            for index in range(0, len(notas)):
                print(f'{notas[index]}\t{index}')
            #obtener el id nota a actualziar
            id_nota = int(input('\n Ingrese el id de la nota a actualizar: '))
            nueva_nota = float(input('Ingrese la nueva nota: '))    
            #Actualizar nota
            notas[id_nota] = nueva_nota
            print('\n Nota actualizada con exito')
        else:
            nombre = estudiantes[cedula]['nombre']
            print(f'\n El estudiante {nombre} no tiene notas asignadas\n')    
#-------------------------------------------------------------------------------------------------------------
#Funcion para consultar estudiantes
def consultar_estudiante(estudiantes: dict):
    #iterar diccionario
    for cedula, info in estudiantes.items():
        nombre= info['nombre']
        apellido= info['apellido']
        print(f'-----------{nombre} {apellido}------------')
        print(f'Cedula: {cedula} ')
        print('Notas: ')
        if 'notas' in info:
            notas = info['notas']
            for n in notas:
                print(f't*{n}')
        else:
            print('El estudiante no tiene notas asignadas')
#-------------------------------------------------------------------------------------------------------------
#funcion para eliminar estudiantes
def eliminar_estudiante(estudiantes: dict):
    print('-------------ELIMINAR  ESTUDIANTE:--------------\n')  
    #obtener la cedula del estudiante
    cedula = input('Por favor ingrese la cedula del estudiante')
    if cedula in estudiantes:
        #Eliminar estudiante
        estudiantes.pop(cedula)
        print('\n Estudiante eliminado con exito \n')
    else:
        print('\n El estudiante con cedula {cedula} no existe en la base de datos ')
        
          


#-------------------------------------------------------------------------------------------------------------
#funcion menu
def menu():
    #Creacion del diccionario
    estudiantes = dict()
    #Creacion del menu
    mensaje_menu ='-------------------CRUD ESTUDIANTES-----------------\n'
    mensaje_menu += '1)Registrar estudiante \n'
    mensaje_menu += '2)Registrar notas del estudiante\n'
    mensaje_menu += '3)Actualizar estudiante\n'
    mensaje_menu += '4)Actualizar notas\n'
    mensaje_menu += '5)Consultar estudiantes\n'
    mensaje_menu += '6)Eliminar estudiante\n'
    mensaje_menu += '7)Eliminar todos los estudiantes\n'
    mensaje_menu += '8)Salir\n'
    mensaje_menu += '>>>'
    
    #Opcion de codigo para poder mostrar el menu y esperar la opcion
    opcion=''
    while opcion!= 8:
        opcion = int(input(mensaje_menu))
        if opcion ==1:
            registrar_estudiante(estudiantes)
        elif opcion == 2:
            registrar_notas(estudiantes)
        elif opcion == 3:
            actualizar_estudiante(estudiantes)
        elif opcion == 4:        
            actualizar_notas(estudiantes)
        elif opcion == 5:
            consultar_estudiante(estudiantes)
        elif opcion == 6:
            eliminar_estudiante(estudiantes)
        elif opcion == 7:
            estudiantes.clear()
            print('\nTodos los estudiantes han sido eliminados con exito')
        elif opcion !=8:
            ('Por favor ingrese una opcion valida')
    

menu()