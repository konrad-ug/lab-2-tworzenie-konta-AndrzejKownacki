import unittest

from ..KontoFirmowe import KontoFirmowe

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "METPOL"
    nip = "1234562346"

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        self.assertEqual(pierwsze_konto.nazwa_firmy, self.nazwa_firmy, "Nazwa firmy nie została zapisana!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe")
        self.assertEqual(pierwsze_konto.nip, self.nip, "NIP nie została zapisany!")

    def test_zbyt_dlugi_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "9082043723498723")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")

    def test_zbyt_krotki_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "324234")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")