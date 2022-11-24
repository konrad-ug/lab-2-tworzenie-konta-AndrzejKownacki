import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestruKont(unittest.TestCase):

    def setUp(self):
        imie = "Dariusz"
        nazwisko = "Testowy"
        pesel = "93211479876"
        self.konto = Konto(imie, nazwisko, pesel, None)
        RejestrKont.dodaj_konto(self.konto)

    def tearDown(self):
        RejestrKont.lista=[]


    def test_dodawnie_drugiego_konta(self):
        RejestrKont.dodaj_konto(self.konto)
        self.assertEqual(RejestrKont.ile_kont(), 2)

    def test_znajdz_konto(self):
        szukane_konto = RejestrKont.wyszukaj_konto_z_peselem(self.konto.pesel)
        self.assertEqual(szukane_konto, self.konto)

    def test_nie_znajdz_konto(self):
        szukane_konto = RejestrKont.wyszukaj_konto_z_peselem("93200079876")
        self.assertIsNone(szukane_konto)