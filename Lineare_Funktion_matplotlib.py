#Lineare Funktion

#Ausgangslage: 1 Liter Benzin kostet CHF 2.- was zur Formel führt:
# y = Zu bezahlender Preis / x = Anzahl Liter die man tankt
#Also: y = x*2

import matplotlib.pyplot

grafik = []

for x in range(11):
    y = x*2
    grafik.append(y)
    print(y)

matplotlib.pyplot.plot(grafik)
matplotlib.pyplot.show()