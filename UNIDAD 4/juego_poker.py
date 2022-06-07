from numpy import random as r
#funcion para crear las cartas

def crear_baraja(id_cartas: list):
    corazones = list(map(lambda id: (id, '♥︎'), id_cartas))
    diamantes = list(map(lambda id: (id, '♦︎'), id_cartas))
    trebol = list(map(lambda id: (id, '♣︎'), id_cartas))
    picas = list(map(lambda id: (id, '♠︎'), id_cartas))
    #Unir las listas en una sola baraja
    baraja = corazones+diamantes+trebol+picas
    #Barajar cartas
    r.shuffle(baraja)
    return baraja

def repartir_cartas(baraja:list):
    carta_1 = baraja.pop()
    carta_2 = baraja.pop()

    return carta_1, carta_2



id_cartas = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
baraja = crear_baraja(id_cartas)

def jugar():
    print('----------- POCKER -----------')
    num_jugadores = int(input('Por favor ingrese el numero de jugadores: '))
    jugadores = {}
    for j in range(num_jugadores):
        jugadores[f'Jugador{j+1}'] = list(repartir_cartas(baraja))
    print(jugadores)


jugar()








misCartas = repartir_cartas(baraja)
print(misCartas)
print('\n')
print(baraja)



#print(crear_baraja(id_cartas))


