#dagen_van_de_week=["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]


#for x in dagen_van_de_week:
#    print(x[0]+x[1])


namen=[]

def toevegennamen(name):
    i = input("wil je een naam toevoegen. y/n \n")
    if i == "y":
        r = input('welke naam wil je toevoegen?\n')
        namen.append(r)
        return toevegennamen(name)
    elif i == 'n':
        print ('oke ik stop met namen toetevoegen.\n')
    else: 
        print ("gelieven y/n intevoeren.")
        return toevegennamen(name)


toevegennamen(namen)

x = input ('wil je de namen afgekort hebben? y/n \n')
if x == "y":
    print ("dit zijn de namen die je hebt ingevoerd maar afgekort.\n")
    for q in namen:
        print(q[0]+q[1])
elif x == 'n':
    print(f'dit zijn al de namen{namen}')
else:
    print(f'dit heb ik niet gevraagt dus geef ik de namen volledig. {namen}')

