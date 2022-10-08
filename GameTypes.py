#from operator import le
#python from turtle import clear

#fps = ["Call of duty", "Apex Legends", "Battlefield", "Valorant", "TitanFall"]
#sandBox = ["Minecraft", "Gmod", "Terraria"]
#br = ["Fortnite", "PUBG"]
#survivalHorror = ["Resident Evil", "Silent Hill", "The Evil Within", "Dead Space"]
#oba = ["LoL", "Smite"]

#gameTypes = { "Fps": fps, "Sand Box": sandBox, "Br": br, "Survival Horror": survivalHorror, "Moba": moba }

#mainCharacters = ["Soap Mactavish", "Mirage", "Jonathan Miller", "Jett", "Ash", "Steve", "Jaro", "Steampunker", "Tfue", "DrDisrespect", "Jill Valentine", "Harry", "Sebastian", "Isaac Clarke", "Ahri", "Susano"]

#print (gameTypes["Moba"])

#for gameType in gameTypes:
    #print (gameType)
    #print (gameTypes[gameType])
    # print (gameType.values())
#for game in gameType:
     #print (game)
    #     for letters in game:
    #         print (letters)

# firstName = "Nick"
# lastName = "Yepez"

# print(firstName + " " + lastName)

#from re import S


# s = "S"
# s += "S"
# s += "S"
# s += "S"
# print (s)
# s = s[:-1]
#for a in range (1,4):
    #print (a)
    #print (s)
    # print (s)
    # print(s[:-1])
    #print(s[:-2])

# s= "S"
# s += "S"
# s += "S"
# s += "S"
# #print (s)
# for a in range (1,4):
#     print (s[:a])
# for a in range (1,4):
#     print (s[1:-a])

d = "E"
s = d
n = 322
for i in range (0,n):
    if (i == 0):
        print (s)
    else :
        s += d
        print (s)
for i in range (1,n):
    s=s[:-1]
    print (s)
