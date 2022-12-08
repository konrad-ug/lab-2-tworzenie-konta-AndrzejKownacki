from app.Konto import Konto
from datetime import date
import requests

#https://wl-api.mf.gov.pl/api/search/nip/8461627563?date=2022-12-08

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.oplata = 5
        self.nip = nip
        self.historia = []

        if len(nip) != 10: 
            self.nip = "Niepoprawny nip"
        else:
            url = "https://wl-api.mf.gov.pl/api/search/nip/"
            data = date.today()
            url = f"{url}{nip}?date={data}"

            get_resp = requests.get(url)
            resp_body = get_resp.json()

            if resp_body['result']['subject'] == None:
                self.nip = "Pranie!"

    def zaciagnij_kredyt_firma(self, kwota):
        czy_przyznany = False
        zus = -1775

        if kwota*2 <= self.saldo and zus in self.historia:
            czy_przyznany = True
        
        if czy_przyznany == True:
            self.saldo = self.saldo + kwota

        return czy_przyznany
