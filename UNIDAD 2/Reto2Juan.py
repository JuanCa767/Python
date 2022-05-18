#funcion
def cliente(informacion:dict):
    
    if informacion['edad'] >18:
        atrac = 'X-Treme'
        aptoV = True
        valorBoleta = 20000
        if informacion['primer_ingreso']==True:
            valorBoleta = valorBoleta - valorBoleta* 0.05
    elif informacion['edad'] >=15:
        atrac = 'Carroschocones'
        aptoV = True
        valorBoleta = 5000
        if informacion['primer_ingreso']==True:
            valorBoleta = valorBoleta - valorBoleta* 0.07
    elif informacion['edad'] >=7: 
        atrac = 'Sillasvoladoras'
        aptoV = True
        valorBoleta = 10000
        if informacion['primer_ingreso']==True:
            valorBoleta = valorBoleta - valorBoleta* 0.05
    else:
        atrac = 'N/A'
        aptoV = False
        valorBoleta = 'N/A'
        
    
    #funcion de salida
    dictSalida ={
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': atrac,
        'apto': aptoV,
        'primer_ingreso':informacion['primer_ingreso'],
        'total_boleta':valorBoleta
    }
    
    return dictSalida

#Definicion del diccionario 
informacion = {
    'id_cliente': 1,
    'nombre' : 'Tatiana Ruiz',
    'edad': 20,
    'primer_ingreso': True
}

#Salida para prueba
print(cliente(informacion))

