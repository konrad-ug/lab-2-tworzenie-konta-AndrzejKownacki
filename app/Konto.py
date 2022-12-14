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

        self.historia = []

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


    def zaksieguj_przelew_wychodzacy(self, kwota):
        if self.saldo >= kwota:
            self.saldo = self.saldo - kwota
            self.historia.append(-kwota)
        
    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo = self.saldo + kwota
        self.historia.append(kwota)

    def przelew_ekspresowy(self, kwota):
        saldoPrzed = self.saldo

        self.zaksieguj_przelew_wychodzacy(kwota)
        

        if self.saldo != saldoPrzed:
            self.saldo -= self.oplata
            self.historia.append(-self.oplata)

   
    def czy_ostatnie_3_transakcji_byly_wplatami(self):
        l = len(self.historia)
        if l >= 3 and self.historia[l-1] > 0 and self.historia[l-2] > 0 and self.historia[l-3] > 0:
            return True
        else:
            return False

    def czy_suma_ostatnich_5_wieksza(self,kwota):
        l = len(self.historia)
        if l >= 5 and kwota < sum(self.historia[-5:]):
            return True
        else:
            return False

    def zaciagnij_kredyt(self, kwota):
        if self.czy_ostatnie_3_transakcji_byly_wplatami() or self.czy_suma_ostatnich_5_wieksza(kwota):
            self.saldo = self.saldo + kwota
            return True
        else:
            return False
