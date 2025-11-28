# Llògica del joc (funcions)

# Llibreries/Importacions

from time import sleep
from robot import robot

# Variables

# Funcions
def janken():
# MODE PARTIDA JANKEN
    
    print ("    QUIN TIPUS DE MODALITAT VOLS JUGAR?"    )
    print ("")
    print ("1 --> EL PRIMER QUE ARRIBI 3 VICTORIES")
    print ("2 --> EL MILLOR DE 5 RONDES")
    print ("S --> SORTIR I TORNAR AL MENÙ PRINCIPAL")
    print ("")
    sleep(1)
    
    mode = input ("TRIA '1', '2' O 'S': ")
    mode = mode.upper()
    flag = 1

    while flag == 1:
        match mode: 
            case '1':
                victories_max = 3
                print ("EL MODE ESCOLLIT ÉS EL PRIMER QUE ARRIBI A 3 VICTÒRIES")
                print ("")
                flag=0
            case '2':
                rondes_max = 5
                print ("EL MODE ESCOLLIT ÉS EL MILLOR DE 5 RONDES")
                print ("")
                flag=0
            case 'S':
                print("SORTINT DEL JOC")
                flag = 0

            case _:
                print("OPCIÓ INCORRECTA. SI US PLAU, INTRODUEIX '1', '2' o 'S'.")
                mode = input ("TRIA '1', '2' O 'S': ")
    
    
# VARIABLES PER A LA PUNTUACIÓ
    puntuacio_usr = 0
    puntuacio_robot = 0
    ronda_actual = 0
    flag2 = 1

# VUCLE JUGADA    
    while flag2 == 1:

# ENTRADA USUARI
        op_jugador = input("PEDRA, PAPER O TISORA? O SORTIR --> S: ")
        op_jugador = op_jugador.upper()
       
        if (op_jugador == "PEDRA") | (op_jugador == "PAPER") | (op_jugador == "TISORA"):

# ENTRADA ROBOT       
            r = robot()
            jugada_robot = r.playing()
            print ("EL ROBOT HA ESCOLLIT: ", jugada_robot)
            sleep(1)

# CONDICIO SI ES UNA COSA PASA UNA ALTRA
        match op_jugador:
            case "PEDRA":
                if jugada_robot == "pedra":
                    print ("EMPAT")
                elif jugada_robot == "paper":
                    puntuacio_robot+=1
                    print (f"ROBOT GUANYA +1 PUNT: PORTA {puntuacio_robot} PUNTS")
                elif jugada_robot == "tisora":
                    puntuacio_usr +=1
                    print (f"HAS GUANYAT +1 PUNT: PORTES {puntuacio_usr} PUNTS")
                sleep(2)


            case "PAPER":
                if jugada_robot == "pedra":
                    puntuacio_usr +=1
                    print (f"HAS GUANYAT +1 PUNT: PORTES {puntuacio_usr} PUNTS")
                elif jugada_robot == "tisora":
                    puntuacio_robot+=1
                    print (f"ROBOT GUANYA +1 PUNT: PORTA {puntuacio_robot} PUNTS")
                elif jugada_robot == "paper":
                    print ("EMPAT")
                sleep(2)


            case "TISORA":
                if jugada_robot == "pedra":
                    puntuacio_robot+=1
                    print (f"ROBOT GUANYA +1 PUNT: PORTA {puntuacio_robot} PUNTS")
                elif jugada_robot == "paper":
                    puntuacio_usr +=1
                    print (f"HAS GUANYAT +1 PUNT: PORTES {puntuacio_usr} PUNTS")
                elif jugada_robot == "tisora":
                    print ("EMPAT")
                sleep(2)

            case "S":
                print ("GRÀCIES PER JUGAR")
                sleep(2)
                flag2 = 0

            case _:
                print ("MMMM, TRIA UNA OPCIÓ CORRECTA")
                sleep(2)

        print (f"PORTEU {ronda_actual} RONDES")
        print (f"PUNTUACIÓ: TÚ {puntuacio_usr} - {puntuacio_robot} ROBOT")

# GESTIÓ DE RONDES
# JOC MILLOR DE 3 VIICTORIES
    
        ronda_actual += 1
        if mode == "1":
            if puntuacio_usr == victories_max:
                print ("HAS GUANYAT EL JOC")
                flag2 = 0
            if puntuacio_robot == victories_max:
                print ("EL ROBOT HA GUANYAT EL JOC")
                flag2 = 0

# JOC EL MILLOR DE 5 RONDES
       
        if ronda_actual >=5 and mode == "2":
            flag2 = 0
            if puntuacio_usr > puntuacio_robot:
                print("HAS GUANYAT LA PARTIDA")
            
            elif puntuacio_robot > puntuacio_usr:
                print("EL ROBOT HA GUANYAT LA PARTIDA")
            
            else:
                print ("EMPAT")

# GUANYADOR DEFINITIU
    