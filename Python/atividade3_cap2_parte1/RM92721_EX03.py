voto1 = input("Digite o seu voto: P para Playstation, X para XBOX e N para NINTENDO ")
voto2 = input("Digite o seu voto: P para Playstation, X para XBOX e N para NINTENDO ")
voto3 = input("Digite o seu voto: P para Playstation, X para XBOX e N para NINTENDO ")
voto4 = input("Digite o seu voto: P para Playstation, X para XBOX e N para NINTENDO ")
voto5 = input("Digite o seu voto: P para Playstation, X para XBOX e N para NINTENDO ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "P":
    playstation = playstation + 1
elif voto1.upper() == "X":
    xbox = xbox + 1
elif voto1.upper() == "N":
    nintendo = nintendo + 1

if voto2.upper() == "P":
    playstation = playstation + 1
elif voto2.upper() == "X":
    xbox = xbox + 1
elif voto2.upper() == "N":
    nintendo = nintendo + 1

if voto3.upper() == "P":
    playstation = playstation + 1
elif voto3.upper() == "X":
    xbox = xbox + 1
elif voto3.upper() == "N":
    nintendo = nintendo + 1

if voto4.upper() == "P":
    playstation = playstation + 1
elif voto4.upper() == "X":
    xbox = xbox + 1
elif voto4.upper() == "N":
    nintendo = nintendo + 1

if voto5.upper() == "P":
    playstation = playstation + 1
elif voto5.upper() == "X":
    xbox = xbox + 1
elif voto5.upper() == "N":
    nintendo = nintendo + 1

if (playstation > xbox) and (playstation > nintendo):
    print("O console escolhido foi o PLAYSTATION, com {} votos.".format(playstation))
elif (xbox > playstation) and (xbox > nintendo):
    print("O console escolhido foi o XBOX, com {} votos.".format(xbox))
elif (nintendo > playstation) and (nintendo > xbox):
    print("O console escolhido foi o NINTENDO, com {} votos.".format(nintendo))
else:
    print("Empatou. Votem novamente")