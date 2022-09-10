def add ( a, b):
    return a + b

def mult ( a, b):
	return a * b

def mult ( a, b):
	return a * b

def div ( a, b):
	return a / b

def subtraction ( a, b ):
	return a - b
# a = 75 
# def isJairHappy(a):
# 	if a >= 75:
# 		return True
# 	else: 
# 		return False


# JairHappinessIndex = 75

# if (isJairHappy(JairHappinessIndex)):
# 	print ("Jair is Happy")

# else:
# 	print ("Jair is not happy")

studentName = "Laura"

print( studentName + " is a student")

# f(x) = x + 1

# f(2) = 2 + 1 = 3

# OscarsScore = 7

# grade = "Passing" if OscarsScore > 7 else "Failing"

# print (grade)

# if ( a > 10):
# 	print ("a is greater than 12")
# 	print ("YAY!!!")
# elif ( a > 16):
# 	print ("a is greater than 16")
# elif( a > 4 and a < 8):
# 	print ("a is greater than four but less than 8")
# else:
# 	print("a is less than 10")
# 	print("Yay!")

# z = raw_input ("What operation do you want to run? A for (Add), S for (subtraction), M for (Multiplicatin), D for (division): ")
# a = raw_input ("What is the first operand you want to add?")
# b = raw_input ("what is the second operand you want to add?")


# if (z == "A"):
# 	print(add(a, b))
# elif (z == "S"):
# 	print(subtraction(a, b))
# elif (z == "M"):
# 	print(mult(a,b))
# elif (z == "D"):
# 	print(div(a,b))
# else:
# 	print("Sorry you did not make a seleciton properly")

#a = "Hello"
#b = "World"

# print (add(a,b))
# print (mult(a,b))
# print (div(a, b))
# print (subtraction(a, b))

#Primitive Datatypes [Consideration: Size and Type]

##Whole Numbers (Java)
#integer: expressed as int ( Negative or positive WHOLE numbers) (4 bytes-> 32 bits -> 2^32 : -2,147,483,648 to 2,147,483,647)
#long integer: expressed as long ( Negative or positive WHOLE numbers) ( 8 bytes -> 64 bits -> 2^64 : -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
#unsigned integer: expressed as unsigned int ( POSITIVE WHOLE NUMBERS) (4 bytes: 0 to 4,294,967,295 )
#unsigned long: expressed as unsigned long ( POSITIVE WHOLE NUMBERS ) ( 8 bytes: 0 to 18,446,744,073,709,551,616)
##Decimals 
#floating point (float)
#double
##Letters & Symbols
# character: char
# string of characters: String
##Logical Values
#boolean 2^1 = 2 = 0,  1

#Operators
##Relational
##Logical
##Functional
# Conditional Operator: expressed as if-else


# I want to know if someone is active in a specific cause
# I need to know the person's name
# I need to know the Cause name we're trying to figure out
# and whether the person is active based on how many events they've participated in
# for that cause. Active is participating in more than 2 events. 

# personsName = raw_input("What is your name? ")
# causesName = raw_input("What is the causes you're interested in? ")
# nEvents = input("How many events have you participated in for this event? ")


# if (nEvents > 2):
# 	print(personsName + " you have been accepted you've participated in an adequate amount of events for " + causesName)
# else:
# 	print("Sorry, " + personsName + ", your participation in "+ causesName +" is denied because you are lacking some of the conditions required")

#Naming Restrictions
#Cannot use a keyword other than it's intention
# if = "hello"
# print(if)
#Cannot reuse defined functions two or more times
#Not true in python but true in most languages
# def printHello(self):
# 	print ("hello")

# def printHello(self):
# 	print("World")

#Naming Conventions
#CASES
#Camel Case: thisIsHowYouNameThings (Functions or Methods or Variables)
#Snake case: this_is_how_you_name_things (In older style variable names )
#Pascal case: ThisIsHowYouNameThings (Classes)
#Constants case: THIS_IS_HOW_YOU_NAME_THINGS ( Constants)
#SEMANTIC MEANING
####BAD PRACTICE TO HAVE NON-DESCRIPTIVE NAMES#####
## BAD ##
def bo():
	r=1
	b=2
	return r * b
## GOOD ##
def areaOfBookshelf():
	length = 1
	width = 2
	return length * width
# print (areaOfBookshelf())
# Syntax vs Semantics
# Syntax error because you forgot the colon after the function definition
# def areaOfBookshelf()
# 	length = 1
# 	width = 2
# 	return length * width
# print (areaOfBookshelf())
# 
# Semantic Error
# Because you're adding instead of multiplying for the area. Not the intended outcome
# def areaOfBookshelf():
# 	length = 1
# 	width = 2
# 	return length + width
# print (areaOfBookshelf())

# Build a tool that allows a user to convert Celsius to Fahrenheit or Fahrenheit to Celsius
# def celsiusToFahrenheit(C):
# 	return ((C*1.8)+32)
# #print (celsiusToFahrenheit(30))
# def fahrenheitToCelsius(F):
# 	return (F-32)*0.5556
# #print (fahrenheitToCelsius(86))
# temperatureType = raw_input("What temperature type do you want to convert to? ('F' for Fahrenheit or 'C' for Celsius) ")
# if (temperatureType == "C"):
# 	celsiusDegrees = input("What's the temperature?")
# 	print (celsiusToFahrenheit(celsiusDegrees))
	
# elif (temperatureType == "F"):
# 	fahrenheitDegrees = input("What's the temperature?")
# 	print (fahrenheitToCelsius(fahrenheitDegrees))
# else: 
# 	print('You can only choose between "C" and "F"')


# Convention vs Syntax 





# Convention vs Configuration


#Data Structures
#Array is a [Linear] collection of values of the same type (homogeneous)
#Java
#public int Bookpages [10] = [23, 407, 33] #of the ten spaces available you've used 3
#zero based indexing
#System.out.print(Bookpages[1]); #print out 407
#Null Pointer Exception or ArrayOutBoundsException

#List is a [Linear] collection of values of any type (non-homogeneous)
#Python 
Hello = ['hair', 37, 't', 3.14, True ]
print (Hello)
print (Hello[4])
Hello[4] = "WASSSUP"
print (Hello[4])
# print (Hello[5]) #wont work
Hello.append("Blitz")
print (Hello[5]) #does work because you've appended an element to array

Trello = []
Trello.append("world")
print (Trello[0])

world = "h"
world = 123
# world.append("Hello") #wont work because the variable is defined as an integer not an array

print (world)

print ( 1 in Hello ) #False
print ( 37 in Hello ) #true

breadListByCountry = [ ['Focaccia', 'Crostini'], ['Baguette', 'Croissant'], ['Kaiser']]

print (breadListByCountry[2])

print (" I want the french bread : " + breadListByCountry[1][1])

#Set, Map, Dictionary 
setTest = {"hello", 12, "2", 12 } #length 3 because 12 is repeated and sets only carry unique values
print ( setTest)
print ( len(setTest)) 
# print ( setTest[1]) #wont work
print ( "hello" in setTest) 
#dictionaries and maps are key, value Pairs
dictionaryTest = { "hello": "world", "Student": "Laura", "hello": "Laura"}
print ( dictionaryTest.keys())
print (dictionaryTest["hello"])
print ("================")



counter = 1

for i in Hello:
	print (counter)
	counter += 1
	print (i)


