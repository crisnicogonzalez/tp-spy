import unittest
from src.myFilters.clarinFilter import ClarinFilter

filter = ClarinFilter()

class ClarinFilterTest(unittest.TestCase):
    def test_have_double_bar(self):
        self.assertFalse(filter.isARelativeLink('//clarin.com/revista-enie/'))

    def test_is_a_section(self):
        self.assertFalse(filter.isARelativeLink('/policiales/'))

    def test_have_double_bar_again(self):
        self.assertFalse(filter.isARelativeLink('//www.clarin.com/deportes/agenda-deportiva/'))

    def test_is_a_section_again(self):
        self.assertFalse(filter.isARelativeLink('/politica/'))

    def test_dont_have_double_bar_word(self):
        self.assertTrue(filter.isARelativeLink('/mundo/occidente-desafia-rusia-masiva-expulsion-diplomaticos-21-paises_0_B1xtUlvcG.html'))

    def test_dont_have_double_bar_society(self):
        self.assertTrue(filter.isARelativeLink('/sociedad/detienen-hombre-realizar-amenazas-bomba-submarino-ara-salta_0_B1CjKQwqM.html'))

    
    if __name__ == '__main__':
        unittest.main()