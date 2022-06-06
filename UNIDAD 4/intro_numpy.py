import numpy as np
#Matriz de una dimension
matriz1D=np.array([34,25,7])
print('Matriz de una dimension')
print(matriz1D)

#-----------------------------------------------
for i in matriz1D:
    matriz1D[2] =44
print(matriz1D)
print(matriz1D.shape,'\n') 

#matriz de 2 dimensiones
matriz2D= np.array([[1,2,3],[4,5,6]])
print('Matriz de 2 dimensiones')
print(matriz2D)
print(matriz2D.shape)

#---------------------------------------------
for i in matriz2D:
    matriz2D[0][0]= 19
    for x in matriz2D:
        matriz2D[1][1]=66

print(matriz2D)

#for i in matriz2D:
    #for x in matriz2D:
    #    matriz2D[i][x]=round(0,20)
#print(matriz2D)

#---------------------------------------------------------------
#matriz de 3 Dimensiones
matriz3D= np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Matriz de 3 Dimensiones')
print(matriz3D)
print(matriz3D.shape)

for i in matriz3D:
    matriz3D[0][1]= 43
    for x in matriz3D:
        matriz3D[1][2]= 99
        for j in matriz3D:
            matriz3D[2][0]=33 

print(matriz3D)

