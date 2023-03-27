import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)



    def negatiivinen_lataaminen_ei_muuta(self):
        kortti = Maksukortti(100)
        self.kortti.lataa_rahaa(-100)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")
