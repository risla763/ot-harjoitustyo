import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alustettu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.ota_rahaa(500),  True)
    
    def test_saldo_pysyy_samana_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20000)
        self.assertEqual(self.maksukortti.ota_rahaa(20000), False)

    def test_saldo_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
