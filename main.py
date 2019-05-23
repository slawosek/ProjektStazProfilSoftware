import csv

def pobranieListyZPliku(nazwa):
    lista = []

    with open(nazwa, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                lista.append(row)
            line_count += 1
    return lista

zawartoscPliku = pobranieListyZPliku('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv')
print(zawartoscPliku)


def sredniaDlaWojewodztwa(rok, wojewodztwo):
    sumaUczestnikow = 0
    liczbaUczestnikowDlaRocznika = {}

    for row in zawartoscPliku:
        if int(row[3]) <= rok and row[0] == wojewodztwo and row[1] == 'Przystąpiło':
            sumaUczestnikow += int(row[4])
            if row[3] in liczbaUczestnikowDlaRocznika.keys():
                liczba = int(row[4])
                liczbaUczestnikowDlaRocznika[row[0]] += liczba
            else:
                liczbaUczestnikowDlaRocznika[row[0]] = int(row[4])

    sredniaLiczbaUczestnikow = sumaUczestnikow/len(liczbaUczestnikowDlaRocznika)

    return sredniaLiczbaUczestnikow

def zdawalnosc(wojewodztwo):
    zdaliNaLata = {}
    uczestniczyliNaLata = {}

    for row in zawartoscPliku:
        if row[0] == wojewodztwo:
            if row[1] == 'Przystąpiło':
                if row[3] in uczestniczyliNaLata.keys():
                    uczestniczyliNaLata[row[3]] += int(row[4])
                else:
                    uczestniczyliNaLata[row[3]] = int(row[4])
            elif row[1] == 'zdało':
                if row[3] in zdaliNaLata.keys():
                    zdaliNaLata[row[3]] += int(row[4])
                else:
                    zdaliNaLata[row[3]] = int(row[4])


    zdawalnoscWojewodztwa = {}

    for klucz,iloscZdanych in zdaliNaLata.items():
        if klucz in uczestniczyliNaLata.keys():
            zdawalnoscWojewodztwa[klucz] = iloscZdanych/uczestniczyliNaLata[klucz]*100

    return zdawalnoscWojewodztwa

def wyswietlanieZdawalnosci(zdawalnoscWojewodztwa):
    for klucz, procentZdanych in zdawalnoscWojewodztwa.items():
        print(klucz + ": " + "{:.2f}".format(procentZdanych) + "%")

def listaWojewodztw():
    setWojewodztw = set()
    for row in zawartoscPliku:
        if row[0] != 'Polska':
            setWojewodztw.add(row[0])
    return setWojewodztw

def najlepszeWojewodztwoWRoku(rok):
    spisWojewodztw = listaWojewodztw()
    najlepszyWynik = 0
    najlepszeWojewodztwo = ''

    print(spisWojewodztw)
    for wojewodztwo in spisWojewodztw:
        slownikZdawalnosc = zdawalnosc(wojewodztwo)
        if str(rok) in slownikZdawalnosc.keys():
            zdawalnoscDlaWojewodztwa = slownikZdawalnosc[str(rok)]
            if zdawalnoscDlaWojewodztwa > najlepszyWynik:
                najlepszyWynik = zdawalnoscDlaWojewodztwa
                najlepszeWojewodztwo = wojewodztwo

    return najlepszeWojewodztwo

def wyswietlanieNajlepszeWojewodztwo(rok):
    print(str(rok) + " - " + najlepszeWojewodztwoWRoku(rok))

def najstarszyRocznik():
    najstarszyrocznik = 3000 #Przyjmuję jako dostatecznie oddaloną zmienną
    for row in zawartoscPliku:
        if int(row[3]) < najstarszyrocznik:
            najstarszyrocznik = int(row[3])
    return najstarszyrocznik


def wykrywanieRegresji():
    spisWojewodztw = listaWojewodztw()
    najstarszyrocznik = najstarszyRocznik()

    for wojewodztwo in spisWojewodztw:
        slownikZdawalnosc = zdawalnosc(wojewodztwo)
        for rok, procenty in slownikZdawalnosc.items():
            poprzedniRok = int(rok)-1
            if poprzedniRok >= najstarszyrocznik:
                if slownikZdawalnosc[str(poprzedniRok)] > procenty:
                    print(wojewodztwo + ": " + str(poprzedniRok) + "->" + rok)


def porownanieWojewodztw(pierwszeWojewodztwo, drugieWojewodztwo):
    slownikPierwszego = zdawalnosc(pierwszeWojewodztwo)
    slownikDrugiego = zdawalnosc(drugieWojewodztwo)
    slownikNajlepszychZDwojki = {}

    for rok, procenty in slownikPierwszego.items():
        if slownikDrugiego[rok] > procenty:
            slownikNajlepszychZDwojki[rok] = pierwszeWojewodztwo
        elif slownikDrugiego[rok] < procenty:
            slownikNajlepszychZDwojki[rok] = drugieWojewodztwo
        else:
            slownikNajlepszychZDwojki[rok] = 'Ta sama zdawalnosc'

    return slownikNajlepszychZDwojki

def wyswietlaniePorownaniaWojewodztw(pierwszeWojewodztwo, drugieWojewodztwo):
    slownikDoWypisania = porownanieWojewodztw(pierwszeWojewodztwo, drugieWojewodztwo)
    for rok,wojewodztwo in slownikDoWypisania.items():
        print(rok + "- " + wojewodztwo)

# 1 zadanie
print(sredniaDlaWojewodztwa(2015, "Podlaskie"))

# 2 zadanie
slownikZdawalnosc = zdawalnosc("Pomorskie")
wyswietlanieZdawalnosci(slownikZdawalnosc)

#3 zadanie
wyswietlanieNajlepszeWojewodztwo(2016)

#4 zadanie
wykrywanieRegresji()

#5 zadanie
wyswietlaniePorownaniaWojewodztw('Dolnośląskie','Mazowieckie')
