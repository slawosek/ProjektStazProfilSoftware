# Przygotowanie środowiska



Do postawienia projektu potrzebny są:
1. Przygotowany projekt w Pythonie z wybranym interpreterem.
2. Aby pobrać moduł pytest należy wpisać w konsoli w swoim IDE:
pip install -U pytest
Chyba że już ten moduł się posiada. W razie problemów z samą biblioteką:
https://docs.pytest.org/en/latest/getting-started.html#getstarted
3. Do folderu projektowego należy przenieść wszystkie pliki z repozytorium.


# Interfejs


Zdefiniowany jest w pliku interfejs.py. Stamtąd należy uruchomić program by wprowadzić komendy.


Dostępne komendy:
- średnia - obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie
- zdawalność  -obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat
- najlepsze - odanie województwa o najlepszej zdawalności w konkretnym roku
- regresja - wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze
- porównanie - porównanie dwóch województw - dla podanych dwóch województw wypisanie, które z województw miało lepszą zdawalność w każdym dostępnym roku


W powyższych instrukcjach potrzebne dane są sprawdzane pod względem poprawności. W kolejnych krokach będzie wyświetlane, co jest potrzebne.

wyjście - zakończenie pracy programu


- wybranie płci - wybranie grupy, która będzie obsługiwana
 - (domyślnie) wszyscy - wszystkie osoby
 - mężczyźni - będą przetwarzane dane tylko mężczyzn
 - kobiety - będą przetwarzane dane tylko kobiet
- lista województw - wyświetla listę dostępnych województw


# Testy

Testy uruchamiane są z poziomu konsoli za pomocą komendy:


pytest


Parametry można zmieniać z poziomu kodu. W razie problemów i wiekszej ilości ustawień ponownie polecam dokumentację pytest:


https://docs.pytest.org/en/latest/getting-started.html#getstarted
