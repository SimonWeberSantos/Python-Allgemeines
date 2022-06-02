# Kalkulation eines Handelsbetriebes (ohne Berücksichtigung der Mehrwertsteuer)

katalogpreisLieferant = float(15687)  # <-- Wenn vorhanden hier den KATALOGPREIS DES LIEFERANTEN in CHF einfügen
rabattLieferant = float(10)  # <-- LIEFERANTENRABATT in % hier eintragen
skontoLieferant = float(5)  # <-- LIEFERANTENSKONTO in % hier eingragen
bezugskosten = float(1200)  # <-- BEZUGSKOSTEN (Transport, Zoll, etc.) hier in CHF eintragen
gemeinkosten = float(40)  # <-- GEMEINKOSTEN (Miete, Personal, Abschrieb, etc) hier in % eintragen
reingewinn = float(10)  # <-- Angestrebter REINGEWINN hier in % eintragen
skonto = float(1)  # <-- SKONTO AN KUNDEN hier in % eintragen
rabatt = float(5)  # <-- RABATT AN KUNDEN hier in % eingragen
katalogpreis = float()  # <-- Wenn vorhanden hier den KATALOGPREIS DES HANDELSBETRIEBES in CHF einfügen

def checkUserEingabe():
    if katalogpreisLieferant == 0.0 and katalogpreis == 0.0:
        return 1
    elif katalogpreisLieferant != 0.0 and katalogpreis != 0.0:
        return 2
    elif katalogpreisLieferant != 0.0 and katalogpreis == 0.0:
        return 3
    elif katalogpreis != 0.0 and katalogpreisLieferant == 0.0:
        return 4

eingabe = checkUserEingabe()

if eingabe == 1:
    input("Bitte entweder Katalogpreis des Lieferantens oder des Handelsbetriebes eingeben und Programm dann neu starten.")
elif eingabe == 2:
    input("Bitte eine der folgenden Eingaben löschen und Programm neu starten: Katalogpreis Handelsbetrieb oder Katalogpreis Lieferant")
elif eingabe == 3:
    # Berechnung der verschiedenen Stufen
    rechnungbetrag = katalogpreisLieferant*(100-rabattLieferant)/100
    einkaufspreis = rechnungbetrag*(100-skontoLieferant)/100
    einstandspreis = einkaufspreis + bezugskosten
    selbstkosten = einstandspreis*(100+gemeinkosten)/100
    nettoverkaufspreis = selbstkosten*(100+reingewinn)/100
    rechnung = nettoverkaufspreis/(100-skonto)*100
    preis = rechnung/(100-rabatt)*100

    # Ausgabe
    print()
    print(f"{'Katalogpreis Lieferanten:':<35} {round(katalogpreisLieferant, 2):>10}")
    print(f"{'Katalogpreis Minus Rabatt':<35} {round(rechnungbetrag, 2):>10}")
    print(f"{'Katalogpreis Minus Skonto':<35} {round(einkaufspreis, 2):>10}")
    print(f"{'Einstandspreis':<35} {round(einstandspreis, 2):>10}")
    print(f"{'Einstandspreis Plus Gemeinkosten':<35} {round(selbstkosten, 2):>10}")
    print(f"{'Netto Verkaufspreis':<35} {round(nettoverkaufspreis, 2):>10}")
    print(f"{'Verkaufspreis Plus Skonto':<35} {round(rechnung, 2):>10}")
    print(f"{'Katalogpreis Handelsbetrieb':<35} {round(preis, 2):>10}")
    print()

elif eingabe == 4:
    # Berechnung der verschiedenen Stufen
    kundenrechnung = katalogpreis/100*(100-rabatt)
    skontorechnung = kundenrechnung/100*(100-skonto)
    selbstkosten = skontorechnung*100/(100+reingewinn)
    einstandspreis = selbstkosten*100/(100+gemeinkosten)
    einkaufspreis = einstandspreis-bezugskosten
    rechnungbetrag = einkaufspreis/(100-skontoLieferant)*100
    listenpreis = rechnungbetrag/(100-rabattLieferant)*100

    # Ausgabe
    print()
    print(f"{'Katalogpreis Handelsbetrieb':<35} {round(katalogpreis, 2):>10}")
    print(f"{'Preis nach Abzug Rabatt':<35} {round(kundenrechnung, 2):>10}")
    print(f"{'Preis nach Abzug Skonto':<35} {round(skontorechnung, 2):>10}")
    print(f"{'Selbstkosten ohne Reingewinn':<35} {round(selbstkosten, 2):>10}")
    print(f"{'Einstandspreis':<35} {round(einstandspreis, 2):>10}")
    print(f"{'Lieferantenpreis minus Skonto':<35} {round(einkaufspreis, 2):>10}")
    print(f"{'Lieferantenpreis minus Rabatt':<35} {round(rechnungbetrag, 2):>10}")
    print(f"{'Katalogpreis Lieferant':<35} {round(listenpreis, 2):>10}")
    print()

input()