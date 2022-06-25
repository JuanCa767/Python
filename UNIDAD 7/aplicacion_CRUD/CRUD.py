import json


import json

#Consultar la ifnormacion de todas la taresas read
def Read(rutaArchivo ='C:/Users/Juan/Documents/GitHub/Python/UNIDAD 7/aplicacion_CRUD/listadoTareas.json'):

    #Cargar el listado de tareas a un diccionario desde la capa de datos (archivo json)
    diccionarioTareas = {} #Contenedor de listado de tareas que gestiona la app

    try:
        with open(rutaArchivo) as archivo:
            diccionarioTareas = json.load(archivo)
    except