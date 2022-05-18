#2 Calcule los intereses de un cdt ->(cantidad*porcentaje*tiempo)/12



def calculoIntereses(cantidad:int, porcentaje:float, tiempo:int):
    #Calcula los intereses para un periodo de tiempo de 3 meses
    conversion = porcentaje / 100
    intereses = (cantidad * porcentaje * tiempo)/12
    print(intereses)

calculoIntereses(10000, 19, 3)