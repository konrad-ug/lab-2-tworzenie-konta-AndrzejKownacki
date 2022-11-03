import unittest

from app.Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Testowy"
    pesel = "93211479876"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_poprawny_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "93211479876", None)
        self.assertEqual(konto.pesel, konto.pesel)

    def test_niepoprawny_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "1479876", None)
        self.assertEqual(konto.pesel, "Niepoprawny pesel!")

    def test_poprawny_kod(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_XYZ")
        self.assertEqual(konto.saldo, 50)
    
    def test_niepoprawny_kod_dlugosc(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_X")
        self.assertEqual(konto.saldo, 0)

    def test_niepoprawny_kod_foramt(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PRO_MXYZ")
        self.assertEqual(konto.saldo, 0)

    def test_niepoprawny_kod_wiek(self):
        konto = Konto(self.imie, self.nazwisko, "53211479876", "PROM_XYZ") 
        self.assertEqual(konto.saldo, 0)
