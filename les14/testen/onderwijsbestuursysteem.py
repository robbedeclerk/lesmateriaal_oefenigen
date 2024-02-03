

class person:
    def __init__(self,voornaam,achternaam,geboortedatum,telefoonnummer ,straat,stad,postcode,land):
        self.voornaam=voornaam
        self.achternaam=achternaam
        self.geboortedatum=geboortedatum
        self.telefoonnummer=telefoonnummer 
        self.straat=straat
        self.stad=stad
        self.postcode=postcode
        self.land=land

class student(person):
    def __init__(self, voornaam, achternaam, geboortedatum, telefoonnummer , straat, stad, postcode, land,inschrijvingstatus,internationaal,vol_deel_tijds):
        super().__init__(voornaam, achternaam, geboortedatum, telefoonnummer , straat, stad, postcode, land)
        self.inschrijvingstatus=inschrijvingstatus
        self.internationaal=internationaal
        self.vol_deel_tijds=vol_deel_tijds

class Professor(person):
    def __init__(self, voornaam, achternaam, geboortedatum, telefoonnummer , straat, stad, postcode, land,salaris,courses,loonverhoging):
        super().__init__(voornaam, achternaam, geboortedatum, telefoonnummer , straat, stad, postcode, land)
        self.salaris=salaris
        self.courses=courses
        self.loonverhoging=loonverhoging

studenten_lijst=[]
Professor_lijst=[]
python={}
math={}
fysica={}


def main():
    x=input('do you want to add a student or Professor(break to quit)\n')
    if x == 'student':
        print('i am going to need some information\n')
        naam=input('what your name')
        voornaam=naam
        achternaam=input('what your family name')
        geboortedatum=input('what your birthday,pleas give in this order(day/month/year)\n')
        telefoonnummer=input('what your phone number\n')
        straat=input('what your street name\n')
        stad=input('what your city')
        postcode=input('what your postal code\n')
        land=input('what your country')
        courses=int(input('how many courses did you sing up for?\n'))
        if courses >= 3:
            vol_deel_tijds='voltijds'
        else:
            vol_deel_tijds='deeltijds'
        if land == 'belgium':
            internationaal='locaal'
        else:
            internationaal='internationaal'
        naam=student(voornaam,achternaam,geboortedatum,telefoonnummer,straat,stad,postcode,land,courses,internationaal,vol_deel_tijds)
        studenten_lijst.append(naam)
        return main()
    elif x == 'Professor':
        print('i am going to need some information\n')
        naam=input('what your name')
        voornaam=naam
        achternaam=input('what your family name')
        geboortedatum=input('what your birthday,pleas give in this order(day/month/year)\n')
        telefoonnummer=input('what your phone number\n')
        straat=input('what your street name\n')
        stad=input('what your city')
        postcode=input('what your postal code\n')
        land=input('what your country')
        salaris=2200
        courses=int(input('how many corses do you teach?\n'))
        if courses >=3:
            y=salaris+salaris/100*5
            loonverhooging=y
        else:
            loonverhooging=0
        naam=Professor(voornaam,achternaam,geboortedatum,telefoonnummer,straat,stad,postcode,land,salaris,courses,loonverhooging)
        Professor_lijst.append(naam)
        return main()
    elif x == 'break':
        print('oke i quit')
    else:
        print('i only can add students or Professors')
        return main()


def assing_clases():
    for item in Professor_lijst[item:]:
        a=input('wil you teach python yes/no\n')
        if a=='yes':
            python.update({'teacher':item, 'course':'python', 'students':studenten_lijst})
        elif a=='no':
            pass
        a=input('wil you teach math yes/no\n')
        if a=='yes':
            math.update({'teacher':item, 'course':'math', 'students':studenten_lijst})
        elif a=='no':
            pass
        a=input('wil you teach fysica yes/no\n')
        if a=='yes':
            fysica.update({'teacher':item, 'course':'fysica', 'students':studenten_lijst})
        elif a=='no':
            pass
        Professor_lijst.pop(item)
        return assing_clases()

