import MaturaClass
from enum import Enum

matura = MaturaClass.Matura()

wojewodztwaSet = matura.listaWojewodztw()
przystapiloZdaloSet = {"Przystąpiło", "zdało"}
plecSet = {"mężczyźni", "kobiety", "wszyscy"}
lataSet = {2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018}


class listaRozkazow(Enum):
    SREDNIA = "średnia"
    ZDAWALNOSC = "zdawalność"
    NAJLEPSZE = "najlepsze"
    REGRESJA = "regresja"
    POROWNYWANIE = "porównanie"
    WYJSCIE = "wyjście"
    PLEC = "wybranie płci"
    LISTA_WOJEWODZTWA = "lista województw"


polecenie = input("Wpisz odpowiednią komendę: "
                  "średnia || zdawalność || najlepsze || regresja || porównanie || wyjście || wybranie płci "
                  "|| lista województw")
while polecenie != listaRozkazow.WYJSCIE.value:
    if polecenie == listaRozkazow.SREDNIA.value:
        rok = int(input("Wpisz rok: "))
        if rok in lataSet:
            wojewodztwo = input("Wpisz wojewodztwo: ")
            if wojewodztwo in wojewodztwaSet:
                matura.wyswietlanieSredniaDlaWojewodztwa(rok, wojewodztwo)
            else:
                print("Bledna nazwa wojewodztwa. Powrot do glownego menu.")
        else:
            print("Bledny rok. Powrot do glownego menu.")

    elif polecenie == listaRozkazow.ZDAWALNOSC.value:
        wojewodztwo = input("Wpisz wojewodztwo: ")
        if wojewodztwo in wojewodztwaSet:
            matura.wyswietlanieZdawalnosci(wojewodztwo)
        else:
            print("Bledna nazwa wojewodztwa. Powrot do glownego menu.")

    elif polecenie == listaRozkazow.NAJLEPSZE.value:
        rok = int(input("Wpisz rok: "))
        if rok in lataSet:
            matura.wyswietlanieNajlepszeWojewodztwo(rok)
        else:
            print("Bledna nazwa wojewodztwa. Powrot do glownego menu.")

    elif polecenie == listaRozkazow.REGRESJA.value:
        matura.wyswietlanieWykrywanieRegresji()

    elif polecenie == listaRozkazow.POROWNYWANIE.value:
        pierwszeWojewodztwo = input("Wpisz pierwsze wojewodztwo: ")
        if pierwszeWojewodztwo in wojewodztwaSet:
            drugieWojewodztwo = input("Wpisz drugie wojewodztwo: ")
            if drugieWojewodztwo in wojewodztwaSet:
                matura.wyswietlaniePorownaniaWojewodztw(pierwszeWojewodztwo, drugieWojewodztwo)
            else:
                print("Bledna nazwa wojewodztwa. Powrot do glownego menu.")
        else:
            print("Bledna nazwa wojewodztwa. Powrot do glownego menu.")


    elif polecenie == listaRozkazow.PLEC.value:
        plec = input("Wpisz grupe docelową: mężczyźni || kobiety || wszyscy")
        if plec in plecSet:
            matura.sortowaniePlec(plec)
        else:
            print("Bledna kategoria. Powrot do glownego menu.")

    elif polecenie == listaRozkazow.LISTA_WOJEWODZTWA.value:
        print(wojewodztwaSet)

    elif polecenie not in listaRozkazow.__members__.values():
        print("Niepoprawny rozkaz.")

    polecenie = input("Wpisz odpowiednią komendę: "
                  "średnia || zdawalność || najlepsze || regresja || porównanie || wyjście || wybranie płci"
                      "|| lista wójewodztw")
