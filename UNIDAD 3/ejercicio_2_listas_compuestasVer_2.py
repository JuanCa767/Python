'''
2) Desarrolle un programa que solicite nombres de estudiantes y posteriormente
    solicite la nota de cada estudiante. Esta información debe guardarla en
    una lista compuesta con la siguiente estructura:
    *Ejemplo:
    [
        ['Juan', 'Pedro'],
        [4.5,   3.2]
    ]
'''

def registrar_estudiantes(lista: list):
    opc = ''
    lista_nombres = []
    while opc != 'N':
        nombre = input('Nombre del estudiante: ')
        lista_nombres.append(nombre)
        opc = input('¿Desea ingresar mas estudiantes? S/N').upper()
    
    lista.append(lista_nombres)


def registar_notas(lista:list):
    op=''
    lista_notas= []
    cant_notas= len(lista[0])
    for i in range(cant_notas):
        nota = float(input(f'Nota del estudiante {i+1}: '))
        lista_notas.append(nota)
        op = input('¿Desea ingresar mas notas? S/N').upper()
        if op == 'N':
            break
        
    lista.append(lista_notas)
 

def menu(): 
    lista = []
    mensaje_menu = '---------------ESTUDIANTES - NOTAS-----------\n'
    mensaje_menu += '1) Registrar estudiantes\n'
    mensaje_menu += '2) Registrar notas\n'
    mensaje_menu += '-1) Salir'
    mensaje_menu += '>>> '

    opcion = 0
    while opcion != -1:
        opcion = int(input(mensaje_menu))
        #Evaluar la opción ingresada por el usuario
        if opcion == 1:
            registrar_estudiantes(lista)
        elif opcion == 2:  
            registar_notas(lista)
        else:
            print("Digite -1 para salir: ")
        print("---------------------------------------------------")
        print(lista)
menu()
