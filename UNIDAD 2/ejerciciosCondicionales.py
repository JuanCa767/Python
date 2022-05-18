def CDT(dinero: float, porcentaje_interes: float, tiempo: int):
    if tiempo <= 2:
        penalidad = dinero * 0.02
        total_dinero = dinero - penalidad
        txt_penalidad = f'La penalidad es de {penalidad}'
        txt_total_dinero = f'El total de dinero a retirar es {total_dinero}'
        return txt_penalidad+'\n'+txt_total_dinero
    else:
        valor_interes = (dinero * porcentaje_interes * tiempo) / 12
        total_dinero = dinero + valor_interes
        txt_intereses = f'El valor de los intereses es de {valor_interes}'
        txt_total_dinero = f'El total de dinero a retirar es {total_dinero}'
        return txt_intereses+'\n'+txt_total_dinero

print(CDT(1000000, 0.3, 3) )


def definir_mayor_edad(nombre:str, edad:int):
    if edad >= 18:
        print(f'{nombre} es mayor de edad')
    else:
        print(nombre,' es menor de edad')

definir_mayor_edad('Juan', 18)
#definir_mayor_edad('Juan', 18)

#Punto 2
#Solución de Andrea
    else:
        print (estudiante, "Aprobó la materia con una nota de", resultado)

rendimientoAcademico("Andrea", 3.4, 5.2, 3.4, 6.1)
#rendimientoAcademico("Andrea", 3.4, 5.2, 3.4, 6.1)
