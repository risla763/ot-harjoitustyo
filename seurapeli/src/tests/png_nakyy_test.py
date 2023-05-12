import unittest
from PIL import ImageGrab

class TestPNG(unittest.TestCase):
    def test_screenshot(self):
        screen = ImageGrab.grab()

        image = screen.crop((0, 0, 100, 100))
        self.assertEqual(image.getcolors(), [(10000, (255, 255, 255))])
