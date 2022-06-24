# Import matplot als plt
import matplotlib.pyplot as plt

# Eröffnung und Festlegung der Listen für die beiden Kurse
kurs1 = []
kurs2 = []

# Kurse aus der .txt Datei auslesen, beim Leerschlag splitten, in float umwandeln und in die vorgefertigten Listen (kurs1 + kurs2) einfügen
with open('Wechselkurse.txt') as f:
    for wechselkurse in f:
        x, y = wechselkurse.split(" ")
        x = float(x)
        y = float(y)
        kurs1.append(x)
        kurs2.append(y)

# Eine Liste für 25 Tage generieren und befüllen
tag = []
for tage in range(1, 26):
    z = float(tage)
    tag.append(z)

# matplotlib erstellen und mit den Listen befüllen + ausgeben
fig, ax = plt.subplots()
ax.plot(tag, kurs1, lw=1, label='Kurs 1', color='red')
ax.plot(tag, kurs2, lw=1, label='Kurs 2', color='blue')
ax.legend()
plt.show()