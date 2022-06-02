#Import Jahr + Umwandlung in int()
import datetime

#Import Wochentag
import calendar 
  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d.%m.%Y').weekday() 
    return (calendar.day_name[born])

# Umstellung auf Deutsch:
import locale
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

#Initialisierung Schleife
fehler=1

#Schleife
while fehler==1:

#Weiterführende Frage
    print('Wann ist Ihr Geburtsdatum (tt.mm.jjjj)?')
    try:
        date=input()
        fehler=0
    except:
        print('Bitte geben Sie das Geburtsdatum im gültigen Format tt.mm.jjjj. an')
        continue

print('Sie sind an einem',findDay(date),'geboren')
input()