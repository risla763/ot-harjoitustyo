import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")



    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)


    
    def test_kortin_saldo_alussa(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")


    def test_lataaminen_kasvattaa_oikein(self):
        self.kortti.lataa_rahaa(100)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 11.00 euroa")


    def test_rahan_ottaminen_toimii(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa",)

        kortti = Maksukortti(100)

        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")

    def test_palauttaa_true(self):
        self.assertEqual(self.kortti.syo_maukkaasti(), True)


    def test_palauttaa_false(self):
        self.assertEqual(self.kortti.syo_maukkaasti(20), False)
        
        




        



