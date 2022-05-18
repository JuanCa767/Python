'''
Desarrolle una función que calcule el valor del interes de un CDT.
    *Ganancias
    si tiempo > 2
    porcentajeInteres = 0.03
    valorIntereses= (capital * porcentajeInteres*tiempo)/12
    valorTotal = capital + valorIntereses
    
    “Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un 
    tiempo de {} meses es: {}”
    
    *Perdida
    si tiempo <=2
    valorPerder = capital * porcentajePerder
    porcentajePerder = 0.02
    valorTotal = capital - valorPerder
    
    “Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un 
    tiempo de {} meses es: {}”
    

'''

def CDT(usuario:str, capital:int, tiempo:int):
        
    #Para el caso de las ganancias
    if tiempo > 2:
        porcentajeInteres = 0.03
        valorIntereses= (capital * porcentajeInteres*tiempo)/12
        valorTotal = capital + valorIntereses        
        txt_mensaje = f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}' 
    elif tiempo <= 2: 
        porcentajePerder = 0.02
        valorPerder = capital * porcentajePerder
        valorTotal = capital - valorPerder
        txt_mensaje = f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}'
   
    return txt_mensaje
    
print(CDT("AB1012", 250000, 4))

