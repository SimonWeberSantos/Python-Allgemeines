#Tabelle mit Verbindungsmaterial erstellen

#Import
import random

#Variables
description = "screw nut washer".split()
material = "galvanised V2A V4A".split()

print()
print(f"{'Quantity':9}{'Description':>12}{'Dimensions':>11}{'Material':>10}")
print()

#loop
for fasteningMaterial in range(22):

    #shuffle
    random.shuffle(description)
    random.shuffle(material)

    #variables
    quantity = random.randint(1, 100)
    width = random.randrange(6, 20, 2)
    lenght = random.randrange(10,105, 5)

    #output
    print(f"{quantity:>8d}  {description[0]:12}{'M':>4}{width:2.0f}{'x':1}{lenght:>3}  {material[0]:10}")

input()
