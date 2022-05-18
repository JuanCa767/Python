incremental = 0

while incremental <= 10:
    print(incremental)
    incremental += 1

#colocamos a cero otra vez el incremental
incremental = 0
while True:
    print(incremental)
    if incremental ==1000:
        #break = rompe el ciclo
        break
    incremental +=1 
    
print ('fin while 1')  

incremental = 0

while incremental != 1001:
    print(incremental)
    incremental +=1

