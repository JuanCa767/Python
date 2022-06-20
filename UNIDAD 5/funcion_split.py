#Utilizacion del split.
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 
10:'octubre', 11:'noviembre', 12:'diciembre'}

fecha = input("Ingrese la fecha en formato dd/mm/aaaa : ")
fecha = fecha.split('/')
print(fecha[0]," del mes ", meses[int(fecha[1])], " del año ",fecha[2])
