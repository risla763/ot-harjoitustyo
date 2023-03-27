import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)


    def pystyy_ostamaan_edullisen_jos(self):

        kortti = Maksukortti(250)

        kortti.syo_edullisesti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
