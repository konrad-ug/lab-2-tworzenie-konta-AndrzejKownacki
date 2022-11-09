
import unittest

from app.Konto import Konto

class TestKsiegowanie(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Testowy"
    pesel= "13467524635"


    def test_historia(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, None)
        konto.saldo = 3000
        konto.zaksieguj_przelew_przychodzacy(200)
        konto.zaksieguj_przelew_wychodzacy(300)
        konto.przelew_ekspresowy(400)