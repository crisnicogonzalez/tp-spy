import unittest
from .src.estractor import isARelativeLink


class FilterRelativeLinks(unittest.TestCase):
    def firstCase(self):
        isARelativeLink('//servicios.lanacion.com.ar/horoscopo') == False

    def secondCase(self):
        isARelativeLink('//recetas.lanacion.com.ar/') == False

    def thirdCase(self):
        isARelativeLink('/espectaculos') == False
    
