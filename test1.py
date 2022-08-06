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

##Whole Numbers
#integer: expressed as int ( Negative or positive WHOLE numbers) (4 bytes: -2,147,483,648 to 2,147,483,647)
#long integer: expressed as long ( Negative or positive WHOLE numbers) ( 8 bytes: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
#unsigned integer: expressed as unsigned int ( POSITIVE WHOLE NUMBERS) (4 bytes: 0 to 4,294,967,295 )
#unsigned long: expressed as unsigned long ( POSITIVE WHOLE NUMBERS ) ( 8 bytes: 0 to 18,446,744,073,709,551,616)
##Decimals 
#floating point (float)
#double
##Letters & Symbols
# character: char
# string of characters: String
##Logical Values
#boolean

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

this_is_your_number = "8"

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

# Build a tool that converts Celsius to Fahrenheit or Fahrenheit to Celsius
def celsiusToFahrenheit(C):
	return ((C*1.8)+32)
#print (celsiusToFahrenheit(30))
def fahrenheitToCelsius(F):
	return (F-32)*0.5556
#print (fahrenheitToCelsius(86))
temperatureType = raw_input("What temperature type do you want to convert to? ('F' for Fahrenheit or 'C' for Celsius) ")
if (temperatureType == "C"):
	celsiusDegrees = input("What's the temperature?")
	print (celsiusToFahrenheit(celsiusDegrees))
	
elif (temperatureType == "F"):
	fahrenheitDegrees = input("What's the temperature?")
	print (fahrenheitToCelsius(fahrenheitDegrees))
else: 
	print('You can only choose between "C" and "F"')


# Convention vs Syntax 





# Convention vs Configuration



