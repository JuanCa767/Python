
#lista vacia

#mi lista
miLista=['juan',20,True]

print(miLista)

primer_elelento = miLista[0]
print(primer_elelento)

segundo_elelento = miLista[1]
print(segundo_elelento)

tercer_elelento = miLista[2]
print(tercer_elelento)


#Actualizar valores de una lista
miLista[0]="Jaime"
print(miLista)

miLista[1]="Ana Maria"
print(miLista)

miLista[2]=10
print(miLista)


#Añadir elementos  a la lista se usa la funcion .append
miLista.append("jhno")
print(miLista)

miLista.append("Maria")
print(miLista)

#Eliminar elementos de una lista
miLista.pop()
print(miLista)
