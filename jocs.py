# Llògica del joc (funcions)

# Llibreries/Importacions

from robot import robot


# Variables

# Game = ["pedra","paper","tisora"]


# Funcions



flag_jugador = 1


def janken():
    while flag_jugador == 1:

        op_jugador = input("QUE TRIES? PEDRA, PAPER O TISORA? O SORTIR --> S: ")
        op_jugador = op_jugador.upper()
        
        r2d2 = robot()
        jugada_robot = r2d2.playing()
        print ("EL ROBOT HA ESCOLLIT:",jugada_robot)
        
        match op_jugador:
            case op_jugador:
                print