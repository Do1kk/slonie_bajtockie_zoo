# Pozwala użyć argumentów wpisanych w terminalu.
import sys


# Definicja metody 1. --------------------------------------------
def metoda_1(kolej_pocz, kolej_kon, wag):
    # Dane początkowe.
    suma1 = 0
    kolej = kolej_pocz[:]
    Inf = 7000
    waga = wag[:]

    # Pętla przestawiania słoni i obliczania sumy.
    while kolej != kolej_kon:
        # Chwilowo najmniejszy słoń i jego dane.
        tmp_slon = min(waga)
        nr_slonia = waga.index(tmp_slon) + 1
        tmp_index = kolej.index(nr_slonia)

        # Słoń który powinien być w miejscu chwilowo najmniejszego słonia.
        nr_slonia_next = kolej_kon[tmp_index]
        tmp_index_next = kolej.index(kolej_kon[tmp_index])

        # Zamiana słoni tylko jeśli nie są one na swoich miejscach.
        if kolej.index(nr_slonia) != kolej_kon.index(nr_slonia):
            kolej[tmp_index] = nr_slonia_next
            kolej[tmp_index_next] = nr_slonia

            # Obliczanie sumy metody 1.
            suma1 += tmp_slon + waga[nr_slonia_next - 1]

        # Ustawienie wartości większej od zakresu, by działała funkcja min().
        waga[nr_slonia_next - 1] = Inf

    return suma1


# Definicja metody 2. ---------------------------------------------
def metoda_2(kolej_pocz, kolej_kon, wag):
    # Dane początkowe.
    suma2 = 0
    kolej = kolej_pocz[:]
    Inf = 7000
    waga = wag[:]

    # Pętla przestawiania słoni i obliczania sumy.
    while kolej != kolej_kon:
        # Chwilowo najmniejszy słoń i jego dane.
        tmp_slon = min(waga)
        nr_slonia = waga.index(tmp_slon) + 1
        tmp_index = kolej.index(nr_slonia)

        nr_slonia_next = kolej_kon[tmp_index]
        tmp_index_next = kolej.index(kolej_kon[tmp_index])

        if kolej.index(nr_slonia) != kolej_kon.index(nr_slonia):
            kolej[tmp_index] = nr_slonia_next
            kolej[tmp_index_next] = nr_slonia

            # Obliczanie sumy metody 2.
            suma2 += tmp_slon + waga[nr_slonia_next - 1]

            if waga[nr_slonia_next - 1] != min(waga):
                # Ustawienie wartości większej od zakresu, by działało  min().
                waga[nr_slonia_next - 1] = Inf

        # Gdy minimum globalne znajdzie swoje miejsce, a pętla się nie skończy.
        else:
            # Minimum lokalne.
            tmp_slon_2 = sorted(waga)[1]
            nr_slonia_2 = waga.index(tmp_slon_2) + 1
            tmp_index_2 = kolej.index(nr_slonia_2)

            # Minimum globalne.
            tmp_slon_next = min(waga)
            nr_slonia_next = waga.index(tmp_slon_next) + 1
            tmp_index_next = kolej.index(nr_slonia_next)

            kolej[tmp_index_2] = nr_slonia_next
            kolej[tmp_index_next] = nr_slonia_2

            # Obliczanie sumy metody 2.
            suma2 += tmp_slon_2 + tmp_slon_next

    return suma2


if __name__ == "__main__":

    # Otwarcie i odczytanie pliku wejściowego.
    with open(sys.argv[1]) as plik:
        linie = plik.readlines()

        # Przypisanie poszczególnych wartości z pliku wejściowego.
        wag = list(map(int, linie[1].split()))
        kolej_pocz = list(map(int, linie[2].split()))
        kolej_kon = list(map(int, linie[3].split()))

    # Wywołanie funkcji.
    suma1 = metoda_1(kolej_pocz, kolej_kon, wag)
    suma2 = metoda_2(kolej_pocz, kolej_kon, wag)

    # Wypisanie prawidłowej sumy.
    if suma1 > suma2:
        print(suma2)
    else:
        print(suma1)
