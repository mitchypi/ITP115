# Mitch Pi, mpi@usc.edu
# ITP 115, Spring 2020
# Lab 2-1
import random

#Tables for valid inputs for size and yes/no
validSize = ['s','S','m','M','l','L']
validYesNo = ['y','Y','yes','Yes','n','N','no','No']
#Table to check if user input yes or no
saidYes = ['y','Y','yes','Yes']
saidNo = ['n','N','no','No']


#asks user for coffee size and checks if input is valid
size = input("What size coffee do you want (S, M, L)?")
while size not in validSize:
    size = input("please put a valid size down (S,M,L)")
#asks user for bean type
bean = input("What type of beans / blend would you like?")

#checks if user wants a random temperature and checks for valid input
randomStatus = input ("would you like a random temperature (y/n)?")
while randomStatus not in validYesNo:
    randomStatus = input("Please answer yes or no")
#gives random temperature in case of yes
if randomStatus in saidYes:
    temp = random.randrange(33,211)
else:
#asks user for temperature input in case of no random temperature
    temp = input("What temperature would you like (in degrees fahrenheit)")

#checks if can convert temp input into float. Prompts user again in case of ValueError in Type Conversion
    tempIsNum = False
    while tempIsNum is False:
        try:
            (float(temp))
            tempIsNum = True
        except ValueError:
            temp = input("Please enter a valid number")
#converts temperature input into float
floatTemp = (float(temp))

#asks user if they want cream or not, checks with validYesNo table to see if input is valid or not
creamInput = input ("Would you like room for cream (y/n)? ")
while creamInput not in validYesNo:
    creamInput = input("Please answer yes or no")

#converts user input for size into displayed size
if size == "s" or size == "S":
    cup = "small"
elif size == "m" or size =="M":
    cup = "medium"
elif size == "l" or size =="L":
    cup = "large"
else:
    cup = "invalid size"

#Checks if drink is hot or cold, converts user temperature input into hot or cold
if floatTemp >= 90:
    feel = "hot"
elif floatTemp <90:
    feel = "iced"
else:
    feel = "invalid temp"


#takes user input for cream and checks if user wants cream or not
if creamInput in saidYes:
    creamStatus = "with cream"
elif creamInput in saidNo:
    creamStatus = "with no cream"
else:
    creamStatus = "invalid amount of cream"

#prints final message
print("You ordered a " +cup+" "+feel+" "+bean+" coffee "+creamStatus)
