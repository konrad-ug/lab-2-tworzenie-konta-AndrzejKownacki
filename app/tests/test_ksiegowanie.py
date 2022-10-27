import unittest

from ..Konto import Konto

class TestKsiegowanie(unittest.TestCase):
    imie = "Dariusz"
    naziwsko = "Testowy"
    pesel= "13467524635"

    def test_udany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew(200)

        self.assertEqual(konto.saldo, 800, "Udało się wykonać przelew")

    def test_nieudany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 100
        konto.zaksieguj_przelew(200)

        self.assertEqual(konto.saldo, 100, "Za mało środków!")