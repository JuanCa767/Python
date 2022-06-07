from numpy import random as r
guion = lambda: print('----------------------------------------------------')
participantes = ['Jorge','Juan','Andrea','Camilo','Jaime','Alejandra','Alfonso','Paola']

#ganadores = r.choice(participantes,size=[2])
ganadores = r.choice(participantes, size=[2], p=[0.1,0.1,0.3,0.1,0.1,0.1,0.1,0.1], replace=False)
print('Ganadores del viaje ', ganadores)

r.shuffle(participantes)
print(participantes)

