class Konto:
    def __init__(self, imie, nazwisko, pesel, kod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel if self.czy_poprawny_pesel(pesel) else "Niepoprawny pesel!"
        self.saldo = 0
        self.oplata = 1

        if self.czy_kod_jest_stringiem(kod):
            if self.czy_poprawny_kod(kod):
                if self.czy_aktualny_kod(pesel):
                    self.kod = kod
                    self.saldo = 50
                else:
                    self.kod = "Nieodpowiedzni rocznik!"
            else:
                self.kod = None
        else:
            self.kod = None

    def czy_poprawny_pesel(self, pesel):
        return len(pesel) == 11

    def czy_kod_jest_stringiem(self, kod):
        return isinstance(kod, str)

    def czy_poprawny_kod(self, kod):
        return len(kod) == 8 and kod.startswith("PROM_")
    
    def czy_aktualny_kod(self, pesel):
        if pesel[0] == '7' or pesel[0] == '8' or pesel[0] == '9':
            return True
        elif pesel[0] == '6':
            if pesel[1] != '0':
                return True
        elif pesel[0] == '0' or pesel[0] == '1':
            if pesel[2] == '2':
                return True
        else:
            return False


    def zaksieguj_przelew(self, kwota):
        if self.saldo >= kwota:
            self.saldo = self.saldo - kwota

    def przelew_ekspresowy(self, kwota):
        saldoPrzed = self.saldo

        self.zaksieguj_przelew(kwota)

        if self.saldo != saldoPrzed:
            self.saldo -= self.oplata