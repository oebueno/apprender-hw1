


myUniversities = [ "ute", "uce", "utn" ]
publicUniversities = [ "uce", "ups", "ug" ]
privateUniversities = [ "usfq", "utpl" ]
universityTypes = {"public": publicUniversities, "private": privateUniversities}
# print (publicUniversities [1])
# print (universityTypes ["private"])
# print (universityTypes["public"])
#print (universityTypes)
#print (myUniversities)
chooseprorty = 1

# for university in myUniversities:
#     #print (chooseprorty)
#     #print (university)
#     print ("This is my " + str (chooseprorty) + " choise: " + university)
#     chooseprorty +=1
#     for letters in university:
#         print (letters)

for universitiesByType in universityTypes:
    print (universitiesByType)#1.-public 2.- private
    for universities in universityTypes[universitiesByType]:#valor de public university list, private list
        print (universities)#1.- uce 2.- usfq
# for universities in universityTypes["private"]:
#     print (universities)
# print (privateUniversities[0])
# print (universityTypes["private"][1])