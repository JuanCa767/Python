from pickletools import int4
import pandas as pd
import numpy as np
print('\x1Bc')
#Asignaturas que ve un estudiante X
#Lista

"""asignaturas= pd.Series(['Matemática','Inglés','Habilidades','Programación'], index=['M01','I02','H03','P04'])
print(asignaturas)

#Diccionario
#Las notas del estudiante X
asignaturas= pd.Series({'Matemática':4.5,'Inglés':2.7,'Habilidades':4.0,'Programación':4.8} )
print(asignaturas)

#Tuplas
asignaturas= pd.Series(('Matemática','Inglés','Habilidades','Programación'), index=['M01','I02','H03','P04'])
print(asignaturas)"""

"""asignaturas= pd.Series(['Matemática','Inglés','Habilidades','Programación'], index=['M01','I02','H03','P04'])
print(asignaturas)
asignaturas.name='Nombre de la serie'
print(asignaturas)
print('Tipo de datos', asignaturas.dtype)
print('Índices', asignaturas.index)
print('Valores', asignaturas.values)"""


"""asignaturas= pd.Series({'Matemática':4.5,'Inglés':2.7,'Habilidades':4.0,'Programación':4.8} )
print(asignaturas)

print('Nota de Matemáticas')
print(asignaturas[0])

print('Nota de Inglés')
print(asignaturas['Inglés'])

print('Notas por rango, Inglés, Habilidades')
print(asignaturas[1:3])

print('Index y por el valor')
print(asignaturas[[3,1]])

print('Función get')
print(asignaturas.get(1))"""

#asignaturas= pd.Series(['Matemática','Inglés','Habilidades','Programación'], index=['M01','I02','H03','P04'])
#print(asignaturas)

"""print('Por índice explícito o etiquetas...')
print(asignaturas.loc['I02'])

print('Por índice implícito')
print(asignaturas.iloc[3])

print('Por índice implícito por rango')
print(asignaturas.iloc[0:3])

print('Por índice implicito las que queremos')
print(asignaturas.iloc[[0,3]])

print('Aleatorios --- sample')
print(asignaturas.sample(1, random_state=0))

print('Eliminada el inglés')
#asignaturas.pop('I02')
print(asignaturas.drop(asignaturas.index[[1,2]]))
#print(asignaturas)"""

"""
print('Elimando pop sin índices explícitos')
x=pd.Series([1,2,3,4])
x.pop(2)
print(x)"""

"""x=pd.Series([1,2,3,4,5,6,7,8,9,10])

#Cuáles edades son mayores a 5

print(x>5)

print('Sólo los números')

print(x[x>5])

print(x.axes)

print('La dimensión o tamaño de mi serie', x.shape[0])"""

"""asignaturas= pd.Series(['Matemática','Inglés','Habilidades','Programación'], index=['M01','I02','H03','P04'])
print(asignaturas)

asignaturas[1]='Español'
print(asignaturas)

asignaturas[0:2]=['Sociales','Filosofía']
print(asignaturas)

asignaturas['M01']='Informática'
print(asignaturas)"""


"""numeros=pd.Series([1,2,3,4,5,6,7,8,9,10])

#Números, los números pares

r=numeros.where(numeros%2==0)
print(r)

#print(r.shape[0])

a=[]
for i in range(r.shape[0]):
    if not(pd.isna(r[i])):
        a.append(r[i])

print(a)"""

#DataFrames
"""#1. Crear un diccionario

ventas={'Manzanas':[60,10,20,30,50],'Peras':[10,40,35,12,10]}

#2. Crear el DataFrames

frutasVendidas= pd.DataFrame(ventas, index=['Lunes','Martes','Miércoles','Jueves','Viernes'])
print(frutasVendidas)

#Atributos

print('Atribujos de index y columns')
print('Imprimir índices')
print(frutasVendidas.index)
print('Imprimir columnas')
print(frutasVendidas.columns)

print('Axes --- Brindar información')
print(frutasVendidas.axes)
print('Dimensión del Dataframes')
print(frutasVendidas.shape)

print('Nombres a mis filas y a mis columnas')
print('Nombre a mis filas')
frutasVendidas.index.name='Días'
frutasVendidas.columns.name='Frutas'
print(frutasVendidas)
print('Los valores')
print(frutasVendidas.values)"""

"""x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])#3x4

print(x)

df=pd.DataFrame(x)
print(df)"""

#Crear DataFrames a partir de varios diccionarios

