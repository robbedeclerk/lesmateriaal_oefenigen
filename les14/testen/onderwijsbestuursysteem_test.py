from onderwijsbestuursysteem import person,student,Professor,main

class student_test(student):
    def __init__(self, voornaam, achternaam, geboortedatum, telefoonnummer , straat, stad, postcode, land,inschrijvingstatus,internationaal,vol_deel_tijds):
        super().__init__(voornaam, achternaam, geboortedatum, telefoonnummer , straat, stad, postcode, land,inschrijvingstatus,internationaal,vol_deel_tijds)




student1_test=student_test('robbe','de clerck','24/12/1998','0492849901','hoge akker 7','brasschaat','2930','belgium',3,'local','voltijds')

class Professor_test(Professor):
    def __init__(self, voornaam, achternaam, geboortedatum, telefoonnummer, straat, stad, postcode, land, salaris, courses, loonverhoging):
        super().__init__(voornaam, achternaam, geboortedatum, telefoonnummer, straat, stad, postcode, land, salaris, courses, loonverhoging)


Professor1_test=Professor_test('koen','de clerck','20/05/1974','04589654','hoge akker 7','brasschaat','2930','belgium',2500,1,0)



def test_main():
    main()