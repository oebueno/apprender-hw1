from operator import le


fps = ["Call of duty", "Apex Legends", "Battlefield", "Valorant", "TitanFall"]
sandBox = ["Minecraft", "Gmod", "Terraria"]
br = ["Fortnite", "PUBG"]
survivalHorror = ["Resident Evil", "Silent Hill", "The Evil Within", "Dead Space"]
moba = ["LoL", "Smite"]

gameTypes = [ fps, sandBox, br, survivalHorror, moba ]

#print (gameTypes)

for gameType in gameTypes:
    #print (gameType)
    for game in gameType:
        #print (game)
        for letters in game:
            #print (letters)
            for i in letters:
                print (i)

