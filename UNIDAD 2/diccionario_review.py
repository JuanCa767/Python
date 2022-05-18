#creaccion de diccionario
persona = {
    'nombre': 'Juan',
    'edad': 45,
    'telefono': '3192558965',
}
#muestra la clave y el valor
print(persona)
#muestra solo el valor porque le doy la clave
print(persona['nombre'])
#modificar diccionario 
persona['nombre'] = 'pedro'
#imrpirm datos del diccionario
print(persona['nombre'])
print(persona['edad'])
print(persona['telefono'])
#imrpirm todo el diccionario 
print(persona)

persona = {
    'nombre': 'Juan',
    'edad': 45,
    'telefono': '3192558965',
    'libros':{
        'titulo': '100 años de soledad',
        'autor': 'Gabrirl Garcia Marquez'        
    }
}

print(persona['libros']['titulo'])
#modificar el nombre del titulo
persona['libros']['titulo'] = 'cien años de soledad'
#presentar lo modificado
print(persona['libros']['titulo'])