import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(1000)

        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")
