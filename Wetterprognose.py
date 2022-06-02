# Wetterprognose

# Import
import random
random.seed

# Variable und Liste
wetter = random.randint(1,2)
print()
tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

# Tabellenkopf mit Textformatierung
print(f"{'Wochentag':<12}{'Wetter':<10}")
print('----------------------')

# Tabelle als "for-Schleife"
for i in range(7):
    wetter = random.randint(1,5)
    if wetter == 1:
        wetter = "Sonnig"
    elif wetter == 2:
        wetter = "Regen"
    elif wetter == 3:
        wetter = "Bewölkt"
    elif wetter == 4:
        wetter = "Gewitter"
    else:
        wetter = "Nebel"
        
    print(f"{tage[i]:<12}{wetter:<10}") # Formatierung der Ausgabe

input()