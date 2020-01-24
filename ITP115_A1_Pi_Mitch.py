# Mitch Pi, mpi@usc.edu
# ITP 115, Spring 2020
# Assignment 1
# Description:
#This program asks for user input and
#creates a a mad libs style story from the user's inputs

#collects user inputs for story, only checks if verb1 ends with an "ing"
verb1 = input("Enter a verb that ends with ing: ")
#checks if the input for verb1 ends with ing
while not verb1.endswith ("ing"):
    verb1 = input("Please enter a verb that ends with ing: ")

friend1 = input("Enter the name of a friend: ")

adj1 = input ("Enter an adjective to describe your friend: ")

appreciate1 = input ("Enter a trait you appreciate about your friend: ")

school1 = input ("Enter the school your friend goes to: ")

#Uses try except to check if user input can be converted into float, takes user input if True
time = (input ("Enter a number that contains a decimal: "))
timeIsFloat = False
while timeIsFloat is False:
    try:
        float(time)
        timeIsFloat = True
    except ValueError:
        time = (input("Please Enter a number that contains a decimal: "))

#Uses try except to check if user input can be converted into int, takes user input if True
int1 = input ("Now enter a integer: ")
isInt1 = False
while isInt1 is False:
    try:
        int(int1)
        isInt1 = True
    except ValueError:
        int1 = input("Please enter a integer: ")

int2 = input ("And another integer: ")
isInt2 = False
while isInt2 is False:
    try:
        int(int2)
        isInt2 = True
    except ValueError:
        int2 = input("Please enter a integer: ")

int3 = input ("And one last integer: ")
isInt3 = False
while isInt3 is False:
    try:
        int(int3)
        isInt3 = True
    except ValueError:
        int3 = input("Please enter a integer: ")

#finally converts the inputs for numbers into actual numbers in case I need to do math
timeReal = float(time)
int1Real = int(int1)
int2Real = int(int2)
int3Real = int(int3)

#math equation, division sign returns float value so I'm okay with using integers in the equation
mathnum = (int1Real+int2Real)/2+3

#converts the inputs from the floats and numbers back into strings just in case 
storynum2 = str(timeReal)
storynum = str(mathnum)
storynum3 = str(int3Real)

#prints the story using user inputs
print("Today you are "+"\'"+verb1+"\'"" with your very " "\'"+adj1+"\'"" friend "+"\'"+friend1+"\'.")
print( "You appreciate how they are "+"\'"+appreciate1+"\'.")
print("The two of you have been friends for " +"\'"+storynum+"\'"+" years and you have been " +"\'"+verb1+"\'"+" for "+"\'"+storynum2+"\'"+" hours." )
print("\'"+friend1+"\'"+" has been a student at "+"\'"+ school1+"\'"+" for "+"\'"+storynum3+"\'"+" year(s).")
print("You two had fun spending time with each other. The end.")
