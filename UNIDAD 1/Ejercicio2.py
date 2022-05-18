'''
3) Desarrolle una función que calcule el valor del interes de un CDT.
    Muestre en pantalla:
        *El valor del interés ganado
        *El valor TOTAL DEL DINERO al momento de retirarlo del CDT
        *Si el usuario retira el dinero menor a dos meses se aplica una penalidad del 2%
            Fórmula: dinero - (dinero * 0.02)
        *Si el usuario retira el dinero menor o igual a dos meses se aplica una penalidad del 2%
            Fórmula: 
                *Penalidad: dinero * 0.02
                *Mostrar en pantalla el valor de la penalidad
        *Si el usuario retira el dinero en un plazo mayor a dos meses su interés será:
            Fórmula:
                *valor_interes = (dinero * porcentaje_interes * tiempo) / 12
            *Mostrar en pantalla el valor del interés ganado
'''

def CDT(dinero: float, interes: float, tiempo: int):
    porcentaje = interes /100
    if tiempo <= 2:
        penalidad = dinero * 0.02
        total_dinero = dinero - penalidad
        txt_penalidad = f'La penalidad es de {penalidad}'
        txt_total_dinero = f'El total de dinero a retirar es {total_dinero}'
        return txt_penalidad+'\n'+txt_total_dinero
    else:
        valor_interes = (dinero * porcentaje * tiempo) / 12
        total_dinero = dinero + valor_interes
        txt_intereses = f'El valor de los intereses es de {valor_interes}'
        txt_total_dinero = f'El total de dinero a retirar es {total_dinero}'
        return txt_intereses+'\n'+txt_total_dinero

print(CDT(1000000, 20,6))
