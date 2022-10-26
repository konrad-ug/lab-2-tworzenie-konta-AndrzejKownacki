import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "93211479876", None)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "93211479876", "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_pesel(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "93211479876", None)
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")

    def test_kod(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "93211479876", "PROM_XYZ")
        if self.assertRegex(pierwsze_konto.kod, r'^PROM_.{3}$', "Zły kupon!"):
            if self.assertRegex(pierwsze_konto.pesel, r'^[7-9][0-9]0[0-9]{8}' or r'^6[1-9]0[0-9]{8}' or r'[0-9][0-9]2[0-9]{8}', "Starość nie radość!"):
                self.saldo += 50
