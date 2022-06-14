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
#rutica = 'C:/Users/Juan/Documents/GitHub/Python/UNIDAD 5/movies.csv'

def listaPeliculas(rutaFileCsv: str) -> str:
    
    if rutaFileCsv.split('.')[-1] == 'csv?raw=true':
        try:
            #Leer el archivo y retornar un dataframe
            movies = pd.read_csv(rutaFileCsv)
            #Crear subConjunto
            subConjunto = movies[['Country','Language','Gross Earnings']]
            #Crear tabla dinámica
            tabla = pd.pivot_table(subConjunto, index=['Country', 'Language'])
            #Retornar los primeros 10 registros

            return tabla.head(10)
        except:
            return "Error al leer el archivo de datos."

    else:
        return 'Extensión inválida.'

print(listaPeliculas(rutaFileCsv))

