namen = {'Simon':'Weber', 'Ester':'Santos', 'Martin':'von Siebenthal','Anna-Paula':'Rodeo', 'Köbi':'Prisling'}

splitNamen = namen.items()

vor = []
nach = []

for vorname, nachname in splitNamen:
    nach.append(nachname)
    vor.append(vorname)

print('Vor-und Nachnamen korrekt:')

a = 0
while a < len(vor):
    print(vor[a], nach[a])
    a += 1

print()
print('Vor-und Nachnamen alphabetisch sortiert')

vor = sorted(vor)
nach = sorted(nach)

a = 0
while a < len(vor):
    print(vor[a], nach[a])
    a += 1