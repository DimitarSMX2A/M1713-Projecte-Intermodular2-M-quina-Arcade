# Llògica del joc (funcions)

# Llibreries/Importacions

from time import sleep
from robot import robot

# Variables

# Funcions

# def menu_janken():
#while tipus_joc == 1:
#       print ("    QUIN TIPUS DE MODALITAT VOLS JUGAR?"    )
#       print ("")
#       print ("1 --> EL PRIMER DE 3 VICTORIES?")
#       print ("2 --> EL PRIMER QUE ARRIBI 5 VEGADES?")
#       print ("S --> SORTIR I TORNAR AL MENÙ PRINCIPAL")
#            sleep(2)
   
#    tipus_joc = input("QUIN TIPUS DE MODALITAT VOLS JUGAR?: ")
#    tipus_joc = tipus_joc.upper()

#   match tipus_joc:
#      case "1":
#         print
#      case "2":
#         print
#      case _:
#         print



def janken():
    opcions = ["PEDRA, PAPER, TISORA, S"]
    flag_ronda = 1
    contador_jugador = 0
    contador_r = 0

    while flag_ronda == 1:
        
        op_jugador = input("PEDRA, PAPER O TISORA? O SORTIR --> S: ")
        op_jugador = op_jugador.upper()
       

        if (op_jugador == "PEDRA") | (op_jugador == "PAPER") | (op_jugador == "TISORA") | (op_jugador == "S"):
            r = robot()
            jugada_robot = r.playing()
            print ("EL ROBOT HA ESCOLLIT: ", jugada_robot)
            sleep(1)

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
                flag_ronda = 0
                sleep(2)

            case _:
                print ("MMMM, TRIA UNA OPCIÓ CORRECTA")
                sleep(2)
