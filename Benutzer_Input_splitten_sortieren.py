#String-Eingabe splitten und sortieren

#Es können beliebig viele Wörter eingegeben werden. WICHTIG!!! Der Anfangsbuchstabe
#muss entweder bei allen Wörtern gross oder klein sein, ansonsten sortiert es nicht korrekt!
print('Beliebige Anzahl Wörter eingeben:')
eingabe_wort = input()

#Wörter aufteilen
ausgabe_wort = eingabe_wort.split(' ')

#Wörter alphabetisch sortieren
ausgabe_wort.sort()

print([ausgabe_wort])

input()