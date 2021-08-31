import math
def Brutto(x):
    print("Ubezpieczenie emerytalne - ",float(x)*9.76/100, " zl\n")
    print("Ubezpieczenie rentowe - ",float(x)*1.5/100, " zl\n")
    print("Ubezpieczenie chorobowe - ",float(x)*2.45/100, " zl\n")
    print("Ubezpieczenie zdrowotne - ",float(x)*7.77/100, " zl\n")
    print("Zaliczka na PIT - ",float(x)*4.89/100, " zl\n")
    print("Kwota netto - ",float(x)*73.63/100, " zl\n")
    return "Koniec"

def Netto(y):
    c=float(y)*100/73.63
    print("Ubezpieczenie emerytalne - ",float(c)*9.76/100, " zl\n")
    print("Ubezpieczenie rentowe - ",float(c)*1.5/100, " zl\n")
    print("Ubezpieczenie chorobowe - ",float(c)*2.45/100, " zl\n")
    print("Ubezpieczenie zdrowotne - ",float(c)*7.77/100, " zl\n")
    print("Zaliczka na PIT - ",float(c)*4.89/100, " zl\n")
    print("Kwota brutto - ",float(c), " zl\n")
    return "Koniec"

a=input("Wybierz typ kwoty, ktora chcesz podac. 1 - brutto. 2 - netto ")
if a=="1":
    x=input("Podaj twoje wynagrodzenie w brutto ")
    print(Brutto(x))
if a=="2":
    y=input("Podaj twoje wynagrodzenie w netto ")
    print(Netto(y))
if a!="1" and a!="2":
    print("Podales niepoprawny znak ")
