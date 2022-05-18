'''
2 Desarrolle un funcion que calcule  y muestre el primedio de 4 notas de un estudiante 
e imprima en consola si el estudiante paso o no la materia. Nota minima 3

'''
#2
def notaFinal(nombre:str, nota1:float, nota2:float, nota3:float, nota4:float):
    promedio = (nota1 + nota2 + nota3 + nota4)/ 4
    if promedio >= 3.0:
        print(nombre," Felicitaciones pasate la materia, su promedio es:  ", promedio)
    else:
        print(nombre, " No pasate la materia, su promedio es: ", promedio, " Intentalo nuevamente")

notaFinal("camilo", 4.0,4.5,3.2,4.0)