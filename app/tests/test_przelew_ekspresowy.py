import unittest

from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe

class TestPrzelewEkspresowy(unittest.TestCase):
    nazwa_firmy = "METPOL"
    nip = "1234562346"

    imie = "Dariusz"
    naziwsko = "Testowy"
    pesel = "13467524635"

    def test_nieudany_ekspresowy_konto(self):
        konto = Konto(self.imie, self.naziwsko, self.pesel, None)
        konto.saldo = 200
        konto.przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 200)

    def test_nieudany_ekspresowy_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 200
        konto.przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 200)

    def test_ekspresowy_konto(self):
        konto = Konto(self.imie, self.naziwsko, self.pesel, None)
        konto.saldo = 2000
        konto.przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 2000-300-1)

    def test_ekspresowy_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 2000
        konto.przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 2000-300-5)