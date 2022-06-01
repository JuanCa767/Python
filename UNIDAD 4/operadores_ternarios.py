
nombres=['juan','Jaime','Pedro','camilo','dayana','maria']
#list comprenhention -------------------------------------------------------------------------
respuesta = [n.upper() if n[0].lower()=='j' else n.lower() for n in nombres]
#print(respuesta)

#funcion normal ------------------------------------------------------------------------------
lista = []
for n in nombres:
    if n[0].lower()=='j':
        lista.append(n.upper())
    else:
        lista.append(n.lower())

#print(lista)

#--------------------------------------------------------------------------------------------
funcion = lambda lista_nombres:[n.upper() if n[0].lower()=='j' else n.lower() for n in lista_nombres]
#print(funcion(nombres))
