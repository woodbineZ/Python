import datetime
from datetime import date
import calendar
def jakiDzien():
    dzis=datetime.datetime.today()
    wczoraj=datetime.datetime.today()-datetime.timedelta(days=1)
    jutro=datetime.datetime.today()+datetime.timedelta(days=1)
    print("Dzisiaj jest: ",str(dzis),"\nJutro bedzie: ",str(jutro),"\nWczoraj byl: ",str(wczoraj))

def kiedyWielkanoc(rok):
    a = rok % 19
    b = rok // 100
    c = rok % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return date(rok, month, day)

def kiedyUrodziny():
    rok=input("Podaj rok twoich narodzin ")
    miesiac=input("Podaj miesiac twoich narodzin (1-12) ")
    dzien=input("Podaj dzien twoich narodzin ")
    x=calendar.weekday(int(rok),int(miesiac),int(dzien))
    if x==0: print("Urodziles sie w poniedzialek!")
    elif x==1: print("Urodziles sie we wtorek!")
    elif x==2: print("Urodziles sie w srode!")
    elif x==3: print("Urodziles sie w czwartek!")
    elif x==4: print("Urodziles sie w piatek!")
    elif x==5: print("Urodziles sie w sobote!")
    elif x==6: print("Urodziles sie w niedziele!")

jakiDzien()
easter=input("Podaj rok, w ktorym chcesz sprawdzic date Wielkanocy ")
print("Wielkanoc wypadnie: ",kiedyWielkanoc(int(easter)))
kiedyUrodziny()
