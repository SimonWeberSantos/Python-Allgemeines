#Importe
import time

#Einführungstext
print("Hallo, ich bin dein Bierbestell-Assistent. Was hättest du gerne?")
time.sleep(3)

def sonstNochWas():
    print("Möchtest du sonst noch etwas? (Ja, Nein)")
    
def zurAuswahl():
    print("Hier die Auswahl:")

def bierbestellung():

    bestellung = 0
    while bestellung <1 or bestellung >4:
        print("1 = Lager")
        print("2 = Ale")
        print("3 = Weizen")
        print("4 = Sonstiges")

        try:
            bestellung = int(input())
            if bestellung <1 or bestellung >4:
                print("Bitte eine Zahl von 1-4 eingeben")

        except:
            print("Bitte eine Zahl von 1 - 4 eingeben")
            

    #Variablen und Listen
    lager = ["Hell/Blond", "Naturtrüb", "Büchse Lager 50cl", "Lager Spez."]
    ale = ["Pale Ale", "IPA", "Red Ale", "Amber"]
    weizen = ["Weissbier", "Hefe-Weissbier", "Dunkles Weissbier"]
    sonstiges = ["Panaché", "Früchtebier", "Alkoholfrei"]

    a = 1

    #Auswahl Gruppe und Sorte


    if bestellung == 1:
        zurAuswahl()
        auswahl1 = 0
        while auswahl1 <1 or auswahl1 >4:
            for i in lager:
                print(a, "=", i)
                a += 1
            try:
                auswahl1 = int(input())
                if auswahl1 <1 or auswahl1 >4:
                    print("Bitte eine Zahl von 1-4 eingeben")
                    a = 1
            except:
                print("Bitte eine Zahl von 1-4 eingeben")
                a = 1
        if auswahl1 == 1:
            return lager[0]
        elif auswahl1 == 2:
            return lager[1]
        elif auswahl1 == 3:
            return lager[2]
        elif auswahl1 == 4:
            return lager[3]
            
    elif bestellung == 2:
        zurAuswahl()
        auswahl2 = 0
        while auswahl2 <1 or auswahl2 >4:
            for i in ale:
                print(a, "=", i)
                a += 1
            try:
                auswahl2 = int(input())
                if auswahl2 <1 or auswahl2 >4:
                    print("Bitte eine Zahl von 1-4 eingeben")
                    a = 1
            except:
                print("Bitte eine Zahl von 1-4 eingeben")
                a = 1
        if auswahl2 == 1:
            return ale[0]
        elif auswahl2 == 2:
            return ale[1]
        elif auswahl2 == 3:
            return ale[2]
        elif auswahl2 == 4:
            return ale[3]
            
    elif bestellung == 3:
        zurAuswahl()
        auswahl3 = 0
        while auswahl3 <1 or auswahl3 >3:
            for i in weizen:
                print(a, "=", i)
                a += 1
            try:
                auswahl3 = int(input())
                if auswahl3 <1 or auswahl3 >3:
                    print("Bitte eine Zahl von 1-3 eingeben")
                    a = 1
            except:
                print("Bitte eine Zahl von 1-3 eingeben")
                a = 1
        if auswahl3 == 1:
            return weizen[0]
        elif auswahl3 == 2:
            return weizen[1]
        elif auswahl3 == 3:
            return weizen[2]
            
    elif bestellung == 4:
        zurAuswahl()
        auswahl4 = 0
        while auswahl4 <1 or auswahl4 >3:
            for i in sonstiges:
                print(a, "=", i)
                a += 1
            try:
                auswahl4 = int(input())
                if auswahl4 <1 or auswahl4 >3:
                    print("Bitte eine Zahl von 1-3 eingeben")
                    a = 1
            except:
                print("Bitte eine Zahl von 1-3 eingeben")
                a = 1
        if auswahl4 == 1:
            return sonstiges[0]
        elif auswahl4 == 2:
            return sonstiges[1]
        elif auswahl4 == 3:
            return sonstiges[2]


#Programm
mehrfachbestellung = "ja"

while mehrfachbestellung != ["n", "N", "nein", "NEIN", "Nein", "NEin"]:
    bestellung1 = bierbestellung()

    sonstNochWas()
    mehrfachbestellung = input()
    if mehrfachbestellung in ["Ja", "ja", "j", "J", "JA"]:
        bestellung2 = bierbestellung()
    else:
        print("Du bekommst also:")
        print("1x", bestellung1)
        break

    sonstNochWas()
    mehrfachbestellung = input()
    if mehrfachbestellung in ["Ja", "ja", "j", "J", "JA"]:
        bestellung3 = bierbestellung()
    else:
        print("Du bekommst also:")
        print("1x", bestellung1)
        print("1x", bestellung2)
        break

    sonstNochWas()
    mehrfachbestellung = input()
    if mehrfachbestellung in ["Ja", "ja", "j", "J", "JA"]:
        bestellung4 = bierbestellung()
    else:
        print("Du bekommst also:")
        print("1x", bestellung1)
        print("1x", bestellung2)
        print("1x", bestellung3)
        break

    sonstNochWas()
    mehrfachbestellung = input()
    if mehrfachbestellung in ["Ja", "ja", "j", "J", "JA"]:
        bestellung5 = bierbestellung()
    else:
        print("Du bekommst also:")
        print("1x", bestellung1)
        print("1x", bestellung2)
        print("1x", bestellung3)
        print("1x", bestellung4)
        break

    sonstNochWas()
    mehrfachbestellung = input()
    if mehrfachbestellung in ["Ja", "ja", "j", "J", "JA"]:
        bestellung6 = bierbestellung()
        print("Du hast die max. Anzahl Artikel erreicht, welche ich tragen kann!")
        print("Du bekommst also:")
        print("1x", bestellung1)
        print("1x", bestellung2)
        print("1x", bestellung3)
        print("1x", bestellung4)
        print("1x", bestellung5)
        print("1x", bestellung6)
        break
    else:
        print("Du bekommst also:")
        print("1x", bestellung1)
        print("1x", bestellung2)
        print("1x", bestellung3)
        print("1x", bestellung4)
        print("1x", bestellung5)
        break

#Ausgabe
input("Besten Dank und Prost :-)")