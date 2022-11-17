import sys 

minimo = 0
maximo = 0



print ("niveles que se encuentran en el juego:")
print ("[1] Nivel principiante: entre los valores 0 y 100")
print ("[2] Nivel medio: entre los valores 0 y 1000")
print ("[3] Nivel profesional: entre los valores 0 y 1000000")
print ("[4] Nivel gamer: entre los numeros 0 y 1000000000000")

while True:
        nivel = int(input("elige nivel escribiendo 1, 2, 3 o 4:") )   

        if nivel <= 1:
                    maximo = maximo + 100 
                    intentoslim = 10
                    break
        elif nivel <= 2:
                    maximo = maximo + 1000
                    intentoslim = 25
                    break
        elif nivel <= 3:
                    maximo = maximo + 1000000
                    intentoslim = 50
                    break
        elif nivel <= 4:
                    maximo = maximo + 1000000000000
                    intentoslim = 65
                    break