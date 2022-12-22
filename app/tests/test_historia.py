import unittest

from ..Konto import Konto


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

        self.assertEqual(konto.historia, [200, -300, -400, -1])

    def test_wysyłanie_maila_z_historia(self):
        konto = Konto(self.imie, self.nazwisko,self.pesel, None)
        konto.saldo = 1000
        konto.zaksieguj_przelew_przychodzacy(100)
        smtp_connector = SMTPConnection()
        smtp_connector = MagicMock(return_value = True)
        status = konto.test_wysyłanie_maila_z_historia("konrad@gmail.com", smtp_connector)
        self.assertTrue(status)
        #sprawdzić czy smtp_connector.wyslij została uruchomiona