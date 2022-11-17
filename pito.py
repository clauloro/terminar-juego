import sys 
from juego import *

def juego():

    intentos=0
    minimo1=minimo
    maximo1=maximo

    valorsecreto = input(f"¿que numero quieres adivinar {minimo} y {maximo}:")
    valor = input(f"mete el numero que se encuentre entre el {minimo} y {maximo}. Si quieres una ayuda escribe -1: ")
    if valor == "-1":
        print(f"tu variable esta entre {minimo1} y {maximo1}")
        pass

    else:
        while not minimo < valor < maximo:
            print(f"tienes que escribir un numero entre {minimo} y {maximo}")
            break

        intentos = intentos + 1    
        if valorsecreto == valor: 
            print("eres un dios gamer jijijiji")
            print(f"los intentos que has utilizado {intentos}")
            nombre = input ("tu usuario")
            print(f"tabla de puntuaciones: nivel n"
                    f"{nombre} _____ {80-intentos} points.") 
            empiezadenuevomaquina= input("te atreves a volver a EMPEZAR")
            if empiezadenuevomaquina == "dale"or"si"or"oui"or"yeah":
                return juego()       
            else: 
                print("nos vemos jefe")        
        else:
            if valor<valorsecreto:
                print("demasiado pequeño")
                minimo1=valor
            if valor>valorsecreto:
                print("demasiado grande") 
                maximo1=valor 
    if intentos==intentoslim:
        print("acabaste tus intentos") 
        empiezadenuevomaquina= input("te atreves a volver a EMPEZAR")
        if empiezadenuevomaquina == "dale"or"si"or"oui"or"yeah":
                return juego()       
        else: 
                print("nos vemos jefe") 
juego()                                      

