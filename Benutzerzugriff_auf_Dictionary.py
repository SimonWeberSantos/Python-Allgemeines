#Benutzerzugriff auf Dictionary

artikelstamm = {
    "100":"Banane",
    "101":"Apfel",
    "102":"Birne",
    "103":"Pfirsich",
    "104":"Orange",
    "105":"Mandarine"
    }

art = False

while art == False:
    eingabe = input("Artikelnummer eingeben: ")
    if eingabe in artikelstamm:
        art = True
    else:
        continue

print(artikelstamm[eingabe])
input()