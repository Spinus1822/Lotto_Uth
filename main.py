import random

class Gra:
    def __init__(self, nick):
        self.nick = nick
        self.liczby = []
        self.ilosc_liczb = 0
        self.zakres = 0
        self.ilosc_losowan = 0
        self.trafione = []
        self.wylosowane_liczby = []

    def pobierz_dane(self):
        self.ilosc_liczb = int(input("Ile liczb chcesz typować?: "))
        self.zakres = int(input("Podaj maksymalny zakres losowania: "))
        self.ilosc_losowan = int(input("Ile razy chcesz losować?: "))
        if self.ilosc_liczb <= 0 or self.zakres <= 0 or self.ilosc_losowan <= 0:
            raise ValueError("Wszystkie wartości muszą być większe od 0.")
        if self.ilosc_liczb > self.zakres:
            raise ValueError("Ilość typowanych liczb nie może przekraczać maksymalnego zakresu.")

    def generuj_liczby(self):
        for _ in range(self.ilosc_losowan):
            self.wylosowane_liczby.append(random.sample(range(1, self.zakres + 1), self.ilosc_liczb))

    def zgadnij_liczby(self):
        for i in range(self.ilosc_liczb):
            liczba = int(input(f"Podaj liczbę {i+1}: "))
            if liczba < 1 or liczba > self.zakres:
                raise ValueError(f"Liczba musi być w zakresie od 1 do {self.zakres}.")
            self.liczby.append(liczba)

    def sprawdz_wyniki(self):
        print("\nWyniki losowań:")
        for i, losowanie in enumerate(self.wylosowane_liczby, start=1):
            trafione_w_losowaniu = set(losowanie) & set(self.liczby)
            self.trafione.append(trafione_w_losowaniu)
            print(f"Losowanie {i}: Wylosowane liczby: {sorted(losowanie)} - Trafione liczby: {sorted(trafione_w_losowaniu)}")

    def zapisz_wyniki(self):
        with open(f"{self.nick}.txt", "w", encoding='utf-8') as plik:
            plik.write(f"Nick: {self.nick}\n")
            plik.write(f"Ilość liczb: {self.ilosc_liczb}, Zakres: {self.zakres}, Ilość losowań: {self.ilosc_losowan}\n")
            plik.write("Typowane liczby: " + ", ".join(map(str, self.liczby)) + "\n")
            for i, trafione in enumerate(self.trafione, start=1):
                plik.write(f"Losowanie {i}: Trafione liczby: " + ", ".join(map(str, trafione)) + "\n")


def main():
    print("Witaj w naszej grze! Powodzenia!")
    nick = input("Podaj swój nick: ")
    gra = Gra(nick)
    try:
        gra.pobierz_dane()
        gra.generuj_liczby()
        gra.zgadnij_liczby()
        gra.sprawdz_wyniki()
        gra.zapisz_wyniki()
        print("\nGra zakończona. Wyniki zostały zapisane w pliku.")
        print("\nPowodzenia w kolejnych rozgrywkach!!")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
