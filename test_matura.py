import MaturaClass


class Test():

    def pomocnicza_najlepsze(self, matura_najlepsze):
        najlepsze_testowe_rok_procenty = {}
        najlepsze_testowe = {}
        for rok in matura_najlepsze.rok:
            najlepsze_testowe_rok_procenty[str(rok)] = 0
        for rok in matura_najlepsze.rok:
            for elem in matura_najlepsze.listaWojewodztw():
                do_petli = float(najlepsze_testowe_rok_procenty.get(str(rok)))
                if do_petli < matura_najlepsze.zdawalnosc(elem)[rok]:
                    najlepsze_testowe_rok_procenty[str(rok)] = matura_najlepsze.zdawalnosc(elem)[rok]
                    najlepsze_testowe[str(rok)] = elem
        return najlepsze_testowe



    def test_srednia(self):
        matura_srednia = MaturaClass.Matura()
        assert matura_srednia.sredniaDlaWojewodztwa(2013,"Podkarpackie") == 88485 / 4

    def test_zdawalnosc(self):
        matura_zdawalnosc = MaturaClass.Matura()
        assert matura_zdawalnosc.zdawalnosc("Pomorskie")["2015"] == 11687 / 15964 * 100

    def test_plec(self):
        matura_plec = MaturaClass.Matura()
        matura_plec.sortowaniePlec("mężczyźni")
        matura_plec.sortowaniePlec("kobiety")
        matura_plec.sortowaniePlec("wszyscy") #w tym przypadku sprawdzane jest czy operacje na listach nie ingerują w dane
        assert matura_plec.sredniaDlaWojewodztwa(2013, "Podkarpackie") == 88485 / 4
        assert matura_plec.zdawalnosc("Pomorskie")["2015"] == 11687 / 15964 * 100

    def test_najlepsze(self):
        matura_najlepsze = MaturaClass.Matura()
        najlepsze_testowe = self.pomocnicza_najlepsze(matura_najlepsze)
        for rok in matura_najlepsze.rok:
            assert matura_najlepsze.najlepszeWojewodztwoWRoku(rok) == najlepsze_testowe[rok]

    def test_regresja(self):
        matura_regresja = MaturaClass.Matura()
        assert ["Dolnośląskie", "2015", "2016"] not in matura_regresja.wykrywanieRegresji()
        assert ["Lubuskie", "2015", "2016"] not in matura_regresja.wykrywanieRegresji()
        assert ["Opolskie", "2010", "2011"] in matura_regresja.wykrywanieRegresji()

    def test_porownywanie(self):
        matura_porownywanie = MaturaClass.Matura()
        zamarznietySet = frozenset(matura_porownywanie.porownanieWojewodztw("Pomorskie","Świętokrzyskie").items())
        assert ("2010", "Pomorskie") in zamarznietySet
        assert ("2011", "Świętokrzyskie") in zamarznietySet
        assert ("2012", "Pomorskie") in zamarznietySet
        assert ("2013", "Pomorskie") in zamarznietySet