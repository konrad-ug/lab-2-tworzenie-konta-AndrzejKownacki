import unittest

from parameterized import parameterized
from app.Konto import Konto

class TestKredyt(unittest.TestCase):
    
    @parameterized([
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
        self.assertEqual(czy,przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, saldo)
