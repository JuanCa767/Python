'''
Crear subconjunto con:
    *Country
    *Language
    *Gross Earnings
Columnas indexadas:
    *Country
    *Language
Retornar 10 registros
'''

import pandas as pd
# ruta file csv
rutaFileCsv ='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv: str) -> str:
    try:
        #Leer el archivo y retornar un dataframe
        movies = pd.read_csv(rutaFileCsv)
        #Crear subConjunto
        subConjunto = movies.loc[:, ['Country','Language','Gross Earnings']]
        #Crear tabla dinámica
        tabla = pd.pivot_table(subConjunto, index=['Country', 'Language'])
        #Retornar los primeros 10 registros
        return tabla.head(10)
    except:
        return "Error al leer el archivo de datos."

print(listaPeliculas(rutaFileCsv))

