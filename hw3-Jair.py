# Build a tool that allows a user to convert Celsius to Fahrenheit or Fahrenheit to Celsiu
#(32 °F − 32) × 5/9 = 0 °C 
# 	print(add(a, b))
# personsName = raw_input("What is your name? ")
# causesName = raw_input("What is the causes you're interested in? ")
# nEvents = input("How many events have you participated in for this event? ")
# if (z == "A"):
# elif (z == "S"):
# else:
# 	print("Sorry you did not make a seleciton properly")
def convertCelsiusToFaherenheint (Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit
#print (convertCelsiusToFaherenheint (37))

def convertFaherenheintToCelcius (Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5/9
    return Celsius
#print (convertFaherenheintToCelcius (98.6))

temperatureType = input("What do you whant to convert Celsius or Faherenheint? (\"C\" for Celsisus or \"F\" for Faherenheint)")

if (temperatureType == "C"):
    celsiusValue = float(input("Whats the value that you need to convert?"))
    print (convertCelsiusToFaherenheint (celsiusValue))

elif (temperatureType == "F"):
    faherenheintValue = float(input("Whats the value that you need to convert?"))
    print (convertFaherenheintToCelcius (faherenheintValue))

else:
    print("Sorry you didn't select Celsius or Frenheint")