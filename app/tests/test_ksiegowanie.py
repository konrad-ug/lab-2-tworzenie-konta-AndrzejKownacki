import unittest

from ..Konto import Konto

class TestKsiegowanie(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Testowy"
    pesel= "13467524635"

    def test_udany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzacy(200)

        self.assertEqual(konto.saldo, 800, "Udało się wykonać przelew")

    def test_nieudany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.saldo = 100
        konto.zaksieguj_przelew_wychodzacy(200)

        self.assertEqual(konto.saldo, 100, "Za mało środków!")

    def test_udany_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.saldo = 1000
        konto.zaksieguj_przelew_przychodzacy(200)


        self.assertEqual(konto.saldo, 1200)
