# Mitch Pi, mpi@usc.edu
# ITP 115, Spring 2020
# Lab 1-1

print(" ___")
print("|   |")
print("|   |")
print("|___|")

print("You don't frighten us, English pig-dogs! \nGo and boil your bottoms, sons of a silly person! \n      -\"Monty Python and the Holy Grail\" ")
month = input("What month are we in?: ")
day = input("What day is it?: ")
date = input("What day of the month is it Today?: ")
if type(date) == int:
    intDate = int(date)
print('Today is ' + day +' '+ month +' '+ date + ' and Tomorrow will be '+ month + '' , intDate+1)
else:
print ("Please put an integer for the date")
#Program cannot tell when it will be a new month e.g: Tomorrow will be January 32 instead of February 1

