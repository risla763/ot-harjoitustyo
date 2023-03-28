import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassappaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_kateis_ostos(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)


    def test_maukas_ostos(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)


    def test_kortti_ostos_edullinen(self):
        self.saldo = 240
        self.kassapaate.syo_edullisesti_kortilla()
        self.assertEqual(self.kassapaate, True)
        self.assertEqual(self.kassapaate, 0)


    def test_kortti_ostos_edullinen_epaonnistuu(self):
        self.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla()
        self.assertEqual(self.kassapaate, False)
        self.assertEqual(self.maksukortti, 100)


    def test_kortti_ostos_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(40000)
        self.assertEqual(self.kassapaate, True)
        self.assertEqual(self.maksukortti, 0)

    def test_kortti_ostos_maukas_epaonnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(10000)
        self.assertEqual(self.kassapaate, False)
        self.assertEqual(self.maksukortti, 100)

    def kortilla_tehty_ostos_ja_kassa(self):
        self.kassapaate.syo_edullisesti_kortilla(24000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def kortilla_tehty_ostos_maukas_ja_kassa(self):
        self.kassapaate.syo_maukkaasti_kortilla()
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def kortille_rahaa_ladattaessa(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.maksukortti, 1100)

    


    


    

    

    

    
        



    