"""unidades_2020={'Hierro':5.2,'Fósforo':7.2, 'Potasio':6.3}
unidades_2021={'Hierro':4.2,'Fósforo':3.2, 'Potasio':6.5}
unidades_2022={'Hierro':5.4,'Fósforo':7.8, 'Potasio':6.8}

elementos=pd.DataFrame([unidades_2020,unidades_2021,unidades_2022], index=[2020,2021,2022])
print(elementos)"""

"""#CRear DataFrames a partir de Series
#Inventario

entran=pd.Series([10,15,24,18,10,14,18,19,10,20,13,14], 
                index=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                'Septiembre','Octubre','Noviembre','Diciembre'])

salen=pd.Series([8,12,10,15,8,12,17,11,9,12,10,11], 
                index=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                'Septiembre','Octubre','Noviembre','Diciembre'])


#Crear el DataFrame

inventario=pd.DataFrame({'Entradas':entran,'Salida':salen})
print(inventario)

#Agregar otra columna
inventario['Saldo']= inventario.Entradas - inventario.Salida
print(inventario)


#Métodos

print('Mostrar los primeros 10')
print(inventario.head(10))
print('Mostrar los 5 últimos')
print(inventario.tail())
print('5 Aleaotorios')
print(inventario.sample(5))
print('Información estadística')
print(inventario.describe())
print('Información básica')
print(inventario.info())"""


#Conteo
"""salen=pd.Series([8,12,8,15,8,12,12,11,11,12,10,11])

print('Conteo de valores')
print(salen.value_counts())"""


#Selección de información
"""ventas=pd.DataFrame({
    'Entradas':[41,25,36,47],
    'Salidas':[40,20,35,42],
    'Valoración': [66,54,70,14],
    'Límite':['No','Si','No','No'],
    'Cambio':[1.43,1.16,-0.5,1.0]
}, index=['Enero','Febrero','Marzo','Abril'])

print(ventas)
print('Por medio de key---columns')
print(ventas['Entradas'])
print('Por medio del index')
print(ventas['Entradas']['Enero'])

#Metodos loc y iloc, get
print('Por el método loc')
print(ventas.loc['Enero'])
print('Por el iloc')
print(ventas.iloc[1])
print('Por el método get')
print(ventas.index.get_loc('Abril'))
print('Por el método get por columnas')
print(ventas.columns.get_indexer(['Cambio']))
print('Por el método get por columnas dos')
print(ventas.columns.get_loc('Cambio'))

#Rango
print('Rango')
print(ventas.iloc[0:2,0:2])
print('Otro Rango')
print(ventas.iloc[1:3,2:4])"""

#DataFrames con Rangos
"""df=pd.DataFrame(np.arange(1,19).reshape([6,3]), 
                index=['a','b','c','d','e','f'],
                columns=['A','B','C'])
print(df)

#Edición de DataFrames
print('Por los índices --- método iloc')
df.iloc[1,2]=-1
print(df)
print('Modificar el número 8 por -8')
df.iloc[2,1]=-8
print(df)
print('Por columnas')
df['A']=[-1,-3,-9,-4,-7,-8]
print(df)

print('Por filas')
df.loc['f']=[0,0,0]
print(df)
print('Por rangos')
df.iloc[0:2,0:2]=-8
print(df)
print('Otro rango')
df.iloc[3:6,1:3]=-1
print(df)"""

#Método where
"""df= pd.DataFrame(np.arange(1,13).reshape([4,3]),
                index=['a','b','c','d'],
                columns=['A','B','C'])

print(df)

#Números pares
r=df.where(df%2==0)
print(r)

#Recorrido por todo el DataFrame

print('Dimensión de r', r.shape)
print('Filas',r.shape[0])
print('Columnas',r.shape[1])

rf=[]

for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if not(pd.isna(r.iloc[i,j])):
            rf.append(r.iloc[i,j])

print(rf)"""


#Eliminar drop
"""df= pd.DataFrame(np.arange(1,13).reshape([4,3]),
                index=['a','b','c','d'],
                columns=['A','B','C'])
print(df)
print('Eliminar por filas')
print(df.drop('c'))

print('Eliminar por varias filas')
print(df.drop(['a','c']))

print('Eliminar por columnas')
print(df.drop(columns='C'))"""

#Función concatenar
df1= pd.DataFrame(np.arange(1,13).reshape([4,3]),
                index=['a','b','c','d'],
                columns=['A','B','C'])

df2= pd.DataFrame(np.arange(1,5).reshape([2,2]),
                index=['a','b'],
                columns=['A','B'])

print('Data 1')
print(df1)

print('Data 2')
print(df2)

print('Concatenado o unido')
dfr=pd.concat([df1,df2])

print(dfr)




        



















