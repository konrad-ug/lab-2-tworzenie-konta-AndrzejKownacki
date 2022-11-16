import unittest

from parameterized import parameterized
from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe

class TestKredyt(unittest.TestCase):
    
    @parameterized.expand([
        ([-100, 100, 100, 100], 500, True, 500),
        ([-100, 100, -100, 100, 1000], 500, True, 500),
        ([100, -100, 100, 1000], 500, True, 500),
        ([-100, 100, 1000], 500, True, 500),
        ([-100, 100, 100], 500, False, 0),
    ])

    def setUp(self):
        imie = "Dariusz"
        nazwisko = "Testowy"
        pesel = "93211479876"
        self.konto = Konto(imie, nazwisko, pesel, None)

    def test_przychodzace_przelewy(self, historia, kwota, oczekiwany_wynik, saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, saldo)

class TestKredytyFirmowe(unittest.TestCase):

    @parameterized.expand([
        (2000, [-100, 1775, 100, 100], 500, True, 2500),
        (2000, [-100, 100, -100, 100, 1000], 500, False, 2000),
        (500, [1775, -100, 100, 1000], 500, False, 500)
    ])

    def setUp(self):
        nazwa_firmy = "METPOL"
        nip = "1234562346"
        self.konto_firmowe = KontoFirmowe(nazwa_firmy, nip)

    def test_przychodzace_przelewy_firmowe(self, saldo_przed, historia, kwota, oczekiwany_wynik, saldo):
        self.konto_firmowe.saldo = saldo_przed
        self.konto_firmowe.historia = historia
        czy_przyznany = self.konto_firmowe.zaciagnij_kredyt_firma(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto_firmowe.saldo, saldo)