class Obywatel():
    def __init__(self, imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc):
        self.imie=imie
        self.nazwisko=nazwisko
        self.ulica=ulica
        self.nr_domu=nr_domu
        self.kod_pocztowy=kod_pocztowy
        self.miejscowosc=miejscowosc
    def __repr__(self):
        return f'IMIE: {self.imie}\nNAZWISKO: {self.nazwisko}\nULICA: {self.ulica}\nNR DOMU: {self.nr_domu}\nKOD POCZTOWY: {self.kod_pocztowy}\nMIEJSCOWOSC: {self.miejscowosc}'
    @classmethod
    def wczytajDane(cls):
        dane=[]
        k=input("Ile ludzi dodajemy do zbioru danych?")
        for x in range(1,int(k)+1):
            y1=input("Podaj imie ")
            y2=input("Podaj nazwisko ")
            y3=input("Podaj ulice ")
            y4=input("Podaj numer domu ")
            y5=input("Podaj kod pocztowy ")
            y6=input("Podaj miejscowosc ")
            dane.append(Obywatel(y1,y2,y3,y4,y5,y6))
            print("Dodano\n")
        return dane
    @classmethod
    def wyswietlWizytowke(cls, data):
        print(data)
        with open('dane.txt', 'w') as file:
            for element in data:
                file.write("-------------------------------\n")
                file.write(f"{element.imie} {element.nazwisko}\n")
                file.write(f"Ul. {element.ulica} {element.nr_domu}\n")
                file.write(f"{element.kod_pocztowy} {element.miejscowosc}\n")
                file.write("-------------------------------\n")
        return "Dane znajdziesz w pliku dane.txt"

o1=Obywatel('Robert', 'Lewandowski','Anfield Road',4,'46-200','Kluczbork')
print(o1)
o2=Obywatel.wczytajDane()
o3=Obywatel.wyswietlWizytowke(o2)
print(o3)


