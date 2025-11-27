# Llibreries 
from time import sleep
from jocs import janken


# Variables


# Funcions



# Menú principal i el bucle de l'aplicació

flag = 1
    
while flag == 1:
            print ("    BENVINGUT/DA AL MINI ARCADE"    )
            print ("")
            print ("1 -> Jugar a Pedra, Paper o Tisora")
            print ("2 -> Jugar a Endevinar Número")
            print ("S -> Sortir")
            print ("")
            sleep(2)

            opcio = input("A QUIN JOC VOLS JUGAR?: ")
            opcio = opcio.upper()
        
            match opcio:
                case "1":
                    janken()
                case "2":
                    print
                case "S":
                    print("GRÀCIES PER JUGAR, FINS LA PRÒXIMA!")
                    flag = 0
                case _:
                    print("NO ESCRIGUIS CAP ALTRA OPCIÓ QUE NO SIGUI 1, 2 O S")
            sleep(2)