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


class Matura():
    def __init__(self):
        self.calaTabela = pobranieListyZPliku('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv')
        self.aktualnaTabela = self.calaTabela.copy()
        self.terytorium = []
        self.przystapiloZdalo = []
        self.plec = []
        self.rok = []
        self.liczbaOsob = []
        self.iloscEncji = len(self.calaTabela)
        for row in self.calaTabela:
            self.terytorium.append(row[0])
            self.przystapiloZdalo.append(row[1])
            self.plec.append(row[2])
            self.rok.append(row[3])
            self.liczbaOsob.append(row[4])


    def wyswietlanieCalosci(self):
        for i in range(self.iloscEncji):
            print(self.terytorium[i], self.przystapiloZdalo[i], self.plec[i], self.rok[i], self.liczbaOsob[i])

    def sredniaDlaWojewodztwa(self, rok, wojewodztwo):
        sumaUczestnikow = 0
        liczbaUczestnikowDlaRocznika = {}

        for i in range(self.iloscEncji):
            if int(self.rok[i]) <= rok and self.terytorium[i] == wojewodztwo and self.przystapiloZdalo[i] == 'Przystąpiło':
                sumaUczestnikow += int(self.liczbaOsob[i])
                if self.rok[i] in liczbaUczestnikowDlaRocznika.keys():
                    liczba = int(self.liczbaOsob[i])
                    liczbaUczestnikowDlaRocznika[self.rok[i]] += liczba
                else:
                    liczbaUczestnikowDlaRocznika[self.rok[i]] = int(self.liczbaOsob[i])

        print(len(liczbaUczestnikowDlaRocznika))
        sredniaLiczbaUczestnikow = sumaUczestnikow/len(liczbaUczestnikowDlaRocznika)

        return sredniaLiczbaUczestnikow

    def wyswietlanieSredniaDlaWojewodztwa(self, rok, wojewodztwo):
        srednia = self.sredniaDlaWojewodztwa(rok, wojewodztwo)
        print(srednia)

    def zdawalnosc(self, wojewodztwo):
        zdaliNaLata = {}
        uczestniczyliNaLata = {}

        for i in range(self.iloscEncji):
            if self.terytorium[i] == wojewodztwo:
                if self.przystapiloZdalo[i] == 'Przystąpiło':
                    if self.rok[i] in uczestniczyliNaLata.keys():
                        uczestniczyliNaLata[self.rok[i]] += int(self.liczbaOsob[i])
                    else:
                        uczestniczyliNaLata[self.rok[i]] = int(self.liczbaOsob[i])
                elif self.przystapiloZdalo[i] == 'zdało':
                    if self.rok[i] in zdaliNaLata.keys():
                        zdaliNaLata[self.rok[i]] += int(self.liczbaOsob[i])
                    else:
                        zdaliNaLata[self.rok[i]] = int(self.liczbaOsob[i])

        zdawalnoscWojewodztwa = {}

        for klucz, iloscZdanych in zdaliNaLata.items():
            if klucz in uczestniczyliNaLata.keys():
                zdawalnoscWojewodztwa[klucz] = iloscZdanych / uczestniczyliNaLata[klucz] * 100

        return zdawalnoscWojewodztwa

    def wyswietlanieZdawalnosci(self, wojewodztwo):

        zdawalnoscWojewodztwa = self.zdawalnosc(wojewodztwo)

        for klucz, procentZdanych in zdawalnoscWojewodztwa.items():
            print(klucz + ": " + "{:.2f}".format(procentZdanych) + "%")

    def listaWojewodztw(self):
        self.setWojewodztw = set()
        for encja in self.terytorium:
            if encja != 'Polska':
                self.setWojewodztw.add(encja)
        return self.setWojewodztw

    def najlepszeWojewodztwoWRoku(self, rok):
        spisWojewodztw = self.listaWojewodztw()
        najlepszyWynik = 0
        najlepszeWojewodztwo = ''

        for wojewodztwo in spisWojewodztw:
            slownikZdawalnosc = self.zdawalnosc(wojewodztwo)
            if str(rok) in slownikZdawalnosc.keys():
                zdawalnoscDlaWojewodztwa = slownikZdawalnosc[str(rok)]
                if zdawalnoscDlaWojewodztwa > najlepszyWynik:
                    najlepszyWynik = zdawalnoscDlaWojewodztwa
                    najlepszeWojewodztwo = wojewodztwo

        return najlepszeWojewodztwo

    def wyswietlanieNajlepszeWojewodztwo(self, rok):
        print(str(rok) + " - " + self.najlepszeWojewodztwoWRoku(rok))

    def najstarszyRocznik(self):
        najstarszyrocznik = 8000  # Przyjmuję jako dostatecznie oddaloną zmienną
        for rok in self.rok:
            if int(rok) < najstarszyrocznik:
                najstarszyrocznik = int(rok)
        return najstarszyrocznik

    def wykrywanieRegresji(self):
        spisWojewodztw = self.listaWojewodztw()
        najstarszyrocznik = self.najstarszyRocznik()

        regresje = []
        for wojewodztwo in spisWojewodztw:
            slownikZdawalnosc = self.zdawalnosc(wojewodztwo)
            for rok, procenty in slownikZdawalnosc.items():
                poprzedniRok = int(rok) - 1
                if poprzedniRok >= najstarszyrocznik:
                    if slownikZdawalnosc[str(poprzedniRok)] > procenty:
                        regresje.append([wojewodztwo,str(poprzedniRok),rok])
        return regresje

    def wyswietlanieWykrywanieRegresji(self):
        regresje = self.wykrywanieRegresji()
        for elem in regresje:
            print(elem[0]+ ": " + str(elem[1]) + "->" + elem[2])

    def porownanieWojewodztw(self, pierwszeWojewodztwo, drugieWojewodztwo):
        slownikPierwszego = self.zdawalnosc(pierwszeWojewodztwo)
        slownikDrugiego = self.zdawalnosc(drugieWojewodztwo)
        slownikNajlepszychZDwojki = {}

        for rok, procenty in slownikPierwszego.items():
            if slownikDrugiego[rok] < procenty:
                slownikNajlepszychZDwojki[rok] = pierwszeWojewodztwo
            elif slownikDrugiego[rok] > procenty:
                slownikNajlepszychZDwojki[rok] = drugieWojewodztwo
            else:
                slownikNajlepszychZDwojki[rok] = 'Ta sama zdawalnosc'


        return slownikNajlepszychZDwojki

    def wyswietlaniePorownaniaWojewodztw(self, pierwszeWojewodztwo, drugieWojewodztwo):
        slownikDoWypisania = self.porownanieWojewodztw(pierwszeWojewodztwo, drugieWojewodztwo)
        for rok, wojewodztwo in slownikDoWypisania.items():
            print(rok + "- " + wojewodztwo)

    def odswiezenieList(self):
        self.terytorium.clear()
        self.przystapiloZdalo.clear()
        self.plec.clear()
        self.rok.clear()
        self.liczbaOsob.clear()
        self.iloscEncji = len(self.aktualnaTabela)
        for row in self.aktualnaTabela:
            self.terytorium.append(row[0])
            self.przystapiloZdalo.append(row[1])
            self.plec.append(row[2])
            self.rok.append(row[3])
            self.liczbaOsob.append(row[4])

    def sortowaniePlec(self, plecWybrana):

        if plecWybrana == "mężczyźni" or plecWybrana == "kobiety":
            self.aktualnaTabela.clear()
            for i in range(len(self.plec)):
                if self.plec[i] == plecWybrana:
                    self.aktualnaTabela.append(self.calaTabela[i])
            self.odswiezenieList()

        elif plecWybrana == "wszyscy":
            self.aktualnaTabela = self.calaTabela
            self.odswiezenieList()
        else:
            print("Wybrano niepoprawna plec. Dostepne komendy: mężczyźni || kobiety || wszyscy")



