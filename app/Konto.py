class Konto:
    def __init__(self, imie, nazwisko, pesel, kod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel if self.czy_poprawny_pesel(pesel) else "Niepoprawny pesel!"
        self.saldo = 0
        self.oplata = 1
        self.kod = kod

    def czy_poprawny_pesel(self, pesel):
        return len(pesel) == 11

    def czy_poprawny_kod(self, kod):
        return len(kod) == 8 and kod.startswith("PROM_")


    def zaksieguj_przelew(self, kwota):
        if self.saldo >= kwota:
            self.saldo = self.saldo - kwota

    def przelew_ekspresowy(self, kwota):
        saldoPrzed = self.saldo

        self.zaksieguj_przelew(kwota)

        if self.saldo != saldoPrzed:
            self.saldo -= self.oplata