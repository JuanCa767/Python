

def cliente (informacion:dict):
    respuesta = dict()
    
    if informacion ['edad'] > 18:
        atra = 'X-Treme'
        aptoA= True
        valor_boleta= 20000
        if informacion['primer_ingreso']== True:
            valor_boleta= valor_boleta - valor_boleta * 0.05
    elif informacion['edad'] >= 15:
        atra = 'Carros chocones'
        aptoA = True
        valor_boleta= 5000
        if informacion['primer_ingreso']== True:
            valor_boleta= valor_boleta - valor_boleta * 0.07    
    elif informacion['edad'] >= 7:
        atra  = 'Sillas Voladoras'
        aptoA = True
        valor_boleta= 10000
        if informacion['primer_ingreso']== True:
            valor_boleta = valor_boleta - valor_boleta * 0.05    
    else:    
        atra = 'NA'
        aptoA = False
        valor_boleta= 'N/A'
        
    #salida
    respuesta = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': atra,
        'apto': aptoA,
        'primer_ingreso': informacion['primer_ingreso'],
        'total_boleta':valor_boleta      
    }
         
        
    return respuesta


#Definicion del diccionario 
informacion = {
    'id_cliente': 4,
    'nombre' : 'Tatiana Ruiz',
    'edad': 17,
    'primer_ingreso': False
}

#Salida para prueba
print(cliente(informacion))