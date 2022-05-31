'''
Desarrollar una funcion anonima para calcular el promedio de tres numeros.
'''
#forma mas sencilla
promedio = lambda n1,n2,n3 : (n1+n2+n3)/3
print(promedio(4.5, 4.2, 4.4))


#otra manera pero sin necesidad
def cal_promedio(promedio):
    promedio = lambda n1,n2,n3 : (n1+n2+n3)/3

print(promedio(4.5,4.2,4.4))

