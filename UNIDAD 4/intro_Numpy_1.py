import numpy as np
guion = lambda: print('----------------------------------------------------')
#crear una matriz
matriz=np.array([10,20,30,40])
print(matriz)
guion()
matriz2D= np.array([[10,20],[30,40]])
print('matriz 2 dimensiones')
print(matriz2D)
guion()
matriz_flotante=np.array([[10,20],[30,40.3]])
print(matriz_flotante)
print(type(matriz_flotante))

guion()
matriz_cadena=np.array([[10,20],[30.2,'40S']])
print(matriz_cadena)
print(matriz_cadena.shape)

guion()

lista_n1=[10,80,20,50,60]
lista_n2=[90,150,40,10,40]

lista_n = [lista_n1+lista_n2]
print(lista_n)

guion()
print('suma de matrices')
matriz_n1=np.array(lista_n1)
matriz_n2=np.array(lista_n2)
sumatoria= matriz_n1+ matriz_n2
print(sumatoria)
guion()
#otra forma de sumar matrices
matriz_sumatoria = np.add(matriz_n1,matriz_n2)
print(matriz_sumatoria)

guion()
print('resta de matricies')
matriz_resta= matriz_n1 - matriz_n2
print(matriz_resta)
guion()
#con funcion
matriz_res=np.subtract(matriz_n1,matriz_n2)
print(matriz_res)

guion()
#Division de matrices
print('Division de matrices')
matriz_division=matriz_n1/matriz_n2
print(matriz_division)

guion()
#Multiplicacion de matrices
print('Multiplicacion de elemento a elemento')
matriz_multipli=matriz_n1*matriz_n2
print(matriz_multipli)
#con funcion
print('multiplicacion de matrices')
mMulplicacion=np.dot(matriz_n1, matriz_n2)
print(mMulplicacion)
guion()
matriz_1=np.array([[1,2,3],[4,5,2]])
matriz_2=np.array([[5,2],[1,3],[2,4]])
matriz_multiplicacion=np.dot(matriz_1,matriz_2)
print(matriz_multiplicacion)

guion()
