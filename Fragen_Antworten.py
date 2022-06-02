#Fragen_Antworten

print('Wie ist dein Name?')
name=input()

print('Wie alt bist du?')
alter=int(input())
pansion = 65 - alter

print('Wo wohnst du?')
wohn=input()

print('''Arbeitest du, dann wähle 1
studierst du, dann wähle 2''')
arbeit=int(input())

#Ausgabe

if arbeit==1:
    print('Das machst du gut '+name+'. In '+str(pansion)+' Jahren wirst du pensioniert.')
else:
    print('Du kommst also aus '+wohn+' und bist am studieren - super!')