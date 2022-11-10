import unittest

from app.Konto import Konto

class TestKredyt(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Testowy"
    pesel = "93211479876"

    def test_3_przychodzace_przelewy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.historia = [-100, 100, 100, 100]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, 500)

    def test_5_w_historii(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.historia = [100, 100, -100, 100, 1000]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, 500)
    
    def test_4_w_historii(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.historia = [100, -100, 100, 1000]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, 500)

    def test_3_w_historii(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.historia = [-100, 100, 1000]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, 500)

    def test_nieudany_kredyt(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.historia = [-100, 100, 100]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)