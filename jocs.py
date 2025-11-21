# Llògica del joc (funcions)

# Llibreries/Importacions

from time import sleep
from robot import robot

# Variables

# Funcions


def janken():
    opcions = ["PEDRA, PAPER, TISORA, S"]
    flag_jugada = 1

    while flag_jugada == 1:

        op_jugador = input("PEDRA, PAPER O TISORA? O SORTIR --> S: ")
        op_jugador = op_jugador.upper()
        
        match op_jugador:
            case opcions if op_jugador != opcions:
                flag_jugada == 0
            case opcions: 
                flag_jugada == 1

        r = robot()
        jugada_robot = r.playing()
        print ("EL ROBOT HA ESCOLLIT:", jugada_robot)
        sleep(2)

        match op_jugador:
            case "PEDRA":
                if jugada_robot == "pedra":
                    print ("EMPAT")
                elif jugada_robot == "paper":
                    print ("ROBOT GUANYA")
                elif jugada_robot == "tisora":
                    print ("HAS GUANYAT +1 PUNT")
                sleep(2)


            case "PAPER":
                if jugada_robot == "pedra":
                    print ("HAS GUANYAT +1 PUNT")
                elif jugada_robot == "tisora":
                    print ("ROBOT GUANYA")
                elif jugada_robot == "paper":
                    print ("EMPAT")
                sleep(2)


            case "TISORA":
                if jugada_robot == "pedra":
                    print ("ROBOT GUANYA")
                elif jugada_robot == "paper":
                    print ("HAS GUANYAT +1")
                elif jugada_robot == "tisora":
                    print ("EMPAT")
                sleep(2)
           
            case "S":
                print ("GRÀCIES PER JUGAR")
                flag_jugada = 0
                sleep(2)
            
            case _:
                print ("MMMM, TRIA UNA OPCIÓ CORRECTA")
                sleep(2)

