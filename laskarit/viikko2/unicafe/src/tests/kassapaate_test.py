import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10000)

    def test_luotu_kassapaate_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_rahaa_paatteessa_oikean_verran(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaita_syoty_nolla(self):

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisia_syoty_nolla(self):

        self.assertEqual(self.kassapaate.edulliset,0)

    def test_kateisosto_edullinen_vaihtoraha(self):
        rahat = self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(rahat, 60)

    def test_kateisosto_kassa_suurenee(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_maksu_lapi_myytyjen_lounaiden_maara_kasvaa(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(kassapaate.edulliset, 1)

    def test_edullinen_maksu_ei_riittava_vaihtorahat(self):
        kassapaate = Kassapaate()

        rahat = kassapaate.syo_edullisesti_kateisella(60)

        self.assertEqual(rahat, 60)

    def test_kateisosto_kassa_pysyy_samana(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_edullisesti_kateisella(60)
        
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_maksu_ei_lapi_myytyjen_lounaiden_maara_ei_kasva(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_edullisesti_kateisella(40)
        
        self.assertEqual(kassapaate.edulliset, 0)

    #kaikki maukkaalla tähän alle

    def test_kateisosto_maukas_vaihtoraha(self):
        rahat = self.kassapaate.syo_maukkaasti_kateisella(400)
        
        self.assertEqual(rahat, 0)

    def test_kateisosto_kassa_suurenee_maukkaasti(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_maukkaasti_kateisella(400)
        
        self.assertEqual(kassapaate.kassassa_rahaa, 100400)

    def test_maukas_maksu_lapi_myytyjen_lounaiden_maara_kasvaa(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_maukkaasti_kateisella(400)
        
        self.assertEqual(kassapaate.maukkaat, 1)

    def test_maukas_maksu_ei_riittava_vaihtorahat(self):
        kassapaate = Kassapaate()

        rahat = kassapaate.syo_maukkaasti_kateisella(60)

        self.assertEqual(rahat, 60)

    def test_kateisosto_kassa_pysyy_samana_maukas(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_maukkaasti_kateisella(60)
        
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_maukas_maksu_ei_lapi_myytyjen_lounaiden_maara_ei_kasva(self):
        kassapaate = Kassapaate()
        osto = kassapaate.syo_maukkaasti_kateisella(40)
        
        self.assertEqual(kassapaate.maukkaat, 0)

    def test_kortilla_tarpeeksi_rahaa(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    
    def test_kortilla_tarpeeksi_rahaa_lounaat_kasvaa(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(kassapaate.edulliset,  1)

    def test_kortilla_ei_tarpeeksi_rahaa(self):
        kassapaate = Kassapaate()
        maksukortti = Maksukortti(10)
        kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(kassapaate.syo_edullisesti_kortilla(maksukortti), False)


    def test_kortilla_tarpeeksi_rahaa_maukas(self):
        kassapaate = Kassapaate()
        kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    
    def test_kortilla_tarpeeksi_rahaa_lounaat_kasvaa_maukas(self):
        kassapaate = Kassapaate()
        kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(kassapaate.maukkaat,  1)

    def test_kortilla_ei_tarpeeksi_rahaa_maukas(self):
        kassapaate = Kassapaate()
        maksukortti = Maksukortti(10)
        kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,10)

        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti,10), None)

    def test_kortille_lataus_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina(self):

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)