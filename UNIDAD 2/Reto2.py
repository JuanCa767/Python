informacion = {
    'id_cliente' : 1,
    'nombre': 'Juan',
    'edad' :3,
    'primer_ingreso' : True
}

def cliente (informacion: dict):
    diccionario = {}
    diccionario ['apto'] = True
    if informacion['edad'] > 18:
        diccionario['atraccion'] = 'X- Treme'
        diccionario['valorBoleta'] = 20000
        if informacion ['primer_ingreso'] == True:
            diccionario['valorBoleta']  -= diccionario['valorBoleta'] * 0.05
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        diccionario['atraccion'] = 'Carroschocones'
        diccionario['valorBoleta'] = 5000
        if informacion ['primer_ingreso'] == True:
            diccionario['valorBoleta']  -= diccionario['valorBoleta'] * 0.07
    elif informacion['edad'] >= 7 and informacion['edad'] <= 15:
        diccionario['atraccion'] = 'Sillas voladoras'
        diccionario['valorBoleta'] = 10000
        if informacion ['primer_ingreso'] == True:
            diccionario['valorBoleta']  -= diccionario['valorBoleta'] * 0.05
    else:
        diccionario['apto'] = False
        diccionario['atraccion'] = 'N/A'
        diccionario['valorBoleta'] = 'N/A'
        
    dictEnd = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 
    diccionario['atraccion'], 'apto': diccionario['apto'], 
    'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': diccionario['valorBoleta']}
    
    return dictEnd

print(cliente(informacion))