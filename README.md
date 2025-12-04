# Sessió 1: Creació tots els # ***fitxer/documents***.

# Sessió 2: Començar a programar el ***"cos"*** del joc # **janken**.

# Sessió 3: Continuar amb el joc # **janken**.

# Sessió 4: Finalitzar el joc # **janken**.

# Sessió 5: Començar i finalitzar el joc # **nana**


# ```***Jocs en Python: Janken i Nana***```

# Aquest repositori conté dos jocs senzills programats en Python: **Janken** (pedra-paper-tisores) i **Nana** (endevina el número). Són exercicis encaminats per a practicar conceptes bàsics de programació com bucles, condicionals, generació de nombres aleatoris, gestió d'entrades d'usuari, etc.

# ```***Descripció***```

# **Janken**: El joc clàssic de pedra-paper-tisora contra l'ordinador. Tria una opció entre pedra, paper o tisora. 

# El joc primeren ens mostra un menu per als diferents modes de partida que hi ha. Seguit, ens demana d'introduir un valor (pedra, paper o tisora). Un cop donat el valor, el robot ens dona el seu valor i llavors comença la comparació _(Condicions)_, un cop fet el proces de les condicions del valor donat de part de l'usuari i robot, ens diu el resultat depenent del mode de joc que hem escollit al principi de tot.

# **Nana**: L'ordinador pensa un número entre 1 i 100, i tu has d'endevinar-lo. Et donarà pistes _("Massa alt", "Massa baix")_ fins que l'encertis.

# El joc primer pensa el numero. Entre en un bucle i amb la funció **try**, ens demana d'introduir nosaltres un numero entre '1' i '100'. Un cop introduït el numero, passa per unes condicions **(if num_jugador < num_random)**, despres de finalitzat les condicions, si hem encertat el numero ens mostra el missatge de que l'hem encertat i el nombre d'intents que hem fet, ja que hem fet una variable per a que cada intent e vagi sumant +1. Gracies a fer-ho amb **try** ens dona la possibilitat de afegir un control d'errors amb **except ValueError**.

# ```***Com executar el ARCADE?***```

# ```1. Assegura't d'instal·lar **Python**.```
# ```2. Clona o descarrega aquest repositori.```
# ```3. Obre la terminal del teu S.O. i ves dis al directori del projecte. Executar-lo amb la comanda **python nom_arxiu.py**```
# ```4. Obre l'arxiu amb Visual Studio Code, simplement executa la terminal i segueix els pasos del exercici.```