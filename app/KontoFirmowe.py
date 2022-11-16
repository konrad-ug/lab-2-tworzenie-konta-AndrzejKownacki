from app.Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.oplata = 5
        self.nip = nip if self.czy_poprawny_nip(nip) else "Niepoprawny NIP!"
        self.historia = []

    def czy_poprawny_nip(self, nip):
        return len(nip) == 10

    def zaciagnij_kredyt_firma(self, kwota):
        czy_przyznany = False
        zus = 1775

        if kwota*2 <= self.saldo and zus in self.historia:
            czy_przyznany = True
        
        if czy_przyznany == True:
            self.saldo = self.saldo + kwota

        return czy_przyznany