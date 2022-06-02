#Tabelle mit Verbindungsmaterial erstellen

#Import
import random

#Variables
description = "screw nut washer".split()
material = "galvanised V2A V4A".split()

print()
print("Quantity Description Dimensions Material")
print()

#loop
for fasteningMaterial in range(22):

    #shuffle
    random.shuffle(description)
    random.shuffle(material)

    #variables
    quantity = random.randint(1, 100)
    width = random.randrange(6, 20, 2)
    lenght = random.randrange(10,100, 5)

    #output
          
    print("{}\t {}\t     M{}x{}\t{}".format(quantity, description[0], width, lenght, material[0]))

input()